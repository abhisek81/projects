def reverse_string(string_input):
    result = ''
    for i in range(len(string_input)-1,-1,-1):
        result = result+string_input[i]

    return result


string_input = input("Enter a string : ")

print(reverse_string(string_input))