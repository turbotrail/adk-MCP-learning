from google.adk.agents import Agent,LoopAgent
from google.adk.sessions import InMemorySessionService
from .sub_agents.training.agent import training_agent
from .sub_agents.researcher.agent import researcher_agent
from .sub_agents.robo_writer.agent import robo_writer
from .sub_agents.robo_critic.agent import robo_critic
session_service_stateful = InMemorySessionService()

robot_agent = LoopAgent(
    name="robot_agent_loop",
    description="Looping mechanism for the robot agent",
    sub_agents=[robo_writer, robo_critic],
    max_iterations=5
)

root_agent = Agent(
    name="refiner_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    description="Refiner agent",
    instruction="""
Work with  researcher_agent , robot_agent and transformer_agent to refine information from documents.
    """,
    sub_agents=[
        researcher_agent,
        robot_agent,
        training_agent
    ]
)
