import sys

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
            el=self.stack[self.top]
            self.stack.pop()
            self.top-=1
        return el

    def peek(self):
        print(self.top)


if __name__ == "__main__":
    obj = Stack()
    while True:
        arr=[1,2,3,4,5]
        rev=[]
        for i in range(len(arr)):
            obj.push(arr[i])
        for i in range(len(arr)):
            rev.append(obj.pop())
    print(rev)   