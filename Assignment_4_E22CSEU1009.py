class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

def print_employee_data(employees):
    for employee in employees:
        print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

def main():
    employee_data = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        sorted_data = sorted(employee_data, key=lambda x: x.age)
    elif choice == 2:
        sorted_data = sorted(employee_data, key=lambda x: x.name)
    elif choice == 3:
        sorted_data = sorted(employee_data, key=lambda x: x.salary)
    else:
        print("Invalid choice")
        return
    
    print("Sorted Employee Data:")
    print_employee_data(sorted_data)

if __name__ == "__main__":
    main()
