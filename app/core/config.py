import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get API key from environment
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment or .env file")

# Initialize OpenAI client
openai_client = OpenAI(api_key=openai_api_key)

# App configuration
APP_TITLE = "Voice Chatbot API"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "An AI voice chatbot API with personality adaptation"

# Default model settings
WHISPER_MODEL = "whisper-1"
CHAT_MODEL = "gpt-3.5-turbo"

# Server settings
HOST = "0.0.0.0"
PORT = 8001
RELOAD = True 