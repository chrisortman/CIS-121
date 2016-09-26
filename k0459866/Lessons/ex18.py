# R A N G E S  A N D  S O R T I N G
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