class Employee:
    def __init__(self,name,post):
        self.name=name
        self.post=post

    def daily_task(self,task_name):
        print(f"He was assigned for {task_name}")

employee1=Employee("Jamal","Assistant Officer")
print(f"Employee name is {employee1.name} and he is in {employee1.post} post")
employee1.daily_task("assist CEO")

class Manager(Employee):
    def daily_task(self, task_name):
        print(f"He was assigned for {task_name}")
manager1=Manager("Kamal","Manager")
print(f"Employee name is {manager1.name} and he is in {manager1.post} post")
manager1.daily_task("manage all workers")