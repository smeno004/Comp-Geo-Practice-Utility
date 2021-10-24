# Library Imports
from os import system, name
from points2D import Points2D

########################################################
# Function Name :   clearScreen
# Parameters    :   -
# Description   :   Clears screen between menus and
#                   outputs
# Returns       :   -  
########################################################
def clearScreen():
    if name == 'nt':
        _ = system("cls")
    
    else:
        _ = system("clear")

########################################################
# Class Name    :   MainMenu
# Properties    :   menuOption - holds current menu option
#                   points2D - Points2D class object
#                   points3D - Points3D class object
#
# Functions     :   printStartMenu
#                   printMainMenu
#                   printAddMenu
#                   initMenu - Start Menu
#                   init2DMainMenu - Main Menu for 2D Utility
#                   init2DAddMenu - Add Points Menu for 2D
#
# Description   :   Class to handle the 2D points list
#                   and run different algorithms
########################################################
class MainMenu:
    def __init__(self, p2d=None, p3d=None):
        self.menuOption = -1
        self.points2D = p2d
        self.points3D = p3d

    def printStartMenu(self):
        clearScreen()
        print ("------------------------------------------")
        print ("--------------- Dimensions ---------------")
        print ("1 - 2D")
        print ("2 - 3D")
        print ("0 - Close Utility")
        print ("------------------------------------------")

    def printMainMenu(self):
        clearScreen()
        print ("-----------------------------------------")
        print ("--------------- Main Menu ---------------")
        print ("1 - Add Points")
        print ("2 - Set Grid")
        print ("3 - Algorithms")
        print ("4 - View Points")
        print ("5 - Clear Board")
        print ("0 - Go Back")
        print ("-----------------------------------------")

    def printAddMenu(self):
        clearScreen()
        print ("------------------------------------------")
        print ("--------------- Add Points ---------------")
        print ("1 - Visual")
        print ("2 - Command Line")
        print ("0 - Go Back")
        print ("------------------------------------------")

    def initMenu(self):
        while True:
            self.printStartMenu()
            self.menuOption = input("Enter Choice: \n> ")

            if (self.menuOption == '1'):
                print ("2D Utility")
                self.init2DMainMenu()
            elif (self.menuOption == '2'):
                print ("3D Utility")
            elif (self.menuOption == '0'):
                print ("Closing Utility")
                break
            else:
                print ("invalid option")

        return

    def init2DMainMenu(self):
        self.points2D = Points2D()

        while True:
            self.printMainMenu()
            self.menuOption = input("Enter Choice: \n> ")

            if (self.menuOption == '1'):
                print ("Adding Points")
                self.init2DAddMenu()
            elif (self.menuOption == '2'):
                print ("Set Grid")
                self.points2D.setGrid()
            elif (self.menuOption == '3'):
                print ("Algo")
            elif (self.menuOption == '4'):
                clearScreen()
                print ("View Points")
                self.points2D.viewPoints()
            elif (self.menuOption == '5'):
                print ("Clear board")
                self.points2D.clearBoard()
            elif (self.menuOption == '0'):
                print ("Go Back")
                break
            else:
                print ("invalid option")

        return

    def init2DAddMenu(self):
        clearScreen()

        while True:
            self.printAddMenu()
            self.menuOption = input("Enter Choice: \n> ")

            if (self.menuOption == '1'):
                self.points2D.AddPointsGraphical2D()
            elif (self.menuOption == '2'):
                self.points2D.AddPointsCMD2D()
            elif (self.menuOption == '0'):
                break
            else:
                print ("Invalid Option")

        return
