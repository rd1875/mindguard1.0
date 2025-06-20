from google.adk.agents import Agent

def suggest_boundaries(flag_type: str) -> dict:
    response_templates = {
        "gaslighting": "I remember things differently, and my feelings are valid.",
        "guilt_tripping": "I care, but I also need space to make my own decisions.",
        "control": "I prefer to have a say in this matter as well."
    }

    if flag_type not in response_templates:
        return {"status": "unknown", "report": "No template available for that pattern."}

    return {
        "status": "ok",
        "report": response_templates[flag_type]
    }

boundary_coach_agent = Agent(
    name="boundary_coach_agent",
    model="gemini-2.0-flash",
    description="Provides healthy boundary-setting suggestions based on manipulation detected.",
    instruction="Help the user respond assertively but respectfully to manipulation attempts.",
    tools=[suggest_boundaries],
)
