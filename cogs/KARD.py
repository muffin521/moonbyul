import discord, random
from discord.ext import commands
from discord.utils import get
from datetime import datetime

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

#//people


class KARD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.kard_bm_gif = ["https://tenor.com/view/kard-kpop-ccg-ccg1-bm-gif-19146457",
            "https://tenor.com/view/kard-kpop-ccg-ccg1-bm-gif-19146414",
            "https://tenor.com/view/ohnana-bm-kard-kpop-gif-9172986",
            "https://tenor.com/view/bm-matthew-kim-kard-kpop-handsome-gif-17826839",
            "https://tenor.com/view/bm-kard-dance-gif-15197862",
            "https://tenor.com/view/kpop-ccg-ccg1-hwaiting-matthew-kim-gif-18337564",
            "https://tenor.com/view/kiss-kard-bm-big-matthew-matthew-kim-gif-16327222",
            "https://tenor.com/view/kard-bm-big-matthew-dance-gif-19503235",
            "https://cdn.discordapp.com/attachments/382901350259884042/471623935620939776/Animated_GIF-downsized_large_6.gif",
            "https://cdn.discordapp.com/attachments/382901350259884042/471617958674956289/Animated_GIF-downsized_large_1.gif",
            "https://pa1.narvii.com/6352/b0957fad5e9691b2228462b99e3911eb511ffe39_hq.gif",
            "https://cdn.discordapp.com/attachments/382901350259884042/382906404543135745/2017-11-21_11-57-29.gif"]

        self.bot.kard_jiwoo_gif = ["https://tenor.com/view/jiwoo-k-pop-gif-11761625",
            "https://tenor.com/view/jiwoo-gif-18078369",
            "https://tenor.com/view/jiwoo-gif-18078383",
            "https://tenor.com/view/kard-kpop-ccg-ccg1-jeon-jiwoo-gif-19146480",
            "https://tenor.com/view/jiwoo-shocked-kard-gif-9442607",
            "https://tenor.com/view/kard-jiwoo-gif-18474024",
            "https://tenor.com/view/jiwoo-k-pop-gif-11761601",
            "https://tenor.com/view/jiwoo-gif-18078543",
            "https://tenor.com/view/jiwoo-gif-18473996",
            "https://tenor.com/view/jiwoo-kard-kpop-sassy-cute-gif-17779099",
            "https://tenor.com/view/jiwoo-k-pop-gif-11761603",
            "https://tenor.com/view/jiwoo-gif-18107781",
            "https://tenor.com/view/kard-beauty-kpop-jiwoo-pretty-gif-16768165",
            "https://tenor.com/view/jiwoo-gif-18099256",
            "https://tenor.com/view/kard-jiwoo-gif-18204638",
            "https://tenor.com/view/kard-gunshot-jiwoo-gif-18474032"]

        self.bot.kard_jseph_gif = ["https://tenor.com/view/kard-kpop-ccg-ccg1-jseph-gif-19146442",
            "https://tenor.com/view/jseph-smile-kard-k-pop-gif-9866990",
            "https://tenor.com/view/j-seph-south-korean-singer-cute-handsome-gif-17875196",
            "https://tenor.com/view/taehyung-kard-jseph-kpop-gif-8375366",
            "https://cdn.discordapp.com/attachments/382901350259884042/383984172752175104/2017-11-25_15-15-02.gif"]

        self.bot.kard_somin_gif = ["https://tenor.com/view/kard-somin-kpop-red-moon-music-video-gif-16319282",
            "https://cdn.discordapp.com/attachments/382901350259884042/471619517827645441/Animated_GIF-downsized_large_3.gif",
            "https://tenor.com/view/somin-sominkard-kard-jiwoo-jiwookard-gif-18137244",
            "https://tenor.com/view/somin-kard-jiwoo-jseph-bm-gif-18137575",
            "https://tenor.com/view/somin-kard-jiwoo-jseph-bm-gif-18137587",
            "https://tenor.com/view/kard-red-moon-somin-kpop-cute-gif-16399002",
            "https://tenor.com/view/somin-kard-sominkard-kardsomin-jiwookard-gif-18137246",
            "https://tenor.com/view/somin-kard-gif-18981833",
            "https://tenor.com/view/heart-kard-somin-gif-18981834",
            "https://tenor.com/view/somin-kard-gif-18981832",
            "https://tenor.com/view/kard-somin-sexy-kpop-fierce-gif-17092003",
            "https://tenor.com/view/jiwoo-somin-bm-kard-jseph-gif-7485227",
            "https://tenor.com/view/kard-somin-bomb-bomb-gif-19500984",
            "https://tenor.com/view/kard-somin-kpop-sexy-fierce-gif-17092000",
            "https://tenor.com/view/somin-kard-jiwoo-jseph-bm-gif-18137566",
            "https://tenor.com/view/kard-somin-jeon-somin-somin-kard-kpop-gif-19503161",
            "https://tenor.com/view/kard-somin-bomb-bomb-kard-somin-gif-19500991",
            "https://tenor.com/view/kard-somin-bomb-bomb-somin-bomb-bomb-kard-somin-bomb-bomb-gif-19501016",
            "https://tenor.com/view/kard-somin-sexy-kpop-fierce-gif-17092002",
            "https://tenor.com/view/kard-somin-bomb-bomb-bomb-bomb-kard-somin-somin-bomb-bomb-kard-bomb-bomb-gif-19501026",
            "https://cdn.discordapp.com/attachments/382901350259884042/382906404543135745/2017-11-21_11-57-29.gif"]

    @commands.command(aliases = ["k.a.r.d"])
    async def kard(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [KARD {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if ctx.channel.id != kbotcom and ctx.guild.id == luminary:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            if arg == "bm":
                await ctx.send(f'<@!{ctx.author.id}> is talking about BM :heart: ')
                await ctx.send(random.choice(self.bot.kard_bm_gif))
                await ctx.message.delete()
            elif arg == "jiwoo":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jiwoo :heart: ')
                await ctx.send(random.choice(self.bot.kard_jiwoo_gif))
                await ctx.message.delete()
            elif arg == "jseph" or arg == "j.seph":
                await ctx.send(f'<@!{ctx.author.id}> is talking about J.Seph :heart: ')
                await ctx.send(random.choice(self.bot.kard_jseph_gif))
                await ctx.message.delete()
            elif arg == "somin":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Somin :heart: ')
                await ctx.send(random.choice(self.bot.kard_somin_gif))
                await ctx.message.delete()

def setup(client):
    client.add_cog(KARD(client))