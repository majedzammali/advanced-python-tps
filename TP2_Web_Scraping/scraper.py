import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrape_books_to_scrape():
    """Scrape book data from books.toscrape.com"""
    base_url = "http://books.toscrape.com"
    response = requests.get(f"{base_url}/catalogue/page-1.html")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    books = []
    for book in soup.select('.product_pod'):
        title = book.h3.a['title']
        price = book.select_one('.price_color').text
        rating = book.select_one('.star-rating')['class'][1]
        
        books.append({
            'title': title,
            'price': price,
            'rating': rating,
            'scraped_at': datetime.now().isoformat()
        })
    
    # Save to CSV
    df = pd.DataFrame(books)
    df.to_csv('scraped_books.csv', index=False)
    print(f"✅ Scraped {len(books)} books")
    return books

if __name__ == "__main__":
    print("🕷️ Starting web scraper...")
    results = scrape_books_to_scrape()
    print(f"📊 Data saved to scraped_books.csv")
    print(results[:3])  # Show first 3 results