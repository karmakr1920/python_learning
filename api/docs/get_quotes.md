# 🧠 CLI Quote Reader in Python

A simple command-line Python app to read inspirational quotes from a public API. You can read quotes in batches, filter them by author or tag, and navigate interactively.

---

## 🚀 Features

- Fetches quotes from [`freeapi.app`](https://freeapi.app/)
- Displays quotes 2 at a time for better readability
- Interactive CLI menu:
  - Show all quotes
  - Show quotes by author
  - Show quotes by tag
- Filters quotes by user input
- Pagination support (fetches more quotes from API pages automatically)

---

## 📂 Project Structure

```bash
.
├── quote_reader.py        # Main Python script
├── README.md              # Project documentation (this file)
└── requirements.txt       # Dependencies (optional but recommended)
````

---

## 🔧 Installation

### 1. Clone the project or download the script

```bash
git clone https://github.com/karmakr1920/python_learning
cd api/get_quotes.py
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install requests
```

---

## 🛠 Usage

```bash
python quote_reader.py
```

You will see a menu like:

```
📚 Welcome to the Quote Reader!

Choose an option:
1. Read all quotes
2. Read quotes by author
3. Read quotes by tag
4. Exit
```

You can choose to filter by:

* Author name (e.g., `Thomas Edison`)
* Tag (e.g., `Motivational`, `Work`, `Wisdom`)

Quotes will appear **2 at a time**, and you'll be prompted to continue.

---

## 🧠 How It Works

* Uses the `requests` module to fetch quote data from the API:

  ```
  https://api.freeapi.app/api/v1/public/quotes?page=1
  ```
* Parses JSON and extracts:

  * `author`
  * `content`
  * `tags`
* Quotes are filtered based on:

  * Author substring match
  * Tags containing the keyword
* Pagination is handled per page (10 quotes per page), but shows **2 at a time**.

---

## 📝 Example Output

```
🧠 Quote by Thomas Edison
"Opportunity is missed by most people because it is dressed in overalls and looks like work."
🏷️ Tags: Opportunity, Work

Do you want to read 2 more quotes? (yes/no):
```

---

## 📦 Optional: Requirements File

You can auto-generate it with `pipreqs`:

```bash
pip install pipreqs
pipreqs . --force
```

It will produce:

```
requests
```

---

## 📌 To-Do / Future Improvements

* [ ] Save favorite quotes to a file
* [ ] Add support for random quote fetching
* [ ] Enhance input validation

---

## 👨‍💻 Author

This project was created as part of learning core Python development and working with real APIs and CLI interaction.

---

## 📜 License

Free to use, modify, and improve. Attribution appreciated but not required.