print "How many days have I been alive?"   
days = 9 + 31 + 365 * 17 + 31 * 4+ 30 * 3 + 29
print "%s days" % (days)
print "How old am I?"
year = 365.25
print "I am %s years old" % round(days /year , 3)
