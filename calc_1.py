def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number")

def get_operator(prompt):
    valid_ops = {"+","-","/","*"}
    while True:
        op = input(prompt).strip()
        if op in valid_ops:
            return op
        print("Please enter valid operator.")

a = get_number("Enter 1st number :")
b = get_number("Enter 2nd number :")
c = get_operator("Enter operator :")

print("You entered :", a , "and", b, "and", c)

has_result = True

if c == '+':
    result = a + b
elif c == '-':
    result = a - b
elif c == '*':
    result = a * b
else:
    if b == 0:
        print("Can not divide by zero")
        has_result = False
    else:
        result = a / b

if has_result:
#print("Result = ", result)
    print(a,c,b,"=", result)