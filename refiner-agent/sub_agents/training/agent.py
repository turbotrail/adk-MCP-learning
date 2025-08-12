from google.adk.agents import LlmAgent

training_agent = LlmAgent(
    name="training_agent",
    model="gemini-2.0-flash",
    description="Training agent to help users learn about a specific topic.",
    instruction="""
    For a given topic, provide a comprehensive overview and key points to consider.
    """,
)
