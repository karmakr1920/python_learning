# Stock Information Fetcher

This Python script allows you to fetch stock information from an API, display the data, search stocks by name or symbol, and mark your favourite stocks. It supports paginated data fetching (2 stocks per page) and stores favourites in a `.txt` file.

## Features

* **Show all stocks (2 at a time)**
* **Search stocks by name or symbol**
* **Mark stocks as favourite and save them to a `.txt` file**
* **Supports paginated fetching of stock data**
* **Modular, CLI-based interface**

## Requirements

* Python 3.x
* `requests` library (install it via `pip install requests`)

## Setup

1. Clone or download this repository to your local machine.

2. Install the required libraries:

   ```bash
   pip install requests
   ```

3. Save the `stocks.py` script to a location on your system.

4. Run the script:

   ```bash
   python stocks.py
   ```

## Usage

After running the script, the main menu will appear, providing the following options:

### 1. Show Stocks (2 at a time)

Fetches and displays 2 stocks per page. After each page, the user can decide whether to continue to the next page or stop.

#### Example:

```text
=== Stock Menu ===
1. Show stocks (2 at a time)
2. Search by name
3. Search by symbol
4. Exit
```

You will see a list of stocks, and after every two stocks, you'll be asked if you want to see the next page of results.

### 2. Search by Stock Name

Searches stocks by name (case-insensitive). The script fetches data in batches, and if matches are found, they will be displayed. You can stop after seeing the first few matches or continue searching for more.

#### Example:

```text
Enter stock name: Apple
```

### 3. Search by Stock Symbol

Searches stocks by their symbol. If a match is found, the stock information will be displayed. You can search for multiple symbols by following the same steps.

#### Example:

```text
Enter stock symbol: AAPL
```

### 4. Exit

Ends the program and exits the script.

---

## Code Structure

### `fetch_stocks_page(page=1, limit=2)`

This function fetches stock data from the API for a given page number and a fixed limit of 2 stocks per page.

### `display_stock(stock)`

Displays the stock information in a readable format.

### `save_to_favourites(stock)`

Saves a stock to a `.txt` file (`favourite_stocks.txt`).

### `show_and_optionally_fav(stock)`

Displays a stock and asks the user if they want to mark it as a favourite.

### `search_stocks_interactive(search_type="name", query="")`

Searches for stocks either by **name** or **symbol** and allows the user to stop searching after finding matches.

### `main_menu()`

The main function where the user can select options from the menu. The choices are:

1. Show stocks
2. Search by name
3. Search by symbol
4. Exit the program

---

## File Storage

* **Favourites**: All stocks marked as favourites will be saved in a text file `favourite_stocks.txt`. Each stock is stored with its **name** and **symbol**.

### Example of `favourite_stocks.txt`:

```text
Apple Inc. (AAPL)
Tesla, Inc. (TSLA)
```

## Notes

* The program fetches stocks in batches (2 per page) to optimize API calls.
* It stores the favourites in a plain text file, which can be modified manually or programmatically.
* The search by **name** or **symbol** fetches data from all available pages, but stops once the matches are found or when the user chooses to stop.

## Troubleshooting

* Ensure you have a stable internet connection, as this script requires external API calls.
* If the API service is down or there's an issue with the endpoint, the script will show an error message.

## License

This project is open source and available under the MIT License.