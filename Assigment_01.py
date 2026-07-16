employees = {
    101: {
        "name": "Satya",
        "age": 27,
        "department": "HR",
        "salary": 50000
    }
}

print(employees)


while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search for Employee")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("Add Employee selected.")
        case 2:
            print("View All Employees selected.")
        case 3:
            print("Search for Employee selected.")
        case 4:
            print("Thank you! Exiting the program.")
            break
        case _:
            print("Invalid Choice! Please try again.")