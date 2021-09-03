import pandas as pd
import os

## change this path to the path of your county votes file
data = pd.read_csv("C:/Users/Miles/Documents/GitHub/Vote/Datasets/county-normal-vote-pres-2008-2016.csv").dropna()
print(data.head())

## make lists for county fips and states
countyfips = []
states = []
## run through data and add values to lists if the rep.normal is >.5
for x in range(len(data)+1):
    try:
        if data["rep.normal"][x] > .5:
            fip = data["res_countyfips"][x]
            fip = fip[9:]
            countyfips.append(fip)

            state = data["res_state"][x]
            states.append(state)
        else:
            pass
    except KeyError:
        pass

## make list for the combined state and fip codes
county = []
## combine state and fip codes
for x in range(len(states)):
    temp = states[x]+str(countyfips[x])
    county.append(temp)
county.sort()
print(len(county))
print("hi")

## change this path to the path of your county fips tool file
fipSheet = pd.read_csv("C:/Users/Miles/Documents/GitHub/Vote/Datasets/countyfipstool20190120.csv").dropna()
## make a dictionary using the fip codes and their respective counties
fipDict = {}
for x in range(len(fipSheet)):
    fip = fipSheet["cfips"][x]
    state = fipSheet["sab"][x]
    temp = state+str(fip)
    fipDict[temp]=fipSheet["cname"][x]

## iterate over the county list, and compare it with the fipDict to get the county names
countyList = []
for x in range(len(county)):
    try:
        temp = fipDict[county[x]]
        countyList.append(temp.upper())
    except KeyError:
        pass
print("hi")

## format all of the counties into "name + county", if they aren't already
for x in range(len(countyList)):
    for y in (("CTY.", "County"),
            ("CNTY.", "County"),
            ("CY", "County"),
            ("C.", "County"),
            ("CNTY", "County"),
            ("CY.", "County"),
            ("CTY", "County"),
            (".", "")):
        temp = countyList[x].replace(*y)
        countyList[x] = temp
## double check that they are all in the correct format
    if "COUNTY" in countyList[x].upper():
        countyList[x] = countyList[x].capitalize()
    else:
        countyList[x] = (countyList[x] + " county").capitalize()
print(len(countyList))
