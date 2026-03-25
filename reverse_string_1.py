def reverse_string(user_input):
    char_list = []
    for i in range(len(user_input)-1,-1,-1):
        char_list.append(user_input[i])

    return "".join(char_list) 



user_input = input("Enter a string : ")

print(reverse_string(user_input))