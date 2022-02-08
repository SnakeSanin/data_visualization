"""
In this project, we take 30 days of earthquake data around the world
and mark them all on a map showing varying degrees of intensity.

"""

import json  # import module for working with json

from plotly.graph_objects import Scattergeo, Layout  # imports the scattergeo chart type and the layout class
from plotly import offline  # import the module offline to display the map

filename = 'data/eq_data_30_day_m1.json'  # save the json file to a variable
with open(filename) as f:  # open our json file and also give it an abbreviated name
    all_eq_data = json.load(f)  # this function converts the data into a format that Python can work with


all_eq_dicts = all_eq_data['features']  # take the data associated with the 'features' key and store it in all_eq_dicts
mags, lons, lats, hover_texts = [], [], [], []  # empty lists for magnitude, longitude, latitude, earthquake places
for eq_dict in all_eq_dicts:  # loop through the dictionary all_eq_dicts
    mag = eq_dict['properties']['mag']  # inside the loop, each earthquake is represented by an eq_dict
    # the magnitude of each earthquake is stored in the 'properties' section of the dictionary with the key 'mag'
    lon = eq_dict['geometry']['coordinates'][0]  # the eq_dict['geometry'] expression accesses a dictionary
    # representing the geometry element earthquake data
    # the second key 'coordinates' retrieves the list of values associated with the key 'coordinates'
    # finally, index 0 asks for the first value in the list of coordinates,
    # corresponding to the longitude of the earthquake
    lat = eq_dict['geometry']['coordinates'][1]  # same as with longitude only the index at the end has changed to 1
    title = eq_dict['properties']['title']  # inside the loop, each earthquake place is represented by an eq_dict
    # the name of each earthquake is stored in the 'properties' section of the dictionary with the key 'title'
    mags.append(mag)  # each magnitude is stored in the mag variable and appended to the mags list
    lons.append(lon)  # each longitude is stored in the lon variable and appended to the lons list
    lats.append(lat)  # each latitude is stored in the lat variable and appended to the lats list
    hover_texts.append(title)  # each earthquake place is stored in the title variable and appended
    # to the hover_texts list

data = [{  # one of the simplest way to define chart data in Plotly
    'type': 'scattergeo',  # chart format
    'lon': lons,  # list with longitude
    'lat': lats,  # list with latitude
    'text': hover_texts,  # list with names of earthquake places
    'marker': {  # use list generator which will generate the correct marker size for each value in the list
        'size': [5*mag for mag in mags],  # we want the size of the marker to match the magnitude of each earthquake,
        # but since it can be very small, we multiply it by 5.
        'color': mags,  # 'color' setting tells Plotly what value should be used to locate each marker on the color bar
        'colorscale': 'Viridis',  # 'colorscale' setting tells Plotly what range of colors should be used
        'reversescale': True,  # flipping our color scheme in the opposite direction
        'colorbar': {'title': 'Magnitude'}  # the color bar is given the title 'Magnitude'
    }
}]
my_layout = Layout(title=all_eq_data['metadata']['title'])  # here we put the title of our entire map, we refer
# to our data so that in case of data change, the title is automatically pulled out of the data


fig = {'data': data, 'layout': my_layout}  # create a dictionary named fig containing data and layout
offline.plot(fig, filename='global_earthquakes.html')  # fig is passed to the plot()
# function with a meaningful filename to output the data
