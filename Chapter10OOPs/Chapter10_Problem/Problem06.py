# Create a class Student with the following attributes: name, roll_no, and marks as list 
# Add a method calculate_average() that returns the average of the marks.
# Add a method display_details() that prints the student’s name, roll number, and average marks.
# Create 3 student objects and display their details.
class Student:
    def __init__(self):
        self.name=input("Enter a name of student ")
        self.roll_no=int(input("Enter a roll number : "))
        self.marks=[]
        print("Enter the marks of 5 ")
        for i in range(1,6):
            mark = int(input(f"Subject {i}: "))
            self.marks.append(mark)
        
    def calculate_average(self):
        return sum(self.marks)//len(self.marks)
    def display_details(self):
        print(f"Name of student  is {self.name}")
        print(f"Rollno of {self.name}  is {self.roll_no}")
        print(f"Marks of {self.name}  is {self.marks}")
        print(f"Average of {self.name}  is {self.calculate_average()}")

s1=Student()
s2=Student()
s3=Student()

s1.display_details()
s2.display_details()
s3.display_details()





    
