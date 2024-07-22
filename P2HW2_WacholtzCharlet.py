#Charlet Wacholtz
#07/07/2024
#P2HW2
#A program that lists grades

module1 = input("Enter grade for Module 1: ")

module2 = input("Enter grade for Module 2: ")

module3 = input("Enter grade for Module 3: ")

module4 = input("Enter grade for Module 4: ")

module5 = input("Enter grade for Module 5: ")

module6 = input("Enter grade for Module 6: ")

grades = [module1, module2, module3, module4, module5, module6]

print(" ")

print("------------Results------------")

print("Lowest Grade: ", min(grades))

print ("Highest Grade: ", max(grades))

print ("Sum of Grades: ", sum(grades))

average = sum(numbers) / len(numbers)

print ("Average: ", average)

print("--------------------------------")
