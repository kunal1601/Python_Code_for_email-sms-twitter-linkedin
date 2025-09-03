from instagrapi import Client

# Create a Client object
client = Client()

# Take user input for Instagram credentials and photo details
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")
photo_path = input("Enter the path to the photo you want to upload: ")
caption = input("Enter the caption for your photo: ")

# Log in to your Instagram account
try:
    client.login(username, password)
    print("Logged in successfully.")
except Exception as e:
    print(f"Failed to log in: {e}")
    exit()  # Exit if login fails

# Upload the photo and get its media ID
try:
    media_id = client.photo_upload(photo_path, caption=caption).pk
    print(f"Photo uploaded successfully with media ID: {media_id}")
except Exception as e:
    print(f"Failed to upload photo: {e}")
