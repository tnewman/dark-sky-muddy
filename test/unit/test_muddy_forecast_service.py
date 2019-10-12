from dark_sky_muddy.dark_sky_api import DarkSkyAPI
from dark_sky_muddy.forecast import Forecast
from dark_sky_muddy.muddy_forecast_service import MuddyForecastService
from unittest.mock import create_autospec
import pytest


@pytest.fixture()
def dark_sky_api() -> DarkSkyAPI:
    return create_autospec(DarkSkyAPI)


@pytest.fixture()
def muddy_forecast_service(dark_sky_api: DarkSkyAPI) -> MuddyForecastService:
    return MuddyForecastService(dark_sky_api)


def test_returns_true_for_a_muddy_forecast(muddy_forecast_service, dark_sky_api):
    dark_sky_api.get_daily_forecasts.return_value = [Forecast(40, 'rain'), Forecast(30, 'snow'), Forecast(30, None)]

    assert muddy_forecast_service.is_three_day_forecast_muddy() is True

    dark_sky_api.get_daily_forecasts.assert_called_once()


def test_returns_false_for_a_non_muddy_forecast(muddy_forecast_service, dark_sky_api):
    dark_sky_api.get_daily_forecasts.return_value = [Forecast(30, 'rain'), Forecast(30, 'snow'), Forecast(30, None)]

    assert muddy_forecast_service.is_three_day_forecast_muddy() is False

    dark_sky_api.get_daily_forecasts.assert_called_once()


def test_only_uses_three_day_forecast(muddy_forecast_service, dark_sky_api):
    dark_sky_api.get_daily_forecasts.return_value = \
        [Forecast(30, 'rain'), Forecast(30, 'snow'), Forecast(30, None), Forecast(40, 'rain')]

    assert muddy_forecast_service.is_three_day_forecast_muddy() is False

    dark_sky_api.get_daily_forecasts.assert_called_once()
