import requests

url = "https://idcs-4537c0d6546b46e1bdd70b28c5cc9817.identity.oraclecloud.com:443/oauth2/v1/token"

#payload = 'grant_type=client_credentials&scope=urn%3Aopc%3Ahgbu%3Aws%3Arna%3AE%3Aamtbpbw9ocvjj3m6dhyg%3Aall'
payload = {
    "grant_type": "client_credentials",
    "scope": "urn:opc:hgbu:ws:rna:E:amtbpbw9ocvjj3m6dhy:all"
}


headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic T0NfUk5BX0NMSUVOVF9hbXRicGJ3OW9jdmpqM202ZGh5Z19BUFBJRDpjN2Y4MjhjOS01ODYyLTQwNzYtYTJlNS02YjA3OTM5ZDY5OWU='
}

#response = requests.request("POST", url, headers=headers, data=payload)

response = requests.post(url, data = payload, headers = headers)

#print(response.text)

token = response.json()["access_token"]

print("Token =" , token)