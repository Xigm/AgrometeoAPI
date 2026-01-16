"""
Configuration module for AgrometeoAPI.
Loads environment variables from .env file.
"""
import os
from pathlib import Path
from typing import Optional

try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False


class Config:
    """Configuration class for API settings."""
    
    def __init__(self):
        """Initialize configuration by loading environment variables."""
        if DOTENV_AVAILABLE:
            # Load .env file from the same directory as this file
            env_path = Path(__file__).parent / '.env'
            load_dotenv(dotenv_path=env_path)
        
        self.api_key: Optional[str] = os.getenv('API_KEY')
        self.api_base_url: str = os.getenv('API_BASE_URL', 'https://api.agrometeo.example.com')
        self.timeout: int = int(os.getenv('TIMEOUT', '30'))
        self.debug: bool = os.getenv('DEBUG', 'False').lower() in ('true', '1', 'yes')
    
    def validate(self) -> None:
        """
        Validate that required configuration values are present.
        
        Raises:
            ValueError: If required configuration values are missing.
        """
        if not self.api_key:
            raise ValueError(
                "API_KEY is not set. Please set it in your .env file or environment variables."
            )


# Create a default config instance
config = Config()
