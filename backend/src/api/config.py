import configparser
import os
from os import getenv
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

_settings: 'Settings | None' = None

# Load .env file from the backend directory (next to src/)
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env'))

class Settings(BaseSettings):
    def __init__(self) -> None:
        super().__init__()
        self._config_parser = self._load_config_file()

    def _load_config_file(self) -> configparser.ConfigParser | None:
        """Load configuration from app.conf file"""
        ...

    def _get_config_value(self, section: str, key: str, default: str = '') -> str:
        """Get value from config file."""
        if self._config_parser and self._config_parser.has_option(section, key):
            return self._config_parser.get(section, key)
        return default
    
    # region properties
    
    @property
    def environment(self) -> str:
        return getenv('ENVIRONMENT', 'dev')
    
    @property
    def auth0_domain(self) -> str:
        return getenv('AUTH0_DOMAIN', '')
    
    @property
    def auth0_api_audience(self) -> str:
        return getenv('AUTH0_AUDIENCE', 'http://localhost:8123/')
    
    @property
    def auth0_algorithms(self) -> str:
        return getenv('AUTH0_ALGORITHMS', 'RS256')
    
    @property
    def auth0_issuer(self) -> str:
        return f'https://{self.auth0_domain}/'
    
    # endregion
    
    class Config:
        env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env')
        extra = 'ignore'

def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
