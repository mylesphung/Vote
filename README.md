# Vote
Uses 2020 Census and MIT election data to identify majority African-American counties that voted Republican in the 2020 presidential election. 
Program breakdown: 
- censusReader: reads the data from the Census, and identifies majority African-American counties
- votesReader: reads the MIT election data, and identifies counties that voted Republican in the 2020 election


Libraries needed: 
- Pandas (reading data)
- Numpy (reading data)
- Geopandas (plotting data)
- Geopy (geocode data)
- Shapely (create geometry objects to plot data)

Data links: 
- County Presidential Returns: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/VOQCHQ
- 2020 Census Population Data: https://data.census.gov/cedsci/table?t=Populations%20and%20People&g=0100000US%240500000&tid=DECENNIALPL2020.P1&hidePreview=true
