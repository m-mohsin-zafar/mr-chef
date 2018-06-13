import serial
import time


class Communication:
    def __init__(self):
        try:
            self.arduino_serial_data=serial.Serial('/dev/ttyACM0', 9600)
        except ConnectionError:
            print("Arduino not found!")

    def send(self, message, delay):
        try:
            self.arduino_serial_data.write(message.encode('utf-8'))
            time.sleep(delay)
        except ConnectionRefusedError:
            print("Unable to send message : {}".format(message))

    def get_synchronized(self, message):
        try:
            self.arduino_serial_data.write(message.encode('utf-8'))
            time.sleep(2)
            while self.arduino_serial_data.in_waiting > 0:
                message = self.arduino_serial_data.readline().decode()
                print(message)
                if message == "SYNC ACK":
                    return
        except ConnectionRefusedError:
            print("Unable to send message : {}".format(message))
