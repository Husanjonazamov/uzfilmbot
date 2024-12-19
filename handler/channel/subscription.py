from aiogram.types import ChatMemberStatus
from aiogram.utils.exceptions import BadRequest

CHANNELS = {
    'channel_1': 'sstesssas',
}



async def check_subscriptions(bot, user_id):

    """
    kannallarni button ko'rinishida foydalanuvchiga yuborish
    """

    not_subscribed = []
    for channel in CHANNELS.values():
        try:
            chat_member = await bot.get_chat_member(f"@{channel}", user_id)
            if chat_member.status not in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR]:
                not_subscribed.append(channel)
        except BadRequest:
            not_subscribed.append(channel)
    return not_subscribed