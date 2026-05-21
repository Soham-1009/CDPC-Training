class Parent:
    def __init__(self):
        self.speed=100
        print("cash, gold")
    
    def bike (self):
        print("Splendor+",self.speed)

class Child:
    def __init__(self):
        self.speed=150
        print("cash, gold")
    
    def bike (self):
        print("Splendor+",self.speed)

obj=Child()
obj.bike()