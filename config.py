import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5988361578:AAHukwb3OyI0BDGmkyVGszSbBSKjEnZUQbo")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", "24281454"))
    API_HASH = os.environ.get("API_HASH", "dbe4521b4291da85becb65c7d4d4c36c")
    AUTH_USERS = os.environ.get("OWNER", "5650200786")
