import requests
from bs4 import BeautifulSoup

# Wikipedia "In the News" section
URL = "https://en.wikipedia.org/wiki/Portal:Current_events"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def scrape_wikipedia_news():
    try:
        # Fetch the webpage
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract only relevant news articles (skip "edit", "history", etc.)
        articles = soup.select(".vevent ul li a[href^='/wiki/']")  

        if not articles:
            print("⚠ No articles found. The website structure may have changed.")
            return

        print("\n🔹 Latest Wikipedia 'In the News' Headlines:")
        for index, article in enumerate(articles[:5]):  # Show only top 5 headlines
            headline = article.get_text(strip=True)
            link = "https://en.wikipedia.org" + article["href"]
            print(f"{index + 1}. {headline} ({link})")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    scrape_wikipedia_news()
