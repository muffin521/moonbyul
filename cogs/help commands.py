import discord, random, os
from discord.ext import commands


class hcommands(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #?Help Command [basic]
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(
            title = 'HELP',
            description = 'All commands start with the prefix [=]',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed.add_field(name='Help Commands', value=f'''```
Iz*One
Blackpink
Mamamoo
Loona
Red Velvet
Others
```''')
        embed.add_field(name='Help', value=f'''
DM <@!{488423352206229505}>
to get your
command added
or with 
questions! 
''')
        embed.add_field(name='Thanks to:', value=f'''\n<@389897179701182465>''')
        await ctx.send(embed=embed)
        await ctx.message.delete()

    #?izone help command
    @commands.command(aliases = ['helpiz*one'])
    async def helpizone(self, ctx):
        embed=discord.Embed(
            title = 'IZ*ONE',
            description = 'All commands start with the prefix [=]',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed.add_field(name='Members [1]', value=f'''```\nSakura\nYuri\nChaeyeon```''')
        embed.add_field(name='Memebers [2]', value=f'''```\nMinju\nHyewon\nWonyoung```''')
        await ctx.send(embed=embed)
        await ctx.message.delete()

    #?loona help command
    @commands.command(aliases = ['helplooπδ'])
    async def helploona(self, ctx):
        embed=discord.Embed(
            title = 'IZ*ONE',
            description = 'All commands start with the prefix [=]',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed.add_field(name='1/3', value=f'''```\nHeejin\nHyunjin```''')
        embed.add_field(name='Odd Eye Circle', value=f'''```\nKim Lip\nChoerry```''')
        await ctx.send(embed=embed)
        await ctx.message.delete()

    #?blackpink help command
    @commands.command(aliases = ['helpbp'])
    async def helpblackpink(self, ctx):
        embed=discord.Embed(
            title = 'BLACKPINK',
            description = 'All commands start with the prefix [=]',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed.add_field(name='Rap Line', value=f'''```\nLisa\nJennie```''')
        embed.add_field(name='Vocal Line', value=f'''```\nJisoo\nRose```''')
        await ctx.send(embed=embed)
        await ctx.message.delete()

    #?mamamoo help command
    @commands.command()
    async def helpmamamoo(self, ctx):
        embed=discord.Embed(
            title = 'MAMAMOO',
            description = 'All commands start with the prefix [=]',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed.add_field(name='Rap Line', value=f'''```\nMoonbyul\nHwasa```''')
        embed.add_field(name='Vocal Line', value=f'''```\nSolar\nWheein```''')
        await ctx.send(embed=embed)
        await ctx.message.delete()

    #?red velvet help command
    @commands.command()
    async def helpredvelvet(self, ctx):
        embed=discord.Embed(
            title = 'RED VELVET',
            description = 'All commands start with the prefix [=]',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed.add_field(name='Members [1]', value=f'''```\nJoy\nIrene\nSeulgi```''')
        embed.add_field(name='Members [2]', value=f'''```\nYeri\nWendy```''')
        await ctx.send(embed=embed)
        await ctx.message.delete()

    #?misc help command
    @commands.command(aliases = ['helpmisc'])
    async def helpothers(self, ctx):
        embed=discord.Embed(
            title = 'MISC',
            description = 'All commands start with the prefix [=]',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed.add_field(name='Mae', value=f'''```\nJessica\nKrystal\nTaemin```''')
        embed.add_field(name='Ple', value=f'''```\nShuhua\nKiki```''')
        embed.add_field(name='Others', value=f'''```\nNatty\nYiren\nFood\nChuu Heart```''')
        await ctx.send(embed=embed)
        await ctx.message.delete()



def setup(client):
    client.add_cog(hcommands(client))
