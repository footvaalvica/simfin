#!/usr/bin/python3

import json
import time

def writeout():
	with open('simfin.json' , 'w') as outfile:
		json.dump({'var':int(var), 'moneyaddrm':int(y), 'whenaddrm':(time.strftime("%d/%m/%Y %H:%M")) }, outfile, indent=4)

open('simfin.json').read()
var = json.loads(open('simfin.json').read())
var = var["var"]
moneyaddrm = json.loads(open('simfin.json').read())
moneyaddrm = moneyaddrm["moneyaddrm"]
whenaddrm = json.loads(open('simfin.json').read())
whenaddrm = whenaddrm["whenaddrm"]

print("What do you want to do?")
x = input()

if x == 'history':
	print("Last time you added/removed %s." %(moneyaddrm))
	print("at %s" %(whenaddrm))

if x == 'howmuch':
	print("You currently have %s" %(var))

if x == 'add':
	print("How much money do you want to add? ")
	y = int(input())
	print ("You now have %s" %(var+y))
	var = (var+y)
	writeout()


if x == 'remove':
	print("How much money do you want to remove? ")
	y = int(input())
	print ("You now have %s" %(var-y))
	var = (var-y)
	writeout()

