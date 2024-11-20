# EuroLeague Basketball Team Stats Scraper

This Python script scrapes team and player statistics from the EuroLeague Basketball website. It uses a combination of **`requests`**, **`BeautifulSoup`**, and **`Selenium`** libraries to extract data and save it to a CSV file.

## Features

1. **Get Team Links**:  
   Retrieves a list of all EuroLeague basketball teams' pages from the main EuroLeague teams page.

2. **Get Team Stats Page Link**:  
   Extracts the specific link to a team's statistics page from the team page.

3. **Scrape Team Stats**:  
   Scrapes detailed player statistics for each team using **`Selenium`**, including:

   - Points, rebounds, assists, and other performance metrics.
   - Shooting percentages (2-point, 3-point, free throw).
   - Defensive and offensive contributions.

4. **Save Data**:  
   Aggregates all the data into a Pandas DataFrame and exports it to a CSV file (`stats.csv`).

## Dependencies

- **Python Libraries**:
  - `requests`: For making HTTP requests.
  - `bs4` (BeautifulSoup): For parsing HTML content.
  - `pandas`: For data manipulation and CSV export.
  - `selenium`: For dynamically loading JavaScript-driven web pages.
- **Selenium WebDriver**: Requires ChromeDriver for handling browser interactions.
