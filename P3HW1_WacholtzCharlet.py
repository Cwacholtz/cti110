#Charlet Wacholtz
#07/07/2024
#P3HW1
#This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = input('Enter grade for Module 1: ')

mod_2 = input('Enter grade for Module 2: ')

mod_3 = input('Enter grade for Module 3: ')

mod_4 = input('Enter grade for Module 1: ')

mod_5 = input('Enter grade for Module 5: ')

mod_6 = input('Enter grade for Module 6: ')

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
add = sum(grades)
avg = sum(grades) / len(grades)

print("Lowest Grade: ", low)

print ("Highest Grade: ", high)

print ("Sum of Grades: ", add)

print ("Average: ", avg)

# determine letter grade for average


if (avg >= 90 and avg <= 100):
    print('Your grade is: A')
        
elif (avg >= 80 and avg <= 79):
    print('Your grade is: B')

elif (avg >= 70 and avg <= 69):
    print('Your grade is: C')

elif (avg >= 60 and avg <= 59):
    print('Your grade is: D')

else:
    print ('Your grade is: F')
    
# TO DO: finish this





