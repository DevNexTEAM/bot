import asyncio
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import nest_asyncio

# Configurar logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Tu token de bot
TOKEN = '7341867073:AAFXGCGVlRnek8cirp1137Xbdh2IXvhVDfQ'

# Tu ID de Telegram para recibir mensajes
ADMIN_ID = 7627481429

# Funciones que maneja los comandos y mensajes
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('¡Hola! Soy tu bot 🛠️')

async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    # 1. Reenviar mensaje al admin
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"📩 Mensaje de {user.username or user.first_name}:\n\n{update.message.text}"
    )

    # 2. Responderle al usuario
    await update.message.reply_text(
        f"👋 ¡Hola {user.first_name}! Gracias por tu mensaje, te responderemos pronto. ✅"
    )

# Función principal
async def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Agregar handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin))

    # Mensaje de confirmación
    print("👨‍💻 Bot iniciado y funcionando correctamente ✅")

    # Ejecutar el bot
    await application.run_polling()

# Ejecutar
if __name__ == '__main__':
    nest_asyncio.apply()
    asyncio.run(main())
