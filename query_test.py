import os

from dotenv import load_dotenv

from ttkm.auth import get_access_token
from ttkm.video import query_videos

load_dotenv()

query = {
    "query": {
        "and": [
            {
                "operation": "EQ",
                "field_name": "hashtag_name",
                "field_values": ["adulting"],
            },
        ]
    },
    "max_count": 20,
    "cursor": 0,
    "start_date": "20240101",
    "end_date": "20240131",
}

test_query = {
    "query": {
        "and": [
            { "operation": "IN", "field_name": "region_code", "field_values": ["US", "CA"] },
            { "operation": "EQ", "field_name": "keyword", "field_values": ["hello world"] }
        ]
    },
    "start_date": "20220615",
    "end_date": "20220628",
    "max_count": 10
}


# Replace with your actual client key and client secret
client_key = os.getenv("CLIENT_KEY")
client_secret = os.getenv("CLIENT_SECRET")

# Call the function with your credentials
token = get_access_token(client_key, client_secret)

# Use the token and the query to query videos
response_json = query_videos(query=query, token=token)

# Print the response
print(response_json)
