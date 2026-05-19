import sys

class getNode:

    def __init__(self):

        self.left = None
        self.data = None
        self.right = None


class DoubleLinkedList:

    def __init__(self):
        self.head = None

    def append(self):
        data = int(input("Enter the data : "))
        newnode = getNode()
        newnode.data = data
        if self.head is None:
            self.head = newnode
        else:
            ptr = self.head
            while ptr.right != None:
                ptr = ptr.right
            ptr.right = newnode
            newnode.left = ptr
            print(data, "is added")

    def traverse(self):

        if self.head == None:
            print("List is empty")
        else:
            ptr = self.head
            while ptr != None:
                print(ptr.data, "<->", end=" ")
                ptr = ptr.right
            print("NULL")

    def addAtbeginning(self):
        data = int(input("Enter the data : "))
        newnode = getNode()
        newnode.data = data
        if self.head == None:
            self.head = newnode
        else:
            newnode.right = self.head
            self.head.left = newnode
            self.head = newnode
            print(data, "is added")


    def addAtbetween(self):
        data = int(input("Enter the data : "))
        key = int(input("Enter data after inserted : "))
        newnode = getNode()
        newnode.data = data
        if self.head == None:
            self.head = newnode
        else:
            ptr = self.head
            while ptr != None:
                if ptr.data == key:
                    break
                ptr = ptr.right
            if ptr == None:
                print("Key not found")
            else:
                ptr1 = ptr.right
                ptr.right = newnode
                newnode.left = ptr
                newnode.right = ptr1
                if ptr1 != None:
                    ptr1.left = newnode
                print(data, "is added")

    def deleteAtbeginning(self):
        if self.head == None:
            print("List not present")
        else:
            ptr = self.head
            ptr1 = ptr.right
            if ptr1 != None:
                ptr1.left = None
            self.head = ptr1
            print(ptr.data, "is deleted")

    def deleteAtEnd(self):
        if self.head == None:
            print("List not present")
        elif self.head.right == None:
            print(self.head.data, "is deleted")
            self.head = None
        else:
            ptr = self.head
            while ptr.right != None:
                ptr1 = ptr
                ptr = ptr.right
            ptr1.right = None
            print(ptr.data, "is deleted")


if __name__ == '__main__':
    obj = DoubleLinkedList()
    while True:
        print("\n1.Append")
        print("2.Traverse")
        print("3.Add at Beginning")
        print("4.Add At Between")
        print("5.Delete At Beginning")
        print("6.Delete At End")
        print("0.Exit")
        n = int(input("Enter your choice : "))
        if n == 1:
            obj.append()
        elif n == 2:
            obj.traverse()
        elif n == 3:
            obj.addAtbeginning()
        elif n == 4:
            obj.addAtbetween()
        elif n == 5:
            obj.deleteAtbeginning()
        elif n == 6:
            obj.deleteAtEnd()
        elif n == 0:
            sys.exit(0)