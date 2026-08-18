# safety_layer.py

from backend.gemini_client import generate_json_response

EMERGENCY_KEYWORDS = [
    "chest pain", "can't breathe", "difficulty breathing",
    "severe bleeding", "suicide", "unconscious", "stroke symptoms",
    "heart attack", "severe allergic reaction", "anaphylaxis"
]

EMERGENCY_MESSAGE = (
    "This may describe a medical emergency. "
    "Please call emergency services or go to the nearest hospital immediately. "
    "This assistant cannot help with urgent or life-threatening situations."
)


def check_emergency(user_input: str) -> bool:
    """
    Checks if the user's message contains any emergency-related keywords.
    Must run BEFORE the rest of the pipeline (retrieval, diagnosis, generation).
    """
    text = user_input.lower()
    return any(keyword in text for keyword in EMERGENCY_KEYWORDS)


def build_review_prompt(response: str, context: str) -> str:
    """
    Builds the prompt used to ask Gemini to review its own previous response.
    """
    return f"""
Review the following medical assistant response and answer with JSON only.

Response to review:
{response}

Source information the response should be based on:
{context}

Answer these 3 questions:
1. "has_dosage": Does the response mention a specific drug dosage or amount? true/false
2. "final_diagnosis": Does the response state a diagnosis as confirmed/final rather than preliminary? true/false
3. "hallucination": Does the response include any claim NOT supported by the source information? true/false

Reply with JSON only, no extra text: {{"has_dosage": ..., "final_diagnosis": ..., "hallucination": ...}}
"""


def review_response(response: str, context: str) -> dict:
    """
    Runs the self-review check on a generated response.
    Returns a dict with the three safety flags.
    """
    review_prompt = build_review_prompt(response, context)
    return generate_json_response(review_prompt)


def apply_safety_disclaimer(response: str, review_result: dict) -> str:
    """
    Adds safety warnings to the generated response.
    """

    warnings = []

    if review_result.get("has_dosage"):
        warnings.append(
            "⚠️ Do not rely on any medication dosage mentioned above without consulting a qualified doctor."
        )

    if review_result.get("final_diagnosis"):
        warnings.append(
            "⚠️ This is a preliminary medical suggestion, not a confirmed diagnosis."
        )

    if review_result.get("hallucination"):
        warnings.append(
            "⚠️ Some information could not be fully verified using the retrieved medical sources."
        )

    general_disclaimer = (
        "\n\n----------------------------------------\n"
        "Medical Disclaimer:\n"
        "This AI assistant provides educational information only.\n"
        "It does NOT replace a doctor, medical diagnosis, or professional treatment.\n"
        "If your symptoms become severe or you believe you have a medical emergency, seek immediate medical care."
    )

    if warnings:
        response += "\n\n" + "\n".join(warnings)

    response += general_disclaimer

    return response