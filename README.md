# Vote
Uses 2020 Census and MIT presidential returns election data to identify majority African-American counties that voted Republican in the 2020 presidential election. Prints out the names of the identified counties, their coordinates (latitude, longitude), and plots them on a map (feature not finished yet). <br /> Note: make sure to change the paths to the datasets in the programs to the corresponding location in your computer.
<br /> Program breakdown: 
- censusReader: reads the data from the Census, and identifies majority African-American counties
- votesReader: reads the MIT election data, and identifies counties that voted Republican in the 2020 election
- plotData: takes the data from censusReader and votesReader to identify the counties that are both majority African-American and Republican, and plots them
<br /> Note: plotData is not yet a finished script- it can identify the counties and geocode them, but cannot yet plot them on a map.
- test: test file used to experiment with plotting on the map (not a functioning or important script- just left it in anyway)

Libraries needed: 
- Pandas (reading data)
- Numpy (reading data)
- Geopandas (plotting data)
- Geopy (geocode data)
- Shapely (create geometry objects to plot data)
- Matplotlib (plot the data)
- censusReader and votesReader (imported into the plotData script to access their outputs)

Caveats:
- Any counties with missing needed data in either the presidental returns or census data can't be used
- plotData script not finished (can't plot yet)

Data links: 
- County Presidential Returns: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/VOQCHQ
- 2020 Census Population Data: https://data.census.gov/cedsci/table?t=Populations%20and%20People&g=0100000US%240500000&tid=DECENNIALPL2020.P1&hidePreview=true
