#Charlet Wacholtz
#P4LAB2
#07/11/2024
#This program will display a multiplication table

keep_going = "yes"

while keep_going.lower() == "yes" :

    num = int(input("Enter an integer: "))
    print("\n")

    if num >= 0:
        for i in range(1, 12, + 1):
            print(f'{num} * {i} = {num * i}')
            print("\n")
    else: 
            print("This program does not handle negative numbers")
            print("\n")

    keep_going = input("Would you like to run the program again? Enter yes or no: ")

print("The program has ended!") 
