import sys


class Getnode:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList_Stack:
    def __init__(self):
        self.head = None
        self.top=None

    def peek(self):

        if self.top==None:
            print("stack is empty")
        else:
            print(self.top.data)


    def push(self):
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
            self.top=newNode
        print(data, "is added")

    def pop(self):
        if self.head==None:
            print("list not present")
        else:
            ptr=self.head
            while ptr.next.next!=None:
                ptr1=ptr
                ptr=ptr.next
            ptr1.next=None
            self.top=ptr1
            print(self.top,"is deleted")

    def traverse(self):
        if self.head == None:
            print("Linked List not present")
        else:
            ptr = self.head
            while ptr != None:
                print(ptr.data, "--")
                ptr = ptr.next
            print("None")

if __name__ == "__main__":

    obj = LinkedList_Stack()

    while True:

        print("1. push")
        print("2. pop")
        print("3. peek")
        print("4. traverse")
        print("0. exit")

        n = int(input("Select any choice: "))

        if n == 1:
            obj.push()

        elif n == 2:
            obj.pop()

        elif n == 3:
            obj.peek()

        elif n == 4:
            obj.traverse()  

        elif n == 0:
            sys.exit(0)
