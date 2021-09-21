import pandas as pd
import numpy as np

def main():
    data = pd.read_csv("C:/Users/Miles/Documents/GitHub/Vote/Datasets/DECENNIALPL2020.P1_data_with_overlays_2021-09-16T090928.csv")
    data2 = data.drop(["GEO_ID", "NAME", "P1_001N", "P1_002N"], axis = 1)
    censusFips = []
#    for i in range(len(data)):
#        total = int(data["P1_001N"][i+1]) ## total population
#        data["P1_004N"][i+1] + ## Black or African American alone
#        data["P1_011N"][i+1] + ## White; Black or African American
#        data["P1_017N"][i+1] + ## Black or African American; Asian
#        data["P1_018N"][i+1] + ## Black or African American; Native Hawaiian and Other Pacific Islander
#        data["P1_019N"][i+1] ## Black or African American; Some Other Race
#        )
#        if (int(testedPopulation) >= maxValues[i+1]):
#            fipscode = data["GEO_ID"][i+1][-5:]
#            censusFips.append(fipscode)
#    print(len(censusFips))
#    print(maxValues, i)
    print(data2)
    print(data2.max(axis = 1))
main()
