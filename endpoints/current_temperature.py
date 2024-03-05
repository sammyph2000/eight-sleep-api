import json
import requests

def get_current_temperature(user_id, access_token):
    url = f"https://app-api.8slp.net/v1/users/{user_id}/temperature"

    payload = {}
    headers = {
            'Content-Type': 'application/json',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'User-Agent': 'iOS App - 6.4.0/48305 - undefined - iOS 17.3.1',
            'Authorization': f'Bearer {access_token}',
            'Accept-Language': 'en-US,en;q=0.9'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text