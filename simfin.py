#!/usr/bin/python3

# TODO's:

# remove possibility to go to negative funds, unless you implement a credit system of some sort.

# perhaps encapsulate your "bank" account as a class, so that you don't end up with a metric fuckton of variables.

# Also good practice for learning.

import json
import time

open('simfin.json').read()
var = json.loads(open('simfin.json').read())
var = var["var"]
moneyaddrm = json.loads(open('simfin.json').read())
moneyaddrm = moneyaddrm["moneyaddrm"]
whenaddrm = json.loads(open('simfin.json').read())
whenaddrm = whenaddrm["whenaddrm"]


def history():
    print("Last time you added/removed %s." % (moneyaddrm))
    print("at %s" % (whenaddrm))


def howmuch():
    print("You currently have %s" % (var))


def remove():
    global var
    print("How much money do you want to remove? ")
    y = input()
    if y.isnumeric() is False:
        print("That's not a valid number!")
        y = 0
        remove()
    z = int(y)
    global lz
    lz = z
    print("You now have %s" % (var - lz))
    var = (var - lz)
    writeout()


def writeout():
    global lz
    with open('simfin.json', 'w') as outfile:
        json.dump({'var': var, 'moneyaddrm': lz, 'whenaddrm': (time.strftime("%d/%m/%Y %H:%M"))}, outfile, indent=4)


def add():
    global var
    print("How much money do you want to add? ")
    y = input()
    if y.isnumeric() is False:
        print("That's not a valid number!")
        y = 0
        add()
    z = int(y)
    global lz
    lz = z
    print("You now have %s" % (var + lz))
    var = (var + lz)
    writeout()


def help():
    print("add for adding money")
    print("howmuch to check money amount")
    print("history to check when you last added/removed money")
    print("remove to remove money")
    print("close to close the program")
    print("and help to run this again")
    start()


def start():
    print("What do you want to do?")
    x = input()
    if x == 'history':
        history()

    elif x == 'howmuch':
        howmuch()

    elif x == 'add':
        add()

    elif x == 'remove':
        remove()

    elif x == 'help':
        help()

    elif x == 'close':
        pass

    else:
        help()


start()
