hrs = input("Enter hours worked:")
hrly_rate = input("Enter hourly rate:")
hrs = float(hrs)
hrly_rate = float(hrly_rate)
if hrs <= 40:
    reg_hrs = hrs
    gross_pay= hrs * hrly_rate
else:
    reg_hrs = 40
    overtime_hrs = hrs - 40
    gross_pay = (reg_hrs * hrly_rate) + (overtime_hrs * hrly_rate * 1.5)
print(gross_pay)
