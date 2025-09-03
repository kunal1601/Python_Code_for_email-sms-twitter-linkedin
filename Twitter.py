import tweepy

# Your credentials
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"

# Authenticate
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Post a Tweet
tweet_text = "Hello Twitter (X)! 🚀 This is my first automated tweet using Python. #Python #TwitterAPI"
try:
    api.update_status(status=tweet_text)
    print("✅ Tweet posted successfully!")
except Exception as e:
    print("❌ Error posting tweet:", e)
