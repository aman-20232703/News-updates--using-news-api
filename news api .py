import requests
import json

# 🔹 Ask the user to enter a topic of interest
query = input("Enter a topic you're interested in (e.g. technology, sports, finance): ")

# 🔹 API endpoint with your NewsAPI key
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-04&sortBy=publishedAt&apiKey=10d29856cc9f41b8bacabcf82e277d7f"

# 🔹 Send a GET request to the API
response = requests.get(url)

# 🔹 Load JSON response into a Python dictionary
data = json.loads(response.text)

print("\nTop News Articles Based on Your Interest:\n")

# 🔹 Loop through each article and print relevant information
for index, article in enumerate(data.get("articles", []), start=1):
    print(f"🔸 Article {index}: {article['title']}")
    print(f"📝 Summary: {article['description']}")
    print("--------------------------------------------------")

# Ending note
print("\nThat's all for now! Stay informed.")
