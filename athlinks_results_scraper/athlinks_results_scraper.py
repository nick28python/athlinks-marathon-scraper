import requests
from bs4 import BeautifulSoup
import csv

# Setup headers and proxy
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

proxies = {
    "http": "http://your_proxy_here",
    "https": "http://your_proxy_here"
}

URL = "https://www.worldfootball.net/all_matches/eng-premier-league-2023-2024/"

def fetch_html():
    response = requests.get(URL, headers=HEADERS, proxies=PROXIES)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code}")
        return None

def parse_matches(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='__')
    data = []

    if not table:
        print("Table not found.")
        return data

    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 6:
            match_date = cols[0].text.strip()
            time = cols[1].text.strip()
            home_team = cols[2].text.strip()
            away_team = cols[4].text.strip()
            score = cols[5].text.strip()

            data.append({
                "date": match_date,
                "time": time,
                "home_team": home_team,
                "away_team": away_team,
                "score": score
            })

    return data

def save_to_csv(data, filename="premier_league_2023_24.csv"):
    with open(filename, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "time", "home_team", "away_team", "score"])
        writer.writeheader()
        writer.writerows(data)
    print(f"✅ CSV saved as: {filename}")

def main():
    html = fetch_html()
    if html:
        matches = parse_matches(html)
        for match in matches[:5]:  # Preview first 5 matches
            print(match)
        save_to_csv(matches)

if __name__ == "__main__":
    main()
