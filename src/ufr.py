#ufr(utility function require) is a list of funtion to show, input etc

def printArray(arr : list):
    for i in range(len(arr)):
        print(arr[i])
    

def inputArray():
    arrs = list(map(int, input().split(" ")))
    return arrs