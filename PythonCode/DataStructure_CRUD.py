
# import sys
# print(sys.path)

from graphviz import Digraph

filepath = "D:\ProfNath_PSA_SM\graph\\"

# Arrays in Python are represented using lists
array_example = [1, 2, 3, 4, 5]

# Operations
array_example.append(6)  # Insert
array_example[2] = 10   # Modify
# array_example.remove(5)
del array_example[1]    # Delete

print("Array Example:", array_example)

#---------------------------------------------#

# Lists are dynamic arrays in Python
list_example = [10, 20, 30, 40, 50]

# Operations
list_example.append(60)     # Insert
list_example[2] = 100       # Modify
list_example.remove(40)     # Delete

print("List Example:", list_example)

#---------------------------------------------#

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            return
        prev.next = current.next
        current = None

    def visualize(self):
        dot = Digraph(comment='The Linked List')

        current = self.head
        i = 0
        while current:
            dot.node(str(i), str(current.data))
            if i > 0:
                # Add an edge from the previous node to this one
                dot.edge(str(i - 1), str(i))
            current = current.next
            i += 1

        # Render the graph to a file
        filename = filepath +'linked_list'
        dot.render(filename, format='png', view=True)
        print(f"Linked list visualization rendered as '{filename}.png'")

# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print("Original linked list:")
linked_list.display()

linked_list.insert_at_beginning(0)
print("\nLinked list after inserting at the beginning:")
linked_list.display()

linked_list.insert_after_node(linked_list.head.next, 10)
print("\nLinked list after inserting after a specific node:")
linked_list.display()

linked_list.delete_node(2)
print("\nLinked list after deleting a node:")
linked_list.display()
linked_list.visualize()
#--------------------------------------------------#

# Using Python list as a stack
stack_example = []

# Operations
stack_example.append(10)  # Push
stack_example.append(20)
stack_example.append(30)
stack_example.append(40)
stack_example.append(50)
stack_example.append(60)
stack_example.pop()     # Pop
stack_example.pop()     # Pop
stack_example.pop()     # Pop

print("Stack Example:", stack_example)

#--------------------------------------------------------#

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
    

    def generate_graph(self,val):
        dot = Digraph(comment='The MinHeap Tree')

        for i in range(len(self.heap)):
            dot.node(str(i), str(self.heap[i]))
            if i != 0:  # If not the root node
                dot.edge(str(self.parent(i)), str(i))

        # return dot
        # filename = 'D:\ProfNath_PSA_SM\graph\minheap_'+str(val)+'.gv'  # You can change the filename and format as needed
        filename = filepath + '\minheap_'+str(val)  # You can change the filename and format as needed
        dot.render(filename, format='png', view=True)  # This will create and automatically open a PNG file
        print(f"Graph rendered as '{filename}.png'")

heapObj = MinHeap()
heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(45)

print(heapObj.extractMin()) # Extracts and prints 2
print(heapObj.getMin()) # Gets the minimum element, prints 3
heapObj.generate_graph(1)

print(heapObj.extractMin())
print(heapObj.getMin())
heapObj.generate_graph(2)

# This code defines a `MinHeap` class with methods for CRUD operations:

# - **Create**: The heap is initialized as an empty list.
# - **Read**: `getMin()` returns the smallest element.
# - **Update**: `insertKey()` inserts a new element into the heap.
# - **Delete**: `extractMin()` removes and returns the smallest element.

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

