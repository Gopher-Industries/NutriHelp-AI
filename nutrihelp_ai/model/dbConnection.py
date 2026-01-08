# nutrihelp_ai/model/dbConnection.py

import os
import sys
from supabase import create_client, Client
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class SupabaseConnection:
    """
    Supabase database connection handler
    Python equivalent of your Node.js dbConnection.js
    """

    _instance: Optional[Client] = None

    @classmethod
    def get_client(cls) -> Client:
        """Get or create Supabase client with environment validation"""
        if cls._instance is None:
            # Get environment variables
            # supabase_url = os.getenv("SUPABASE_URL")
            # supabase_anon_key = os.getenv("SUPABASE_ANON_KEY")
            supabase_url = "https://mdauzoueyzgtqsojttkp.supabase.co"
            supabase_anon_key = "sb_publishable_iPtvcFFdWB3q9YweOVHw8Q_ZEyhv_Jh"

            # Check if environment variables are loaded
            if not supabase_url or not supabase_anon_key:
                print('❌ Missing required environment variables:')
                print(
                    f'   SUPABASE_URL: {"✓ Set" if supabase_url else "✗ Missing"}')
                print(
                    f'   SUPABASE_ANON_KEY: {"✓ Set" if supabase_anon_key else "✗ Missing"}')
                print('\n💡 Please check your .env file contains:')
                print('   SUPABASE_URL=your_supabase_project_url')
                print('   SUPABASE_ANON_KEY=your_supabase_anon_key')
                sys.exit(1)

            # Create Supabase client
            try:
                cls._instance = create_client(supabase_url, supabase_anon_key)
                logger.info("✅ Supabase client connected successfully")
                print("✅ Supabase client connected successfully")
            except Exception as e:
                logger.error(f"❌ Failed to connect to Supabase: {str(e)}")
                print(f"❌ Failed to connect to Supabase: {str(e)}")
                sys.exit(1)

        return cls._instance


# Export the connection function (like module.exports in Node.js)
def get_supabase() -> Client:
    """
    Get Supabase client instance
    Equivalent to: module.exports = createClient(...)
    """
    return SupabaseConnection.get_client()


# Test connection when run directly
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    print("Testing Supabase connection...")
    try:
        client = get_supabase()
        print("✅ Connection test successful!")
        print(f"📍 Connected to: {os.getenv('SUPABASE_URL')}")
    except Exception as e:
        print(f"❌ Connection test failed: {str(e)}")
