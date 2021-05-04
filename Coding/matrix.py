class A:
    def __init__(self):
        self.nr=int(input())
        self.nc=int(input())
    
        
        self.matrix=[]
        for i in range(self.nr):
            self.col=[]
            for j in range(self.nc):
                self.element=int(input())
                self.col.append(self.element)
            self.matrix.append(self.col)
        
    def printMatrix(self):
        for i in range(0,self.nr):
            for j in range(0,self.nc):
                print(self.matrix[i][j],end=" ")
            print()
    #def sumMat(self,A,B):
        

    
a=A()
b=A()
#a.printMatrix()

