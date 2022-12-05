import os
from os import getenv
from dotenv import load_dotenv
from os import environ

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "784589736").split()))

LOG_GROUP = environ.get("LOG_GROUP", "-1001630162995")
if LOG_GROUP:
    LOG_GROUP = int(LOG_GROUP)
