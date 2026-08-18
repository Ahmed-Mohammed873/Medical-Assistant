# backend/pipeline.py

from backend.safety_layer import (
    check_emergency,
    review_response,
    apply_safety_disclaimer,
    EMERGENCY_MESSAGE,
)

from backend.diagnosis import diagnose
from backend.retrieval import retrieve
from backend.prompt_builder import build_diagnosis_prompt
from backend.gemini_client import generate_response


def run_pipeline(user_input: str) -> dict:
    """
    Complete Medical Assistant Pipeline.
    """

    # ==========================================================
    # Step 1 : Emergency Check
    # ==========================================================

    if check_emergency(user_input):
        return {
            "status": "emergency",
            "response": EMERGENCY_MESSAGE
        }

    # ==========================================================
    # Step 2 : Diagnosis
    # ==========================================================

    diagnosis_result = diagnose(user_input)

    predicted_disease = diagnosis_result["disease"]

    # ==========================================================
    # Step 3 : Retrieve Medical Context
    # ==========================================================

    rag_results = retrieve(user_input, top_k=5)

    context = "\n\n".join(chunk["text"] for chunk in rag_results)

    # ==========================================================
    # Step 4 : Build Prompt
    # ==========================================================

    prompt = build_diagnosis_prompt(
        symptoms=user_input,
        diagnosis=predicted_disease,
        rag_results=rag_results
    )

    # ==========================================================
    # Step 5 : Generate Final Response
    # ==========================================================

    response = generate_response(prompt)

    # ==========================================================
    # Step 6 : Safety Review
    # ==========================================================

    review = review_response(
        response=response,
        context=context
    )

    # ==========================================================
    # Step 7 : Apply Safety Disclaimer
    # ==========================================================

    final_response = apply_safety_disclaimer(
        response,
        review
    )

    # ==========================================================
    # Return Result
    # ==========================================================

    return {
        "status": "success",
        "symptoms": user_input,
        "diagnosis": diagnosis_result,
        "retrieved_chunks": rag_results,
        "review": review,
        "response": final_response
    }