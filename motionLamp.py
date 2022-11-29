import RPi.GPIO as GPIO     # Import Library to access GPIO PIN
import time                 # To access delay function

PIR_PIN = 7                 # Define PIN for PIR
Relay_PIN = 11              # Define PIN for Relay
GPIO.setmode(GPIO.BOARD)    # Consider complete raspberry-pi board
GPIO.setwarnings(False)     # To avoid same PIN use warning

GPIO.setup(Relay_PIN,GPIO.OUT)   # Set pin function as output
GPIO.setup(PIR_PIN,GPIO.IN)   # Set pin function as input

try:

        time.sleep(2)
        while True:
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
