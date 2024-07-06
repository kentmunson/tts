import datetime
import os

from dotenv import load_dotenv
import pandas as pd

from ttkm.auth import get_access_token
from ttkm.video import query_videos

load_dotenv()

fields = [
    "id",
    "create_time",
    "username",
    "video_description",
    "like_count",
    "comment_count",
    "share_count",
    "view_count",
    "hashtag_names"
]

query = {
    "query": {
        "and": [
            {
                "operation": "EQ",
                "field_name": "hashtag_name",
                "field_values": ["adulting"],
            },
            {
                "operation": "IN",
                "field_name": "region_code",
                "field_values": ["US"],
            },
        ]
    },
    "max_count": 20,
    "cursor": 0,
    "start_date": "20240101",
    "end_date": "20240131",
}

# Replace with your actual client key and client secret
client_key = os.getenv("CLIENT_KEY")
client_secret = os.getenv("CLIENT_SECRET")

# Call the function with your credentials
token = get_access_token(client_key, client_secret)

# TODO - Build loop for each month

# Use the token and the query to query videos
response_json = query_videos(query=query, token=token, fields=fields)

# Print the response
print(response_json)

# Load it into a dataframe
df = pd.DataFrame(response_json["data"]["videos"])

df["timestamp"] = df["create_time"].apply(lambda x: datetime.datetime.fromtimestamp(x))

print(df.head())

# TODO - Combine dataframes and dump it
