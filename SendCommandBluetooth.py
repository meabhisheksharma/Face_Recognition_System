import bluetooth
import sys

bd_addr = "00:21:13:00:F9:BA"  # itade address
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))
print('Connected')

def sendData(comm):
    sock.send(comm)

def recieveData():
    adata = sock.recv(3)
    return adata
def closeSocket():
    sock.close()