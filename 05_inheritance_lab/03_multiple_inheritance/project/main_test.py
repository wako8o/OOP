from project.employee import Employee
from project.person import Person
from project.teacher import Teacher


p = Person()
e = Employee()
print(p.sleep())
print(e.get_fired())
t = Teacher()
print(t.sleep())
print(t.get_fired())
print(t.teach())
print(isinstance(t, Person))
print(isinstance(t, Employee))
print(isinstance(t, Teacher))
print(isinstance(p, Teacher))
print(isinstance(e, Teacher))
print(isinstance(p, Employee))
print(isinstance(e, Person))
print(isinstance(t, object))
print(isinstance(p, object))
print(isinstance(e, object))
print(isinstance(Teacher, object))
print(isinstance(Employee, object))
print(isinstance(Person, object))
print(isinstance(Teacher, type))
print(isinstance(Employee, type))
print(isinstance(Person, type))
