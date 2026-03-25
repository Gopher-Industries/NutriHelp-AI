# nutrihelp_ai/agents/__init__.py
import os
from nutrihelp_ai.services.active_ai_backend import GroqChromaBackend
from .agent_hf import AgentHF

def get_agent():
    backend = os.getenv("NUTRIBOT_BACKEND", "groq").lower()
    if backend == "hf_legacy":
        return AgentHF()
    return GroqChromaBackend()
