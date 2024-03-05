import json
import requests

def temperature(user_id, authorization, temperature_level):
    url = f"https://app-api.8slp.net/v1/users/{user_id}/temperature"

    payload = json.dumps({
    "currentLevel": temperature_level
    })
    headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {authorization}',
            'x-datadog-sampling-priority': '0',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/json',
            'User-Agent': 'iOS App - 6.4.0/48305 - Apple iPhone15,2 - iOS 17.3.1',
            'Connection': 'keep-alive'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response.text