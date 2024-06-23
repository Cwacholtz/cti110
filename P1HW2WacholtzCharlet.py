#Charlet Wacholtz
#06/23/2024
#P1HW2
#This program calculates and displays travel expenses

print ("This program calculates and displays travel expenses")

print (" ")

print("Enter Budget:", end=" ")
budget = int(input())

print (" ")

print ("Enter your travel destination:", end=" ")
destination = input()

print (" ")

print ("How much do you think you will spend on gas?", end=" ")
gas = int(input())

print (" ")

print ("Approximately, how much will you need for accomodation/hotel?", end=" ")
accomodation = int(input())

print (" ")

print ("Last, how much do you need for food?", end=" ")
food = int(input())

print (" ")

print ("------------Travel Expenses------------")

print ("Location:", destination)

print ("Initial Budget:", budget)

print (" ")

print ("Fuel:", gas)

print ("Accomodation:", accomodation)

print ("Food:", food)

print (" ")

leftovers = budget - gas - accomodation - food 

print ("Remaining Balance:", leftovers)
