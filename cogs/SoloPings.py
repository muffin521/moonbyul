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


class SoloPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.natty_gif = ["https://thumbs.gfycat.com/BlankBlaringAmurratsnake-size_restricted.gif",
            "https://thumbs.gfycat.com/ScholarlyUnitedCutworm-max-1mb.gif",
            "https://media.giphy.com/media/f7Xr9BVORnb0vDEraT/giphy.gif",
            "https://giphy.com/gifs/jpEGzlpjwOn1RK0qlZ",
            "https://tenor.com/view/natty-schoolidol-gif-9239469",
            "https://giphy.com/gifs/vOzalSmlR1cVr535rb",
            "https://giphy.com/gifs/AWcuiZbziFmwuc0uQW",
            "https://giphy.com/gifs/sksJILJA9Ab0HiOIIp",
            "https://giphy.com/gifs/hL7aBcWxpzp0VrljNu",
            "https://tenor.com/view/dance-nt-natty-natty_gif-%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-gif-19179900",
            "https://tenor.com/view/%EB%82%98%EB%9D%A0-%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-nt-natty-natty_gif-gif-19177703",
            "https://tenor.com/view/%EB%82%98%EB%9D%A0-%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-nt-natty-natty_gif-gif-19359163",
            "https://tenor.com/view/%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-%EB%82%98%EB%9D%A0-nt-natty-natty-teddybear-gif-19176290",
            "https://tenor.com/view/%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-nt-natty-natty_gif-opps-gif-19266831",
            "https://tenor.com/view/%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-%EB%82%98%EB%9D%A0-nt-natty-natty-teddybear-gif-19176299",
            "https://tenor.com/view/%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-%EB%82%98%EB%9D%A0-nt-natty-natty_gif-gif-19360526"]

        #9
        self.bot.alexa_gif = ["https://tenor.com/view/no-ahhhh-emotions-ai-trooper-alexa-gif-18362239",
            "https://tenor.com/view/alexa-alexa-kpop-wink-cute-wink-alex-christine-gif-18426203",
            "https://tenor.com/view/sunlight-alexa-alexa-kpop-villain-alexa-villain-gif-18426653",
            "https://tenor.com/view/alexa-kpop-alexa-dance-do-or-die-alexazblabel-gif-18228202",
            "https://tenor.com/view/millenasia-millenesia-project-alexa-alexa-kpop-bale-bale-kpop-gif-18240233",
            "https://tenor.com/view/okay-ok-what-is-it-say-alexa-gif-18669905",
            "https://tenor.com/view/alexa-kpop-alexa-quadratic-equation-maths-alex-christine-gif-19114670",
            "https://tenor.com/view/shocked-shocking-unbelievable-villian-alexa-gif-18776700",
            "https://tenor.com/view/alexa-alexa-kpop-alexa-universe-rule-the-world-alexa-alexa-rule-the-world-gif-18285902"]

        #10
        self.bot.chungha_gif = ["https://tenor.com/view/kiss-love-chunga-korean-gif-11126096",
            "https://tenor.com/view/chungha-gif-18541917",
            "https://tenor.com/view/chungha-stare-smokey-eyes-gif-14390425",
            "https://tenor.com/view/chungha-gif-14681679",
            "https://tenor.com/view/kim-chungha-chungha-cute-smile-gif-13261337",
            "https://tenor.com/view/kim-chungha-chungha-cute-gorgeous-smile-gif-12547851",
            "https://tenor.com/view/kim-chungha-chungha-wink-sexy-gif-12547847",
            "https://tenor.com/view/chungha-kim-chungha-kpop-pretty-cute-gif-16653910",
            "https://tenor.com/view/rae-chungha-fancam-play-kpop-gif-18963908",
            "https://tenor.com/view/chungha-kim-chungha-kpop-cute-pretty-gif-16521270"]
        
        self.bot.iu_gif = ["https://tenor.com/view/iu-fighting-cute-celeb-alarm-gif-16215337",
            "https://tenor.com/view/iu-meh-cute-annoyed-gif-14687766",
            "https://tenor.com/view/iu-lee-jieun-cute-cf-pout-gif-16660666",
            "https://tenor.com/view/iu-cindy-cute-producers-smile-gif-17223449",
            "https://tenor.com/view/iu-hairflip-gif-11159215",
            "https://tenor.com/view/iu-iu-heart-%EC%95%84%EC%9D%B4%EC%9C%A0-heart-gif-18994163",
            "https://tenor.com/view/iu-badass-hotel-del-luna-jang-man-wol-gif-14912690",
            "https://tenor.com/view/iu-jang-man-wol-pensive-hotel-del-luna-drama-gif-16047677",
            "https://tenor.com/view/cute-clapping-happy-funny-fun-gif-17239556",
            "https://gfycat.com/smallshadyalbatross",
            "https://gfycat.com/linedequalgoa",
            "https://gfycat.com/knobbydelectableindiancow-wisewords-iutv",
            "https://gfycat.com/adolescentwaterygalapagosmockingbird",
            "https://tenor.com/view/iu-lee-ji-eun-gif-11126094",
            "https://tenor.com/view/%EC%97%90%EC%9E%87-%EC%9D%B4%EC%A7%80%EC%9D%80-hello-positive-vibes-iu-gif-17116417",
            "https://tenor.com/view/iuxsuga-iu-eight-%EC%9D%B4%EC%A7%80%EC%9D%80-smile-iu-gif-17116404",
            "https://tenor.com/view/iu-lee-ji-eun-kpop-korean-hae-soo-gif-16549021",
            "https://tenor.com/view/iu-lee-ji-eun-kpop-korean-pretty-gif-15906983",
            "https://tenor.com/view/iu-bbibbi-lee-jieun-pretty-beautiful-gif-15740850",
            "https://tenor.com/view/iu-laugh-cute-anniversary-jieun-gif-18576961",
            "https://tenor.com/view/iu-iu-cute-iu-blueming-iu-girl-group-iu-love-poem-gif-15592264",
            "https://tenor.com/view/iu-iu-cute-iu-blueming-iu-girl-group-iu-love-poem-gif-15592209",
            "https://tenor.com/view/iu-soda-drinks-lee-ji-eun-unnie-angel-gif-18087723",
            "https://tenor.com/view/iu-lee-ji-eun-kpop-pretty-cute-gif-17417749",
            "https://tenor.com/view/good-job-well-done-daebak-awesome-thumb-up-gif-17648286",
            "https://tenor.com/view/iu-lee-ji-eun-kpop-cute-pretty-gif-17923363",
            "https://tenor.com/view/iu-lee-ji-eun-kpop-pretty-cute-gif-17845103",
            "https://tenor.com/view/hotel-del-luna-iu-eating-chew-bite-gif-17750091",
            "https://tenor.com/view/bye-annyeong-see-ya-see-you-see-you-tomorrow-gif-17648285",
            "https://tenor.com/view/delicious-cant-stop-unstoppable-eating-again-gif-17375580",
            "https://tenor.com/view/iu-lee-ji-eun-wink-cute-pretty-gif-17535138",
            "https://tenor.com/view/iu-lee-ji-eun-kpop-pretty-cute-gif-17417717",
            "https://tenor.com/view/iu-lee-jieun-cute-cf-pout-gif-16660666",
            "https://tenor.com/view/iu-lee-jieun-kpop-pretty-cute-gif-17078417"]

        #8
        self.bot.somi_gif = ["https://tenor.com/view/jeon-somi-ioi-pout-thinking-gif-14321378",
            "https://tenor.com/view/jeon-somi-ioi-fake-smile-laugh-gif-14321383",
            "https://tenor.com/view/somi-somsom-silly-tongue-wacky-gif-9002693",
            "https://tenor.com/view/somi-vitasom-smile-happy-rwar-gif-8960237",
            "https://tenor.com/view/somi-vitasom-%EC%A0%84%EC%86%8C%EB%AF%B8-%ED%98%BC%ED%98%88-gif-8958800",
            "https://tenor.com/view/jeon-somi-ioi-stare-hmmp-hmp-gif-14321391",
            "https://tenor.com/view/jeon-so-mi-gif-8389636",
            "https://tenor.com/view/somi-jeon-somi-what-you-waiting-for-somi-comeback-somi-teaser-gif-17861737"]

        #8
        self.bot.yukika_gif = ["https://tenor.com/view/yukika-cute-yukika-cute-yukika-being-cute-gif-18862414",
            "https://tenor.com/view/yukika-japanese-soul-lady-gif-18312979",
            "https://tenor.com/view/yukika-japanese-soul-lady-gif-18313007",
            "https://tenor.com/view/yukika-mixnine-fist-gif-14017170",
            "https://tenor.com/view/yukika-wave-hello-gif-14017162",
            "https://tenor.com/view/yukika-hswcix-gif-19442465",
            "https://tenor.com/view/yukika-gif-19463874",
            "https://tenor.com/view/yukika-japanese-soul-lady-gif-18312979"]

        #



    @commands.command()
    async def natty(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Natty :teddy_bear:')
                await ctx.send(random.choice(self.bot.natty_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Natty :teddy_bear:')
            await ctx.send(random.choice(self.bot.natty_gif))
            await ctx.message.delete()

    @commands.command()
    async def alexa(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about AleXa :blue_heart:')
                await ctx.send(random.choice(self.bot.alexa_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about AleXa :blue_heart:')
            await ctx.send(random.choice(self.bot.alexa_gif))
            await ctx.message.delete()

    @commands.command()
    async def chungha(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chung Ha :heart:')
                await ctx.send(random.choice(self.bot.chungha_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Chung Ha :heart:')
            await ctx.send(random.choice(self.bot.chungha_gif))
            await ctx.message.delete()

    @commands.command()
    async def iu(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about IU <:blueming:787451831478910996>')
                await ctx.send(random.choice(self.bot.iu_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about IU <:blueming:787451831478910996>')
            await ctx.send(random.choice(self.bot.iu_gif))
            await ctx.message.delete()

    @commands.command()
    async def somi(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Somi :heart:')
                await ctx.send(random.choice(self.bot.somi_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Somi :heart:')
            await ctx.send(random.choice(self.bot.somi_gif))
            await ctx.message.delete()

    @commands.command()
    async def yukika(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yukika :heart:')
                await ctx.send(random.choice(self.bot.yukika_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yukika :heart:')
            await ctx.send(random.choice(self.bot.yukika_gif))
            await ctx.message.delete()

def setup(client):
    client.add_cog(SoloPings(client))