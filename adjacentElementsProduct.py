inputArray = [1,2,3,20,32,44]

def adjacentElementsProduct(inputArray):
    max = inputArray[0]
    highestnumber=0
    secondnumber=0
    for i in inputArray:
        if i > max:
            highestnumber = i
    for j in inputArray:
        if max < j:
            if j < highestnumber:
                secondnumber = j
    print(secondnumber,highestnumber)

adjacentElementsProduct(inputArray)