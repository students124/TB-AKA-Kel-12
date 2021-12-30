# importing the required module
import timeit
import numpy as np
import pandas as pd
from src.BubbleSort import bubbleSort
from src.RadixSort import countingSort, radixSort
from src.ufr import printArray,inputArray
from src.plot import makePlot


def main():
    arr10 = list(np.random.randint(low=1, high=1000, size=10))
    arr100 = list(np.random.randint(low=1, high=1000, size=100))
    arr1000 = list(np.random.randint(low=1, high=1000, size=1000))
    arr10000 = list(np.random.randint(low=1, high=1000, size=10000))
    arr100000 = list(np.random.randint(low=1, high=1000, size=100000))    

    #n = 10 for radix
    rn10 = timeit.timeit(lambda : radixSort(arr10))

    #n = 100 for radix
    rn100 = timeit.timeit(lambda : radixSort(arr100))

    #n = 1000 for radix
    rn1000 = timeit.timeit(lambda : radixSort(arr1000))

    #n = 10000 for radix
    rn10000 = timeit.timeit(lambda : radixSort(arr10000))

    # #n = 1000 for radix
    rn100000 = timeit.timeit(lambda : radixSort(arr100000))

    #n = 10 for bubble
    dn10 = timeit.timeit(lambda : bubbleSort(arr10))

    #n = 100 for bubble
    dn100 = timeit.timeit(lambda : bubbleSort(arr100))

    # #n = 1000 for bubble
    dn1000 = timeit.timeit(lambda : bubbleSort(arr1000))

    # # #n = 10000 for bubble
    dn10000 = timeit.timeit(lambda : radixSort(arr10000))

    # # #n = 100000 for bubble
    dn100000 = timeit.timeit(lambda : radixSort(arr100000))


    # corresponding y axis values for radix
    x1 = [10,100,1000,10000,100000]
    # x axis values for radix
    y1 = [rn10,rn100,rn1000,rn10000,rn10000]

    # corresponding y axis values for bubble
    x2 = [10,100,1000,10000,100000]
    # x axis values for radix for bubble
    y2 = [rn10,rn100,rn1000,rn10000,rn100000]

    df = pd.DataFrame({
        "Data" : x1,
        "Radix" : y1,
        "Bubble" : y2
    })

    print(df)
    makePlot(x1,y1,x2,y2,"Data n", "Running Time", "Radix VS Bubble")

    

if __name__ == '__main__':
    main()