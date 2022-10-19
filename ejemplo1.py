
import logging,requests
from requests import status_codes
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


#docu de los replies https://core.telegram.org/bots/update56kabdkb12ibuisabdubodbasbdaosd#:~:text=Formatting%20options,-The%20Bot%20API&text=You%20can%20use%20bold%2C%20italic,style%20or%20HTML%2Dstyle%20formatting.
def hola(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hellooooo {user.mention_markdown_v2()}\!',
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
    update.message.reply_text('Mira, así está la cosa: ')
    update.message.reply_text('Puedes mandar: /hola para que te salude')
    update.message.reply_text('/coahuila para mandarte algo muy coahuilense')
    update.message.reply_text('/api para hacer health check del API httpbin')
    update.message.reply_text('/chuck para obtener un chiste random de chuck norris')
    update.message.reply_text('/patito para obtener un patito random')


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

def geolocate(user_input):
    answer = "me dijistes :  " + user_input
    return answer
    r = requests.get('https://api.chucknorris.io/jokes/random')
    chiste=r.json()
    print(chiste['value'])
    update.message.reply_text('Un chistin del chuck norris en inglés: ')
    update.message.reply_text(chiste['value'])

def ip_check(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Por favor escribe una ip a geolocalizar ')
    user_input = update.message.text
    update.message.reply_text(geolocate(user_input))


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5681615186:AAHgK6j8FPYes1omN39UmCkMiK85VKcBc1Y")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("hola", hola))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("coahuila", coahuila))
    dispatcher.add_handler(CommandHandler("api", test_apiconnection))
    dispatcher.add_handler(CommandHandler("chuck", chuck_norris))
    dispatcher.add_handler(CommandHandler("patito", patito))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
