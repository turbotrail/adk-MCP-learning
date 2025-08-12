from google.adk.agents import LlmAgent

robo_critic = LlmAgent(
    name="robo_critic",
    model="gemini-2.0-flash",
    description="Robot critic agent",
    instruction="""
    Provide constructive criticism and feedback on text to ensure it sounds more robotic.
    """,
)
