from pyrogram import Client

from config import (API_HASH, API_ID, BOT_TOKEN, STRING1)

app = Client(
    "YukkiMusicBot",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

ASS_CLI_1 = Client(STRING1, API_ID, API_HASH)

