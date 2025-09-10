# nutrihelp_ai/agents/__init__.py
import os
from .agent_hf import AgentHF
from .agent_groq import AgentGroq

def get_agent():
    backend = os.getenv("NUTRIBOT_BACKEND", "hf").lower()
    if backend == "groq":
        return AgentGroq()
    return AgentHF()
