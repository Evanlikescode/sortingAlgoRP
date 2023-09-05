

def bubbleSort(data):
    for i in range(len(data)):
        ada_pertukaran = False
        for j in range(0, len(data) - i - 1):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
                ada_pertukaran = True
        if ada_pertukaran == False:
            print(data)
            break


data = [10,9,8,7,5]
# [9,10,8,7,5] - 0
# [9,8,10,7,5] - 1
# [9,8,7,10,5] - 2
# [9,8,7,5,10] - 3

# [8,9,7,5,10] - 0
# [8,7,9,5,10] - 1
# [8,7,5,9,10] - 2

# [7,8,5,9,10] - 0
# [7,5,8,9,10] - 1

# [5,7,8,9,10] - 0

bubbleSort(data)