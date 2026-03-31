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
