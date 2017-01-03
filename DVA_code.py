'''Found big problem
DVA code doesnt account that it has already been through chosen path
make a recorder for it to go by
recusion forgets to add original lengths from path to path
rewrite DVA
'''


from Distance_vect import *
from supermap import *
import time
global debug
debug = True
global snap_this
snap_this = ''
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
        answer = input()
        global snap_this
        if snap_this == dest_ltr:
            print('starting to break')
            taggle = []
            taggle.append(0)
            taggle.append(snap_this)
            return taggle
        else:
            tarmnet= []
            tarmnet.append(0)
            tarmnet.append(source_ltr)

            if debug:
                print('I choose recursion')
                print('Face down')
                print('End turn')
                print(source_ltr,dest_ltr)
                
            

            if source_ltr == None:
                    print('stop here')
                    return tarmnet[0]
                
            if source_ltr == dest_ltr:
                    print('got out in the else statement!!!')
                    return tarmnet


            
            blue = 9999
            red = 9999
            yellow = 9999
            green = 9999
            xylis= ''
            
            
            xylis= DVA_table.find(source_ltr)
            print('this is the first xylis')
            print(source_ltr,   xylis)
            
            if debug:
                print('im in blue')
                
            if xylis.left == dest_ltr:
                    
                        print('going inside blue')
                        snap_this = xylis.left
                        if debug:
                            print(snap_this)
                        blue =xylis.l_value + DVA(xylis.left,dest_ltr)[0]
                        if debug == True:
                            print('this is left')
                            print((xylis.left), (dest_ltr))
                        print('getting out of blue')
                    
            if debug:
                print('im in red')
                
            if xylis.right == dest_ltr:
                        print('going inside red to get a value')
                        snap_this = xylis.right
                        if debug:
                            print(snap_this)
                        red = xylis.r_value + DVA(xylis.right,dest_ltr)[0]
                        if debug == True:
                            print('this is right')
                            print((xylis.right), (dest_ltr))
                        print('getting out of red')
            if debug:       
                print('im in yellow')
                
            if  xylis.up == dest_ltr:
                    print('going inside yellow to get a valuue')
                    snap_this = xylis.up
                    if debug:
                        print(snap_this)
                    yellow =xylis.u_value + DVA(xylis.up,dest_ltr)[0]
                    if debug == True:
                        print('this is up')
                        print((xylis.up), (dest_ltr))
                    print('getting out of yellow')
            if debug:
                print('im in green')
                
            if  xylis.down == dest_ltr:
                        
                        print('going inside green to get a value')
                        snap_this = xylis.down
                        if debug:
                            print(snap_this)
                        green =xylis.d_value + DVA(xylis.down,dest_ltr)[0]
                        if debug == True:
                            print('this is down')
                            print((xylis.down), (dest_ltr))
                        print('getting out of green')
                        


            
                        
            else:

                if debug:
                    print('now looking for destination')
                    time.sleep(2)
                    print('now im going to blue')
                            
                if xylis.l_value != 0:
                        if xylis.left != dest_ltr:
                            print('going inside blue to get a value')
                            snap_this = xylis.left
                            if debug:
                                print(snap_this)
                            blue =xylis.l_value + DVA(xylis.left,dest_ltr)[0]
                        print('im in blue')
                        if debug == True:
                            print(blue)
                            print((xylis.left), (dest_ltr))
                if debug:       
                    print('now im going to red')
                    
                if xylis.r_value != 0:
                        if xylis.right != dest_ltr:
                            print('going inside red to get a value')
                            snap_this = xylis.right
                            if debug:
                                print(snap_this)
                            red = xylis.r_value + DVA(xylis.right,dest_ltr)[0]
                        print('im in red')
                        if debug == True:
                            print('this is right')
                            print((xylis.right), (dest_ltr))
                        print('getting out of red')
                if debug:       
                    print('now im going to yellow')
                    
                if xylis.u_value != 0:
                        if xylis.up != dest_ltr:
                            print('going inside yellow to get a value')
                            snap_this = xylis.up
                            if debug:
                                print(snap_this)
                            yellow =xylis.u_value + DVA(xylis.up,dest_ltr)[0]
                        print('im in yellow')
                        if debug == True:
                            print('this is up')
                            print((xylis.up), (dest_ltr))
                        print('get getting out of yellow')
                if debug:
                    print('now im going to green')
                               
                if xylis.d_value != 0:
                        if xylis.down != dest_ltr:
                            print('going inside green to get a value')
                            snap_this = xylis.down
                            if debug:
                                print(snap_this)
                            green =xylis.d_value + DVA(xylis.down,dest_ltr)[0]
                        print('im in green')
                        if debug == True:
                            print('this is down')
                            print((xylis.down), (dest_ltr))
            
                
            if debug:
                print("if the letter here is not matching up with the dest something doesn't know something")
                print(snap_this)    
                print("got out thoo :)")
                        
            if debug == True:
                print('here is the minimun value')
                print(min(blue,red,yellow,green))
            tarmnet = []
            tarmnet.append(min(blue,red,yellow,green))
            if debug:
                print(tarmnet)
            tarmnet.append(source_ltr)
            if debug:
                print(tarmnet)
            return tarmnet

                


    
        

def table(table,a,b,c,d,e):


        print("     /   u    /    v    /    x    /    y    /    z")
        print("     /")
        print("  u  /__"+str(DVA(a,a))[1]+"_____"+str(DVA(a,b))+"______"+str(DVA(a,c))+"____"+str(DVA(a,d))+"________"+str(DVA(a,e))+"_________________")
        print("     /")
        print("     /")
        #print("  v  /__"+str(DVA(b,a))+"_____"+str(DVA(b,b))+"______"+str(DVA(b,c))+"____"+str(DVA(b,d))+"________"+str(DVA(b,e))+"_________________")
        print("     /")
        print("     /")
        #print("  x  /__"+str(DVA(c,a))+"_____"+str(DVA(c,b))+"______"+str(DVA(c,c))+"____"+str(DVA(c,d))+"________"+str(DVA(c,e))+"_________________")
        print("     /")
        print("     /")
        #print("  y  /__"+str(DVA(d,a))+"_____"+str(DVA(d,b))+"______"+str(DVA(d,c))+"____"+str(DVA(d,d))+"________"+str(DVA(d,e))+"_________________")
        print("     /")
        print("     /")
        #print("  z  /__"+str(DVA(e,a))+"_____"+str(DVA(e,b))+"______"+str(DVA(e,c))+"____"+str(DVA(e,d))+"________"+str(DVA(e,e))+"_________________")
        print("     /")
        print("     /")
        print("     /")
        print("     /")


global DVA_table
DVA_table= SuperMap(5)
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



print(str(DVA('u','x'))[1])
#table(DVA_table,'u','v','x','y','z')
