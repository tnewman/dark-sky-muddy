from dark_sky_muddy.forecast import Forecast
from typing import List
import requests


class DarkSkyAPI:
    def __init__(self, api_key: str):
        """
        Dark Sky API Client.
        :param api_key: A working Dark Sky API Key.
        """
        if not api_key:
            raise ValueError('Dark Sky API key is not defined!')

        self._api_key = api_key

    def get_daily_forecasts(self, latitude: float, longitude: float) -> List[Forecast]:
        """
        Gets daily weather forecasts for the next week.
        :param latitude: Latitude (positive or negative) to retrieve forecasts for.
        :param longitude: Longitude (positive or negative) to retrieve forecasts for.
        :return: Weather forecasts for the next week.
        """
        response = requests.get(f'https://api.darksky.net/forecast/{self._api_key}/{latitude},{longitude}')

        if response.status_code != 200:
            raise Exception(response.text)

        json = response.json()
        daily_forecasts = json['daily']['data']

        return [Forecast(forecast.get('temperatureMax'), forecast.get('precipType')) for forecast in daily_forecasts]
