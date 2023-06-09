# Lake Color Analysis
## Summary
This code was used for a research project for BIO374 (Research in Aquatic Ecology). This project analyzed the relationship between dominate wavelength and turbidity data from 3 lakes in the Canadian Rocky Mountians: Opabin, Peyto, and Zigadenus.

## Data Extraction
Extracted Sentiel-2 SR band data (Red, Green, Blue, NIR, SWIR) of 3 lakes in the Canadian Rocky Monunatin using Climate Engine Research Application.

## Procedure
**Preprocessing**
1. Filter out data when RGB values < NIR and SWIR values.
2. Calculate Remote Sensing Reflectance (Rrs) -- divide all values by PI.

**Processing**
1. Calculate chromaticity coordinates (only x, y needed) using equations 1-5 found in https://www.mdpi.com/2072-4292/10/2/180. To adjust for one blue band rather than two, use coefficents for Sentiel-2 10m from https://doi.org/10.3390/rs10020180. Equations involve calculating normalized trisimulus values (X,Y,Z) then chromaticity coordinates (x,y,z).
2. Dominant Wavelength -- Manually add values to calculator (https://luminus-cie1931-demo.anvil.app/)

## color.py
* Calculates chromaticity coordinates (x, y).
* Input: csv file containing dates and RGB values.
* Output: csv file containg dates and chromaticity coordinates.

This is an example of running the converter with an input file called opabin_band.csv:

```
python3 color.py opabin_band.csvt

```

## plot.py
* Generates multiple graphs to represent data.
* Input: csv file containing dominate wavelength, turbidity, year, Julian date.
* Output: Graph in PNG file format.

This is an example of graphing with input files called Opabin.csv, Peyto.csv, Zigadenus.csv and the corresponding lake names:

```
python3 plot.py Opabin.csv Peyto.csv Zigadenus.csv Opabin Peyto Zigadenus

```


## Resources:
Equations from:
Giardino, Claudia, et al. "The color of water from space: 
A case study for Italian lakes from Sentinel-2." Geospatial 
analyses of Earth Observation (EO) data. IntechOpen, 2019.

Coefficient corrections from:
Van der Woerd, H.J.; Wernand, M.R. Hue-Angle Product for 
Low to Medium Spatial Resolution Optical Satellite Sensors. 
Remote Sens. 2018, 10, 180. https://doi.org/10.3390/rs10020180

