#This script simulates the Tug-of-War game!

import RPi.GPIO as GPIO
import time
import sys
from random import randint

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Game Definitions
#Dependent on breadboard setup
WL = 4 #arbitrary number
L3 = 17
L2 = 27
L1 = 22
N = 12
R1 = 16
R2 = 20
R3 = 21
WR = 7 #arbitrary number

Right = 23
Left = 18

#Inputs: (2 Buttons)
GPIO.setup(Right, GPIO.IN)
GPIO.setup(Left, GPIO.IN)

#Outputs: (7 LEDs)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(N, GPIO.OUT)
GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
GPIO.setup(R3, GPIO.OUT)

def reset(GPIO):
	cleared = False
	while cleared == False:
		if GPIO.input(Right) == True or GPIO.input(Left) == False:
			GPIO.output(R3, GPIO.LOW)
			GPIO.output(R2, GPIO.LOW)
			GPIO.output(R1, GPIO.LOW)
			GPIO.output(N, GPIO.LOW)
			GPIO.output(L1, GPIO.LOW)
			GPIO.output(L2, GPIO.LOW)
			GPIO.output(L3, GPIO.LOW)
			time.sleep(0.5)
			GPIO.output(R3, GPIO.HIGH)
			GPIO.output(R2, GPIO.HIGH)
			GPIO.output(R1, GPIO.HIGH)
			GPIO.output(N, GPIO.HIGH)
			GPIO.output(L1, GPIO.HIGH)
			GPIO.output(L2, GPIO.HIGH)
			GPIO.output(L3, GPIO.HIGH)
			time.sleep(0.5)
			GPIO.output(R3, GPIO.LOW)
			GPIO.output(R2, GPIO.LOW)
			GPIO.output(R1, GPIO.LOW)
			GPIO.output(N, GPIO.LOW)
			GPIO.output(L1, GPIO.LOW)
			GPIO.output(L2, GPIO.LOW)
			GPIO.output(L3, GPIO.LOW)
			cleared = True

