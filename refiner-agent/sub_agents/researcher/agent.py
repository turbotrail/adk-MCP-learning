from google.adk.agents import Agent

researcher_agent = Agent(
    name="researcher_agent",
    model="gemini-2.0-flash",
    description="Researcher agent",
    instruction="""
    Work with the refiner_agent to gather and summarize information from various sources.
    """,
)
