from Distance_vect import *
class network:

    def __init__(self):
        self.route = []

    class leaf:

        def __init__(self):
        
            self.node = ''
            self.left= ''
            self.right = ''
            self.up = ''
            self.down = ''

        class values:

            def __init__(self):

                self.l_value = 0
                self.r_value = 0
                self.u._value = 0
                self.d_value =0

    def add(self,node,left,right,up,down,l,r,u,d):

        self.leaf.node = node
        self.leaf.left = left
        self.leaf.right = right
        self.leaf.up = up
        self.leaf.down = down
        self.leaf.values.l_value = l
        self.leaf.values.r_value = r
        self.leaf.values.u_value = u
        self.leaf.values.d_value = d

    def add_to_Network(self,leaf):
        self.network.route.append(leaf)
        

    def table(self):
        print("     /   u    /    v    /    x    /    y    /    z")
        print("     /")
        print("  u  /__"+str(DVA('u','v'))+"___________________________________________")
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


Network = network()
Network.add('u',None,'v',None,'y',0,1,0,2)
Network.add('v','u','z',None,'x',1,6,0,3)
Network.add('y',None,'x','u',None,0,3,2,0)
Network.add('x','y','z','v',None,3,3,2,0)
Network.add('z','x',None,'v',None,2,0,6,0)
Network.table()

