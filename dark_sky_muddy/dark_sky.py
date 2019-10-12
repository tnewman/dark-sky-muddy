from typing import List, Optional
import requests


class Forecast:
    def __init__(self, temperature: float, precipitation_type: Optional[str]):
        self.temperature = temperature
        self.precipitation_type = precipitation_type


class DarkSkyAPI:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError('Dark Sky API key is not defined!')

        self._api_key = api_key

    def get_daily_forecasts(self, latitude: float, longitude: float) -> List[Forecast]:
        response = requests.get(f'https://api.darksky.net/forecast/{self._api_key}/{latitude},{longitude}')

        if response.status_code != 200:
            raise Exception(response.text)

        json = response.json()
        daily_forecasts = json['daily']['data']

        return [Forecast(forecast.get('temperatureMax'), forecast.get('precipType')) for forecast in daily_forecasts]
