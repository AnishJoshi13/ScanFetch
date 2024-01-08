# ScanFetch

This Python application extracts product details including images and descriptions from various shopping websites based on provided product titles. It utilizes web scraping techniques to fetch information and stores the data in an Excel file for easy access.

## Features

- **Product Title Extraction:** Extracts product titles from an input Excel file.
- **Image Retrieval:** Fetches 2-3 image URLs for each product title using DuckDuckGo search.
- **Description Extraction:** Utilizes Selenium to find product descriptions from search engine results.
- **Excel Output:** Outputs the collected data (product titles, image URLs, and descriptions) into a new Excel file.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/AnishJoshi13/ScanFetch.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Chrome Driver Version 120 for Win 64 based systems is provided in ThirdParty/chromedriver-win64. Replace chrome-win64 with the chromedriver version compatible with your system and chrome browser version. Downloads chromedriver from https://chromedriver.chromium.org/downloads

## Usage

1. Prepare an input Excel file with a column named "Product Title" containing the product titles.

2. Run the application:

    ```bash
    python product_scraper.py input_file.xlsx output_file.xlsx
    ```

3. Retrieve the output Excel file containing product details.

## Example

Input Excel:

| Product Title                     |
|-----------------------------------|
| Product A                         |
| Product B                         |
| ...                               |

Output Excel:

| Product Title    | Image 1 URL    | Image 2 URL    | Description    |
|------------------|----------------|----------------|----------------|
| Product A        | URL1           | URL2           | Description A  |
| Product B        | URL3           | URL4           | Description B  |
| ...              | ...            | ...            | ...            |

