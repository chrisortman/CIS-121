"""
Bryant Conquest
This calculates the distance of a storm
9/16
"""

####Imports
imp

####Prompts
"""All the prompts and variables"""
intro = "This program will calcule the distance of a storm."
intro2 = "Press q to exit the program or press n to keep going."
choiceq = ("What would you like to do? ")
distance = 0
output_1 = "The storm is"
output_2 = "miles away"
seconds = int(sys.argv[1])

####functions
def what_to_do():
    print intro
    print intro2
    print choiceq
def yes():
    distance = seconds/5.00
    count = 0
    while count < 1:
        print output_1,
        print distance,
        print output_2
        count = count + 1
    

####Main
while True:
    what_to_do()
    choicea = raw_input()
    if choicea == "n":
        yes()
    elif choicea == "q":
        break