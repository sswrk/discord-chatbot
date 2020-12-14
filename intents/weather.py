import pytemperature
import os
from pyowm.owm import OWM


def translate(weather):
    translations = {
        "Clear": 'Czysto',
        "Clouds": 'Pochmurnie',
        "Rain": "Deszczowo",
        "Mist": "Mgła",
        "Thunderstorm": "Burza",
        "Drizzle": "Mżawka",
        "Snow": "Śnieg",
        "Fog": "Mgła",
        "Tornado": "Tornado"
    }
    return translations[weather]


def truncate(f, n):
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d + '0' * n)[:n]])


def check_for_weather(message):
    if message.content.find("podaj") != -1 or message.content.find("jak") != -1:
        if message.content.find("pogod") != -1 or message.content.find("temperatur") != -1 or message.content.find(
                "zachmurzenie") != -1 \
                or message.content.find("ciśnienie") != -1:
            owm = OWM(os.getenv('OWM_APIKEY'))
            manager = owm.weather_manager()
            weather = manager.weather_at_place(name=os.getenv('OWM_LOCATION')).weather

            reply = f"Aktualna pogoda w {os.getenv('OWM_LOCATION')}:\n" \
                    f"{translate(weather.status)}\n" \
                    f"Temperatura: {truncate(pytemperature.k2c(weather.temp['temp']), 1)} stopni Celsjusza\n" \
                    f"Ciśnienie: {weather.pressure['press']} hPa"

            return reply

    return ""
