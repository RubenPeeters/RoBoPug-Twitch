import os
import traceback
import datetime
import logging
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
            "cogs.spotify"
        ]
        self.main_logger = logging.getLogger('RoBoPug.main')
        self.chat_logs = open(f"./chat-logs/RoBoPug_{datetime.datetime.utcnow()}.chat", 'w')
    
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
        self.main_logger.info(f'---------------------------')
        self.main_logger.info(f'Logged in as {self.nick}')
        self.main_logger.info(f'User id is {self.user_id}')
        self.main_logger.info(f'---------------------------')
        for cog in self.startup_cogs:
            try:
                self.load_module(cog)
                self.main_logger.info(f'Loaded module: {cog}')
            except Exception as e:
                self.main_logger.error(f'Couldn\'t load module {cog},  {e}')
        self.main_logger.info(f'Loading modules - DONE.')
        for channel in self.connected_channels:
            self.main_logger.info(f'Connected to {channel.name}')
        self.main_logger.info(f'Joining channels - DONE.')
                
        if not hasattr(self, 'bot_uptime'):
            self.bot_uptime = datetime.datetime.utcnow()

    async def event_command_error(self, ctx, exception):
        self.main_logger.error(f'{exception}')

if __name__ == "__main__":
    # set up logging to file - see previous section for more details
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=f'./logs/RoBoPug_{datetime.datetime.utcnow()}.log',
                        filemode='w')
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)
    bot = Bot()
    bot.run()
