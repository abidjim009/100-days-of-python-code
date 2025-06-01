import requests

def get_news(topic, api_key):
    url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("articles", [])
        
        if not articles:
            print(f"No news articles found for topic: {topic}")
            return
        
        print(f"\nTop News for Topic: {topic}\n" + "-"*40)
        for idx, article in enumerate(articles[:5], 1):  # Limit to top 5 articles
            print(f"{idx}. {article['title']}")
            print(f"   Source: {article['source']['name']}")
            print(f"   URL: {article['url']}\n")
    else:
        print("Failed to fetch news:", response.status_code)

# === Replace 'your_api_key_here' with your actual API key from https://newsapi.org ===
API_KEY = "your_api_key_here"
topic = input("Enter a topic to fetch news: ")
get_news(topic, API_KEY)
