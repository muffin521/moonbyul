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

#//people
muffin = 488423352206229505


class CLC(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.clc_yeeun_gif = ["https://tenor.com/view/yeeun-clc-gif-19116003",
            "https://tenor.com/view/yeeun-clc-gif-19116004",
            "https://tenor.com/view/yeeun-clc-gif-19116007",
            "https://tenor.com/view/yeeun-clc-gif-19116012",
            "https://tenor.com/view/yeeun-clc-bad-girls-jang-gif-13252706",
            "https://tenor.com/view/yeeun-clc-crystal-clear-cute-girl-group-gif-15041212",
            "https://tenor.com/view/clc-yeeun-clc-yeeun-rap-kpop-gif-15340668",
            "https://tenor.com/view/clc-kpop-yeeun-gif-18657579",
            "https://tenor.com/view/yeeun-jang-clc-cute-stare-gif-13329818",
            "https://tenor.com/view/yeeun-jang-yeeun-cute-clc-kpop-gif-17883335",
            "https://tenor.com/view/yeeun-clc-crystal-clear-cute-girl-group-gif-15041189",
            "https://tenor.com/view/yeeun-clc-bad-girls-jang-gif-13252063",
            "https://tenor.com/view/yeeun-jang-clc-flip-hair-gif-13252498",
            "https://tenor.com/view/yeeun-jang-clc-gif-13328477",
            "https://tenor.com/view/jang-ye-eun-selfie-talking-cute-pretty-gif-16653425",
            "https://tenor.com/view/yeeun-jang-yeeun-clc-crystal-clear-girl-group-gif-15041366",
            "https://tenor.com/view/crystal-clear-jang-kpop-yeeun-clc-gif-14859536",
            "https://tenor.com/view/yay-wink-cute-yeeun-clc-gif-14300869",
            "https://tenor.com/view/yeeun-jang-clc-not-yummy-gif-13252749",
            "https://tenor.com/view/crystal-clear-jang-kpop-devil-yeeun-gif-14999392",
            "https://tenor.com/view/chonnasorn-sajakul-yeeun-clc-sorn-gif-13252160"]

        self.bot.clc_sorn_gif = ["https://tenor.com/bqihb.gif",
            "https://tenor.com/bunmH.gif",
            "https://tenor.com/bunmN.gif",
            "https://tenor.com/view/sorn-clc-gif-18620769",
            "https://tenor.com/view/clcsorn-sorn-clc-gif-18176207",
            "https://tenor.com/view/sorn-clc-gif-18563360"]
        
        self.bot.clc_eunbin_gif = ["https://tenor.com/RCQt.gif",
            "https://tenor.com/RCSH.gif",
            "https://tenor.com/9gg1.gif",
            "https://tenor.com/view/devil-crystal-clear-mbc-music-core-kwon-eunbin-kpop-gif-15048708"]

        self.bot.clc_yujin_gif = ["https://tenor.com/ba9ol.gif",
            "https://tenor.com/bunmO.gif",
            "https://tenor.com/3LBO.gif",
            "https://tenor.com/view/yujin-yujinclc-yeeun-yeeunclc-clchelicopter-gif-19218780",
            "https://tenor.com/view/yujin-yujinclc-clc-yeeun-sorn-gif-19221197"]

        self.bot.clc_seunghee_gif = ["https://tenor.com/view/crystal-clear-%ec%98%a4-%ec%94%a8%ec%97%98%ec%94%a8-kpop-%ec%98%a4%ec%8a%b9%ed%9d%ac-gif-17069531",
            "https://tenor.com/view/crystal-clear-kpop-phone-devil-gif-14977696",
            "https://tenor.com/view/eyebrow-kpop-bangs-clc-oh-gif-14148382",
            "https://tenor.com/view/oh-seunghee-clc-gif-13251990"]

        self.bot.clc_seungyeon_gif = ["https://tenor.com/view/seungyeon-clc-please-begging-gif-13944535",
            "https://tenor.com/view/seungyeon-chang-clc-gif-13252414",
            "https://tenor.com/view/seungyeon-chang-clc-hobgoblin-pretty-gif-13252470",
            "https://tenor.com/view/black-dress-seungyeon-chang-clc-gif-13251952",
            "https://tenor.com/view/seungyeon-chang-clc-gif-13252136"]

        self.bot.clc_elkie_gif = ["https://tenor.com/view/puppy-dog-elkie-clc-gif-13944542",
            "https://tenor.com/view/elkie-singer-clc-gif-18154058",
            "https://tenor.com/view/chong-tingyan-crystal-clear-elkie-chong-kpop-devil-gif-15036131",
            "https://tenor.com/view/chong-tingyan-elkie-clc-come-here-gif-13252022",
            "https://tenor.com/view/chong-tingyan-elkie-clc-hi-gif-13252481"]

    @commands.command()
    async def clc(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [CLC {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "yeeun":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Yeeun :heart:')
                    await ctx.send(random.choice(self.bot.clc_yeeun_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yeeun :heart:')
                await ctx.send(random.choice(self.bot.clc_yeeun_gif))
                await ctx.message.delete()
        elif arg == "sorn":
            if ctx.guild.id == luminary and ctx.channl.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Sorn :heart:')
                await ctx.send(random.choice(self.bot.clc_sorn_gif))
                await ctx.message.delete()
        elif arg == "eunbin":
            if ctx.guild.id == luminary and ctx.channl.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Eunbin :heart:')
                await ctx.send(random.choice(self.bot.clc_eunbin_gif))
                await ctx.message.delete()
        elif arg == "yujin":
            if ctx.guild.id == luminary and ctx.channl.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yujin :heart:')
                await ctx.send(random.choice(self.bot.clc_yujin_gif))
                await ctx.message.delete()
        elif arg == "seunghee":
            if ctx.guild.id == luminary and ctx.channl.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Seunghee :heart:')
                await ctx.send(random.choice(self.bot.clc_seunghee_gif))
                await ctx.message.delete()
        elif arg == "seungyeon":
            if ctx.guild.id == luminary and ctx.channl.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Seungyeon :heart:')
                await ctx.send(random.choice(self.bot.clc_seungyeon_gif))
                await ctx.message.delete()
        elif arg == "elkie":
            if ctx.guild.id == luminary and ctx.channl.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Elkie :heart:')
                await ctx.send(random.choice(self.bot.clc_elkie_gif))
                await ctx.message.delete()

def setup(client):
    client.add_cog(CLC(client))