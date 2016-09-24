total = 0
numbers = range(1,21)


for num in numbers:
    
    if num % 2 == 0:
        total = total + num
        
    elif num % 5 == 0:
        print "Checkpoint %d" %num
        
print total, "- Total"