import os
import logging
from twitchio.ext import commands

class games(commands.Cog):
    """
    Goal is to implement some sort of collecting game.
    Collected items can be used to battle other players.
    Rarer items give higher chance of winning
    Starter element decides your affinity. 
    Affinity decides which items are stronger for you.
    Starter elements:
        - Fire (0)
        - Water (1)
        - Wind (2)
        - Earth (3)
    Starter items:
        - None
    Starter spells:
        - Elemental
    Items:
        - Axe
        - Knife
        - Sword
        - Bow
        - Blowpipe
        - Throwing knife
        - Wand
        - Armor
            - Ranged
            - Melee
            - Magic
        - ...
    
    How to get items:
        - Daily roll when online
        - Subscribing (should have highest prio as it promotes longevity)
        - Gifting subs
        - Donating bits
        - Donating (should have second highest prio as you keep more money)

    """
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.games_logger = logging.getLogger('RoBoPug.games')
    
    @commands.command()
    async def play(self, ctx: commands.Context):
        await ctx.send(f"Not implemented yet.")
    
    
    


def prepare(bot: commands.Bot):
    bot.add_cog(games(bot))