from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "LLM Provider Gateway"
    app_env: str = "local"

    groq_api_key: str | None = None
    gemini_api_key: str | None = None

    ollama_base_url: str = "http://localhost:11434/v1"
    ollama_model: str = "llama3.2:1b"

    groq_base_url: str = "https://api.groq.com/openai/v1"
    groq_model: str = "openai/gpt-oss-20b"

    gemini_model: str = "gemini-2.5-flash"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()