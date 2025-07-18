import tkinter as tk
from tkinter import messagebox
import cohere
from gtts import gTTS
import os
import time
import random
from playsound import playsound
import threading

# مفتاح Cohere
API_KEY = "05RVR7KnkCxDYs1RLguSc4NsuxNgjTDuHsOCDuZG"
co = cohere.Client(API_KEY)


def generate_response(user_input):
    try:
        response = co.generate(
            model='command-r-plus',
            prompt=user_input,
            max_tokens=150,
            temperature=0.7,
        )
        return response.generations[0].text.strip()
    except Exception as e:
        print(f"خطأ في توليد الرد: {e}")
        return "حدث خطأ أثناء توليد الرد."

def speak_text(text):
    try:
        filename = f"response_{int(time.time())}_{random.randint(1000,9999)}.mp3"
        tts = gTTS(text=text, lang='ar')
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        messagebox.showerror("خطأ", f"فشل تشغيل الصوت: {e}")

def on_ask():
    question = entry.get().strip()
    if question == "":
        messagebox.showinfo("تنبيه", "اكتب سؤالك أولاً.")
        return

    response = generate_response(question)

    # عرض الرد مباشرة
    response_label.config(text=response, wraplength=450, justify="right")

    # تشغيل الصوت في الخلفية
    threading.Thread(target=speak_text, args=(response,), daemon=True).start()

root = tk.Tk()
root.title("المساعد الذكي")
root.geometry("520x420")
root.configure(bg="#e9f1fc")

title = tk.Label(root, text="المساعد الذكي", font=("Segoe UI", 22, "bold"), bg="#e9f1fc", fg="#0b5394")
title.pack(pady=15)

entry = tk.Entry(root, font=("Segoe UI", 14), width=45, justify="right", bg="white", fg="black", relief="groove", bd=2)
entry.pack(pady=12)

ask_button = tk.Button(root, text="اسأل", font=("Segoe UI", 13, "bold"), bg="#0b5394", fg="white", width=10, command=on_ask)
ask_button.pack(pady=8)

response_label = tk.Label(root, text="", font=("Segoe UI", 14), bg="#e9f1fc", fg="#333", wraplength=450, justify="right")
response_label.pack(pady=20)

root.mainloop()