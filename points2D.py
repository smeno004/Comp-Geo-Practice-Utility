import matplotlib.pyplot as plt

########################################################
# Class Name    :   Points2D
# Properties    :   pointsList (list of (x,y) points)
#
# Functions     :   AddPointsGraphical2D - Visual utility
#                       to add points to pointsList
#                   AddPointsCMD2D - Textual utility to
#                       add points to pointsList
#                   clearBoard - removes all the points
#                   setGrid - sets grid limits to user input
#                   viewPoints - outputs the points list
#                       and its visual representation
#
# Description   :   Base class to handle the 2D points
#                   list and run different algorithms
########################################################
class Points2D:
    def __init__(self, pL=[], gxmin=0, gxmax=10, gymin=0, gymax=10):
        self.pointsList = pL
        self.grid_xmin = gxmin
        self.grid_xmax = gxmax
        self.grid_ymin = gymin
        self.grid_ymax = gymax

    def clearBoard(self):
        self.pointsList = []

    def setGrid(self):
        gxmin = float(input("Grid X Min: > "))
        gxmax = float(input("Grid X Max: > "))
        gymin = float(input("Grid Y Min: > "))
        gymax = float(input("Grid Y Max: > "))

        self.grid_xmin = gxmin
        self.grid_xmax = gxmax
        self.grid_ymin = gymin
        self.grid_ymax = gymax

    def viewPoints(self):
        print (self.pointsList)

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlim([self.grid_xmin, self.grid_xmax])
        ax.set_ylim([self.grid_ymin, self.grid_ymax])

        if (self.pointsList != []):
            plt.scatter(*zip(*self.pointsList))
        
        plt.grid(b=True)
        plt.show()

        input("Press <Enter> to continue: \n> ")

    def AddPointsGraphical2D(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlim([self.grid_xmin, self.grid_xmax])
        ax.set_ylim([self.grid_ymin, self.grid_ymax])

        # Move left y-axis and bottim x-axis to centre, passing through (0,0)
        # ax.spines['left'].set_position('center')
        # ax.spines['bottom'].set_position('center')

        # Eliminate upper and right axes
        # ax.spines['right'].set_color('none')
        # ax.spines['top'].set_color('none')

        # Show ticks in the left and lower axes only
        # ax.xaxis.set_ticks_position('bottom')
        # ax.yaxis.set_ticks_position('left')

        def onclick(event):
            print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
                (event.button, event.x, event.y, event.xdata, event.ydata))

            self.pointsList.append(( round(event.xdata,2), round(event.ydata, 2) ))

            plt.plot(event.xdata, event.ydata, 'bo')
            fig.canvas.draw()

        def on_close(event):
            print('Done adding points...')

        fig.canvas.mpl_connect('button_press_event', onclick)
        fig.canvas.mpl_connect('close_event', on_close)

        plt.grid(b=True)
        plt.show()

    def AddPointsCMD2D(self):
        nP = int( input("Specify the number of points to be added: \n> ") )

        for i in range(nP):
            print ("{} :".format(i))
            x = float(input("\t X: > "))
            y = float(input("\t Y: > "))
            self.pointsList.append( (x,y) )

        input("Press <Enter> to continue: \n> ")
