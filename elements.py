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
# [5,6,8,9,10,11,]

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
    
#print (valence, len(group), len(valence))