def startup_sequence():
        count = 0
	while count < 2:
                GPIO.output(N, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(N, GPIO.LOW)
                GPIO.output(L1, GPIO.HIGH)
                GPIO.output(R1, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(L1, GPIO.LOW)
                GPIO.output(R1, GPIO.LOW)
                GPIO.output(L2, GPIO.HIGH)
                GPIO.output(R2, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(L2, GPIO.LOW)
                GPIO.output(R2, GPIO.LOW)
                GPIO.output(L3, GPIO.HIGH)
                GPIO.output(R3, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(L3, GPIO.LOW)
                GPIO.output(R3, GPIO.LOW)
                GPIO.output(L2, GPIO.HIGH)
                GPIO.output(R2, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(L2, GPIO.LOW)
                GPIO.output(R2, GPIO.LOW)
                GPIO.output(L1, GPIO.HIGH)
                GPIO.output(R1, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(L1, GPIO.LOW)
                GPIO.output(R1, GPIO.LOW)
                count+=1

        GPIO.output(N, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(N, GPIO.LOW)
        GPIO.output(L1, GPIO.HIGH)
        GPIO.output(R1, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(L1, GPIO.LOW)
        GPIO.output(R1, GPIO.LOW)
        GPIO.output(L2, GPIO.HIGH)
        GPIO.output(R2, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(L2, GPIO.LOW)
        GPIO.output(R2, GPIO.LOW)
        GPIO.output(L3, GPIO.HIGH)
        GPIO.output(R3, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(L3, GPIO.LOW)
        GPIO.output(R3, GPIO.LOW)

def win_sequence(score):
        count = 0
	if score == WR:
		print("Congratulations Mr. Right!")
		while count < 3:
                        GPIO.output(L3, GPIO.HIGH)
                        time.sleep(0.05)
                        GPIO.output(L3, GPIO.LOW)
                        GPIO.output(L2, GPIO.HIGH)
                        time.sleep(0.05)
                        GPIO.output(L2, GPIO.LOW)
                        GPIO.output(L1, GPIO.HIGH)
                        time.sleep(0.05)
                        GPIO.output(L1, GPIO.LOW)
                        GPIO.output(N, GPIO.HIGH)
                        time.sleep(0.05)
                        GPIO.output(N, GPIO.LOW)
                        GPIO.output(R1, GPIO.HIGH)
                        time.sleep(0.05)
                        GPIO.output(R1, GPIO.LOW)
                        GPIO.output(R2, GPIO.HIGH)
                        time.sleep(0.05)
                        GPIO.output(R2, GPIO.LOW)
                        GPIO.output(R3, GPIO.HIGH)
                        time.sleep(0.05)
                        GPIO.output(R3, GPIO.LOW)
                        count+=1

	elif score == WL:
		print("Lefties have always been better at everything ;)")
		while count < 3:
                        GPIO.output(R3, GPIO.HIGH)
                        time.sleep(0.05)
                        GPIO.output(R3, GPIO.LOW)
                        GPIO.output(R2, GPIO.HIGH)
                        time.sleep(0.05)
                        GPIO.output(R2, GPIO.LOW)
                        GPIO.output(R1, GPIO.HIGH)
                        time.sleep(0.05)
                        GPIO.output(R1, GPIO.LOW)
                        GPIO.output(N, GPIO.HIGH)
                        time.sleep(0.05)
                        GPIO.output(N, GPIO.LOW)
                        GPIO.output(L1, GPIO.HIGH)
                        time.sleep(0.05)
                        GPIO.output(L1, GPIO.LOW)
                        GPIO.output(L2, GPIO.HIGH)
                        time.sleep(0.05)
                        GPIO.output(L2, GPIO.LOW)
                        GPIO.output(L3, GPIO.HIGH)
                        time.sleep(0.05)
                        GPIO.output(L3, GPIO.LOW)
                        count+=1

def tugofwar(GPIO):

	score = N
	while True:

                ready = False
                while ready == False:
                        time.sleep(randint(1, 2))
                        if GPIO.input(Right) == False and GPIO.input(Left) == True: ready = True
                        else: print("Let go of the button! No cheating!")






		GPIO.output(score, GPIO.HIGH)
		print("Click that button!")
		while True:
			if GPIO.input(Right) == True or GPIO.input(Left) == False: #equal chance
                                time.sleep(0.1)
				print("Someone clicked it~!")
				GPIO.output(score, GPIO.LOW)
				if GPIO.input(Left) == False: #Left pushed first
					if score == L3:		score = WL
					elif score == L2:	score = L3
					elif score == L1:	score = L2
					elif score == N:	score = L1
					elif score == R1:	score = N
					elif score == R2:	score = R1
					elif score == R3:	score = R2
				if GPIO.input(Right) == True: #Right pushed first
					if score == L3:		score = L2
					elif score == L2:	score = L1
					elif score == L1:	score = N
					elif score == N:	score = R1
					elif score == R1:	score = R2
					elif score == R2:	score = R3
					elif score == R3:	score = WR
				time.sleep(0.1)

				if score == WR or score == WL:
					if score == WR:
						GPIO.output(R1, GPIO.HIGH)
						GPIO.output(R2, GPIO.HIGH)
						GPIO.output(R3, GPIO.HIGH)

					elif score == WL:
						GPIO.output(L1, GPIO.HIGH)
						GPIO.output(L2, GPIO.HIGH)
						GPIO.output(L3, GPIO.HIGH)

					time.sleep(0.4)
					GPIO.output(R3, GPIO.LOW)
					GPIO.output(R2, GPIO.LOW)
					GPIO.output(R1, GPIO.LOW)
					GPIO.output(N, GPIO.LOW)
					GPIO.output(L1, GPIO.LOW)
					GPIO.output(L2, GPIO.LOW)
					GPIO.output(L3, GPIO.LOW)
					break
				else:
					GPIO.output(score, GPIO.HIGH)
					time.sleep(0.4)
					GPIO.output(score, GPIO.LOW)
					break

		if score == WR or score == WL: return score

if __name__ == "__main__":
	print("Hello! Welcome to Tug of War!")

	wantToPlay = True
	startup_sequence()
	while wantToPlay == True:
		print("Are you ready?")

		while True:
			if GPIO.input(Right) == True or GPIO.input(Left) == False: break

		print("Let's begin!")

		reset(GPIO)
		score = tugofwar(GPIO)
		win_sequence(score)

		print("Want to Play Again?")
		wantToPlay = False
		count = 0
		while count < 70:
			if GPIO.input(Right) == True or GPIO.input(Left) == False:
				wantToPlay = True
				break
			count+=1
			time.sleep(0.1)

	print("Thank you for playing!")
	sys.exit()
