FROM python:3.7
WORKDIR /app
RUN pip3 install pipenv gunicorn
COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy --system
COPY . ./
CMD ["gunicorn", "--bind", "0.0.0.0", "-w", "4", "dark_sky_muddy.muddy_forecast_app:app"]
