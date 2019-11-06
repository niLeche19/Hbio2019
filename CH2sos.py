#############################################
#Atom electron program for Hbio 2019        #
#Author: Nick Lee                           #
#Date of creation: 11/2/19                  #
#===========================================#
#Instructions for use:                      #
#

import elements
from time import sleep
valence = elements.valence
elist = elements.pairings
elecone = 0
electwo = 0

def pgebreak():
    print(" ")

def begin():
    pgebreak()
    verdict = input("Press c to calculate, or press q to quit. ")
    if verdict == 'c':
         start()
    elif str(verdict) == "q":
        sleep(1)
        pgebreak()
        print("Goodbye!")
        return('')
    else:
        print("Try again backaroo.")
        begin()

def bond(x2, y2):
    pgebreak()
    x = valence[elecone]
    y = valence[electwo]
    if x == 8 or y == 8:
        print("You've entered a noble gas! Those don't like to bond to anything.")
        begin()

    if x == y and (x + y) >= 8:
        print("These atoms can form a covalent bond!")
        sleep(1)
        pgebreak()
        covcharge(x - 8)
        
    elif (x + y) == 8:
        print("These elements can form an ionic bond.")
        sleep(1)
        pgebreak()
        if (x - 8) < (y - 8):
            ioncharge(x2, y2)
        else:
            ioncharge(y2, x2)
        
    else:
        print("I can't find any bonds in these atoms ¯\(°_°)/¯")
        begin()
        
def covcharge(c):
    ccc = ""
    if c > 0:
        ccc = "+" + str(c)
    else:
        ccc = str(c)
    print("The molecule will have a charge of " + ccc + ".")
    begin()

def ioncharge(o, t):
    print("This molecule contains a " + elist[o][0] +
          " molecule with a charge of +" + str(valence[o]) + " and a "
          + elist[t][0] + " molecule with a chage of " + str(valence[t] - 8))

def start():
    pgebreak()
    good = 0
    global elecone, electwo
    try:
        elecone = int(input("How many electrons does atom number one have? ")) - 1
        electwo = int(input("How many electrons does atom number two have? ")) - 1
    except:
        print("Please input an electron value for both.")
        start()

    if elecone == 0 and electwo == 0:
        sleep(1)
        pgebreak()
        print("These two atoms form a covalent bond to make H2.")
        begin()
    else:
        if good == 20:
            print("Try again")
        else:
            body()

def body():
    global elecone, electwo
    pgebreak()
    if elecone > 107 or electwo > 107:
        print("One of your atoms has an impossible number of electrons!")
        sleep(1)
        begin()
    else:
        print("Atom number one is " + elist[elecone][0] + " and atom number two is " + elist[electwo][0] + ".")
        sleep(1)
        bond(elecone, electwo)

        begin()
        
begin()




