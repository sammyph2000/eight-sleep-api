import json
import requests

### Dates should be in standard YYYY-MM-DD format

def get_trends(user_id, access_token, start_date, end_date):
    url = f"https://client-api.8slp.net/v1/users/{user_id}/trends?from={start_date}&to={end_date}&tz=America%2FNew_York&include-main=false&include-all-sessions=true&model-version=v2"

    payload = {}
    headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {access_token}',
            'x-datadog-sampling-priority': '1',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/json',
            'User-Agent': 'iOS App - 6.4.0/48305 - Apple iPhone15,2 - iOS 17.3.1',
            'Connection': 'keep-alive',
            'x-datadog-origin': 'rum'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text