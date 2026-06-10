import telebot
import requests
import os
from flask import Flask
from threading import Thread

BOT_TOKEN = "8719936624:AAHhCZPc8VCp29s8dtDZQIY0PZX1pqjMNI0"
GEMINI_KEY = "SIZNING_GEMINI_API_KALITINGIZ" # O'zingizning kalitingizni yozing
CHANNEL_ID = "@A_ToolsX"

bot = telebot.TeleBot(BOT_TOKEN)
bot.remove_webhook()

# 1. Flask serveri (Render portni ko'rishi uchun)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot ishlayapti!"

def run_server():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
# 3. Asosiy handlerlar
@bot.message_handler(func=lambda message: True)
def chat(message):
        
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
        data = {"contents": [{"parts": [{"text": message.text}]}]}
        response = requests.post(url, json=data).json()
        reply = response['candidates'][0]['content']['parts'][0]['text']
        bot.reply_to(message, reply)
    except Exception:
        bot.reply_to(message, "Kechirasiz, tizimda xatolik yuz berdi.")

# 4. Server va botni birga ishga tushirish
if __name__ == "__main__":
    Thread(target=run_server).start()
    bot.infinity_polling()
    
