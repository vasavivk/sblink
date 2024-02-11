 
import sys
from os import environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = 23028247
    API_HASH = "659c5f1124a81ad789a6ea021da73f4d"
    BOT_TOKEN = "6810418594:AAFKZkzxQ9YkP3By6jdzu8m-Dhimiu0im0c"
    SLEEP_THRESHOLD = 20  # 1 minte
    WORKERS = 60  # 6 workers = 6 commands at once
    BIN_CHANNEL = "-1002105902998"  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    PORT = 8080
    BIND_ADDRESS = "0.0.0.0"
    PING_INTERVAL = 1200
    HAS_SSL = "y"
    NO_PORT = "y"
    HASH_LENGTH = 6
    FQDN ="https://streamlintgweb-cdd83d7eb771.herokuapp.com"
    URL = "http{}://{}{}/".format(
            "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
        )
    KEEP_ALIVE = 'true'
    DEBUG = "true"
    USE_SESSION_FILE = 'true'
    ALLOWED_USERS = []
