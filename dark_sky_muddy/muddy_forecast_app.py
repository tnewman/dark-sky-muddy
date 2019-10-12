from dark_sky_muddy.config import DARK_SKY_API_KEY
from dark_sky_muddy.dark_sky_api import DarkSkyAPI
from dark_sky_muddy.muddy_forecast_service import MuddyForecastService
from flask import Flask, render_template


app = Flask(__name__)
dark_sky_api = DarkSkyAPI(DARK_SKY_API_KEY)
muddy_forecast_service = MuddyForecastService(dark_sky_api)


@app.route('/', methods=['GET'])
def muddy_forecast():
    is_three_day_forecast_muddy = muddy_forecast_service.is_three_day_forecast_muddy()
    return render_template('muddy_forecast.html', is_three_day_forecast_muddy=is_three_day_forecast_muddy)
