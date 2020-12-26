import discord, random, os
from discord.ext import commands

byulver = '1.1.5'

#//people
muffin = 488423352206229505
gareth = 389897179701182465
weakado = 259409277482041344
ple = 416903886968979466
mia = 709690937680461865
dj = 373369932303433728
jat = 236787566530134017

class scommand(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def info(self, ctx):
        servers = len(self.client.guilds)
        embed = discord.Embed(
            title = 'BOT INFORMATION',
            description = 'lob u <:moonbyulheart:790333102924627968>‎',
            colour = discord.Colour.from_rgb(198, 237, 154))
        embed.set_footer(text='')
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/775473868277284885/778452371607912518/Blue_Moonbyul.jpg')
        embed.add_field(name='Moonbyul Ver.', value= byulver, inline=True)
        embed.add_field(name='Python Ver.', value='3.8.1', inline=True)
        embed.add_field(name='Ping:', value=f'{round(self.client.latency * 1000)}ms', inline=True)
        embed.add_field(name='Servers:', value=servers, inline=True)
        embed.add_field(name='Developer:', value=f'<@{muffin}>', inline=True)
        embed.add_field(name='Helper:', value=f'‏‏‎<@{gareth}>', inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def bot(self, ctx):
        embed = discord.Embed(
            title = 'Moonbyul Bot <:moonbyulheart:790333102924627968>',
            description = 'lob u <:moonbyulheart:790333102924627968>',
            colour = discord.Colour.from_rgb(198, 237, 154))
        embed.set_footer(text='')
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/775473868277284885/778452371607912518/Blue_Moonbyul.jpg')
        embed.add_field(name='Developer:', value=f'<@{muffin}>\n \n**Helper:**\n<@{gareth}>', inline=True)
        embed.add_field(name='Ping:', value=f'{round(self.client.latency * 1000)}ms\n \n**Moonbyul Ver.**\n{byulver}', inline=True)
        embed.add_field(name='Top Gifs:', value=f'‏‏‎<@{weakado}>\n<@{ple}>\n<@{mia}>\n<@{jat}>\n<@{dj}>', inline=True)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(scommand(client))