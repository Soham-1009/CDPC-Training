import sys

# Node Class
class getNode:

    def __init__(self):

        self.data = None
        self.next = None


# Queue Class
class Queue:

    def __init__(self):

        self.front = None
        self.rear = None

    # ENQUEUE Operation
    def enqueue(self):

        data = int(input("Enter data : "))

        newnode = getNode()

        newnode.data = data

        # If queue is empty
        if self.front == None:

            self.front = newnode
            self.rear = newnode

        else:

            self.rear.next = newnode

            self.rear = newnode

        print(data, "is inserted")

    # DEQUEUE Operation
    def dequeue(self):

        if self.front == None:

            print("Queue Underflow")

        else:

            ptr = self.front

            self.front = self.front.next

            # If queue becomes empty
            if self.front == None:

                self.rear = None

            print(ptr.data, "is deleted")

    # PEEK Operation
    def peek(self):

        if self.front == None:

            print("Queue is empty")

        else:

            print("Front element is :", self.front.data)

    # DISPLAY Queue
    def display(self):

        if self.front == None:

            print("Queue is empty")

        else:

            ptr = self.front

            print("\nQueue Elements:")

            while ptr != None:

                print(ptr.data, "->", end=" ")

                ptr = ptr.next

            print("NULL")


# Main Function
if __name__ == '__main__':

    obj = Queue()

    while True:

        print("\n1.Enqueue")
        print("2.Dequeue")
        print("3.Peek")
        print("4.Display")
        print("0.Exit")

        n = int(input("Enter your choice : "))

        if n == 1:

            obj.enqueue()

        elif n == 2:

            obj.dequeue()

        elif n == 3:

            obj.peek()

        elif n == 4:

            obj.display()

        elif n == 0:

            sys.exit(0)