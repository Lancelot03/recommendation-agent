from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Import local modules
from models.user_profile import UserProfile
from data_sources.mongodb_source import MongoDBDataSource
from data_sources.news_source import NewsAPIDataSource
from recommendation.engine import RecommendationEngine

# Initialize FastAPI app
app = FastAPI(
    title="Personalized Recommendation Agent",
    description="AI-driven recommendation microservice",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Credentials (in a real-world scenario, use environment variables)
MONGO_URI = "mongodb+srv://Harsh:Harshsingh2003%40@aira.htvju.mongodb.net/?retryWrites=true&w=majority&appName=AIRA"
NEWS_API_KEY = "3-4IK6W5IKfuJxx9zzux_cFwa62zHVYl9_KPNwhB0fTMhqHq"

# Initialize data sources
mongodb_source = MongoDBDataSource(
    connection_string=MONGO_URI,
    database='AIRA'
)

news_source = NewsAPIDataSource(
    api_key=NEWS_API_KEY
)

# Initialize recommendation engine
recommendation_engine = RecommendationEngine([
    mongodb_source, 
    news_source
])

@app.post("/recommend")
async def get_recommendations(user_profile: UserProfile):
    try:
        recommendations = await recommendation_engine.generate_recommendations(user_profile)
        return {
            "user_id": user_profile.user_id,
            "recommendations": recommendations
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Optional: Uvicorn server entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
