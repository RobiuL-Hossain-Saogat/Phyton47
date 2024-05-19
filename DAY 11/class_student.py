class Student:
    def __init__(self,name,class_roll,class_no):
        self.name=name
        self.class_roll=class_roll
        self.class_no=class_no

Student1=Student("Robiul",20,7)
print(f"The student name is {Student1.name} and his Class Roll is {Student1.class_roll} and he stays in class no : {Student1.class_no}")
