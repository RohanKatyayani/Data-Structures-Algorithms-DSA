# A String is a sequence of Characters
# Strings are immutable in python, once created, cannot be changed in place
# common operations: indexing, slicing, concatenation, searching, and reversing.

# Todo 1: Check if a String is Palindrome (A String that reads the same forward and backwards)

def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("racecar")) # True
print(is_palindrome("hello")) # False

# Todo 2: Count Vowels and Consonants

def count_vowels_consonants(s: str):
    vowels = set("aeiouAEIOU")
    vowel_count = 0
    consonant_count = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

print(count_vowels_consonants("Hello World!")) # Vowels = 3, Consonants = 7

# Todo 3: Reverse words in a sentence

def reverse_string(sentence: str) -> str:
    words = sentence.split()
    return " ".join(reversed(words))

print(reverse_string("Data Structures and Algorithms")) # Algorithms and Structures Data
