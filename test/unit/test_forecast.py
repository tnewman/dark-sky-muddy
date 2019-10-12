from dark_sky_muddy.forecast import Forecast


def test_is_muddy_with_rain_above_freezing():
    assert Forecast(40, 'rain').is_muddy() is True


def test_is_not_muddy_with_no_rain_above_freezing():
    assert Forecast(40, None).is_muddy() is False


def test_is_not_muddy_with_rain_below_freezing():
    assert Forecast(30, 'rain').is_muddy() is False


def test_is_not_muddy_with_no_rain_below_freezing():
    assert Forecast(30, None).is_muddy() is False


def test_is_not_muddy_with_other_precip_type():
    assert Forecast(30, 'snow').is_muddy() is False
