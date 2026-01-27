# Reverse words in Sentence

# Method 1
def reverse_words(sentence):
    words = sentence.split()
    rev_words = []

    for word in words:
        rev_words.append(word[::-1])

    return " ".join(rev_words)
print(reverse_words("Python is Powerful"))



# Reverse the order along with each words in sentence
def reverse_order(sentence):
    words = sentence.split()
    words.reverse()

    result = []

    for word in words:
        result.append(word[::-1])
    return " ".join(result)

print(reverse_order("Python is Powerful"))