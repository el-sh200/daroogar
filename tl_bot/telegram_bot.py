import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from customer.models import Customer

API_KEY = '6203495338:AAHrYQ1R3_1P97z47v58f5VMDi4OCxwTVNk'


def start_command(update, context):
    update.message.reply_text('Hello  :)')


def help_command(update, context):
    update.message.reply_text('help  :)')


def custom_command(update, context):
    update.message.reply_text('custom  :)')


def send_file(update, context):
    update.message.reply_text('sending you a file...  :)')
    file_path = 'logo.png'
    with open(file_path, 'rb') as f:
        context.bot.send_document(chat_id=update.effective_chat.id, document=f)


# def last_prescription(update, context):
#     update.message.reply_text('Here is your last prescription')
#     chat_id = update.message.chat_id
#     # Prompt the user to share their phone number
#     phone_keyboard = [[telegram.KeyboardButton(text="Share my phone number", request_contact=True)]]
#     reply_markup = telegram.ReplyKeyboardMarkup(keyboard=phone_keyboard, one_time_keyboard=True)
#     bot.send_message(chat_id=chat_id, text="Please share your phone number", reply_markup=reply_markup)
#     counter = 53
#
#     file_path = f'media/prescription/pre-{counter}.pdf'
#     with open(file_path, 'rb') as f:
#         context.bot.send_document(chat_id=update.effective_chat.id, document=f)

def last_prescription(update, context):
    chat_id = update.message.chat_id
    # Prompt the user to share their phone number
    phone_keyboard = [[telegram.KeyboardButton(text="Share my phone number", request_contact=True)]]
    reply_markup = telegram.ReplyKeyboardMarkup(keyboard=phone_keyboard, one_time_keyboard=True)
    context.bot.send_message(chat_id=chat_id, text="Please share your phone number", reply_markup=reply_markup)

    def handle_contact(update, context):
        # Check if the user shared their phone number
        if update.message.contact:
            phone_number = update.message.contact.phone_number
            # Check if the phone number is in the database
            cus = Customer.objects.filter(mobile_number=phone_number)
            if cus.exists():
                print(cus.first())
                customer = cus.first()
                last_pr = customer.prescription_set.last()
                # Send the file to the user
                update.message.reply_text('Here is your last prescription')
                counter = last_pr.pk
                file_path = f'media/prescription/pre-{counter}.pdf'
                with open(file_path, 'rb') as f:
                    context.bot.send_document(chat_id=update.effective_chat.id, document=f)
            else:
                # Send an error message to the user
                update.message.reply_text("Your phone number was not found in the database. Please try again.")
        else:
            # Send an error message to the user
            update.message.reply_text("You did not share your phone number. Please try again.")
        # Remove the handler for contact updates
        dp.remove_handler(contact_handler)

    # Add a handler for contact updates
    contact_handler = MessageHandler(Filters.contact, handle_contact)
    dp.add_handler(contact_handler)


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
    global dp
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))
    dp.add_handler(CommandHandler('sendfile', send_file))
    dp.add_handler(CommandHandler('last', last_prescription))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Errors
    dp.add_error_handler(error)

    # Run Bot
    print('before ')
    updater.start_polling()

    updater.idle()
    print('after')
