import pandas as pd

names = ["USPS", "GEOID", "ALAND", "AWATER", "ALAND_SQMI", "INTPTLAT", "INTPTLONG"]
data = pd.read_csv("C:/Users/Miles/Desktop/2021_Gaz_116CDs_national.txt")
print(data.head())
data.to_csv("C:/Users/Miles/Desktop/testfile.csv")
