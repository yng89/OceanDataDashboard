import pandas as pd
from flask import Flask, render_template
import os

app = Flask(__name__, static_folder='/home/yng21001/Yam/sofar/static')

def read_csv_data(csv_filename):
    if os.path.exists(csv_filename):
        df = pd.read_csv(csv_filename)
        return df
    else:
        return None

@app.route('/')
def render_dashboard():
    humidity_data = read_csv_data('/home/yng21001/Yam/sofar/humidity_data.csv')
    peak_period_data = read_csv_data('/home/yng21001/Yam/sofar/peakPeriod_data.csv')
    significant_wave_height_data = read_csv_data('/home/yng21001/Yam/sofar/significantWaveHeight_data.csv')
    timestamp_data = read_csv_data('/home/yng21001/Yam/sofar/timestamp_data.csv')
    location_data = read_csv_data('/home/yng21001/Yam/sofar/location_data.csv')


    last_humidity = humidity_data['data'].iloc[0] if humidity_data is not None else "No data"
    last_peak_period = peak_period_data['waves'].iloc[0] if peak_period_data is not None else "No data"
    last_significant_wave_height = significant_wave_height_data['waves'].iloc[0] if significant_wave_height_data is not None else "No data"
    last_timestamp = timestamp_data['waves'].iloc[0] if timestamp_data is not None else "No data"

    return render_template('dashboard.html',
                           humidity_data=humidity_data.to_dict('records') if humidity_data is not None else None,
                           peak_period_data=peak_period_data.to_dict('records') if peak_period_data is not None else None,
                           significant_wave_height_data=significant_wave_height_data.to_dict('records') if significant_wave_height_data is not None else None,
                           last_humidity=last_humidity,
                           last_peak_period=last_peak_period,
                           last_significant_wave_height=last_significant_wave_height,
                           last_timestamp=last_timestamp,
                           location_data=location_data.to_dict('records') if location_data is not None else None)

if __name__ == '__main__':
    app.run(debug=True)