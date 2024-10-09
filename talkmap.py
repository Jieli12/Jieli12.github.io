"""
Author      : Jie Li, Innovision IP Ltd., and School of Mathematics Statistics
				and Actuarial Science, University of Kent.
Date        : 2024-10-09 16:15:23
Last Edited : 2024-10-09 21:21:09
Last Author : Jie Li
File Path   : /Jieli12.github.io/talkmap.py
Description :








Copyright (c) 2024, Jie Li, jl725@kent.ac.uk
All Rights Reserved.
"""

# # Leaflet cluster map of talk locations
#
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
#
# Run this from the _talks/ directory, which contains .md files of all your talks.
# This scrapes the location YAML field from each .md file, geolocates it with
# geopy/Nominatim, and uses the getorg library to output data, HTML,
# and Javascript for a standalone cluster map.
#
# Requires: glob, getorg, geopy

import glob

import getorg
from geopy.geocoders import Nominatim

# Initialize Nominatim with a unique user_agent
geocoder = Nominatim(user_agent="talk_map_name")

# Dictionary to store locations
location_dict = {}

# Iterate over markdown files in the _talks directory
for file in glob.glob("_talks/*.md"):
    with open(file, "r") as f:
        lines = f.read()
        if 'location: "' in lines:
            loc_start = lines.find('location: "') + 11
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            location = lines_trim[:loc_end]

            # Geocode the location and store it in the dictionary
            location_dict[location] = geocoder.geocode(location)
            print(location, "\n", location_dict[location])

m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(
    location_dict, folder_name="talkmap/", hashed_usernames=False
)
