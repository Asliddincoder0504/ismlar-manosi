import json
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


def load_names_db():
    with open("ismlar_baza.json", "r", encoding="utf-8") as file:
        return json.load(file)


def find_name_meaning(name, names_db):
    for item in names_db:
        if item["properties"]["name"].lower() == name.lower():
            return item["properties"]["meaning"]
    return "Kechirasiz, bu ism bazada topilmadi."


def start(update: Update, context):
    update.message.reply_text("""Assalomu alaykum va Rahmatullohi va Barokatuh! 
    O'zingiz  yoki biror yaqin tanishingiz ism manosini bilmoqchimsz?  
    Ismni yozing! Bazi ismlar manosi topilmasligi mumkin""")


def handle_message(update: Update, context):
    user_text = update.message.text
    names_db = load_names_db()
    meaning = find_name_meaning(user_text, names_db)
    update.message.reply_text(f"{user_text}: {meaning}")


def main():
    TOKEN = "6494372838:AAG-1atdMYSE7KmgWDCsRFuuW_qA9T5jXhU"
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    print("Bot ishga tushdi...")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
