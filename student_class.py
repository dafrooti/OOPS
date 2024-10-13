# getter method
class Student():
    def __init__(self, name, age, height, classes):
        self.name = name
        self.age = age
        self.height = height
        self.classes = classes

# getter method
    def printdetails(self):
        print(self.name, self.age, self.height, self.classes)
# setter method   
    def changedetails(self):
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")
        self.height = input("Enter Height: ")
        self.classes = input("What are your classes: ")
        print(self.name, self.age, self.height, self.classes)

id = Student("Shruti", 16, 5, "History")
# id.printdetails()
id.changedetails()