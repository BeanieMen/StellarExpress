import requests
import os

# URL of the Flask server
url = 'http://localhost:80/api/upload'

# Path to the image file
image_path = 'test/a.jpg'

# Open the image file in binary mode
with open(image_path, 'rb') as file:
    # Send a POST request with the image file
    response = requests.post(url, files={'file': file})

# Print the response from the server
print(response.json())
