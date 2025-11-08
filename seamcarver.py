#!/usr/bin/env python3

from picture import Picture
import math

class SeamCarver(Picture):
    ## TO-DO: fill in the methods below
    def energy(self, i: int, j: int) -> float:

       
        


        '''
        Return the energy of pixel at column i and row j
        '''

        #Can be itterated using loops using i, j, and a constant a, just for testing purposes
        #checks if self[x_1,y] exists, else sets x to be i

        try:
            X_1=self[i+1,j] 
        except KeyError:
            X_1=self[i,j]
        try:
            X_2=self[i-1,j] 
        except KeyError:
            X_2=self[i,j] 
        try:
            Y_1=self[i,j+1] 
        except KeyError:
            Y_1=self[i,j]
        try:
            Y_2=self[i,j-1] 
        except KeyError:
            Y_2=self[i,j] 

        R_x=X_1[0]-X_2[0]
        G_x=X_1[1]-X_2[1]
        B_x=X_1[2]-X_2[2]
        R_y=Y_1[0]-Y_2[0]
        G_y=Y_1[1]-Y_2[1]
        B_y=Y_1[2]-Y_2[2]


        print(R_x, G_x, B_x, R_y, G_y, B_y, R_x**2+G_x**2+B_x**2+R_y**2+G_y**2+B_y**2)
        
        energy=math.sqrt(R_x**2+G_x**2+B_x**2+R_y**2+G_y**2+B_y**2)

        
        return energy
        
        raise NotImplementedError

    def find_vertical_seam(self) -> list[int]:
        '''
        Return a sequence of indices representing the lowest-energy
        vertical seam
        '''

        print(self.energy(0,2))

        raise NotImplementedError

    def find_horizontal_seam(self) -> list[int]:
        '''
        Return a sequence of indices representing the lowest-energy
        horizontal seam
        '''

        print(self[0,0])
        
        raise NotImplementedError

    def remove_vertical_seam(self, seam: list[int]):
        '''
        Remove a vertical seam from the picture
        '''
        raise NotImplementedError

    def remove_horizontal_seam(self, seam: list[int]):
        '''
        Remove a horizontal seam from the picture
        '''
        print(self.get(0,0))

        raise NotImplementedError

class SeamError(Exception):
    pass



