
#!/usr/bin/env python
"""Display US Counties.

"""

# import datetime
import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

Map.setCenter(-110, 40, 5)
states = ee.FeatureCollection('TIGER/2018/States')
    # .filter(ee.Filter.eq('STUSPS', 'MN'))
# // Turn the strings into numbers
states = states.map(lambda f: f.set('STATEFP', ee.Number.parse(f.get('STATEFP'))))

state_image = ee.Image().float().paint(states, 'STATEFP')

visParams = {
  'palette': ['purple', 'blue', 'green', 'yellow', 'orange', 'red'],
  'min': 0,
  'max': 50,
  'opacity': 0.8,
};

counties = ee.FeatureCollection('TIGER/2016/Counties')  

image = ee.Image().paint(states, 0, 2)
Map.setCenter(-99.844, 37.649, 5)
# Map.addLayer(image, {'palette': 'FF0000'}, 'TIGER/2018/States')
Map.addLayer(image, visParams, 'TIGER/2016/States');
Map.addLayer(ee.Image().paint(counties, 0, 1), {}, 'TIGER/2016/Counties')

# Display the map.
Map
