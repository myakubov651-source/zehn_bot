import telebot
import requests

BOT_TOKEN = "8719936624:AAHhCZPc8VCp29s8dtDZQIY0PZX1pqjMNI0"
GEMINI_KEY = "SIZNING_GEMINI_API_KALITINGIZ"
CHANNEL_ID = "@A_ToolsX" # Kanal manzili

bot = telebot.TeleBot(BOT_TOKEN)

# Kanalga obunani tekshirish funksiyasi
def check_subscription(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            return True
        return False
    except:
        return False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if check_subscription(message.from_user.id):
        bot.reply_to(message, "Salom! Men Zehn AI botman. Savollaringizni yozing.")
    else:
        bot.reply_to(message, "🚀 To use this bot, you must join our channel: https://t.me/A_ToolsX")

@bot.message_handler(func=lambda message: True)
def ask_ai(message):
    if not check_subscription(message.from_user.id):
        bot.reply_to(message, "🚀 To use this bot, you must join our channel: https://t.me/A_ToolsX")
        return

    # Agar obuna bo'lsa, AI javob beradi
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_KEY}"
        data = {"contents": [{"parts": [{"text": message.text}]}]}
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            reply = response.json()['candidates'][0]['content']['parts'][0]['text']
            bot.reply_to(message, reply)
        else:
            bot.reply_to(message, "Xatolik yuz berdi.")
    except Exception as e:
        bot.reply_to(message, "Tizimda xatolik.")

bot.infinity_polling()
