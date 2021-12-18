import matplotlib.pyplot as plt

def makePlot(x1 : int,y1 : int,x2 : int,y2 : int):
    # plotting the points
    plt.plot(x1, y1)
    plt.plot(x2,y2)
    
    # naming the x axis
    plt.xlabel('Input Size')
    # naming the y axis
    plt.ylabel('Running time')
    
    # giving a title to my graph
    plt.title('Radix VS Bubble')
    
    # function to show the plot
    plt.show()