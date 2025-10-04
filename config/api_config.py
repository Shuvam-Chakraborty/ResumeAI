import os

# API Configuration
# Create from openrouter.ai -> meta-llama/llama-4-maverick:free
# LLAMA_API_KEY = os.getenv('LLAMA_API_KEY', 'your-api-key-here')
LLAMA_API_KEY = os.getenv('LLAMA_API_KEY', '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')
LLAMA_API_URL = "https://openrouter.ai/api/v1/chat/completions"
LLAMA_MODEL = "meta-llama/llama-4-maverick:free"

# API Settings
API_TIMEOUT = 30
MAX_TOKENS = 500
TEMPERATURE = 0.7