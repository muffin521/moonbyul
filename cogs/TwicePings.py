import discord, random, os
from discord.ext import commands

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

class gamerPings(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.mina_gif = []

        self.sana_gif = []

        self.momo_gif = []

        self.jeongyeon_gif = []
        
        self.tzuyu_gif = []

        self.nayeon_gif = []

        self.dahyun_gif = []

        self.jihyo_gif = []

        self.chaeyoung_gif = ["https://tenor.com/view/chaeyoung-twice-kpop-jyp-jypnation-gif-14436666"]


    @commands.command()
    async def mina(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Mina :heart:')
                await ctx.send(random.choice(self.mina_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Mina :heart:')
            await ctx.send(random.choice(self.mina_gif))
            await ctx.message.delete()
    
    @commands.command()
    async def sana(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Sana :heart:')
                await ctx.send(random.choice(self.sana_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Sana :heart:')
            await ctx.send(random.choice(self.sana_gif))
            await ctx.message.delete()

    @commands.command()
    async def momo(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Momo :heart:')
                await ctx.send(random.choice(self.momo_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Momo :heart:')
            await ctx.send(random.choice(self.momo))
            await ctx.message.delete()
    
    @commands.command()
    async def jeongyeon(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jeongyeon :heart:')
                await ctx.send(random.choice(self.jeongyeon_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jeongyeon :heart:')
            await ctx.send(random.choice(self.jeongyeon_gif))
            await ctx.message.delete()

    @commands.command()
    async def tzuyu(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Tzuyu :heart:')
                await ctx.send(random.choice(self.tzuyu_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Tzuyu :heart:')
            await ctx.send(random.choice(self.tzuyu_gif))
            await ctx.message.delete()

    @commands.command()
    async def nayeon(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Nayeon :heart:')
                await ctx.send(random.choice(self.nayeon_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Nayeon :heart:')
            await ctx.send(random.choice(self.nayeon_gif))
            await ctx.message.delete()

    @commands.command()
    async def dahyun(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Dahyun :heart:')
                await ctx.send(random.choice(self.dahyun_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Dahyun :heart:')
            await ctx.send(random.choice(self.dahyun_gif))
            await ctx.message.delete()

    @commands.command()
    async def jihyo(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jihyo :heart:')
                await ctx.send(random.choice(self.jihyo_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jihyo :heart:')
            await ctx.send(random.choice(self.jihyo_gif))
            await ctx.message.delete()

    @commands.command()
    async def chaeyoung(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chaeyoung :heart:')
                await ctx.send(random.choice(self.chaeyoung_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Chaeyoung :heart:')
            await ctx.send(random.choice(self.chaeyoung_gif))
            await ctx.message.delete()



def setup(client):
    client.add_cog(gamerPings(client))