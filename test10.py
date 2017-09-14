#!/usr/bin/python3
import random


from time import sleep

print("please select:")
print("1 rock")
print("2 paper")
print ("3 scissors")

player=input("choose from 1-3:")
if player==1:
	print("you choose Rock")
	sleep(2)
	print("CPU chooses paper")
	sleep(.5)
	print("you lose, and you will never win!")

elif player==2:
	print("you choose paper")
	sleep(2)
	print("CPU chooses scissors")
	sleep(.5)
	print("you lose, and ypu will never win!")

else:
	print("you choose scissors")
	sleep(2)
	print("CPU chooses rock")
	sleep(.5)
	print("you win,and you you will never win!")