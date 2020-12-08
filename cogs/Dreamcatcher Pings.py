import discord, random
from discord.ext import commands

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

#//people


class DreamCatcherPings(commands.Cog):


    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(DreamCatcherPings(client))