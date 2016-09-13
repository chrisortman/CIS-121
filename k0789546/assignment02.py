# imports the argv commands
from sys import argv

# prints the text to the user
print "Set your birth year as an arguement"

# assigns each arguement a name
script, birthyear = argv

# the input from the user gets changed to an "int" and gets the age by subtracting the input from 2016
age = 2016 - int(birthyear)

# assigns the number 365.25 to the variable "days"
days = 365.25

# multiplies the variable "age" and "days" to get the total number of days
daysTotal = age * days

#defines a function that takes one parameter
def years(b):
    
# concatenates the variable "age" and "daysTotal" into the text
    print "You are %s years old, and you have been alive for %s days" % (age, daysTotal)

# does the same thing as the line above but with the name of the script
    print "The program you are running is called %s" % script
   
# calls the function years with one arguement
years(birthyear)





