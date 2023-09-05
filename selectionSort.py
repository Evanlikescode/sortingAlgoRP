
def selectionSort(data):
    for i in range(0, len(data) - 1):
        min_data = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_data]:
                min_data = j
            temp = data[i]
            data[i] = data[min_data]
            data[min_data] = temp
    print(data)

data = [10,9,8,7,5]

selectionSort(data)