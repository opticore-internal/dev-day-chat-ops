import os
import click
import requests
from telegram.ext import Application, CommandHandler


BOT_TOKEN = os.getenv("BOT_TOKEN", None)
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", None)

if BOT_TOKEN is None:
    print("Please set the BOT_TOKEN environment variable")
    exit(1)
if WEATHER_API_KEY is None:
    print("Please set the WEATHER_API_KEY environment variable")
    exit(1)


def get_weather(location):
    url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}&apikey={WEATHER_API_KEY}"
    response = requests.get(url)
    return response.json()


async def send_weather(update, context):
    location = context.args[0]
    weather = get_weather(location)
    message = f"""
{location}
--------------------------------
Temperature: {weather['data']['values']['temperature']}
Humidity: {weather['data']['values']['humidity']}
Wind Speed: {weather['data']['values']['windSpeed']}
"""
    await update.message.reply_text(message)


async def start(update, context):
    await update.message.reply_text("Hello World!")


@click.command()
def main():
    print("Starting telegram poller...")
    application = Application.builder().token(BOT_TOKEN).build()
    start_handler = CommandHandler("start", start)
    weather_handler = CommandHandler("weather", send_weather)
    application.add_handler(start_handler)
    application.add_handler(weather_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
