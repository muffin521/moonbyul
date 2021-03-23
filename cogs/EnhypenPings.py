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

class EnhypenPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.sunoo_gif = ["https://tenor.com/view/sunoo-enhypen-enhypen-sunoo-chamber5-halloween-fruit-gif-18991845",
            "https://tenor.com/view/sunoo-kimsunoo-enhypen-sunoo-enhypen-enhypen-sunoo-gif-18562350",
            "https://tenor.com/view/sunoo-kimsunoo-enhypen-enhypen-sunoo-sunoo-enhypen-gif-18562288",
            "https://tenor.com/view/sunoo-kimsunwoo-kimsunoo-gif-18475279",
            "https://tenor.com/view/sunoo-kimsunoo-enhypen-gif-18534459",
            "https://tenor.com/view/sunoo-kimsunoo-kimsunwoo-gif-18496745",
            "https://tenor.com/view/sunoo-sunoo-enhypen-sunoo-sunflower-iland-iland-sunoo-gif-18676497",
            "https://tenor.com/view/enhypen-iland29-%E3%82%BD%E3%83%8C-gif-19801932",
            "https://tenor.com/view/sunoo-enhypen-gif-19394237",
            "https://tenor.com/view/sunoo-kim-sunoo-sunoo-enhypen-seattltes-sunoo-cute-gif-20342832",
            "https://tenor.com/view/sunoo-sunoo-gif-sunoo-gifs-enhypen-enhypen-gif-gif-20188099",
            "https://tenor.com/view/sunoo-sunoo-enhypen-kim-sunoo-gif-20703332"]

        self.bot.sunghoon_gif = ["https://tenor.com/view/sunghoon-parksunghoon-sunghoon-iland-gif-18497043",
            "https://tenor.com/view/sunghoon-parksunghoon-iland-sunghoon-iland-sunghoon-enhypen-gif-18588345",
            "https://tenor.com/view/sunghoon-park-sunghoon-enhypen-sunghoon-sunghoon-sunoo-tom-jerry-gif-19180220",
            "https://tenor.com/view/enhypen-sunghoon-sunghoon-enhypen-gif-18817568",
            "https://tenor.com/view/sunghoon-parksunghoon-enhypen-gif-18530989"]
        
        self.bot.jake_gif = ["https://tenor.com/view/shim-jake-jake-enhypen-jake-gif-18619802",
            "https://tenor.com/view/jake-shim-jake-jake-enhypen-gif-18619795",
            "https://tenor.com/view/jake-enhypen-enhypenjake-gif-18667629",
            "https://tenor.com/view/jake-enhypen-enhypen-jake-gif-18719902",
            "https://tenor.com/view/jake-enhypen-jake-enhypen-iland-gif-18670778"]

        self.bot.jungwon_gif = ["https://tenor.com/view/yang-jungwon-jungwon-iland-jungwon-iland-gif-18187930",
            "https://tenor.com/view/yang-jungwon-jungwon-enhypen-jungwon-jungwon-enhypen-enhypen-gif-19247505",
            "https://tenor.com/view/yang-jungwon-jungwon-enhypen-jungwon-jungwon-enhypen-enhypen-gif-19012991",
            "https://tenor.com/view/yang-jungwon-jungwon-jungwon-iland-iland-mnet-iland-gif-18563027",
            "https://tenor.com/view/yang-jungwon-jungwon-iland-jungwon-enhypen-jungwon-mnet-iland-gif-18732853"]

        self.bot.heeseung_gif = ["https://tenor.com/view/heeseung-leeheeseung-heedeungie-gif-18445098",
            "https://tenor.com/view/halloween-fruit-enhypen-chamber5-enhypen-heeseung-heeseung-gif-18991852",
            "https://tenor.com/view/heeseung-leeheeseung-heeseung-iland-gif-18435020",
            "https://tenor.com/view/heeseung-leeheeseung-heeseung-iland-gif-18440665",
            "https://tenor.com/view/heeseung-iland-enhypen-heart-enhypenheeseung-gif-19350769"]

        self.bot.jay_gif = ["https://tenor.com/view/jay-jay-enhypen-enhypen-jay-iland-mnet-iland-gif-18611729",
            "https://tenor.com/view/jay-%EC%A0%9C%EC%9D%B4-iland-enhypen-gif-18606251",
            "https://tenor.com/view/halloween-fruit-jay-enhypen-enhypen-chamber5-gif-18991847",
            "https://tenor.com/view/enhypen-enhypen-gif-enhypen-jay-enhypen-meme-park-jay-gif-18978288",
            "https://tenor.com/view/enhypen-enhypen-gif-enhypen-jay-enhypen-jay-park-jay-park-gif-18678278"]

        self.bot.niki_gif = ["https://tenor.com/view/niki-niki-enhypen-niki-woah-woah-niki-dance-gif-19028474",
            "https://tenor.com/view/niki-nishimura-riki-iland-niki-iland-niki-enhypen-gif-18606852",
            "https://tenor.com/view/niki-iland-niki-niki-iland-niki-sleeping-iland-niki-sleeping-gif-18451085",
            "https://tenor.com/view/niki-sassy-sass-enhypen-ooh-gif-19076870",
            "https://tenor.com/view/enhypen-niki-iland-nikienhypen-gif-19295388"]

    @commands.command()
    async def enhypen(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Enhypen {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "sunoo":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Sunoo :heart:')
                await ctx.send(random.choice(self.bot.sunoo_gif))
                await ctx.message.delete()
        elif arg == "sunghoon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Sunghoon :heart:')
                await ctx.send(random.choice(self.bot.sunghoon_gif))
                await ctx.message.delete()
        elif arg == "jake":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jake :heart:')
                await ctx.send(random.choice(self.bot.jake_gif))
                await ctx.message.delete()
        elif arg == "jungwon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jungwon :heart:')
                await ctx.send(random.choice(self.bot.jungwon_gif))
                await ctx.message.delete()
        elif arg == "heeseung":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Heeseung :heart:')
                await ctx.send(random.choice(self.bot.heeseung_gif))
                await ctx.message.delete()
        elif arg == "niki" or arg == "ni-ki":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Ni-Ki :heart:')
                await ctx.send(random.choice(self.bot.niki_gif))
                await ctx.message.delete()
        elif arg == "jay":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jay :heart:')
                await ctx.send(random.choice(self.bot.jay_gif))
                await ctx.message.delete()


def setup(client):
    client.add_cog(EnhypenPings(client))