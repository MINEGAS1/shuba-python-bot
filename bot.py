import random
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8400518828:AAGJhXYoYdbPwFH8MMzegbPaqlc-2r2653A"
PORT = int(os.environ.get("PORT", 10000))
RENDER_URL = os.environ.get("RENDER_EXTERNAL_URL", "")

PRICES = {
    "Оцени шубу!": [3000, 4000, 5000],
    "Оцени шубу.": [5000, 6000, 7000, 8000],
    "Оцени, шубу": [8000, 9000, 10000, 11000, 12000],
    "Оцени эту шубу": [12000, 13000, 14000, 15000],
    "Оцени пожалуйста шубу": [15000, 16000, 17000, 18000, 19000, 20000],
}

HELP_TEXT = """
Команды:
Оцени шубу! — 3-5 тыс. рублей
Оцени шубу. — 5-8 тыс. рублей
Оцени, шубу — 8-12 тыс. рублей
Оцени эту шубу — 12-15 тыс. рублей
Оцени пожалуйста шубу — 15-20 тыс. рублей
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Для получения помощи напишите /help")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT)

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    caption = update.message.caption
    if caption and caption in PRICES:
        price = random.choice(PRICES[caption])
        await update.message.reply_text(f"{price} рублей")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    
    if RENDER_URL:
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            webhook_url=f"{RENDER_URL}/webhook"
        )
    else:
        app.run_polling()

if __name__ == "__main__":
    def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    
    if RENDER_URL:
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            webhook_url=f"{RENDER_URL}/webhook"
        )
    else:
        app.run_polling()
