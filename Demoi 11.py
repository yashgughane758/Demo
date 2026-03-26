hsc=float(input("Enetr hsc score "))
cet=float(input("Entr cet score "))
if(hsc>60):
    if(cet>100):
        print("Eigible for addmision")
    else:
        print("Not eiligible because cet score is below 100")
else:
    print("Not eiligible beacuse hsc score is below 60")
    