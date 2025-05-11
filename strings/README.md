# 📘 Python Strings – Notes & Practice

## 🔍 What Are Strings?

Strings are **sequences of characters** used to store and represent text. In Python, they are enclosed in single (`' '`) or double (`" "`) quotes.

```python
greeting = "Hello, World!"
````

---

## ✅ Why Strings Matter

* Used for **displaying messages**, user input, file operations, etc.
* Powerful built-in methods for formatting, searching, manipulating, and validating text.
* Mastery of strings is essential for **web development**, **data processing**, and **automation**.

---

## 🔧 Common String Operations

| Operation     | Example             | Output         |
| ------------- | ------------------- | -------------- |
| Indexing      | `s[0]`              | `'H'`          |
| Slicing       | `s[1:5]`            | `'ello'`       |
| Length        | `len(s)`            | `13`           |
| Concatenation | `'Hello' + 'World'` | `'HelloWorld'` |
| Repetition    | `'ha'*3`            | `'hahaha'`     |
| Membership    | `'H' in s`          | `True`         |
| Iteration     | `for ch in s:`      | each character |

---

## 🧰 String Methods

### 📝 Case Conversion

```python
s.lower()       # lowercase
s.upper()       # uppercase
s.title()       # Title Case
s.capitalize()  # Capitalize first letter
```

### 🔎 Searching and Checking

```python
s.find('o')           # First index of 'o'
s.startswith('He')    # True
s.endswith('!')       # True
s.count('l')          # Count of 'l'
```

### 🧹 Cleaning and Modifying

```python
s.strip()         # Remove surrounding whitespace
s.replace('l', 'x') # Replace characters
s.split(',')       # Split into list by comma
' '.join(list)     # Join list with space
```

### ✅ Validation

```python
s.isdigit()     # True if all characters are digits
s.isalpha()     # True if all characters are letters
s.isalnum()     # Letters and numbers only
s.isspace()     # True if only whitespace
```

---

## 💡 String Formatting

### 🔧 f-Strings (Recommended)

```python
name = "John"
age = 22
print(f"My name is {name} and I am {age} years old.")
```

### 🧱 `.format()` Method

```python
"{} scored {} marks".format("Alice", 95)
```

---

## 🧪 Practice Problems

1. Reverse a string using slicing.
2. Count the number of vowels in a string.
3. Check if a string is a palindrome.
4. Extract the domain from an email address.
5. Convert a sentence to title case without using `.title()`.

---

## 🚀 Mini Project Ideas

* **Email Validator**: Check if user input is a valid email using basic string methods.
* **Word Counter**: Input a paragraph and count the frequency of each word.
* **Text Formatter**: Take user input and return it in uppercase, lowercase, and title case formats.

---

## 📚 References

* [Python `str` documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
* [Real Python - Working with Strings](https://realpython.com/python-strings/)

---

Happy Coding! 💻✨
