import json
import requests

def get_access_token(client_key, client_secret, output_fp="token_info.json", dump=False):
    # Endpoint URL
    endpoint_url = "https://open.tiktokapis.com/v2/oauth/token/"

    # Request headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    # Request body parameters
    data = {
        'client_key': client_key,
        'client_secret': client_secret,
        'grant_type': 'client_credentials',
    }

    # Make the POST request
    response = requests.post(endpoint_url, headers=headers, data=data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response JSON
        response_json = response.json()
        print("Acquired access token, expires in", response_json['expires_in'])

        if dump:
            with open(output_fp, "w") as f:
                json.dump(response_json, f)
        
        return response_json['access_token']
    else:
        # If the request was not successful, print the error response JSON
        print("Error:", response.json())