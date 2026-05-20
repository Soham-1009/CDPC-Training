import sys


class BST:
    def __init__(self, key):
        self.leftchild = None
        self.rightchild = None
        self.data = key

    def insert(self, key):
        if self.data is None:
            self.data = key
            return
        elif self.data == key:
            return
        else:
            if key < self.data:
                if self.leftchild:
                    self.leftchild.insert(key)
                else:
                    self.leftchild = BST(key)
            elif key > self.data:
                if self.rightchild:
                    self.rightchild.insert(key)
                else:
                    self.rightchild = BST(key)

    def inorder(self):
        if self.leftchild:
            self.leftchild.inorder()
        print(self.data, end=" -> ")
        if self.rightchild:
            self.rightchild.inorder()

    def preorder(self):
        print(self.data, end=" -> ")
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightchild:
            self.rightchild.preorder()

    def postorder(self):
        if self.leftchild:
            self.leftchild.postorder()
        if self.rightchild:
            self.rightchild.postorder()
        print(self.data, end=" -> ")

    def search(self, key):
        if self.data == key:
            return True
        elif key < self.data:
            if self.leftchild:
                return self.leftchild.search(key)
            else:
                print("key not found")
        else:
            if self.rightchild:
                return self.rightchild.search(key)
            else:
                print("key not found")


if __name__ == "__main__":
    root = BST(None)
    while True:
        print("\n1. Insert")
        print("2. Inorder")
        print("3. Preorder")
        print("4. Postorder")
        print("5. Search")
        print("0. Exit")

        n = int(input("Select any choice:"))
        if n == 1:
            # root.insert()
            arr = [36, 26, 46, 21, 31, 11, 24, 41, 56, 51, 36, 66]
            for i in range(len(arr)):
                root.insert(arr[i])
        if n == 2:
            root.inorder()
        if n == 3:
            root.preorder()
        if n == 4:
            root.postorder()
        if n == 5:
            key = int(input("Enter key to search: "))
            if root.search(key):
                print("Key found")
            else:
                print("Key not found")
        if n == 0:
            sys.exit(0)
