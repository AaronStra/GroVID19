# GroVID19
This tool was created in the framework of the CodeVsCovid19 Hackathon.
We tackeld the issue of panic buying during the Covid19 pandemic in early 2020. As people started stocking toilet paper and other basic goods an even distribution of shoppers to grocery stores can help to alleviate temporary shortages. We hope to achieve this by pointing users to stores in their surroundings that are the least crowded. We use realtime activity data if available and average activity data to complement. We used the Google Maps Places API (https://developers.google.com/places/web-service/intro?hl=de) together with the on top built Populartimes library (https://github.com/m-wrzr/populartimes) to use the first's popular times feature.

The graph below shows the loads on supermarkets in Singapore on the 29th of March, 2020 at 1 pm. There was no noticable panic buying going on in Singapore. However, there is a noticable mismatch between the loads of different grocery stores.
![Marina Graphic](/images/MarinaBaySands_Data.png)
For customers this is not too big of a problem besides the crowd itself and longer queuing times. However, in times of panic buying this could mean that people heading to crowded stores won't find basic goods anymore.

Panic buying seems to be an acute situation. We made the assumption that in such a case the activity at grocery stores may be skewed towards earlier hours in the day, but a relatively low loaded store will also be less loaded than others in times of shortage.

## How to get started
+ Clone/Download this repository
+ Get a Google Maps API key https://developers.google.com/places/web-service/get-api-key
+ Replace the dummy API key in the GroVID19 Python code with your own key
+ Install Populartimes from github using `pip install --upgrade git+https://github.com/m-wrzr/populartimes`
+ Install NumPy using `pip install numpy`
+ Install Flask `pip install flask`
+ Open a console and change the directory to the GroVID19 directory
+ Enter `export FLASK_APP=grovid19_v2.py`
+ Enter `flask run`
+ Open `home.html`in the browser of your choice
  
 ## Example Call
After launch the user can type in the following information:
+ Current location - this parameter will be used to start a google places request and find the location of the user. We choose the first entry in the list of results given by google.
+ Type of store - right now the options are Gorcery/Supermarket, Pharmacy and Bakery. This input is fed directly to the google places request according to the place type identified by google.
+ Travel distance - this parameter defines a search radius for shops around the location of the user and is a parameter of the Populartimes library. 

After pressing submit the user has to wait some time depending on the number of stores available in the specified radius. The results are filtered according to the availability of popular times data and if they are currently open.
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
 The usefulness of the current version our tool depends on the following factors:
 
 ### Accuracy of Google Maps activity data
 The reliability of google's popular times data can be questioned as it is done here https://www.linkedin.com/pulse/how-accurate-googles-popular-time-function-m%C3%A9lissa-sanchot. Compared with evaluations based on camera footage the Google results seem to lack major features of the actual activity.
 
 ### Availability of Popular Times Data
Depending on the region, popular times data could be scarce. We already added the average activity to our evaluation as current popularity data is even harder to get from nearby places.
 
 ### Relevance of Search Results
To identify supermarkets and grocery stores we use the predefined location types (https://developers.google.com/places/supported_types). However, as some companies define themselfes as grocery stores while they're actually selling health and beauty products or are actually petrol stations the top result could be useless for the user.

## Potential Improvements and Extensions
### Giving the User more Choice
Alternatively to showing the least crowded store it would be possible to present a ranking of stores. This way the user can adjust the selection scheme to his needs. Also useless picks like discussed recently would be omitted by the user.

### Gather and Evaluate Data independently of Google


 
 
