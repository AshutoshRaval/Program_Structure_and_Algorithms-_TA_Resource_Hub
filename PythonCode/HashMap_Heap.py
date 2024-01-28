# from graphviz import Digraph

# filepath = "D:\ProfNath_PSA_SM\graph\Test\\"

print("\nImplementation of HashTable")
def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % 100

get_hash('Sam')

# https://docs.python.org/3/library/operator.html
# Here we are overwriting the function default __getitem__ and __setitem__ function
class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        step = 0
        print("\ngetItem item form array")
        h = self.get_hash(key)
        print("Hash Value of key", key," is", h)
        print("No of step req for the operation", step+1)   
        return self.arr[h]
    
    def __setitem__(self, key, val):
        step = 0
        print("\nsetItem item form array")
        h = self.get_hash(key)
        print("Hash Value of key", key," is", h)
        self.arr[h] = val
        print("No of step req for the operation", step+1)    
        
    def __delitem__(self, key):
        step = 0
        print("\ndelete item form array")
        h = self.get_hash(key)
        print("Hash Value of key", key," is", h)
        self.arr[h] = None      
        print("No of step req for the operation", step+1)   

# Creating Hash Table
t = HashTable()

# Adding values in the hash map based on the key
# t[key] = value 
t["Sam"] = 310
t["Tom"] = 420


print("\nArray format of the hashtable", t.arr)

# Adding/Updatig values in the hash map based on the key
t["Adam"] = 88

# geting/Read the value based on the key provided
print("Value of the key is ", t["Adam"])

# Delete form the hashTable
del t["Tom"]
print("\nArray format of the hashtable", t.arr)

print("\n=======================================")
#Note :- dictonary is python specific implements hash table

print("\nExample for hash Table in python")
# Declare a dictionary 
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Accessing the dictionary with its key
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])


# Declare and updating a dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

# Initialize the dictionary
my_dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Delete an entry with a specific key
del my_dict['Name']
print("After deleting key 'Name':", my_dict)

# Clear all entries in the dictionary
my_dict.clear()
print("After clearing the dictionary:", my_dict)

# Delete the entire dictionary
del my_dict

# Trying to access the dictionary after deletion will cause an error
# Uncomment the line below to see the error
# print("Trying to access the deleted dictionary:", my_dict)


print("\n=======================================")
print("Heap Example")
print("#-Heap Opreations-#")

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insertKey(self, k):
        # Insert the new key at the end
        self.heap.append(k)
        # Fix the min heap property if it's violated
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.heap) and self.heap[left] < self.heap[i]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)


    def extractMin(self):
        if len(self.heap) <= 0:
            return float("inf")
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        
        return root

    def getMin(self):
        return self.heap[0] if self.heap else float("inf")

    def display(self):
        print(self.heap)
    

    # def visualize(self,val):
    #     dot = Digraph(comment='The MinHeap Tree')

    #     for i in range(len(self.heap)):
    #         dot.node(str(i), str(self.heap[i]))
    #         if i != 0:  # If not the root node
    #             dot.edge(str(self.parent(i)), str(i))

    #     # return dot
    #     # filename = 'D:\ProfNath_PSA_SM\graph\minheap_'+str(val)+'.gv'  # You can change the filename and format as needed
    #     filename = filepath + '\minheap_'+str(val)  # You can change the filename and format as needed
    #     dot.render(filename, format='png', view=True)  # This will create and automatically open a PNG file
    #     print(f"Graph rendered as '{filename}.png'")

heapObj = MinHeap()
heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(45)
print("Heap after inserting all elements")
heapObj.display()
# heapObj.visualize(0)

print("\nExtracting Min", heapObj.extractMin()) # Extracts and prints 2
print("Heap after extracting min", heapObj.display())
heapObj.display()

print("\nGetting Min", heapObj.getMin()) # Gets the minimum element, prints 3
print("Heap after geting min")
heapObj.display()
# heapObj.visualize(1)


print("\nExtracting Min", heapObj.extractMin())# Extracts and prints 3
print("Heap after extracting next min")
heapObj.display()

print("\nGetting Min", heapObj.getMin())# Gets the minimum element, prints 4
print("Heap after geting next min")
heapObj.display()
# heapObj.visualize(2)

# This code defines a `MinHeap` class with methods for CRUD operations:

# - **Create**: The heap is initialized as an empty list.
# - **Read**: `getMin()` returns the smallest element.
# - **Update**: `insertKey()` inserts a new element into the heap.

# ### Understanding the Code

# - **insertKey**: Inserts a new key by appending it to the end of the list and then percolates it up to maintain the heap property.
# - **heapify**: Ensures that the subtree rooted at index `i` is a heap. Primarily used in `extractMin`.
# - **extractMin**: Removes and returns the root (minimum element) of the heap. It places the last element at the root and then calls `heapify` to maintain heap property.
# - **getMin**: Simply returns the element at the root, which is the minimum in a min heap.

# ### Learning Points

# - Heaps are efficient for priority queue operations.
# - They ensure that the element with the highest (or lowest) priority is always at the root.
# - Heaps are not sorted structures, but they do have some order properties.

# Feel free to modify and play around with this code to deepen your understanding. If you have any specific questions or need clarification on any part of the heap implementation, feel free to ask!

#------------------------------------------------#
