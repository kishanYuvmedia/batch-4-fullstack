class myClass:
    def __init__(self, name,age,city):
        self.myName = name
        self.myAge = age
        self.myCity = city

    def printName(self):
        return f"Hello, {self.myName}!"
    def printAge(self):
        return f"You are {self.myAge} years old."
    def printCity(self):
        return f"You live in {self.myCity}."

myObj = myClass("John", 30, "New York")
print(myObj.printName())
print(myObj.printAge())
print(myObj.printCity())