from google.adk.agents import Agent
import re

def detect_cognitive_load(text: str) -> dict:
    overload_keywords = ['had to', 'needed to', 'remember', 'planned', 'managed', 'took care', 'responsible for']
    count = sum(1 for k in overload_keywords if k in text.lower())
    
    if count >= 3:
        return {
            "status": "high",
            "report": f"Detected cognitive overload: {count} signs found."
        }
    else:
        return {
            "status": "low",
            "report": "No major signs of overload detected."
        }

cognitive_load_agent = Agent(
    name="cognitive_load_agent",
    model="gemini-2.0-flash",
    description="Detects signs of cognitive overload from user journaling or task logs.",
    instruction="You are a cognitive load detector. Identify if the user is mentally overloaded.",
    tools=[detect_cognitive_load],
)
