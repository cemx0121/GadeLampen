import requests

url = "https://gadelampenrest.azurewebsites.net/api/Lamps/"

def CollectBulbInfo():
    # Collect info about the bulb running this script
    res = requests.get(url)
    data = res.json()
    existingDeviceNames = []
    length = len(data)
    for i in range(length):
        existingDeviceNames.append(data[i]["deviceName"])
    while True:
        global deviceName
        deviceName = input("Angiv hvad navnet på denne pære er: ")
        if deviceName not in existingDeviceNames:
            break
        else:
            print("Et device med dette navn eksistere allerede! Prøv nyt navn!")
    while True:
        try:
            global turnOnDuration
            turnOnDuration = int(input("Angiv hvor længe pæren skal lyse når den fanger bevægelse i sekunder: "))
            break
        except ValueError:
            print("Indtast venligst et gyldigt input(hel tal)")
    while True:
        try:
            global watt
            watt = int(input("Angiv hvor mange watt denne pære bruger: "))
            break
        except ValueError:
            print("Indtast venligst et gyldigt input(hel tal)")
    return deviceName, turnOnDuration, watt
