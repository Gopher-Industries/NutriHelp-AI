"""Legacy compatibility wrapper for the active Groq + Chroma backend."""

from nutrihelp_ai.services.active_ai_backend import GroqChromaBackend


class AgentClass(GroqChromaBackend):
    """Backwards-compatible alias for older imports."""
