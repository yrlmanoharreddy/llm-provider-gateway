from enum import Enum

class Provider(str, Enum):
    OLLAMA = "ollama"
    GEMINI = "gemini"
    GROQ = "groq"

class Framework(str, Enum):
    DIRECT = "direct"
    LANGCHAIN = "langchain"
    LLAMAINDEX = "llamaindex"

class TaskType(str, Enum):
    CHAT = "chat"
    SUMMARIZE = "summarize"
    EXTRACT_JSON = "extract-json"
    CLASSIFY = "classify"