import requests
import json
import pandas as pd
from datetime import datetime, timedelta
import time
import os

spotter_id = "SPOT-30344R" 
api_token = "59fa53cce25ab403507cb17bf1c26c"
api_url = f"https://api.sofarocean.com/api/latest-data?spotterId={spotter_id}"

def fetch_and_update_csv(data_key, csv_filename, value_key):
    response = requests.get(api_url, headers={"token": api_token})
    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            if data_key == 'data':
                current_time = data['track'][0]['timestamp']
                value_to_append = data[value_key]
            else:
                current_time = data[data_key][0]['timestamp']
                value_to_append = next((d[value_key] for d in data[data_key]), None)

            if value_to_append is not None:
                if os.path.exists(csv_filename):
                    df = pd.read_csv(csv_filename)
                    df = df.append({'Time': current_time, data_key: value_to_append}, ignore_index=True)
                else:
                    df = pd.DataFrame([{'Time': current_time, data_key: value_to_append}])

                df['Time'] = pd.to_datetime(df['Time'])
                df = df.sort_values(by='Time', ascending=False).reset_index(drop=True)
                df = df.head(120) 

                df.to_csv(csv_filename, index=False)
                print(f"CSV updated for {data_key} at {current_time}")
            else:
                print(f"{data_key} value not found in the API response.")
        else:
            print("No data found in the API response.")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

while True:
    fetch_and_update_csv('waves', 'peakPeriod_data.csv', 'peakPeriod')
    fetch_and_update_csv('waves', 'timestamp_data.csv', 'timestamp')
    fetch_and_update_csv('waves', 'significantWaveHeight_data.csv', 'significantWaveHeight')
    fetch_and_update_csv('data', 'humidity_data.csv', 'humidity')
    time.sleep(3600)