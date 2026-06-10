import os
import telebot
import google.generativeai as genai

BOT_TOKEN = os.environ.get("BOT_TOKEN")
GEMINI_KEY = os.environ.get("GEMINI_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        # Bu qator xatoni sizga loglarda ko'rsatadi
        print(f"XATOLIK: {e}") 
        bot.reply_to(message, f"Tizim xatosi: {e}")

bot.infinity_polling()
