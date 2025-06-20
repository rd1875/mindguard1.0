from mindguard_agents import root_agent

if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()
    root_agent.run()
