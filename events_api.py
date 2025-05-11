import requests

class EventAPI:
    def __init__(self, base_url="http://localhost:3000"):
        self.base_url = base_url

    def get_events(self):
        try:
            response = requests.get(f"{self.base_url}/api/events")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return data['events']
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

# Usage example
if __name__ == "__main__":
    api = EventAPI()
    events = api.get_events()
    if events:
        for event in events:
            print(f"Title: {event['title']}, City: {event['city']}, Date: {event['datetime']}") 