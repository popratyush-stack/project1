#1
print(type(10))
print(type("hello"))
print(type(3.14))
a=3
b=4
nameee=a>b
print(type(nameee))

#2
a="100"
a=int(a)
a+=50
print(a) 

#3 create a tip calculator take a bill amount and tip percentage,calculate the tip and total 
bill_amount = float(input("Enter bill amount: "))
tip_percentage = float(input("Enter tip percentage: "))
tip = bill_amount * (tip_percentage / 100)
total = bill_amount + tip
print("Tip:", tip)
print("Total:", total)  

#4 check if a number is even or odd using the modulus operator (%)
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:    
    print("Odd")


#5 print "hello {name},you are {age} years old" using f-string formatting
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old")

#6 convert celsius to fahrenheit and display with one decimal place
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.1f}")

#7 create a formatted receipt: ask for 3 items and their prices, display each item and the total cost
items = []
total_cost = 0
for i in range(3):
    item_name = input(f"Enter name of item {i+1}: ")
    item_price = float(input(f"Enter price of item {i+1}: "))
    items.append((item_name, item_price))
    total_cost += item_price

print("\nReceipt:")
for item_name, item_price in items:
    print(f"{item_name}: ${item_price:.2f}")
print(f"Total Cost: ${total_cost:.2f}")


#8 ask the user for a number and print whether if it is positive, negative or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#write a grading system take score and print the grade
score = int(input("Enter score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#ask age and print ticket price
age = int(input("Enter age: "))
if age < 12:
    print("Ticket price: $5")
elif age < 18:
    print("Ticket price: $10")
elif age < 65:
    print("Ticket price: $15")
else:
    print("Ticket price: $10")   

#ask for a username and password.Print "Access granted" only if both are correct
correct_username = "admin"
correct_password = "password123"
username = input("Enter username: ")
password = input("Enter password: ")
if username == correct_username and password == correct_password:
    print("Access granted")
else:
    print("Access denied")
#check if a number is between 1 and 100 (inclusive) using and operator
num = int(input("Enter a number: "))
if num >= 1 and num <= 100:
    print("Number is between 1 and 100")
else:
    print("Number is out of range")

#write a program that checks if a year is a leap year (divisible by 4 but not by 100, or divisible by 400)
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year")
else:
    print("The year is not a leap year")
