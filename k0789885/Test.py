from sys import argv

script, filename = argv

txt = open(filename)

prompt = '> '

year = 365.25
shDays = 29.00
corAns = round(year/shDays, 2)
myName = "Gage"



print "" #Blank line For seperating
print "" #Blank line For seperating
print "" #Blank line For seperating



print("Hay buddy, real quick I'm gonna invade your file %s.") % filename

print "" #Blank line For seperating

print txt.read()

print "" #Blank line For seperating

print "I don't think that worked, type the file name so I can try again:"

print "" #Blank line For seperating








def typefile():
    file_again = raw_input("> ")
    if file_again == "me.txt":
        return open(file_again)
    else:
        print "" #Blank line For seperating
        print "" #Blank line For seperating
        return typefile()
        
typefile()








print "" #Blank line For seperating



print("Okay, so now that that's out of the way, what's your name?")
name = raw_input(prompt)

print "" #Blank line For seperating

print ("Hello %s, my name is %s") % (name, myName)

print "" #Blank line For seperating

print("How many months are in a Year if all months were 29 days long?\n")
ans = raw_input(prompt)

print "" #Blank line For seperating

def say_hi():
    print("Unfortunately %s, %s days is most likely incorrect.") % (name, ans)

say_hi()

print "" #Blank line For seperating

print("The correct answer is displayed below, with the correct equationing and science.")

print "" #Blank line For seperating

print "365 Days / 29 Days = %s Months (Rounded)." % corAns

print "" #Blank line For seperating

print "Thanks For Playing!"