import RPi.GPIO as GPIO
import time
from firebase import firebase


firebase = firebase.FirebaseApplication('YOUR_FIREBASE_URL', None)


ir_sensor_pin = 17  


GPIO.setmode(GPIO.BCM)
GPIO.setup(ir_sensor_pin, GPIO.IN)


def read_ir_sensor():
    return GPIO.input(ir_sensor_pin)


while True:
    ir_value = read_ir_sensor()

    
    data = {'ir_value': ir_value}
    firebase.post('/sensor_data', data)

    
    time.sleep(5)
