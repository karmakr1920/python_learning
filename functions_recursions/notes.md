# 🧠 Functions and Recursion in Python

Welcome! This guide is designed to help students understand the core concepts of **functions** and **recursion** in Python with beginner-friendly explanations, examples, and tips.

---

## 📘 Table of Contents

1. [What is a Function?](#-what-is-a-function)
2. [Why Use Functions?](#-why-use-functions)
3. [How to Define and Call a Function](#-how-to-define-and-call-a-function)
4. [What is Recursion?](#-what-is-recursion)
5. [Recursion Example: Factorial](#-recursion-example-factorial)
6. [Tips for Using Recursion](#-tips-for-using-recursion)
7. [Need Practice?](#-need-practice)
8. [Extra Resources](#-extra-resources)

---

## 🔹 What is a Function?

A **function** is a reusable block of code that performs a specific task.

```python
def greet(name):
    print("Hello", name)

greet("Alice")  # Output: Hello Alice
🔹 Why Use Functions?
✅ Avoid code repetition
✅ Break down large problems
✅ Improve code readability
✅ Enable reuse and testing

🔹 How to Define and Call a Function
python
Copy
Edit
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # Output: 7
🔹 What is Recursion?
Recursion happens when a function calls itself to solve a smaller version of a problem.

Every recursive function must have:

A base case (when to stop)

A recursive call (moving toward the base case)

🔹 Recursion Example: Factorial
The factorial of a number n is:
n! = n × (n-1) × (n-2) × ... × 1

🧾 Code:
python
Copy
Edit
def factorial(n):
    if n == 0:
        return 1  # base case
    else:
        return n * factorial(n - 1)  # recursive call
▶️ How factorial(3) Works:
scss
Copy
Edit
factorial(3)
→ 3 * factorial(2)
→ 3 * (2 * factorial(1))
→ 3 * (2 * (1 * factorial(0)))
→ 3 * (2 * (1 * 1)) → 6
🔹 Tips for Using Recursion
✅ Always define a base case
⚠️ Avoid infinite recursion
⚠️ Deep recursion can cause stack overflow
💡 Sometimes loops (iteration) are simpler

📚 Extra Resources
Python Docs – Functions

Recursion Visualizer (pythontutor.com)

FreeCodeCamp – Recursion Explained

Happy coding! 🚀