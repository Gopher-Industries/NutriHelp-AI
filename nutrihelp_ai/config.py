# ============================================================================
# FILE 1: config.py
# Configuration file with API keys and settings
# ============================================================================

# Gemini API Configuration
# ⚠️ EXPOSED! REVOKE IMMEDIATELY!
# GEMINI_API_KEY = "AIzaSyA_kYa1kKVfpFYdIMcX9Idqq70lfYvCy7o"
GEMINI_API_KEY = "AIzaSyBRFwdgWDN0QLbW1i3cfymseDNQx2YoXB4"
# Note: This model does not exist. Use "gemini-1.5-flash"
GEMINI_MODEL = "gemini-2.5-flash"

# Voice settings
VOICE_RATE = 150  # Speed of speech
VOICE_VOLUME = 0.9  # Volume (0.0 to 1.0)

# Speech recognition settings
LISTEN_TIMEOUT = 10  # Seconds to wait for speech
PHRASE_TIME_LIMIT = 15  # Max seconds for a phrase
