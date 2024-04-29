#if stands for only true value
#in if function we can skip typing true
Has_Good_Credit= True
Has_High_Income= True
is_Criminal= False
if(Has_Good_Credit and Has_High_Income and not is_Criminal):
    print("you are eligible for loan")
else:
    print("you are not eligible for loan application")