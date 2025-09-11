import google.generativeai as genai
from anyio import fail_after, to_thread
from app.core.settings import gemini_settings
from app.prompts.templates import Template


def _get_model() -> genai.GenerativeModel:
    if not gemini_settings.api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured")
    genai.configure(api_key=gemini_settings.api_key)
    return genai.GenerativeModel(gemini_settings.model)


def generate_gemini_response(user_input: str, template: Template) -> str:
    prompt = template.substitute(user_input=user_input)
    try:
        model = _get_model()
        response = model.generate_content(prompt)
        # google-generativeai returns response with candidates; .text property flattens
        return (response.text or "").strip()
    except Exception as e:  # noqa: BLE001
        return f"Error: {str(e)}"


async def generate_gemini_response_async(user_input: str, template: Template, timeout_seconds: float = 20.0) -> str:
    try:
        async with fail_after(timeout_seconds):
            return await to_thread.run_sync(generate_gemini_response, user_input, template)
    except TimeoutError:
        return "Error: Request to Gemini timed out"
