import os
from dotenv import load_dotenv
from disc.bot import bot

# load env
load_dotenv()

# start the app
if __name__ == '__main__':
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))

