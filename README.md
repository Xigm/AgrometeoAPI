# AgrometeoAPI

A Python client for accessing the Agrometeo API.

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Xigm/AgrometeoAPI.git
   cd AgrometeoAPI
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API key**
   - Copy `.env.example` to `.env`
   - Edit `.env` and add your actual API key
   ```bash
   cp .env.example .env
   # Then edit .env with your API key
   ```

## Usage

### Basic Example

```python
from agrometeo_api import AgrometeoAPIClient

# Using context manager (recommended)
with AgrometeoAPIClient() as client:
    # Make API requests
    response = client.get('/your-endpoint')
    print(response)
```

### Without Context Manager

```python
from agrometeo_api import AgrometeoAPIClient

client = AgrometeoAPIClient()
try:
    response = client.get('/your-endpoint')
    print(response)
finally:
    client.close()
```

## Configuration

Configuration is managed through environment variables. See `.env.example` for available options:

- `API_KEY` (required): Your API key
- `API_BASE_URL` (optional): Base URL for the API
- `TIMEOUT` (optional): Request timeout in seconds
- `DEBUG` (optional): Enable debug mode

## Project Structure

```
AgrometeoAPI/
├── .env.example          # Template for environment variables
├── .gitignore           # Git ignore file (includes .env)
├── README.md            # This file
├── config.py            # Configuration loader
├── agrometeo_api.py     # Main API client
└── requirements.txt     # Python dependencies
```

## Security

- Never commit your `.env` file (it's already in `.gitignore`)
- Keep your API keys secret
- Use environment variables for sensitive data