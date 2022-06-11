import os
import logging
from twitchio.ext import commands



class basic(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.basic_logger = logging.getLogger('rbotp.basic')


    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f"Hello, {ctx.author.name}!")

    @commands.Cog.event()
    async def event_message(self, message):
        if message.echo:
            return
        # print(message.content)

    @commands.command()
    async def botuptime(self, ctx: commands.Context):
        """Tells you how long the bot has been up for."""
        try:
            await ctx.send(f"Bot uptime: {self.bot.get_uptime(which=self.bot.bot_uptime)}!")
        except Exception as e:
            self.basic_logger.error(e)
    
    


def prepare(bot: commands.Bot):
    bot.add_cog(basic(bot))