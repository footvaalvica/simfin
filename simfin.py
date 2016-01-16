#!/usr/bin/python3.4

#imports the simfin.json module (needed to write and read the json file).
import json

#Opens the simfin.json file for loading the variable.
open('simfin.json').read()
var = json.loads(open('simfin.json').read())
var = var["var"]

#Asks the user if he wants to add or to remove money.
print("What do you want to do?")
x = input()

if x == 'howmuch':
	print("You currently have %s" %(var))
	
if x == 'add':
	print("How much money do you want to add? ")
	y = int(input())
	print ("You now have %s" %(var+y))
	var = (var+y)
	with open('simfin.json', 'w') as outfile:
		json.dump({'var':int(var)}, outfile, indent=4)

if x == 'remove':
	print("How much money do you want to remove? ")
	y = int(input())
	print ("You now have %s" %(var-y))
	var = (var-y)
	with open('simfin.json' , 'w') as outfile:
		json.dump({'var':int(var)}, outfile, indent=4)
		
