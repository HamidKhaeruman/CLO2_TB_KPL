import json
import os
from typing import Dict, Any, Optional

class ConfigLoader:
    """
    A class to handle runtime configuration loading with defensive programming techniques.
    Implements runtime configuration construction pattern.
    """
    
    def __init__(self, config_file: str = 'soal_config.json'):
        """
        Initialize the ConfigLoader with a configuration file.
        
        Args:
            config_file: Name of the JSON configuration file
        """
        self.config_file = os.path.join(os.path.dirname(__file__), config_file)
        self._config_data = None
        self._last_modified = 0
        
    def _validate_config(self, config: Any) -> bool:
        """
        Validate the configuration structure.
        
        Args:
            config: Loaded configuration data
            
        Returns:
            bool: True if configuration is valid, False otherwise
        """
        if not isinstance(config, list):
            return False
            
        required_keys = {'category', 'question', 'answer'}
        for item in config:
            if not isinstance(item, dict):
                return False
            if not required_keys.issubset(item.keys()):
                return False
            if not all(isinstance(item[key], str) for key in required_keys):
                return False
                
        return True
    
    def _load_config_file(self) -> Optional[Dict]:
        """
        Safely load and parse the configuration file.
        
        Returns:
            Optional[Dict]: Parsed configuration data or None if error occurs
        """
        try:
            # Check if file exists and is readable
            if not os.path.exists(self.config_file):
                raise FileNotFoundError(f"Configuration file not found: {self.config_file}")
            if not os.access(self.config_file, os.R_OK):
                raise PermissionError(f"No read permission for file: {self.config_file}")
                
            # Get last modified time for potential caching
            current_modified = os.path.getmtime(self.config_file)
            
            # Only reload if file has changed or did not been loaded yet
            if self._config_data is None or current_modified > self._last_modified:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    
                if not self._validate_config(config):
                    raise ValueError("Invalid configuration structure")
                    
                self._config_data = config
                self._last_modified = current_modified
                
            return self._config_data
            
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON configuration: {e}")
        except (FileNotFoundError, PermissionError, ValueError) as e:
            print(f"Configuration error: {e}")
        except Exception as e:
            print(f"Unexpected error loading configuration: {e}")
            
        return None
    
    def get_config(self) -> Optional[Dict]:
        """
        Public method to get the configuration data.
        Implements defensive programming by handling all potential errors.
        
        Returns:
            Optional[Dict]: The configuration data or None if error occurs
        """
        return self._load_config_file()
    
    def get_questions_by_category(self, category: str) -> Optional[list]:
        """
        Get questions filtered by category.
        
        Args:
            category: The category to filter questions by
            
        Returns:
            Optional[list]: List of questions in the category or None if error occurs
        """
        config = self.get_config()
        if config is None:
            return None
            
        try:
            return [q for q in config if q['category'].lower() == category.lower()]
        except Exception as e:
            print(f"Error filtering questions by category: {e}")
            return None

def load_quiz_data() -> Optional[list]:
    """
    Public function to load quiz data using ConfigLoader.
    Maintains compatibility with existing code.
    
    Returns:
        Optional[list]: List of quiz questions or None if error occurs
    """
    loader = ConfigLoader()
    return loader.get_config()