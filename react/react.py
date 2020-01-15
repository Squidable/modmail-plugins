import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

class ReactOnWord(commands.Cog):
    """Reacts with a banana emoji if someone says a certain word."""
    def __init__(self, bot):
        self.bot = bot
        self.coll = bot.plugin_db.get_partition(self)

    @commands.group()
    @checks.has_permissions(PermissionLevel.ADMIN)
    async def react(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('not good')

    @react.command()
    async def word(self, ctx, *, word):

        await ctx.send(f'hello and {word}')

    @commands.Cog.listener()
    async def on_message(self, message):
        if 'BANANA' in message.content.upper():
            await message.add_reaction('\N{BANANA}')

def setup(bot):
    bot.add_cog(ReactOnWord(bot))