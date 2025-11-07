#WAP class Calculator capable of finding square,cube,and Square_root of number
class Calculator:
    def __init__(self):
        print("Calculator start")
    def square(self,num):
        return num * num
    def cube(self,num):
        return num * num * num

    def square_root(self,num):  
        return num ** 0.5
num=int(input("Enter a number: "))
calc = Calculator()
print(f"Square of {num} is: {calc.square(num)}\nCube of {num} is: {calc.cube(num)}\nSquareroot of {num} is: {calc.square_root(num):2f}\n")    