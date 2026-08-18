from backend.pipeline import run_pipeline

question = input("Enter symptoms: ")

result = run_pipeline(question)

print("\n==============================")
print("STATUS")
print(result["status"])

if result["status"] == "emergency":
    print(result["response"])

else:
    print("\nPredicted Disease:")
    print(result["diagnosis"]["disease"])

    print("\nFinal Response:")
    print(result["response"])

    print("\nSafety Review:")
    print(result["review"])