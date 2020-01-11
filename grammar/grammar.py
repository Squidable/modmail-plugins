import discord
from discord.ext import commands
from grammarbot import GrammarBotClient

class Grammar(commands.Cog):
    """Grammar checker."""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        await channel.send('hi')

def setup(bot):
    bot.add_cog(Grammar(bot))