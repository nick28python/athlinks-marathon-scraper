<h1 align="center">Athlinks Marathon Results Scraper</h1>
<h3 align="center">Automated data extraction of marathon event results using Python + Proxies + BeautifulSoup</h3>
<h4 align="center">“No face, just results. Let the code do the heavy lifting.”</h4>

---

## 🧠 About This Project
This Python script scrapes marathon race result data from [Athlinks.com](https://www.athlinks.com), using:
- **Proxy rotation** for stealth scraping
- **Custom headers** to bypass blocks
- **BeautifulSoup** for HTML parsing
- **CSV export** for clean data usability

Built for automation, speed, and scale — this scraper is battle-tested and ready for production-level scraping.

---

## ⚙️ How It Works
1. Fetches HTML content from the Athlinks event result page (using rotating proxies)
2. Parses runner data like:
   - Name
   - Bib Number
   - Category
   - Time
   - Rank
3. Saves everything to a structured `.csv` file.

---

## 🛠 Tech Stack
- **Python 3.10+**
- **Requests** for fetching data
- **BeautifulSoup** for parsing
- **Proxies** via DataImpulse (for anonymous access)
- **CSV module** for exporting data

---

## 🚀 How to Use

```bash
# Step 1: Install dependencies
pip install requests beautifulsoup4

# Step 2: Run the script
python athlinks_scraper.py

# Output will be saved as:
athlinks_results_2023_dummy.csv

🔒 Note on Proxies

This script uses premium rotating proxies from DataImpulse.
To make it work:

    Replace the current proxy string with your valid proxy credentials.

    Or switch to a free/public proxy (not recommended for stability).
