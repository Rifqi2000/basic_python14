class Dog: #class
    #breed: None #property/attribute

    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    def eat(self): #method = function didalam class
        print(self.breed,"itu sedang makan")

    def sleep(self): #method = function didalam class
        print(self.breed,"itu sedang tidur")