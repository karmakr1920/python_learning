# 1. Reverse a string using slicing.

my_str= "Python is awesome"
rev_str= my_str[::-1]
print(rev_str)
#output ==> emosewa si nohtyP

# 2. Count the number of vowels in a string.
vowels = "aeiou"
sentence = "I'm learning the basics of Python"
count = 0
# for vowel in sentence:
#     if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
#         count += 1
for char in sentence:
    if char in vowels:
        count += 1
print(count)

# 3. Check if a string is a palindrome.
is_palindrome = "Naveen"

# Normalize the string
normalized = is_palindrome.lower()

# Check palindrome
if normalized == normalized[::-1]:
    print("Yes")
else:
    print("No")

# 4. Extract the domain from an email address.

# email = "example@gmail.com"
# domain = email.split("@")[1]
# print("Domain:", domain)
def extract_domain(email):
    if "@" in email and "." in email.split("@")[-1]:
        return email.split("@")[1]
    else:
        return "Invalid email format"

print(extract_domain("hello@github.io"))  # github.io
print(extract_domain("invalidemail.com"))  # Invalid email format


words = my_str.split()
title_case = ' '.join(word[0].upper() + word[1:] if len(word) > 0 else '' for word in words)
print(title_case)

