from HeadFirstDesignPatterns.chapter_2.displays import CurrentConditionsDisplay, StatisticsDisplay, ForecastDisplay, \
    HeatIndexDisplay
from HeadFirstDesignPatterns.chapter_2.models import WeatherData

if __name__ == '__main__':
    w_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data=w_data)
    statistics_display = StatisticsDisplay(weather_data=w_data)
    forecast_display = ForecastDisplay(weather_data=w_data)
    heat_index_display = HeatIndexDisplay(weather_data=w_data)
    line = "-" * 60
    print(line)
    w_data.set_measurements(80, 65, 30.4)
    print(line)
    w_data.set_measurements(82, 70, 29.2)
    print(line)
    w_data.set_measurements(78, 90, 29.2)
    print(line)
    w_data.remove_observer(statistics_display)
    w_data.remove_observer(heat_index_display)
    w_data.set_measurements(79, 76, 32.2)
    print(line)
    w_data.remove_observer(current_display)
    w_data.set_measurements(78, 90, 29.2)
    print(line)
    w_data.register_observer(statistics_display)
    w_data.set_measurements(77, 78, 30.2)
    print(line)
