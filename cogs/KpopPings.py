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
weakado = 259409277482041344
k8 = 573974040679809044
mae = 492769416610840586
kiwi = 390317665463566336
kate = 382715972722753536

class KpopPings(commands.Cog):

    def __init__(self, client):
        self.client = client

        #7
        self.yiren_gif = ["https://tenor.com/view/yireon-hearts-wishing-wish-produce48-gif-11924127",
            "https://tenor.com/view/love-you-more-wink-side-eye-flirt-smile-gif-16944406",
            "https://tenor.com/view/%E7%8E%8B%E6%80%A1%E4%BA%BAwang-yiren-cute-kpop-smile-gif-16236336",
            "https://tenor.com/view/wang-yiren-everglow-kpop-cute-sad-gif-16526333",
            "https://tenor.com/view/everglow-yiren-wang-yiren-maknae-rapper-gif-15970519",
            "https://tenor.com/view/wang-yiren-everglow-kpop-fierce-gif-15559282",
            "https://tenor.com/view/%E7%8E%8B%E6%80%A1%E4%BA%BAwang-yiren-cute-kpop-smile-gif-16236336"]

        #19
        self.yeeun_gif = ["https://tenor.com/view/yeeun-clc-gif-19116003",
            "https://tenor.com/view/yeeun-clc-gif-19116004",
            "https://tenor.com/view/yeeun-clc-gif-19116007",
            "https://tenor.com/view/yeeun-clc-gif-19116012",
            "https://tenor.com/view/yeeun-clc-bad-girls-jang-gif-13252706",
            "https://tenor.com/view/yeeun-clc-crystal-clear-cute-girl-group-gif-15041212",
            "https://tenor.com/view/clc-yeeun-clc-yeeun-rap-kpop-gif-15340668",
            "https://tenor.com/view/clc-kpop-yeeun-gif-18657579",
            "https://tenor.com/view/yeeun-jang-clc-cute-stare-gif-13329818",
            "https://tenor.com/view/yeeun-jang-yeeun-cute-clc-kpop-gif-17883335",
            "https://tenor.com/view/yeeun-clc-crystal-clear-cute-girl-group-gif-15041189",
            "https://tenor.com/view/yeeun-clc-bad-girls-jang-gif-13252063",
            "https://tenor.com/view/yeeun-jang-clc-flip-hair-gif-13252498",
            "https://tenor.com/view/yeeun-jang-clc-gif-13328477",
            "https://tenor.com/view/jang-ye-eun-selfie-talking-cute-pretty-gif-16653425",
            "https://tenor.com/view/yeeun-jang-yeeun-clc-crystal-clear-girl-group-gif-15041366",
            "https://tenor.com/view/crystal-clear-jang-kpop-yeeun-clc-gif-14859536",
            "https://tenor.com/view/yay-wink-cute-yeeun-clc-gif-14300869",
            "https://tenor.com/view/yeeun-jang-clc-not-yummy-gif-13252749",
            "https://tenor.com/view/crystal-clear-jang-kpop-devil-yeeun-gif-14999392"]

        #11
        self.lucas_gif = ["https://tenor.com/view/lucas-wayv-heart-gif-14723401",
            "https://tenor.com/view/smile-handsome-cute-lucas-nct-gif-15246419",
            "https://tenor.com/view/nct-lucas-nct-lucas-cute-smile-gif-12612522",
            "https://tenor.com/view/nct-lucas-being-extra-hi-gif-14904496",
            "https://tenor.com/view/pout-kiss-handsome-cute-lucas-gif-15246420",
            "https://tenor.com/view/lucas-nct-way-v-gif-13770508",
            "https://tenor.com/view/wong-yukhei-lucas-nct-cute-kpop-gif-16350448",
            "https://tenor.com/view/lucas-nct-wayv-gif-19030351",
            "https://tenor.com/view/lucas-nct-smile-gif-19015832",
            "https://tenor.com/view/lucas-smile-cute-poke-cheek-gif-12719055",
            "https://tenor.com/view/lucas-nct-wong-yukhei-wayv-gif-14579895"]


    #yiren (everglow) command for weakado
    @commands.command()
    async def yiren(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{weakado}>, <@!{ctx.author.id}> is talking about Yiren :orange_heart:')
                await ctx.send(random.choice(self.yiren_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yiren :orange_heart:')
            await ctx.send(random.choice(self.yiren_gif))
            await ctx.message.delete()
    
    #yeeun (clc) command for me
    @commands.command()
    async def yeeun(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Yeeun :heart:')
                await ctx.send(random.choice(self.yeeun_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yeeun :heart:')
            await ctx.send(random.choice(self.yeeun_gif))
            await ctx.message.delete()

    @commands.command()
    async def lucas(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{kate}>, <@!{ctx.author.id}> is talking about Lucas :heart: ')
                await ctx.send(random.choice(self.lucas_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Lucas :heart:')
            await ctx.send(random.choice(self.lucas_gif))
            await ctx.message.delete()
    


def setup(client):
    client.add_cog(KpopPings(client))