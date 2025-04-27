import asyncio
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Configurar logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Tu token de bot
TOKEN = '7341867073:AAFXGCGVlRnek8cirp1137Xbdh2IXvhVDfQ'  # ← Asegúrate de poner tu token real aquí

# Funciones que maneja los comandos y mensajes
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('¡Hola! Soy tu bot 🛠️')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Dijiste: {update.message.text}")

# Función principal
async def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Agregar handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Mensaje de confirmación
    print("🧑‍💻 Bot iniciado y funcionando correctamente ✅")

    # Ejecutar el bot
    await application.run_polling()

# Ejecutar
if __name__ == '__main__':
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
