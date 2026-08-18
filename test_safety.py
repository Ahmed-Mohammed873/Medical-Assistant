from backend.safety_layer import (
    check_emergency,
    review_response,
    apply_safety_disclaimer,
)
# Test 1: emergency detection
print("Emergency test 1:", check_emergency("I have severe chest pain"))
print("Emergency test 2:", check_emergency("What are the symptoms of diabetes?"))

# Test 2: response review
sample_response = "You definitely have diabetes. Take 500mg of metformin twice a day."
sample_context = "Diabetes symptoms include increased thirst, frequent urination, and fatigue."

review_result = review_response(sample_response, sample_context)
print("Review result:", review_result)

final_response = apply_safety_disclaimer(sample_response, review_result)
print("Final response with disclaimers:")
print(final_response)