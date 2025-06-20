from google.adk.agents import Agent

def generate_insight(cognitive_status: str, manipulation_flags: dict) -> dict:
    if cognitive_status == "high" and manipulation_flags.get("status") == "alert":
        return {
            "status": "warning",
            "report": "You may be experiencing burnout and emotional manipulation. Please take a break and set boundaries."
        }
    elif cognitive_status == "high":
        return {
            "status": "fatigued",
            "report": "You might be mentally overloaded. Consider delegating or taking rest."
        }
    elif manipulation_flags.get("status") == "alert":
        return {
            "status": "red_flag",
            "report": "Certain phrases suggest emotional manipulation. Trust your intuition and seek clarity."
        }
    else:
        return {
            "status": "stable",
            "report": "You appear to be emotionally stable based on current inputs."
        }

insight_agent = Agent(
    name="insight_agent",
    model="gemini-2.0-flash",
    description="Provides emotional insights based on manipulation and load detection agents.",
    instruction="Offer helpful, gentle insights based on the user's mental state.",
    tools=[generate_insight],
)
