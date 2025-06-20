from google.adk.agents import Agent
from typing import Dict

def detect_manipulation(text: str) -> Dict:
    red_flags = [
        "if you loved me", "you always", "you never", "you're overreacting",
        "i said sorry", "you're too sensitive", "you're just imagining things",
        "i do everything for you"
    ]
    
    detected = [phrase for phrase in red_flags if phrase in text.lower()]
    
    if detected:
        return {
            "status": "warning",
            "flags": detected,
            "message": "Possible emotional manipulation detected."
        }
    else:
        return {
            "status": "clear",
            "message": "No emotional manipulation detected."
        }

message_analyzer_agent = Agent(
    name="message_analyzer_agent",
    model="gemini-2.0-flash",
    description="Detects emotionally manipulative language in user input.",
    instruction="Look for signs of emotional manipulation like guilt-tripping or gaslighting.",
    tools=[detect_manipulation],
)
