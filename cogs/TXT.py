import discord, random
from discord.ext import commands

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574


class txtPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        #7
        self.bot.txt_soobin_gif = ["https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-soobin-gif-17906793",
            "https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-soobin-gif-17599191",
            "https://tenor.com/view/soobin-txt-choisoobin-tomorrowbytogether-tomorrowxtogether-gif-16277376",
            "https://tenor.com/view/choi-soobin-txt-tomorrow-by-together-tomorrow-x-together-todo-gif-16311084",
            "https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-soobin-gif-16642602",
            "https://tenor.com/view/soobin-txt-tomorrow-x-together-kpop-choi-soobin-gif-19186061",
            "https://tenor.com/view/choi-soobin-txt-tomorrow-by-together-tomorrow-x-together-todo-gif-16311086"]

        #7
        self.bot.txt_yeonjun_gif = ["https://tenor.com/view/tomorrow-by-together-big-hit-entertainmen-txt-yeonjun-handsome-gif-17716681",
            "https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-yeonjun-gif-17647828",
            "https://tenor.com/view/yeonjun-txt-tomorrow-by-together-blue-hour-moa-gif-18951417",
            "https://tenor.com/view/yeonjun-txt-tomorrow-x-together-kpop-yeonjun-noona-gif-19211100",
            "https://tenor.com/view/yeonjun-txt-tomorrow-x-together-kpop-yeonjun-noona-gif-19211095",
            "https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-yeonjun-gif-17647836",
            "https://tenor.com/view/choi-yeonjun-txt-tomorrowbytogether-tomorrowxtogether-gif-16277571"]

        #7
        self.bot.txt_beomgyu_gif = ["https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-beomgyu-gif-17683775",
            "https://tenor.com/view/beomgyu-txt-tomorrow-x-together-kpop-choi-beomgyu-gif-19211104",
            "https://tenor.com/view/performance-stage-dance-dance-performance-%EB%B2%94%EA%B7%9C-gif-15902416",
            "https://tenor.com/view/choi-beomgyu-txt-tomorrow-by-together-tomorrow-x-together-todo-gif-16310981",
            "https://tenor.com/view/beomgyu-beomgyu-model-beomgyu-runway-txt-beomgyu-beomgyu-txt-gif-18950063",
            "https://tenor.com/view/choi-beomgyu-txt-tomorrow-by-together-tomorrow-x-together-todo-gif-16310980",
            "https://tenor.com/view/beomgyu-choi-beomgyu-txt-tomorrow-x-together-kpop-gif-19211432"]

        #7
        self.bot.txt_taehyun_gif = ["https://tenor.com/view/txt-taehyun-kang-taehyun-kang-taehyun-txt-taehyun-txt-gif-18959632",
            "https://tenor.com/view/taehyun-kang-taehyun-txt-tomorrow-x-together-taehyunie-gif-19009636",
            "https://tenor.com/view/txt-taehyun-taehyun-kang-taehyun-taehyun-heart-gif-19290757",
            "https://tenor.com/view/kang-taehyun-txt-tomorrowbytogether-tomorrowxtogether-gif-16277417",
            "https://tenor.com/view/txt-taehyun-taehyun-txt-taehyun-aegyo-kangtaehyun-taehyun-cute-gif-19361155",
            "https://tenor.com/view/kang-taehyun-txt-tomorrow-by-together-tomorrow-x-together-todo-gif-16310954",
            "https://tenor.com/view/txt-taehyun-txt-txt-taehyun-kangtaehyun-txt-drama-gif-19384362"]

        #7
        self.bot.txt_hueningkai_gif = ["https://tenor.com/view/txt-huening-kai-hyuka-txt-hueningkai-huening-kai-blue-hour-gif-19341353",
            "https://tenor.com/view/love-huening-kai-wink-confetti-performance-gif-16420492",
            "https://tenor.com/view/performance-stage-music-dance-dance-performance-gif-15902429",
            "https://tenor.com/view/huening-kai-im-dead-ghost-cute-handsome-gif-16798350",
            "https://tenor.com/view/hueningkai-huening-kai-kpop-txt-gif-19211443",
            "https://tenor.com/view/txt-puma-puma-huening-kai-hyuka-kai-gif-18009318",
            "https://tenor.com/view/txt-huening-kai-cant-you-see-me-gif-18717975"]

    @commands.command()
    async def txt(self, ctx, *, arg):
        if arg == "soobin":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Soobin :rabbit:')
                await ctx.send(random.choice(self.bot.txt_soobin_gif))
                await ctx.message.delete()
        elif arg == "yeonjun":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yeonjun :fox:')
                await ctx.send(random.choice(self.bot.txt_yeonjun_gif))
                await ctx.message.delete()
        elif arg == "beomgyu":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Beomgyu :bear:')
                await ctx.send(random.choice(self.bot.txt_beomgyu))
                await ctx.message.delete()
        elif arg == "taehyun":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Taehyun :chipmunk:')
                await ctx.send(random.choice(self.bot.txt_taehyun_gif))
                await ctx.message.delete()
        elif arg == "huening kai":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Huening Kai :penguin:')
                await ctx.send(random.choice(self.bot.txt_hueningkai_gif))
                await ctx.message.delete()

    @commands.command()
    async def soobin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Soobin :rabbit:')
                await ctx.send(random.choice(self.bot.soobin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Soobin :rabbit:')
            await ctx.send(random.choice(self.bot.soobin_gif))
            await ctx.message.delete()

    @commands.command()
    async def yeonjun(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yeonjun :fox:')
                await ctx.send(random.choice(self.bot.yeonjun_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yeonjun :fox:')
            await ctx.send(random.choice(self.bot.yeonjun_gif))
            await ctx.message.delete()

    @commands.command()
    async def beomgyu(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Beomgyu :bear:')
                await ctx.send(random.choice(self.bot.beomgyu))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Beomgyu :bear:')
            await ctx.send(random.choice(self.bot.beomgyu_gif))
            await ctx.message.delete()

    @commands.command()
    async def taehyun(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Taehyun :chipmunk:')
                await ctx.send(random.choice(self.bot.taehyun_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Taehyun :chipmunk:')
            await ctx.send(random.choice(self.bot.taehyun_gif))
            await ctx.message.delete()

    @commands.command(aliases = ['huening'])
    async def hueningkai(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Huening Kai :penguin:')
                await ctx.send(random.choice(self.bot.hueningkai_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Huening Kai :penguin:')
            await ctx.send(random.choice(self.bot.hueningkai_gif))
            await ctx.message.delete()

def setup(client):
    client.add_cog(txtPings(client))