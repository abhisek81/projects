a = float(input("Enter 1st number :"))
b = float(input("Enter 2nd number :"))
c = input("Enter operator :")

print ("You entered :", a ,"and", b, "and" , c)

if c == '+':
    result = a + b
elif c == '-':
    result = a - b
elif c == '*':
    result = a * b
else:
    result = a / b

print("Result = ", result)