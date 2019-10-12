from dark_sky_muddy.config import LATITUDE, LONGITUDE
from dark_sky_muddy.dark_sky_api import DarkSkyAPI


class MuddyForecastService:
    def __init__(self, dark_sky_api: DarkSkyAPI):
        self._dark_sky_api = dark_sky_api

    def is_three_day_forecast_muddy(self) -> bool:
        three_day_forecast = self._dark_sky_api.get_daily_forecasts(LATITUDE, LONGITUDE)[0:3]

        for forecast in three_day_forecast:
            if forecast.is_muddy():
                return True

        return False
