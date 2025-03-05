import aiohttp
from typing import List, Dict

class NewsAPIDataSource:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/top-headlines"
    
    async def fetch_data(self, user_profile):
        try:
            async with aiohttp.ClientSession() as session:
                # More comprehensive category mapping
                categories = {
                    'technology': 'technology',
                    'sports': 'sports',
                    'music': 'entertainment',
                    'movies': 'entertainment',
                    'books': 'general',
                    'travel': 'general',
                    'food': 'health',
                    'fitness': 'health'
                }
                
                # Select first matching category
                selected_category = next(
                    (categories.get(str(interest).lower(), 'general') 
                     for interest in user_profile.interests), 
                    'general'
                )
                
                params = {
                    'apiKey': self.api_key,
                    'category': selected_category,
                    'language': (user_profile.preferred_languages[0] 
                                 if user_profile.preferred_languages 
                                 else 'en'),
                    'pageSize': 20
                }
                
                async with session.get(self.base_url, params=params) as response:
                    if response.status == 200:
                        data = await response.json()
                        return [
                            {
                                'title': article.get('title', ''),
                                'source': article.get('source', {}).get('name', ''),
                                'url': article.get('url', ''),
                                'category': selected_category
                            } for article in data.get('articles', [])
                        ]
                    print(f"News API error: {response.status}")
                    return []
        except Exception as e:
            print(f"News API fetch error: {e}")
            return []
