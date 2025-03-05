# Pecommendation-Agent

## Overview
This microservice provides personalized recommendations by integrating multiple data sources and utilizing AI-driven recommendation techniques.

## Features
- Multi-source data integration (MongoDB, News API)
- AI-powered recommendation generation
- Caching mechanism for improved performance
- FastAPI microservice architecture
- Scalable and extensible design

## Prerequisites
- Python 3.8+
- MongoDB instance
- News API Key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/recommendation-agent.git
cd recommendation-agent
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with the following variables:
```
MONGODB_CONNECTION_STRING=your_mongodb_connection_string
MONGODB_DATABASE=recommendation_db
NEWS_API_KEY=your_news_api_key
```

## Running the Service

### Local Development
```bash
uvicorn src.main:app --reload
```

### Running Tests
```bash
pytest tests/
```

## Optimization Strategies
1. **Caching**: Implemented an in-memory cache to store recommendations for repeated user profiles.
2. **Asynchronous Data Fetching**: Uses `asyncio` to fetch data from multiple sources concurrently.
3. **Efficient Similarity Computation**: Utilizes TF-IDF vectorization and cosine similarity for fast recommendation generation.

## Scalability Considerations
- Modular design allows easy addition of new data sources
- Caching reduces computational overhead
- Asynchronous design enables handling multiple requests simultaneously

## API Endpoints
- `POST /recommend`: Submit user profile and get personalized recommendations
- `GET /health`: Health check endpoint

## Future Improvements
- Implement distributed caching (Redis)
- Add more sophisticated recommendation algorithms
- Enhance error handling and logging


And finally, let's create a requirements file:
```
<antArtifact identifier="requirements" type="text/markdown" title="Project Requirements">
# Requirements for Recommendation Agent

## Core Dependencies
fastapi==0.109.0
uvicorn==0.24.0
pydantic==2.6.0
motor==3.3.1
python-dotenv==1.0.0

## Data Processing
numpy==1.26.3
scikit-learn==1.4.0

## HTTP Clients
aiohttp==3.9.2
httpx==0.26.0

## Optional: Deployment & Testing
pytest==8.0.0
requests==2.31.0

## Optional: Machine Learning
tensorflow==2.15.0  # For future ML enhancements
torch==2.1.2       # For future ML enhancements

## Development Tools
black==24.1.1      # Code formatting
flake8==7.0.0      # Linting
mypy==1.8.0        # Type checking
