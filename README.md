# Glossary-bot for Discord
This is the glossary bot, to help you to have a glossary on your prefered discord server.


A complete and shameless ripoff of the officially unofficial Pimoroni Discord bot!

Feel free to mess around with the code and make improvements where you
can!


# Install

Make sure you have python 3.6 or more recent and virtualenv installed on your system then:

Then run under linux:

```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

from the root of the repository to install glo and all dependencies.

Then each time you open a new terminal, don't forget to re-run `. venv/bin/activate`

# Running
In order to run this bot for yourself, you need:
- A Discord server within which you have permission to add a bot.
- A bot application, which can be created here:
    https://discordapp.com/developers/applications/me
- A bot token.
- A bot client ID.

In order to add the bot to a server, simply navigate to
    https://discordapp.com/api/oauth2/authorize?client_id=[CLIENT ID]&scope=bot&permissions=0, replacing [CLIENT ID] with your bot's client ID.

The bot token may be specified on the command line or placed in the
environment variable `DISCORD_BOT_TOKEN`.

To use all the features you also need some other API credentials. Note:
environment variables use the config file syntax, not the command line
syntax. See glossarybot.conf.example.
