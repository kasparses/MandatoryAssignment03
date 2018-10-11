
def fibonacci(n):
    fibonacciList = [1, 1]
    
    currentNum = 0
    precedingNum1 = 1
    precedingNum2 = 1
    
    if (n > 2):
        for i in range(0, n-2):
            
            currentNum = precedingNum1 + precedingNum2
            fibonacciList.append(currentNum)
            precedingNum2 = precedingNum1
            precedingNum1 = currentNum
    
    return fibonacciList

print(fibonacci(10))


    