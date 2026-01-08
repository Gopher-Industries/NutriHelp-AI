# nutrihelp_ai/model/fetchUserHealthConditions.py

from .dbConnection import get_supabase
from typing import List, Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

async def fetch_user_health_conditions(user_id: str) -> List[Dict[str, Any]]:
    """
    Fetch health conditions for a specific user with full condition details
    
    JavaScript equivalent:
    async function fetchUserHealthConditions(userId) {
        const { data, error } = await supabase
            .from('user_health_conditions')
            .select(`
                *,
                health_conditions (*)
            `)
            .eq('user_id', userId);
        if (error) throw error;
        return data;
    }
    
    Args:
        user_id: User ID to fetch health conditions for
        
    Returns:
        List of user health conditions with nested condition details
        Each item contains:
        - id: user_health_condition record ID
        - user_id: User ID
        - condition_id: Health condition ID
        - severity: Condition severity (mild, moderate, severe)
        - diagnosed_date: When condition was diagnosed
        - health_conditions: Nested health condition details (name, description)
        
        Returns empty list if no conditions found
        
    Raises:
        Exception: If database query fails
    """
    try:
        supabase = get_supabase()
        
        response = (
            supabase.table('user_health_conditions')
            .select('*, health_conditions(*)')
            .eq('user_id', user_id)
            .execute()
        )
        
        if response.data:
            condition_names = [
                item.get('health_conditions', {}).get('name', 'Unknown')
                for item in response.data
            ]
            logger.info(f"✅ Fetched {len(response.data)} health conditions for user: {user_id} ({', '.join(condition_names)})")
            return response.data
        else:
            logger.info(f"ℹ️ No health conditions found for user: {user_id}")
            return []
            
    except Exception as error:
        logger.error(f"❌ Error fetching user health conditions: {str(error)}")
        raise error


async def fetch_user_condition_names(user_id: str) -> List[str]:
    """
    Fetch only the names of user's health conditions
    
    Args:
        user_id: User ID
        
    Returns:
        List of condition names (strings)
        
    Example:
        ['Diabetes', 'Hypertension', 'Celiac Disease']
    """
    try:
        conditions = await fetch_user_health_conditions(user_id)
        condition_names = [
            cond.get('health_conditions', {}).get('name', '')
            for cond in conditions
            if cond.get('health_conditions')
        ]
        return [name for name in condition_names if name]  # Filter empty strings
        
    except Exception as error:
        logger.error(f"❌ Error fetching user condition names: {str(error)}")
        raise error


async def add_user_health_condition(
    user_id: str, 
    condition_id: int, 
    severity: str = 'moderate',
    diagnosed_date: Optional[str] = None
) -> Dict[str, Any]:
    """
    Add a health condition to a user
    
    Args:
        user_id: User ID
        condition_id: Health condition ID
        severity: Condition severity ('mild', 'moderate', 'severe')
        diagnosed_date: Date diagnosed (YYYY-MM-DD format)
        
    Returns:
        Created user_health_condition record
        
    Raises:
        Exception: If database insert fails
    """
    try:
        supabase = get_supabase()
        
        data = {
            'user_id': user_id,
            'condition_id': condition_id,
            'severity': severity
        }
        
        if diagnosed_date:
            data['diagnosed_date'] = diagnosed_date
        
        response = (
            supabase.table('user_health_conditions')
            .insert(data)
            .execute()
        )
        
        if response.data:
            logger.info(f"✅ Added health condition {condition_id} to user: {user_id}")
            return response.data[0]
        else:
            raise Exception("Failed to add health condition")
            
    except Exception as error:
        logger.error(f"❌ Error adding user health condition: {str(error)}")
        raise error


async def remove_user_health_condition(user_id: str, condition_id: int) -> bool:
    """
    Remove a health condition from a user
    
    Args:
        user_id: User ID
        condition_id: Health condition ID to remove
        
    Returns:
        True if successfully removed
        
    Raises:
        Exception: If database delete fails
    """
    try:
        supabase = get_supabase()
        
        response = (
            supabase.table('user_health_conditions')
            .delete()
            .eq('user_id', user_id)
            .eq('condition_id', condition_id)
            .execute()
        )
        
        logger.info(f"✅ Removed health condition {condition_id} from user: {user_id}")
        return True
            
    except Exception as error:
        logger.error(f"❌ Error removing user health condition: {str(error)}")
        raise error


# Export
__all__ = [
    'fetch_user_health_conditions',
    'fetch_user_condition_names',
    'add_user_health_condition',
    'remove_user_health_condition'
]


# Test functions
if __name__ == "__main__":
    import asyncio
    from dotenv import load_dotenv
    load_dotenv()
    
    async def test():
        print("Testing user health conditions functions...")
        try:
            user_id = "user123"
            
            # Test fetch user conditions
            print(f"\n1. Fetching conditions for user: {user_id}")
            conditions = await fetch_user_health_conditions(user_id)
            print(f"✅ Found {len(conditions)} conditions:")
            for cond in conditions:
                hc = cond.get('health_conditions', {})
                print(f"   - {hc.get('name')}: {cond.get('severity')}")
            
            # Test fetch condition names only
            print(f"\n2. Fetching condition names only...")
            names = await fetch_user_condition_names(user_id)
            print(f"✅ Condition names: {', '.join(names)}")
            
            # Uncomment to test add/remove (will modify database)
            # print(f"\n3. Testing add condition...")
            # await add_user_health_condition(user_id, 1, 'mild')
            # print("✅ Condition added")
            
            # print(f"\n4. Testing remove condition...")
            # await remove_user_health_condition(user_id, 1)
            # print("✅ Condition removed")
            
        except Exception as e:
            print(f"❌ Error: {e}")
    
    asyncio.run(test())