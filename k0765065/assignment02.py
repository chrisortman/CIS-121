from sys import argv

script, y, m, t = argv

#statement = "You are" #start of the output
hours_in_a_day = 24 #hours in one Earth day
hours_in_year = 365 * hours_in_a_day #hours in one Earth year
#h = "hours old" #statement that will be used to end the output

#y = input("How old in years are you? ") #prompts the user to input their age in years.
#m = input("How many days has it been since your last birthday? ") #237 #prompts the user to input the number of days since their last birthday
#t = input("How many hours has it been since midnight? ") #prompts the user to input how many hours it has been since midnight

y = int(y)
m = int(m)
t = int(t)

def calc_hours_old(y, m, t):
    hours_old = y * hours_in_year + m * hours_in_a_day + t
    print "You are %d hours old" % hours_old #calculates how old the user is in hours and then prints it out

calc_hours_old(y, m, t)
