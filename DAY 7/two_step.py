login_attemp=0
while(login_attemp<2):
 username=input("Enter the username : ")
 password=input("Enter the password : ")


 if username=="robiul" and password=="open":
    print('''A verification code has been sent to your mobile 
number. please enter the code to verify our account''')
 else:
    print("Yor Username and Password is Incorrect")
    login_attemp=login_attemp+1
    break
    
    
 verify_attempt=0
 while(verify_attempt<3):
    verification_code=int(input("Enter the verification code : "))

    if verification_code==12345678:
        print("Your Log in Approved")
        break
    else:
        print("Please enter correct verification code")
        verify_attempt=verify_attempt+1
        continue
 else:
    print("Your verification has been failed")
    break