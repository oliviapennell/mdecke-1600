## 
# @file linked_list.py
#
# Template for linked_list class.
#
# @author Michael John Decker, Ph.D.

class node :
    def __init__(self, item, prev = None, next = None) : 
        self.item = item
        self.prev = prev
        self.next = next

    def __str__(self) :
        return str(self.item)

    def __repr__(self) :
        return repr(self.item)


## linked_list
# Implements a doubly-linked list ADT
# @invariant (len == 0 and head == None and tail == None)
#         or (len != 0 and head != None and tail != None and head.prev == None and tail.next == None)
# You do not have to call your data members head/tail, but should be descriptive names
import functools
class linked_list :


    class iterator :

        def __init__(self, head) :
            self.current=head
        def __next__(self) :
            if self.current.next == None :
                raise stopiteration
            self.current = self.current.next
            return self.current
        def __iter__(self):
            return linked_list.iterator(self, self.head)
    ## constructor - iterable is an iterable object that initializes
    #  the linked_list in the order iterable is traversed
    def __init__(self, iterable = []) :
        self.length = 0
        self.head = node(None)
        self.tail = node(None)
        self.iterable = iterable
        for i in iterable :
            self.push_back(i)

    ## constant time access to first/last node, respectively
    #  @returns the first/last node, respectively
    def front(self) : 
        if self :
            self.front = self.head
            return self.front
        return None
    def back(self) : 
        if self :
            self.back = self.tail
            return self.back
        return None


    ## constant time insertion of a data item (any element)
    #  as the first/last (respectively) element 
    def push_front(self, item) :
        entry = node(item)
        if not self :
            self.head = entry
            self.tail = entry
            self.length +=1
        else :
            self.head.prev = entry 
            self.head.next = self.head
            self.head = entry
            self.length+=1

    def push_back(self, item) :
        entry = node(item)
        if not self :
            self.head=entry
            self.tail = entry
            self.length +=1
        else :
            self.tail.prev = entry
            self.tail.next = self.tail
            self.tail = entry
            self.length +=1
           

    ## constant time removal of the first/last (respectively) node/item
    #  @returns the item (not the node)
    def pop_front(self) : 
        if len(self) > 0 :
            self.head = self.head.next
            self.head.prev = None
            self.length -=1 
            return self.head.item
    def pop_back(self) : 
        if len(self) > 0 :
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return self.tail.item

    ## Turns list into a string representation.
    #  Strings prints identical to how 
    #  it would if it were a Python list
    #  @returns the string representation 
    def __str__(self) :
        stringList = "["
        i=0
        for val in self :
            if i < self.length-1 :
                stringList+=(str(val) + ",")
                i+=1
            else :
                stringList+=(str(val))
                i+=1
        stringList += "]"
        return stringList

    ## Provides an iterator over an instance of the linked list
    #  iterator is a separate class (either external or inner)
    #  that iterates from first to last.
    # __next__ returns a node
    #  @returns an iterator
    def __iter__(self) : 
        return linked_list.iterator(self)
    #returns an instance of iterator (use iterator/circularqueue repo code for reference)
    #tihis gets called automatically when there is a for loop
    #write code that calls an iterator and returnsit
    #no template provided for iterator, look at circularqueue for reference of iterator

    ## Generator function to iterate over the linked list from last to first.
    #  Generates nodes.
    def __reversed__(self) : 
        for i in range(0, 1000) :
            yield i

    ## converts linked list to a bool
    #  @returns False if empty, True otherwise
    def __bool__(self) : 
        if len(self) > 0 :
            return True
        else :
            return False

    ## Computes length of linked list
    #  @returns the length of the linked list 
    def __len__(self) : 
        return self.length

    ## implements Python sequence-style equality and less-then 
    #  (on the items held and not the nodes), respectively
    #   Ensures other is another linked list, if not assertion fail
    #   @returns True if equal/less-than, False otherwise
    def __eq__(self, other) : 
        otherNode = (other.head)
        selfNode = (self.head)
        for i in range (0, self.length) :
            if selfNode.item != otherNode.item :
                return False
            else :
                otherNode = otherNode.next
                selfNode = selfNode.next
                return True
    def __lt__(self, other) : 
        otherNode = (other.head)
        selfNode = (self.head)
        for i in range (0, self.length) :
            if selfNode.item < otherNode.item :
                return True
            else :
                otherNode = otherNode.next
                selfNode = selfNode.next
        return False
    ## implements in operator
    #  @returns True if item is in linked-list, False otherwise
    def __contains__(self, item) : 
        for i in self :
            if i.item == item :
                return True
        return False
    #contains is an opoerator that i need to override. use iterator in ths function

    def __next__(self):
        return self.next













    ## insert_after and remove are extra credit (5 points)
    #  All or nothing, linked-list must function perfectly to be elligible
    #  No partial credit

    ## constant time insertion of the data item (any element) after node
    #  @pre (precondition) node is in the linked list (self)
    def insert_after(self, node, item) : pass


    ## constant time removal of node from the linked list (self)
    #  @pre (precondition) node is in the linked list (self)
    def remove(self, node) : pass

