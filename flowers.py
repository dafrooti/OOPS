class Flower():
    def __init__(self, type, size, color, name):
        self.type = type
        self.size = size
        self.color = color
        self.name = name
    
    def writedetails(self):
        self.type = input("Enter type of flower: ")
        self.size = input("Enter the size of the flower: ")
        self.color = input("Enter the color of the flower: ")
        self.name = input("Enter the name of the flower: ")
        print(self.type, self.size, self.color, self.name)

id = Flower("indoor", "small", "white", "flower")
id.writedetails()