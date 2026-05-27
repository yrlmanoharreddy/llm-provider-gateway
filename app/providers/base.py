from abc import ABC, abstractmethod
from app.schemas.llm_schema import LLMRequest


class BaseLLMProvider(ABC):

    @abstractmethod
    def generate(self, request: LLMRequest)-> tuple[str, str]
        """
        Returns:
        output_text, model_name
        """
        pass