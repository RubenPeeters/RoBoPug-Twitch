import os
import logging
from twitchio.ext import commands



class basic(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.basic_logger = logging.getLogger('RBotP.basic')

    @commands.Cog.event()
    async def event_message(self, message):
        if message.echo:
            return
        # print(message.content)
    
    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send(f"Discord: https://discord.gg/vbknFwz")

    @commands.command(aliases=['h'])
    async def help(self, ctx: commands.Context):
        self.basic_logger.info(f"The available commands are: {', '.join(self.bot.commands.keys())}.")
        await ctx.send(f"The available commands are: {', '.join(self.bot.commands.keys())}.")

    @commands.command()
    async def botuptime(self, ctx: commands.Context):
        """Tells you how long the bot has been up for."""
        try:
            self.basic_logger.info(f"Bot uptime: {self.bot.get_uptime(which=self.bot.bot_uptime)}.")
            await ctx.send(f"Bot uptime: {self.bot.get_uptime(which=self.bot.bot_uptime)}.")
        except Exception as e:
            self.basic_logger.error(e)
    
    


def prepare(bot: commands.Bot):
    bot.add_cog(basic(bot))