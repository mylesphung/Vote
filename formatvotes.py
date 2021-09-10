import pandas as pd
## read data into dataframe
def main():
    data = pd.read_csv("/Users/MP/Documents/GitHub/Vote/Datasets/countypres_2000-2020.csv").dropna()
## for mac use: /Users/MP/Documents/GitHub/Vote/Datasets/countypres_2000-2020.csv
## for windows use: C:/Users/Miles/Documents/GitHub/Vote/Datasets/countypres_2000-2020.csv

    ## sort the data into separate dataframes by year, and reset/replace the index (only using 2020 because the Census data is from 2020)
    data2020 = pd.DataFrame(data[data.year == 2020])
    data2020.reset_index(drop=True, inplace=True)

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
    ## have to make the lists global in order to use in other scripts
    global repFips
    global countyNames
    countyNames = []
    repFips = []
    rowNumber = ()
    for key, value in countyFlipped.items():
        partyVotes = {}
        for x in range(len(value)):
            partyVotes[data2020["party"][value[x]]] = data2020["candidatevotes"][value[x]]
            rowNumber = value[x]
        if max(partyVotes, key=partyVotes.get) == "REPUBLICAN":
            repFips.append(key)
            countyNames.append(str(data2020["county_name"][rowNumber]+", "+data2020["state"][rowNumber]+", USA"))
    print(len(repFips))
    print(len(countyNames))
main()
