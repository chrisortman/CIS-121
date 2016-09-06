statement = "You are" #start of the output
days_in_a_year = 365 #days in one Earth year
hours_in_a_day = 24 #hours in one Earth day
h = "hours old" #statement that will be used to end the output

y = input("How old in years are you? ") #prompts the user to input their age in years.
m = input("How many days has it been since your last birthday? ") #235 #prompts the user to input the number of days since their last birthday
t = input("How many hours has it been since midnight? ") #prompts the user to input how many hours it has been since midnight

print statement, y * days_in_a_year * hours_in_a_day + m * hours_in_a_day + t, h #calculates how old the user is in hours and then prints it out
