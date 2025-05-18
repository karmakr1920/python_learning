import requests

API_URL = 'https://api.freeapi.app/api/v1/public/stocks'
FAV_FILE = 'favourite_stocks.txt'

# ---------- API FETCH ----------
def fetch_stocks_page(page=1, limit=2):
    try:
        response = requests.get(API_URL, params={"page": page, "limit": limit})
        data = response.json()
        if data["statusCode"] == 200 and "data" in data:
            return data["data"]
        else:
            print("Error: Invalid API response.")
            return None
    except Exception as e:
        print(f"Error fetching stocks: {e}")
        return None

# ---------- DISPLAY ----------
def display_stock(stock):
    print("\n--------------------------")
    for key, value in stock.items():
        print(f"{key}: {value}")

# ---------- FAVOURITES ----------
def save_to_favourites(stock):
    try:
        with open(FAV_FILE, 'a') as f:
            f.write(f"{stock['Name']} ({stock['Symbol']})\n")
        print("Stock saved to favourites.")
    except Exception as e:
        print(f"Error saving to favourites: {e}")

# ---------- SEARCH UTILITY ----------
def show_and_optionally_fav(stock):
    display_stock(stock)
    fav = input("Mark as favourite? (y/n): ").strip().lower()
    if fav == 'y':
        save_to_favourites(stock)

# ---------- PAGINATED VIEW ----------
def show_stocks_paginated():
    page = 1
    while True:
        result = fetch_stocks_page(page)
        if not result:
            break

        stocks = result['data']
        for stock in stocks:
            show_and_optionally_fav(stock)

        if result['nextPage']:
            more = input("Show next stocks? (y/n): ").strip().lower()
            if more == 'y':
                page += 1
            else:
                break
        else:
            print("No more stocks to show.")
            break

# ---------- OPTIMIZED SEARCH ----------
def search_stocks_interactive(search_type="name", query=""):
    page = 1
    found_any = False

    while True:
        result = fetch_stocks_page(page)
        if not result:
            break

        stocks = result['data']

        if search_type == "name":
            matches = [s for s in stocks if query.lower() in s['Name'].lower()]
        else:  # symbol
            matches = [s for s in stocks if query.lower() == s['Symbol'].lower()]

        if matches:
            found_any = True
            for stock in matches:
                show_and_optionally_fav(stock)

            if not result['nextPage']:
                print("End of search results.")
                break

            more = input("Search next page for more matches? (y/n): ").strip().lower()
            if more != 'y':
                break

        elif result['nextPage']:
            page += 1
        else:
            break

    if not found_any:
        print("No matching stocks found.")

# ---------- MENU ----------
def main_menu():
    while True:
        print("\n=== Stock Menu ===")
        print("1. Show stocks (2 at a time)")
        print("2. Search by name")
        print("3. Search by symbol")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        match choice:
            case '1':
                show_stocks_paginated()

            case '2':
                name = input("Enter stock name: ").strip()
                search_stocks_interactive(search_type="name", query=name)

            case '3':
                symbol = input("Enter stock symbol: ").strip()
                search_stocks_interactive(search_type="symbol", query=symbol)

            case '4':
                print("Exiting program.")
                break

            case _:
                print("Invalid choice. Please enter 1–4.")

# ---------- RUN ----------
if __name__ == '__main__':
    main_menu()
