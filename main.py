import telebot
import google.generativeai as genai

BOT_TOKEN = "8719936624:AAHhCZPc8VCp29s8dtDZQIY0PZX1pqjMNI0"
GEMINI_KEY = "AQ.Ab8RN6JbgktnH2IFmDTum1N_5RNVLOiBFilcf7LAVx5qLqacVA"

bot = telebot.TeleBot(BOT_TOKEN)
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Kechirasiz, tizimda xatolik yuz berdi.")

bot.infinity_polling()
