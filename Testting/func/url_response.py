import requests

def get_response():
    response = requests.get("https://example.com/id")
    print(response)
    if response.status_code == 200:
        print(response.json())
        return response.json()['slideshow']

