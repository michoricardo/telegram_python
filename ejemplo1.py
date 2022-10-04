
import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


#docu de los replies https://core.telegram.org/bots/update56kabdkb12ibuisabdubodbasbdaosd#:~:text=Formatting%20options,-The%20Bot%20API&text=You%20can%20use%20bold%2C%20italic,style%20or%20HTML%2Dstyle%20formatting.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Que rollo perroooo {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

def coahuila(update: Update, context: CallbackContext) -> None:
    """te manda un video de gatitos"""
    update.message.reply_text(' Bienvenido a Coahuila https://youtu.be/PbYU8fB8S5E')
    #update.message.reply_text('\U0001F534')U+1F618
    update.message.reply_text('\N{Sauropod}')
    update.message.reply_html(
        '<strong>buenas noshes :)  </strong>',
        reply_markup=ForceReply(selective=True),
    )

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("prohibidooooo")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("coahuila", coahuila))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()