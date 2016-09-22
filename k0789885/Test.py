total = 0

ar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ar1 = ar[0]
ar2 = ar[1]
ar3 = ar[2]
ar4 = ar[3]
ar5 = ar[4]
ar6 = ar[5]
ar7 = ar[6]
ar8 = ar[7]
ar9 = ar[8]
ar10 = ar[9]
ar11 = ar[10]
ar12 = ar[11]
ar13 = ar[12]
ar14 = ar[13]
ar15 = ar[14]
ar16 = ar[15]
ar17 = ar[16]
ar18 = ar[17]
ar19 = ar[18]
ar20= ar[19]

            
            
            
            

ar1,ar2,ar3,ar4,ar5,ar6,ar7,ar8,ar9,ar10,ar11,ar12,ar13,ar14,ar15,ar16,ar17,ar18,ar19,ar20 = ar

for i in ar:
    if ar%2 == 0:
        total += ar
    else:
        if ar%5 == 0:
            print ("Checkpoint") + ar
        else:
            print ar 
            
print (total + ("- Total"))
