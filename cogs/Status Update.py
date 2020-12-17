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
muffin = 488423352206229505

class Status(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def status(self, ctx, arg = "play", *, message):
        if arg == "playing":
            embed = discord.Embed(
                title = 'Status Changed To',
                description = f'{message}',
                colour = discord.Colour.from_rgb(198, 237, 154))
            await ctx.send(embed=embed)
            await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f'{message}'))
        elif arg == "listening":
            embed = discord.Embed(
                title = 'Status Changed To',
                description = f'{message}',
                colour = discord.Colour.from_rgb(198, 237, 154))
            await ctx.send(embed=embed)
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{message}'))
        elif arg == "streaming":
            embed = discord.Embed(
                title = 'Status Changed To',
                description = f'{message}',
                colour = discord.Colour.from_rgb(198, 237, 154))
            await ctx.send(embed=embed)
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f'{message}'))
        else:
            embed = discord.Embed(
                title = 'Status Changed To',
                description = f'{message}',
                colour = discord.Colour.from_rgb(198, 237, 154))
            await ctx.send(embed=embed)
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{message}'))


def setup(client):
    client.add_cog(Status(client))