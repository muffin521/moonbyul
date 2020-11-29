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

        #10
        self.chungha_gif = ["https://tenor.com/view/kiss-love-chunga-korean-gif-11126096",
            "https://tenor.com/view/chungha-gif-18541917",
            "https://tenor.com/view/chungha-stare-smokey-eyes-gif-14390425",
            "https://tenor.com/view/chungha-gif-14681679",
            "https://tenor.com/view/kim-chungha-chungha-cute-smile-gif-13261337",
            "https://tenor.com/view/kim-chungha-chungha-cute-gorgeous-smile-gif-12547851",
            "https://tenor.com/view/kim-chungha-chungha-wink-sexy-gif-12547847",
            "https://tenor.com/view/chungha-kim-chungha-kpop-pretty-cute-gif-16653910",
            "https://tenor.com/view/rae-chungha-fancam-play-kpop-gif-18963908",
            "https://tenor.com/view/chungha-kim-chungha-kpop-cute-pretty-gif-16521270"]

    #natty command
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

    #alexa command
    @commands.command()
    async def alexa(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about AleXa :blue_heart:')
                await ctx.send(random.choice(self.alexa_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about AleXa :blue_heart:')
            await ctx.send(random.choice(self.alexa_gif))
            await ctx.message.delete()

    #chung ha command
    @commands.command()
    async def chungha(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chung Ha :heart:')
                await ctx.send(random.choice(self.chungha_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Chung Ha :heart:')
            await ctx.send(random.choice(self.chungha_gif))
            await ctx.message.delete()


def setup(client):
    client.add_cog(SoloPings(client))