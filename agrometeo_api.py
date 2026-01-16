"""
Main API client for Agrometeo API.
Provides methods to interact with the API endpoints.
"""
import requests
from typing import Dict, Any, Optional
from config import config


class AgrometeoAPIClient:
    """Client for interacting with the Agrometeo API."""
    
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        """
        Initialize the API client.
        
        Args:
            api_key: API key for authentication. If not provided, uses config.
            base_url: Base URL for the API. If not provided, uses config.
        """
        self.api_key = api_key or config.api_key
        self.base_url = base_url or config.api_base_url
        self.timeout = config.timeout
        
        if not self.api_key:
            raise ValueError("API key is required. Set it via parameter or .env file.")
        
        # Setup session for connection pooling
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        })
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Make an HTTP request to the API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            params: Query parameters
            json: JSON body data
            
        Returns:
            Dict containing the JSON response
            
        Raises:
            ValueError: If endpoint is empty
            requests.exceptions.RequestException: If the request fails
        """
        if not endpoint.strip():
            raise ValueError('Endpoint cannot be empty')
        
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        response = self.session.request(
            method=method,
            url=url,
            params=params,
            json=json,
            timeout=self.timeout,
        )
        
        response.raise_for_status()
        return response.json()
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make a GET request to the API.
        
        Args:
            endpoint: API endpoint path
            params: Query parameters
            
        Returns:
            Dict containing the JSON response
        """
        return self._make_request('GET', endpoint, params=params)
    
    def post(
        self,
        endpoint: str,
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Make a POST request to the API.
        
        Args:
            endpoint: API endpoint path
            json: JSON body data
            params: Query parameters
            
        Returns:
            Dict containing the JSON response
        """
        return self._make_request('POST', endpoint, params=params, json=json)
    
    def close(self):
        """Close the session."""
        self.session.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


# Example usage
if __name__ == '__main__':
    # Example of how to use the client
    try:
        # Using context manager (recommended)
        with AgrometeoAPIClient() as client:
            # Example: Make a GET request to a hypothetical endpoint
            # response = client.get('/stations')
            # print(response)
            print("API client initialized successfully!")
            print(f"Base URL: {client.base_url}")
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please create a .env file based on .env.example and set your API_KEY")
    except Exception as e:
        print(f"Error: {e}")
