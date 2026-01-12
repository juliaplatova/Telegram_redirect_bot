import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username or "no_username"
    print(f"User clicked: ID={user_id}, username=@{username}")
    
    await update.message.reply_text("Привет! Вот ссылка на канал: https://t.me/+5ehzskWsAAc5ZGFi")

if __name__ == "__main__":
    token = os.environ["BOT_TOKEN"]
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
