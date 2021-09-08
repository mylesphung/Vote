import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from formatvotes import repFips

locator = Nominatim(user_agent="myGeocoder")
location = locator.geocode("Autauga, Alabama, USA")

print(location.address)
print(location.latitude, location.longitude)

for i in range(len(repFips)):
