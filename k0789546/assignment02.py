from sys import argv

print "Set the year you were born as an arguement"

script, birthyear = argv
#years = input("What year were you born:\n")  
age = 2016 - int(birthyear)
days = 365.25
daysTotal = age * days

print "You are %s years old, and you have been alive for %s days" % (age, daysTotal)
print "The program you are running is called %s" % script






