import random
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("8523611351:AAFgBDt4qXJP3gGU7-EdCc6V8zuYBfJFji4")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎲 Salom! Zerikkaningizda narda o‘ynaymiz.\n"
        "/roll — tosh tashlash"
    )

async def roll(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_dice = random.randint(1, 6)
    bot_dice = random.randint(1, 6)

    if user_dice > bot_dice:
        result = "🎉 Siz yutdingiz!"
    elif user_dice < bot_dice:
        result = "😄 Bot yutdi!"
    else:
        result = "🤝 Durrang!"

    await update.message.reply_text(
        f"🎲 Siz: {user_dice}\n"
        f"🎲 Bot: {bot_dice}\n\n"
        f"{result}"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("roll", roll))
app.run_polling()
