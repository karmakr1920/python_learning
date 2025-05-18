# 🎬 YouTube Video Manager (CLI App)

This is a simple command-line YouTube video manager app built with Python and SQLite. It allows users to:

- Add, update, delete, list videos
- Bookmark videos to a plain-text playlist file
- View bookmarked videos and auto-flag videos no longer existing in the database

---

## 🗃️ Database

- SQLite3 database file: `youtube_videos.db`
- Table structure:

```sql
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
);
````

---

## 📁 Playlist File

* Bookmarked videos are saved in `playlist.txt`
* Format is human-readable:

  ```
  ID: 1, Name: Python Basics, Time: 12:30
  ID: 5, Name: SQL Intro, Time: 09:45  --> [No longer exists]
  ```
* When viewing the playlist, the app checks if the video still exists in the database and updates the line accordingly.

---

## 🛠️ Features

* ✅ Add new video (name + time)
* ✅ List all videos with ID
* ✅ Update or delete any video by ID (video list shown before operation)
* ✅ Bookmark videos (video list shown first)
* ✅ View playlist with deleted entries marked
* ✅ Clean CLI experience (no emojis, minimal dependencies)

---

## 📦 Requirements

* Python 3.x
* SQLite3 (comes pre-installed with Python)
* No external libraries needed

---

## 🧑‍💻 How to Run

```bash
python youtube_manager.py
```

---

## 🧰 Bonus for VS Code Users: View SQLite Data in VS Code

### 🔌 Use the **SQLite Viewer** Extension

1. Open VS Code
2. Go to Extensions (`Ctrl+Shift+X`)
3. Search: **SQLite Viewer** (by *Alex Covizzi*)
4. Install it

### ▶️ Usage:

* Open the `youtube_videos.db` file in VS Code
* Right-click → **Open Database**
* You’ll see a sidebar with all tables
* Click on `videos` to view or run SQL queries like:

  ```sql
  SELECT * FROM videos;
  ```

---

### 🧪 Bonus Terminal Tip (Optional)

If `sqlite3` is installed, you can use the terminal inside VS Code:

```bash
sqlite3 youtube_videos.db
```

Inside the prompt:

```sql
.tables
SELECT * FROM videos;
.quit

---

## 📌 Author

This CLI app was created for learning and managing YouTube-style content with basic database skills and file handling.