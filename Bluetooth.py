import bluetooth
import RPi.GPIO as GPIO

data="data"

def bluetooth_communication():
    global data
    print('The client can connect...')
    server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 1
    server.bind(("", port))
    server.listen(1)
    client, address = server.accept()
    print("Connected to ", address)
    data = 'Data from phone'
    data = data.encode()
    client.send(data)
    while True:
        data = (client.recv(1024)).decode()
        print("received [%s]" % data)

