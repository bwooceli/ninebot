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
