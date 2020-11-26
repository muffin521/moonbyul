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
lulu = 721653307998994453

class BTSPings(commands.Cog):

    def __init__(self, client):
        self.client = client

        #
        self.v_gif = []

        #
        self.suga_gif = []

        #
        self.jhope_gif = []

        #
        self.jungkook_gif = []

        #
        self.jin_gif = []

        #
        self.jimin_gif = []

        #
        self.rm_gif = []

    #v command for lulu
    @commands.command()
    async def v(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@!{ctx.author.id}> is talking about V :heart:')
                await ctx.send(random.choice(self.v_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about V :heart:')
            await ctx.send(random.choice(self.v_gif))
            await ctx.message.delete()

    #suga command for lulu
    @commands.command()
    async def suga(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@!{ctx.author.id}> is talking about Suga :heart:')
                await ctx.send(random.choice(self.suga_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Suga :heart:')
            await ctx.send(random.choice(self.suga_gif))
            await ctx.message.delete()

    #j-hope command for lulu
    @commands.command(aliases = ['j-hope'])
    async def jhope(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@!{ctx.author.id}> is talking about J-Hope :heart:')
                await ctx.send(random.choice(self.jhope_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about J-Hope :heart:')
            await ctx.send(random.choice(self.jhope_gif))
            await ctx.message.delete()

    #jungkook command for lulu
    @commands.command()
    async def jungkook(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@!{ctx.author.id}> is talking about Jungkook :heart:')
                await ctx.send(random.choice(self.jungkook_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jungkook :heart:')
            await ctx.send(random.choice(self.jungkook_gif))
            await ctx.message.delete()

    #jin command for lulu
    @commands.command()
    async def jin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@!{ctx.author.id}> is talking about Jin :heart:')
                await ctx.send(random.choice(self.jin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jin :heart:')
            await ctx.send(random.choice(self.jin_gif))
            await ctx.message.delete()

    #jimin command for lulu
    @commands.command()
    async def jimin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@!{ctx.author.id}> is talking about Jimin :heart:')
                await ctx.send(random.choice(self.jimin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jimin :heart:')
            await ctx.send(random.choice(self.jimin_gif))
            await ctx.message.delete()

    #rm command for lulu
    @commands.command()
    async def rm(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@!{ctx.author.id}> is talking about RM :heart:')
                await ctx.send(random.choice(self.rm_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about RM :heart:')
            await ctx.send(random.choice(self.rm_gif))
            await ctx.message.delete()

def setup(client):
    client.add_cog(BTSPings(client))