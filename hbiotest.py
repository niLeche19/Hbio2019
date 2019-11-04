#############################################
#Atom electron program for Hbio 2019        #
#Author: Nick Lee                           #
#Date of creation: 11/2/19                  #
#===========================================#
#Instructions for use:                      #

from HBIO import elements
from time import sleep
elist = elements.pairings
elecone = 0
electwo = 0

def pgebreak():
    print(" ")

def begin():
    pgebreak()
    verdict = input("Press c to calculate, or press q to quit. ")
    if verdict == "c":
        start()
    else:
        sleep(1)
        pgebreak()
        print("Goodbye!")

def start():
    pgebreak()
    global elecone, electwo
    elecone = int(input("How many electrons does atom number one have? "))
    electwo = int(input("How many electrons does atom number two have? "))
    body()

def body():
    global elecone, electwo
    pgebreak()
    if elecone > 108 or electwo > 108:
        print("one of your atoms has an impossible number of electrons!")
        sleep(1)
        begin()
    else:
        print("Atom number one is " + elist[elecone][0] + " and atom number two is " + elist[electwo][0] + ".")
        sleep(2)
        begin()
begin()
