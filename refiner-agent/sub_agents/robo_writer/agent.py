from google.adk.agents import LlmAgent

robo_writer = LlmAgent(
    name="robo_writer",
    model="gemini-2.0-flash",
    description="Robot writer agent",
    instruction="""
    Ensure to maintain a robotic tone and style in all written content.
    """,
)
