def reverse_string(user_input):
    char_list = list(user_input)
    
    left = 0
    right = len(user_input)-1

    while left < right:
        temp = char_list[left]
        char_list[left] = char_list[right]
        char_list[right] = temp

        left = left+1
        right = right-1

    return "".join(char_list) 

user_input = input("Enter a string : ")

print(reverse_string(user_input))