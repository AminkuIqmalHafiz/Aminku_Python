#Trade Logger

### Overview
This is a robust, interactive command-line application built entirely in Python. I designed this tool to simulate a quantitative trading desk's end-of-day logging system. Instead of relying on static, hardcoded arrays, this application allows users to manually input their daily trades in real-time, stores them in memory, and dynamically calculates performance metrics including Net PnL, Win Rate, and the most profitable trade of the session. It also features a custom, color-coded ANSI terminal interface for professional data visualization.

### What I Learned 
By building this project from scratch, I successfully implemented and mastered the following core Python concepts:

* **While Loop (`while True`):** I engineered an infinite application loop that keeps the program running and returns the user to the main menu after every action, only terminating when the "Exit Protocol" is explicitly triggered.
* **Exception Handling(`try / except`):** I implemented robust error handling to sanitize user inputs. By catching `ValueError` exceptions, the application gracefully rejects invalid data (like typing text when a float is required) and reprompts the user without crashing the script.
* **List/Dictionary:** I wrote logic that takes raw user inputs, formats them into a structured Python dictionary, and dynamically uses `.append()` to inject them into a master list serving as the application's runtime database.
* **Dictionary Utilisation:** I built custom functions to iterate over the logged data in a single pass ($O(N)$ time complexity), successfully maintaining running tallies for total profit/loss and tracking the "All-Time High" trade.
* **ANSI Colour Codes:** I defined custom ANSI string variables to inject hex color codes and bold formatting directly into the terminal prints, dynamically turning the UI red for negative outputs and green for positive metrics.
* **Modular Function Design:** I abstracted the complex math into separate helper functions (`get_best_trades` and `winrate`) to keep the main application loop clean, readable, and scalable.

### Execution
To run this application natively in your terminal, ensure you have Python installed and run the following command in the directory where your file is saved:
```bash
python trade_logger.py

(Note: Follow the on-screen menu prompts to begin logging trades).