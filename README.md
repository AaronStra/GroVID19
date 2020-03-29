# GroVID19
GroVID19 helps users identify the least crowded stores in their vicinity. It allows the user to find a 'Grocery Store', a 'Pharmacy' or a 'Bakery', in their chosen vicinity, with the least crowds. Using this tool will allow the user to make an informed decision regarding the probability of availability of goods, and avoid crowded stores, thereby mitigating the spread of COVID-19.

This tool was created during the CodeVsCovid19 Hackathon.
It tackles the issue of panic buying during the COVID-19 pandemic. As people are stocking up on essential items such as canned foods, medicines, toilet paper, etc., supermarkets, pharmacies and similar stores are experiencing a large surge in customers - popularly referred to as 'panic buyers'. GroVID19 aims to "flatten the curve" by helping the customers choose the least crowded stores in their vicinity. This helps in easing the pressure on the supply-chain, while helping prevent large crowds from gathering in a single store.

GroVID19 uses realtime activity data of the stores (if available) along with their average activity data. This is achieved using the Google Maps Places API (https://developers.google.com/places/web-service/intro?hl=de) together with the on top-built Populartimes repository (https://github.com/m-wrzr/populartimes) to use the Places API's popular times feature.

The graph below shows the loads on supermarkets in Singapore on the 29th of March, 2020 at 1 pm. The stores are sorted according to their load and identified with an index ("Store Index"). There was no noticable panic buying going on in Singapore. However, there is a noticable mismatch between the loads of different grocery stores as can be seen by the difference to the red average line.
![Marina Graphic](/images/MarinaBaySands_Data.png)

While crowd surges are not a pressing concern during ordinary times, extra-ordinary times like the current ones require us all to be extra-cautious, and uniting together (in spirit, but not physically!) to prevent the spread of COVID-19.


## How to get started
GroVID19 is implemented as a Flask app. An HTML form is used to get the preferences from the user which are then transferred to the Flask app using the POST method. The app uses the Google Maps Places API along with the PopularTimes repository, to search for the user's location, identify relevant stores in the chosen vicinity, and then identify the least crowded store, according to the chosen specifications.

Please ensure you have python3 installed in your system
In order to use GroVID19 on a Linux system:

+ Install pip for python3 using `sudo apt install python3-pip`
+ Clone/Download this repository
+ Get a Google Maps API key https://developers.google.com/places/web-service/get-api-key
+ Replace the dummy API key in the GroVID19 Python code with your own key
+ Install Flask `pip3 install flask`
+ Install Populartimes from github using `pip3 install --upgrade git+https://github.com/m-wrzr/populartimes`
+ Install NumPy using `pip3 install numpy`
+ Install Pandas using `pip3 install pandas`
+ Open a console and change the directory where you have cloned the GroVID19 repository
+ Enter `export FLASK_APP=grovid19_vp.py`
+ Enter `flask run`
+ Open `home.html`in the browser of your choice
  
 ## Example Call
In the browser window, the user should provide the following preferences:
+ Current location - this parameter will be used to start a google places request and find the location of the user. We choose the first entry in the list of results given by Google.
+ Type of store - the user can choose a category of stores - 'Grocery', 'Pharmacy' and 'Bakery'. The list of stores is directly obtained from the data provided by the Google Place API.
+ Travel distance - this parameter defines a search radius for stores around the location of the user 

After pressing submit the user has to wait some time depending on the number of stores available in the specified radius. The results are filtered according to the availability of activity data and whether they are open at the time of the search.
![RequestScreen](/images/InitialRequest.png)
We include two types of data to find out the least crowded store:
+ Current activity data if available
+ Average activity data at current time
The store with the smallest popularity value is selected.
The result is presented with its name as a link. 
![ResultScreen](/images/Result.png)
By clicking the link the user can see the place on google maps.
![MapsResultScreen](/images/MapsResult.png)

 ## Limitations
 This prototype version of GroVID19 is limited by following following factors:
 
 ### Accuracy of Google Maps activity data
 The reliability of google's popular times data can be questioned as it is done here https://www.linkedin.com/pulse/how-accurate-googles-popular-time-function-m%C3%A9lissa-sanchot. Compared with evaluations based on camera footage the Google results seem to lack major features of the actual activity.
 
 ### Availability of Popular Times Data
Depending on the region, real-time activity data could be scarce. For stores lacking the real-time activity data, GroVID19 uses their average activity data to identify the least crowded stores.
 
 ### Relevance of Search Results
To identify supermarkets and grocery stores GroVID19 uses the predefined location types (https://developers.google.com/places/supported_types). However in the dataset, some companies are mis-tagged as 'Grocery Stores' while they're actually 'Health and Beauty' or other 'Utility' stores. This may cause some results to not be of the best relevance for the user.

## Potential Improvements and Extensions
### Giving the User more Choice
A possible solution to overcome the mis-tagged stores is by providing the users with a short list (3 - 5) of stores, satisfying the user's preferences. Depending on the selections by the user, feedback can be collected to omit mis-tagged stores.

### User Account and Remaining Stocks Value
Running the system on a server with multiple clients, users could create accounts and setup their region of interest.
Then, a database could be created collecting the activity at stores up to the point of request. Based on this, a "remaining stocks" value could be calculated and the user would get recommendations based on this value. A series of unusually high numbers of activity at a store in the morning would indicate a bad choice for the user.

 
 
