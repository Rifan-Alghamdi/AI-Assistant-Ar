from vosk import Model, KaldiRecognizer 
import wave 
import json 
 

model = Model("models/ar") 
 

wf = wave.open("converted.wav", "rb") 
 

if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE": 
    print("⚠️ الملف يجب أن يكون WAV بصيغة PCM أحادي (mono)") 
    exit(1) 
 

rec = KaldiRecognizer(model, wf.getframerate()) 
rec.SetWords(True) 
 

result_text = "" 
 
print("⏳ جاري تحويل الصوت إلى نص...") 
 
while True: 
    data = wf.readframes(4000) 
    if len(data) == 0: 
        break 
    if rec.AcceptWaveform(data): 
        res = json.loads(rec.Result()) 
        result_text += res.get("text", "") + " " 
 

res = json.loads(rec.FinalResult()) 
result_text += res.get("text", "") 
 

print("\n📄 النص الناتج:") 
print(result_text) 
 

with open("output.txt", "w", encoding="utf-8") as f: 
    f.write(result_text) 
 
print("\n✅ تم حفظ النص في ملف output.txt")
