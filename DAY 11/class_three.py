# class declaration

class Customer:
    def __init__(self,name,membership_type):
        self.name=name
        self.membership_type=membership_type
        print(f"customer name is {name} and s/he wants to choose {membership_type} membership type")

    def update_membership(self,new_membership):
        self.membership_type=new_membership

Robiul=Customer("Robiul","Diamond")
Robiul.update_membership("Platinum")
print(f"Good News! New customer {Robiul.name} wants to choose {Robiul.membership_type} ")