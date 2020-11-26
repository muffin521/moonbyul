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

class KpopPings(commands.Cog):

    def __init__(self, client):
        self.client = client

        #9
        self.natty_gif = ["https://thumbs.gfycat.com/BlankBlaringAmurratsnake-size_restricted.gif",
            "https://thumbs.gfycat.com/ScholarlyUnitedCutworm-max-1mb.gif",
            "https://media.giphy.com/media/f7Xr9BVORnb0vDEraT/giphy.gif",
            "https://giphy.com/gifs/jpEGzlpjwOn1RK0qlZ",
            "https://tenor.com/view/natty-schoolidol-gif-9239469",
            "https://giphy.com/gifs/vOzalSmlR1cVr535rb",
            "https://giphy.com/gifs/AWcuiZbziFmwuc0uQW",
            "https://giphy.com/gifs/sksJILJA9Ab0HiOIIp",
            "https://giphy.com/gifs/hL7aBcWxpzp0VrljNu"]

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

        #9
        self.alexa_gif = ["https://tenor.com/view/no-ahhhh-emotions-ai-trooper-alexa-gif-18362239",
            "https://tenor.com/view/alexa-alexa-kpop-wink-cute-wink-alex-christine-gif-18426203",
            "https://tenor.com/view/sunlight-alexa-alexa-kpop-villain-alexa-villain-gif-18426653",
            "https://tenor.com/view/alexa-kpop-alexa-dance-do-or-die-alexazblabel-gif-18228202",
            "https://tenor.com/view/millenasia-millenesia-project-alexa-alexa-kpop-bale-bale-kpop-gif-18240233",
            "https://tenor.com/view/okay-ok-what-is-it-say-alexa-gif-18669905",
            "https://tenor.com/view/alexa-kpop-alexa-quadratic-equation-maths-alex-christine-gif-19114670",
            "https://tenor.com/view/shocked-shocking-unbelievable-villian-alexa-gif-18776700",
            "https://tenor.com/view/alexa-alexa-kpop-alexa-universe-rule-the-world-alexa-alexa-rule-the-world-gif-18285902"]

        #
        self.giselle_gif = []

        #self.yukika_gif = []

    
    #natty (solo) command
    @commands.command()
    async def natty(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Natty :teddy_bear:')
                await ctx.send(random.choice(self.natty_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Natty :teddy_bear:')
            await ctx.send(random.choice(self.natty_gif))
            await ctx.message.delete()

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
                await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Yein :heart:')
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

    #alexa (solo) command for me
    @commands.command()
    async def alexa(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about AleXa :blue_heart:')
                await ctx.send(random.choice(self.alexa_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about AleXa :blue_heart:')
            await ctx.send(random.choice(self.alexa_gif))
            await ctx.message.delete()

    #giselle command for k8
    @commands.command
    async def giselle(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{k8}>, <@!{ctx.author.id}> is talking about Giselle :heart:')
                await ctx.send(random.choice(self.giselle_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Giselle :heart:')
            await ctx.send(random.choice(self.giselle_gif))
            await ctx.message.delete()




def setup(client):
    client.add_cog(KpopPings(client))