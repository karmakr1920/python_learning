# 👤 Random User Fetcher (Python CLI)

A simple Python script that fetches random user data from the [FreeAPI](https://api.freeapi.app/) and displays useful user details in the terminal.

---

## 🌐 API Used

**Endpoint**:  
[`https://api.freeapi.app/api/v1/public/randomusers/user/random`](https://api.freeapi.app/api/v1/public/randomusers/user/random)

---

## 📋 Features

- Fetches a random user's:
  - Full name (first + last)
  - Username
  - Email
  - Country
- Clean and readable CLI output
- Fast and lightweight — no heavy dependencies

---

## 🔧 Installation & Setup

### 1. Clone or download the script

```bash
git https://github.com/karmakr1920/python_learning
cd api/get_random_user.py
````

### 2. Install dependencies

```bash
pip install requests
```

> Or use `requirements.txt` if provided.

---

## 🚀 Usage

Run the script:

```bash
python random_user.py
```

Example Output:

```
👤 Random User Info
🧑 Name     : Alice Johnson
🔐 Username : alice_j
📧 Email    : alice.johnson@example.com
🌍 Country  : United States
```

---

## 🛠 How It Works

1. Makes a `GET` request to the API.
2. Parses the JSON response to extract:

   * `name.first` + `name.last` → Full Name
   * `login.username`
   * `email`
   * `location.country`
3. Displays the data in a clean format.

---

## 📦 Requirements

* Python 3.x
* `requests` module

Install with:

```bash
pip install requests
```

---

## 🚧 Possible Improvements

* [ ] Fetch multiple users at once
* [ ] Save user data to a CSV or JSON file
* [ ] Add CLI arguments (e.g. `--count 5`)
* [ ] Include avatar / picture URL

---

## 👨‍💻 Author

This tool was created to practice working with REST APIs and JSON parsing in Python.

Feel free to fork, improve, or reuse!

---

## 📜 License

Free to use, modify, and distribute for learning and educational purposes.