import discord, random, os
from discord.ext import commands

byulver = '1.3.6'

#//people
muffin = 488423352206229505 #// other things
gareth = 389897179701182465 #// other things
k8 = 573974040679809044 #.not in
weakado = 259409277482041344
ple = 416903886968979466
dj = 373369932303433728 #.not in
aster = 495714786823241728 
himiko = 745060875483742258
naomi = 175498897324507138
nina = 689578336737165314

class scommand(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            title = 'Pong!',
            description = 'lob u <:moonbyulheart:790333102924627968>‎',
            colour = discord.Colour.from_rgb(198, 237, 154))
        # embed.set_footer(text='')
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/775473868277284885/778452371607912518/Blue_Moonbyul.jpg')
        embed.add_field(name='Ping:', value=f'{round(self.client.latency * 1000)}ms', inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def info(self, ctx):
        servers = len(self.client.guilds)
        embed = discord.Embed(
            title = 'BOT INFORMATION',
            description = 'lob u <:moonbyulheart:790333102924627968>‎',
            colour = discord.Colour.from_rgb(198, 237, 154))
        # embed.set_footer(text='')
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/775473868277284885/778452371607912518/Blue_Moonbyul.jpg')
        embed.add_field(name='Moonbyul Ver.', value= byulver, inline=True)
        embed.add_field(name='Python Ver.', value='3.8.1', inline=True)
        embed.add_field(name='Ping:', value=f'{round(self.client.latency * 1000)}ms', inline=True)
        embed.add_field(name='Servers:', value=servers, inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def bot(self, ctx):
        embed = discord.Embed(
            title = 'Moonbyul Bot <:moonbyulheart:790333102924627968>',
            description = 'lob u <:moonbyulheart:790333102924627968>',
            colour = discord.Colour.from_rgb(198, 237, 154))
        embed.set_footer(text='')
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/775473868277284885/778452371607912518/Blue_Moonbyul.jpg')
        embed.add_field(name='Developer:', value=f'<@{muffin}>\n \n**Helpers:**\n<@{gareth}>\n<@{aster}>\n<@{k8}>', inline=True)
        embed.add_field(name='Ping:', value=f'{round(self.client.latency * 1000)}ms\n \n**Moonbyul Ver.**\n{byulver}', inline=True)
        embed.add_field(name='Top Gifs:', value=f'<@{naomi}>\n<@{nina}>\n<@{k8}>\n<@{himiko}>\n<@{weakado}>\n<@{aster}>')
        embed.add_field(name='Invite Link', value=f'[Moonbyul Invite](https://discord.com/oauth2/authorize?client_id=770750635850858506&permissions=273472&scope=bot)', inline=False)
        await ctx.send(embed=embed)
        #. <@{naomi}>\n<@{nina}>\n<@{k8}>\n<@{himiko}>\n<@{weakado}>\n<@{aster}>

    @commands.command()
    @commands.is_owner()
    async def servers(self, ctx):
            guilds = self.client.guilds
            
            for server in guilds:
                guild = str(server)
                guild_id = str(server.id)
                owner = str(server.owner_id)
                members = str(server.member_count)
                
                await ctx.send("**"+ guild + "**\n" + "Server ID: " + guild_id + "\nOwner ID: " + owner + "\nMembers: " + members)

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            title = 'Invite Links',
            description = 'lob u <:moonbyulheart:790333102924627968>‎',
            colour = discord.Colour.from_rgb(198, 237, 154))
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/775473868277284885/778452371607912518/Blue_Moonbyul.jpg')
        embed.add_field(name='Support Server', value=f'https://discord.gg/Ntk9Jp26yx', inline=True)
        embed.add_field(name='Invite Link', value=f'[Moonbyul Invite](https://discord.com/oauth2/authorize?client_id=770750635850858506&permissions=273472&scope=bot)', inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(scommand(client))