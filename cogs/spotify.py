import os
import spotipy
import logging
from twitchio.ext import commands

import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials



class spotify(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.username = os.environ['SPOTIPY_USER_NAME']
        self.scope = "user-read-playback-state user-modify-playback-state"
        self.token = util.prompt_for_user_token(self.username, self.scope, os.environ['SPOTIPY_CLIENT_ID'], os.environ['SPOTIPY_CLIENT_SECRET'], os.environ['SPOTIPY_REDIRECT_URI'])
        self.spotify = spotipy.Spotify(auth=self.token)
        self.spotify_logger = logging.getLogger('RoBoPug.spotify')
    
    @commands.command(aliases=['sr'])
    async def songrequest(self, ctx: commands.Context, *, uri):
        """Adds a song to the back of the queue"""
        try:
            song_info = self.spotify.add_to_queue(uri)
            await ctx.send(f"Added song to queue.")
        except Exception as e:
            await ctx.send(f"Something went wrong, make sure you use a spotify uri, id or url.")
            self.spotify_logger.error(e)
    
    
    @commands.command(aliases=['song', 'np'])
    async def nowplaying(self, ctx: commands.Context):
        """Displays the currently playing song (spotify)"""
        try:
            song_info = self.spotify.currently_playing()
            if song_info is not None:
                song_name = song_info['item']['name']
                song_artist = song_info['item']['artists'][0]['name']
                await ctx.send(f"Currently playing: {song_name} by {song_artist}.")
            else:
                await ctx.send(f"Currently not playing a spotify song.")
        except Exception as e:
            self.spotify_logger.error(e)
    

def prepare(bot: commands.Bot):
    bot.add_cog(spotify(bot))