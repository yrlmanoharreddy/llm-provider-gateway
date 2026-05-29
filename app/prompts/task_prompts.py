from app.core.enums import TaskType

def build_prompts(task: TaskType, user_input: str, labels: list[str] | None=None) -> str:
    
    if task == TaskType.CHAT:
        return user_input
    if task == TaskType.SUMMARIZE:
        return f"Summarize the following text clearly and conciesely. Text: {user_input}"
    
    if task == TaskType.EXTRACT_JSON:
        return f"""Extract structured JSON from the text below
        Return only valide JSON. Do not include markdown

        Text:
        {user_input}
        """
    
    if task==TaskType.CLASSIFY:
        label_text = ", ".join(labels or ["Positive", "negative", "neutral"])
        return """
        Classify the text into one of these labels: {label_text}.
        Return only the label.
        Text:
        {user_input}
        """
    
    return user_input

