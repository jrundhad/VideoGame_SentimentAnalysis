# importing the requests library
import requests
from datetime import datetime
  
# api-endpoint
URL = "http://store.steampowered.com/appreviews/230410?json=1?"
cursor = "*"

  
# defining a params dict for the parameters to be sent to the API
while(cursor != None):
    PARAMS = {
        'filter':"updated",
        'language': "english",
        'review_type' :"all",
        'cursor' : cursor,
        'purchase_type': "",
        'num_per_page': "100"
        }
    
    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)
    
    # extracting data in json format
    data = r.json()
    reviews = data["reviews"]
    cursor = data["cursor"]
    for review in reviews:
        print(datetime.fromtimestamp(review['timestamp_updated']))
  