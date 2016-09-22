week = 7
# days in a week

weekends = 2
# counts both days in a standard weekend

# vars (h = )
holidays = 16
# counts the days off in a holiday (manually put in)
months = 10
# establishes how many months are in the year
  
print weekends 
# now I'll make the program display the amount of days in the school year 
total = ((months * (4 * week)) - (months * (4 * weekends)) - holidays)

print "There will be %r days in the school year." % total
