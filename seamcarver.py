#!/usr/bin/env python3

from picture import Picture
import math, sys
import time

class SeamCarver(Picture):
    ## TO-DO: fill in the methods below
    def energy(self, i: int, j: int) -> float:
        '''
        Return the energy of pixel at column i and row j
        '''
        #does that pixel exist

        #Can be itterated using loops using i, j, and a constant a, just for testing purposes
        #checks if self[x_1,y] exists, else sets x to be i

        if i-1>=0:
            left_x=self[i-1,j]
        else: left_x=self[self._width-1,j]
        if i+1<=self._width-1:
            right_x=self[i+1,j]
        else: right_x=self[0,j]  
        if j-1>=0:
            up_y=self[i,j-1]
        else: up_y=self[i,self._height-1]  
        if j+1<=self._height-1:
            down_y=self[i,j+1]
        else: down_y=self[i,0]  
    
        R_x=left_x[0]-right_x[0]
        G_x=left_x[1]-right_x[1]
        B_x=left_x[2]-right_x[2]
        R_y=up_y[0]-down_y[0]
        G_y=up_y[1]-down_y[1]
        B_y=up_y[2]-down_y[2]

        # print(left_x, right_x , up_y, down_y, R_x , G_x, B_x, R_y , G_y, B_y)

        # print(R_x, G_x, B_x, R_y, G_y, B_y, R_x**2+G_x**2+B_x**2+R_y**2+G_y**2+B_y**2)
        
        energy=math.sqrt(R_x**2+G_x**2+B_x**2+R_y**2+G_y**2+B_y**2)

        
        return energy
        
        raise NotImplementedError

    def find_vertical_seam(self) -> list[int]:
        '''
        Return a sequence of indices representing the lowest-energy
        vertical seam
        '''
        
        print(self.energy(1,0))

        
        start_time = time.time()
        vertical_seam=dict()
        memoization=dict()
        w=0
        q=sys.maxsize
        #Energy Inefficient Method
        def M(i,j):
            energypath=0
            if i<0: i=0
            if i>self._width-1: i=self._width-1
            if j==0:
                energypath=self.energy(i,j)
            else:
                energypath=self.energy(i,j) + min(M(i-1,j-1),M(i,j-1),M(i+1,j-1))
            return energypath
        
        while w < self._width: 
            q=min(q,M(w,self._height-1))
            w+=1

        def vertical_seam_memoization(i,j, memoization):
            for a in range(self._width):
                for b in range(self._height):
                    memoization[a,b]=sys.maxsize
            return VS(i,j,memoization)

        def VS(i,j, memoization):

            if i<0: 
                i=0
            if i>self._width-1:
                i=self._width-1
            if memoization[i,j]<sys.maxsize:
                return memoization[i,j]
            energypath=0
            if j<=0:
                
                energypath=self.energy(i,j)
                print("energypathcalled")
            else:
                energypath=sys.maxsize
                energypath=self.energy(i,j) + min(VS(i-1,j-1, memoization),VS(i,j-1, memoization),VS(i+1,j-1, memoization))
            memoization[i,j]=energypath
            vertical_seam[i,j]=energypath

            return energypath
        w=0
        lnbro=sys.maxsize
        while w < self._width: 
            lnbro=min(lnbro,vertical_seam_memoization(w, self._height-1, vertical_seam))
            w+=1
        
        k=0

        while k<self._height:
            print(self.energy(0,k), self.energy(1,k), self.energy(2,k)) #self.energy(3,k), self.energy(4,k), self.energy(5,k)
            k+=1
        
        #tests
        print(math.sqrt(52020))
        print(M(0,0))
        print(vertical_seam_memoization(0,0,memoization))
        print(M(0,1))
        print(vertical_seam_memoization(0,3,memoization))
        print(self.energy(0,0)+self.energy(0,1)+self.energy(0,2)+self.energy(0,3))
        print(q)
        print(lnbro)
        print(vertical_seam)
        print("--- %s seconds ---" % (time.time() - start_time))
        return vertical_seam
    
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



