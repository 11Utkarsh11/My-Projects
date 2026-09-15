class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print("Employee is working")

class Developer(Employee):
    def __init__(self, name, salary, programming_lang):
        super().__init__(name, salary)
        self.programming_lang = programming_lang

    def work(self):
        print(f"{self.name} is writing {self.programming_lang} code")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def work(self):
        print(f"{self.name} is managing a team of {self.team_size}")

class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def all_employees(self):
        for employee in self.employees:
            print(f"Name: {employee.name}\nSalary: {employee.salary}")

    def all_work(self):
        for employee in self.employees:
            employee.work()

# Create employees

employee1 = Employee("Utkarsh", 45000)
employee2 = Employee("Rahul", 50000)

developer1 = Developer("Aman", 60000, "Python")
developer2 = Developer("Rohit", 65000, "JavaScript")

manager1 = Manager("Priya", 80000, 6)
manager2 = Manager("Neha", 90000, 10)


# Create employee management system

company = EmployeeManagement()


# Add employees

company.add_employee(employee1)
company.add_employee(developer1)
company.add_employee(developer2)
company.add_employee(manager1)
company.add_employee(manager2)


# Display all employees

company.all_employees()


# Make all employees work

company.all_work()


# Remove an employee

company.remove_employee(developer2)


# Display employees again

company.all_employees()


# Make all employees work again

company.all_work()


# Bonus: Try removing an employee who isn't in the company

company.remove_employee(developer2)