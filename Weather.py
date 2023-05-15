import requests,json
from celery import Celery
from celery.schedules import crontab


def get_weather_status(city: str)->str:
    api_key = "435744b930e3d41b754c08cedd23c364"
    base_url =  "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    app = Celery('wether',backend='redis://localhost', broker='redis://localhost:6379/0')
    app.conf.beat_schedule = {
        'every-1-minute': {
            'task': 'task111.get_weather_status',
            'schedule': crontab(minute='*/1'),
            'args': ('Tehran','mashhad', 'shiraz', 'semirom', 'ahvaz', 'baghdad', 'vaan', 'haraat', 'saari')
        }
    }
    app.conf.timezone = 'UTC'
    response = requests.get(complete_url)
   