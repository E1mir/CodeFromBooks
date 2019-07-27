from HeadFirstDesignPatterns.chapter_2.interfaces import Observer, DisplayElement
from HeadFirstDesignPatterns.chapter_2.models import WeatherData


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self._temperature = None
        self._humidity = None
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self._temperature} F degrees and {self._humidity}% humidity")


class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self._max_temp = 0
        self._min_temp = 200
        self._temp_sum = 0
        self._num_readings = 0
        self._avg_temp = 0

        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self._temp_sum += temperature
        self._num_readings += 1
        self._avg_temp = self._temp_sum / self._num_readings

        self._max_temp = max(temperature, self._max_temp)
        self._min_temp = min(temperature, self._min_temp)

        self.display()

    def display(self):
        print(f"Avg/Max/Min temperature = {self._avg_temp}/{self._max_temp}/{self._min_temp}")


class HeatIndexDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self._heat_index = 0
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, t: float, rh: float, pressure: float):
        self._heat_index = self._compute_heat_index(t, rh)
        self.display()

    def display(self):
        print(f"Heat index is {self._heat_index:.5f}")

    @staticmethod
    def _compute_heat_index(t: float, rh: float):
        index = (
            (16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) +
             (0.00941695 * (t ** 2)) + (0.00728898 * (rh ** 2)) +
             (0.000345372 * (t ** 2 * rh)) - (0.000814971 * (t * rh ** 2)) +
             (0.0000102102 * (t ** 2 * rh ** 2)) - (0.000038646 * (t ** 3)) + (0.0000291583 * (rh ** 3)) +
             (0.00000142721 * (t ** 3 * rh)) + (0.000000197483 * (t * rh ** 3)) -
             (0.0000000218429 * (t ** 3 * rh ** 2)) +
             0.000000000843296 * (t ** 2 * rh ** 3)) -
            (0.0000000000481975 * (t ** 3 * rh ** 3))
        )
        return index


class ForecastDisplay(Observer, DisplayElement):
    def __init__(self, weather_data: WeatherData):
        self._current_pressure = 29.92
        self._last_pressure = None

        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self._last_pressure = self._current_pressure
        self._current_pressure = pressure
        self.display()

    def display(self):
        message = ""
        if self._current_pressure > self._last_pressure:
            message = "Improving weather on the way!"
        elif self._current_pressure == self._last_pressure:
            message = "More of the same"
        elif self._current_pressure < self._last_pressure:
            message = "Watch out for cooler, rainy weather.."
        print(f"Forecast: {message}")
