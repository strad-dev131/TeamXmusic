from TeamX.core.bot import TeamX
from TeamX.core.dir import dirr
from TeamX.core.git import git
from TeamX.core.userbot import Userbot
from TeamX.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = TeamX()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
