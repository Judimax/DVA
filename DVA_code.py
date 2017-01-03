'''ran into class copying properties, trying to find different ways
of adding while preserving the identity
'''


from Distance_vect import *
from supermap import *
import time
global debug
debug = True
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

def DVA(source_ltr,dest_ltr):

        time.sleep(2)
        print(source_ltr,dest_ltr)

        if source_ltr == None:
                print('stop here')
                return 0
            
        elif source_ltr == dest_ltr:
                print('ima crasshhhh!!!')
                return 0 


        
        blue = 9999
        red = 9999
        yellow = 9999
        green = 9999
        xylis= ''
        print("i cant seem to get out of here")
        if source_ltr != dest_ltr:
            xylis= DVA_table.find([source_ltr])
            print(source_ltr)
        elif xylis == '':return
        
        if xylis.l_value != 0:
                if xylis.left != dest_ltr:
                    blue =xylis.l_value + DVA(xylis.left,dest_ltr)
                    print('going inside blue')
                print('im in blue')
                if debug == True:
                    print(blue)
                    
        if xylis.r_value != 0:
                if xylis.right != dest_ltr:
                    red = xylis.r_value + (xylis.right,dest_ltr)
                    print('going inside')
                print('im in red')
                
                if debug == True:
                    print('this is right')
                    
                    print((xylis.right), (dest_ltr))
                print('getting out of red')
        if xylis.u_value != 0:
                if xylis.up != dest_ltr:
                    yellow =xylis.u_value + DVA(xylis.up,dest_ltr)
                    print('going inside yellow')
                print('im in yellow')
                if debug == True:
                    print(yellow)
                    
        if xylis.d_value != 0:
                if xylis.down != dest_ltr:
                    green =xylis.d_value + DVA(xylis.down,dest_ltr)
                    print('going inside green')
                print('im in green')
                if debug == True:
                    print(green)
                    
                    
        if debug == True:
            print('here is the minimun value')
            print(min(blue,red,yellow,green))
        return min(blue,red,yellow,green)

                


    
        

def table(table,a,b,c,d,e):


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



debug = False
DVA_table = SuperMap(5)
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

DVA_table['u'] = u
DVA_table['v'] = v
DVA_table['x'] = x
DVA_table['y'] = y
DVA_table['z'] = z


print(DVA_table)

print(DVA_table.find('x'))



table(DVA_table,'u','v','x','y','z')
