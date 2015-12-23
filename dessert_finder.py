import requests
import json
from json import load


#search for all restaurants within 5000 km of Hackbright location
desserts = {"fields":["name","menus"],"venue_queries":[{"location":{"geo":{"$in_lat_lng_radius" :[37.788666,-122.411462,5000]}}}],"api_key":"f598a788f6c9151a539a11fa63085cda8ce2884b"}

#testing: search for all restaurants with category of bakeries/dessert
#bakeries = {"fields":["name","categories"],"venue_queries":[{"location":{"geo": {"$in_lat_lng_radius" : [37.788666,-122.411462,5000]}},"categories":{"str_id":"desserts"},"categories":{"str_id":"bakeries"}}],"api_key":"f598a788f6c9151a539a11fa63085cda8ce2884b"}

r = requests.post("https://api.locu.com/v2/venue/search/", data=json.dumps(desserts))
#b = requests.post("https://api.locu.com/v2/venue/search/", data=json.dumps(bakeries))

#print b.content
#print r.content

# create a file for JSON results
# out_file = open("test.json","w")


# #put results into file

# json.dump(r,out_file)    

# Open a JSON result from querying LOCU api for restaurants.
#json1_file = open('json_string.json')
#change fle to giant string
#json1_str = json1_file.read()
#json.loads gives me a python dictionary
#parsed_json = json.loads(json1_str)
parsed_json = json.loads(r.content)


#assign each level to a variable.
all_venues = (parsed_json['venues'])


def is_sugar(str):
    # if string contains dessert or sweet or upper/lowercase, return True, with one exception for overly inclusive menu
    result = (('dessert' in str.lower()) or ('sweet' in str.lower())) and ('salad' not in str.lower() and ('wine' not in str.lower()))
   #print "                [", str.encode('ascii', 'ignore'), ']    ', result
    return result



#write a function that, given a subsection object, returns list of strings

all_menu_desserts = []
all_section_desserts = []
all_subsection_desserts = []
all_contents_desserts = []


for venue in all_venues:
    if 'menus' in venue:
        all_menus = venue['menus']
        for menu in all_menus:
            if is_sugar(menu['menu_name']):
                print '    ', menu['menu_name'].encode('ascii', 'ignore')
                all_menu_desserts.append(menu)  # no results - data doesn't include menus named 'Dessert'

            if 'sections' in menu:
                all_sections = menu['sections']
                for section in all_sections:
                    if is_sugar(section['section_name']):   #if section name includes sugar
                        print venue['name'] #todo: add address, phone number, website, hours to query and results
                        all_section_desserts.append(section)  
                        print '        ', section['section_name'].encode('ascii', 'ignore') 
                        if 'subsections' in section:  #print subsection contents of sugar sections
                            all_subsections = section['subsections']
                            for subsection in all_subsections:
                                all_subsection_desserts.append(subsection) 
                                print '        ', subsection['subsection_name'].encode('ascii', 'ignore')
                                if 'contents' in subsection:
                                    all_contents = subsection['contents']
                                    for content in all_contents:
                                        if 'name' in content:
                                       #   print content
                                            print'                ', content['name'].encode('ascii', 'ignore')
                                            if 'description' in content:   
                                                print'                ', content['description'].encode('ascii', 'ignore')   
                                            if 'price' in content:
                                                print'                ', content['price'].encode('ascii', 'ignore')                       
                                        all_contents_desserts.append(content)

                    else:  #even if the section name isn't  Dessert, check the subsection name for Dessert
                        if 'subsections' in section:  #if section contains subsections
                            all_subsections = section['subsections']  #if so, add it to all_subsections
                            for subsection in all_subsections:
                                if is_sugar(subsection['subsection_name']):  #check to see if subsection name contains dessert
                                    all_subsection_desserts.append(subsection)
                                    print '        ', subsection['subsection_name'].encode('ascii', 'ignore')
                                    if 'contents' in subsection:
                                        all_contents = subsection['contents']
                                        for content in all_contents:
                                            if 'name' in content:
                                                print'                ', content['name'].encode('ascii', 'ignore')
                                                if 'description' in content:
                                                    print'                ', content['description'].encode('ascii', 'ignore')
                                                if 'price' in content:
                                                    print'                ', content['price'].encode('ascii', 'ignore')
                                            all_contents_desserts.append(content)

# # print all_menu_desserts
# # print all_section_desserts
# print all_subsection_desserts
# print all_contents_desserts

        





        


