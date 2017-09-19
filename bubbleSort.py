# Bubble Sort algorithm

def bubbleSort (jakesList):
    for i in range (0, len(jakesList) - 1):
        for j in range (0, len(jakesList) - 1 - i):
            if jakesList[j] > jakesList[j + 1]:
                jakesList[j], jakesList[j + 1] = jakesList[j + 1], jakesList[j]
    return jakesList

theList = [3, 77, 33, 2, 99, 54, 22, 1, 444, 666, 333, 222, 878, 345, 934, 234, 13]
print (bubbleSort(theList))

# [1, 2, 3, 13, 22, 33, 54, 77, 99, 222, 234, 333, 345, 444, 666, 878, 934]
