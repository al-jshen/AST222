import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord

hdf = SkyCoord('3h32m39.s', '-27d47m29.1s', frame='icrs')
print(hdf.galactic)
