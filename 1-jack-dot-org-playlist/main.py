# import modules 
import requests
import random
import webbrowser

# get user input (mental state and activity)
emotion = input("Mental state? ").lower().strip()
activity = input("Activity? ").lower().strip()

# read the Jack.org spreadsheet
headers = {"Authorization": "Bearer key11VPF3xYEIsES0"}

response = requests.get("https://api.airtable.com/v0/appywQzwZYTT5lFQO/Table%201", headers=headers)

response = response.json()

found = False
link = ""

for row in response["records"]:

  if emotion == row["fields"]["mentalState"].lower() and activity == row["fields"]["activity"].lower():
    print(row["fields"]["spotifyLink"])
    webbrowser.open(row["fields"]["spotifyLink"])
    found = True

if found == False:
  # random.shuffle(response["records"])
  print(response["records"][0]["fields"]["spotifyLink"])
  webbrowser.open(random.choice(response["records"])["fields"]["spotifyLink"])
