import requests 
from bs4 import BeautifulSoup

def scraper(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    bio_div = soup.find('div', class_='wikipedia-extract')

    if bio_div:
        text = bio_div.get_text().strip()

        if text.startswith('Wikipedia'):
            text = text[9:].strip() 
    
        print("🎵 Success! Found biography:")
        print("=" * 50)
        print(text)
        return text
    else:
        print("No biography div found")
        return None
    

scraper('https://musicbrainz.org/artist/cd689e77-dfdd-4f81-b50c-5e5a3f5e38a4')
