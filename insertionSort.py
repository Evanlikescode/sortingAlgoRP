
def insertionSort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j = j - 1

        data[j+1] = key
        print(data)

data = [10,9,8,7,5]
insertionSort(data)
