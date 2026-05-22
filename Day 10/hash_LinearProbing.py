class LinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None]*size
        # self.table=[ for i in range (size)]

    def hashfunction(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hashfunction(key)
        while self.table[index] is not None:
            index = (index+1) % self.size
        self.table[index] = key

    def display(self):
        for i in range(10):
            print(self.table[i])


h = LinearProbing(10)
h.insert(15)
h.insert(25)
h.insert(35)
h.display()
