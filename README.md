#  Python GUI & Web Scraping Toolkit

This repository contains a collection of Python-based applications that demonstrate GUI development using Tkinter, database interaction with SQLite, and web scraping using BeautifulSoup. Each program is organized by problem area and includes modular design, user interaction, and error handling.

---

## 📂 Project Structure

### 🎬 Problem 1 – Movie CLI Manager (`sqlite3`)
A command-line interface to manage a movie database:
- `add_movie()` prevents duplicates
- `delete_movie()` prompts confirmation before deletion
- `min` command displays all movies under a user-specified runtime
- Files:
  - `db.py`
  - `objects.py`
  - `ui.py`

---

### 💸 Problem 2 – Future Value & Fuel Efficiency GUI
#### Future Value Calculator:
- Two independent calculator panels
- Supports Clear, Clear All, and Exit buttons
- Validates numeric input for investment calculations

#### Fuel Efficiency Calculator:
- Toggle between US (MPG) and Metric (L/100km)
- Updates labels and calculations accordingly
- GUI built using Tkinter

Files:
- `business.py`
- `mpg_gui.py`
- `ui.py` (reused)

---

### 🌐 Problem 4 – BBC News Web Scraper
Scrapes top BBC headlines using `requests` and `BeautifulSoup`:
- Extracts and formats:
  - Headline text
  - Absolute URLs
  - Metadata date (standardized)
  - Tag (genre)
- Handles relative dates by converting them to absolute format

Files:
- `scrape_headlines.py`
- `scraper_helper.py`

---

## ▶️ How to Run

Make sure you have the necessary packages installed:

```bash
pip install requests beautifulsoup4
