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
k8 = 573974040679809044

class DreamCatcherPings(commands.Cog):

    #wizzy has gifs!!
    def __init__(self, bot):
        self.bot = bot

        self.bot.dreamcatcher_jiu_gif = ["https://tenor.com/view/onex-1x-jiu-hawt-kim-minji-hawt-jiu-gif-18812596",
            "https://cdn.discordapp.com/attachments/771238115255255060/785294061132709930/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/785294061996605470/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/785294062764818452/image2.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/785294063871721472/image3.gif"]

        self.bot.dreamcatcher_dami_gif = ["https://tenor.com/view/dreamcatcher-%EB%93%9C%EB%A6%BC%EC%BA%90%EC%B3%90-dami-cute-dance-gif-12255241",
            "https://tenor.com/view/dami-dreamcatcher-dcboca-gif-18178539",
            "https://tenor.com/view/dreamcatcher-dami-gif-18622933",
            "https://tenor.com/view/dreamcatcher-dami-full-moon-dreamcatcher-dami-arrow-gif-18971647",
            "https://tenor.com/view/lee-yubin-dami-dreamcatcher-meemoy-boca-gif-18893268",
            "https://tenor.com/view/dami-zombie-dreamcatcher-lee-yubin-boca-gif-18882718",
            "https://tenor.com/view/dami-dreamcatcher-boca-dc-dcboca-gif-18201110",
            "https://tenor.com/view/dreamcatcher-cute-yoohyeon-dami-gif-12143809",
            "https://tenor.com/view/dami-kwave-sexy-dance-dreamcatcher-gif-12249892",
            "https://tenor.com/view/dami-dami-dreamcatcher-dreamcatcher-dance-gif-13832007",
            "https://tenor.com/view/dreamcatcher-dami-lee-yoobin-kpop-pretty-gif-15563905",
            "https://tenor.com/view/dami-dami-dreamcatcher-dreamcatcher-cute-smile-gif-13831991",
            "https://tenor.com/view/dreamcatcher-dami-lee-yubin-main-rapper-lead-dancer-gif-17558548",
            "https://tenor.com/view/dami-dami-dreamcatcher-dreamcatcher-sexy-dance-gif-13832025",
            "https://tenor.com/view/dami-dreamcatcher-boca-dcboca-dc-gif-18229330",
            "https://tenor.com/view/dreamcatcher-su-a-kim-bora-dami-havana-gif-12130542",
            "https://tenor.com/view/dreamcatcher-su-a-kim-bora-dami-havana-gif-12130543",
            "https://tenor.com/view/dream-catcher-kpop-girl-group-piri-insomnia-gif-16831355",
            "https://tenor.com/view/king-kong-dreamcatcher-dami-lee-yubin-main-rapper-gif-15879177",
            "https://tenor.com/view/kpop-dream-catcher-dami-chewing-gif-15563908",
            "https://tenor.com/view/dreamcatcher-dami-lee-yoobin-kpop-pretty-gif-15563904",
            "https://tenor.com/view/dream-catcher-lee-yubin-cute-dami-kpop-gif-17900509",
            "https://tenor.com/view/dami-dream-catcher-cute-wave-kpop-gif-15515589",
            "https://tenor.com/view/dami-dreamcatcher-smile-happy-cute-gif-11972846",
            "https://tenor.com/view/dami-dreamcatcher-boca-dcboca-kpop-gif-18229558",
            "https://tenor.com/view/dami-dreamcatcher-boca-dcboca-kpop-gif-18229536",
            "https://tenor.com/view/dreamcatcher-dami-lee-yubin-main-rapper-lead-dancer-gif-17720409",
            "https://tenor.com/view/dreamcatcher-dami-lee-yubin-kpop-pretty-gif-15811393"]

        self.bot.dreamcatcher_gahyeon_gif = []

        self.bot.dreamcatcher_handong_gif = []

        self.bot.dreamcatcher_siyeon_gif = []

        self.bot.dreamcatcher_sua_gif = []

        self.bot.dreamcatcher_yoohyeon_gif = []

    @commands.command(aliases = ['dream'])
    async def dreamcatcher(self, ctx, *, arg):
        if arg == "jiu" or arg == "catcher jiu":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{k8}>, <@!{ctx.author.id}> is talking about JiU :rabbit: ')
                    await ctx.send(random.choice(self.bot.dreamcatcher_jiu_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about JiU :rabbit:')
                await ctx.send(random.choice(self.bot.dreamcatcher_jiu_gif))
                await ctx.message.delete()
        elif arg == "dami" or arg == "catcher dami":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Dami :heart:') 
                await ctx.send(random.choice(self.bot.dreamcatcher_dami_gif))
                await ctx.message.delete()

    @commands.command()
    async def jiu(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{k8}>, <@!{ctx.author.id}> is talking about JiU :rabbit: ')
                await ctx.send(random.choice(self.bot.dreamcatcher_jiu_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about JiU :rabbit:')
            await ctx.send(random.choice(self.bot.dreamcatcher_jiu_gif))
            await ctx.message.delete()

def setup(client):
    client.add_cog(DreamCatcherPings(client))