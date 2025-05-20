import sqlite3

DB_NAME = 'youtube_videos.db'
PLAYLIST_FILE = 'playlist.txt'

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    if not videos:
        print("No videos found.")
        return []
    print("\nList of Videos:")
    for video in videos:
        print(f"ID: {video[0]}, Name: {video[1]}, Time: {video[2]}")
    return videos

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print("Video added successfully.")

def update_video(video_id, new_name, new_time):
    cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
    if cursor.fetchone() is None:
        print("Video ID not found.")
        return
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()
    print("Video updated successfully.")

def delete_video(video_id):
    cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
    if cursor.fetchone() is None:
        print("Video ID not found.")
        return
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
    print("Video deleted successfully.")

def bookmark_video():
    videos = list_videos()
    if not videos:
        return

    video_id = input("Enter video ID to bookmark: ").strip()
    cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
    video = cursor.fetchone()

    if not video:
        print("Invalid video ID.")
        return

    try:
        with open(PLAYLIST_FILE, 'r') as f:
            lines = f.readlines()
            if any(f"ID: {video_id}," in line and "[No longer exists]" not in line for line in lines):
                print("This video is already bookmarked.")
                return
    except FileNotFoundError:
        lines = []

    entry = f"ID: {video[0]}, Name: {video[1]}, Time: {video[2]}\n"
    with open(PLAYLIST_FILE, 'a') as f:
        f.write(entry)
    print("Video bookmarked successfully.")

def show_playlist():
    try:
        with open(PLAYLIST_FILE, 'r') as f:
            lines = f.readlines()

        if not lines:
            print("Playlist is empty.")
            return

        updated_lines = []
        print("\nBookmarked Videos:")
        for line in lines:
            line = line.strip()
            parts = line.split(", ")
            try:
                video_id = int(parts[0].split(":")[1])
            except (IndexError, ValueError):
                print(line)
                updated_lines.append(line + "  --> [Invalid Format]")
                continue

            cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
            if cursor.fetchone():
                print(line)
                updated_lines.append(line)
            else:
                if "[No longer exists]" not in line:
                    line += "  --> [No longer exists]"
                print(line)
                updated_lines.append(line)

        with open(PLAYLIST_FILE, 'w') as f:
            for updated_line in updated_lines:
                f.write(updated_line + '\n')

    except FileNotFoundError:
        print("Playlist file not found.")

def remove_from_playlist():
    try:
        with open(PLAYLIST_FILE, 'r') as f:
            lines = f.readlines()
        if not lines:
            print("Playlist is empty.")
            return

        print("Playlist Entries:")
        for line in lines:
            print(line.strip())

        video_id = input("Enter video ID to remove from playlist: ").strip()
        updated_lines = [line for line in lines if f"ID: {video_id}," not in line]

        if len(updated_lines) == len(lines):
            print("Video ID not found in playlist.")
            return

        with open(PLAYLIST_FILE, 'w') as f:
            f.writelines(updated_lines)

        print("Video removed from playlist.")

    except FileNotFoundError:
        print("Playlist file not found.")

def search_video_by_name():
    search_term = input("Enter name or part of video name to search: ").strip().lower()
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    results = [v for v in videos if search_term in v[1].lower()]

    if not results:
        print("No matching videos found.")
    else:
        print("\nSearch Results:")
        for video in results:
            print(f"ID: {video[0]}, Name: {video[1]}, Time: {video[2]}")

def main():
    while True:
        print("\nYouTube Manager Menu:")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Bookmark Video to Playlist")
        print("6. Show Playlist")
        print("7. Remove Video from Playlist")
        print("8. Search Video by Name")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ").strip()

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == '3':
            videos = list_videos()
            if not videos:
                continue
            video_id = input("Enter video ID to update: ")
            name = input("Enter new name: ")
            time = input("Enter new time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            videos = list_videos()
            if not videos:
                continue
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            bookmark_video()
        elif choice == '6':
            show_playlist()
        elif choice == '7':
            remove_from_playlist()
        elif choice == '8':
            search_video_by_name()
        elif choice == '9':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

    conn.close()

if __name__ == "__main__":
    main()
