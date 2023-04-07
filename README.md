# Lake Color Analysis

## Data Extraction
Extracted Sentiel-2 SR band data (Red, Green, Blue, NIR, SWIR) of 3 lakes in the Canadian Rocky Monunatin using Climate Engine Research Application.

## Preprocessing
1. Filter out data when RGB values < NIR and SWIR values.
2. Calculate Remote Sensing Reflectance (Rrs) -- divide all values by PI.

## Processing
1. Calculate chromaticity coordinates (only x, y needed) using equations 1-5 found in https://www.mdpi.com/2072-4292/10/2/180. To adjust for one blue band rather than two, use coefficents for Sentiel-2 10m from https://doi.org/10.3390/rs10020180. Equations involve calculating normalize trisimulus values (X,Y,Z) then chromaticity coordinates (x,y,z).
2. Dominant Wavelength -- Manually add values to calculator (https://luminus-cie1931-demo.anvil.app/)

## Resources:
Equations from:
Giardino, Claudia, et al. "The color of water from space: 
A case study for Italian lakes from Sentinel-2." Geospatial 
analyses of Earth Observation (EO) data. IntechOpen, 2019.

Coefficient corrections from:
Van der Woerd, H.J.; Wernand, M.R. Hue-Angle Product for 
Low to Medium Spatial Resolution Optical Satellite Sensors. 
Remote Sens. 2018, 10, 180. https://doi.org/10.3390/rs10020180

