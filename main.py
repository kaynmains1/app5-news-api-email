import requests
from send_email import send_email

api_key = "890603a55bfa47048e4490069ebee18c"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&apiKey=" \
      "890603a55bfa47048e4490069ebee18c&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: New daily mail" + "\n" + body + article["title"] \
                + "\n" + str(article["description"]) + "\n" \
                + str(article["url"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)