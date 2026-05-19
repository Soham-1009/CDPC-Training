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

class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 100

    def isFull(self):
        if self.top == self.CAPACITY - 1:
            return True
        else:
            return False

    def push(self, ele):
        if self.isFull():
            print("Stack is Full")
        else:
            self.top = self.top + 1
            self.stack.append(ele)
            print(ele, "is pushed")

    def traverse(self):
        for i in range(self.top, -1, -1):
            print(self.stack[i])

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            ele = self.stack[self.top]
            self.stack.pop()
            self.top -= 1
        return ele

    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print(self.stack[self.top])
            
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
            pass

    obj = Stack()
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")
        ch = int(input("Select any Choice: "))
        if ch == 1:
            ele = int(input("Enetr Data: "))
            obj.push(ele)
        elif ch == 2:
            obj.pop()
        elif ch == 3:
            obj.peek()
        elif ch == 4:
            obj.traverse()
        elif ch == 0:
            pass

    obj1 = Queue()
    obj2 = Stack()
    for i in range(obj1.CAPACITY):
        ele = int(input("Enter Element: "))
        obj1.insert(ele)
    for x in range(obj1.CAPACITY):
        ele = obj1.delete()
        obj2.push(ele)
    for x in range(obj1.CAPACITY):
        ele = obj2.pop()
        obj1.insert(ele)
    obj1.traverse()
