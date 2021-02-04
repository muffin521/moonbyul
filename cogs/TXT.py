import discord, random
from discord.ext import commands
from datetime import datetime

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

        self.bot.txt_yeonjun_gif = ["https://tenor.com/view/tomorrow-by-together-big-hit-entertainmen-txt-yeonjun-handsome-gif-17716681",
            "https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-yeonjun-gif-17647828",
            "https://tenor.com/view/yeonjun-txt-tomorrow-by-together-blue-hour-moa-gif-18951417",
            "https://tenor.com/view/yeonjun-txt-tomorrow-x-together-kpop-yeonjun-noona-gif-19211100",
            "https://tenor.com/view/yeonjun-txt-tomorrow-x-together-kpop-yeonjun-noona-gif-19211095",
            "https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-yeonjun-gif-17647836",
            "https://tenor.com/view/choi-yeonjun-txt-tomorrowbytogether-tomorrowxtogether-gif-16277571",
            "https://cdn.discordapp.com/attachments/807006158665285673/807006777908133909/Tumblr_l_211673872934920.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807006778868236368/Tumblr_l_211734956508022.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807006781368565861/Tumblr_l_211753081701713.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807006782345445426/Tumblr_l_211780453128838.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807006782919802880/Tumblr_l_211787843879044.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007035090141184/Tumblr_l_211855654035737.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007035492270120/Tumblr_l_211876113648802.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007035958886420/Tumblr_l_211882417654633.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007036767993917/Tumblr_l_211886198497652.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007037585358868/Tumblr_l_211926113807949.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007038198120508/Tumblr_l_211929646072896.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007038902239232/Tumblr_l_212168482875773.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007039262818365/Tumblr_l_212173662393167.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007668350091334/Tumblr_l_212295783828017.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007669285683200/Tumblr_l_213925366730520.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007669654257684/Tumblr_l_213935720058328.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007670451437618/Tumblr_l_213953962443217.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007671009804308/Tumblr_l_213953365225509.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007671692689458/Tumblr_l_213959735187955.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007672465358888/Tumblr_l_213964612717849.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007673530581055/Tumblr_l_213968417346962.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007674033635348/Tumblr_l_213971776728731.gif"]

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
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [TXT | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
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
                await ctx.send(random.choice(self.bot.txt_beomgyu_gif))
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


def setup(client):
    client.add_cog(txtPings(client))