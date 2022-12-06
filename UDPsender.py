from socket import *
from datetime import *

serverName = "255.255.255.255"
serverPort = 18000

def SendUDPPacket(deviceName, turnOnTime, watt, turnOnDuration, cityname, country):
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    message = '{"deviceName":"'+ str(deviceName) +'","turnedOn":"'+ turnOnTime +'", "watt": '+ str(watt) +', "turnOnDuration": '+ str(turnOnDuration) +', "city":"'+ str(cityname) +'", "country":"'+ str(country) +'"}'
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    clientSocket.close()
