# QUESTION NO.1

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data, temp=None):
        if self.head == None:
            node = Node(data)
            self.head = node
            node.next = self.head
            return

        if temp == None:
            temp = self.head

        if temp.next == self.head:
            node = Node(data)
            node.next = self.head
            temp.next = node
            return

        self.push(data, temp.next)

    def traverse(self, temp=None):
        if temp == None:
            temp = self.head

        if temp.next == self.head:
            print(temp.data, end="\n")
            return
        print(temp.data, end="-->")
        self.traverse(temp.next)


if __name__ == "__main__":
    clist = CircularLinkedList()
    clist.push(21)
    clist.push(30)
    clist.push(7)
    clist.push(5)
    print("Traversed Circular Linked List: ", end="\n")
    clist.traverse()

# QUESTION NO.2

# Applications of Circular Linked Lists:

""" 
      1. Useful for implementation of a queue. Unlike this implementation,
      we don’t need to maintain two-pointers for the front and rear if we use a circular linked list.
      We can maintain a pointer to the last inserted node and the front can always be obtained as next of last 
"""

""" 
      2.Circular lists are useful in applications to go around the list repeatedly. 
      For example, when multiple applications are running on a PC, 
      it is common for the operating system to put the running applications on a list and then cycle through them, 
      giving each of them a slice of time to execute, and then making them wait while the CPU is given to another application. 
      It is convenient for the operating system to use a circular list so that when it reaches the end of the list it can
      cycle around to the front of the list.
"""

"""
     3.Circular Doubly Linked Lists are used for the implementation of advanced data structures like the Fibonacci Heap.

"""