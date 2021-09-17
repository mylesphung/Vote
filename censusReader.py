import pandas as pd

def main():
    data = pd.read_csv("C:/Users/Miles/Documents/GitHub/Vote/Datasets/DECENNIALPL2020.P1_data_with_overlays_2021-09-16T090928.csv")
    censusFips = []
    for i in range(len(data)):
        total = data["!!Total:"][i]
        africanAmerican = data["!!Total:!!Population of one race:!!Black or African American alone"][i]
        code = data["GEO_ID"][i][-5:]
        censusFips.append(code)
    print(censusFips)
main()
