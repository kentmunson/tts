from datetime import date, datetime, timedelta
import os
from random import randint
import time
from typing import List

from dotenv import load_dotenv
import pandas as pd

from ttkm.auth import get_access_token
from ttkm.video import query_videos

load_dotenv()

current_date = date(2024, 7, 1)

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
    "is_random": True,
}


def embed_link(id: int):
    """Return a static link to a TikTok video, given its ID."""
    return f"https://www.tiktok.com/embed/{id}"


def dump_dataframes(current_date: date, dataframes: List[pd.DataFrame]):
    """Dump a list of dataframes marked with the previous date."""
    previous_date_str = (current_date - timedelta(days=1)).strftime("%Y%m")
    fp = f"data/tiktok_adulting_{previous_date_str}.csv"
    monthly_df = pd.concat(dataframes).reset_index(drop=True)
    monthly_df.to_csv(fp)


# Replace with your actual client key and client secret
client_key = os.getenv("CLIENT_KEY")
client_secret = os.getenv("CLIENT_SECRET")

# Call the function with your credentials
token = get_access_token(client_key, client_secret)

# Build loop for each month
today = date.today()
dataframes = []

while current_date < today:
    # Print or use the first day of the current month
    if current_date.day == 1:
        # Print for keeping track of progress
        print(f"Querying {str(current_date)}")

        if dataframes:
            # Dump the previous month's dataframes
            dump_dataframes(current_date, dataframes)

            # Reset the list
            dataframes = []

    # Update query
    current_date_str = current_date.strftime("%Y%m%d")

    query["start_date"] = current_date_str
    query["end_date"] = current_date_str
    
    # Use the token and the query to query videos
    response_json = query_videos(query=query, token=token, fields=fields)

    # Print the response
    print(response_json)

    data = response_json.get("data")
    if data["videos"]:
        # Load it into a dataframe
        df = pd.DataFrame(response_json["data"]["videos"])

        # Reformat timestamp
        df["timestamp"] = df["create_time"].apply(lambda x: datetime.fromtimestamp(x))

        # Create link
        df["embed_link"] = df["id"].apply(embed_link)

        # Store it in memory
        dataframes.append(df)        

    current_date += timedelta(days=1)
    time.sleep(randint(3, 7))

# Dump any remaining dataframes
dump_dataframes(current_date, dataframes)

print("All finished!")
