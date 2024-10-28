# Football Match Data Scraper

A Selenium-based Python project to automate the extraction of match information and statistics from the Premier League section of the [Livescore website](https://www.livescore.com/en/football/england/premier-league/results/). This project collects data like match details, scores, and statistics and stores them in JSON files for further analysis or use in other applications.

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Output](#output)
- [Project Structure](#project-structure)
- [Features](#features)

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/football-match-scraper.git
   cd football-match-scraper
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. **Environment Variables**  
   Create a `.env` file in the root directory to store your credentials. This project requires the following environment variables:

   ```plaintext
   user=your_username
   password=your_password
   ```

2. **Download ChromeDriver**  
   Ensure you have [ChromeDriver](https://sites.google.com/chromium.org/driver/) installed and compatible with your version of Chrome. Place it in a directory accessible from your PATH.

## Usage

1. **Run the main script**  
   To start scraping data, run the following command:

   ```bash
   python main.py
   ```

2. **Wait for the process to complete**  
   The script will automatically navigate to the specified Livescore URL, retrieve match links, gather details for each match, and save them in JSON files.

## Output

The project generates two JSON files:

- **`match_links.json`**: Contains all extracted match links from the main page.
- **`matchs_data.json`**: Contains detailed match data for each game, including:
  - Teams and scores
  - Start time, stadium, and referee details
  - Match statistics (e.g., shots on target, possession, corners)
- **`matchs_data.csv`**: the same as *matchs_data.json** but csv file

## Project Structure

- **`main.py`**: The main script that coordinates data scraping, processing, and saving.
- **`src/crawler.py`**: Functions for crawling data.
- **`src/logger.py`**: Function to process and save data.
- **`src/data_processor.py`**: Function to setup logger.
- **`src/utils.py`**: Helper functions, such as setting up the Selenium WebDriver.
- **`src/proxies_manager.py`**: Manages proxies to use different IP.
- **`src/user_agent_manager.py`**: Manages user agents to mimic different browsing sessions.

## Features

- **Automated Scrolling**: Automatically scrolls through the results page to load all available matches.
- **Detailed Match Data Collection**: Extracts comprehensive match data, including teams, scores, stats, and additional information like stadium and referee.
- **Dynamic User Agents**: Uses a rotating user agent list to mimic different browsing sessions, reducing the chance of bot detection.
- **Dynamic proxy (optional)**: Uses a rotating proxies list to use different IP, reducing the chance of bot detection.
- **Error Handling**: Exception handling to ensure graceful failure in case of missing data or site changes.

---

Feel free to adjust as necessary!