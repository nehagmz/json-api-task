# JSON and API Interaction Task

## Project Overview
This script demonstrates the interaction with a REST API using Python. It reads JSON data from a file, sends data to an API using a POST request, retrieves data using a GET request, and combines the results into a single JSON file.

## API Details
- **API Endpoints Used**:
  - GET: `https://jsonplaceholder.typicode.com/posts/1`
  - POST: `https://jsonplaceholder.typicode.com/posts`
- **Request/Response Format**:
  - POST payload example:
    ```json
    {
        "FirstName": "John",
        "LastName": "Doe"
    }
    ```
  - POST response example:
    ```json
    {
        "FirstName": "John",
        "LastName": "Doe",
        "id": 101
    }
    ```
  - GET response example:
    ```json
    {
        "userId": 1,
        "id": 1,
        "title": "Sample Title",
        "body": "Sample body content."
    }
    ```
- **Response Status Handling**:
  - Handles HTTP errors and unexpected responses with clear error messages.

## Setup and Installation
- **Python Version Requirement**: Python 3.6+
- **Dependencies**:
  - `requests` library (Install using `pip install requests`)
- **Installation Steps**:
  1. Clone the repository.
  2. Navigate to the project directory.
  3. Install dependencies using `pip install -r requirements.txt`.

## Usage
1. Ensure the `data/sample_request.json` file exists with the required JSON input.
2. Run the script using:
   ```bash
   python src\api_json_handler.py
   ```
3. Output will be written to `data/sample_response.json`.

## Sample Output
Example combined output in `sample_response.json`:
```json
{
    "Input Data": {
        "key": "value"
    },
    "GET API Data": {
        "userId": 1,
        "id": 1,
        "title": "Sample Title",
        "body": "Sample body content."
    },
    "POST API Data": {
        "FirstName": "John",
        "LastName": "Doe",
        "id": 101
    }
}
```

## Implementation Details
- **Key Decisions**:
  - Used the `requests` library for API communication.
  - Separated concerns into distinct functions for readability and maintainability.
- **Challenges Faced**:
  - Ensuring proper error handling for file and API operations.
  - Combining data from multiple sources into a unified format.
- **Additional Libraries Used**:
  - None beyond Python standard libraries and `requests`.
