from vosk import Model, KaldiRecognizer
import wave
import json

# تحميل النموذج
model = Model("models/ar")

# فتح ملف الصوت
wf = wave.open("converted.wav", "rb")

# التحقق من تنسيق الملف
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("⚠️ الملف يجب أن يكون WAV بصيغة PCM أحادي (mono)")
    exit(1)

# إعداد المحول
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)

# تجميع النص الناتج
result_text = ""

print("⏳ جاري تحويل الصوت إلى نص...")

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        res = json.loads(rec.Result())
        result_text += res.get("text", "") + " "

# الحصول على آخر جزء
res = json.loads(rec.FinalResult())
result_text += res.get("text", "")

# طباعة النص
print("\n📄 النص الناتج:")
print(result_text)

# حفظه في ملف
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(result_text)

print("\n✅ تم حفظ النص في ملف output.txt")