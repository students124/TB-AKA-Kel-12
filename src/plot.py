import matplotlib.pyplot as plt

def makePlot(x1 : int,y1 : int,x2 : int,y2 : int, xLabel : str, yLabel : str, title : str):
    # plotting the points
    plt.plot(x1, y1, color='r', label='Radix')
    
    plt.plot(x2,y2, color='g', label='Bubble')
    
    
    # naming the x axis
    plt.xlabel(xLabel)
    # naming the y axis
    plt.ylabel(yLabel)
    
    # giving a title to my graph
    plt.title(title)
    
    # giving a grid
    plt.grid()

    # showing all the legend mark
    plt.legend()

    # function to show the plot
    plt.show()