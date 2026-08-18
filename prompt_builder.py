# prompt_builder.py

def build_diagnosis_prompt(symptoms: str, diagnosis: str, rag_results: list) -> str:
    """
    Build the prompt sent to Gemini.
    """

    context_text = ""

    for i, result in enumerate(rag_results[:3], start=1):
        context_text += f"""
Source {i} ({result['source']} - {result['focus_area']}):
{result['text']}
"""

    prompt = f"""
You are a safe medical information assistant.

IMPORTANT RULES:

1. Answer ONLY using the information in the Sources section.
2. Do NOT make up information.
3. If the sources are not enough, clearly say that.
4. The predicted disease is ONLY a preliminary suggestion, NOT a confirmed diagnosis.
5. Never prescribe medications or provide drug dosages.
6. Always recommend consulting a qualified doctor.
7. Respond in the SAME language used by the user.
   - If the user writes in Arabic, answer in Arabic.
   - If the user writes in English, answer in English.
   - Otherwise answer in the user's language.
8. Keep the answer short (around 150-200 words).
9. Use simple language and bullet points whenever possible.

=========================
User Symptoms:
{symptoms}

Predicted Disease:
{diagnosis}

Sources:
{context_text}
=========================

Generate your answer with this structure:

- Preliminary condition
- Brief explanation
- Possible symptoms/causes (from the sources only)
- Recommendation
"""
    return prompt