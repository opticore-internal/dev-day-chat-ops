# Developer Guide: Creating a Telegram Bot

Welcome to Development Day at Opticore! Today, we will explore how to build a simple Telegram bot. The techniques discussed can be extended to develop chat operations on other platforms as well.

This guide assumes that you have Python and pip installed on your system, and that you have a mobile device with Telegram installed.

## Installation

1) First, install virtualenv if it's not already installed:

    ``` bash
    pip install virtualenv
    ```

    Create a virtual environment named venv:

    ``` bash
    python -m venv venv
    ```

2) Enable virtual environment:

    ``` bash
    source ./venv/bin/activate
    ```

3) Install python dependancies:

    ``` bash
    pip install -r requirements.txt
    ```

## Development

### Stage 1-2: Setting up Click

Click is a Python library for creating command-line interfaces. It simplifies entry point creation for your applications, utilizing decorators to convert ordinary Python functions into CLI commands.

### Stage 3: Creating the Basic Bot

Start a new chat with the BotFather on your Telegram app to create a new bot:

1) Send `/newbot` to BotFather.
2) Follow the prompts to set your bot’s name and username.
3) BotFather will provide an HTTP API token upon completion.

Set the bot and API environment variables:

``` bash
export BOT_TOKEN=[Your_Telegram_Bot_Token]
export WEATHER_API_KEY=[Your_Weather_API_Token]
```

### Stage 4: Implementing the Python Poller

With the bot token, initialize your bot using the Python Telegram Bot library. Create a Telegram Application and add command handlers. Ensure functions handling these commands are asynchronous to manage multiple requests simultaneously:

``` python
async def command_handler_function():
    # Implementation goes here
```

### Stage 5: Adding Weather Query Functionality

Add a function to query weather information. Start with a simple command to fetch weather for a predetermined location like London. Later, enhance it to accept any location as a command argument.

### Stage 6: Customizing Commands

Enable the weather command to accept location input from the user. Modify the existing function to parse this input and fetch weather accordingly.

### Stage 7: Implementing Error Handling

Improve user experience by adding error handling. Use try-except blocks to manage errors gracefully, such as when a user forgets to include necessary command arguments.
