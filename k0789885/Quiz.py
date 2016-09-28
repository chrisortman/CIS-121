total = 0

for i in range(21):
    if i%2 == 0:
        total += i
    else:
        if i%5 == 0:
            print "Checkpoint: %s" % i
        else:
            print i 
            
print "%s - Total" % total