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
k8 = 573974040679809044

class DreamCatcherPings(commands.Cog):

    #wizzy has gifs!!
    def __init__(self, bot):
        self.bot = bot

        

    

def setup(client):
    client.add_cog(DreamCatcherPings(client))