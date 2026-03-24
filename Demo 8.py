tl=int(input("Enter total lecture "))
ta=int(input("Enter total lecture attended "))
pa=(ta/tl)*100
print("percentage of attended lecture=",pa)
if(pa>=75):
    print("Eiligible for exam")
elif(pa>=60 and pa<=74.99):
    print("Submit assignment and then eiligible")
elif("pa<=40 and pa<=50.99"):
    print("Attend extra lecture,submit assignment and then eiligible")
else:
    print("Try next year")