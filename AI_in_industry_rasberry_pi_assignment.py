import RPi.GPIO as GPIO
import time
from firebase import firebase

# Initialize Firebase
firebase = firebase.FirebaseApplication('YOUR_FIREBASE_URL', None)

# Define GPIO pin for IR sensor
ir_sensor_pin = 17  # Example pin, change it according to your wiring

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ir_sensor_pin, GPIO.IN)

# Function to read IR sensor data
def read_ir_sensor():
    return GPIO.input(ir_sensor_pin)

# Main loop
while True:
    ir_value = read_ir_sensor()

    # Send data to Firebase
    data = {'ir_value': ir_value}
    firebase.post('/sensor_data', data)

    # Add a delay to control the data sending rate
    time.sleep(1)