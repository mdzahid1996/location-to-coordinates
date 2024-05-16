import requests
import json
import os
import time

# Define the Google Maps API key
api_key = "YOUR_GOOGLE_MAPS_API_KEY"

# Example JSON array data
json_data = [
    # Add your JSON locations data here
]

# Function to get latitude and longitude using Google Maps Geocoding API
def get_lat_long(address, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        return None, None

# List to store the HTML list items
location_list_items = []

# Iterate through the JSON data and generate the HTML list items
for index, item in enumerate(json_data):
    address = item["Address"]
    location_name = item["LOCATION"]
    latitude, longitude = get_lat_long(address, api_key)
    print (address,location_name, latitude, longitude)
    if latitude is not None and longitude is not None:
        list_item = f'<li data-address="{address}" data-longitude="{longitude:.4f}" data-latitude="{latitude:.4f}" data-value="{index + 1}">{location_name} ({address})</li>'
        location_list_items.append(list_item)
    else:
        print(f"Could not geocode address: {address}")
    
    # Add a 2-second delay between each request
    time.sleep(2)

# Define the path to the Downloads folder
downloads_folder = os.path.expanduser('~/Downloads/')
output_file_path = os.path.join(downloads_folder, 'location_list.html')

# Write the generated list items to an HTML file
with open(output_file_path, 'w') as file:
    for item in location_list_items:
        file.write(f'{item}\n')

# Print the first few generated list items as a sample
for item in location_list_items[:5]:
    print(item)
