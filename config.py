import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = 26692918
API_HASH = "2b239375e141e882a33b59820ce827be"
# ------------------------------------------------------
BOT_TOKEN = "6789724300:AAHWTREMKE-Y-52iVx-9YsMMgutQpS9kyoU"
# -------------------------------------------------------
OWNER_USERNAME = "alone_x_moder"
# --------------------------------------------------------
BOT_USERNAME = "Hinata_X_Music_robot"
# --------------------------------------------------------
BOT_NAME = "HINATA"
# ---------------------------------------------------------
ASSUSERNAME = "Naruto_X_Hinata"
# ---------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ishu9805/tanjiromusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
) 
# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = getenv("SERVER_PLAYLIST_LIMIT", "3000")

#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = "mongodb+srv://babusona:hinatababy@cluster0.t0lfelh.mongodb.net/"
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = getenv("DURATION_LIMIT", 16000)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = -1001975521991
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = 7378476666
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------

#-----------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = "https://t.me/blade_x_community"
SUPPORT_CHAT = "https://t.me/blade_x_support"
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "60"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 250))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = "BQGtHS0Aqef1ZiRD-DCnf_L3LU-Jzju0IaYfixtuqjOLWMNe2wJZOa4HV2HKHcQjJrQ6JBe0FYZtbGG5S7EQ5oCVwcF5OhFtgn8axRg3vR-XnfmC5c9AR7SFohUQotl3hY4LV9hFQY4b3Zfq8XGNQ8Mx3jv8uzxyNYLQlCi6yT7WzjKlAhZ0XqbqmA63eMsHbTBTplzF7miaO-5s1LKmnZ7pqRqBdnzUuvbuQW2dHObHM7onYcqvi_GzzL_1vbIt4Ty4tbjG1itg0vSkit5Y5xtQTpTPYkJsd2jXEZyzfuJXWnK0HUCF5swZpoAonCvcqDRYZuIBHFI7X6bIaZuzxLH9ov8GhgAAAAGtITP-AA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/cfbdee8103102bcb2e5da.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/00360393a15daf7fc4e9d.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
STATS_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/48f39202823b358203234.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e575ae40d6635250974e1.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
