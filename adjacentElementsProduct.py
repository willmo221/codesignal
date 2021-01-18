inputArray = [1,2,7,3,9,4,6]

def adjacentElementsProduct(inputArray):
    max = inputArray[0] * inputArray[1]
    for i in range(len(inputArray) - 1):
        if inputArray[i] * inputArray[i+1] > max:
            max = inputArray[i] * inputArray[i+1]
    print(max)

adjacentElementsProduct(inputArray)