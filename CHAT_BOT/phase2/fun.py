import os
import requests

# Get the OpenAPI key from the environment variable
openapi_key = os.getenv("OPENAPI_KEY")

# Use the OpenAPI key to make an API request
headers = {"Authorization": f"Bearer {openapi_key}"}
response = requests.get("(link unavailable)", headers=headers)

# Print the response
print(response.json())
