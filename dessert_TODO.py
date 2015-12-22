import requests
import json
#from locu.api import VenueApiClient, MenuItemApiClient

#note: this is incomplete. TODO: more inclusive search query and loop through results

#we will want to post using r = requests.post(url, data=json.dumps(payload)) - json.dumps takes a python dictionary and treats it as JSON
# try to use this code to do different kind of searches - substitute a variable/parameter into any part of this.
# can take venue query parameter

#search for restaurants with category of Bakery or Desserts
bakeries = {"fields":["name","categories"],"venue_queries":[{"location":{"geo": {"$in_lat_lng_radius" : [37.788666,-122.411462,5000]}},"categories":{"str_id":"desserts"},"categories":{"str_id":"desserts"}}],"api_key":"f598a788f6c9151a539a11fa63085cda8ce2884b"}
#string ID: contains bakeries or bakery


#desserts = {fields:["name","menus"],"venue_queries":[{"location":{"locality":"San Francisco"},{"menus":{"$present":true}"}}],"api_key":"f598a788f6c9151a539a11fa63085cda8ce2884b"}

r = requests.post("https://api.locu.com/v2/venue/search/", data=json.dumps(bakeries))

print r.content


# curl -X POST https://api.locu.com/v2/venue/search/ -d '{"fields":["name","menu_items","location","categories","description"],"menu_item_queries":[{"price":{"$ge":15},"name":"steak"}],"venue_queries":[{"location":{"locality":"San Francisco"}}],"api_key":"f598a788f6c9151a539a11fa63085cda8ce2884b"}'
