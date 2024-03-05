import json
import requests

### Username should be your "email"

def oauth2_tokens(username, password, client_id, client_secret):
    url = "https://auth-api.8slp.net/v1/tokens"

    payload = json.dumps({
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "password",
    "username": username,
    "password": password
    })
    headers = {
            'content-type': 'application/json',
            'accept': 'application/json',
            'x-datadog-sampling-priority': '0',
            'accept-language': 'en-US,en;q=0.9',
            'user-agent': 'iOS App - 6.4.0/48305 - Apple iPhone15,2 - iOS 17.3.1',
            'x-datadog-origin': 'rum'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text