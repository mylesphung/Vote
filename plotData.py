import pandas as pd
import geopandas as gpd
from geopy.geocoders import ArcGIS
from shapely.geometry import Point
from geopandas import GeoDataFrame
from votesReader import repLocations
from censusReader import censusFips

repFips = list(repLocations.keys()) ## find matches between the censusFips and repLocations keys
countyFips = set(censusFips).intersection(repFips)
countyFips = list(countyFips)
print(countyFips)
print(len(countyFips))

countyNames = []
for i in range(len(countyFips)): ## plug the matched fips back into repLocations to get their actual names
    countyNames.append(repLocations.get(countyFips[i]))
print(countyNames)

locator = ArcGIS(user_agent="countygeocoder")
countyLocations = {}
for i in range(len(countyNames)):
    latlong = locator.geocode(countyNames[i], timeout=None);
    countyLocations[latlong.latitude] = latlong.longitude
print(countyLocations)
print(len(countyLocations))

countyData = pd.DataFrame.from_dict(countyLocations)
geometry = [Point(xy) for key, value in countyLocations]
