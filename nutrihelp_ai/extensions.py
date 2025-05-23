# nutrihelp_ai/extensions.py
from slowapi.extension import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
