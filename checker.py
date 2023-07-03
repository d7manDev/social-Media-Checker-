import random
import string
import requests

def generate_random_username(length):
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for i in range(length))
    return username

def check_tiktok_username(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

def check_twitter_username(username):
    url = f"https://twitter.com/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

def check_instagram_username(username):
    url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

def check_youtube_username(username):
    url = f"https://www.youtube.com/user/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

def check_snapchat_username(username):
    url = f"https://www.snapchat.com/add/{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

# Define numbers for each platform
PLATFORMS = {
    1: "tiktok",
    2: "twitter",
    3: "instagram",
    4: "youtube",
    5: "snapchat"
}

# Ask user for desired username length and platform to check
length = int(input("Enter desired username length: "))
print("Choose a platform to check:")
for num, platform in PLATFORMS.items():
    print(f"{num}: {platform}")
platform_num = int(input())

# Check platform for available usernames
if platform_num == 1:
    check_username = check_tiktok_username
elif platform_num == 2:
    check_username = check_twitter_username
elif platform_num == 3:
    check_username = check_instagram_username
elif platform_num == 4:
    check_username = check_youtube_username
elif platform_num == 5:
    check_username = check_snapchat_username
else:
    print("Invalid platform entered. Please choose a number between 1 and 5.")
    exit()

available_usernames = []
while True:
    username = generate_random_username(length)
    if check_username(username):
        print(f"Username '{username}' is taken.")
    else:
        print(f"Username'{username}' is available!")
        available_usernames.append(username)

    if len(available_usernames) >= 10:
        break

# Write available usernames to text file
with open("available_usernames.txt", "w") as file:
    for username in available_usernames:
        file.write(username + "\n")

print(f"Found {len(available_usernames)} available usernames for {PLATFORMS[platform_num]}. Results written to available_usernames.txt.")