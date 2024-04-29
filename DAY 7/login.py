login_attempt=0
while(login_attempt<=3):
    username=input("Enter the Username : ")
    password=input("Enter the Password : ")
    if username=="Robiul" and password=="123":
        print(f"Welcome {username}")
        break
    else:
        print("Please try again")
        login_attempt=login_attempt+1
        continue
else:
    print("The system has been locked")

