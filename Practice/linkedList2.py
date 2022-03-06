class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.prev = None
    
    def insert(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.prev = new_node
        else:
            self.prev.next = new_node
            self.prev = self.prev.next
    
    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node
    
    def printLinkedList(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next