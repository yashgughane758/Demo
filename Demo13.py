mn=int(input("Enter month number "))
if(mn==1 or mn==3 or mn==5 or mn==7 or mn==8 or mn==10 or mn==12):
    print("It has 31 days")
elif(mn==4 or mn==6 or mn==9 or mn==11):
    print("It has 30 days")
elif(mn==2):
    print("It has 28 or 29 days")
else:
    print("Invalid month number")