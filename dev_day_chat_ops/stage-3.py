import os
import click
from telegram.ext import Application, CommandHandler


BOT_TOKEN = os.getenv('BOT_TOKEN', "")

async def test(update, context):
    await update.message.reply_text('Hello World!')


@click.command()
def main():
    print("Starting telegram poller...")
    application = Application.builder().token(BOT_TOKEN).build()
    test_handler = CommandHandler('test', test)
    application.add_handler(test_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
