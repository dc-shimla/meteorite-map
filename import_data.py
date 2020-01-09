import pandas as pd
import requests

def ImportData():
    
    # Import NASA meteor data json
    data_json = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json?$limit=50000')

    # Convert json to python list
    data_list = data_json.json()

    # Convert python list to pandas dataframe
    df = pd.DataFrame(data_list)
    
    print(df.dtypes)
    print('df: {0}'.format(df.shape))
    
    return(df)