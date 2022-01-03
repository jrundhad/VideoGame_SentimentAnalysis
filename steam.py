
# importing the requests library
import requests
  
# api-endpoint
URL = "http://store.steampowered.com/appreviews/230410?json=1?"
  

  
# defining a params dict for the parameters to be sent to the API
PARAMS = {
    'filter':"recent",
    'language': "english",
    'review_type' :"all",
    'purchase_type': "",
    'num_per_page': "1"
    }
  
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
  
# extracting data in json format
data = r.json()
reviews = data["reviews"]
  
# extracting latitude, longitude and formatted address 
# of the first matching location
for review in reviews:
    print(review['review'])
  