import json
import requests

def get_access_token(client_id, client_secret, refresh_token):
    url = "https://auth-api.8slp.net/v1/tokens"

    payload = json.dumps({
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "refresh_token",
    "refresh_token": refresh_token
    })
    headers = {
            'content-type': 'application/json',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'user-agent': 'iOS App - 6.4.0/48305 - Apple iPhone15,2 - iOS 17.3.1'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text
