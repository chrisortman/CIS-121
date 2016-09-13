from sys import argv #imports argv to the program

script, y, m, t = argv #makes variables script, y, m, and t argvs

#statement = "You are" #start of the output
hours_in_a_day = 24 #hours in one Earth day
hours_in_year = 365 * hours_in_a_day #hours in one Earth year
#h = "hours old" #statement that will be used to end the output

#y = input("How old in years are you? ") #prompts the user to input their age in years.
#m = input("How many days has it been since your last birthday? ") #237 #prompts the user to input the number of days since their last birthday
#t = input("How many hours has it been since midnight? ") #prompts the user to input how many hours it has been since midnight

y = int(y) #converts y into and Integer
m = int(m) #converts m into and Integer
t = int(t) #converts t into and Integer

def calc_hours_old(y, m, t): #defines the function calc_hours_old and states the necessary inputs
    hours_old = y * hours_in_year + m * hours_in_a_day + t #calculates how old the user is in hours
    print "You are %d hours old" % hours_old #calculates how old the user is in hours and then prints it out

calc_hours_old(y, m, t) #runs the function calc_hours_old
