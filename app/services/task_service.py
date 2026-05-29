from app.schemas.llm_schema import LLMRequest, LLMResponse
from app.services.gateway_factory import GatewayFactory


class TaskService:
    def execute(self, request: LLMRequest)-> LLMResponse:
        provider_adaptor = GatewayFactory.get_provider(request.framework)
        output, model = provider_adaptor.generate(request)

        return LLMResponse(
            provider=request.provider,
            framework=request.framework,
            task=request.task,
            model=model,
            output=output
        )