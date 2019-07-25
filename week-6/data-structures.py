# linked list
class Node:
    def __init__(self, data, next=None, previous=None):
        """ The next variable will represent the next item in our list, and we can go down the list until we have a none.
        """
        self.data = data
        self.next = next
        self.previous = previous #This is used in a doubly linked list
# python has a generic list type, has append, indexing into list
# uses a dynamic array, extending memory automatically when you get to the end
# actually puts pointers into the list to ensure each item in the list is the same size

# stack: data structure with LIFO, add and remove only from the top, practically speaking moves pointer up and down the data array
# stacks are done using a list

# queues: FIFO, keep track of start and back of the list
# in python to use queues, from collection import deque

# trees: sort of like linked lists, but nodes can point to multiple other nodes on the same tree
# binary tree: common subtype, always 0-2 children, right and left

class NodeTree:
    def __init__(self, data, right, left):
        """ Everything on a tree structure ends up being O(log n), how many elements you need to go down grows with the log of the length.
        """
        self.data = data
        self.right = right
        self.left = left

    def __repr__(self):
        s = ' '
        if self.right != None:
            s += print(self.right) + ', '
        s += self.data + ', '
        if self.left != None:
            s += print(self.left) + ', '
        return s

# Exercise: print numbers in a tree in order. Assume right tree is larger and left tree is smaller.
def printacc(node):
    try:
        if node.right != None:
            printacc(node.right)
    except:
        pass
    print(node.data)
    try:
        if node.left != None:
            printacc(node.right)
    except:
        pass


d = NodeTree(8, 10, NodeTree(5, None, 2))
printacc(d)
print(d.left.left)


# a graph is like a tree, but any element can point to any other element, no limitations

# hash/hashmap/dictionary: if we have a bunch of elements we want to link, goal is to spread out data,
# hash function: work in constant time, as do hash lookups

L = [1, 9, 3, 6, 2]
k = 13

def twoEqK(L, k):
    """ Takes a list and checks if any two elements in the list add up to k.
    """
    dictionary = {}
    for i in L:
        if k - i in dictionary:
            return True
        dictionary[i] = None
    return False

print(twoEqK(L, k))
