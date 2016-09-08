from sys import argv # makes it so you can import text for a variable
script, x = argv # sets x = to whatever you type in
print "How old im I?" # prints text
#pls work
months = 12.0 # sets variable
weeks = 4.3 # sets variable
days = 7.0 # sets variable 
hours = 24.0 # sets variable
minutes = 60.0 # sets variable
seconds = 60.0 # sets variable

time = int(x) * months * weeks * days * hours *minutes *seconds


def calc_seconds(time):
    print "You are %d seconds old" % (time)
    
calc_seconds(time) 