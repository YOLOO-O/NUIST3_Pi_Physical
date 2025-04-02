# LED.py 
# Author: Liu Zibo
# ID: 20110005@mail.wit.ie(SETU)/202283890001(NUIST)
# Date: 2025-03-31 
# Description: A simple script to control an LED using Raspberry Pi's GPIO.

import RPi.GPIO as GPIO  # Import the RPi.GPIO module for controlling GPIO pins
import time  # Import the time module for adding delays

# Set up GPIO mode to BCM (Broadcom SOC channel numbering)
GPIO.setmode(GPIO.BCM)

# Disable warnings from GPIO (e.g., if the pin was already in use)
GPIO.setwarnings(False)

# Set GPIO pin 18 as an output pin
GPIO.setup(18, GPIO.OUT)

try:
    print("LED on")  # Print message to indicate LED is turning on
    GPIO.output(18, GPIO.HIGH)  # Turn the LED on
    time.sleep(1)  # Keep the LED on for 1 second

    print("LED off")  # Print message to indicate LED is turning off
    GPIO.output(18, GPIO.LOW)  # Turn the LED off

finally:
    GPIO.cleanup()  # Reset GPIO settings to avoid conflicts
