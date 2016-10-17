def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp

alist = [532, 232, 22314, 1, 9, 3, 5, 6, 8, 7, 8, 45]
bubbleSort(alist)
print(alist)