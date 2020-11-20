import discord, random, os
from discord.ext import commands


class scommand(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def status(self, ctx):
        servers = len(self.client.guilds)
        embed = discord.Embed(
            title = 'BOT INFORMATION',
            description = 'lob u :heart:‎',
            colour = discord.Colour.from_rgb(198, 237, 154))
        embed.set_footer(text='')
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/775473868277284885/778452371607912518/Blue_Moonbyul.jpg')
        embed.add_field(name='Moonbyul Ver.', value='1.0.0', inline=True)
        embed.add_field(name='Python Ver.', value='3.8.1', inline=True)
        embed.add_field(name='Ping:', value=f'{round(self.client.latency * 1000)}ms', inline=True)
        embed.add_field(name='Servers:', value=servers, inline=True)
        embed.add_field(name='Developer:', value='<@488423352206229505>', inline=True)
        embed.add_field(name='Helper:', value='‏‏‎<@389897179701182465>', inline=True)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(scommand(client))