class Employee:
    def __init__(self,name,post,salary):
        self.name=name
        self.post=post
        self.salary=salary

    def promotion_of_employee(self,promotion,increase_salary):
        self.post=promotion
        self.salary=increase_salary

employee1=Employee("jamal","Manager",40000)
print(f"Employee name is {employee1.name} and His Post is {employee1.post} and his monthly salary is {employee1.salary} taka")
employee1.promotion_of_employee("Director",60000)
print(f"Employee {employee1.name} is promoted to {employee1.post} with {employee1.salary} salary")