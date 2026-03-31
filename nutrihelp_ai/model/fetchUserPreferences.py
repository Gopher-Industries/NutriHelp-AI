# nutrihelp_ai/model/fetchUserPreferences.py

from .dbConnection import get_supabase
from typing import Optional, Dict, Any, List
import logging

logger = logging.getLogger(__name__)


async def fetch_user_preferences(user_id: str) -> Optional[Dict[str, Any]]:
    """
    Fetch user preferences (activity_level, dietary_preference, etc.)

    JavaScript equivalent:
    async function fetchUserPreferences(userId) {
        const { data, error } = await supabase
            .from('user_preferences')
            .select('*')
            .eq('user_id', userId)
            .single();
        if (error) throw error;
        return data;
    }

    Args:
        user_id: User ID to fetch preferences for

    Returns:
        User preferences dict with fields: activity_level, dietary_preference, 
        health_goals, meals_per_day, etc.
        Returns None if preferences not found

    Raises:
        Exception: If database query fails
    """
    try:
        supabase = get_supabase()

        response = (
            supabase.table('user_preferences')
            .select('*')
            .eq('user_id', user_id)
            .execute()
        )

        if response.data and len(response.data) > 0:
            prefs = response.data[0]
            logger.info(
                f"✅ Fetched preferences for: {user_id} (activity: {prefs.get('activity_level')}, diet: {prefs.get('dietary_preference')})")
            return prefs
        else:
            logger.warning(f"⚠️ No preferences found for: {user_id}")
            return None

    except Exception as error:
        logger.error(f"❌ Error fetching preferences: {str(error)}")
        raise error


async def fetch_user_allergies(user_id: str) -> List[str]:
    """
    Fetch user allergies as list of strings

    JavaScript equivalent:
    async function fetchUserAllergies(userId) {
        const { data, error } = await supabase
            .from('user_allergies')
            .select('allergy_name')
            .eq('user_id', userId);
        if (error) throw error;
        return data.map(item => item.allergy_name);
    }

    Args:
        user_id: User ID to fetch allergies for

    Returns:
        List of allergy names (strings)
        Returns empty list if no allergies found

    Raises:
        Exception: If database query fails
    """
    try:
        supabase = get_supabase()

        response = (
            supabase.table('user_allergies')
            .select('allergy_name')
            .eq('user_id', user_id)
            .execute()
        )

        if response.data:
            allergies = [item['allergy_name'] for item in response.data]
            logger.info(
                f"✅ Fetched {len(allergies)} allergies for: {user_id} ({', '.join(allergies)})")
            return allergies
        else:
            logger.info(f"ℹ️ No allergies found for: {user_id}")
            return []

    except Exception as error:
        logger.error(f"❌ Error fetching allergies: {str(error)}")
        raise error


# Export
__all__ = ['fetch_user_preferences', 'fetch_user_allergies']


# Test functions
if __name__ == "__main__":
    import asyncio
    from dotenv import load_dotenv
    load_dotenv()

    async def test():
        print("Testing fetch_user_preferences and fetch_user_allergies...")
        try:
            # Test preferences
            prefs = await fetch_user_preferences("user123")
            print(f"✅ Preferences: {prefs}")

            # Test allergies
            allergies = await fetch_user_allergies("user123")
            print(f"✅ Allergies: {allergies}")

        except Exception as e:
            print(f"❌ Error: {e}")

    asyncio.run(test())
