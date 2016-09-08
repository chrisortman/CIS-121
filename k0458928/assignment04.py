#This line asks the user to input an integer that will be recorded as my age
my_age = input("Enter your age:")
#This line asks the user to input an integer that will be recorded as days_in_a_year
days_in_a_year = input("How many days are in a year?")

hours_in_a_day = 24
#This line tells you how many seconds you've been alive based on the recorded integers
print "how many seconds have i been alive?", my_age * days_in_a_year * hours_in_a_day * 60 * 60

black_cars = 8

red_cars = 6

print "What is the total number of black and red cars?", (black_cars + red_cars)

print "How many more black cars are there than red cars?", (black_cars - red_cars)