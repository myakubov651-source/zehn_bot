import telebot
import requests
import urllib.parse

BOT_TOKEN = "8719936624:AAHhCZPc8VCp29s8dtDZQIY0PZX1pqjMNI0"
GEMINI_KEY = "AQ.Ab8RN6KAPpTpsEdCkBqMqC65cOlczM1Sjqu-eurHzWcQL48ZnA"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men Zehn AI yordamchiman. Savollaringizni yozing.")

@bot.message_handler(commands=['image'])
def generate_image(message):
    prompt = message.text.replace('/image', '').strip()
    if not prompt:
        bot.reply_to(message, "Iltimos, rasm tavsifini yozing.")
        return
    bot.reply_to(message, "🎨 Rasm chizilmoqda...")
    image_url = f"https://image.pollinations.ai/p/{urllib.parse.quote(prompt)}?width=1024&height=1024&nologo=true"
    bot.send_photo(message.chat.id, image_url, caption=f"✨ So'rov: {prompt}")

@bot.message_handler(func=lambda message: True)
def ask_ai(message):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
    response = requests.post(url, json={"contents": [{"parts": [{"text": message.text}]}]})
    if response.status_code == 200:
        bot.reply_to(message, response.json()['candidates'][0]['content']['parts'][0]['text'])
    else:
        bot.reply_to(message, "Xatolik yuz berdi.")

bot.infinity_polling()
