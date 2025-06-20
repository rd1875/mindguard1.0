from google.adk.agents import Agent
from mindguard_agents.message_analyzer_agent import detect_manipulation
from .cognitive_load_agent import detect_cognitive_load
from .insight_agent import generate_insight
from mindguard_agents.pattern_detector_agent import update_pattern_memory as detect_patterns
from .boundary_coach_agent import suggest_boundaries

root_agent = Agent(
    name="mindguard_emotional_safety",
    model="gemini-1.5-flash",
    description="Detects emotional manipulation and mental overload",
    instruction=(
        "You're an emotional safety AI. Analyze user text for emotional manipulation,"
        " cognitive strain, and provide insights or boundary coaching."
    ),
    tools=[
        detect_manipulation,
        detect_cognitive_load,
        detect_patterns,
        generate_insight,
        suggest_boundaries
    ]
)
