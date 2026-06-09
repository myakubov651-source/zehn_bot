import telebot
import requests

BOT_TOKEN = "8719936624:AAHhCZPc8VCp29s8dtDZQIY0PZX1pqjMNI0"
GEMINI_KEY = "YANGI_API_KALITINGIZNI_SHU_YERGA_QUYING"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men Zehn AI botman.")

@bot.message_handler(func=lambda message: True)
def ask_ai(message):
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
        headers = {'Content-Type': 'application/json'}
        data = {"contents": [{"parts": [{"text": message.text}]}]}
        
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            reply = result['candidates'][0]['content']['parts'][0]['text']
            bot.reply_to(message, reply)
        else:
            bot.reply_to(message, "Xatolik yuz berdi. API kalitni tekshiring.")
    except Exception as e:
        bot.reply_to(message, "Tizimda xatolik yuz berdi.")

bot.infinity_polling()
