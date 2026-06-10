import os
import telebot
import google.generativeai as genai

# Render'dan kalitlarni chaqirib olish
BOT_TOKEN = os.environ.get("BOT_TOKEN")
GEMINI_KEY = os.environ.get("GEMINI_KEY")

# Telegram va Gemini sozlamalari
bot = telebot.TeleBot(BOT_TOKEN)
genai.configure(api_key=GEMINI_KEY)

# Modelni sozlash (Ensiklopediya kabi javob berishi uchun)
model = genai.GenerativeModel('gemini-pro')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Men sizning shaxsiy yordamchingizman. "
                          "Mendan istalgan narsa haqida so‘rashingiz mumkin: tarix, fan, "
                          "musiqa olami yoki boshqa har qanday savol!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Foydalanuvchi xabarini Gemini'ga yuborish
        # Prompt: "Sen bilimdon yordamchisan" deb belgilaymiz
        prompt = f"Sen bilimdon yordamchisan. Foydalanuvchining savoliga aniq va tushunarli javob ber: {message.text}"
        response = model.generate_content(prompt)
        
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "Kechirasiz, bu savolga hozir javob bera olmayman. Boshqa savol so‘rab ko‘ring.")
        print(f"Error: {e}")

if __name__ == "__main__":
    bot.polling(none_stop=True)
    
