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
ple = 416903886968979466
mae = 492769416610840586
muffin = 488423352206229505

class IdlePings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        #7
        self.bot.minnie_gif = ["https://tenor.com/view/%EC%97%AC%EC%9E%90%EC%95%84%EC%9D%B4%EB%93%A4-minnie-%EB%AF%BC%EB%8B%88-%E7%B1%B3%E5%A6%AE-cute-gif-18186679",
            "https://tenor.com/view/minnie-gidle-ohmygod-omg-kpop-gif-18256855",
            "https://tenor.com/view/minnie-minnie-nicha-minnie-nicha-yontararak-nicha-yontararak-nicha-gif-18888803",
            "https://tenor.com/view/minnie-gidle-gif-15784676",
            "https://tenor.com/view/minnie-g-idle-nicha-yontararak-kpop-pretty-gif-16351087",
            "https://tenor.com/view/minnie-minnie-nicha-minnie-nicha-yontararak-nicha-yontararak-nicha-gif-18888791",
            "https://tenor.com/view/minnie-gidle-%EB%AF%BC%EB%8B%88-%EC%97%AC%EC%9E%90%EC%95%84%EC%9D%B4%EB%93%A4-%EC%95%84%EC%9D%B4%EB%93%A4-gif-17062450"]

        #8
        self.bot.miyeon_gif = ["https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-18962243",
            "https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-18962348",
            "https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-18962294",
            "https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-18962324",
            "https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-18962177",
            "https://tenor.com/view/miyeon-miyeon-gidle-cho-miyeon-gif-18403777",
            "https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-18962317",
            "https://tenor.com/view/miyeon-cho-miyeon-jo-miyeon-gidle-idle-gif-18962152"]

        #9
        self.bot.shuhua_gif = ["https://tenor.com/view/pop-taiwanese-kpop-yehshuhua-selfdefense-gif-18118582",
            "https://tenor.com/view/gidle-shuhua-%ec%97%ac%ec%9e%90%ec%95%84%ec%9d%b4%eb%93%a4-%ec%95%84%ec%9d%b4%eb%93%a4-%ec%8a%88%ed%99%94-gif-16949157",
            "https://tenor.com/view/shuhua-idle-gidle-yeh-shu-hua-cube-entertainment-gif-16929431",
            "https://tenor.com/view/glasses-shuhua-idle-yeh-gidle-gif-13052094",
            "https://tenor.com/view/yeh-shu-hua-gidle-heart-love-gif-13052095",
            "https://tenor.com/view/kpop-shuhua-gidle-pretty-gif-14904506",
            "https://tenor.com/view/shuhua-kpop-gif-18740565",
            "https://tenor.com/view/%E8%88%92%E8%8F%AF-gidle-%EC%8A%88%ED%99%94-shuhua-wave-gif-16738706",
            "https://tenor.com/view/shuhua-yeh-shuhua-shuhua-gidle-shuhua-idle-gidle-gif-19200395"]

        #8
        self.bot.soojin_gif = ["https://tenor.com/view/soojin-gif-18250849",
            "https://tenor.com/view/gidle-soojin-seo-soojin-idle-gif-15287479",
            "https://tenor.com/view/soojin-gidle-wink-gif-13805713",
            "https://tenor.com/view/soojin-seo-soojin-gidle-idle-soojin-gidle-gif-18888703",
            "https://tenor.com/view/soojin-gif-18526389",
            "https://tenor.com/view/soojin-seo-soojin-gidle-idle-sujin-gif-18866361",
            "https://tenor.com/view/soojin-soojin-gidle-gif-18404859",
            "https://tenor.com/view/soojin-gif-19272378"]

        #32
        self.bot.soyeon_gif = ["https://tenor.com/view/soyeon-jeon-gif-19050110",
            "https://tenor.com/view/soyeon-jeon-soyeon-gidle-idle-soyeon-gidle-gif-18962551",
            "https://tenor.com/view/soyeon-jeon-soyeon-gidle-idle-soyeon-gidle-gif-18962536",
            "https://tenor.com/view/soyeon-jeon-soyeon-soyeon-gidle-soyeon-idle-gidle-gif-19200289",
            "https://tenor.com/view/idle-soyeon-g-idle-soyeon-jeon-soyeon-soyeon-cute-gif-16629896",
            "https://tenor.com/view/soyeon-jeon-soyeon-gidle-idle-soyeon-gidle-gif-18962545",
            "https://tenor.com/view/soyeon-jeon-soyeon-gidle-idle-soyeon-gidle-gif-18962456",
            "https://giphy.com/gifs/GIDLE-gidle-gi-dle-dumdi-ihLlzoKG2gdOV718GN",
            "https://tenor.com/view/soyeon-jeon-gif-19050106",
            "https://tenor.com/view/jeon-soyeon-gif-19180116",
            "https://tenor.com/view/soyeon-jeon-gidle-gif-19180104",
            "https://tenor.com/view/jeon-soyeon-gif-19180115",
            "https://tenor.com/view/soyeon-jeon-soyeon-gidle-unpretty-rapstars3-smile-gif-15122585",
            "https://tenor.com/view/soyeon-senorita-g-idle-cute-kpop-kpop-girl-group-gif-15338342",
            "https://tenor.com/view/kcon2019thailand-kcon2019th-kcon2019-kcon-%EC%BC%80%EC%9D%B4%EC%BD%98-gif-15500055",
            "https://tenor.com/view/wow-thing-soyeon-soyeon-rap-gif-15842099",
            "https://tenor.com/view/gidle-soyeon-gidle-han-soyeon-kpop-han-mma-gif-17953864",
            "https://tenor.com/view/soyeon-soy-gidle-gif-19050069",
            "https://tenor.com/view/soyeon-jelly-baloon-g-idle-soyeon-jeon-soyeon-kpop-gif-17901528",
            "https://tenor.com/view/dancing-gidle-soyeon-cosmopolitan-dance-moves-gif-18221991",
            "https://tenor.com/view/soyeon-soyeon-gidle-soyeon-idle-gidle-idle-gif-18962475",
            "https://tenor.com/view/soyeon-soyeon-gidle-soyeon-idle-gidle-idle-gif-18962486",
            "https://tenor.com/view/soyeon-soy-gif-19050109",
            "https://tenor.com/view/soyeon-gidle-ohmygod-kpop-omg-gif-18312959",
            "https://tenor.com/view/g-idle-soyeon-jeon-soyeon-kpop-cute-gif-15859587",
            "https://tenor.com/view/g-idle-soyeon-jeon-soyeon-kpop-cute-gif-17901589",
            "https://tenor.com/view/soyeon-jeon-soyeon-gidle-idle-soyeon-gidle-gif-18962437",
            "https://tenor.com/view/gidle-gidle-lion-soyeon-gif-15722063",
            "https://tenor.com/view/soyeon-jeon-soyeon-soyeon-gidle-soyeon-idle-gidle-gif-19200276",
            "https://tenor.com/view/soyeon-jeon-soyeon-soyeon-gidle-soyeon-idle-gidle-gif-19200299",
            "https://tenor.com/view/soyeon-jeon-soyeon-gidle-idle-soyeon-gidle-gif-18962542",
            "https://tenor.com/view/soyeon-kda-the-baddest-gif-18262396"]

        #9
        self.bot.yuqi_gif = ["https://tenor.com/view/%EC%95%84%EC%9D%B4%EB%93%A4-%EC%9A%B0%EA%B8%B0-%EC%97%AC%EC%9E%90%EC%95%84%EC%9D%B4%EB%93%A4-g-idle-yuqi-gif-16254335",
            "https://tenor.com/view/yuqi-heart-cute-gif-13344124",
            "https://tenor.com/view/yuqi-song-yuqi-smile-eyes-cute-gif-17354259",
            "https://tenor.com/view/gidle-yuqi-mishuqi-wink-gif-17988600",
            "https://tenor.com/view/yuqi-dog-lover-cute-gif-13943997",
            "https://tenor.com/view/song-yuqi-yuqi-oh-my-god-gidle-ending-fairy-gif-17354516",
            "https://tenor.com/view/yuqi-yuqifancam-yuqigidle-cute-smile-gif-12588694",
            "https://tenor.com/view/g-idle-yuqi-song-yuqi-chinese-singer-pretty-gif-17257186",
            "https://tenor.com/view/kpop-g-idle-yuqi-uwu-oof-gif-12719365"]

    @commands.command()
    async def minnie(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{ple}>, <@!{ctx.author.id}> is talking about Minnie :heart:')
                await ctx.send(random.choice(self.bot.minnie_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Minnie :heart:')
            await ctx.send(random.choice(self.bot.minnie_gif))
            await ctx.message.delete()

    @commands.command()
    async def miyeon(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{ple}>, <@!{ctx.author.id}> is talking about Miyeon :heart:')
                await ctx.send(random.choice(self.bot.miyeon_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Miyeon :heart:')
            await ctx.send(random.choice(self.bot.miyeon_gif))
            await ctx.message.delete()

    @commands.command()
    async def shuhua(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{ple}>, <@!{ctx.author.id}> is talking about Shuhua :heart:')
                await ctx.send(random.choice(self.bot.shuhua_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Shuhua :heart:')
            await ctx.send(random.choice(self.bot.shuhua_gif))
            await ctx.message.delete()

    @commands.command()
    async def soojin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{ple}>, <@!{ctx.author.id}> is talking about Soojin :heart:')
                await ctx.send(random.choice(self.bot.soojin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Soojin :heart:')
            await ctx.send(random.choice(self.bot.soojin_gif))
            await ctx.message.delete()

    @commands.command()
    async def soyeon(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@{ple}>, <@!{ctx.author.id}> is talking about Soyeon :lollipop:')
                await ctx.send(random.choice(self.bot.soyeon_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Soyeon :lollipop:')
            await ctx.send(random.choice(self.bot.soyeon_gif))
            await ctx.message.delete()    

    @commands.command()
    async def yuqi(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{ple}>, <@!{ctx.author.id}> is talking about Yuqi :heart:')
                await ctx.send(random.choice(self.bot.yuqi_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yuqi :heart:')
            await ctx.send(random.choice(self.bot.yuqi_gif))
            await ctx.message.delete()

def setup(client):
    client.add_cog(IdlePings(client))