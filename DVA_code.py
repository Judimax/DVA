'''used method so python can see as one object neighbor not an object and a string'''


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
        self.innerdict = {}
        
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
    
    def tval (self,value = ''):
        for i in self.innerlist:
            print(i)
            if value == i:
                return i
            
        

def DVB(source_ltr, dest_ltr,KM_P = [],hands = {'left':'l_value','right':'r_value','up':'u_value','down':'d_value'}):
    
    print('hands-----\n',hands,type(hands))
    print('source_ltr, dest_ltr,KM_P')
    print(source_ltr, dest_ltr,KM_P)
    KMP = [] #keep moving foward
    KMP += KM_P
    KMP.append(source_ltr)
    print('after we append KM_P')
    print('source_ltr, dest_ltr,KMP')
    print(source_ltr, dest_ltr,KMP)
    
    if source_ltr == dest_ltr:
        vald =0
        print('equal',vald)
        return vald
    
    else:
        KTLR = [] #memory of neighbors
        TLFT = [] #memory of paths
        choices = [] #memory of lengths 
        path_sum = 0 #gets the sum
        
        xylis= DVA_table.find(source_ltr)
        print('KTLR,TLFT,choices,path_sum,xylis('+ source_ltr +')')
        print(KTLR,TLFT,choices,path_sum,xylis)
        for i in hands:
            jalis = 'xylis.' + i
            print(type(jalis))
            if xylis.i == None:
                print(i)
                print('xylis('+ xylis.i +')')
                print(xylis.i)
                print('\n')
                
                if xylis.i not in KMP:
                    KTLR.append(xylis.i)
                    print(i)
                    print('KTLR')
                    print(KTLR)
                    print('\n')
                    path_sum += xylis.hands[i] + DVB(KTLR[-1],dest_ltr,KMP)
                    print('in source_ltr    ' + source_ltr)
                    print(i)
                    print('path_sum from  ' + source_ltr+ ' to ' + dest_ltr)
                    print(path_sum, xylis.hands[i],path_sum-xylis.hands[i] )
                    choices.append(path_sum)
                    print(i)
                    print('choices')
                    print(choices)
                    print('\n')
        
        #DVC(source_ltr,dest_ltr,xylis,TLFT,KMP,choices,path_sum)
        print('here are you choices and here is the shortest neighbor')
        print(choices,min(choices))
        return min(choices)
        

        
        '''--------------------code to loop on'''
        KMP.append(source_ltr) #knows not to go back
        path_sum += 0 
        xylis= DVA_table.find(source_ltr) #activates the string as a xylis
        #node
        if KMP[-1] == dest_ltr:
            TLFT.append(KMP)
            KMP= []
            choices.append(path_sum)
            path_sum = 0
        if debug:
            
            print(xylis)
            print(path_sum)
            print(TLFT)
            print(KMP)
            
        '''--------------------------- code to loop on'''
        KMP.append(xylis.right)
        path_sum += xylis.r_value
        xylis = DVA_table.find(KMP[-1])
        if KMP[-1] == dest_ltr:
            TLFT.append(KMP)
            KMP= []
            choices.append(path_sum)
            path_sum = 0
            
        #node
        if debug:
            
            print(xylis)
            print(path_sum)
            print(TLFT)
            print(KMP)
            
        '''---------------------------------------'''
        KMP.append(xylis.down)
        path_sum+= xylis.d_value
        xylis = DVA_table.find(KMP[-1])
        if KMP[-1] == dest_ltr: 
            TLFT.append(KMP)
            KMP = []
            choices.append(path_sum)
            path_sum = 0
            
        #node
        if debug:
            print(xylis)
            print(path_sum)
            print(TLFT)
            print(KMP)
            
        '''-----------------------------------------'''
        KMP.append(source_ltr)
        path_sum+= xylis.d_value
        xylis = DVA_table.find(KMP[-1])
        if KMP[-1] == dest_ltr: 
            TLFT.append(KMP)
            KMP = []
            choices.append(path_sum)
            path_sum = 0
        #node
        if debug:
            print(xylis)
            print(path_sum)
            print(TLFT)
            print(KMP)
            
        '''-----------------------------------------'''
        KMP.append(xylis.down)
        path_sum+= xylis.d_value
        xylis = DVA_table.find(KMP[-1])
        if KMP[-1] == dest_ltr: 
            TLFT.append(KMP)
            KMP = []
            choices.append(path_sum)
            path_sum = 0
        #node
        if debug:
            print(xylis)
            print(path_sum)
            print(TLFT)
            print(KMP)
            
        '''-----------------------------------------'''
        KMP.append(xylis.right)
        path_sum+= xylis.r_value
        xylis = DVA_table.find(KMP[-1])
        if KMP[-1] == dest_ltr: 
            TLFT.append(KMP)
            KMP = []
            choices.append(path_sum)
            path_sum = 0
        #node
        if debug:
            print(xylis)
            print(path_sum)
            print(TLFT)
            print(KMP)
            
        '''-----------------------------------------'''

        return min(choices)

def DVC(self,src , dest, path_mem, len_mem, KMF, len_product ):
        '''--------------------code to loop on'''
        KMP.append(source_ltr) #knows not to go back
        path_sum += 0 
        xylis= DVA_table.find(source_ltr) #activates the string as a xylis
        #node
        if KMP[-1] == dest_ltr:
            TLFT.append(KMP)
            KMP= []
            choices.append(path_sum)
            path_sum = 0
            return 
        if debug:
            
            print(xylis)
            print(path_sum)
            print(TLFT)
            print(KMP)
            
        '''--------------------------- code to loop on'''
    
        
    
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
        print("  u  /__"+str(DVB(a,a))[1]+"_____"+str(DVB(a,b))+"______"+str(DVB(a,c))+"____"+str(DVB(a,d))+"________"+str(DVB(a,e))+"_________________")
        print("     /")
        print("     /")
        #print("  v  /__"+str(DVB(b,a))+"_____"+str(DVB(b,b))+"______"+str(DVB(b,c))+"____"+str(DVB(b,d))+"________"+str(DVB(b,e))+"_________________")
        print("     /")
        print("     /")
        #print("  x  /__"+str(DVB(c,a))+"_____"+str(DVB(c,b))+"______"+str(DVB(c,c))+"____"+str(DVB(c,d))+"________"+str(DVB(c,e))+"_________________")
        print("     /")
        print("     /")
        #print("  y  /__"+str(DVB(d,a))+"_____"+str(DVB(d,b))+"______"+str(DVB(d,c))+"____"+str(DVB(d,d))+"________"+str(DVB(d,e))+"_________________")
        print("     /")
        print("     /")
        #print("  z  /__"+str(DVB(e,a))+"_____"+str(DVB(e,b))+"______"+str(DVB(e,c))+"____"+str(DVB(e,d))+"________"+str(DVB(e,e))+"_________________")
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
'''u.add(None,'v',None,'y',0,1,0,2)
v.add('u','z',None,'x',1,6,0,3)
x.add('y','z','v',None,3,2,3,0)
y.add(None,'x','u',None,0,3,2,0)
z.add('x',None,'v',None,2,0,6,0)'''

u.add(None,'v',None,None,0,1,0,0)
v.add('u',None,None,'x',1,0,0,3)
x.add(None,None,'v',None,0,0,3,0)

DVA_table['u'] = u
DVA_table['v'] = v
DVA_table['x'] = x
#DVA_table['y'] = y
#DVA_table['z'] = z


print(DVA_table)
print(u.tval('right'))



#print(str(DVB('u','x')))
#table(DVB_table,'u','v','x','y','z')
