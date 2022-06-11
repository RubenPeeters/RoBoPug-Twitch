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
        self.spotify_logger = logging.getLogger('rbotp.spotify')
    
    @commands.command(aliases=['songrequest'])
    async def sr(self, ctx: commands.Context, *, uri):
        """Adds a song to the back of the queue"""
        try:
            song_info = self.spotify.add_to_queue(uri)
            self.spotify_logger.info(f"Added song to queue!")
            await ctx.send(f"Added song to queue!")
        except Exception as e:
            await ctx.send(f"Something went wrong, make sure you use a spotify uri, id or url.")
            self.spotify_logger.error(e)
    
    
    @commands.command()
    async def nowplaying(self, ctx: commands.Context):
        """Displays the currently playing song (spotify)"""
        try:
            song_info = self.spotify.currently_playing()
            song_name = song_info['item']['name']
            song_artist = song_info['item']['artists'][0]['name']
            self.spotify_logger.info(f"Currently playing: {song_name} by {song_artist}!")
            await ctx.send(f"Currently playing: {song_name} by {song_artist}!")
        except Exception as e:
            self.spotify_logger.error(e)
    

    


def prepare(bot: commands.Bot):
    bot.add_cog(spotify(bot))