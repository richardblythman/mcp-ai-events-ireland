# Events Agent

An agent that fetches events from an API and uses OpenAI Agents library to provide search, summarization, and recommendation capabilities.

## Installation

This project uses `uv` for dependency management. If you don't have `uv` installed, you can install it following the instructions at [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv).

### Install dependencies with uv

```bash
uv pip install -e .
```

## Configuration

Create a `.env` file in the project root with your OpenAI API key:

```
OPENAI_API_KEY=your-api-key-here
```

## Usage

Run the interactive agent:

```bash
python events_agent.py
```

The agent will:
1. Ask what you'd like to know about events in Dublin
2. Use the events API to fetch the latest event data
3. Provide information based on your query

You can ask various questions about events such as:
- "What AI events are happening in Dublin?"
- "Can you summarize the upcoming events?"
- "What would you recommend for someone interested in machine learning?"

## Architecture

The Events Agent uses the OpenAI Agents framework to create a system of specialized agents:

1. **Orchestrator Agent** - The main agent that coordinates the specialized agents and has these tools:
   - **fetch_events** - Fetches the latest events data from the API
   - **search_events** - Finds events matching specific criteria
   - **summarize_events** - Generates summaries for events
   - **recommend_events** - Recommends events based on user preferences

The orchestrator agent first uses the fetch_events tool to get the latest data, then decides which specialized agent to use based on the user's query.