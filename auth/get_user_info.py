import json
import requests

def get_user_info(access_token):
    url = "https://client-api.8slp.net/v1/users/me"

    payload = {}
    headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {access_token}',
            'x-datadog-sampling-priority': '0',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/json',
            'User-Agent': 'iOS App - 6.4.0/48305 - Apple iPhone15,2 - iOS 17.3.1',
            'Connection': 'keep-alive',
            'x-datadog-origin': 'rum'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text

def get_user_id(user_info):
    data = json.loads(user_info)
    user_id = data['user']['userId']
    return user_id