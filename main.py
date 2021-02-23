import requests
import json
import datetime as dt


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


def get_sunrise_sunset(latitude, longitude, formatted=False):
    """
    https://sunrise-sunset.org/api
    :param latitude:
    :param longitude:
    :param formatted:
    :return: tuple(sunrise, sunset)
    """
    params = {
        "lat":  latitude,
        "lng":  longitude,
        "formatted":    1 if formatted else 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    # print(response.url)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    return sunrise, sunset


iss_position = get_iss_position()

TURIN_LATITUDE = 45.068371
TURIN_LONGITUDE = 7.683070
sunrise, sunset = get_sunrise_sunset(TURIN_LATITUDE, TURIN_LONGITUDE)
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]

print("ISS current position              : ", iss_position)
print("Sunrise/Sunset at current location: ", sunrise, sunset )
print("Sunrise hour 24h                  : ", sunrise_hour)
print("Sunset hour 24h                   : ", sunset_hour)
print("current time                      : ", dt.datetime.now())
print("current hour                      : ", dt.datetime.now().hour)
