
from sys import argv
#script, num = argv



zero = { 0 : " -- ",
         1 : "|  |",
         2 : "|  |",
         3 : "    " ,
         4 : "|  |",
         5 : "|  |",
         6 : " -- " }

one = { 0 : "   ",
        1 : "  |",
        2 : "  |",
        3 : "   ",
        4 : "  |",
        5 : "  |",
        6 : "   " }

two = { 0 : " -- ",
        1 : "   |",
        2 : "   |",
        3 : " -- ",
        4 : "|   ",
        5 : "|   ",
        6 : " -- " }

three = { 0 : " -- ",
          1 : "   |",
          2 : "   |",
          3 : " -- ",
          4 : "   |",
          5 : "   |",
          6 : " -- " }

four = { 0 : "    ",
         1 : "|  |",
         2 : "|  |",
         3 : " -- ",
         4 : "   |",
         5 : "   |",
         6 : "    " }

five = { 0 : " -- ",
        1 : "|   ",
        2 : "|   ",
        3 : " -- ",
        4 : "   |",
        5 : "   |",
        6 : " -- " }

six = { 0 : " -- ",
        1 : "|   ",
        2 : "|   ",
        3 : " -- ",
        4 : "|  |",
        5 : "|  |",
        6 : " -- " }

seven = { 0 : "-- ",
          1 : "  |",
          2 : "  |",
          3 : "   ",
          4 : "  |",
          5 : "  |",
          6 : "   " }

eight = { 0 : " -- ",
          1 : "|  |",
          2 : "|  |",
          3 : " -- ",
          4 : "|  |",
          5 : "|  |",
          6 : " -- " }

nine = { 0 : " -- ",
         1 : "|  |",
         2 : "|  |",
         3 : " -- ",
         4 : "   |",
         5 : "   |",
         6 : "    " }

num = raw_input("Enter 10 digits: ")
numList = []
number = num
orion = len(num)
mouse = 0

for i in number:
    if i == "0":
        numList.append(zero)
    elif i == "1":
        numList.append(one)
    elif i == "2":
        numList.append(two)
    elif i == "3":
        numList.append(three)
    elif i == "4":
        numList.append(four)
    elif i == "5":
        numList.append(five)
    elif i == "6":
        numList.append(six)
    elif i == "7":
        numList.append(seven)
    elif i == "8":
        numList.append(eight)
    elif i == "9":
        numList.append(nine)
    
    
        
        
            
            #print zero[mouse], one[mouse], two[mouse], three[mouse], four[mouse], five[mouse], six[mouse], seven[mouse], eight[mouse], nine[mouse]


dog = 0
while dog < 7:
    print numList[0][dog], numList[1][dog]
    
print len(numList)



"""

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a1, a2 = " ", " ", " ",\
" ", " ", " "," ", " ", " "," ", " ", " "," ", " ", " "," ", " ", " "," ", " ", " "," ", " ", " ",\
" ", " ", " "," "

a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1, m1, n1, o1, p1, q1, r1, s1, t1,\
u1, v1, w1, x1, y1, z1, a2, a3 = " ", " ", " "," ", " ", " "," ", " ", " "," ",\
" ", " "," ", " ", " "," ", " ", " "," ", " ", " "," ", " ", " "," ", " ", " ", " "

#if num == "7":
 #   b, c, h, l, t, x = "-", "-", "|", "|", "|", "|"

col1 = { 0 : a, 1 : e, 2 : i, 3 : m, 4 : q, 5 : u, 6 : y } 
col2 = { 0 : b, 1 : f, 2 : j, 3 : n, 4 : r, 5 : v, 6 : z } 
col3 = { 0 : c, 1 : g, 2 : k, 3 : o, 4 : s, 5 : w, 6 : a1 } 
col4 = { 0 : d, 1 : h, 2 : l, 3 : p, 4 : t, 5 : x, 6 : a2 } 

col5 = { 0 : a1, 1 : e1, 2 : i1, 3 : m1, 4 : q1, 5 : u1, 6 : y1 } 
col6 = { 0 : b1, 1 : f1, 2 : j1, 3 : n1, 4 : r1, 5 : v1, 6 : z1 } 
col7 = { 0 : c1, 1 : g1, 2 : k1, 3 : o1, 4 : s1, 5 : w1, 6 : a2 } 
col8 = { 0 : d1, 1 : h1, 2 : l1, 3 : p1, 4 : t1, 5 : x1, 6 : a3 } 

def one1():
    col4[1], col4[2], col4[4], col4[5] = "|", "|", "|", "|"
   
def one2():
    col8[1], col8[2], col8[4], col8[5] = "|", "|", "|", "|" 
    
def two():
    col2[0], col3[0], col4[1], col4[2], col2[3], col3[3], col1[4], col1[5], col2[6], col3[6] = "-",\
    "-", "|", "|", "-","-", "|", "|", "-", "-"

def three():
    col2[0], col3[0], col4[1], col4[2], col2[3], col3[3], col4[4], col4[5], col2[6], col3[6] = "-",\
    "-", "|", "|", "-","-", "|", "|", "-", "-"
    
def four():
    col1[0], col4[0], col1[1], col4[1], col2[2], col3[2], col4[3], col4[4]  = "|", "|", "|", "|", "-", "-", "|", "|"
    

    
    
def letter():
    col2[0], col3[0], col1[1], col4[1] = "-", "-", "|", "|"
    
user = num
spot = []
for i in user:
    spot.append(i)
print spot
mouse = 0
while mouse < 7:
    
    for h in spot:
        if h == "1":
            one1(), one2()
        elif h == "2":
            two(), one2()
        elif h == "b":
            letter()
        elif h == "3":
            three()
        elif h == "4":
            four()
    
            
        
    print col1[mouse], col2[mouse], col3[mouse], col4[mouse],\
    col5[mouse], col6[mouse], col7[mouse], col8[mouse]
    mouse += 1       


##################
mouse = 0
#while len(num) < 7:
    
#for i in x:
    
    #sphere.append(x)   
    #print sphere
#print col1[mouse], col2[mouse], col3[mouse], col4[mouse]
#mouse += 1

            col4[1], col4[2], col4[4], col4[5] = "|", "|", "|", "|"
            
            
            
        elif num == "2":
            col2[0], col3[0], col4[1], col4[2], col2[3], col3[3], col1[4], col1[5], col2[6], col3[6] = "-",\
            "-", "|", "|", "-","-", "|", "|", "-", "-"
            print col1[mouse], col2[mouse], col3[mouse], col4[mouse]
            mouse += 1


     
b = num
j = []
for i in b:
    print i
    j.append(i)   
print j

    
"""



    




        
            
    
    
