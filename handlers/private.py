from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
𝐀 𝐏𝐨𝐰𝐞𝐫𝐟𝐮𝐥, 𝐒𝐦𝐚𝐫𝐭 🎵 𝐆𝐫𝐨𝐮𝐩 𝐌𝐮𝐬𝐢𝐜 𝐏𝐥𝐚𝐲𝐞𝐫
✌️Maded By 💞 [🅺🅰︎🅽🅽🆄](https://t.me/XD_dead_killer) 🔥━━━━━━━━━━━━━━━━━**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰𝗢𝘄𝗻𝗲𝗿❱", url="https://t.me/XD_dead_killer")
                  ],[
                    InlineKeyboardButton(
                        "❰𝗦𝘂𝗽𝗽𝗼𝗿𝘁❱", url="https://t.me/kannu_op"
                    ),
                    InlineKeyboardButton(
                        "❰𝗚𝗿𝗼𝘂𝗽❱", url="https://t.me/world_friendship_love_chat"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❰𝗦𝗼𝘂𝗿𝗰𝗲❱", url="https://github.com/devellyf/xdkillermusic"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("hexor") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁 𝗢𝗻𝗹𝗶𝗻𝗲 𝗡𝗼𝘄\n🌠𝗛𝗲𝘅𝗼𝗿 𝗫𝗗 <3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌼𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/Prayagraj_Op")
                ]
            ]
        )
   )
