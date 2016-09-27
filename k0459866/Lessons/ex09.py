from sys import argv
birthyear = input("What year where you born?\n")

script, birthyear = argv
birthyear = int(birthyear)

def calc_age(birthyear):
    print "You are %d years old" % (2016 - birthyear)

calc_age(birthyear)