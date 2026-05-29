from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

from app.providers.base import BaseLLMProvider
from app.schemas.llm_schema import LLMRequest
from app.prompts.task_prompts import build_prompts
from app.core.enums import Provider
from app.core.config import settings
class LangChainProvider(BaseLLMProvider):
    def _get_llm(self, provider: Provider, temperature: float, max_tokens: int):
        if provider == Provider.OLLAMA:
            return ChatOpenAI(
                api_key= "ollama",
                base_url=settings.ollama_base_url,
                model=settings.ollama_model,
                temperature=temperature,
                max_tokens=max_tokens
            ), settings.ollama_model
        if provider == Provider.GEMINI:
            return ChatGoogleGenerativeAI(
                google_api_key = settings.gemini_api_key,
                model = settings.gemini_model,
                temperature=temperature,
                max_output_tokens = max_tokens
            ), settings.gemini_model
        if provider == Provider.GROQ:
            return ChatOpenAI(
                api_key=settings.groq_api_key,
                base_url=settings.groq_base_url,
                model=settings.groq_model,
                temperature=temperature,
                max_tokens=max_tokens,
            ), settings.groq_model
        
        raise ValueError(f"Unsupported provider: {provider}")

    def generate(self, request: LLMRequest)-> tuple[str, str]:
        prompt = build_prompts(request.task, request.input, request.labels)

        client, model = self._get_llm(
            request.provider,
            request.temperature,
            request.max_tokens
        )

        response = client.invoke(
            [
                SystemMessage(content=request.system_prompt or "You are a helpful AI assistant."),
                HumanMessage(content=prompt)
            ]
        )

        return response.content, model