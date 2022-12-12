import requests

#Our API

#Get the response date from the given API
response = requests.get('https://lamperestapi.azurewebsites.net/api/Lamps/SearchLampInfoByDevicename/Phillips%20Hue')

#Checks if the given data from the API matches our expectation
def test1_api():
    body = response.json()
    assert response.status_code == 200
    assert body[0]['deviceName'] == 'Phillips Hue'
    assert body[0]['turnedOn'] == '2022-12-08T15:00:00'
    assert body[0]['watt'] == 10
    assert body[0]['turnOnDuration'] == 10
    assert body[0]['city'] == 'Miami'
    assert body[0]['country'] == 'US'

#prints out the status code
print(f'status code: {response.status_code}')

#prints out the Json string
print(json.dumps(response.json()))
_______________________________________________________________________________________________________________________________________________________________________

#3.Party API

#Get the response date from the given API
response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=copenhagen&appid=08ee16c2dc794824ee9b4d2f71a7091d')

#Checks if the given data from the API matches our expectation
def test2_api():
    body = response.json()
    assert response.status_code == 200
    assert body['name'] == 'Copenhagen'
    assert body['timezone'] == 3600
    assert body['coord']['lon'] == 12.5655
    assert body['coord']['lat'] == 55.6759
    assert body['sys']['country'] == 'DK'
    
#prints out the status code
print(f'status code: {response.status_code}')

#prints out the Json string
print(json.dumps(response.json()))
