import discord, random
from discord.ext import commands

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

class PlePings(commands.Cog):

    def __init__(self, client):
        self.client = client

        #8
        self.shuhua_gif = ["https://tenor.com/view/pop-taiwanese-kpop-yehshuhua-selfdefense-gif-18118582",
        "https://tenor.com/view/gidle-shuhua-%ec%97%ac%ec%9e%90%ec%95%84%ec%9d%b4%eb%93%a4-%ec%95%84%ec%9d%b4%eb%93%a4-%ec%8a%88%ed%99%94-gif-16949157",
        "https://tenor.com/view/shuhua-idle-gidle-yeh-shu-hua-cube-entertainment-gif-16929431",
        "https://tenor.com/view/glasses-shuhua-idle-yeh-gidle-gif-13052094",
        "https://tenor.com/view/yeh-shu-hua-gidle-heart-love-gif-13052095",
        "https://tenor.com/view/kpop-shuhua-gidle-pretty-gif-14904506",
        "https://tenor.com/view/shuhua-kpop-gif-18740565",
        "https://tenor.com/view/%E8%88%92%E8%8F%AF-gidle-%EC%8A%88%ED%99%94-shuhua-wave-gif-16738706"]

        #8
        self.kiki_gif = ["https://tenor.com/view/xu-kiki-xu-jiaqi-7senses-the9-snh48-gif-17740947",
        "https://tenor.com/view/xu-jiaqi-kiki-7senses-snh48-slide-gif-17754236",
        "https://tenor.com/view/xu-jiaqi-pretty-cute-kiki-7senses-gif-17837322",
        "https://tenor.com/view/xu-jiaqi-kiki-7senses-snh48-smile-gif-17946346",
        "https://tenor.com/view/xu-jiaqi-kiki-7senses-snh48-smile-gif-17946344",
        "https://tenor.com/view/xu-jiaqi-kiki-xu-7senses-the9-snh48-gif-17754440",
        "https://tenor.com/view/xu-jiaqi-snh48-kiki-7senses-hat-gif-15001516",
        "https://tenor.com/view/kiki-xu-jiaqi-mama-mama-kiki-xu-jiaqi-dance-gif-17098415"]


    #shuhua command for ple
    @commands.command()
    async def shuhua(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@416903886968979466>, <@!{ctx.author.id}> is talking about Shuhua')
                await ctx.send(random.choice(self.shuhua_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Shuhua')
            await ctx.send(random.choice(self.shuhua_gif))
            await ctx.message.delete()

    #kiki command for ple and mae
    @commands.command()
    async def kiki(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@416903886968979466>, <@492769416610840586>, <@!{ctx.author.id}> is talking about Kiki')
                await ctx.send(random.choice(self.kiki_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@416903886968979466>, <@492769416610840586>, <@!{ctx.author.id}> is talking about Kiki')
            await ctx.send(random.choice(self.kiki_gif))
            await ctx.message.delete()


def setup(client):
    client.add_cog(PlePings(client))