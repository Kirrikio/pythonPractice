class listExample:

    ''' Init '''
    def __init__(self, myList):
        self.myList = myList

    ''' Getting List Data '''
    def printList(self):
        print(self.myList)

    def printListItems(self):
        for x in self.myList:
            print(x)

    def getListLength(self):
        print(len(self.myList))

    #Counts how many times a value appears in list
    def countValueAppears(self, value):
        print(self.myList.count(value))

    def getIndexOfValue(self, value):
        print(self.myList.index(value))

    def reverseList(self):
        self.myList.reverse()
        self.printList()

    #Sorts in ascending order
    def sortList(self):
        self.myList.sort()
        self.printList()

    def sortMethod(a, value):
        
        return(value % 2 == 0)
        
    def sortListWithParam(self):
        self.myList.sort(reverse = True, key = self.sortMethod)
        self.printList()
        
    ''' Adding items '''
    def addItem(self, value):
        self.myList.append(value)
        self.printList()

    def addItemAt(self, index, value):
        self.myList.insert(index, value)
        self.printList()

    def copyList(self):
        copiedList = self.myList.copy()
        print(copiedList)

    def extendList(self, secondList):
        self.myList.extend(secondList)
        self.printList()

    ''' Removing items '''
    def popListIndex(self, x):
        self.myList.pop(x)
        self.printList()

    def removeValue(self, value):
        self.myList.remove(value)
        self.printList()

    def removeItemAt(self, index):
        del self.myList[index]
        self.printList()

    def deleteList(self):
        del self.myList
        try:
            print(self.myList)
        except:
            print("The list has been deleted")

    def emptyList(self):
        self.myList.clear()
        self.printList()
