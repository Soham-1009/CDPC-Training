class LinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hashfunction(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hashfunction(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hashfunction(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return "Not found"

    def delete(self, key):
        index = self.hashfunction(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

    def display(self):
        print(self.table)


h = LinearProbing(10)
h.insert(1,"Hamza")
h.insert(2,"Yalina")
h.insert(3,"Dawood")

print(h.search(1))

h.display()
h.delete(3)
h.display()
