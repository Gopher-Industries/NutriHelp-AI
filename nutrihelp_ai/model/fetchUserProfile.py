# nutrihelp_ai/model/fetchUserProfile.py

from .dbConnection import get_supabase
from typing import Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)


async def fetch_user_profile(user_id: str) -> Optional[Dict[str, Any]]:
    """
    Fetch user profile (age, gender, weight, height, etc.)

    JavaScript equivalent:
    async function fetchUserProfile(userId) {
        const { data, error } = await supabase
            .from('users')
            .select('*')
            .eq('id', userId)
            .single();
        if (error) throw error;
        return data;
    }

    Args:
        user_id: User ID to fetch profile for

    Returns:
        User profile dict with fields: id, age, gender, weight, height, etc.
        Returns None if user not found

    Raises:
        Exception: If database query fails
    """
    try:
        supabase = get_supabase()

        response = (
            supabase.table('users')
            .select('*')
            .eq('user_id', user_id)
            .execute()
        )

        if response.data and len(response.data) > 0:
            user = response.data[0]
            logger.info(
                f"✅ Fetched user profile: {user_id} (age: {user.get('age')}, gender: {user.get('gender')})")
            return user
        else:
            logger.warning(f"⚠️ User not found: {user_id}")
            return None

    except Exception as error:
        logger.error(f"❌ Error fetching user profile: {str(error)}")
        raise error


# Export (like module.exports)
__all__ = ['fetch_user_profile']


# Test function
if __name__ == "__main__":
    import asyncio
    from dotenv import load_dotenv
    load_dotenv()

    async def test():
        print("Testing fetch_user_profile...")
        try:
            profile = await fetch_user_profile("user123")
            if profile:
                print(f"✅ Profile fetched: {profile}")
            else:
                print("⚠️ User not found")
        except Exception as e:
            print(f"❌ Error: {e}")

    asyncio.run(test())
