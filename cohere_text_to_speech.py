import cohere
from gtts import gTTS
import os

API_KEY ="05RVR7KnkCxDYs1RLguSc4NsuxNgjTDuHsOCDuZG"

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


if not os.path.exists("responses_audio"):
    os.makedirs("responses_audio")


with open("cohere_responses.txt", "w", encoding="utf-8", errors="ignore") as file:
    for idx, question in enumerate(questions, start=1):
        try:
       
            reply = generate_response(question)

            
            file.write(f"🟡 السؤال: {question}\n")
            file.write(f"🟢 الرد: {reply}\n")
            file.write("-" * 40 + "\n")

         
            tts = gTTS(text=reply, lang='ar')
            audio_filename = f"responses_audio/response_{idx}.mp3"
            tts.save(audio_filename)
            print(f"✅ تم حفظ الصوت: {audio_filename}")

        except Exception as e:
            print(f"❌ حصل خطأ في السؤال: {question}")
            print(f"🔍 الخطأ: {e}")
