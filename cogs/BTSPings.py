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

    def __init__(self, bot):
        self.bot = bot

        self.bot.v_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781374550419439626/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374550906503188/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374551534600212/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374552059543592/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374552461934622/image4.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374552924094494/image5.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374553388613632/image6.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374553905168405/image7.gif",
            "https://tenor.com/view/kim-taehyung-taehyung-bts-bts-v-hot-gif-14822919",
            "https://tenor.com/view/bts-done-taehyung-tired-sleepy-gif-16117979",
            "https://tenor.com/view/taehyung-kim-taehyung-smile-tae-gucci-boy-gif-16369645",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-v-kim-taehyung-gif-17104113",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-v-kim-taehyung-gif-16658106",
            "https://tenor.com/view/taehyung-kpop-oppa-cute-smile-gif-8626038",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-v-kim-taehyung-gif-16993427",
            "https://tenor.com/view/taehyung-bts-cute-handsome-looking-gif-16986526",
            "https://tenor.com/view/taehyung-peace-cute-gif-19086526",
            "https://tenor.com/view/taehyung-kim-taehyung-tae-tae-tae-vante-gif-18345939"]

        self.bot.suga_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781376996051517460/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376997473255434/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376998244483112/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376998852788224/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377281868300318/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377282270035987/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377283252158484/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377284031905842/image3.gif",
            "https://tenor.com/view/bts-suga-kpop-uwu-big-baby-boi-gif-12988023",
            "https://tenor.com/view/bts-suga-cute-smile-kpop-gif-13230684",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-suga-suga-gif-17096216",
            "https://tenor.com/view/bts-suga-laugh-smile-gif-14696728",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-suga-suga-gif-9734489",
            "https://tenor.com/view/bts-suga-kpop-cute-smirk-gif-6231660",
            "https://tenor.com/view/haha-yoongi-nod-gif-12218918",
            "https://tenor.com/view/bts-nod-cheeks-cute-yoongi-gif-14760712",
            "https://tenor.com/view/bts-min-yoongi-run-gif-13961845",
            "https://tenor.com/view/bts-beautiful-shy-blush-teeth-gif-19573947",
            "https://tenor.com/view/yoongi-sad-cute-face-gif-19211545",
            "https://tenor.com/view/bts-yoongi-smile-gif-15454873",
            "https://tenor.com/view/bts-yoongi-funny-gif-14760711"]

        self.bot.jhope_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781376181487796224/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376182888431616/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376183551918090/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376184256430100/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376185291767838/image4.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376186805649408/image5.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376187368472626/image6.gif",
            "https://tenor.com/view/jhope-bts-gif-12584763",
            "https://tenor.com/view/bts-jhope-hoseok-jung-gif-14371797",
            "https://tenor.com/view/jhope-hobi-yes-hoseok-gif-16178897",
            "https://tenor.com/view/jhope-jhopebts-btsjhope-hobi-bts-gif-18149405",
            "https://tenor.com/view/jhope-heart-%EB%B0%A9%ED%83%84-%EC%A0%9C%EC%9D%B4%ED%99%89-%EB%B0%A9%ED%83%84%EC%86%8C%EB%85%84%EB%8B%A8-gif-10577474",
            "https://tenor.com/view/jhope-stare-serious-gif-12853415"]

        #9
        self.bot.jungkook_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781375454966972426/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375486843551775/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375522592129024/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375594725376000/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375595178491904/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375596798279710/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375705270583306/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375706437255178/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375707854012416/image2.gif"]

        #12
        self.bot.btsjin_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781378238282727464/image0.gif",
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
        self.bot.jimin_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781377634956345383/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377635636609044/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377636190519296/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377637137645578/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377637863391262/image4.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377786698661888/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377787608301568/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377788585181184/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377789689200640/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377790510760006/image4.gif"]

        self.bot.rm_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781374090497753098/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374226607112252/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374227605225482/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374228132790323/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374228456275968/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374229014511646/image4.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374229836333086/image5.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374230364160030/image6.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374230952411136/image7.gif",
            "https://tenor.com/view/namjoon-bts-bangtan-boys-bangtan-sonyeondan-kpop-gif-12559453",
            "https://tenor.com/view/namjoon-kim-namjoon-rm-joonie-gif-18400460",
            "https://tenor.com/view/rap-monster-kpop-bts-heart-silly-gif-8137935",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-rap-monster-kim-namjoon-gif-17774036",
            "https://tenor.com/view/namjoon-rm-kim-namjoon-joonie-smile-gif-18345522",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-rap-monster-kim-namjoon-gif-17848085",
            "https://tenor.com/view/bts-rm-kpop-smile-namjoon-gif-16911179",
            "https://tenor.com/view/bts-nam-joon-rap-monster-gif-9813314",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-rap-monster-kim-namjoon-gif-17848254",
            "https://tenor.com/view/bts-rm-namjoon-gif-18205004",
            "https://tenor.com/view/bts-kim-nam-joon-aesthetic-rm-gif-15168245",
            "https://tenor.com/view/namjoon-bts-kpop-walk-gif-12559450",
            "https://tenor.com/view/kim-namjoon-bts-rm-laugh-lol-gif-10964941",
            "https://tenor.com/view/bts-heart-rm-cute-namjoon-gif-13444506"]

    @commands.command()
    async def v(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about V :heart:')
                await ctx.send(random.choice(self.bot.v_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about V :heart:')
            await ctx.send(random.choice(self.bot.v_gif))
            await ctx.message.delete()

    @commands.command()
    async def suga(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Suga :heart:')
                await ctx.send(random.choice(self.bot.suga_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Suga :heart:')
            await ctx.send(random.choice(self.bot.suga_gif))
            await ctx.message.delete()

    @commands.command(aliases = ['j-hope'])
    async def jhope(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about J-Hope :heart:')
                await ctx.send(random.choice(self.bot.jhope_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about J-Hope :heart:')
            await ctx.send(random.choice(self.bot.jhope_gif))
            await ctx.message.delete()

    @commands.command()
    async def jungkook(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jungkook :heart:')
                await ctx.send(random.choice(self.bot.jungkook_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jungkook :heart:')
            await ctx.send(random.choice(self.bot.jungkook_gif))
            await ctx.message.delete()

    @commands.command()
    async def jin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jin :heart:')
                await ctx.send(random.choice(self.bot.btsjin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jin :heart:')
            await ctx.send(random.choice(self.bot.btsjin_gif))
            await ctx.message.delete()

    @commands.command()
    async def jimin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jimin :heart:')
                await ctx.send(random.choice(self.bot.jimin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jimin :heart:')
            await ctx.send(random.choice(self.bot.jimin_gif))
            await ctx.message.delete()

    @commands.command(aliases = ['namjoon'])
    async def rm(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about RM :heart:')
                await ctx.send(random.choice(self.bot.rm_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about RM :heart:')
            await ctx.send(random.choice(self.bot.rm_gif))
            await ctx.message.delete()

def setup(client):
    client.add_cog(BTSPings(client))