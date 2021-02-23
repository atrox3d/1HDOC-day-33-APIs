import requests
import json


def get_iss_position():
    """
    http://open-notify.org/Open-Notify-API/ISS-Location-Now/
    :return: iss_position: tuple(latitude, longitude)
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]

    iss_position = (latitude, longitude)
    return iss_position


def get_sunrise_sunset(params):
    """
    https://sunrise-sunset.org/api
    :param params:
    :return: tuple(sunrise, sunset)
    """
    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    # print(response.url)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    return sunrise, sunset


TURIN = {
    "lat": 45.068371,
    "lng": 7.683070,
}

print(get_sunrise_sunset(TURIN))