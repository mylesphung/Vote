import pandas as pd
import geopandas as gpd
from geopy.geocoders import DataBC
from shapely.geometry import Point
from geopandas import GeoDataFrame
from formatvotes import repFips, countyNames

locator = DataBC(user_agent="countygeocoder")
location = locator.geocode("Autauga, Alabama, USA")

print(location.address)
print(location.latitude, location.longitude)

countyLocations = {}
for i in range(30):
    latlong = locator.geocode(countyNames[i], timeout=None);
    countyLocations[latlong.latitude] = latlong.longitude

countyData = pd.DataFrame.from_dict(countyLocations)
geometry = [Point(xy) for key, value in countyLocations]
