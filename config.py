# config.py

import os

class Config:
    # MongoDB Configuration
    MONGO_URI = os.environ.get("MONGO_URI") or "mongodb+srv://yashitiwary:9838yashi@cluster0.r5x2deh.mongodb.net/diet_planner?retryWrites=true&w=majority"
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-this")
    
    # Google Gemini Configuration (FREE!)
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyAu4Oddsfl1HNGmHR6ya5BzJ1fPSAkK240")
    GEMINI_MODEL = "gemini-2.0-flash"  # Correct model name
    
    # AI Configuration
    AI_TEMPERATURE = 0.7  # Creativity level for meal generation
    AI_MAX_TOKENS = 2000  # Max response length
    
    # Rate Limiting for AI API calls
    AI_RATE_LIMIT_PER_USER = 50  # Gemini has generous free tier
    
    # Caching
    CACHE_EXPIRY = 3600  # 1 hour cache for AI responses
    
    # Meal Planning Defaults
    DEFAULT_CUISINE_STYLE = "international"
    DEFAULT_MEAL_COMPLEXITY = "medium"
    MAX_INGREDIENTS_PER_MEAL = 12
    
    # Feature Flags
    ENABLE_AI_MEAL_PLANNING = os.environ.get("ENABLE_AI_MEAL_PLANNING", "true").lower() == "true"
    ENABLE_NUTRITION_TRACKING = os.environ.get("ENABLE_NUTRITION_TRACKING", "true").lower() == "true"
    
    # Development/Production
    DEBUG = os.environ.get("FLASK_DEBUG", "true").lower() == "true"
    TESTING = os.environ.get("TESTING", "false").lower() == "true"
    
    # Session Configuration
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = 86400  # 24 hours in seconds