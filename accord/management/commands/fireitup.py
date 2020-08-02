from django.core.cache import caches
from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import now
from django.utils import timezone

from django.conf import settings

import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingAnyRole


# ctx.guild to fetch the Guild of the command, if any.
# ctx.message to fetch the Message of the command.
# ctx.author to fetch the Member or User that called the command.
# ctx.send() to send a message to the channel the command was used in.

class GettingStarted(commands.Cog):
    """Getting Started"""
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Hey look, everybody! {0.mention} is here! @{0.mention} you can type \n> >>help\n for ninebot commands'.format(member))


    @commands.command()
    async def newhere(self, ctx, *, member: discord.Member = None):
        """- sends helpful info for newbies"""

        onboarding = """
1) You can (but don't have to) change your nickname by typing 
> /nick Emperor Kuzco
or something clever like that.  Or right-click yourself on the list to your right.
This change will ONLY change your nickname on this server, not any other discord servers you might join

2) If there are some channels that you don't want to get alerts/notifications for, long-press or right click them and mute (can be done temporarily or permanently)

3) You are able to create channels of your own, so go nuts.  If things start getting too cluttered, we can organize them or prune down the line.

4) Not that it's a hard rule, but ideally this is limited to people that the majority of us know personally, and who we have a better-than-zero chance of seeing in the real world in the next couple of years.  I started this because getting friends together online has kind of been hard given that more and more people are boycotting Facebook and/or Twitter, and that even on those platforms it's hard to actually just talk because of the large audiences.  So you're more than welcome to invite people, but I'd like to keep it to former apt9 keyholders, halloween party goers (of any era), christmas gift-wrap throwers, and the like.

"""

        member = member or ctx.author
        await ctx.send(f'Ok, {member.name}, here\'s some useful info to get started\nThis message will self-destruct in 60 seconds, but you can read it again by typing \n> >>help\n{onboarding}',
            delete_after=60)
        # else:
        #     await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        # self._last_member = member


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass
        # parser.add_argument('--campaign_id', nargs='+')

    def handle(self, *args, **options):
        bot = commands.Bot(command_prefix='>>')

        @bot.event
        async def on_ready():
            print('Ready!')

        @bot.command()
        async def ping(ctx):
            """replies ... pong.  super useful"""
            await ctx.send('pong')

        # @client.command()
        # @commands.is_owner()
        @bot.command()
        @commands.has_any_role('dev')
        async def begone(ctx, *, member: discord.Member = None):
            """Only Devs can banish the bot"""
            try:
                await ctx.bot.logout()
            except:
                await ctx.send("Sorry, only devs can banish the bot")

        bot.add_cog(GettingStarted(bot))

        bot.run(settings.DISCORD_TOKEN)


