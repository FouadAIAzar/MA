import os
from dotenv import load_dotenv

def load_environment_variables():
    """Load environment variables from .env file."""
    # Locate the .env file relative to this script
    dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..', '.env')
    load_dotenv(dotenv_path)

