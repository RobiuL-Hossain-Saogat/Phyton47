# creating a class

class Room:
    # properties declaration
    length=0
    width=0

    # defining a function
    def calculate_area(self):
        print("Area of room is : ",self.length*self.width)



# # create object from room class
# drawing_room=Room()

# # assigning value
# drawing_room.length=20
# drawing_room.width=15

# # accessing the method
# drawing_room.calculate_area()

bed_room=Room()
bed_room.length=10
bed_room.width=10
bed_room.calculate_area()