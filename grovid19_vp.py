import requests, json

import populartimes

import numpy as np

import pandas as pd

from datetime import datetime, timedelta

from flask import Flask, redirect, url_for, request

# Create Flask App
app = Flask(__name__)

# Get Google Places API: https://developers.google.com/places/web-service/get-api-key and replace
MyAPI_key = "xyz"

# URL for request to google place text search to find user address based on what is typed in
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# constant factor used later to calculate the area (longitude, latitude) to scan for stores
alpha = 180/(np.pi*6371000)

# Create Output after the store with the lowest activity was found
@app.route('/success/<store_place_id>')
def success(store_place_id):
    store_name = df.iloc[df[0].idxmin(),1]
    store_gmap_url = "https://www.google.com/maps/place/?q=place_id:" + store_place_id

# General error message
@app.route('/error/<about>')
def error(about):
    return 'there has been an error: %s' % about

# Run Store Search and Selection
@app.route('/grovid19_v1',methods = ['POST', 'GET'])
def grovid19_v1():
    if request.method == 'POST':
        # Import User Input
        user_address = request.form['form_address']
        store_type = request.form['form_store_type']
        radius = request.form['form_radius']
        radius = int(radius)
        
        # Find the google place from the user_address input
        user_address_res = requests.get(url + 'query=' + user_address +    '&key=' + MyAPI_key)

        x = user_address_res.json()
        
        # Get location data from search result
        user_location = x["results"][0]["geometry"]["location"]

        user_latitude = user_location["lat"]
        user_longitude = user_location["lng"]
        
        # Define search area around the user location
        delta = radius*alpha

        p1 = (user_latitude-delta, user_longitude-delta)
        p2 = (user_latitude+delta, user_longitude+delta)
        
        # Depending on the place type - find places with populartimes data within the given radius around the user's location
        if store_type == 'supermarket':
            results = populartimes.get(MyAPI_key,["grocery_or_supermarket"],p1,p2,radius = radius, all_places=False,n_threads = 10)
        
        if store_type == 'pharmacy':
            results = populartimes.get(MyAPI_key,["pharmacy"],p1,p2,radius = radius, all_places=False,n_threads = 10)

        if store_type == 'bakery':
            results = populartimes.get(MyAPI_key,["bakery"],p1,p2,radius = radius, all_places=False,n_threads = 10)
        
        
        # Find out the current time at the user's location (can only be found by a place details request)
        user_location_id = x["results"][0]["reference"]

        url_details = "https://maps.googleapis.com/maps/api/place/details/json?"
        user_location_details_res = requests.get(url_details+"key="+MyAPI_key+"&place_id="+ user_location_id)
        y = user_location_details_res.json()

        utc_offset=y["result"]["utc_offset"]
        time_now = datetime.utcnow()+timedelta(hours=utc_offset/60)
        
        # Create a list of stores with their activity data (current if available, otherwise average at current time)
        # Closed stores (activity=0) are omitted
        store_list = []

        for item in results:
            if "current_popularity" in item:
                store_list.append([item["current_popularity"],item["name"],item["id"]])
            else:
                temp = item["populartimes"][time_now.weekday()]["data"][time_now.hour]
                if temp!=0:
                    store_list.append([temp,item["name"],item["id"]])
        
        # If no Stores are found give out an error
        if len(store_list) == 0:
            #return 'there has been an error: No data available for this choice'
            return redirect(url_for('error',about = 'No data available for this choice'))
        
        # Select the store with the least activity and get its ID and name
        df=pd.DataFrame(store_list)
        min_activity_index = df[0].idxmin()
        store_place_id=df.iloc[df[0].idxmin(),2]
        store_name = df.iloc[df[0].idxmin(),1]
        
        # Create google maps link based of store_place_id
        store_gmap_url = "https://www.google.com/maps/place/?q=place_id:" + store_place_id
        
        #return 'This store has the least crowd: %s' % store_gmap_url
        #return redirect(url_for('success',store_place_id))
        return '<html><body><center><p>This store has the least crowd:</p><p> <h4> <a href = {}> {} </a> </h4> </p></center></body></html>'.format(store_gmap_url,store_name)

    else:
        return redirect(url_for('error',about = 'the form only works using POST method'))

if __name__ == '__main__':
    app.run(debug = True)
