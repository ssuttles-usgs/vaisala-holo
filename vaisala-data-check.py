import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
# %%
ds = xr.open_dataset('http://geoport.usgs.esipfed.org/thredds/dodsC/sand/usgs/users/dnowacki/wind/gri.nc')
# %%

(ds.time.diff(dim='time')/pd.Timedelta('1s')).plot()
plt.ylim(0,2500)
