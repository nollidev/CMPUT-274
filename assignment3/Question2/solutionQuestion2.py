# Name: Nathan Edillon
# ccid: nedillon
# studentId: nedillon
# operating system: Fedora Linux 41
# python version: 3.13.0

# Starter Code from https://www.geeksforgeeks.org/python-linked-list/
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)
            
        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position = position+1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    # Update node of a linked list at a given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0

    # Print method for the linked list
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()
    
    # Removes all duplicate nodes from the linked list
    def remove_duplicates(self):
        current_node = self.head
        duplicates = [current_node.data] # starting with first value in list
        while(current_node.next):
            if current_node.next.data not in duplicates: # record dupes then cycle
                duplicates.append(current_node.next.data) 
                current_node = current_node.next
            else:
                current_node.next = current_node.next.next # reassign pointer to next next

    # Merges all nodes from llist2 into the linked list object, maintains sorted order
    def merge(self, llist2):
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = llist2.head # append second list onto back of first list
        
        current_node = self.head
        while(current_node.next):
            if (current_node.data > current_node.next.data):
                a, b = current_node.data, current_node.next.data # assign a > b
                current_node.data, current_node.next.data = b, a # then swap a < b
                current_node = self.head # reset list traversal
            else:
                current_node = current_node.next

def main():
    llist_nodes = input().split()
    if llist_nodes[0] == 'duplicate':
        llist = LinkedList()
        for i in range(1, len(llist_nodes)):
            llist.insertAtEnd(int(llist_nodes[i]))
        llist.remove_duplicates()
        llist.printLL()  
    else:
        llist1 = LinkedList()
        llist2 = LinkedList()
        llist2_index = llist_nodes.index("llist2")
        for i in range (1, llist2_index):
            llist1.insertAtEnd(int(llist_nodes[i]))
        for i in range(llist2_index + 1, len(llist_nodes)):
            llist2.insertAtEnd(int(llist_nodes[i]))
        llist1.merge(llist2)
        llist1.printLL()

if __name__ == "__main__":
    main()
