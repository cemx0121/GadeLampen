from socket import *
import time
from datetime import *

serverName = "255.255.255.255"
serverPort = 18000

def SendUDPPacket(deviceName, turnOnTime)
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    timeNow = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
    message = '{"deviceName":"'+ deviceName +'","turnedOn":"'+ turnOnTime +'"}'
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    time.sleep(5)
    clientSocket.close()
