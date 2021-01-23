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

class April(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.april_chaekyung_gif = ["https://tenor.com/view/yoon-chaekyung-come-on-wink-april-korean-gif-12724653",
            "https://tenor.com/view/yoon-chaekyung-smile-saving-in-my-heart-april-korean-gif-11651926https://tenor.com/view/yoon-chaekyung-smile-saving-in-my-heart-april-korean-gif-11651926",
            "https://tenor.com/view/chaekyung-yoochaekyung-chaewon-naeun-leenaeun-gif-18159977",
            "https://tenor.com/view/chaekyung-gif-18153828",
            "https://tenor.com/view/chaekyung-gif-18153845",
            "https://tenor.com/view/chaekyung-gif-18153731"]

        self.bot.april_chaewon_gif = ["https://tenor.com/view/april-chaewon-kim-chaewon-oh-my-mistake-girl-group-gif-19385727",
            "https://tenor.com/view/chaewon-april-chaewon-chaewon-kpop-gif-19153936",
            "https://tenor.com/view/chaewon-april-chaewon-chaewon-kpop-gif-19153938",
            "https://tenor.com/view/chaewon-april-chaewon-chaewon-kpop-gif-19153935",
            "https://tenor.com/view/chaewon-april-chaewon-chaewon-kpop-gif-19154986",
            "https://tenor.com/view/april-chaewon-chaewon-chaewon-kpop-gif-19154990",
            "https://tenor.com/view/chaewon-april-chaewon-chaewon-kpop-gif-19154988",
            "https://tenor.com/view/chaewon-april-chaewon-chaewon-kpop-gif-19154985",
            "https://tenor.com/view/chaewon-april-chaewon-chaewon-kpop-gif-19153963",
            "https://tenor.com/view/chaewon-april-chaewon-chaewon-kpop-gif-19153940",
            "https://tenor.com/view/chaewon-april-chaewon-gif-19155256",
            "https://tenor.com/view/chaewon-april-chaewon-gif-19155254"]

        self.bot.april_naeun_gif = ["https://gfycat.com/blushingpreciouskomododragon",
            "https://tenor.com/view/%EC%9D%B4%EB%82%98%EC%9D%80-%EC%97%90%EC%9D%B4%ED%94%84%EB%A6%B4-gif-18177576",
            "https://tenor.com/view/naeun-april-naeunapril-aprilnaeun-now-gif-18056208",
            "https://tenor.com/view/naeun-april-gif-18727983",
            "https://tenor.com/view/naeun-chococo27-april-cute-pretty-gif-17153963",
            "https://gfycat.com/basicspottedcreature",
            "https://gfycat.com/backplumpantarcticgiantpetrel",
            "https://tenor.com/view/april-naeun-huh-sad-cute-pretty-gif-17509610",
            "https://tenor.com/view/%EC%9D%B4%EB%82%98%EC%9D%80-%EC%97%90%EC%9D%B4%ED%94%84%EB%A6%B4-gif-18177571",
            "https://tenor.com/view/lee-naeun-april-smile-happy-gif-16982296",
            "https://tenor.com/view/oh-my-mistake-april-naeun-kpop-being-pretty-is-my-mistake-gif-16617876",
            "https://tenor.com/view/naeun-april-leenaeun-%EC%97%90%EC%9D%B4%ED%94%84%EB%A6%B4-%EC%9D%B4%EB%82%98%EC%9D%80-gif-18118903"]

        self.bot.april_yena_gif = ["https://tenor.com/view/april-yena-yena-april-gif-19168655",
            "https://tenor.com/view/yena-april-yena-gif-19167284",
            "https://tenor.com/view/yena-april-yena-gif-19155364",
            "https://tenor.com/view/yena-april-yena-gif-19167273",
            "https://tenor.com/view/yena-april-yena-gif-19155391",
            "https://tenor.com/view/april-yena-april-yena-gif-19168652",
            "https://tenor.com/view/yena-april-yena-gif-19167268",
            "https://tenor.com/view/yena-april-yena-gif-19167266",
            "https://tenor.com/view/yena-april-yena-gif-19167279"]

        self.bot.april_rachel_gif = ["https://tenor.com/view/rachel-april-april-rachel-rachel-kpop-gif-19206221",
            "https://tenor.com/view/rachel-april-april-rachel-rachel-kpop-gif-19206231",
            "https://tenor.com/view/rachel-rachel-kpop-april-rachel-gif-19153877",
            "https://tenor.com/view/rachel-april-april-rachel-rachel-kpop-gif-19206194",
            "https://tenor.com/view/rachel-april-april-rachel-rachel-kpop-gif-19206193",
            "https://tenor.com/view/rachel-songnayeon-april-gif-19626842",
            "https://tenor.com/view/%EC%97%90%EC%9D%B4%ED%94%84%EB%A6%B4-%EB%A0%88%EC%9D%B4%EC%B2%BC-rachel-%EC%84%B1%EB%82%98%EC%97%B0-%EB%82%98%EC%97%B0-gif-18118918",
            "https://tenor.com/view/april-rachel-rachel-kpop-april-rachel-gif-19206241",
            "https://tenor.com/view/april-rachel-april-rachel-rachel-kpop-gif-19206224",
            "https://tenor.com/view/rachel-rachel-kpop-april-rachel-gif-19153870",
            "https://tenor.com/view/ahh-thinking-hmm-confused-unsure-gif-14606325",
            "https://tenor.com/view/rachel-songnayeon-april-gif-19626847"]

        self.bot.april_jinsol_gif = ["https://tenor.com/view/april-jinsol-april-jinsol-gif-19168301",
            "https://tenor.com/view/april-jinsol-april-jinsol-gif-19168280",
            "https://tenor.com/view/jinsol-april-jinsol-april-gif-19168088",
            "https://tenor.com/view/jinsol-april-jinsol-april-gif-19168052",
            "https://tenor.com/view/jinsol-april-jinsol-april-gif-19168075",
            "https://gfycat.com/tatteredtartgemsbuck",
            "https://tenor.com/view/april-jinsol-april-jinsol-gif-19168279",
            "https://tenor.com/view/april-jinsol-april-jinsol-gif-19168292",
            "https://tenor.com/view/jinsol-april-jinsol-april-gif-19168057",
            "https://tenor.com/view/jinsol-april-jinsol-april-gif-19168049"]

        self.bot.april_hyunjoo_gif = ["https://tenor.com/view/jinsol-april-jinsol-april-gif-19168049",  
            "https://gfycat.com/considerateimpurecommabutterfly",
            "https://gfycat.com/angelicelegantgarpike",
            "https://gfycat.com/agitatedgregariousafricanbushviper-mechabear-hyunjoo-kpop",
            "https://gfycat.com/handsomeweebufeo",
            "https://gfycat.com/impossibleopulentdiamondbackrattlesnake-mechabear-hyunjoo-kpop",
            "https://gfycat.com/thirstydimwittedhydatidtapeworm",
            "https://gfycat.com/selfreliantilliterateamericanmarten",
            "https://gfycat.com/idlediscreteimpala",
            "https://gfycat.com/longadmiredindianspinyloach",
            "https://gfycat.com/sentimentaldistortedcleanerwrasse",
            "https://gfycat.com/jointbolddogwoodtwigborer",
            "https://gfycat.com/whisperedlinearcapybara"]


    @commands.command()
    async def april(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [April {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "chaekyung":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chaekyung :heart:')
                await ctx.send(random.choice(self.bot.april_chaekyung_gif))
                await ctx.message.delete()
        elif arg == "chaewon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chaewon :heart:')
                await ctx.send(random.choice(self.bot.april_chaewon_gif))
                await ctx.message.delete()
        elif arg == "naeun":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Naeun :heart:')
                await ctx.send(random.choice(self.bot.april_naeun_gif))
                await ctx.message.delete()
        elif arg == "yena":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yena :heart:')
                await ctx.send(random.choice(self.bot.april_yena_gif))
                await ctx.message.delete()
        elif arg == "rachel":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Rachel :heart:')
                await ctx.send(random.choice(self.bot.april_rachel_gif))
                await ctx.message.delete()
        elif arg == "jinsol":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jinsol :heart:')
                await ctx.send(random.choice(self.bot.april_jinsol_gif))
                await ctx.message.delete()
        elif arg == "hyunjoo":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Hyunjoo :heart:')
                await ctx.send(random.choice(self.bot.april_hyunjoo_gif))
                await ctx.message.delete()

def setup(client):
    client.add_cog(April(client))