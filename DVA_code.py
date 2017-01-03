'''solves prev neigbor path '''
from collections import OrderedDict
from Distance_vect import *
from supermap import *
import time
global debug
debug = True
global snap_this
snap_this = ''
class digit():
    
            
    def __init__(self,name):

        self.name = name
        self.innerlist = [] #hold all information about the objects neighbors
        
    def add(self,left,right,up,down,l,r,u,do):

        
        a = ['left',left]
        b= ['l_value',l]
        ab= [a,b]
        c = ['right',right]
        d = ['r_value',r]
        cd = [c,d]
        e =['up',up]
        f =['u_value',u]
        ef = [e,f]
        g = ['down',down]
        h = ['d_value',do]
        gh = [g,h]
        self.innerlist += [ab,cd,ef,gh]
        

    def __str__(self):

        node = self.name + '\n'
        for i in self.innerlist:
            i = str(i)
            i = i.strip("[")
            i = i.strip("]")
            node += i + '\n'
        return node
    
    def valt (self,value = ''):
        
        for i in self.innerlist:
            for k in i:
                for l in k:
                    print(l)
                    if value == l:
                        
                        return k[1]
            
    def __iter__(self):
        self.__i__= 0
        return self
        

def DVB(source_ltr, dest_ltr,KTL_R=[],KM_P = []):

    if debug:
        print('source_ltr, dest_ltr,KTL_R,KM_P')
        print(source_ltr, dest_ltr,KTL_R,KM_P)
    KMP = [] #keep moving foward
    KMP += KM_P
    KMP.append(source_ltr)
    if debug:
        print('after we append KM_P')
        print('source_ltr, dest_ltr,KMP')
        print(source_ltr, dest_ltr,KMP)
    
    if source_ltr == dest_ltr:
        my_dest =0
        if debug:
            print('equal',my_dest)
        return my_dest
    
    else:
        KTLR = [] #memory of neighbors
        
        TLFT = [] #memory of paths
        choices = [] #memory of lengths 
        path_sum = 0 #gets the sum
        
        xylis= DVA_table.find(source_ltr)
        if debug:
            print('KTLR,TLFT,choices,path_sum\n,xylis('+ source_ltr +')')
            print(KTLR,TLFT,choices,path_sum)
        i = 0
        for i in xylis.innerlist:
            if i[0][1] != None:
                if debug:
                    print('===========')
                    print(i[0][0])
                    print(i[0][1])
                    print(KTLR)
                    print('in xylis('+ source_ltr+')')
                    print('\n')
                
                if i[0][1] not in KMP:
                    if i[0][1] not in KTL_R:
                        
                        if debug:
                            print(KTLR)
                        KTLR.append(i[0][1])
                        if debug:

                            print(i)
                            print('KTLR')
                            print(KTLR)
                            print('\n')
                        path_sum += i[1][1] + DVB(KTLR[-1],dest_ltr,KTLR,KMP)
                        if debug:
                            print('in source_ltr    ' + source_ltr)
                            print('\n')
                            print('path_sum from  ' + source_ltr+ ' to ' + dest_ltr)
                            print(path_sum, i[1][1],path_sum-i[1][1])
                        choices.append(path_sum)
                        path_sum = 0
                        if debug:
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
                            KTLR.append(i[0][1])
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
        print("  u  /__"+str(DVB(a,a))+"__\n___"+str(DVB(a,b))+"___\n___"+str(DVB(a,c))+"_\n___"+str(DVB(a,d))+"____\n____"+str(DVB(a,e))+"________\n_________")
        print("     /")
        print("     /")
        print("  v  /__"+str(DVB(b,a))+"__\n___"+str(DVB(b,b))+"___\n___"+str(DVB(b,c))+"_\n___"+str(DVB(b,d))+"___\n_____"+str(DVB(b,e))+"_____\n____________")
        print("     /")
        print("     /")
        print("  x  /__"+str(DVB(c,a))+"__\n___"+str(DVB(c,b))+"__\n____"+str(DVB(c,c))+"__\n__"+str(DVB(c,d))+"___\n_____"+str(DVB(c,e))+"______\n___________")
        print("     /")
        print("     /")
        print("  y  /__"+str(DVB(d,a))+"_____"+str(DVB(d,b))+"______"+str(DVB(d,c))+"____"+str(DVB(d,d))+"________"+str(DVB(d,e))+"_________________")
        print("     /")
        print("     /")
        print("  z  /__"+str(DVB(e,a))+"_____"+str(DVB(e,b))+"______"+str(DVB(e,c))+"____"+str(DVB(e,d))+"________"+str(DVB(e,e))+"_________________")
        print("     /")
        print("     /")
        print("     /")
        print("     /")


global DVA_table
DVA_table= SuperMap(5)
u = digit('u')
v = digit('v')
x = digit('x')
y = digit('y')
z = digit('z')
u.add(None,'v',None,'y',0,1,0,2)
v.add('u','z',None,'x',1,6,0,3)
x.add('y','z','v',None,3,2,3,0)
y.add(None,'x','u',None,0,3,2,0)
z.add('x',None,'v',None,2,0,6,0)



DVA_table['u'] = u
DVA_table['v'] = v
DVA_table['x'] = x
DVA_table['y'] = y
DVA_table['z'] = z


#print(DVA_table)

#print(u.valt('right'))
print(str(DVB('u','x')))
#table(DVA_table,'u','v','x','y','z')
