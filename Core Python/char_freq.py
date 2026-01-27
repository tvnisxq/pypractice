# Return a string with character frequencies

# Method 1
def char_frequency(s):
    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq
print("---- Simple Dictionary ----")
print(char_frequency("Programming"))


# Method 2
def char_frequency(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
print("---- dict.get() function aplied ----")
print(char_frequency("Programming"))


# Method 3
from collections import Counter
def count_char(s):
    result = dict(Counter(s))
    return result

print("---- Counter Method applied ----")
word = input("Enter the word: ")
print(count_char(word))