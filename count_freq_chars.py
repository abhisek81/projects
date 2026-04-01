def count_freq_chars(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] = freq[ch]+1
        else:
            freq[ch] = 1
    return freq

s = input("Enter a string : ")
print(count_freq_chars(s))

