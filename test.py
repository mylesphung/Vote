import pandas as pd
from geopy.geocoders import DataBC
from formatvotes import repFips, countyNames

locator = DataBC(user_agent="countygeocoder")
location = locator.geocode("Autauga, Alabama, USA")

print(location.address)
print(location.latitude, location.longitude)

countyLocations = []
for i in range(750):
    latlong = locator.geocode(countyNames[i], timeout=None);
    countyLocations.append(latlong)
