# GroVID19
GroVID19 helps users identify the least crowded stores in their vicinity. It allows the user to find a 'Grocery Store', a 'Pharmacy' or a 'Bakery', in their chosen vicinity, with the least crowds. Using this tool will allow the user to make an informed decision regarding the probability of availability of goods, and avoid crowded stores, thereby mitigating the spread of CoVID-19.

This tool was created during the CodeVsCovid19 Hackathon.
It tackles the issue of panic buying during the Covid19 pandemic. As people are stocking up on essential items such as canned foods, medicines, toilet paper, etc., supermarkets, pharmacies and similar stores are experiencing a large surge in customers - popularly referred to as 'panic buyers'. GroVID19 aims to "flatten the curve" by helping the customers choose the least crowded stores in their vicinity. This helps in easing the pressure on the supply-chain, while helping prevent large crowds from gathering in a single store.

GroVID19 uses realtime activity data of the stores (if available) along with their average activity data. This is achieved using the Google Maps Places API (https://developers.google.com/places/web-service/intro?hl=de) together with the on top-built Populartimes repository (https://github.com/m-wrzr/populartimes) to use the Places API's popular times feature.

The graph below shows the loads on supermarkets in Singapore on the 29th of March, 2020 at 1 pm. There was no noticable panic buying going on in Singapore. However, there is a noticable mismatch between the loads of different grocery stores.
![Marina Graphic](/images/MarinaBaySands_Data.png)

While crowd surges are not a pressing concern during ordinary times, extra-ordinary times like the current ones require us all to be extra-cautious, and uniting together (in spirit, but not physically!) to prevent the spread of CoVID-19.


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

### User Account and Remaining Stocks Value
Running the system on a server with multiple clients, users could create accounts and setup their region of interest.
Then, a database could be created collecting the activity at stores up to the point of request. Based on this, a "remaining stocks" value could be calculated and the user would get recommendations based on this value. A series of unusually high numbers of activity at a store in the morning would indicate a bad choice for the user.

 
 
