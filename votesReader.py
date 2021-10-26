import pandas as pd
## read data into dataframe
def main():
    data = pd.read_csv("C:/Users/Miles/Documents/GitHub/Vote/Datasets/countypres_2000-2020.csv")
## for mac use: /Users/MP/Documents/GitHub/Vote/Datasets/countypres_2000-2020.csv
## for windows use: C:/Users/Miles/Documents/GitHub/Vote/Datasets/countypres_2000-2020.csv

    ## sort the data into separate dataframes by year, and reset/replace the index (only using 2020 because the Census data is from 2020)
    data2020 = pd.DataFrame(data[data.year == 2020])
    data2020.reset_index(drop=True, inplace=True)

    ## make a dictionary with all of the fips codes and their corresponding row numbers
    countyFips = {}
    for i in range(len(data2020)):
        countyFips[i] = data2020["county_fips"][i]

    ## use a flipped dictionary to match combine row numbers with their corresponding fips code
    countyFlipped = {}
    for key, value in countyFips.items():
        if value not in countyFlipped:
            countyFlipped[value] = [key]
        else:
            countyFlipped[value].append(key)

    ## unpack the values of the flipped dictionary, and add the fips of counties with majority republican vote
    ## have to make the lists global in order to use in other scripts

    global repLocations
    repLocations = {}
    rowNumber = ()
    for key, value in countyFlipped.items():
        partyVotes = {}
        for i in range(len(value)):
            partyVotes[data2020["party"][value[i]]] = data2020["candidatevotes"][value[i]]
            rowNumber = value[i]
        if max(partyVotes, key=partyVotes.get) == "REPUBLICAN":
            repLocations[key] = str(data2020["county_name"][rowNumber]+", "+data2020["state"][rowNumber]+", USA")
    print(len(repLocations))
main()
