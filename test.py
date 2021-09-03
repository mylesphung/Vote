import pandas as pd
data = pd.read_csv("C:/Users/Miles/Documents/GitHub/Vote/Datasets/countypres_2000-2020.csv").dropna()
print(data)
dataLength = len(data)

dataOne = pd.DataFrame()
data2004 = pd.DataFrame()
data2008 = pd.DataFrame()
data2012 = pd.DataFrame()
data2016 = pd.DataFrame()
data2020 = pd.DataFrame()
for x in range(dataLength):
    if data["year"][x] == 2000:
        dataOne.append(data["county_fips"][x])
    if data["year"][x] == 2004:
        data2004.append(data["county_fips", "party", "candidatevotes"][x])
if data["year"][x] == 2008:
    data2008.append(data["county_fips", "party", "candidatevotes"][x])
if data["year"][x] == 2012:
    data2012.append(data["county_fips", "party", "candidatevotes"][x])
if data["year"][x] == 2016:
    data2016.append(data["county_fips", "party", "candidatevotes"][x])
if data["year"][x] == 2020:
    data2020.append(data["county_fips", "party", "candidatevotes"][x])
