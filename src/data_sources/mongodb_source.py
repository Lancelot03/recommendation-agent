import motor.motor_asyncio
import urllib.parse
from typing import List, Dict

class MongoDBDataSource:
    def __init__(self, connection_string: str, database: str):
        # Properly parse the connection string
        parsed_uri = urllib.parse.urlparse(connection_string)
        self.client = motor.motor_asyncio.AsyncIOMotorClient(connection_string)
        self.db = self.client[database]
    
    async def fetch_data(self, user_profile):
        try:
            # Example of fetching content based on user interests
            interests = user_profile.interests
            
            collection = self.db['content']
            query = {
                'category': {'$in': [str(interest) for interest in interests]},
                'language': {'$in': user_profile.preferred_languages or ['en']}
            }
            
            cursor = collection.find(query).limit(50)
            results = await cursor.to_list(length=50)
            
            return [
                {
                    'id': str(item.get('_id', '')),
                    'title': item.get('title', ''),
                    'category': item.get('category', ''),
                    'relevance_score': item.get('relevance_score', 0.0)
                } for item in results
            ]
        except Exception as e:
            print(f"MongoDB fetch error: {e}")
            return []
