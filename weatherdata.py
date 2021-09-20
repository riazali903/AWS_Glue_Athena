import requests
import pandas as pd
from pprint import pprint
from datetime import datetime, timedelta
import time
import math


class WeatherData:
    def __init__(self):
        self.five_days = []
        self.frames = []

    def set_vars(self):
        now = datetime.now()
        for x in range(5):
            d = now - timedelta(days=x)
            d = d.strftime("%Y-%m-%d")
            d1 = time.mktime(datetime.strptime(d,"%Y-%m-%d").timetuple())
            d1 = math.trunc(d1)
            self.five_days.append(d1)

    def parsing(self):
        lon = -0.12570
        lat = 51.50850
        api_key = '12379f060b354d4a1edafa28418ae871'

        for day in self.five_days:
            url = f'https://api.openweathermap.org/data/2.5/onecall/timemachine?' \
                  f'lat={lat}&lon={lon}&dt={day}&appid={api_key}'

            res = requests.get(url).json()
            df = pd.DataFrame(res['hourly'])
            self.frames.append(df)

    def data_wrangling(self):
        df = pd.concat(self.frames)
        df['dt'] = pd.to_datetime(df['dt'], unit='s')
        df.drop(['dew_point', 'uvi', 'clouds', 'wind_deg', 'wind_gust',
                            'weather','rain'], axis=1, inplace=True)
        return df


    # hist_weather = f'https://api.openweathermap.org/data/2.5/onecall/timemachine?' \
    #                f'lat={lat}&lon={lon}&dt={1632092400}&appid={api_key}'


    # res = requests.get(url).json()
    # df = pd.DataFrame(res['hourly'])
    # print(df.head())
    # pprint(res)

    #resultframe = pd.concat(frames)
    #resultframe.pop('rain')

obje = WeatherData()
obje.set_vars()
obje.parsing()
dframe = obje.data_wrangling()