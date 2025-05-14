## 📝 What is a List?

A **list** is a built-in Python data structure used to store **multiple items** in a **single variable**. Lists are:

* **Ordered**
* **Mutable** (can be changed)
* **Allow duplicates**
* Can contain **mixed data types**

```python
my_list = [1, 2, 3, 'apple', True]
```

---

## 🔧 Creating Lists

```python
empty_list = []
numbers = [1, 2, 3, 4]
mixed = [1, "two", 3.0, False]
```

---

## 📌 Common List Operations

### ✅ Accessing Elements

```python
numbers = [10, 20, 30]
print(numbers[0])  # 10
print(numbers[-1]) # 30
```

### ✅ Modifying Elements

```python
numbers[1] = 25
```

### ✅ Adding Elements

```python
numbers.append(40)
numbers.insert(1, 15)
```

### ✅ Removing Elements

```python
numbers.remove(25)  # removes first occurrence
popped = numbers.pop()  # removes last item
```

### ✅ Slicing

```python
sublist = numbers[1:3]  # from index 1 to 2
```

---

## 🧰 Useful List Methods

| Method          | Description                     |
| --------------- | ------------------------------- |
| `.append(x)`    | Add item to end                 |
| `.extend([])`   | Add multiple items              |
| `.insert(i, x)` | Insert at index                 |
| `.remove(x)`    | Remove first occurrence of item |
| `.pop([i])`     | Remove and return item at index |
| `.index(x)`     | Return first index of item      |
| `.count(x)`     | Count occurrences of item       |
| `.sort()`       | Sort list in place              |
| `.reverse()`    | Reverse list in place           |
| `.copy()`       | Create a shallow copy           |
| `.clear()`      | Remove all items                |

---

## 🔄 Iterating Over a List

```python
for item in my_list:
    print(item)

# Using index
for i in range(len(my_list)):
    print(my_list[i])
```

---

## 💡 List Comprehensions

```python
squares = [x*x for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

---

## 📦 Nested Lists

```python
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][0])  # Output: 3
```

---

## 📎 Tips

* Avoid modifying a list while iterating over it.
* Use list comprehensions for clean, efficient code.
* Lists are **mutable** — use `.copy()` to avoid aliasing issues.