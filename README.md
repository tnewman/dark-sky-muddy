# Dark Sky Muddy
A web application showing whether or not it will be muddy over the next 3 days.

## Prerequisites
1. [Python 3](https://www.python.org/)
2. [Pipenv](https://pipenv.kennethreitz.org/en/latest/)
3. `DARK_SKY_API_KEY` environment variable set to your Dark Sky API Key

## Install Pipenv Dependencies
```bash
pipenv install --dev
```

## Run App in Dev Mode
```bash
pipenv run run_dev.py
```
The application can be accessed at `http://localhost:5000` in the browser.

## Run Tests
- Note: The `DARK_SKY_API_KEY` environment variable is required to run integration tests.
```bash
pipenv run pytest
```

## Run App in Docker
```bash
docker build -t dark-sky-muddy .
docker run -e DARK_SKY_API_KEY=yourapikey -p 8000:8000 dark-sky-muddy
```
The application can be accessed at `http://localhost:8000` in the browser.
