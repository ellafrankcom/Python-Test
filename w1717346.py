#Ella Frankcom w1717346
"""
This is induvidual work of my own
4th March 2021
"""

import math
import numpy as np

class Polybase:
    def __init__(self, nv = 2): #initialize variables
        self.nv = nv

    def coord(self, list1 = [][]): #create 2d list of blank spaces
        self.list1 = list1
        for i in range nv:
            for j in range nv:
            list1[i][j] = " "

    def set_coord(self, x, y): #prompt user for values
        x = int(input("Please input your x values, seperated by a space: ")
        y = int(input("Please input your y values, seperated by a space: ")
        self.x = x
        self.y = y
        for i in x.split(): #add values to list using user input, seperated by split
            for j in y.split():
                self.list1.append(int(i), int(j))

    def get_coord(self):  #returns list
        return self.list1

    def get_vert(self): #returns number of co-ordinates
        return self.nv


class Geomov:
    def __init__(self, theta = 0.0, mag = 1, unit): #initilize variables
        self.theta = theta
        self.mag = mag
        self.units = math.degrees(unit)

    def set_mag(self, mag): #set the scale using user input
        self.mag = float(input("Input the scale of the matrix: ")


    def set_thetad(self, theta): #set theta to degrees
        self.theta = theta*(math.pi/180)

    def set_thetar(self, theta):  #set theta to radians
        self.theta = math.radians(theta)

    def get_thetad(self): #return theta in degrees
        return math.degrees(self.theta)

    def get_thetar(self): #return theta in radians
        return math.radian(self.theta)

    def get_mad(self): #return scale
        return self.mag

    def multmat(self, rotmat, coordmat, vert, theta, x, y, list1): #creating and multplying the matrices
        x, y = np.cos(theta), np.sin(theta)
        self.rotmat = np.array(((x, -s), (y, c))) #rotating matrix
        self.coordmat = coordmat
        self.vert = vert
        vert = int(input("input number of vertices") #user inputs number of vertices
        
        if rotmat[i][].length == list1[][i]:
            #Multiply the matrices
            for k in range(rotmat[i][]):
                for i in range(list1[][j]):
                    for j in range(rotmat[][j]):
                        self.coordmat = [i][j] += rotmat[i][k] * list1[k][j]
            
            #Display multiplies
            print("coordmat:")
            for i in range(list1[i][]):
                for j in range(rotmat[][j]):
                    print("{:7.3f}".format(coordmat[i][j]),end=" ")
                
        else:
            print("Wrong Dimension ")
        
    def rot_geo(self, theta, rotnat, x, y):
        x, y = np.cos(theta), np.sin(theta)
        self.rotmat = np.array(((x, -s), (y, c))) #rotating matrix

        if rotmat[i][].length == list1[][i]:  #multiplying the matrices
            #Multiply the matrices
            for k in range(rotmat[i][]):
                for i in range(list1[][j]):
                    for j in range(rotmat[][j]):
                        self.coordmat = [i][j] += rotmat[i][k] * list1[k][j]
            
            #Display multiplies
            print("coordmat:")
            for i in range(list1[i][]):
                for j in range(rotmat[][j]):
                    print("{:7.3f}".format(coordmat[i][j]),end=" ")
            return self.coordmat
                
        else:
            print("Wrong Dimension ")

        
    def scale_geo(self, mag, multmat()):
        #build a new matrix buy multiplying 2 together using another method
        self.mag = mag
        multmat(mag)
        return self.coordmat #return new matrix
        
                

class poly(Polybase, Geomov): #inherit from other classes
    def ___init__(self, Polybase, Geomov):
        super().__init__(nv, list1, coordmat, mag, rotmat, theta, x, y, vert, unit)

    def conCoor(self, x, y, coordmat):
        x = int(input("Please input your x values, seperated by a space: ")
        y = int(input("Please input your y values, seperated by a space: ")
        self.x = x
        self.y = y
        for i in x.split(): #add values to list using user input, seperated by split
            for j in y.split():
                self.list1.append(int(i), int(j))
                self.coordmat = self.list1

    def display_coor(self, Polybase):
        return self.nv
        return x, y

    def rotpoly(self, rot_geo()):
        return self.coordmat

    def rescalepoly(self, scale_geo):
        return self.coordmat
        

a= poly(4)
print(a.get_coord())
a.display_coor()
a.set_thetad(45)
a.rotpoly()
a.display_coor()
a.set_mag(2)
a.rescalepoly()
a.display_coor()
        
        
