# importing the required module
from src.BubbleSort import bubbleSort
from src.RadixSort import countingSort, radixSort
from src.ufr import printArray,inputArray
from src.plot import makePlot

def main():
    # x axis values for radix
    x1 = [1,2,3]
    # corresponding y axis values for radix
    y1 = [2,4,1]

    # x axis values for radix for bubble
    x2 = [4,5,6]
    # corresponding y axis values for bubble
    y2 = [4,8,2]

    makePlot(x1,y1,x2,y2)
    

if __name__ == '__main__':
    main()