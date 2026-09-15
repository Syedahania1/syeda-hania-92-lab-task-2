hours=float(input("enter hours worked:"))
rate=float(input("enter hourly rate:"))
if hours<40:
    pay=hours*rate
    print("hours are less than 40")
    print("total pay=",pay)
elif hours ==40:
    pay=hours*rate
    print("hours are equal to 40")
    print("total pay=",pay)
else:
    overtime=hours-40
    total_pay=(40*rate)+(overtime*rate*1.5)
    print("hours are greater than 40")
    print("total pay=",total_pay)