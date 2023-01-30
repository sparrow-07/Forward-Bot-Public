import os

class Config(object):
    
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6071709130:AAFlW_BU95LoTxXtiHLDhsNg0zwhOzkCjwM")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", "24198383"))
    API_HASH = os.environ.get("API_HASH", "819a631e42b840a60ac6f923e1290bce")
    AUTH_USERS = os.environ.get("OWNER", "5757479875")
