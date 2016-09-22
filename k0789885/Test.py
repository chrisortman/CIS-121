from sys import argv

script, filename = argv



txt = open(filename)

prompt = '> '

fingers = 8
toes = 10
corAns = round(8+10, 2)
myName = "Gage"
x = 0
file_again = ""



print "" #Blank line For seperating
print "" #Blank line For seperating
print "" #Blank line For seperating



print("Hay buddy, real quick I'm gonna invade your file %s.") % filename

print "" #Blank line For seperating

print txt.read()

print "" #Blank line For seperating

print "I don't think that worked, type the file name so I can try again:"

print "" #Blank line For seperating
        

while file_again != "MyGame.py":
    file_again = raw_input("> ")
    if file_again == "MyGame.py":
        print open(file_again)
    else:
        if x < 3:
            print "" #Blank line For seperating
            x = x + 1
            print ("That wasn't right buddy, try again.")
        else:
            print "" #Blank line For seperating
            print ("Come on, just type 'MyGame.py'.")



print "" #Blank line For seperating



print("Okay, so now that that's out of the way, what's your name?")
name = raw_input(prompt)

print "" #Blank line For seperating

if name == "Julian":
    print ("Hello %s, my name is %s") % (name, myName)
else:
    print ("Hello %s, how's football going? :)") % name



print "" #Blank line For seperating

print("How many fingers and toes do you have, minus your thumbs?\n")
ans = raw_input(prompt)

print "" #Blank line For seperating

def say_hi():
    print("Unfortunately %s, %s is most likely incorrect.") % (name, ans)

say_hi()

print "" #Blank line For seperating

print("The correct answer is displayed below, with the correct equationing and science.")

print "" #Blank line For seperating

print "8 Fingers + 10 Toes = %s in total." % corAns

print "" #Blank line For seperating

print "Thanks For Playing!"