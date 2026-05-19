import sys


class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = -1
        self.CAPACITY = 100

    def isFull(self):
        if self.rear == self.CAPACITY - 1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.rear == -1:
            return True
        else:
            return False

    def insert(self, ele):
        if self.isFull():
            print("Queue is Full")
        else:
            self.rear = self.rear + 1
            self.queue.append(ele)
            print(ele, "is inserted")

    def traverse(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])

    def delete(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            ele = self.queue[self.front]
            for i in range(1, self.rear + 1):
                self.queue[i - 1] = self.queue[i]
            self.rear -= 1
            
        return ele

    def peek(self):
        print(self.queue[self.rear])

    # def peek(self):
    #     if self.isEmpty():
    #         print("queue is empty")
    #     else:
    #         print(self.rear)


if __name__ == "__main__":
    obj = Queue()
    while True:
        print("1. Insert")
        print("2. Delete")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")
        ch = int(input("Select any Choice: "))
        if ch == 1:
            ele = int(input("Enter Data: "))
            obj.insert(ele)
        elif ch == 2:
            obj.delete()
        elif ch == 3:
            obj.peek()
        elif ch == 4:
            obj.traverse()
        elif ch == 0:
            sys.exit(0)
