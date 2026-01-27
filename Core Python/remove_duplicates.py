# Remove duplicates without using set

# Method 1
def remove_duplicates(arr):
    result = []

    for num in arr:
        if num not in result:
            result.append(num)
    
    result.sort()
    return result
print("---- Auxiliary List method ----")
print(remove_duplicates([1, 2, 2, 3, 5, 5, 5, 4, 3, 6, 6, 7, 7]))
print("Time: O(n²)\nSpace: O(n)")

# Method 2
def remove_duplicates(arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    result.sort()
    return result

print("---- Hashing applied ----")
print(remove_duplicates([1, 2, 2, 3, 5, 5, 5, 4, 3, 6, 6, 7, 7]))
print("Time: O(n log n)\nSpace: O(n)")

def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    result = []

    for word in words:
        result.append(word[::-1])
    
    return " ".join(result)
print(reverse_words("Python is Powerful"))