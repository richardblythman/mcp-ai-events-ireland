import requests
import asyncio
from pydantic import BaseModel
from agents import Agent, Runner, function_tool
from dotenv import load_dotenv
from typing import List

load_dotenv()

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

class Event(BaseModel):
    id: str
    title: str
    city: str
    datetime: str
    organiser: str
    blurb: str
    description: str
    url: str
    createdAt: str

class Events(BaseModel):
    events: List[Event]

@function_tool
def get_events(city: str) -> Events:
    print("[debug] get_events called")
    api = EventAPI()
    events = api.get_events()
    return Events(events=[Event(**event) for event in events])


events_agent = Agent(
    name="Events Agent",
    instructions="You are a helpful agent that can help me find events in a city.",
    tools=[get_events],
)


async def main():
    result = await Runner.run(events_agent, input="What events are happening in Dublin?")
    print(result.final_output)
    # The weather in Tokyo is sunny.


if __name__ == "__main__":
    asyncio.run(main())