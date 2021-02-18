from api.core.services import OpenWeatherMapAPI
from flask_sqlalchemy import SQLAlchemy

class OpenWeatherMapFlask:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not app.config.get("OWM_API_KEY"):
            raise RuntimeError("OWM_API_KEY needs to be set.")

        api_key = app.config.get("OWM_API_KEY")
        units = app.config.get("OWM_UNITS") or "metric"

        self.owm = OpenWeatherMapAPI(api_key, units=units)

    def forecast(self, *args, **kwargs):
        return self.owm.forecast(*args, **kwargs)


db = SQLAlchemy()
owm = OpenWeatherMapFlask()

