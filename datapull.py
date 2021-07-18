import requests
import numpy as np
import pandas as pd
url = "https://api.census.gov/data/2019/acs/acs5?"
querystring = (
    "get=NAME,B02015_009E,B02015_009M"+
    "&for=state:*"+
    "&key=1a298f4e88c8eae54083a9336f71879a5b4b4241"
)
response = requests.get(url+querystring)
print(response.status_code)
d = response.json()
data = np.asarray(d)
print(data)
