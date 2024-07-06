import json
import requests

VIDEO_URL = "https://open.tiktokapis.com/v2/research/video/query/?fields=id,video_description"

def query_videos(query: dict, token: str):
    """Query TikTok video API with parameters defined in 'query.'"""
    # Request headers
    headers = {
        "Authorization": f"Bearer {token}",
        'Content-Type': 'application/json',
    }
    print(query)

    # for some reason, the API did not like data as a dict, so we dump it
    response = requests.post(VIDEO_URL, headers=headers, data=json.dumps(query))
    print(response.status_code)
    return response.json()
