salary=float(input("enter salary of the person: "))
if salary>20000:
    tax=0.5*salary
elif salary>10000:
    tax=0.2*salary
else:
    tax=0.1*salary
print("tax deducted is:",tax)
