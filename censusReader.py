import pandas as pd
import numpy as np

def main():
    data = pd.read_csv("C:/Users/Miles/Documents/GitHub/Vote/Datasets/DECENNIALPL2020.P1_data_with_overlays_2021-09-16T090928.csv")
    data2 = data.drop( ## takes out the index and total columns, so it can be used to find max values later
    ["GEO_ID", "NAME", "P1_001N", "P1_002N", "P1_009N", "P1_026N"],
    axis = 1)
    data2List = data2.values.tolist() ## turned the value into a list so I can make the values integers

    global censusFips
    censusFips = []
    for i in range(1, len(data)):
        AAPopulation = (
        int(data["P1_004N"][i]) + ## Black or African American alone
        int(data["P1_011N"][i]) + ## White; Black or African American
        int(data["P1_016N"][i]) + ## Black or African American; American Indian and Alaska Native
        int(data["P1_017N"][i]) + ## Black or African American; Asian
        int(data["P1_018N"][i]) + ## Black or African American; Native Hawaiian and Other Pacific Islander
        int(data["P1_019N"][i]) ## Black or African American; Some Other Race
        )
        rowList = data2List[i]
        for x in range(len(rowList)):
            rowList[x] = int(rowList[x])
        maxVal = max(rowList)
        if AAPopulation >= maxVal:
            fipscode = float(data["GEO_ID"][i][-5:])
            censusFips.append(fipscode)
    print("censusFips: " + str(len(censusFips)))
main()
