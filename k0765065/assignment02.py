statement = "You are"
days_in_a_year = 365
hours_in_a_day = 24
h = "hours old"

y = input("How old in years are you? ")
m = input("How many days has it been since your last birthday? ")
t = input("How many hours has it been since midnight? ")

print statement, y * days_in_a_year * hours_in_a_day + m * hours_in_a_day + t, h
