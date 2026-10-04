import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load configuration values
APP_NAME = os.getenv("APP_NAME")
DEBUG = os.getenv("DEBUG")
MAX_STUDENTS = os.getenv("MAX_STUDENTS")
API_KEY = os.getenv("API_KEY")
