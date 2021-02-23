import requests
import json
import datetime as dt
import time


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

    print("iss position for google maps: ", latitude, longitude)
    iss_position_tuple = (float(latitude), float(longitude))
    iss_position_dict = {
        "latitude": float(latitude),
        "longitude": float(longitude)
    }
    return iss_position_dict


def is_iss_above(latitude, longitude):
    iss_position = get_iss_position()
    current_position = {
        "latitude": float(latitude),
        "longitude": float(longitude)
    }
    print("iss_position    : ", iss_position)
    print("current_position: ", current_position)

    print("(current latitude - 5.0) <= iss latitude <=  (current latitude + 5.0) : ", end="")
    if (current_position["latitude"] - 5.0) <= iss_position["latitude"] <= (current_position["latitude"] + 5.0):
        print(True)
        print("(current longitude - 5.0) <= iss longitude <=  (current longitude + 5.0) : ", end="")
        if (current_position["longitude"] - 5.0) <= iss_position["longitude"] <= (current_position["longitude"] + 5.0):
            print(True)
            print("iss is above: ", True)
            return True
        else:
            print(False)
            print("iss is above: ", False)
            return False
    else:
        print(False)
        print("iss is above: ", False)
        return False


def get_sunrise_sunset(latitude, longitude, formatted=False):
    """
    https://sunrise-sunset.org/api
    :param latitude:
    :param longitude:
    :param formatted:
    :return: tuple(sunrise, sunset)
    """
    params = {
        "lat": latitude,
        "lng": longitude,
        "formatted": 1 if formatted else 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    # print(response.url)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    return sunrise, sunset


def is_night(latitude, longitude):
    sunrise, sunset = get_sunrise_sunset(latitude, longitude)
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])

    current_hour = dt.datetime.now().hour
    print(type(current_hour))
    print("sunrise hour    : ", sunrise_hour)
    print("sunset hour     : ", sunset_hour)
    print("current hour    : ", current_hour)

    print("sunrise_hour >= current_hour >= sunset_hour: ", end="")
    if sunrise_hour >= current_hour >= sunset_hour:
        print(True)
        print("is night: ", True)
        return True
    else:
        print(True)
        print("is night: ", False)
        return False


TURIN_LATITUDE = 45.068371
TURIN_LONGITUDE = 7.683070

iss_above = is_iss_above(latitude=TURIN_LATITUDE, longitude=TURIN_LONGITUDE)
is_dark = is_night(TURIN_LATITUDE, TURIN_LONGITUDE)

while True:
    if iss_above and is_dark:
        # send mail
        print("you can see the ISS now")
    else:
        print("you cannot see the ISS now")
    time.sleep(60)

