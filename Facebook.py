import requests

# Replace these with your details
PAGE_ID = "your_page_id"
ACCESS_TOKEN = "your_page_access_token"

# Graph API endpoint
url = f"https://graph.facebook.com/{PAGE_ID}/feed"

# Message to post
payload = {
    "message": "Hello Facebook! 🚀 This is an automated post from Python."
}

# Send the request
response = requests.post(url, data=payload, params={"access_token": ACCESS_TOKEN})

if response.status_code == 200:
    print("✅ Post published successfully!")
    print("Post ID:", response.json())
else:
    print("❌ Error:", response.status_code, response.text)
