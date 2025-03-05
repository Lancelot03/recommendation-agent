import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict
import asyncio

class RecommendationEngine:
    def __init__(self, data_sources: List):
        self.data_sources = data_sources
        self.cache = {}
    
    async def generate_recommendations(self, user_profile, top_k=10):
        # Check cache first
        cache_key = user_profile.user_id
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        # Fetch data from multiple sources concurrently
        source_data = await asyncio.gather(
            *[source.fetch_data(user_profile) for source in self.data_sources]
        )
        
        # Flatten the data from all sources
        all_items = [item for source in source_data for item in source]
        
        # If no items found, return empty list
        if not all_items:
            return []
        
        # Extract text features for recommendations
        texts = [
            f"{item.get('title', '')} {item.get('category', '')}" 
            for item in all_items
        ]
        
        # Compute similarity based on user interests and content
        user_interests_text = " ".join(str(interest) for interest in user_profile.interests)
        texts.append(user_interests_text)
        
        # Use TF-IDF and cosine similarity for recommendation
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(texts)
        
        # Compute similarity scores
        user_profile_vector = tfidf_matrix[-1]
        content_vectors = tfidf_matrix[:-1]
        similarity_scores = cosine_similarity(user_profile_vector, content_vectors)[0]
        
        # Rank recommendations
        ranked_indices = np.argsort(similarity_scores)[::-1]
        
        recommendations = [
            {
                'item': all_items[idx],
                'similarity_score': float(similarity_scores[idx])
            } 
            for idx in ranked_indices[:top_k]
        ]
        
        # Cache results
        self.cache[cache_key] = recommendations
        
        return recommendations
