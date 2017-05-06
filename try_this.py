from Distance_vect import *
import Distance_vect


class leaf:


    def __init__(self):
        
    
        self.left= ''
        self.right = ''
        self.up = ''
        self.down = ''
        self.values = t()

    def __str__(self):

        return str(self.left) + str(self.right) + str(self.up) + str(self.down) + "\n" + str(self.values.l_value) + str(self.values.r_value) + str(self.values.u_value) + str(self.values.d_value)   

def add(node,left,right,up,down,l,r,u,d):


        node.left = left
        node.right = right
        node.up = up
        node.down = down
        node.values.l_value = l
        node.values.r_value = r
        node.values.u_value = u
        node.values.d_value = d


        

def table(a,b,c,d,e):

        print("     /   u    /    v    /    x    /    y    /    z")
        print("     /")
        print("  u  /__"+str(DVA(u,u))+"___"+str(DVA(u,v))+"________________________________________")
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


u = leaf()
v = leaf()
x = leaf()
y = leaf()
z = leaf()
if __name__ == "__main__":
    add(u,None,'v',None,'y',0,1,0,2)
    add(v,'u','z',None,'x',1,6,0,3)
    add(x,None,'z','v',None,0,3,2,0)
    add(y,None,'x','u',None,3,3,2,0)
    add(z,'x',None,'v',None,2,0,6,0)
    print(str(u))
    print(str(v))
    table(u,v,x,y,z)
