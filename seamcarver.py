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

        
        def energy(i: int,j: int):
            return self.energy(i,j)


        start_time = time.time()
        returned_seam=[]
        memoization=dict()
        w=0
        q=sys.maxsize
        #Energy Inefficient Method
        ''' def M(i,j):
            energypath=0
            if i<0: i=0
            if i>self._width-1: i=self._width-1
            if j==0:
                energypath=self.energy(i,j)
            else:
                energypath=self.energy(i,j) + min(M(i-1,j-1),M(i,j-1),M(i+1,j-1))
            return energypath
        '''
        ''' while w < self._width: 
            q=min(q,M(w,self._height-1))
            w+=1
        '''   

        '''
        #Energy Semi Efficient Method. 
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
            else:
                energypath=sys.maxsize
                energypath=self.energy(i,j) + min(VS(i-1,j-1, memoization),VS(i,j-1, memoization),VS(i+1,j-1, memoization))
            memoization[i,j]=energypath
            vertical_seam[i,j]=energypath

            return energypath
        w=0

        #use divide and countuer this 
        lnbro=sys.maxsize
        while w < self._width: 
            lnbro=min(lnbro,vertical_seam_memoization(w, self._height-1, vertical_seam))
            w+=1
        ''' 
        #Energy Efficient (Bottom Up Approach) Method. 
        energypath=0
        def arraybuilder_solution() -> list[int]:
            
            for a in range(self._height):
                for b in range(self._width):
                    energy=0
                    if a==0:
                        energy=self.energy(b,a)
                        memoization[b,a]=energy
                    else:
                        if b==0:
                            energy=self.energy(b,a)+min(memoization[b,a-1],memoization[b+1,a-1])
                            memoization[b,a]=energy
                        elif b==self._width-1:
                            energy=self.energy(b,a)+min(memoization[b-1,a-1],memoization[b,a-1])
                            memoization[b,a]=energy
                        else:
                            energy=self.energy(b,a)+min(memoization[b-1,a-1],memoization[b,a-1],memoization[b+1,a-1])
                            memoization[b,a]=energy
            
            

            #Get the minimum energy in the lowest part of the graph:
            lowestenergy=sys.maxsize
            lowestenergyx=0
            for c in range(self._width):
                if memoization[c,self._height-1] < lowestenergy:
                    lowestenergy=memoization[c,self._height-1]
                    lowestenergyx=c


            #retracing those steps
            vertical_seam=list()

            for d in range(self._height):
                
                if lowestenergyx==0:
                    candidates={lowestenergyx: memoization[lowestenergyx,self._height-1-d], lowestenergyx+1: memoization[lowestenergyx+1,self._height-1-d]}
                elif lowestenergyx==self._width-1:
                    candidates={lowestenergyx-1 :memoization[lowestenergyx-1,self._height-1-d], lowestenergyx: memoization[lowestenergyx,self._height-1-d]}
                else:
                    candidates={lowestenergyx-1 :memoization[lowestenergyx-1,self._height-1-d], lowestenergyx: memoization[lowestenergyx,self._height-1-d], lowestenergyx+1: memoization[lowestenergyx+1,self._height-1-d]}

                lowestenergyx=min(candidates, key=candidates.get)
                vertical_seam.append(lowestenergyx)
                
            vertical_seam.reverse()
            
            return vertical_seam

        #Energy Efficient (top down Approach) Method.

        #tests
        #print(M(0,0))
        returned_seam=arraybuilder_solution()
        #print(M(0,1))
        #print(q)
        print("--- %s seconds ---" % (time.time() - start_time))
        return returned_seam
    
        raise NotImplementedError

    def find_horizontal_seam(self) -> list[int]:
        '''
        Return a sequence of indices representing the lowest-energy
        horizontal seam
        '''

        original_energy_function=self.energy



        originalheight=self._height
        originalwidth=self._width

        self._width=originalheight
        self._height=originalwidth

        def horizontal_energy(i: int,j :int):
            a=0
            self._height=originalheight
            self._width=originalwidth
            a=original_energy_function(j,i)
            self._width=originalheight
            self._height=originalwidth
            return  a
            
        
        self.energy=horizontal_energy

        horizontal_seam=[]

        horizontal_seam=self.find_vertical_seam()

        self.energy=original_energy_function
        self._height=originalheight
        self._width=originalwidth


        print(horizontal_seam)
        return horizontal_seam


        
        
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



