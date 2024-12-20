import json
import requests

# Function to read JSON data from a file
def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return None

# Function to write JSON data to a file
def write_json(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error writing JSON to {file_path}: {e}")

# Function to make a GET API request
def fetch_api_data_get(api_url):
    response = requests.get(api_url)
    if 200 <= response.status_code < 300:
        return response.json()
    else:
        raise Exception(f"Non-success status code: {response.status_code}")

# Function to make a POST API request
def fetch_api_data_post(api_url, payload):
    response = requests.post(api_url, json=payload)
    if 200 <= response.status_code < 300:
        return response.json()
    else:
        raise Exception(f"Error posting data to API: {response.status_code}")

# Main function to handle the task
def main():
    input_file = "data/sample_request.json"
    output_file = "data/sample_response.json"

    # Step 1: Read JSON data from input file
    input_data = read_json(input_file)
    if input_data is None:
        print("Aborting script due to input file error.")
        return

    # Step 2: Make a GET request to the API
    api_url_get = "https://jsonplaceholder.typicode.com/posts/2"
    api_data_get = fetch_api_data_get(api_url_get)
    if api_data_get is None:
        print("Aborting script due to GET API error.")
        return

    # Step 3: Payload for POST request 
    payload = {"FirstName": "John","LastName": "Doe"}

    # Step 4: Make a POST request to the API
    api_url_post = "https://jsonplaceholder.typicode.com/posts"
    api_data_post = fetch_api_data_post(api_url_post, payload)
    if api_data_post is None:
        print("Aborting script due to POST API error.")
        return

    # Step 5: Combine data
    combined_data = {
        "Input Data": input_data,
        "GET API Data": api_data_get,
        "POST API Data": api_data_post
    }

    # Step 6: Write combined data to output file
    write_json(combined_data, output_file)
    print("Script executed successfully!")

# Run the main function
if __name__ == "__main__":
    main()
