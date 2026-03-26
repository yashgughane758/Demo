exp=float(input("Enter experience in years "))
ls=float(input("Enter number of leaves "))
if(exp>2.5):
    if(ls<30):
        print("Employee will get bonus")
    else:
        print("Employee will not get bonus because number of leaves is more than 30")
else:
    print("Employee will not get bonus because experience is not less than 2.5 years")


