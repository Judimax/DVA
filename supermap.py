"""-----------------------------------------------------------------------------
Author: Michael Odumosu
Course: CSC 112
Assignment: Project 4
Date: 5/3/16
Description: This program makes uses and mainipulation the algorithm of List ADT
(Abstract Data Type) in order to keep and store information about a certain object
whether it be people or anything, at the same time using less memory
----------------------------------------------------------------------------------"""
from Array import *
from Quicksort algorithm import *

class SuperMap:

    class Node:
        def __init__(self,key,value):
            self.key = key   #for speedups
            self.value = value
            self.next= None

        def __str__(self):
            return self.key + str(self.value)

    def __init__(self, N=0):
        """The constructor method, this provides the framework for the List ADT, and also presets the size
            speedups hash"""
        self.headptr = None
        self.tailptr = None
        self.speedups = Array(N) #this is an array
        self.speedups_len = N
        self.debug = False
        self.z = 0

    def __str__(self):
        """This has the Supermap object print out everything in the Linked List
            instead of printing out what type of object it is and its location in memory"""

        runner =self.headptr
        retVal = "{"
        if self.headptr == None:
            retVal += "}"
            return retVal
        while runner != self.tailptr:
            retVal += runner.key + " : " + str(runner.value) + ", "
            runner = runner.next
        retVal += runner.key + " : " + str(runner.value)
        retVal += "}"
        return retVal

        
    """------------------------------------------------------------------------------------"""
    
    def _insert(self,key,value):
        """Really the append method, but name changed through professors
            discretion. This method takes the key and the value and appends
            it to the linked list in memory. Also returns it if method is needed
            for a future operation"""
        
        newnode = self.Node(key,value)
        if self.headptr == None:
            self.headptr = newnode
            self.tailptr = newnode        
        else:
            self.tailptr.next = newnode
            self.tailptr = newnode
        return newnode

    """--------------------------------------------------------------------------------------"""

    def _make_hash(self,key):
        """This method uses the ASCII value of the key modulus the length of speedups
            to decide where to put the key in the speedups hash"""
        
        sum = 0
        for i in key:
            sum += ord(i)
        return sum % self.speedups_len

    """------------------------------------------------------------------------------------"""
            
    def length(self):
        """This method finds the length of a the linked list with one unit as Node and once done
            returns the length as an int"""

        length_one = self.headptr
        lnth=1
        while length_one.next != None:
            length_one = length_one.next
            lnth += 1
        return lnth

    def delete(self,key):
        """This method finds the Node that you want to delete by using the key and
            finding the matching node. First it checks if its in the speedups and
            deletes it if it is there. Then its goes through the linked list and
            if it is there, has the previous Node's pointer point to the next Node
            virtually deleting the Node from the linked list"""

        break_out = 0 #For loop breaking and adt node location purposes
        not_fst = 0
        remove = self._make_hash(key)
        if self.speedups[remove] == key:
            self.speedups[remove] = None

        runner = self.headptr
        prev = None
        while runner != None:
            if break_out ==1 :
                return True
            elif runner.key == key and not_fst == 0:
                self.headptr = runner.next 
                break_out =1
                self.z =1
            elif runner.key == key and not_fst > 0:
                if runner == self.tailptr:
                    self.tailptr = prev
                    prev.next = None
                    break_out = 1
                else:
                    prev.next = runner.next
                    break_out = 1
            not_fst += 1
            prev= runner
            runner = runner.next
        if break_out == 1:
            return True
        return False


    def clear(self):
        """This method deletes everything in the speedups hash as well as the Linked List itself"""
        self.headptr.next = None
        self.tailptr= None
        self.headptr = None
        self.purge()

    def purge(self):
        """This method deletes everything in the speedups but does not the touchs
            the Linked List"""

        for index in range(len(self.speedups)):
            self.speedups[index] = None
                       
    def dump(self):
        """This method prints out all the information contained each Node of the
            Linked List namely: id, hash number, key, value, id of the next.
            It also prints out id of the nodes that curretly hold positions in the
            speedups hash"""

        runner = self.headptr
        info = "The linked list chain\n" + "----------------------------\n"
        while runner != None:
            data = ""
            data += "id: " +str(self.xid(runner)) + "\n"
            data += "   hash: " + str(self._make_hash(runner.key)) + "\n"
            data += "   key: " + str(runner.key) + "\n"
            data += "   value: " +str(runner.value) + "\n"
            data += "   next: " + str(self.xid(runner.next)) + "\n"
            info += data 
            runner = runner.next
        info += "\n" + "The speedups array:\n" + "---------------------------------------\n" 
        for index in range(len(self.speedups)):
            info += str(index) + ".  " + str(self.xid(self.speedups[index])) +  "\n"
        info += "-----------------end-------------------"
        print(info)
    """-----------------------------------------------------------------------"""

    def __setitem__(self, key, value):
        """This method is used either to insert a newnode or change a value in an existing node
            by going through speedups and linked to determine if the key-value pair exists"""

        not_in_speedups =0
        if self.headptr == None:
            nodepointer = self._insert(key,value)
            self._insert_in_speedups(nodepointer)
        elif self.headptr != None:
            exist = self._find_in_speedups(key)
            if exist != None:
                exist.value = value
                return "Value fould in the hash and changed"
            not_in_speedups =1  
        if not_in_speedups == 1:
            present = self._find_in_chain(key)
            if present == None:
                pass
            elif present.key == key:
                present.value = value
                self._insert_in_speedups(present)
                return " Value found in the chain and changed"
            nodepointer = self._insert(key,value)
            self._insert_in_speedups(nodepointer)

    """------------------------------------------------------------------------"""

    def __getitem__(self,key):
        """This method looks through the speedups hash and the Linked List
            to find the Node associated with the given key. If it finds it
            it specifies where it is found and returns the value of that
            associated key. Else it returns None"""

        not_in_speedups =0
        
        if self.headptr == None:
            return None
        elif self.headptr != None:
            exist = self._find_in_speedups(key)
            if exist != None:
                if self.debug == True:
                    print("in_find_in_speeduups key =", key )
                    print("trying to find in speedups, key=", key," hash(key)= ",self._make_hash(key))
                    print("found", key,"in speedups")
                    return str(exist.value)
                else:
                    return str(exist.value)
            not_in_speedups =1
            
        if not_in_speedups ==1:
            present = self._find_in_chain(key)
            if present == None:
                pass
            elif present != None:
                self._insert_in_speedups(present)
                if self.debug == True:
                    print("in_find_in_speeduups, key =", key )
                    print("trying to find in speedups, key=", key," hash(key)= ",self._make_hash(key))
                    print("did not find", key,"in speedups")
                    print("in_find_in_chain, key=", key)
                    print("found ", key," in chain")
                    print("Inserting ",key," into speedups at location",self._make_hash(key))
                    return str(present.value)
                else:
                    print("found ",key," in chain")
                    return str(present.value)
                
        
        if self.debug == True:
            print("in_find_in_speeduups, key =", key )
            print("trying to find in speedups, key=", key," hash(key)= ",self._make_hash(key))
            print("did not find", key,"in speedups")
            print("in_find_in_chain, key=", key)
            print("did not find ", key," in chain")
            return None
        else:
            return None
        
    """------------------------------------------------------------------------"""

    def _insert_in_speedups(self, nodepointer):
        """This method simply inserts the key of the given Node, into the index
            given by the _make_hash method"""
        
        box = self._make_hash(nodepointer.key)
        self.speedups[box] = nodepointer.key
    """ ------------------------------------------------------------------------"""

    def _find_in_speedups(self,key):
        """This method finds if the node for the associated key is in the speedups
            If it is found it returns the associated node. Else it returns None"""
        
        box = self._make_hash(key)
        if self.speedups[box] == key:
            runner = self.headptr
            while runner != None:
                if runner.key == key:
                    return runner
                runner = runner.next 
        else:
            return None

    """ ----------------------------------------------------------------------"""

    def _find_in_chain(self,key):
        """This method finds if the node for the associated key is in the Linked List.
            If it is found it returns the ass
        print("     /")ociated node. Else it returns None"""
            
        runner = self.headptr
        while runner != None:
            if runner.key == key:
                return runner
            runner = runner.next
        else:
            return None

    """----------------------------------------------------------------------"""

    def getPointer(self, key):
        """This method finds the associated Node containing the key and returns it in both
            the Linked List and the speedups, else it returns None"""

        target = self._find_in_speedups(key)
        if target == None:
            target = self._find_in_chain(key)
        if target == None:
            return N
        print("found", key," in chain")
        return target

    def getFirstPointer(self):
        """This method provides and easy way for the system interface to get the first Node of the
            Linked list, the headptr"""
        runner = self.headptr
        while runner != None:
            if runner.key == key:
                return runner
            runner = runner.next
        else:
            return None
        return self.headptr

    def xid(self, pointer):
        """This method remedies the memory location of the 'None' object by literally returning None
            in place of its memory location if the node does not exist"""
        if pointer == None:
            return "None"
        else:
            return str(id(pointer))
        
    def find(self,key):
        """This method finds the key in the linked list and returns its node"""

        runner = self.headptr
        while runner != None:
            if runner.key == key:
                return runner.value
            runner = runner.next
        else:
            return None
        
    def getKeys(self): #Find out why memory does not like adding itself to a list
        """This method gets all the keys in the linked list and sorts them according to
            the keys and returns that sorted list"""

        those_Keys = []
        runner = self.headptr

        while runner != None:
            those_Keys.append(runner.key)
            runner = runner.next

        return quicksort(those_Keys, 0 ,len(those_Keys)-1)
    
        
        

        

            

        

        

        
            
            

            

    
                

    
        
            
            
            
        
            

            
            
        
    
            

            
        
