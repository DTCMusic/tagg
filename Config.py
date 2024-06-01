import os


class Config():
    # Bu dəyərləri my.telegram.org saytından əldə edin
    #>>> https://my.telegram.org
    API_ID = int(os.environ.get("API_ID","16089646"))
    API_HASH = os.environ.get("API_HASH","7ce9ffba92ce7e56ca7d5e6f73201002")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","7493261373:AAFwQVBj3IOu557mqGFNnOrcG3YnnNOxsCA:")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","NezrinChatRobot")
    BOT_NAME = os.environ.get("BOT_NAME","nezrin")
    BOT_ID = int(os.environ.get("BOT_ID","7493261373"))
    SUDO_USERS = os.environ.get("SUDO_USERS","thagiyev").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT","ioj")
    OWNER_ID = int(os.environ.get("OWNER_ID","6634423600"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME","uijio;kl,")
