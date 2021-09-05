import pandas as pd
## read data into dataframe
data = pd.read_csv("C:/Users/Miles/Documents/GitHub/Vote/Datasets/countypres_2000-2020.csv").dropna()

## sort the data into separate dataframes by year, and reset/replace the index (only using 2020 because the Census data is from 2020)
data2020 = pd.DataFrame(data[data.year == 2020])
data2020.reset_index(drop=True, inplace=True)
print(data2020)

## make a dictionary with all of the fips codes and their corresponding row numbers
countyFips = {}
for x in range(len(data2020)):
    countyFips[x] = data2020["county_fips"][x]

## use a flipped dictionary to match combine row numbers with their corresponding fips code
countyFlipped = {}
for key, value in countyFips.items():
    if value not in countyFlipped:
        countyFlipped[value] = [key]
    else:
        countyFlipped[value].append(key)

## unpack the values of the flipped dictionary, and add the fips of counties with majority republican vote
repFips = []
for key, value in countyFlipped.items():
    partyVotes = {}
    for x in range(len(value)):
        partyVotes[data2020["party"][value[x]]] = data2020["candidatevotes"][value[x]]
    if max(partyVotes, key=partyVotes.get) == "REPUBLICAN":
        repFips.append(key)
print(repFips)
