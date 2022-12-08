import requests

url = "https://gadelampenrest.azurewebsites.net/api/Lamps/"

# Collect user info about the bulb running this script
def CollectBulbInfo():
    # Makes HTTP GET Request to our own API and saves the data
    res = requests.get(url)
    data = res.json()
    # Creates a new array with every devicename from the data
    existingDeviceNames = []
    length = len(data)
    for i in range(length):
        existingDeviceNames.append(data[i]["deviceName"])
    # Checks if the user input for devicename already exists in the database, if it does error message is printed and user gets to try again.
    while True:
        global deviceName
        deviceName = input("Angiv hvad navnet på denne pære er: ")
        if deviceName not in existingDeviceNames:
            break
        else:
            print("Et device med dette navn eksistere allerede! Prøv nyt navn!")
    # Checks if the user input is valid integer, if not user gets to try again
    while True:
        try:
            global turnOnDuration
            turnOnDuration = int(input("Angiv hvor længe pæren skal lyse når den fanger bevægelse i sekunder: "))
            break
        except ValueError:
            print("Indtast venligst et gyldigt input(hel tal)")
    # Checks if the user input is valid integer, if not user gets to try again
    while True:
        try:
            global watt
            watt = int(input("Angiv hvor mange watt denne pære bruger: "))
            break
        except ValueError:
            print("Indtast venligst et gyldigt input(hel tal)")
    return deviceName, turnOnDuration, watt
