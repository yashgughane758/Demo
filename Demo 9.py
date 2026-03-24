bill=float(input("Enter bill amounnt"))
if(bill>5000):
    discount=0.10*bill
    fb=bill-discount
    print("After discount bill amount=",fb)
elif(bill>=3500 and bill<=5000):
    discount=0.05*bill
    fb=bill-discount
    print("After discount bill amount")
elif(bill>=2000 and bill<=3499):
    print("After discont bill amount")
else:
    print("No discount")