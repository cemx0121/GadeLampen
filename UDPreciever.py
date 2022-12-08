import json
from socket import *
import threading
import requests

URL = 'https://gadelampenrest.azurewebsites.net/api/lamps'
def Add(lampInfo):
    response = requests.post(URL, json=lampInfo)
    return response

def handleClient(message, clientAddress):
    print("From IP/Port:", clientAddress)
    decodedMessage = message.decode()
    print(decodedMessage)
    newMessage = json.loads(decodedMessage)
    response = Add(newMessage)
    print(response.status_code, response.reason)

serverPort = 18000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("The server is ready to receive")
while True:
 message, clientAddress = serverSocket.recvfrom(2048)
 threading.Thread(target=handleClient, args=(message, clientAddress)).start()
