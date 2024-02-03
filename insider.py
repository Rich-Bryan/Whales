import requests
import json
import config

url = "https://api.benzinga.com/api/v1/signal/option_activity"

api_key = config.API_KEYS


querystring = {"token":api_key,"parameters[tickers]":"AAPL"}

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers, params=querystring)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response text as JSON
    data = response.json()

    # Specify the file name for the JSON file
    json_file_name = "response_data.json"

    # Save the JSON data to a file
    with open(json_file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"JSON data saved to {json_file_name}")
else:
    print(f"Error: {response.status_code}, {response.text}")

