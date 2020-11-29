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

class ItzyPings(commands.Cog):

    def __init__(self, client):
        self.client = client

        #7
        self.yeji_gif = ["https://tenor.com/view/yeji-itzy-jyp-entertainment-kpop-cute-gif-16653975",
            "https://tenor.com/view/yeji-yeji-itzy-hwang-yeji-gif-18718150",
            "https://tenor.com/view/yeji-hwang-yeji-itzy-wink-salute-gif-17307566",
            "https://tenor.com/view/yeji-itzy-jyp-entertainment-kpop-cute-gif-16653970",
            "https://tenor.com/view/hwang-yeji-yeji-itzy-jyp-entertainment-kpop-gif-16652420",
            "https://tenor.com/view/kpop-itzy-yeji-cute-icy-gif-14653975",
            "https://tenor.com/view/itzy-yeji-itzy-yeji-hwang-yeji-kpop-gif-18379032"]

        #8
        self.ryunjin_gif = ["https://tenor.com/view/ryujin-%EB%A5%98%EC%A7%84-itzy-shinryujin-gif-14922418",
            "https://tenor.com/view/ryujin-dance-moves-shake-it-pretty-gif-16723839",
            "https://tenor.com/view/ryujin-itzy-blow-kiss-shinryujin-gif-14437581",
            "https://tenor.com/view/itzy-ryujin-shin-ryujin-kpop-pretty-gif-15639935",
            "https://tenor.com/view/ryujin-itzy-shin-ryujin-kpop-cute-gif-16653996",
            "https://tenor.com/view/itzy-ryujin-gif-18137656",
            "https://tenor.com/view/itzy-jyp-entertainment-shin-ryujin-ryujin-main-rapper-gif-16721301",
            "https://tenor.com/view/ryujin-itzy-gif-18835542"]

        #7
        self.chaeryeong_gif = ["https://tenor.com/view/itzy-chaeryeong-chaer-kpop-wannabe-gif-16689232",
            "https://tenor.com/view/chaeryeong-chaeryeong-itzy-lee-chaeryeong-gif-18568144",
            "https://tenor.com/view/chaeryeong-chaeryeong-itzy-itzy-gif-18553550",
            "https://tenor.com/view/chaeryeong-chaeryeong-itzy-itzy-chaeryeong-itzy-lee-chaeryeong-gif-13767624",
            "https://tenor.com/view/chaeryeong-chaeryeong-itzy-lee-chaeryeong-gif-18743380",
            "https://tenor.com/view/chaeryeong-chaeryeong-itzy-lee-chaeryeong-gif-18909774",
            "https://tenor.com/view/chaeryeong-chaeryeong-itzy-lee-chaeryeong-not-shy-gif-18568206"]

        #7
        self.yuna_gif = ["https://tenor.com/view/yuna-yuna-itzy-itzy-yuna-shin-yuna-itzy-gif-13910454",
            "https://tenor.com/view/yuna-yuna-itzy-shin-yuna-gif-18719264",
            "https://tenor.com/view/yuna-shin-yuna-yuna-itzy-itzy-yuna-itzy-gif-13835000",
            "https://tenor.com/view/yuna-yuna-itzy-shin-yuna-gif-18829861",
            "https://tenor.com/view/yuna-shin-yuna-yuna-shin-gif-18387313",
            "https://tenor.com/view/itzy-yuna-gif-19088943",
            "https://tenor.com/view/yuna-gif-18390135"]

        #7
        self.lia_gif = ["https://tenor.com/view/kpop-lia-strawberry-itzy-cute-gif-16770693",
            "https://tenor.com/view/lia-liaitzy-itzylia-itzy-gif-18066742",
            "https://tenor.com/view/lia-itzy-choi-jisu-pretty-model-gif-17200845",
            "https://tenor.com/view/itzy-lia-itzy-lia-kpop-cute-gif-17092840",
            "https://tenor.com/view/lia-liaitzy-itzylia-itzy-gif-18066804",
            "https://tenor.com/view/itzy-itzy-lia-lia-%EB%A6%AC%EC%95%84-%EC%9E%88%EC%A7%80-gif-18073067",
            "https://tenor.com/view/liaitzy-itzy-lia-gif-18066766"]

    @commands.command()
    async def yeji(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yeji :heart:')
                await ctx.send(random.choice(self.yeji_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yeji :heart:')
            await ctx.send(random.choice(self.yeji_gif))
            await ctx.message.delete()

    @commands.command()
    async def ryujin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Ryunjin :heart:')
                await ctx.send(random.choice(self.ryunjin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Ryunjin :heart:')
            await ctx.send(random.choice(self.ryunjin_gif))
            await ctx.message.delete()

    @commands.command()
    async def chaeryeong(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chaeryeong :heart:')
                await ctx.send(random.choice(self.chaeryeong_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Chaeryeong :heart:')
            await ctx.send(random.choice(self.chaeryeong_gif))
            await ctx.message.delete()

    @commands.command()
    async def yuna(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yuna :heart:')
                await ctx.send(random.choice(self.yuna_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yuna :heart:')
            await ctx.send(random.choice(self.yuna_gif))
            await ctx.message.delete()

    @commands.command()
    async def lia(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Lia :heart:')
                await ctx.send(random.choice(self.lia_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Lia :heart:')
            await ctx.send(random.choice(self.lia_gif))
            await ctx.message.delete()


def setup(client):
    client.add_cog(ItzyPings(client))