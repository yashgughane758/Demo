nod=int(input("Enetr of days "))
age=float(input("Enter age "))
gender=input("Enter gender m for male and f for female ")
if(age>=18 and age<=40 and gender=='M' or gender=='m'):
    salary=nod*800
    print("salary of a person=",salary)
elif(age>=18 and age<=40 and gender=='F' or gender=='f'):
    salary=nod*900
    print("salaruy of a person=",salary)
elif(age>=41 and age<=60 and gender=='M' or gender=='m'):
    salary=nod*1000
    print("salafry of a person=",salary)
elif(age>=41 and age<=60 and gender=='F' or gender=='f'):
    salary=nod*1100
    print("salary of a person=",salary)
else:
    print("not working")