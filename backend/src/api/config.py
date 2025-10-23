import configparser
from os import getenv
from pydantic_settings import BaseSettings

_settings: 'Settings | None' = None

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
    
    # endregion
    
    class Config:
        env_file = '.env'
        extra = 'ignore'

def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
