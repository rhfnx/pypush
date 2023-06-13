randomArray = [1,12,4,6,9,7,8,3,2,46]

def bubbleSort(array):
    length = len(array)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0,length):
            if array[i] > array[i+1]:
                sorted = False
                array[i],array[i+1] = array[i+1],array[i]
    return array

print(bubbleSort(randomArray))