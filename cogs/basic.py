import os
import logging
from twitchio.ext import commands



class basic(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.basic_logger = logging.getLogger('RoBoPug.basic')

    @commands.Cog.event()
    async def event_message(self, message):
        if message.echo:
            return
        self.bot.chat_logs.write(f'{message.author.name}: {message.content}\n')
    
    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send(f"/announce Discord: https://discord.gg/vbknFwz")

    @commands.command(aliases=['h'])
    async def help(self, ctx: commands.Context):
        await ctx.send(f"The available commands are: {', '.join(self.bot.commands.keys())}.")

    @commands.command()
    async def botuptime(self, ctx: commands.Context):
        """Tells you how long the bot has been up for."""
        try:
            await ctx.send(f"Bot uptime: {self.bot.get_uptime(which=self.bot.bot_uptime)}.")
        except Exception as e:
            self.basic_logger.error(e)
    
    


def prepare(bot: commands.Bot):
    bot.add_cog(basic(bot))