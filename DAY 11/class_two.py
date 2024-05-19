# assigning player class

class Player:

    # using constructor
    def __init__(self,shirt_no,position):
        self.shirt_no=shirt_no
        self.position=position
        # print(f"Messi shirt no is {shirt_no} and his position is {position}")

    def shot(self,times):
        print(f"shots total {times} numbers of occassion")

Messi=Player(10,"RW")
print(f"Messi shirt no is {Messi.shirt_no} and his position is {Messi.position}")
Messi.shot(4)