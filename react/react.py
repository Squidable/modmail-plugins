import logging
import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

log = logging.getLogger("Modmail")

class ReactOnWord(commands.Cog):
    """Reacts with a banana emoji if someone says a certain word."""
    def __init__(self, bot):
        self.bot = bot
        self.coll = bot.plugin_db.get_partition(self)

    @commands.group()
    @checks.has_permissions(PermissionLevel.ADMIN)
    async def setreact(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('not good')

    @setreact.command()
    async def word(self, ctx, word):
        await self.coll.find_one_and_update(
            {"_id": "reactonword-config"},
            {"$set": {"word": {"word": word}}},
            upsert=True,
        )

    @commands.Cog.listener()
    async def on_message(self, message):
        log.info("A message has been sent.")
        setword = await self.coll.find_one({"_id": "reactonword-config"})
        if setword is None:
            if 'BANANA' in message.content.upper():
                await message.add_reaction('\N{BANANA}')
        else:
            wordy = setword["word"]["word"]
            if wordy.upper in message.content.upper():
                await message.add_reaction('\N{BANANA}')

def setup(bot):
    bot.add_cog(ReactOnWord(bot))