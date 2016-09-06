print "This program will calculate your age."

#print "What year where you born?"
born = int(raw_input("What year where you born?\n"))

#print "What's the current year?"
year = int(raw_input("What's the current year?\n"))

age = year - born

print "So you where born in %r?" % born
print "And the current year is %r?" % year
print "That would mean you're %r!" % age

if age >= 18:
    print "You're an adult, aren't you?"
else:
    print "You'll be 18 soon."