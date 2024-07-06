import json
import requests

from typing import List

VIDEO_URL = "https://open.tiktokapis.com/v2/research/video/query/"

def build_url(fields: List, base_url: str = VIDEO_URL):
    if not fields:
        raise ValueError("You did not specify any fields to pull!")
    fields_substr = ",".join(fields)
    return base_url + "?fields=" + fields_substr

def query_videos(query: dict, token: str, fields: List):
    """Query TikTok video API with parameters defined in 'query.'"""
    # Request headers
    headers = {
        "Authorization": f"Bearer {token}",
        'Content-Type': 'application/json',
    }
    print(query)

    # Build URL
    url = build_url(fields)
    print(url)

    # For some reason, the API did not like data as a dict, so we dump it
    response = requests.post(url, headers=headers, data=json.dumps(query))
    print(response.status_code)

    return response.json()
