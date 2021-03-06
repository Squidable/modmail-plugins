import discord
from discord.ext import commands
import random

class EightBall(commands.Cog):
    """
    Ask ModMail a question and get an answer from a ever-growing list of answers.

    Disclaimer: These answers are jokes and should be taken as jokes.
    For legal advice, talk to a lawyer.
    For general advice, don't take it from a bot.
    """
    def __init__(self, bot):
        self.bot = bot

    balllist = [
        'Yes.',
        'No.',
        'Of course.',
        'Good luck making that happen.',
        'It may happen.',
        'The chance of that happening is as likely as dolphins singing \'Happy Birthday\' all of a sudden.',
        'No, just... no.',
        'The magic sources say yes, don\'t ask me who they are!',
        'Ask again later, or never, it is not my decision.',
        'Outlook good.',
        'Seems nice.',
        'Ask again later.',
        'Concentrate and ask again.',
        'It might be yes, but how am I supposed to know!?',
        'Don\'t count on it.',
        'Maybe yes, maybe no.',
        'Yes - definitely.',
        'No - definitely not.',
        'Why are you asking me?',
        'Noooooooooooooooooooooooooooo.',
        'Error 404, response not found. Ask again later.',
        'I see \'Yes\' in your future.',
        'Only you know the answer... unless someone else knows.',
        'Why are you asking me questions, don\'t you have something better to do?',
        'The answer you are seeking is not available at the moment.',
        'Definitely, no.',
        'Stars aligned, I don\'t know what that means',
        'Saturn is bright today (or tonight).',
        'You think I\'m a magic 8 ball or something?',
        'Yes, yes, yes yes yes. The gods say: no.',
        'Yes sir. (or ma\'am or whatever you prefered to be called.)',
        '\"Bzzzzt- We got incoming. New message. Message: \'No.\'',
        'Let it go, let it goooooo! Can\'t hold it back any— Um... This is awkward... \"Ask again later."',
        'Repeat your question.',
        'Does not compute.',
        'Thy answer is aye.',
        'Prithee, asketh again.',
        'Error 63.84e45: Question overload! System failure. Try again later.',
        'You shall ask again. LISTEN TO ME!',
        'Yeet.',
        'It\'s obviously no—just kidding, it\'s yes.',
        'Affirmative.',
        'Whatever you say.',
        'Most likely.',
        'It is decidedly so.',
        'Not now, maybe when you\'re older.',
        'The wise gods say... *suspenceful music plays* \"No.\"',
        'Yes!!!',
        '\"Hello, TotallyNotFakeCyGuy here and your answer is—\" What is he doing here?! GET OUT! And for you... \"Please try again later.\"',
        'New message recieved: Yes',
        'Of course... not. Jkjk, yes...or is it? It isn\'t not of course not not the opposite of not no. Confusion: 1000. Ask again later.',
        'Try again ~~later~~ right now.',
        '[REDACTED]',
        'Let\'s leave the answer into the unknown, into the unknown.',
        'godTransmissionError: Evil intercepted. Please try again.',
        '\"Don\'t take advice from a bot\" - Abraham Lincoln',
        'Ask again in 3.8 minutes.',
        '~~Yes, definitely.~~',
        'Sorry for the interruption: If you would like to add this plugin to your ModMail bot, use the command below! Now, the answer you\'ve been waiting for: [Please try again later.]',
        'Yes. WAHOO!!! Wait, that\'s good, right?',
        'Message recieved. Message: [Error 6.88e8: Message not recieved, try again later.]',
        '<insert answer here>'
    ]

    @commands.command(aliases = ['ateball', '8bl'])
    async def eightball(self, ctx, *, question):
        """
        Ask ModMail 8-Ball a question and get a response!

        Usage: [prefix]eightball <question>
        """
        choice = random.choice(self.balllist)
        embed=discord.Embed(title=f"Question by {ctx.author}:", description=question, color=0x51eaff)
        embed.set_author(name="8-Ball", url="https://github.com/realcyguy/modmail-plugins/", icon_url="https://media.istockphoto.com/photos/pool-ball-picture-id491993923?k=6&m=491993923&s=612x612&w=0&h=u6SNe9jYA1ZidZ_vfU1LHpaDVNnrbUFivOKxazcrNCI=")
        embed.add_field(name="Answer:", value=choice, inline=False)
        embed.set_footer(text="?plugin add realcyguy/modmail-plugins/8ball")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(EightBall(bot))
