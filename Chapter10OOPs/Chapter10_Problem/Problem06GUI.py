import tkinter as tk
from tkinter import messagebox

# 1. Modified Student class (no console input, returns a string)
class Student:
    """
    Holds student data and provides methods to process it.
    """
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def calculate_average(self):
        """Calculates the average of the student's marks."""
        # Use float division (/) for a more accurate average
        return sum(self.marks) / len(self.marks) if self.marks else 0 

    def get_details_string(self):
        """Returns a formatted string with the student's details."""
        avg = self.calculate_average()
        return (
            f"Name: {self.name}\n"
            f"Roll No: {self.roll_no}\n"
            f"Marks: {self.marks}\n"
            f"Average: {avg:.2f}\n"  # Format average to 2 decimal places
            "--------------------\n"
        )

class StudentGUI:
    """
    Manages the main application window and its widgets.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Student Details App 🎓")
        
        self.students = []  # List to hold the student objects
        self.total_students = 0 # Will store the number from the entry field
        
        # --- Create a main frame ---
        main_frame = tk.Frame(root, padx=15, pady=15)
        main_frame.pack()

        # --- Input Frame (for labels and entries) ---
        input_frame = tk.LabelFrame(main_frame, text="Enter Student Data", padx=10, pady=10)
        input_frame.pack()
        
        # --- Labels and Entries (Corrected Grid Layout) ---
        
        # Row 0: Name
        tk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky='w', pady=3)
        self.name_entry = tk.Entry(input_frame, width=30)
        self.name_entry.grid(row=0, column=1, pady=3, columnspan=2)
        
        # Row 1: Roll No
        tk.Label(input_frame, text="Roll No:").grid(row=1, column=0, sticky='w', pady=3)
        self.roll_entry = tk.Entry(input_frame, width=30)
        self.roll_entry.grid(row=1, column=1, pady=3, columnspan=2)

        # Row 2: Total Students
        tk.Label(input_frame, text="Total Students:").grid(row=2, column=0, sticky='w', pady=3)
        self.num_entry = tk.Entry(input_frame, width=30)
        self.num_entry.grid(row=2, column=1, pady=3, columnspan=2)
        
        # Row 3: Marks
        tk.Label(input_frame, text="Marks:").grid(row=3, column=0, sticky='w', pady=3)
        self.mark_entries = []  # List to hold the 5 mark entry widgets
        marks_frame = tk.Frame(input_frame)
        marks_frame.grid(row=3, column=1, columnspan=2)
        
        for i in range(5):
            entry = tk.Entry(marks_frame, width=5)
            entry.grid(row=0, column=i, padx=2)
            self.mark_entries.append(entry)
            
        # --- Add Student Button ---
        # Initial text is generic, will be updated after total is set
        self.add_button = tk.Button(main_frame, text="Add Student", command=self.add_student, font=('Arial', 10, 'bold'))
        self.add_button.pack(pady=10)

        # --- Output Frame (for results) ---
        output_frame = tk.LabelFrame(main_frame, text="All Student Details", padx=10, pady=10)
        output_frame.pack(fill='both', expand=True)
        
        # Scrollbar for the text box
        scrollbar = tk.Scrollbar(output_frame)
        scrollbar.pack(side='right', fill='y')
        
        self.output_text = tk.Text(output_frame, height=15, width=50, state='disabled', wrap='word', yscrollcommand=scrollbar.set)
        self.output_text.pack(fill='both', expand=True)
        scrollbar.config(command=self.output_text.yview)

    def add_student(self):
        """
        Called when the 'Add Student' button is clicked.
        Validates input, creates a Student object, and updates the GUI.
        """
        
        # 1. Get and set the total number of students IF it hasn't been set yet
        if self.total_students == 0:
            try:
                total_str = self.num_entry.get()
                self.total_students = int(total_str)
                if self.total_students <= 0:
                    self.total_students = 0 # Reset on invalid input
                    raise ValueError("Total students must be a positive number.")
                
                # If successful, disable the entry and update button
                self.num_entry.config(state='disabled')
                self.add_button.config(text=f"Add Student (0/{self.total_students})")

            except ValueError as e:
                messagebox.showerror("Invalid Input", f"Please set a valid total number of students first.\n{e}")
                return

        # 2. Check if we have already reached the limit
        if len(self.students) >= self.total_students:
            messagebox.showinfo("Limit Reached", f"You have already added all {self.total_students} students.")
            return

        # 3. Get data from entries and validate
        try:
            name = self.name_entry.get()
            roll_no_str = self.roll_entry.get()
            
            if not name or not roll_no_str:
                raise ValueError("Name and Roll No cannot be empty.")
                
            roll_no = int(roll_no_str)
            
            marks = []
            for entry in self.mark_entries:
                mark_str = entry.get()
                if not mark_str:
                    raise ValueError("All 5 marks must be entered.")
                marks.append(int(mark_str))

        except ValueError as e:
            messagebox.showerror("Invalid Input", f"Error: {e}\nPlease check your inputs.")
            return
        
        # 4. Create Student object and add to list
        new_student = Student(name, roll_no, marks)
        self.students.append(new_student)
        
        # 5. Update the output text box
        self.update_output(new_student)
        
        # 6. Clear entries for the next student
        self.clear_entries()
        
        # 7. Update button text
        count = len(self.students)
        self.add_button.config(text=f"Add Student ({count}/{self.total_students})")
        
        # 8. If we have reached the total, disable button and show final message
        if count == self.total_students:
            self.add_button.config(text=f"All {self.total_students} Students Added", state='disabled')
            messagebox.showinfo("Complete", f"All {self.total_students} student details have been recorded.")

    def clear_entries(self):
        """Clears all input fields."""
        self.name_entry.delete(0, 'end')
        self.roll_entry.delete(0, 'end')
        for entry in self.mark_entries:
            entry.delete(0, 'end')
        self.name_entry.focus()  # Set cursor to name entry for next input

    def update_output(self, student):
        """Appends the new student's details to the output text box."""
        details = student.get_details_string()
        
        self.output_text.config(state='normal')    # Enable writing
        self.output_text.insert('end', details)    # Insert at the end
        self.output_text.config(state='disabled')  # Disable writing

# 3. Main execution block
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = StudentGUI(root)  # Create our application instance
    root.mainloop()  # Start the GUI event loop