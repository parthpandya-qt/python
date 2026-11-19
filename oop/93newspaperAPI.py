import requests
import json

query= input("search the name of news:")

url =f"https://newsapi.org/v2/everything?q={query}&from=2025-06-02&sortBy=publishedAt&apiKey=a3a36278a0f6402c95409f59390233c6"

response = requests.get(url)
data = response.text
json_data = json.loads(data)

for article in json_data["articles"]:
    print(article["title"])
    print(article["description"])
    print("------------------------------------------------------")
    print("\n")
