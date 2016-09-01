Year = 365.25
ShDays = 29.00
Name = "Gage"

print "Hi my name is %s" % Name
print ""

x = input("How many months are in a Year if all months were 29 days long?\n")
print "" #Blank line For seperating
print "365 / 29 = %d" % round(Year/ShDays, 2)