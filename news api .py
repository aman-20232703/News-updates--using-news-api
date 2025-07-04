import requests
import json

# 🔹 Ask the user to enter a topic of interest
query = input("Enter a topic you're interested in (e.g. technology, sports, finance, any others): ")

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

"""
Enter a topic you're interested in (e.g. technology, sports, finance, any others): technology

output:-
~~~~~~~~~~

Top News Articles Based on Your Interest:

🔸 Article 1: ICMAI National Students’ Convocation 2025: President of India highlights the role of cost accountants in nation-building
📝 Summary: President Murmu addressed ICMAI's convocation, emphasizing cost accountants' vital role in India's economic progress and sustainable future. She highlighted their historical importance, linking accounting to accountability, referencing Gandhi's cost-efficienc…
--------------------------------------------------
🔸 Article 2: Hindu pilgrimage begins in Kashmir in wake of India-Pakistan conflict
📝 Summary: Security has been beefed up for this pilgrimage, taking place just months after a deadly gun attack in the area.
--------------------------------------------------
🔸 Article 3: US $1,000 quick loan No Credit Check Loans: Radcred Launches Instant Bad Credit Loans For Emergency Need
📝 Summary: RadCred Unveils Flexible $1,000 Quick Loan Options—No Credit Checks Required for U.S. Borrowers in 2025 RadCred Unveils Flexible $1,000 Quick Loan Options—No Credit Checks Required for U.S. Borrowers in 2025
--------------------------------------------------
🔸 Article 4: I'm Rethinking My Upgrade Based on These 5 iPhone 17 Pro Max Rumors
📝 Summary: If these rumors pan out, I might embrace Apple's next large-sized iPhone.
--------------------------------------------------
🔸 Article 5: Meet the SDV Committers: Elena Gantner from Eclipse S-CORE
📝 Summary: Meet the SDV Committers: Elena Gantner from Eclipse S-CORE


"""
