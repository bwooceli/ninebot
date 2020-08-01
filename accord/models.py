from django.conf import settings
from django.db import models

import discord
from discord.ext import commands



#class DiscordServer(models.Model):
#    name = models.CharField(max_length=255, blank=True)   
#    token = models.CharFIeld(max_length=255)
#    guild = models.CharField(max_length=255)
#
#    def get_client(self):
#        client = discord.client()
#
#
#class Bot(models.Model):
#    server = models.ForeignKey('DiscordServer')


bot = commands.Bot(command_prefix='() ')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#@bot.event
#async def on_member_join(member):
#    role = discord.utils.get(member.server.roles, id="<role ID>")
#    await bot.add_roles(member, role)

@bot.command()
async def what(ctx):
    await ctx.send("It doesn't matter ... it's for my ass")


# @client.command()
# @commands.is_owner()
@bot.command()
async def shutdown(ctx):
    await ctx.bot.logout()

print(f'{settings.DISCORD_TOKEN}')
bot.run(settings.DISCORD_TOKEN)

