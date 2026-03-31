# nutrihelp_ai/model/fetchAllHealthConditions.py

from .dbConnection import get_supabase
from typing import List, Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


async def fetch_all_health_conditions() -> List[Dict[str, Any]]:
    """
    Fetch all health conditions from database

    JavaScript equivalent (YOUR EXACT CODE):
    async function fetchAllHealthConditions() {
        let { data, error } = await supabase
            .from('health_conditions')
            .select('*');
        if (error) throw error;
        return data;
    }

    Returns:
        List of health condition dicts with fields: id, name, description, etc.
        Returns empty list if no conditions found

    Raises:
        Exception: If database query fails
    """
    try:
        supabase = get_supabase()

        response = supabase.table('health_conditions').select('*').execute()

        if response.data:
            logger.info(f"✅ Fetched {len(response.data)} health conditions")
            return response.data
        else:
            logger.warning("⚠️ No health conditions found in database")
            return []

    except Exception as error:
        logger.error(f"❌ Error fetching health conditions: {str(error)}")
        raise error


async def fetch_health_condition_by_id(condition_id: int) -> Optional[Dict[str, Any]]:
    """
    Fetch a specific health condition by ID

    Args:
        condition_id: Health condition ID

    Returns:
        Health condition dict or None if not found
    """
    try:
        supabase = get_supabase()

        response = (
            supabase.table('health_conditions')
            .select('*')
            .eq('id', condition_id)
            .execute()
        )

        if response.data and len(response.data) > 0:
            condition = response.data[0]
            logger.info(f"✅ Fetched health condition: {condition.get('name')}")
            return condition
        else:
            logger.warning(f"⚠️ Health condition not found: {condition_id}")
            return None

    except Exception as error:
        logger.error(f"❌ Error fetching health condition: {str(error)}")
        raise error


async def fetch_health_condition_by_name(name: str) -> Optional[Dict[str, Any]]:
    """
    Fetch a specific health condition by name

    Args:
        name: Health condition name

    Returns:
        Health condition dict or None if not found
    """
    try:
        supabase = get_supabase()

        response = (
            supabase.table('health_conditions')
            .select('*')
            .ilike('name', f'%{name}%')
            .execute()
        )

        if response.data and len(response.data) > 0:
            condition = response.data[0]
            logger.info(f"✅ Fetched health condition: {condition.get('name')}")
            return condition
        else:
            logger.warning(f"⚠️ Health condition not found: {name}")
            return None

    except Exception as error:
        logger.error(f"❌ Error fetching health condition: {str(error)}")
        raise error


# Export (like module.exports)
__all__ = [
    'fetch_all_health_conditions',
    'fetch_health_condition_by_id',
    'fetch_health_condition_by_name'
]


# Test function
if __name__ == "__main__":
    import asyncio
    from dotenv import load_dotenv
    load_dotenv()

    async def test():
        print("Testing fetch_all_health_conditions...")
        try:
            conditions = await fetch_all_health_conditions()
            print(f"✅ Fetched {len(conditions)} health conditions:")
            for cond in conditions:
                print(f"   - {cond.get('name')}: {cond.get('description')}")

            # Test by ID
            if conditions:
                first_id = conditions[0].get('id')
                print(f"\nTesting fetch by ID ({first_id})...")
                cond = await fetch_health_condition_by_id(first_id)
                print(f"✅ Found: {cond.get('name')}")

            # Test by name
            print("\nTesting fetch by name ('Diabetes')...")
            cond = await fetch_health_condition_by_name('Diabetes')
            if cond:
                print(f"✅ Found: {cond.get('name')}")
            else:
                print("⚠️ Not found")

        except Exception as e:
            print(f"❌ Error: {e}")

    asyncio.run(test())
