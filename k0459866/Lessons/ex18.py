# R A N G E S  A N D  S O R T I N G
#RANGES
nums = range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = range(0,10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = range(0,10,2)
[0, 2, 4, 6, 8]
nums = range(10,0,-1)
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
nums = range(10,0)
[]
################################################################################
#BUBBLE SORTING EXAMPLE
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
################################################################################
#OWN TYPED SORTING
def firstSort(list_1):
    for passnum in range(len(list_1)-1,0,-1):
        for i in range(passnum):
            if list_1[i]>list_1[i+1]:
                temp = list_1[i]
                list_1[i] = list_1[i+1]
                list_1[i+1] = temp

list_1 = [1,84,4,36,3,134,124,44,10,52,72,12,42,76,33]
firstSort(list_1)
print(list_1)