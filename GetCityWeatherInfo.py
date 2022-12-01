import requests
from datetime import datetime

def GetCityWeatherInfo():
    while True:
        city = input("Hvilken by befinder du dig i? : ")  # Takes input which city the lamp is in.
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=08ee16c2dc794824ee9b4d2f71a7091d".format(city)  # Gets the weather data from third party API from the city from the input.
        res = requests.get(url)  # Makes a HTTP GET request to the URL and saves the response
        data = res.json()  # Saves the data from the response in JSON format
        print(res)  # Prints the response code
        if res.status_code == 404:  # Checks if the response code isn't 404, if it is 404 you start over in the while loop
            print("Den søgte by findes ikke! Prøv igen!")
        else:
            global timezone
            timezone = data["timezone"]
            global visibility
            visibility = data["visibility"] / 1000 # To get visibility in kilometers
            # Saves the sunrise/sunset time in UNIX format and adds the timezone from the API
            sunrise_time_unixAndTimezone = data["sys"]["sunrise"] + timezone
            sunset_time_unixAndTimezone = data["sys"]["sunset"] + timezone
            # Saves two variables as datetime types with only YMDHMS. The datetime is set by the data imported from the API
            # The variables are made global to be accessed outside of the function
            global sunset_time
            global sunrise_time
            sunrise_time = datetime.utcfromtimestamp(sunrise_time_unixAndTimezone).strftime("%Y-%m-%d %H:%M:%S")
            sunset_time = datetime.utcfromtimestamp(sunset_time_unixAndTimezone).strftime("%Y-%m-%d %H:%M:%S")
            print(data["name"])
            print("Solopgang:", sunrise_time)
            print("Solnedgang:", sunset_time)
            print("Sigtbarhed(km):", visibility)
            break
