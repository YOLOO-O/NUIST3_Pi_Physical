# Quiz2.py
# Author: Liu Zibo
# ID: 20110005@mail.wit.ie(SETU)/202283890001(NUIST)
# Date: 2025-04-02
# Description: A Python quiz game with LED indicators for correct and incorrect answers

import RPi.GPIO as GPIO
import time

# Define GPIO pins for LEDs
GREEN_LED = 17  # Green LED for correct answers
RED_LED = 18    # Red LED for incorrect answers

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setwarnings(False)

def light_led(pin, duration=1):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin, GPIO.LOW)

def quiz():
    print("Welcome to the Python Quiz!")
    print("Answer the following questions:")
   
    questions = [
        "1) Which of the following is NOT a Python data type?\n   a) int\n   b) float\n   c) rational\n   d) string\n   e) bool",
        "2) Which of the following is NOT a built-in operation in Python?\n   a) +\n   b) %\n   c) abs()\n   d) sqrt()",
        "3) In a mixed-type expression involving ints and floats, Python will convert:\n   a) floats to ints\n   b) ints to strings\n   c) floats and ints to strings\n   d) ints to floats",
        "4) The best structure for implementing a multi-way decision in Python is:\n   a) if\n   b) if-else\n   c) if-elif-else\n   d) try",
        "5) What statement can be executed in the body of a loop to cause it to terminate?\n   a) if\n   b) exit\n   c) continue\n   d) break"
    ]
   
    correct_answers = ["c", "d", "d", "c", "d"]
    score = 0
   
    for i in range(len(questions)):
        print("\n" + questions[i])
        user_answer = input("Enter your answer (a/b/c/d): ").strip().lower()
       
        if user_answer == correct_answers[i]:
            print("Correct!")
            light_led(GREEN_LED)
            score += 1
        else:
            print("Incorrect!")
            light_led(RED_LED)
   
    print("\nQuiz completed!")
    print(f"You got {score}/{len(questions)} questions correct.")
   
    GPIO.cleanup()

# Run the quiz function
quiz()
