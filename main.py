import os
import traceback
import datetime
from twitchio.ext import commands

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=os.environ['TMI_TOKEN'],
            prefix=os.environ['BOT_PREFIX'],
            initial_channels=[os.environ['CHANNEL']]
        )
        self.startup_cogs = [
            "cogs.basic",
        ]
    
    def get_uptime(self, *, brief=False, which=None):
        now = datetime.datetime.utcnow()
        delta = now - which
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        if not brief:
            if days:
                fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds'
            else:
                fmt = '{h} hours, {m} minutes, and {s} seconds'
        else:
            fmt = '{h}h {m}m {s}s'
            if days:
                fmt = '{d}d ' + fmt

        return fmt.format(d=days, h=hours, m=minutes, s=seconds)
    

    async def event_ready(self):
        print(f'---------------------------')
        print(f'Logged in as {self.nick}')
        print(f'User id is {self.user_id}')
        print(f'---------------------------')
        for cog in self.startup_cogs:
            try:
                self.load_module(cog)
            except Exception as e:
                print(f'Couldn\'t load module {cog},  {e}')
        for channel in self.connected_channels:
            print(f'Connecting to {channel}')
        if not hasattr(self, 'bot_uptime'):
            self.bot_uptime = datetime.datetime.utcnow()

    async def event_command_error(self, ctx, exception):
        exception = getattr(exception, 'original', exception)
        tb = ''.join(traceback.format_exception(type(exception), exception, exception.__traceback__, chain=False))
        print(f"---------------------------------------------------- \
                Command failed\n \
                User: {ctx.author.name}\n \
                Error: {type(exception).__name__}: {exception}\n \
                Traceback: {tb}\n \
                ----------------------------------------------------```")



if __name__ == "__main__":
    bot = Bot()
    bot.run()
