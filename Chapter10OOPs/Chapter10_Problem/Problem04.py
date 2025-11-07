#Problwm4:Add a static method in problem-2(Calculator) to greet the user with Hello
#Problem2:WAP class Calculator capable of finding square,cube,and Square_root of number
class Calculator:
    @staticmethod
    def greet():
        print("Hello")

    def __init__(self):
        print("Calculator started")  # Constructor runs first when object is created

    def square(self, num):
        return num * num

    def cube(self, num):
        return num * num * num

    def square_root(self, num):  
        return num ** 0.5


num = int(input("Enter a number: "))

Calculator.greet()  # Greet the user
calc = Calculator()

print(f"Square of {num} is: {calc.square(num)}")
print(f"Cube of {num} is: {calc.cube(num)}")
print(f"Square root of {num} is: {calc.square_root(num):.2f}")
