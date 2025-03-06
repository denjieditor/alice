import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 26179888
API_HASH = "b63b1c69cf3bcd032d4a2463cc84be2e"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7725357171:AAGxs9GpcLMsenkVecnzNZQBNhfHSOho2q8"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://denji:@denji.0qi3h.mongodb.net/?retryWrites=true&w=majority&appName=denji
"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002242379033

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 5478596071

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("lonelyxmusic")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-874144d7-f3e6-40a9-84ad-2e73fc39a3d7")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/animeclanzero2"
SUPPORT_GROUP = "https://t.me/animeclanzero2"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", bcfe26b0ebc3428882a0b5fb3e872473)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", 907c6a054c214005aeae1fd752273cc4)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQGPeTAAfVI4O9jYTkpHhS3g-OrPG-RGuJM95iPyG2Gf4iHprcksu3PLIYtgurC4FMLGdpRGJXCCVQbKwzMf1-pCSY2IQkJcolglruISD4_lhGLh6Ajx0Lt1YQaxImGATK8nceV3-Lpkg9SBZ8IvCUdToUjjj28os6Za363eNqtvRcqSYufvzMHM5_u8UPzrfM9IDdKnLt5-oagGF5LlE201pPBsAU9pT092OIatvTVfZiSZEXPmQBWbj511LRYTfDHC28OkS3QKieNXm_TYEPrZeTaP8C7CpNSCjFQp-wlTBkjuU80tQ442_85bZbzg8FaNnma4Sjp_qjuMhPTwamtlb7vnggAAAAHMd5hzAQ"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/f586172fe40a0b5d0b0df.jpg"

PING_IMG_URL = "https://graph.org/file/f586172fe40a0b5d0b0df.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/763a841a2ad5cbb1e2fc5.jpg"
STATS_IMG_URL = "https://graph.org/file/f586172fe40a0b5d0b0df.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("https://t.me/animeclanzero2")
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("https://t.me/animeclanzero2")
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
