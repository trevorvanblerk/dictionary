import requests

query = input("Enter a word:\n")

response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+query)

print("\n")

if response.status_code == 200:
	print("Meaning: \n" +response.json()[0]['meanings'][0]['definitions'][0]['definition'])
elif response.status_code == 404:
	print("The word did not have any meaning in the dictionary.")
else:
	print(response)