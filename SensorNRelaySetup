import RPi.GPIO as GPIO     # Import Library to access GPIO PIN
import time                 # To access delay function
from GetCityWeatherInfo import *
from datetime import timedelta

sunset_time, sunrise_time, visibility, timezone = GetCityWeatherInfo()

PIR_PIN = 7                 # Define PIN for PIR
Relay_PIN = 11              # Define PIN for Relay
GPIO.setmode(GPIO.BOARD)    # Consider complete raspberry-pi board
GPIO.setwarnings(False)     # To avoid same PIN use warning
GPIO.setup(Relay_PIN,GPIO.OUT)   # Set pin function as output
GPIO.setup(PIR_PIN,GPIO.IN)   # Set pin function as input

try:
    while True:
        timeNow = (datetime.utcnow() + timedelta(seconds=timezone)).strftime("%Y-%m-%d %H:%M:%S")
        if sunrise_time < timeNow < sunset_time and visibility > 5: # Checks if the time now is within sunrise and sunset
            print("The sun is up and the visibility is above 5km! Motion sensor and lamp OFF! Checking in 1 minute again")
            print("Current time:", timeNow)
            time.sleep(60)
        else:
            if GPIO.input(PIR_PIN) == GPIO.HIGH:
                print("Motion Detected! Current time:", timeNow)
                GPIO.output(Relay_PIN, GPIO.LOW) # Relay ON
                time.sleep(10)
            else:
                print("No motion detected! Current time:", timeNow)
                GPIO.output(Relay_PIN, GPIO.HIGH) # Relay OFF
                time.sleep(1)
except:
    GPIO.cleanup()
