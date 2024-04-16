# Dev Day 1 - Chat Ops

Welcome to the new Development day at Opticore. We will be looking over how to build a simple telegram bot. The methodologies used here, can be used to create mode chatops in other platforms.

This guide assumes you already have python and pip installed on your system, and you have access to a mobile device with Telegram installed.

## Installation

1) Create virtual environment

    ``` bash
    pip install virtualenv
    ```

    ``` bash
    # Creates virtual environment called `venv`
    python -m venv venv
    ```

2) Enable virtual environment

    ``` bash
    source ./venv/bin/activate
    ```

3) Install python dependancies

    ``` bash
    pip install -r requirements.txt
    ```

## Development

### Setting up Click (Stage 1 - 2)

Click is a python module for creating entrypoints into your application. Click allows you to define functions that can be used from the command line. This is a package built on top of python argparse.

### Creating Basic Bot

On your mobile device you will need to start a new chat with the `BotFather` (a telegram bot for creating new bots).

In the chat you will need to type `/newbot`, this will start the process for creating a telegram bot.

The bot will now prompt you for information, name and username. The bot will then respond with a HTTP API key. You then need to set your environment variables with the key.

``` bash
export BOT_TOKEN=[telegram token]
export WEATHER_API_KEY=[weather token]
```

### Creating Python Poller (Stage 3)

Using the token from the previous setup you are now ready to create the python poller. Using the telegram python module, using the Application import to create a telegram application. Commands can then be added to the application through the use of the `CommandHandler`.

Functions that are used for handlers need to be asynconous to allow multiple requests at the same time. This is done through the `async` keyword before defining your function.

### Adding More Useful Information


curl --request GET --url 'https://api.tomorrow.io/v4/weather/realtime?location=toronto&apikey=iFP2iLeFzokjGvhgfpgr0M5oEyMsFVHw' --header 'accept: application/json'