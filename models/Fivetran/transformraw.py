import pandas as pd
import json

def model(dbt, session):
    # Load the source data
    raw_json_df = dbt.source("source_1", "raw").to_pandas()

    json_str = raw_json_df['DATA'].iloc[0]
   
    json_data = json.loads(json_str)
    data_records = json_data['data']

    # Each record is a list; we convert it into a DataFrame
    df = pd.DataFrame(data_records)
    column_names = [col['name'] for col in json_data['meta']['view']['columns']]
    df.columns = column_names  # Set the DataFrame column names

    # Perform any additional transformations if necessary

    return df