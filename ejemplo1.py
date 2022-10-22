'''
Updater is a class whose responsibility it is to fetch updates from Telegram, either via get_updates or via a webhook
Dispatcher is a class whose responsibility it is to do something with the updates. This is done through the Handlers as explained in the docs of Dispatcher.add_handler. It also manages in-memory dictionaries that can be used to store bot/chat/user related data
CallbackContext is a convenience class used in the PTB framework to provide access to commonly used objects into your handler callbacks. For each update one instance of this class is built by the Dispatcher and passed to the handler callbacks as second argument.
'''

import logging,requests,os,dotenv
from requests import status_codes
from telegram import Update, ForceReply,Bot
from telegram.ext.dispatcher import run_async
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CommandHandler,ContextTypes,MessageHandler,filters
# Update es el contenido del mensaje que mandó la persona que interactúa con el bot
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def hola(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hola hola {user.mention_markdown_v2()}\!',
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
    update.message.reply_text('Este es el único museo chido de Saltillo https://g.page/museodeldesierto?share')

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Ve al botón que está arriba de tu teclado, ese menú te dirá lo que puedo hacer :) ')


def test_apiconnection(update: Update, context: CallbackContext) -> None:
    r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    print(r.status_code) #Para confirmar en la consola
    respuesta=status_codes._codes[r.status_code][0]
    print(respuesta)
    update.message.reply_text('API funcionando, código  ' + str(r.status_code) + ' que significa: '+ respuesta)

def chuck_norris(update: Update, context: CallbackContext) -> None:
    r = requests.get('https://api.chucknorris.io/jokes/random')
    chiste=r.json()
    print(chiste['value'])
    update.message.reply_text('Un chistin del chuck norris en inglés: ')
    update.message.reply_text(chiste['value'])

def patito(update: Update, context: CallbackContext) -> None:
    r = requests.get('https://random-d.uk/api/v2/random')
    img=r.json()
    update.message.reply_text(img['url'])

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def ip_menu(update: Update, context: CallbackContext,dispatcher) -> None:
    update.message.reply_text('Entraste al menú de la ip ')
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, ip_mensaje))

def ip_mensaje(update: Update, context: CallbackContext,dispatcher) -> None:
    ip_usuario=update.message.text
    update.message.reply_text('Enviaste la ip: ' + ip_usuario)

def main() -> None:
    dotenv.load_dotenv()
    mybot_token=os.getenv("BOT_TOKEN")
    # Create the Updater and pass it your bot's token.
    updater = Updater(mybot_token)

    #siempre definir al bot como dispatcher.updater
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("hola", hola))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("coahuila", coahuila))
    dispatcher.add_handler(CommandHandler("api", test_apiconnection))
    dispatcher.add_handler(CommandHandler("chuck", chuck_norris))
    dispatcher.add_handler(CommandHandler("patito", patito))
    dispatcher.add_handler(CommandHandler("ip", ip_menu))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
