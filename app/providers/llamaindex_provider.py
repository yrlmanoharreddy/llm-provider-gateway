from llama_index.llms.openai_like import OpenAILike
from llama_index.llms.google_genai import GoogleGenAI



from app.providers.base import BaseLLMProvider
from app.schemas.llm_schema import LLMRequest
from app.prompts.task_prompts import build_prompts
from app.core.enums import Provider
from app.core.config import settings

class LlamaIndexProvider(BaseLLMProvider):
    def _getllm(self, provider: Provider):
        if provider==Provider.OLLAMA:
            return OpenAILike(
                model= settings.ollama_model,
                api_base=settings.ollama_base_url,
                api_key="ollama",
                is_chat_model=True
            ), settings.ollama_model
        if provider == Provider.GEMINI:
            return GoogleGenAI(
                model=settings.gemini_model,
                api_key=settings.gemini_api_key,
            ), settings.gemini_model
        raise ValueError(f"Unsupported provider: {provider}")
    def generate(self, request: LLMRequest)->tuple[str, str]:
        prompt = build_prompts(request.task, request.input, request.labels)

        client, model = self._getllm(request.provider)
        final_prompt = f"""
        System:
        {request.system_prompt or "You are a helpful AI assistant."}

        User:
        {prompt}
        """
        response = client.complete(final_prompt)
        return str(response), model
