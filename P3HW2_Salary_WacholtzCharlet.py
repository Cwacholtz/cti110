#Charlet Wacholtz
#07/09/2024
#P3HW2
#A program that calculates an employee's pay

name = input("Enter the employee's name: ")

HoursWorked = float(input("Enter the number of hours worked: "))

PayRate = float(input("Enter the employee's pay rate: "))

if HoursWorked > 40:
    ovtHours = HoursWorked - 40
    
    ovtPay = ovtHours * (PayRate *1.5)

    regPay = 40 * PayRate

    grossPay = regPay + ovtPay


else:
    ovtHours = 0

    ovtPay = 0

    regPay = PayRate *HoursWorked

    grossPay = regPay


print("-" * 40)

print("Employee name:",name,"\n")

print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime":<12}{"Overtime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')

print("-" * 85)

print(f'{HoursWorked:<15}{PayRate:<12}{ovtHours:<12}{ovtPay:<20.2f}{"$"}{regPay:<20.2f}{"$"}{grossPay:<.2f}')



    
