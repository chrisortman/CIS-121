
# Do something with math!

print "What time is it?"

t = input('Enter the hour... ')
k = input('Enter the minute(s)... ')

print "What time will it be in an hour and 10 minutes?"

if (70 + k) > 60:
    if (10+k)%60 < 10:
        h = t + 2
        print h,":",0,(10+k)%60,"PM","Contingent"
    else:
        h= t + 1
        print h,":",(10+k)%60,"PM"

print "What time will it be in 2 hours and 20 minutes?"

if (80+k) > 60:
    if (20+k)%60 < 10:
        h = t + 3
        print h,":",0,(20+k)%60,"PM","Contingent"
    else:
        h = t + 2
        print h,":",(20+k)%60,"PM"

print "What time will it be in 3 hours and 30 minutes?"

if (90+k) > 60:
    if (30+k)%60 < 10:
        h = t + 4
        print h,":",0,(30+k)%60,"PM","Contingent"
    else:
        h = t + 3
        print h,":",(30+k)%60,"PM"
