def is_palindrome(x):
    original = x
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit 
        x = x // 10   
    
    if original == reversed_num:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
x = int(input("Enter an integer : "))

print(is_palindrome(x))