import telebot
import google.generativeai as genai

# TOKEN va API KALITLARNI SHU YERGA YOZING
BOT_TOKEN = "SIZNING_TOKENINGIZNI_SHU_YERGA_YOZING"
GEMINI_KEY = "SIZNING_KALITINGIZNI_SHU_YERGA_YOZING"

# Bot va Gemini sozlamalari
bot = telebot.TeleBot(=8719936624:AAHhCZPc8VCp29s8dtDZQIY0PZX1pqjMNI0
GE)
genai.configure(Ab8RN6JwtqQ9Zpw7xPemqQjoRuezdThXxNy1maBeciorl4kgcg)
model = genai.GenerativeModel('gemini-pro')

# Kanal tekshiruvisiz oddiy chat funksiyasi
@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Kechirasiz, tizimda xatolik yuz berdi.")

print("Bot ishga tushdi...")
bot.infinity_polling()
