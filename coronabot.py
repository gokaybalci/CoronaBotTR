import logging
import handlers

from telegram.ext import Updater
from telegram.ext import CommandHandler

# Create an updater
updater = Updater(token='TOKEN HERE', use_context=True)

# Expose the dispatcher locally
dispatcher = updater.dispatcher

# Configure warning level logging.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.WARNING)

# Create a list of all handlers
handlers = {
    "giris": handlers.giris_handler,
    "yardim" : handlers.yardim_handler,
    "vaka" : handlers.vaka_handler,
    "iyilesen" : handlers.iyilesen_handler,
    "olum" : handlers.olum_handler,
    "rakam": handlers.rakam_handler
}

# Add all handlers to the dispatcher
for handler_name in handlers:
    dispatcher.add_handler(CommandHandler(handler_name, handlers[handler_name]))

# Start the bot
updater.start_polling()
