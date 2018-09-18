#Single Linked List code:

class sllExample:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def getSize(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found == True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def printList(self):
        current = self.head
        for x in range(self.getSize()):
            print(x , " " , current.data)
            current = current.get_next()

    def insertAfterIndex(self, index, data):
        if index <= self.getSize():
            current = self.head
            for x in range(0, index + 1, 1):
                
                if x == index:
                    new_node = Node(data)
                    new_node.set_next(current.get_next())
                    current.set_next(new_node)
                else:
                   current = current.get_next() 

    def deleteAfterIndex(self, index):
        if index <= self.getSize():
            current = self.head
            for x in range(0, index + 1, 1):
                if x == index:
                    obsoleteNode = current.next_node
                    current.set_next(current.next_node.next_node)
                    del obsoleteNode
                else:
                   current = current.get_next()

    def deleteFirstNode(self):
        obsoleteNode = self.head
        self.head = self.head.next_node
        del obsoleteNode
        
    def createList(self):
        for x in range(10,0,-1):
            self.insert(x)

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data= data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

