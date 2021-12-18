# importing the required module
import timeit
import numpy as np
from src.BubbleSort import bubbleSort
from src.RadixSort import countingSort, radixSort
from src.ufr import printArray,inputArray
from src.plot import makePlot


def main():
    # arr10 = random.sample(range(1,1000), 10)
    arr10 = list(np.random.randint(low=1, high=1000, size=10))
    # arr100 = list(np.random.randint(low=1, high=1000, size=100))
    # arr1000 = list(np.random.randint(low=1, high=1000, size=1000))
    # arr10000 = list(np.random.randint(low=1, high=1000, size=10000))
    # arr100000 = list(np.random.randint(low=1, high=1000, size=100000))    

    #n = 10 for radix
    rn10 = timeit.timeit(lambda : radixSort(arr10), number=1)
    #n = 100 for radix
    rn100 = timeit.timeit(lambda : radixSort(arr10), number=10)
    #n = 1000 for radix
    rn1000 = timeit.timeit(lambda : radixSort(arr10), number=100)
    #n = 10000 for radix
    rn10000 = timeit.timeit(lambda : radixSort(arr10), number=1000)
    #n = 1000 for radix
    rn100000 = timeit.timeit(lambda : radixSort(arr10), number=10000)

    #n = 10 for bubble
    dn10 = timeit.timeit(lambda : bubbleSort(arr10),number=1)
    #n = 100 for bubble
    dn100 = timeit.timeit(lambda : bubbleSort(arr10),number=10)
    #n = 1000 for bubble
    dn1000 = timeit.timeit(lambda : bubbleSort(arr10),number=100)
    #n = 10000 for bubble
    dn10000 = timeit.timeit(lambda : radixSort(arr10),number=1000)
    #n = 100000 for bubble
    dn100000 = timeit.timeit(lambda : radixSort(arr10),number=10000)


    # x axis values for radix
    x1 = [rn10, rn100, rn1000,rn10000,rn100000]
    # corresponding y axis values for radix
    y1 = [10,100,1000,10000,100000]

    # x axis values for radix for bubble
    x2 = [dn10,dn100,dn1000,dn10000,dn100000]
    # corresponding y axis values for bubble
    y2 = [10,100,1000,10000,100000]

    makePlot(x1,y1,x2,y2, "Running Time", "Input Size", "Radix VS Bubble")
    

if __name__ == '__main__':
    main()