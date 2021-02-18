import requests


class OpenWeatherMapAPI:
    BASE_URL = "https://api.openweathermap.org/data/2.5/{}".format

    def __init__(self, api_key, units="metric"):
        self.api_key = api_key
        self.units = units

    def forecast(self, city, state_code=None, country_code=None):
        q = [city]

        if state_code is not None:
            q.append(state_code)

        if state_code is not None and country_code is not None:
            q.append(country_code)

        query_string = {
            "q": ','.join(q),
            "appid": self.api_key,
            "units": self.units,
        }

        return requests.get(self.BASE_URL("forecast"), params=query_string)
