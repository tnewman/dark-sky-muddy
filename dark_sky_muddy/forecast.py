from typing import Optional


FREEZING_TEMPERATURE_DEGREES_F = 32


class Forecast:
    def __init__(self, temperature: float, precipitation_type: Optional[str]):
        """
        Represents the weather forecast for a day.
        :param temperature: The temperature in fahrenheit.
        :param precipitation_type: The type of precipitation (rain, snow, or sleet). Can be None if no precipitation is
        possible.
        """
        self.temperature_degrees_f = temperature
        self.precipitation_type = precipitation_type

    def is_muddy(self) -> bool:
        """
        Checks if the forecast is muddy.
        :return: True if the forecast is muddy, otherwise false.
        """
        return self.precipitation_type == 'rain' and self.temperature_degrees_f > FREEZING_TEMPERATURE_DEGREES_F
