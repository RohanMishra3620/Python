#can you changr the self Parameter inside a class
#to something else (say" harry").try changing self
#to "slf" or "harry" and see the effect 
class Programmer:
    company = "Microsoft"  # Class attribute

    def __init__(slf):
        slf.name = input("Enter the name of the employee: ")
        slf.project = input("Enter the project name: ")
        slf.salary = int(input("Enter the salary of the employee: "))

    def print_details(harry):
        print("\n--- Programmer Details ---")
        print(f"Company : {harry.company}\nName    : {harry.name}\nProject : {harry.project}\nSalary  : ₹{harry.salary}\n")
# Creating objects for two programmers
obj1 = Programmer()
obj1.print_details()

obj2 = Programmer()
obj2.print_details()
