import cohere

API_KEY = "05RVR7KnkCxDYs1RLguSc4NsuxNgjTDuHsOCDuZG"

co = cohere.Client(API_KEY)

questions = [
    "كيف حالك؟",
    "أنا مهتم بتعلم أشياء جديدة، كيف أبدأ؟",
    "ما هو الذكاء الاصطناعي؟",
    "كيف أتعلم الإلكترونيات بشكل فعّال؟",
    "ما أهمية التعلم المستمر؟"
]

def generate_response(user_input):
    response = co.generate(
        model='command-r-plus',
        prompt=user_input,
        max_tokens=200,
        temperature=0.7,
    )
    return response.generations[0].text.strip()

# ✅ حفظ الردود بدون أرقام
with open("cohere_responses.txt", "w", encoding="utf-8", errors="ignore") as file:
    for q in questions:
        try:
            reply = generate_response(q)
            file.write(f"🟡 السؤال: {q}\n")
            file.write(f"🟢 الرد: {reply}\n")
            file.write("-" * 40 + "\n")
        except Exception as e:
            file.write(f"❌ حصل خطأ أثناء الرد على: {q}\n")
            file.write(f"السبب: {str(e)}\n")
            file.write("-" * 40 + "\n")

print("✅ تم حفظ الردود في ملف: cohere_responses.txt")