import sys


class Getnode:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):

        if self.head == None:
            print("Linked List not present")

        else:
            ptr = self.head

            while ptr != None:
                print(ptr.data, "->", end=" ")
                ptr = ptr.next

            print("None")

    def append(self):

        data = int(input("Enter data: "))

        newNode = Getnode()
        newNode.data = data

        if self.head == None:
            self.head = newNode

        else:
            ptr = self.head

            while ptr.next != None:
                ptr = ptr.next

            ptr.next = newNode

        print(data, "is added")

    def addAtBegin(self):

        data = int(input("Enter data: "))

        newNode = Getnode()
        newNode.data = data

        if self.head == None:
            self.head = newNode

        else:
            newNode.next = self.head
            self.head = newNode

        print(data, "is added at beginning")

    def addAnywhere(self):

        data = int(input("Enter data: "))
        key = int(input("Enter key: "))

        newNode = Getnode()
        newNode.data = data

        if self.head == None:
            print("Linked List not present")

        else:
            ptr = self.head

            while ptr != None:

                if key == ptr.data:
                    break

                ptr = ptr.next

            if ptr == None:
                print("Key not found")

            else:
                ptr1 = ptr.next
                ptr.next = newNode
                newNode.next = ptr1

                print(data, "is added")

    def deleteAtBegin(self):
        if head==None:
            print("list not present")
        else:
            ptr=self.head
            ptr1=ptr.next
            ptr.next=None
            head=ptr1
            print(ptr.data,"is deleted")

    def delAtEnd(self):
        if self.head==None:
            print("list not present")
        else:
            ptr=self.head
            while ptr.next.next!=None:
                ptr1=ptr
                ptr=ptr.next
            ptr1.next=None
            print(ptr.data,"is deleted")

if __name__ == "__main__":

    obj = LinkedList()

    while True:

        print("1. Append")
        print("2. Traverse")
        print("3. Add at begin")
        print("4. Add Anywhere")
        print("5. Delete at begin")
        print("6. Delete at end")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:
            obj.append()

        elif n == 2:
            obj.traverse()

        elif n == 3:
            obj.addAtBegin()

        elif n == 4:
            obj.addAnywhere()

        elif n == 5:
            obj.deleteAtBegin()
        
        elif n == 6:
            obj.delAtEnd()

        elif n == 0:
            sys.exit(0)
