import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

API_KEY = '6203495338:AAHrYQ1R3_1P97z47v58f5VMDi4OCxwTVNk'


def start_command(update, context):
    update.message.reply_text('Hello  :)')


def help_command(update, context):
    update.message.reply_text('help  :)')


def custom_command(update, context):
    update.message.reply_text('custom  :)')


def send_file(update, context):
    update.message.reply_text('sending you a file...  :)')
    file_path = '../t.txt'
    with open(file_path, 'rb') as f:
        context.bot.send_document(chat_id=update.effective_chat.id, document=f)


def handle_response(text: str) -> str:
    if 'hello' in text:
        return 'Hello to You'
    return 'Idk'


def handle_message(update, context):
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    print(f"User ({update.message.chat.id}) says: '{text}' in {message_type}")

    if message_type == 'group':
        if '@daroogar' in text:
            new_text = text.replace('@daroogar', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)
    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def start_bot():
    print('starting...')
    updater = Updater(API_KEY, use_context=True)
    print('after updater')
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))
    dp.add_handler(CommandHandler('sendfile', send_file))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Errors
    dp.add_error_handler(error)

    # Run Bot
    print('before ')
    updater.start_polling()

    updater.idle()