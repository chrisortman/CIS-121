def bubblesort(aList):
    for num in range(len(aList) - 1, 0, -1):
        for i in range(num):
            if aList[i] > aList[i+1]:
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp

list_1 = [54,26,93,17,77,31,44,55,20]
bubblesort(list_1)
print list_1