# importing the requests library
import requests
import csv
from datetime import datetime
  
# api-endpoint
URL = "http://store.steampowered.com/appreviews/230410?json=1?"
cursor = "*"

header = ['date', 'reviews', 'voted_up']
with open('reviews.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
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
        if data["query_summary"]["num_reviews"] ==0:
            break;
        for review in reviews:
            print(datetime.fromtimestamp(review['timestamp_updated']))
            header = [datetime.fromtimestamp(review['timestamp_updated']), review['review'], review['voted_up']]
            writer.writerow(header)      
  