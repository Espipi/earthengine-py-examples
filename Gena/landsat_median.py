import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_TOA')\
    .filter(ee.Filter.eq('WRS_PATH', 44))\
    .filter(ee.Filter.eq('WRS_ROW', 34))\
    .filterDate('2014-01-01', '2015-01-01')

median = collection.median()

Map.setCenter(-122.3578, 37.7726, 12)
Map.addLayer(median, {"bands": ['B4', 'B3', 'B2'], "max": 0.3}, 'median')

# Display the map.
Map
