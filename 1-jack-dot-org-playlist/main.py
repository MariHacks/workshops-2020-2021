import requests
import os

airtable_token = os.getenv("AIRTABLE_TOKEN")

emotion = input("What is your emotion? ")
activity = input("What is your activity? ")

headers = {"Authorization": f"Bearer {airtable_token}"}
response = requests.get("https://api.airtable.com/v0/appywQzwZYTT5lFQO/Table%201", headers=headers)

for row in response.json()["records"]:
	if row["fields"]["activity"] == activity and emotion==row["fields"]["mentalState"]:
		print(row["fields"]["spotifyLink"])
