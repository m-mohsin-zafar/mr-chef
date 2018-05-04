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

    def send_homing(self, arm):
        try:
            message = '{} goHome'.format(arm)
            self.arduino_serial_data.write(message.encode('utf-8'))
            time.sleep(1)
        except ConnectionRefusedError:
            print("Unable to send message : {}".format(message))

