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

        #20
        self.yein_gif = ["https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-yein-%EC%98%88%EC%9D%B8-gif-18419239",
            "https://tenor.com/view/lovelyz-yein-%EC%98%88%EC%9D%B8-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kpop-gif-16459793",
            "https://tenor.com/view/lovelyz-kpop-yein-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EC%98%88%EC%9D%B8-gif-18588376",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-yein-%EC%98%88%EC%9D%B8-gif-18419239",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-yein-%EC%98%88%EC%9D%B8-gif-18213767",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-yein-%EC%98%88%EC%9D%B8-gif-18213757",
            "https://tenor.com/view/lovelyz-kpop-yein-eat-it-gif-16074106",
            "https://tenor.com/view/lovelyz-kpop-kei-mijoo-yein-gif-18565694",
            "https://tenor.com/view/yein-blow-a-bubble-bubble-gum-gum-lovelyz-gif-11607390",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-yein-kpop-%EC%98%88%EC%9D%B8-gif-16459879",
            "https://tenor.com/view/lovelyz-lvlz-jung-yein-yein-gorani-gif-16341215",
            "https://tenor.com/view/yein-lovelyz-kpop-girlgroup-fight-gif-18292941",
            "https://media.discordapp.net/attachments/170383062633283584/755514607308636260/ecd790977d987c6bc0db74a80ca893fb.gif",
            "https://gfycat.com/quarterlymerrydingo",
            "https://gfycat.com/oldfashionedspiritedbluefish",
            "https://gfycat.com/uncomfortablesafebarbet",
            "https://tenor.com/view/yein-lovelyz-oblivate-gif-18541914",
            "https://tenor.com/view/yein-lovelyz-oblivate-gif-18541915",
            "https://gfycat.com/sparserawdiplodocus",
            "https://gfycat.com/lavishteemingalligatorgar"]

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

        #20
        self.kei_gif = ["https://tenor.com/view/lovelyz-kpop-kei-heart-%eb%9f%ac%eb%b8%94%eb%a6%ac%ec%a6%88-gif-18565559",
            "https://tenor.com/view/obliviate-lovelyz-lovelyzkei-kimjiyeon-kei-gif-18226419",
            "https://media.discordapp.net/attachments/448355257383387138/738587515237302312/254A623658B808590C.gif",
            "https://media.discordapp.net/attachments/448355257383387138/738587871904137266/99998A3F5C5A9C4553.gif",
            "https://tenor.com/view/lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kei-%EC%BC%80%EC%9D%B4-gif-16303444",
            "https://tenor.com/view/lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kei-%EC%BC%80%EC%9D%B4-gif-16303756",
            "https://tenor.com/view/kei-kpop-i-go-lovelyz-over-and-over-gif-15309714",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kpop-lovelyz-%EC%BC%80%EC%9D%B4-kei-gif-18182587",
            "https://tenor.com/view/kpop-lovelyz-kei-i-go-lovelinus-gif-15336273",
            "https://tenor.com/view/kpop-korean-lovelyz-kei-gif-10760158",
            "https://tenor.com/view/lovelyz-kei-delicous-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-16496984",
            "https://tenor.com/view/lovelyz-kei-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EC%BC%80%EC%9D%B4-kpop-gif-16516714",
            "https://tenor.com/view/lovelyz-kei-kim-jiyeon-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-16626147",
            "https://tenor.com/view/kpop-lovelyz-kei-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EC%BC%80%EC%9D%B4-gif-18225963",
            "https://tenor.com/view/lovelyz-kei-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EC%BC%80%EC%9D%B4-gif-18588396",
            "https://tenor.com/view/kei-lovelyz-adorable-braid-gif-18525447",
            "https://tenor.com/view/kpop-korean-lovelyz-kei-gif-10760160",
            "https://tenor.com/view/lovelyz-kei-mijoo-kiss-kpop-gif-16318978",
            "https://tenor.com/view/lovelyz-lovelyz-kei-kei-kim-kei-kim-jiyeon-gif-16341360",
            "https://tenor.com/view/lovelyz-kei-will-kpop-gif-14248063"]

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

        #
        #self.yukika_gif = []


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

    #yein (lovelyz) command for me
    @commands.command()
    async def yein(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@{mae}>, <@{kiwi}>, <@!{ctx.author.id}> is talking about Yein :heart:')
                await ctx.send(random.choice(self.yein_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yein :heart:')
            await ctx.send(random.choice(self.yein_gif))
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

    #kei (lovelyz) command for me
    @commands.command()
    async def kei(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Kei :yellow_heart:')
                await ctx.send(random.choice(self.kei_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Kei :yellow_heart:')
            await ctx.send(random.choice(self.kei_gif))
            await ctx.message.delete()

    @commands.command()
    async def lucas(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Lucas :heart: ')
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