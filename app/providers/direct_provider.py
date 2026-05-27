from openai import OpenAI
from google import genai

from app.providers.base import BaseLLMProvider
from app.schemas.llm_schema import LLMRequest
from app.prompts.task_prompts import build_prompts
from app.core.enums import Provider
from app.core.config import settings

class DirectProvider(BaseLLMProvider):

    def _get_openai_comp(self, provider: Provider):
        if provider == Provider.OLLAMA:
            return OpenAI(
                api_key="ollama",
                base_url=settings.ollama_base_url,
            ), settings.ollama_model
        if provider == Provider.GROQ:
            return OpenAI(
                api_key=settings.groq_api_key,
                base_url=settings.groq_base_url
            ), settings.groq_model
        raise ValueError(f"Provider {provider} is not OpenAI-compatible in this adapter.")

    def generate(self, request: LLMRequest)-> tuple[str, str]:
        prompt = build_prompts(request.task, request.input, request.labels)

        if request.provider == Provider.GEMINI:
            client = genai.Client()
            response = client.models.generate_content(
                model = settings.gemini_model,
                contents=prompt,
            )
            return response.text or "", settings.gemini_model
        
        client, model = self._get_openai_comp(request.provider)

        response = client.chat.completions.create(
            model = model,
            messages= [
                {
                    "role": "system",
                    "content": request.system_prompt or "You are a helpful AI assistant.",
                },
                {
                    "role" : "user",
                    "content" : prompt,
                }
            ],
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )
        return response.choices[0].message.content or "", model