# Create a class programer with Storing 
# information of few programers working in Microsoft.
class Programmer:
    company = "Microsoft"  # Class attribute

    def __init__(self):
        self.name = input("Enter the name of the employee: ")
        self.project = input("Enter the project name: ")
        self.salary = int(input("Enter the salary of the employee: "))

    def print_details(self):
        print("\n--- Programmer Details ---")
        print(f"Company : {self.company}\nName    : {self.name}\nProject : {self.project}\nSalary  : ₹{self.salary}\n")
# Creating objects for two programmers
obj1 = Programmer()
obj1.print_details()

obj2 = Programmer()
obj2.print_details()
