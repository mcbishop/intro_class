import requests
import json
from json import load

#Open a JSON result from querying LOCU API for restaurants within 5000 km of Hackbright's location.

json1_file = open('json_string.json')
json1_str = json1_file.read()
parsed_json = json.loads(json1_str)


#assign each level to a variable.
all_venues = (parsed_json['venues'])



def is_sugar(str):
    # if string contains dessert or sweet or upper/lowercase, return True, with one exception for overly inclusive menu
    result = (('dessert' in str.lower()) or ('sweet' in str.lower())) and ('salad' not in str.lower())
   #print "                [", str.encode('ascii', 'ignore'), ']    ', result
    return result



#write a function that, given a subsection object, returns list of strings

all_menu_desserts = []
all_section_desserts = []
all_subsection_desserts = []
all_contents_desserts = []

#search each section and subsection for a name containing 'dessert' variations by calling function is_sugar.
#once found, print name of restaurant, section or subsection name, and its contents.

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



        


