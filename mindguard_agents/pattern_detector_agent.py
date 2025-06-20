from google.adk.agents import Agent
from collections import defaultdict
import datetime

user_history = defaultdict(list)

def update_pattern_memory(user_id: str, message: str, flag_type: str) -> dict:
    timestamp = datetime.datetime.now().isoformat()
    user_history[user_id].append((timestamp, message, flag_type))
    
    past_week = [msg for ts, msg, ft in user_history[user_id][-7:] if ft == flag_type]
    
    return {
        "status": "tracked",
        "report": f"{len(past_week)} instances of '{flag_type}' pattern in recent interactions."
    }

pattern_detector_agent = Agent(
    name="pattern_detector_agent",
    model="gemini-2.0-flash",
    description="Tracks and summarizes repeated red flag behaviors over time.",
    instruction="Track emotional manipulation or mental strain patterns from user history.",
    tools=[update_pattern_memory],
)
