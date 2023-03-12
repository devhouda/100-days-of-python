#Day 2 - Understanding Data Types and How to Manipulate Strings

#Concepts Practised: data types, numbers, operations, type conversion, f-strings
##f"your score is {variable}"

#Tip Calculator:
print("Welcome to the tip Calculator!")
amount = float(input("What is the total bill amount?\n$:"))
tip = int(input("How much tip would you like to give?\nPercent:"))
people = int(input("How many people to split the bill?\nPeople:"))
total = ("{:.2f}".format((((amount * (tip / 100)) + amount) / people)))
print(f"Each person should pay: ${total}")