import RPi.GPIO as GPIO     # Import Library to access GPIO PIN
import time as t                 # To access delay function
from GetCityWeatherInfo import *
from datetime import datetime, timedelta
from UDPsender import *

# Collect info about the bulb running this script
deviceName = input("Angiv hvor navnet på denne pære: ")
turnOnDuration = input("Angiv hvor længe pæren skal lyse når den fanger bevægelse: ")
watt = input("Angiv hvor mange watt denne pære bruger: ")
sunset_time, sunrise_time, visibility, timezone, cityname, country = GetCityWeatherInfo()

PIR_PIN = 7                 # Define PIN for PIR
Relay_PIN = 11              # Define PIN for Relay
GPIO.setmode(GPIO.BOARD)    # Consider complete raspberry-pi board
GPIO.setwarnings(False)     # To avoid same PIN use warning
GPIO.setup(Relay_PIN,GPIO.OUT)   # Set pin function as output
GPIO.setup(PIR_PIN,GPIO.IN)   # Set pin function as input

try:
    while True:
        timeNow = (datetime.utcnow() + timedelta(seconds=timezone)).strftime("%Y-%m-%dT%H:%M:%S")
        if sunrise_time < timeNow < sunset_time and visibility > 5: # Checks if the time now is within sunrise and sunset
            print("The sun is up and the visibility is above 5km! Motion sensor and lamp OFF! Checking in 1 minute again")
            print("Current time:", timeNow)
            t.sleep(60)
        else:
            if GPIO.input(PIR_PIN) == GPIO.HIGH:
                print("Motion Detected! Current time:", timeNow)
                GPIO.output(Relay_PIN, GPIO.LOW) # Relay ON
                SendUDPPacket(deviceName, timeNow, watt, turnOnDuration, cityname, country)
                t.sleep(turnOnDuration)
            else:
                print("No motion detected! Current time:", timeNow)
                GPIO.output(Relay_PIN, GPIO.HIGH) # Relay OFF
                t.sleep(1)
except:
    GPIO.cleanup()
