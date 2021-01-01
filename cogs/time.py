import discord, random, os, datetime
#import pytz
from discord.ext import commands
from datetime import datetime

 #(tz=None)



#  https://docs.python.org/3/library/datetime.html#datetime.datetime.now

class time(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def muffintime(self, ctx):
        muffin_time = datetime.now()
        await ctx.send(f'It is currently {muffin_time.strftime("%H:%M:%S")} for Muffin!')

    # @commands.command()
    # async def garethtime(self, ctx):
    #     gareth_time = datetime.now(pytz.utc)
    #     await ctx.send(f'It is currently {gareth_time.strftime("%H:%M:%S")} for Gareth!')

def setup(client):
    client.add_cog(time(client))