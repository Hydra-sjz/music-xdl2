import os
from os import getenv
from dotenv import load_dotenv
from os import environ

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5203326675:AAFDyhD-bYzr2vBfgydGNVJoAunbrbNcfQE")
API_ID = int(os.environ.get("API_ID", "11984338"))
API_HASH = os.environ.get("API_HASH", "ea4cb0f090d7366f7e4ab9dfc116acc7")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "784589736").split()))

LOG_GROUP = environ.get("LOG_GROUP")
if LOG_GROUP:
    LOG_GROUP = int(LOG_GROUP)

#Port
PORT = os.environ.get("PORT", "8080")
