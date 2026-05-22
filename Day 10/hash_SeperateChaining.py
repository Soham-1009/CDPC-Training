class hashtable:
    def __init__(self, size):
        self.size = size
        self.table = []
        # self.table=[ for i in range (size)]
        for i in range(size):
            self.table.append([])

    def hashfunction(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hashfunction(key)
        self.table[index].append(key)

    def display(self):
        for i in range(10):
            print(self.table[i])


h = hashtable(10)
h.insert(15)
h.insert(25)
h.insert(35)
h.display()
