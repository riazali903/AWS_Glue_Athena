import requests,json,time,math
import pandas as pd
from pprint import pprint
from datetime import datetime, timedelta



class WeatherData:

    def __init__(self):
        pass
        #self.five_days = []
        #self.frames = []

    def set_vars(self):
        print('set_vars working')

        print('set_var worked')

    def parsing(self):
        print('into parser')
        now = datetime.now()

        day = now.strftime("%Y-%m-%d")
        day = time.mktime(datetime.strptime(day, "%Y-%m-%d").timetuple())
        day = math.trunc(day)
        lon = -0.12570
        lat = 51.50850
        api_key = '7d2751fa65dfe0f3c12e2f2728ca2cef'
        url = f'https://api.openweathermap.org/data/2.5/onecall/timemachine?' \
              f'lat={lat}&lon={lon}&dt={day}&appid={api_key}'

        res = requests.get(url).json()
        return pd.DataFrame(res['hourly'])

    def data_wrangling(self):
        df = self.parsing()
        df['dt'] = pd.to_datetime(df['dt'], unit='s')
        df.drop(['dew_point', 'uvi', 'clouds', 'wind_deg', 'wind_gust',
                'weather',], axis=1, inplace=True)
        df.set_index('dt', inplace=True)
        df.to_json('weather.json', orient='index', indent=2,
                   date_format='iso', date_unit='s')
        return df


obje = WeatherData()
obje.set_vars()
dframe = obje.data_wrangling()



