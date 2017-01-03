'''update seems to be printing values properly with subclass as digits that
represents the node keeps intended data integrity or IDI'''


from Distance_vect import * 
from supermap import *
class digit():
    
            
    def __init__(self):
    

        self.left= ''
        self.right = ''
        self.up = ''
        self.down = ''
        self.l_value = 0
        self.r_value = 0
        self.u_value = 0
        self.d_value =0

    def add(self,left,right,up,down,l,r,u,d):


        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.l_value= l
        self.r_value = r
        self.u_value = u
        self.d_value = d

    def __str__(self):

        return str(self.left) + str(self.right) + str(self.up) + str(self.down)  + str(self.l_value) + str(self.r_value) + str(self.u_value) + str(self.d_value)+ '\n'

DVA_table = []

    
        

def table(a,b,c,d,e):

        print("     /   u    /    v    /    x    /    y    /    z")
        print("     /")
        print("  u  /__"+str(DVA(a,a))+"___"+str(DVA(a,b))+"________________________________________")
        print("     /")
        print("     /")
        print("  v  /_____________________________________________")
        print("     /")
        print("     /")
        print("  x  /_____________________________________________")
        print("     /")
        print("     /")
        print("  y  /_____________________________________________")
        print("     /")
        print("     /")
        print("  z  /_____________________________________________")
        print("     /")
        print("     /")
        
        print("     /")
        print("     /")

if __name__ == "__main__":

    DVA_table = SuperMap()
    u = digit()
    v = digit()
    x = digit()
    y = digit()
    z = digit()
    u.add(None,'v',None,'y',0,1,0,2)
    v.add('u','z',None,'x',1,6,0,3)
    x.add('y','z','v',None,3,3,2,0)
    y.add(None,'x','u',None,0,3,2,0)
    z.add('x',None,'v',None,2,0,6,0)
    
    DVA_table.append('u',u)
    DVA_table.append('v',v)
    DVA_table.append('x',x)
    DVA_table.append('y',y)
    DVA_table.append('z',z)

    print(DVA_table)

    
    
    #table(u,v,x,y,z)
