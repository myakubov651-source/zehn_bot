import os
import telebot
import google.generativeai as genai

# Render sozlamalaridan kalitlarni o‘qiydi
BOT_TOKEN = os.environ.get("BOT_TOKEN")
GEMINI_KEY = os.environ.get("GEMINI_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
genai.configure(api_key=GEMINI_KEY)

# Gemini modelini sozlash
model = genai.GenerativeModel('gemini-pro')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men sizning yordamchingizman. Menga istalgan savol (tarix, fan, musiqa) bering, men javob beraman.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Gemini'dan javob olish
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Kechirasiz, javob olishda xatolik yuz berdi. Iltimos, qaytadan urinib ko‘ring.")

bot.polling(none_stop=True)
