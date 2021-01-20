import discord, random
from discord.ext import commands
from datetime import datetime

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.logs
logs = 786515662214397973
#.luminary bot-commands
kbotcom = 764610881513324574

#//people
weakado = 259409277482041344

class everglow(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

        self.bot.eu_gif = ["https://tenor.com/view/eu-everglow-gif-18228811",
            "https://tenor.com/view/everglow-cute-aesthetic-kpop-gif-19189917",
            "https://tenor.com/view/everglow-eu-cute-gif-18070457",
            "https://tenor.com/view/everglow-eu-park-jiwon-leader-kpop-gif-16259144",
            "https://tenor.com/view/eu-everglow-gif-18601722",
            "https://tenor.com/view/eu-everglow-gif-18228815",
            "https://tenor.com/view/eu-everglow-gif-18891279",
            "https://tenor.com/view/everglow-eu-par-jiwon-leader-kpop-gif-16227322",
            "https://tenor.com/view/everglow-kpop-pretty-cute-beautiful-gif-15571693"]

        self.bot.mia_gif = ["https://tenor.com/view/everglow-mia-blow-kiss-kpop-cute-gif-15818623",
            "https://tenor.com/view/everglowmia-salute-gif-18117807",
            "https://tenor.com/view/everglow-mia-pretty-photoshoot-kpop-gif-15789180",
            "https://tenor.com/view/ginkoro-gif-17994290",
            "https://tenor.com/view/mia-everglow-pretty-windy-kpop-gif-16262724",
            "https://tenor.com/view/everglow-kpop-pretty-beautiful-cute-gif-15571739",
            "https://tenor.com/view/mia-everglow-kpop-kpop-girl-group-kpop-singer-gif-15341399",
            "https://tenor.com/view/everglow-kpop-cute-pretty-beautiful-gif-15562411",
            "https://tenor.com/view/everglow-dance-cute-smile-mic-gif-15070516",
            "https://tenor.com/view/everglow-mia-smile-gif-18564778",
            "https://tenor.com/view/mia-everglow-gif-18670931"]

        self.bot.yiren_gif = ["https://tenor.com/view/yireon-hearts-wishing-wish-produce48-gif-11924127",
            "https://tenor.com/view/love-you-more-wink-side-eye-flirt-smile-gif-16944406",
            "https://tenor.com/view/%E7%8E%8B%E6%80%A1%E4%BA%BAwang-yiren-cute-kpop-smile-gif-16236336",
            "https://tenor.com/view/wang-yiren-everglow-kpop-cute-sad-gif-16526333",
            "https://tenor.com/view/everglow-yiren-wang-yiren-maknae-rapper-gif-15970519",
            "https://tenor.com/view/wang-yiren-everglow-kpop-fierce-gif-15559282",
            "https://tenor.com/view/%E7%8E%8B%E6%80%A1%E4%BA%BAwang-yiren-cute-kpop-smile-gif-16236336",
            "https://tenor.com/view/kpop-chinese-wang-yiren-everglow-smile-gif-15558804",
            "https://tenor.com/view/everglow-yiren-wang-yiren-kpop-cute-gif-16554167",
            "https://tenor.com/view/wang-yiren-everglow-kpop-cute-pretty-gif-15559396",
            "https://tenor.com/view/%E7%8E%8B%E6%80%A1%E4%BA%BA-wang-yiren-cute-pretty-kpop-gif-16236334",
            "https://tenor.com/view/everglow-yiren-wang-yiren-maknae-rapper-gif-16264216",
            "https://tenor.com/view/everglow-kpop-cute-pretty-beautiful-gif-15972795",
            "https://tenor.com/view/everglow-yiren-wang-yiren-kpop-cute-gif-16554171",
            "https://tenor.com/view/everglow-yiren-wang-yiren-maknae-rapper-gif-15907156",
            "https://tenor.com/view/everglow-gif-16227422",
            "https://tenor.com/view/everglow-cute-pretty-kpop-gif-15916228",
            "https://tenor.com/view/yiren-everglow-la-di-da-kpop-stone-music-gif-18570277"]

        self.bot.aisha_gif = ["https://tenor.com/view/everglow-aisha-heo-yoorim-lead-rapper-kpop-gif-16271018",
            "https://tenor.com/view/everglow-aisha-heo-yoorim-lead-rapper-kpop-gif-16264245",
            "https://tenor.com/view/aisha-everglow-gif-18934290",
            "https://tenor.com/view/everglow-aisha-heo-yoorim-lead-rapper-kpop-gif-16220721",
            "https://tenor.com/view/everglow-aisha-heo-yoorim-lead-rapper-kpop-gif-15907107",
            "https://tenor.com/view/everglow-aisha-heo-yoorim-lead-rapper-kpop-gif-15970488",
            "https://tenor.com/view/everglow-dance-kpop-wink-gif-15789124",
            "https://tenor.com/view/everglow-everglow-la-di-da-yiren-aisha-shiyeon-gif-19326454",
            "https://tenor.com/view/everglow-aisha-heo-yoorim-lead-rapper-kpop-gif-16271021",
            "https://tenor.com/view/everglow-aisha-heo-yoorim-lead-rapper-kpop-gif-16259147",
            "https://tenor.com/view/everglow-aisha-heo-yoorim-lead-rapper-kpop-gif-16271022"]

        self.bot.onda_gif = ["https://tenor.com/view/everglow-onda-jo-serim-vocalist-kpop-gif-15970349",
            "https://tenor.com/view/everglow-onda-jo-serim-vocalist-kpop-gif-16263345",
            "https://tenor.com/view/everglow-cute-pretty-kpop-smile-gif-15818709",
            "https://tenor.com/view/everglow-onda-jo-serim-vocalist-kpop-gif-16481547",
            "https://tenor.com/view/everglow-onda-gif-18337504",
            "https://tenor.com/view/everglow-finger-gun-cute-wink-kpop-gif-15970368",
            "https://tenor.com/view/everglow-onda-jo-serim-vocalist-kpop-gif-16194399",
            "https://tenor.com/view/onda-everglow-gif-18337507",
            "https://tenor.com/view/everglow-onda-gif-18337506",
            "https://tenor.com/view/everglow-onda-onda-everglow-gif-19501054"]

        self.bot.sihyeon_gif = ["https://tenor.com/view/everglow-sihyeon-kim-sihyeon-face-of-the-group-rapper-gif-16281910",
            "https://tenor.com/view/everglow-sihyeon-kim-sihyeon-face-of-the-group-rapper-gif-16481660",
            "https://tenor.com/view/everglow-kim-sihyeon-sihyeon-playing-with-hair-kpop-gif-15818759",
            "https://tenor.com/view/everglow-sihyeon-kim-sihyeon-face-of-the-group-rapper-gif-15907131",
            "https://tenor.com/view/everglow-sihyeon-kim-sihyeon-face-of-the-group-rapper-gif-16281918",
            "https://tenor.com/view/everglow-sihyeon-kim-sihyeon-face-of-the-group-rapper-gif-15970364",
            "https://tenor.com/view/everglow-kim-sihyeon-sihyeon-kpop-pretty-gif-15818626",
            "https://tenor.com/view/everglow-cute-pretty-sihyeon-kpop-gif-15600838",
            "https://tenor.com/view/everglow-sihyeon-kim-sihyeon-face-of-the-group-rapper-gif-16281904",
            "https://tenor.com/view/everglow-sihyeon-kim-sihyeon-face-of-the-group-rapper-gif-16221390",
            "https://tenor.com/view/everglow-sihyeon-kim-sihyeon-face-of-the-group-rapper-gif-16220701"]

    @commands.command()
    async def everglow(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Everglow {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}]`" )
        if arg == "eu" or arg == "e:u":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about E:U :heart: ')
                await ctx.send(random.choice(self.bot.eu_gif))
                await ctx.message.delete()
        elif arg =="mia":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Mia :heart: ')
                await ctx.send(random.choice(self.bot.mia_gif))
                await ctx.message.delete()
        elif arg == "yiren":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{weakado}>, <@!{ctx.author.id}> is talking about Yiren :orange_heart:')
                    await ctx.send(random.choice(self.bot.yiren_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yiren :orange_heart:')
                await ctx.send(random.choice(self.bot.yiren_gif))
                await ctx.message.delete()
        elif arg == "aisha":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Aisha :heart: ')
                await ctx.send(random.choice(self.bot.aisha_gif))
                await ctx.message.delete()
        elif arg == "onda":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Onda :heart: ')
                await ctx.send(random.choice(self.bot.onda_gif))
                await ctx.message.delete()
        elif arg == "sihyeon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Sihyeon :heart: ')
                await ctx.send(random.choice(self.bot.sihyeon_gif))
                await ctx.message.delete()

    @commands.command(aliases = ['e:u'])
    async def eu(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about E:U :heart: ')
                await ctx.send(random.choice(self.bot.eu_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about E:U :heart:')
            await ctx.send(random.choice(self.bot.eu_gif))
            await ctx.message.delete()

    @commands.command()
    async def mia(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Mia :heart: ')
                await ctx.send(random.choice(self.bot.mia_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Mia :heart:')
            await ctx.send(random.choice(self.bot.mia_gif))
            await ctx.message.delete()

    @commands.command()
    async def yiren(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{weakado}>, <@!{ctx.author.id}> is talking about Yiren :orange_heart:')
                await ctx.send(random.choice(self.bot.yiren_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yiren :orange_heart:')
            await ctx.send(random.choice(self.bot.yiren_gif))
            await ctx.message.delete()

    @commands.command()
    async def aisha(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Aisha :heart: ')
                await ctx.send(random.choice(self.bot.aisha_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Aisha :heart:')
            await ctx.send(random.choice(self.bot.aisha_gif))
            await ctx.message.delete()

    @commands.command()
    async def onda(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Onda :heart: ')
                await ctx.send(random.choice(self.bot.onda_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Onda :heart:')
            await ctx.send(random.choice(self.bot.onda_gif))
            await ctx.message.delete()

    @commands.command()
    async def sihyeon(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Sihyeon :heart: ')
                await ctx.send(random.choice(self.bot.sihyeon_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Sihyeon :heart:')
            await ctx.send(random.choice(self.bot.sihyeon_gif))
            await ctx.message.delete()



def setup(client):
    client.add_cog(everglow(client))