import re, os, time
import datetime


id_pattern = re.compile(r'^.\d+$') 


class Config:

    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    SESSION_NAME = ":memory:"

    api_id_str = os.environ.get("9472424")
    API_ID = int(api_id_str) if api_id_str is not None else 0  # Replace 0 with a suitable default value


    API_HASH = os.environ.get("API_HASH")

    CLIENT_ID = os.environ.get("CLIENT_ID")

    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

    BOT_OWNER = int(os.environ.get("BOT_OWNER"))

    BOT_START_TIME = time.time()
    
    BOT_START_DATETIME = datetime.datetime.now().strftime("%B %d, %Y %I:%M:%S %p")

    DB_NAME = os.environ.get("DB_NAME", "Utubeitbot")  

    DB_URL = os.environ.get("DB_URL")

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
