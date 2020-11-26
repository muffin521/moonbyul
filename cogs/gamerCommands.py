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

        self.dream_gif = ["https://tenor.com/view/dream-george-not-found-sapnap-speedrunning-manhunt-gif-18187566",
            "https://tenor.com/view/minecraft-dream-gif-18394858",
            "https://tenor.com/view/popipo-dream-scrundy-pundy-technoblade-sapnap-gif-18226411",
            "https://tenor.com/view/dream-dreamwastaken-minecraft-desert-dance-gif-18987175",
            "https://tenor.com/view/dream-dreamwastaken-minecraft-gif-18176440",
            "https://tenor.com/view/dream-team-minecraft-love-dream-sapnap-gif-18710509"]

        self.food_gif = ["https://gfycat.com/uncomfortablesafebarbet",
            "https://tenor.com/view/jenniekim-gif-18818029",
            "https://tenor.com/view/tipton2109-nct-nct-mark-mark-lee-regular-gif-13173755",
            "https://tenor.com/view/sakura-miyawaki-sakura-izone-%E3%81%95%E3%81%8F%E3%82%89-%E5%AE%AE%E8%84%87%E5%92%B2%E8%89%AF-gif-14974458",
            "https://tenor.com/view/jisoo-food-blackpink-kpop-eating-gif-9473818",
            "https://tenor.com/view/hwasa-lollipop-kpop-be-calm-beautiful-day-gif-18873828",
            "https://tenor.com/view/lalisa-manoban-lisa-blackpink-lollipop-kpop-gif-17772815",
            "https://tenor.com/view/seulgi-kang-seulgi-red-velvet-cute-bear-gif-16728717",
            "https://tenor.com/view/wheein-mamamoo-eating-eggs-eating-egg-idol-gif-18928054",
            "https://tenor.com/view/mamamoo-hwasa-ahn-hye-jin-vocalist-rapper-gif-17583679",
            "https://tenor.com/view/hwasa-eat-eating-ramen-hot-gif-12261725",
            "https://tenor.com/view/mamamoo-solar-eating-pole-bibimbap-gif-16227163",
            "https://tenor.com/view/izone-hyewon-eating-gif-13780770",
            "https://tenor.com/view/chou-tzuyu-kpop-gif-11360919",
            "https://tenor.com/view/toosie-slide-cute-eat-jennie-jennie-kim-gif-16780128",
            "https://media.giphy.com/media/disxZ6CKe4b9wbFhhT/giphy.gif",
            "https://tenor.com/view/mamamoo-wheein-strawberry-yum-gif-7596438",
            "https://tenor.com/view/jo-yuri-yuri-iz-one-cute-eating-gif-14800422",
            "https://gfycat.com/miserableslipperygartersnake",
            "https://gfycat.com/aridpitifulchipmunk",
            "https://gfycat.com/zealousunsightlyhumpbackwhale",
            "https://gfycat.com/vaguefreshflickertailsquirrel",
            "https://tenor.com/view/mark-mark-lee-nct-cold-eating-gif-14683790",
            "https://gfycat.com/unconsciousweirdfishingcat",
            "https://tenor.com/view/yeeun-jang-clc-not-yummy-gif-13252749",
            "https://tenor.com/view/yum-delicious-cheng-xiao-yummy-gif-12031986",
            "https://gfycat.com/flamboyantunlinedisabellinewheatear",
            "https://gfycat.com/limpingunrulygrasshopper",
            "https://gfycat.com/sentimentalmadeupgrayfox"]

        self.chuuheart_gif = ["https://static.apester.com/user-images/cb/cb60802a9e5ff8aa501df36ddfa56cce.gif",
            "https://tenor.com/view/mamamoo-wheein-heart-kpop-dance-gif-16331749",
            "https://tenor.com/view/kpop-loona-chuu-heart-love-gif-18586088",
            "https://tenor.com/view/chuu-loona-hamburguer-heart-heart-untitled127-gif-13827374",
            "https://tenor.com/view/chuu-loona-chuu-loona-cute-kpop-gif-16242378",
            "https://media.discordapp.net/attachments/758500230386679848/775129870559870976/ezgif-7-864231320452.gif",
            "https://tenor.com/view/seulgi-kang-seulgi-red-velvet-cute-pretty-gif-16937522",
            "https://tenor.com/view/wendy-shon-son-seungwan-red-velvet-%ec%9b%ac%eb%94%94-%eb%a0%88%eb%93%9c%eb%b2%a8%eb%b2%b3-gif-16069063",
            "https://tenor.com/view/yoona-im-yoona-%ec%9c%a4%ec%95%84-snsd-girls-generation-gif-14170845",
            "https://tenor.com/view/heart-love-apple-heart-chuu-heart-da-vinki-gif-18549840",
            "https://tenor.com/view/sakura-izone-sakura-miyawaki-sakura-saku-chan-chaekura-kkura-gif-13532539",
            "https://cdn.discordapp.com/attachments/704248706269970488/776652835617898516/image0.gif",
            "https://tenor.com/view/yeeun-jang-yeeun-cute-clc-kpop-gif-17883335",
            "https://tenor.com/view/g-idle-yuqi-song-yuqi-kpop-cute-gif-17667093"]

        self.monke = ["https://www.youtube.com/watch?v=PipzizkF-SY",
            "https://www.youtube.com/watch?v=-JUhUI_KvUI",
            "https://www.youtube.com/watch?v=05sJVEwZuZ4",
            "https://www.youtube.com/watch?v=2EKKMof_Ywg"]

    @commands.command()
    async def dream(self, ctx):
        if ctx.guild.id == jst:
            await ctx.send(f'<@150742733743587328>, <@!{ctx.author.id}> is talking about Dream :cactus:')
            await ctx.send(random.choice(self.dream_gif))
            await ctx.message.delete()

    @commands.command()
    async def food(self, ctx):
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to #bot-commands', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'Aster is the best :smiling_face_with_3_hearts:')
            await ctx.send(random.choice(self.food_gif))
            await ctx.message.delete()

    @commands.command(aliases = ['nyam'])
    async def chuuheart(self, ctx):
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to #bot-commands', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx. send(f'nyam')
            await ctx.send(random.choice(self.chuuheart_gif))
            await ctx.message.delete()

    @commands.command()
    async def screm(self, ctx):
        await ctx.send('https://tenor.com/view/loona-loona-hyunjin-hyunjin-kim-hyunjin-loona-aeong-gif-18902504')
        await ctx.message.delete()

    @commands.command()
    async def rahul(self, ctx):
        if ctx.guild.id == jst:
            await ctx.send(f'<@579636764889841665> monke ' + random.choice(self.monke))
            await ctx.message.delete()

    @commands.command()
    async def weakado(self, ctx):
        if ctx.guild.id == jst:
            await ctx.send(f'<@259409277482041344> fiesta good \nhttps://www.youtube.com/watch?v=eDEFolvLn0A')
            await ctx.message.delete()

    @commands.command()
    async def veery(self,ctx):
        await ctx.send(f'https://cdn.discordapp.com/attachments/735713250989309984/779101391871934484/veery_good.mp3')
        await ctx.message.delete()

    @commands.command()
    async def sex(self, ctx):
        if ctx.guild.id == jst:
            await ctx. send(f'https://www.youtube.com/watch?v=VfCYZ3pks48&list=FLFkJiNcjfwfDWZMEHJ1C_Ew&index=522')
            await ctx.message.delete()

    @commands.command()
    async def ren(self, ctx):
        await ctx.send(f'I love you <@749085760354910280>')

    @commands.command()
    async def muffin(self, ctx):
        await ctx.send(f'<@!{ctx.author.id}> :heart: you <@488423352206229505>')

def setup(client):
    client.add_cog(gamerPings(client))