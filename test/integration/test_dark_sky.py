from dark_sky_muddy.config import DARK_SKY_API_KEY, LATITUDE, LONGITUDE
from dark_sky_muddy.dark_sky import DarkSkyAPI
import pytest


@pytest.fixture()
def dark_sky_api() -> DarkSkyAPI:
    return DarkSkyAPI(DARK_SKY_API_KEY)


def test_get_daily_forecasts(dark_sky_api: DarkSkyAPI):
    forecasts = dark_sky_api.get_daily_forecasts(LATITUDE, LONGITUDE)

    assert 7 <= len(forecasts)
    assert forecasts[0].temperature is not None
    assert forecasts[0].precipitation_type is not None


def test_constructor_rejects_missing_api_key():
    with pytest.raises(Exception):
        # noinspection PyTypeChecker
        DarkSkyAPI(api_key=None)
