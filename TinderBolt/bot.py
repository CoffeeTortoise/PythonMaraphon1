from telegram.ext import ApplicationBuilder, MessageHandler, filters
from telegram.ext import CallbackQueryHandler, CommandHandler

# тут будем писать наш код :)

from constants import Constants
import handlers as hs
import button_handler as bh
import command_handler as ch


def main() -> None:
    Constants.DIALOG.mode = None
    Constants.DIALOG.list = []
    Constants.DIALOG.count = 0
    Constants.DIALOG.user = {}

    app = ApplicationBuilder().token(Constants.TOKEN).build()
    app.add_handler(CommandHandler('start', ch.start))
    app.add_handler(CommandHandler('gpt', ch.gpt))
    app.add_handler(CommandHandler('date', ch.date))
    app.add_handler(CommandHandler('message', ch.message))
    app.add_handler(CommandHandler('profile', ch.profile))
    app.add_handler(CommandHandler('opener', ch.opener))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hs.greetings))
    app.add_handler(CallbackQueryHandler(bh.date_button, pattern='^date_.*'))
    app.add_handler(CallbackQueryHandler(bh.message_button, pattern='^message_.*'))
    app.add_handler(CallbackQueryHandler(bh.hello_button))
    app.run_polling()


if __name__ == '__main__':
    # https://t.me/CoffeeTortoiseAwesome_bot
    main()
