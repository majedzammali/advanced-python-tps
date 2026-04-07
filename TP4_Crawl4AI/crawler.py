import asyncio
import json
from crawl4ai import WebCrawler
from datetime import datetime

async def crawl_website():
    """Crawl a website using Crawl4AI"""
    
    print("🕸️ Starting Crawl4AI crawler...")
    
    # Initialize crawler
    crawler = WebCrawler()
    crawler.warmup()
    
    # URLs to crawl
    urls = [
        "https://example.com",
        "https://python.org",
    ]
    
    results = []
    
    for url in urls:
        print(f"📡 Crawling: {url}")
        try:
            result = await crawler.arun(url)
            
            # Extract useful information
            data = {
                'url': url,
                'title': result.title if hasattr(result, 'title') else 'N/A',
                'text_length': len(result.markdown) if hasattr(result, 'markdown') else 0,
                'crawled_at': datetime.now().isoformat(),
                'content_preview': (result.markdown[:200] if hasattr(result, 'markdown') else 'No content') + "..."
            }
            results.append(data)
            print(f"✅ Successfully crawled {url}")
        except Exception as e:
            print(f"❌ Error crawling {url}: {e}")
    
    # Save results
    with open('crawled_data.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    return results

def main():
    """Main function to run crawler"""
    print("🚀 Crawl4AI Demo")
    print("=" * 50)
    
    # Run async crawler
    results = asyncio.run(crawl_website())
    
    print(f"\n📊 Summary: Crawled {len(results)} websites")
    print("💾 Data saved to crawled_data.json")
    
    # Display results
    for r in results:
        print(f"\n📍 {r['url']}")
        print(f"   Title: {r['title']}")
        print(f"   Content length: {r['text_length']} chars")

if __name__ == "__main__":
    main()