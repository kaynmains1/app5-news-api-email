import requests

api_key = "efafa33301d84109b0581e484bd8459d"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-11-23&sortBy=publishedAt&apiKey=efafa33301d84109b0581e484bd8459d"

request = requests.get(url)

content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])