class Animal:
    def speak(self):
        print("sound")

class Dog(Animal):
    def speak(self):
        print("woof woof !!!")

class Cat(Animal):
    def speak(self):
        print("Meowwww !!!")

a=Dog()
b=Cat()
a.speak()
b.speak()

