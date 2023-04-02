from django.core.management.base import BaseCommand
from tl_bot.telegram_bot import start_bot


class Command(BaseCommand):
    help = 'Runs telegram bot'

    def handle(self, *args, **kwargs):
        print('going to start...')
        start_bot()
        print('started...')
