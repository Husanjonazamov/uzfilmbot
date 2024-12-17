MAIN_MENU = \
"""
<b>Asosiy menyu</b>
"""

START_USER = \
"""
<b>
👋 Assalomu alaykum. Botimizga xush kelibsiz.

✍🏻 Kino kodini yuboring.
</b>
"""

DOWNLOAD_MOVIES_HANDLER = \
"""
<b>
✍🏻 kino kodini yuboring!
</b>
"""

CHANNEL_REQUEST = \
"""
<b>
Iltimos, quyidagi kanallarga obuna bo'ling 👇
</b>
"""

CHANNEL_CHECK = \
"""
<b>
👋 Assalomu alaykum. Botimizga xush kelibsiz.

✍🏻 Kino kodini yuboring.
</b>
"""

CHANNEL_ERROR = \
"""
<b>
❌ Siz hali hamma kanallarga obuna bo'lmadingiz. Iltimos, quyidagi kanallarga obuna bo'ling
</b>
"""

KOD_IS_NOT = \
"""
<b>
❌ Siz mavjud bo'lmagan kodni yubordingiz!
</b>
"""


NO_EPISODES_FOUND = \
"""
kod
"""

def MOVIES_SEND(**kwargs):
    movies_send = ""

    movies_send += f"<b>🎬 Nomi: #{kwargs['title']}</b>\n\n"
    movies_send += f"<b>📅 Yili: {kwargs['year']}</b>\n"
    movies_send += f"<b>🌐 Tili: {kwargs['language']}</b>\n"
    movies_send += f"<b>📀 sifati: {kwargs['quality']}</b>\n"
    movies_send += f"<b>🏳️ Davlati: {kwargs['country']}</b>\n"
    movies_send += f"<b>🎭 Janri: {kwargs['genre']}</b>\n"
    movies_send += f"<b>📥 Yuklash: <a href='https://t.me/TVkino_uzbot'>{kwargs['download_count']}</a></b>\n\n"
    movies_send += f"<b>🤖 Bizning bot:  <code>@UzFilm_robot</code></b>\n"

    return movies_send


def TREYLER_SEND(**kwargs):
    treyler_send = "🥳 Bizda yangi premyera\n\n"

    treyler_send += f"<b>🔢 Kodi: <code>{kwargs['code']}</code></b>\n\n"
    treyler_send += f"<b>{kwargs['description']}</b>\n\n"
    treyler_send += f"<b>🤖 Bizning bot:  <code>@UzFilm_robot</code></b>\n"

    return treyler_send



def MOVIES_LIST_SEND(title, code):
    return f"<b>🎬 [{title}] -- kod: ({code})</b>\n\n"


def EPISODE(**kwargs):
    episode_send = ""

    episode_send += f"<b>🎬 Nomi: #{kwargs['episode_title']} {kwargs['episode_number']}-qism</b>\n\n"
    episode_send += f"<b>📅 Yili: {kwargs['episode_year']}</b>\n"
    episode_send += f"<b>🌐 Tili: {kwargs['episode_language']}</b>\n"
    episode_send += f"<b>📀 sifati: {kwargs['episode_quality']}</b>\n"
    episode_send += f"<b>🏳️ Davlati: {kwargs['episode_country']}</b>\n"
    episode_send += f"<b>🎭 Janri: {kwargs['episode_genre']}</b>\n"
    episode_send += f"<b>📥 Yuklash: <a href='https://t.me/TVkino_uzbot'>{kwargs['episode_download_count']}</a></b>\n\n"
    episode_send += f"<b>🤖 Bizning bot:  <code>@UzFilm_robot</code></b>\n"

    return episode_send



def get_response(**kwargs):
    response = ''
    
    response += f"<b>{kwargs['title']} Kategoriyani tanlang:</b>\n\n"
    response += f"{kwargs['index']}. {kwargs['title']} ({kwargs['year']}) - kod: {kwargs['code']}\n\n"

    return response




MOVIES_SEARCH = \
"""
<b>
✍🏻 Iltimos, qidiruv so'rovini kiriting:
</b>
"""

SEARCH_NOT_FOUND = \
"""
<b>
Afsuski hech narsa topilmadi 😔
</b>
"""

CATEGORY_SELECT = \
"""
<b>Kategoriyani tanlang:</b>
"""

CATEGORY_ERROR = \
"""
<b>Kategoriyalar topilmadi.</b>
"""

CATEGORY_MOVIES = \
"""
<b>kategoriyasidagi filmlar:</b>
"""



CATEGORY_NOT_MOVIES  = \
"""
<b>Afsuski! filmlar topilmadi. 😔</b>
"""

NOT_ADMIN = \
"""
<b>Siz admin emasiz !</b>
"""

TREYLER_SUCCES = \
"""
<b>Treylerni tanlang</b>
"""

TREYLER_NOT_FOUND = \
"""
<b>Treyler topilmadi</b>
"""


NO_SEASON_SELECTED = \
"""
Serial uchun fasl topilmadi
"""


# movies not fount

MOVIE_NOT_FOUND = \
"""
Kechirasiz, lekin hozircha bu mavsum uchun film topa olmadik.
"""