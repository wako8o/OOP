class Employee:

    def __init__(self, id_:int, first_name:str,last_name:str, salary:int):
        self.id = id_
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        salary = self.salary * 12
        return salary

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary

employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())
