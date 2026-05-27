from pydantic import BaseModel, Field

from app.core.enums import Provider, Framework, TaskType

class LLMRequest(BaseModel):
    provider: Provider = Field(... , examples=["groq"])
    framework: Framework = Field(..., examples=["direct"])
    task: TaskType = Field(..., examples=["chat"])
    input: str = Field(..., min_length=1)
    system_promt: str | None = None
    labels: list[str] | None = None
    temperature: float = 0.2
    max_tokens: int = 512

class LLMResponse(BaseModel):
    provider: str
    framework: str
    task: str
    model: str
    output: str