element = ["Hydrogen","Helium","Lithium","Beryllium","Boron","Carbon","Nitrogen","Oxygen","Fluorine","Neon","Sodium","Magnesium","Aluminum","Silicon","Phosphorus","Sulfur","Chlorine","Argon","Potassium","Calcium","Scandium","Titanium","Vanadium","Chromium","Manganese","Iron","Cobalt","Nickel","Copper","Zinc","Gallium","Germanium","Arsenic","Selenium","Bromine","Krypton","Rubidium","Strontium","Yttrium","Zirconium","Niobium","Molybdenum","Technetium","Ruthenium","Rhodium","Palladium","Silver","Cadmium","Indium","Tin","Antimony","Tellurium","Iodine","Xenon","Cesium","Barium","Lanthanum","Cerium","Praseodymium","Neodymium","Promethium","Samarium","Europium","Gadolinium","Terbium","Dysprosium","Holmium","Erbium","Thulium","Ytterbium","Lutetium","Hafnium","Tantalum","Tungsten","Rhenium","Osmium","Iridium","Platinum","Gold","Mercury","Thallium","Lead","Bismuth","Polonium","Astatine","Radon","Francium","Radium","Actinium","Thorium","Protactinium","Uranium","Neptunium","Plutonium","Americium","Curium","Berkelium","Californium","Einsteinium","Fermium","Mendelevium","Nobelium","Lawrencium","Rutherfordium","Dubnium","Seaborgium","Bohrium","Hassium","Meitnerium"]
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109]
group = [1,18,1,2,13,14,15,16,17,18,1,2,13,14,15,16,17,18,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,1,2,3,102,102,102,102,102,102,102,102,102,102,102,102,102,102,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,1,2,3,102,102,102,102,102,102,102,102,102,102,102,102,102,103,4,5,6,7,8,9]
valence = []

twopers = [2,3,4,7,12,102]
othertwos = [23,73,105,74,106,26,76,108,27,77,109,28,110,111]
oners = [41,24,42,44,45,78,29,47,79]
others = [14,15,16,17,18]

pairings = []

for i in range(len(number)-1):
    pairings.append([element[i], number[i], group[i]])

for i in range(len(group)):
    if group[i] == 1:
        valence.append(1)
    elif group[i] == 103 or group[i] == 13:
        valence.append(3)
    elif i == 46:
        valence.append(18)
    for f in oners:
        if number[i] == f:
            valence.append(1)
    for g in othertwos:
        if number[i] == g:
            valence.append(2)
    for j in twopers:
        if group[i] == j:
            valence.append(2)
    for h in range(len(others)):
        if group[i] == others[h]:
            valence.append(h+4)

#############################################
#Atom electron program for Hbio 2019        #
#Author: Nick Lee                           #
#Date of creation: 11/2/19                  #
#===========================================#
#Instructions for use:                      #
#

#import elements
from time import sleep
valence = valence
elist = pairings
elecone = 0
electwo = 0

def pgebreak():
    print(" ")

def begin():
    pgebreak()
    verdict = input("Press c to calculate, or press q to quit. ")
    if verdict == "c":
         start()
    elif str(verdict) == "q":
        #sleep(1)
        print(" ")
        print("Goodbye!")
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
        print("These atoms can form a covalent bond.")
        #sleep(1)
        pgebreak()
        covcharge(x - 8)
        
    elif (x + y) == 8:
        print("These elements can form an ionic bond.")
        #sleep(1)
        pgebreak()
        if (x - 8) < (y - 8):
            ioncharge(x2, y2)
        else:
            ioncharge(y2, x2)
        
    else:
        print("I can't find any bonds in these atoms.")
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
          " atom with a charge of +" + str(valence[o]) + " and a "
          + elist[t][0] + " atom with a chage of " + str(valence[t] - 8))

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
        #sleep(1)
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
        #sleep(1)
        begin()
    else:
        print("Atom number one is " + elist[elecone][0] + " and atom number two is " + elist[electwo][0] + ".")
        #sleep(1)
        bond(elecone, electwo)

        begin()
        
begin()




