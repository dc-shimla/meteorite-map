import pandas as pd
from import_data import ImportData

def CleanData():
  met_df = ImportData()  
  print('met_df_1: {0}'.format(met_df.shape))

  # Drop rows with NaN in reclat and/or recling
  met_df = met_df.dropna(axis=0, how="any", subset=['reclat', 'reclong'])
  print('met_df_2: {0}'.format(met_df.shape))

  # Determine no. of rows where latitude and longitude = 0.000000
  zero_df = met_df.loc[(met_df['reclat'] == '0.000000') & (met_df['reclong'] == '0.000000')]
  print('zero_df: {0}'.format(zero_df.shape))

  # Drop rows where latitude and longitude is 0.000000
  met_df = met_df.drop(met_df[(met_df['reclat'] == '0.000000') & (met_df['reclong'] == '0.000000')].index)
  print('met_df_3: {0}'.format(met_df.shape))

  # Convert year column from pandas object to pandas datetime64 datatype
  met_df['year'] =  pd.to_datetime(met_df['year'], format='%Y-%m-%dT%H:%M:%S.%f', errors = 'coerce')

  # Extract year from column (datatype:datetime64) and update column value (new datatype:float64) 
  met_df['year'] = met_df['year'].dt.year

  # Convert float64 to int64 to remove decimal | Fill any NA/NaN for year with 0
  met_df['year'] = met_df['year'].fillna(0).astype('int64')

  print(met_df.dtypes)
  print(met_df.head())
 
  return met_df
