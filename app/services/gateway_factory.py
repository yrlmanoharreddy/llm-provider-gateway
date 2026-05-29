from app.core.enums import Framework
from app.providers.base import BaseLLMProvider
from app.providers.direct_provider import DirectProvider
from app.providers.langchain_provider import LangChainProvider
from app.providers.llamaindex_provider import LlamaIndexProvider
class GatewayFactory:
    @staticmethod
    def get_provider(framwork: Framework) -> BaseLLMProvider:
        if framwork == Framework.DIRECT:
            return DirectProvider()
        if framwork == Framework.LANGCHAIN:
            return LangChainProvider()
        if framwork == Framework.LLAMAINDEX:
            return LlamaIndexProvider()
        
        raise ValueError(f"Unsupported framework: {framework}")