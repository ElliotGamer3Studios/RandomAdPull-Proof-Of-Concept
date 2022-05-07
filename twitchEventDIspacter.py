#IDK if this even works (prob not) and I have no good way to test it _/('-')\_
from twitchAPI.pubsub import PubSub
from twitchAPI.types import Twitch
from twitchAPI.types import AuthScope
import auth as auth
import randomAdPull as randomAdPull

twitch = Twitch(auth.app_id, auth.app_secret)
twitch.authenticate_app([])
twitch.set_user_authentication(auth.user_auth_token, [AuthScope.CHANNEL_READ_REDEMPTIONS], auth.user_auth_refresh_token)

pubsub = PubSub(twitch)
pubsub.start()
uuid = pubsub.listen_channel_points(auth.channel_id, randomAdPull.randomAdURL()) #call the random ad event
