import requests

def get_quotes(page=1):
    url = f'https://api.freeapi.app/api/v1/public/quotes?page={page}'
    response = requests.get(url)
    json_data = response.json()

    if json_data["statusCode"] == 200 and "data" in json_data:
        quote_data = json_data["data"]["data"]
        total_pages = json_data["data"]["totalPages"]
        results = []
        for quote in quote_data:
            author = quote['author']
            content = quote['content']
            tags = quote['tags']
            results.append((author, content, tags))
        return results, total_pages
    else:
        raise Exception("Failed to fetch data")

def display_quote(quote):
    author, content, tags = quote
    print(f"\n🧠 Quote by {author}")
    print(f"\"{content}\"")
    print(f"🏷️ Tags: {', '.join(tags) if tags else 'None'}")

def apply_filters(quotes, author_filter=None, tag_filter=None):
    filtered = []
    for quote in quotes:
        author, _, tags = quote
        if author_filter and author_filter.lower() not in author.lower():
            continue
        if tag_filter and all(tag_filter.lower() not in tag.lower() for tag in tags):
            continue
        filtered.append(quote)
    return filtered

def quote_reader(author_filter=None, tag_filter=None):
    page = 1
    total_pages = 1
    quote_index = 0
    filtered_quotes = []

    while True:
        if quote_index >= len(filtered_quotes):
            if page > total_pages:
                print("\n✅ No more matching quotes to show.")
                break

            try:
                quotes, total_pages = get_quotes(page)
            except Exception as e:
                print("Error:", e)
                break

            page += 1
            quote_index = 0
            filtered_quotes = apply_filters(quotes, author_filter, tag_filter)

            if not filtered_quotes:
                continue

        # Show 2 quotes at a time
        for _ in range(2):
            if quote_index < len(filtered_quotes):
                display_quote(filtered_quotes[quote_index])
                quote_index += 1
            else:
                break

        user_input = input("\nDo you want to read 2 more quotes? (yes/no): ").strip().lower()
        if user_input != 'yes':
            break

def main_menu():
    print("📚 Welcome to the Quote Reader!")

    while True:
        print("\nChoose an option:")
        print("1. Read all quotes")
        print("2. Read quotes by author")
        print("3. Read quotes by tag")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            quote_reader()
        elif choice == '2':
            author = input("Enter author name: ").strip()
            quote_reader(author_filter=author)
        elif choice == '3':
            tag = input("Enter tag: ").strip()
            quote_reader(tag_filter=tag)
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select a number from 1 to 4.")

if __name__ == '__main__':
    main_menu()
