# importing the required module
import matplotlib.pyplot as plt
from src.BubbleSort import bubbleSort
from src.RadixSort import countingSort, radixSort
from src.ufr import printArray

def makePlot():
    # x axis values
    x = [1,2,3]
    # corresponding y axis values
    y = [2,4,1]
    
    # plotting the points
    plt.plot(x, y)
    
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    
    # giving a title to my graph
    plt.title('My first graph!')
    
    # function to show the plot
    plt.show()


def main():
    makePlot()
    

if __name__ == '__main__':
    main()