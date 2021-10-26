import pandas as pd
import geopandas as gpd
from geopy.geocoders import Nominatim
from shapely.geometry import Point
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
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

city = []
state = []
country = []
for i in range(len(countyNames)):
    partitioned = countyNames[i].split(",")
    city.append(partitioned[0])
    state.append(partitioned[1])
    country.append("USA")
print(city)
print(state)
print(country)

locator = Nominatim(user_agent="countygeocoder")

lat = []
long = []
for i in range(len(countyNames)):
    latlong = locator.geocode(countyNames[i], timeout=None);
    lat.append(latlong.latitude)
    long.append(latlong.longitude)
##print(countyLocations)
##print(len(countyLocations))
countyData = pd.DataFrame({"City": city, "State": state, "Country": country, "Latitude": lat, "Longitude": long})
print(countyData)
gdf = gpd.GeoDataFrame(countyData,
geometry = gpd.points_from_xy(countyData.Latitude, countyData.Longitude))
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
df = gpd.overlay(gdf, world, how="symmetric_difference")
df.plot()
plt.show()
