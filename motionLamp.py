import RPi.GPIO as GPIO     # Import Library to access GPIO PIN
import time                 # To access delay function
import requests
from datetime import datetime, timedelta


while True:
    city = input("Hvilken by befinder du dig i? : ") # Takes input which city the lamp is in.

    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=08ee16c2dc794824ee9b4d2f71a7091d".format(city) # Gets the weather data from third party API from the city from the input

    res = requests.get(url) # Makes a HTTP GET request to the URL and saves the response
    data = res.json() # Saves the data from the response in JSON format
    print(res) # Prints the response code
    if res.status_code != 404: #Checks if the response code isn't 404, if it is 404 you start over in the while loop
        timezone = data["timezone"]
        # Saves the sunrise/sunset time in UNIX format and adds the timezone
        sunrise_time_unixAndTimezone = data["sys"]["sunrise"]+timezone
        sunset_time_unixAndTimezone = data["sys"]["sunset"]+timezone
        # Saves two variables as datetime types with only YMDHMS. The datetime is set by the data imported from the API
        sunrise_time = datetime.utcfromtimestamp(sunrise_time_unixAndTimezone).strftime("%Y-%m-%d %H:%M:%S")
        sunset_time = datetime.utcfromtimestamp(sunset_time_unixAndTimezone).strftime("%Y-%m-%d %H:%M:%S")
        print("Sunrise:", sunrise_time)
        print("Sunset:", sunset_time)
        break

PIR_PIN = 7                 # Define PIN for PIR
Relay_PIN = 11              # Define PIN for Relay
GPIO.setmode(GPIO.BOARD)    # Consider complete raspberry-pi board
GPIO.setwarnings(False)     # To avoid same PIN use warning
GPIO.setup(Relay_PIN,GPIO.OUT)   # Set pin function as output
GPIO.setup(PIR_PIN,GPIO.IN)   # Set pin function as input
mockTime = datetime(2022, 11, 30, 17, 15, 15).strftime("%Y-%m-%d %H:%M:%S")

try:
    while True:
        timeNow = (datetime.utcnow() + timedelta(seconds=timezone)).strftime("%Y-%m-%d %H:%M:%S")
        if sunrise_time < timeNow < sunset_time: # Checks if the time now is within sunrise and sunset
            print("The sun is up! Motion sensor OFF! Checking in 1 minute again!")
            time.sleep(60)
        else:
            if GPIO.input(PIR_PIN) == GPIO.HIGH:
                print("Motion Detected!")
                GPIO.output(Relay_PIN, GPIO.LOW) # Relay ON
                time.sleep(10)
            else:
                print("No motion detected!")
                GPIO.output(Relay_PIN, GPIO.HIGH) # Relay OFF
                time.sleep(1)
except:
    GPIO.cleanup()
