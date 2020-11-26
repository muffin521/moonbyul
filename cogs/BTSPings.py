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
princessuwu = 716841614185857086

class BTSPings(commands.Cog):

    def __init__(self, client):
        self.client = client

        #8
        self.v_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781374550419439626/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374550906503188/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374551534600212/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374552059543592/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374552461934622/image4.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374552924094494/image5.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374553388613632/image6.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374553905168405/image7.gif"]

        #8
        self.suga_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781376996051517460/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376997473255434/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376998244483112/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376998852788224/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377281868300318/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377282270035987/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377283252158484/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377284031905842/image3.gif"]

        #7
        self.jhope_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781376181487796224/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376182888431616/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376183551918090/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376184256430100/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376185291767838/image4.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376186805649408/image5.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376187368472626/image6.gif"]

        #9
        self.jungkook_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781375454966972426/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375486843551775/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375522592129024/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375594725376000/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375595178491904/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375596798279710/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375705270583306/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375706437255178/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375707854012416/image2.gif"]

        #12
        self.jin_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781378238282727464/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378239204556810/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378240916619264/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378241817608192/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378242749005904/image4.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378361071108106/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378361943261194/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378363729510430/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378364875210812/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378548342587402/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781379997059121192/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781379997788274698/image1.gif"]

        #10
        self.jimin_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781377634956345383/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377635636609044/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377636190519296/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377637137645578/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377637863391262/image4.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377786698661888/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377787608301568/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377788585181184/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377789689200640/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377790510760006/image4.gif"]

        #9
        self.rm_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781374090497753098/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374226607112252/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374227605225482/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374228132790323/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374228456275968/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374229014511646/image4.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374229836333086/image5.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374230364160030/image6.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374230952411136/image7.gif"]

    @commands.command()
    async def v(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about V :heart:')
                await ctx.send(random.choice(self.v_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about V :heart:')
            await ctx.send(random.choice(self.v_gif))
            await ctx.message.delete()

    @commands.command()
    async def suga(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Suga :heart:')
                await ctx.send(random.choice(self.suga_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Suga :heart:')
            await ctx.send(random.choice(self.suga_gif))
            await ctx.message.delete()

    @commands.command(aliases = ['j-hope'])
    async def jhope(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about J-Hope :heart:')
                await ctx.send(random.choice(self.jhope_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about J-Hope :heart:')
            await ctx.send(random.choice(self.jhope_gif))
            await ctx.message.delete()

    @commands.command()
    async def jungkook(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jungkook :heart:')
                await ctx.send(random.choice(self.jungkook_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jungkook :heart:')
            await ctx.send(random.choice(self.jungkook_gif))
            await ctx.message.delete()

    @commands.command()
    async def jin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jin :heart:')
                await ctx.send(random.choice(self.jin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jin :heart:')
            await ctx.send(random.choice(self.jin_gif))
            await ctx.message.delete()

    @commands.command()
    async def jimin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jimin :heart:')
                await ctx.send(random.choice(self.jimin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jimin :heart:')
            await ctx.send(random.choice(self.jimin_gif))
            await ctx.message.delete()

    @commands.command(aliases = ['namjoon'])
    async def rm(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about RM :heart:')
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