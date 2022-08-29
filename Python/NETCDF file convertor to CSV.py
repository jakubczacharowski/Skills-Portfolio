# Import all key libraries

import xarray as xr
import os

# Set up project parameters

local_storage_directory = r"C:\Users\Jakss\Desktop\MALARIA DATA"
netcdf_dir = local_storage_directory + '/LCMI/'
csv_dir = local_storage_directory + '/csv/'

files_to_convert = local_storage_directory + '/LCMI/'

print(files_to_convert)

# NETCDF Conversion

for filename in os.listdir(files_to_convert):
    ds = xr.open_dataset(files_to_convert + filename)
    df = ds.to_dataframe()
    df.to_csv(csv_dir + filename[:-4] + '.csv')
    print(filename + ' has been processed to .csv')