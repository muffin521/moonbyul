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


class weeekly(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.weeekly_soojin_gif = ["https://media.discordapp.net/attachments/782405901515751445/790061522478039041/SJ1.gif",
            "https://tenor.com/view/soojin-soojinweeekly-weeekly-weeeklysoojin-rookie2020-gif-19217007",
            "https://cdn.discordapp.com/attachments/790062429866426368/790074792190541834/SOOJIN1.gif",
            "https://tenor.com/view/weeeklysoojin-weeekly-soojin-gif-19216994",
            "https://tenor.com/view/boss-puppy-lee-soojin-soojin-weeekly-sv-gif-18790774",
            "https://tenor.com/view/weeekly-soojin-lee-soojin-kpop-cute-gif-17374750",
            "https://tenor.com/view/soojin-weeekly-pat-gif-18049939",
            "https://tenor.com/view/weeeklysoojin-gif-19217520",
            "https://tenor.com/view/weeekly-soojin-weeekly-soojin-no-money-weeekly-no-momey-gif-18802164"]

        self.bot.weeekly_jiyoon_gif = ["https://media.discordapp.net/attachments/782405901515751445/790061610936958976/JY1.gif",
            "https://cdn.discordapp.com/attachments/790062585054625873/790074833609949214/JIYOON4.gif",
            "https://cdn.discordapp.com/attachments/790062585054625873/790074875695071292/JIYOON3.gif",
            "https://cdn.discordapp.com/attachments/790062585054625873/790074900815282207/JIYOON2.gif",
            "https://cdn.discordapp.com/attachments/790062585054625873/790074926430027836/JIYOON1.gif",
            "https://tenor.com/view/jiyoon-weeekly-gif-18604350",
            "https://tenor.com/view/jiyoon-weeekly-cute-pretty-gif-17532953",
            "https://tenor.com/view/weeekly-weeekly-jiyoon-jiyoon-gif-18127931",
            "https://tenor.com/view/pretty-jiyoon-weeekly-smile-weeekly-jiyoon-gif-18128574",
            "https://tenor.com/view/weeekly-jiyoon-jiyoon-weeekly-cute-gif-18128670",
            "https://tenor.com/view/shocked-jiyoon-weeekly-weeekly-jiyoon-weeekly-shocked-gif-18226642",
            "https://tenor.com/view/jiyoon-weeekly-weeekly-jiyoon-shin-jiyoon-gif-19422209"]

        self.bot.weeekly_monday_gif = ["https://media.discordapp.net/attachments/782405901515751445/790061529511886858/MD1.gif",
            "https://cdn.discordapp.com/attachments/790062662905102346/790074986702438450/MONDAY1.gif",
            "https://tenor.com/view/weeekly-jaehee-weeekly-jaehee-jaehee-heart-weeekly-heart-gif-18849380",
            "https://tenor.com/view/weeekly-jihan-weeekly-jihan-jihyo-weeekly-jihyo-gif-18860644",
            "https://tenor.com/view/weeekly-soojin-monday-jiyoon-soeun-gif-18168556",
            "https://tenor.com/view/monday-weeekly-laugh-kpop-cute-gif-17478647",
            "https://tenor.com/view/weeekly-monday-weeekly-monday-playm-gif-18227541",
            "https://tenor.com/view/monday-weeekly-smirk-gif-18059513"]

        self.bot.weeekly_soeun_gif = ["https://media.discordapp.net/attachments/782405901515751445/790061900464390144/SN1.gif",
            "https://media.discordapp.net/attachments/782405901515751445/790061824346161202/SN2.gif",
            "https://media.discordapp.net/attachments/782405901515751445/790061567625396224/SN3.gif",
            "https://tenor.com/view/weeekly-soeun-weeekly-soeun-gif-18130042",
            "https://tenor.com/view/weeekly-weeekly-jiyoon-weeekly-soeun-soeun-jiyoon-gif-18216326",
            "https://tenor.com/view/weeekly-weeekly-soeun-soeun-playm-entertainment-playm-gif-18087242"]

        self.bot.weeekly_jaehee_gif = ["https://media.discordapp.net/attachments/782405901515751445/790061927333101588/JH1.gif",
            "https://media.discordapp.net/attachments/782405901515751445/790061542749372416/JH3.gif",
            "https://cdn.discordapp.com/attachments/790062758556336128/790075085779894273/JAEHEE1.gif",
            "https://tenor.com/view/weeekly-jaehee-weeekly-jaehee-jaehee-sad-weeekly-jaehee-sad-gif-18217735",
            "https://tenor.com/view/jaehee-weeekly-weeekly-jaehee-weeekly-think-jaehee-think-gif-19422471",
            "https://tenor.com/view/jaehee-weeekly-weeekly-jaehee-weeekly-jaehee-cute-jaehee-cute-gif-18217794"]

        self.bot.weeekly_jihan_gif = ["https://cdn.discordapp.com/attachments/790062796150407209/790075153744658442/JIHAN3.gif",
            "https://cdn.discordapp.com/attachments/790062796150407209/790075171691692032/JIHAN2.gif",
            "https://cdn.discordapp.com/attachments/790062796150407209/790075206399950908/JIHAN1.gif",
            "https://tenor.com/view/jihan-weeekly-weeekly-jihan-han-jihyo-kpop-gif-18464277",
            "https://tenor.com/view/weeekly-jihan-weeekly-jihan-cute-gif-18128616"]

        self.bot.weeekly_zoa_gif = ["https://media.discordapp.net/attachments/782405901515751445/790061591798087690/ZA3.gif",
            "https://cdn.discordapp.com/attachments/790062825796141077/790075277409255512/ZOA1.gif",
            "https://cdn.discordapp.com/attachments/790062825796141077/790075317947203634/ZOA2.gif",
            "https://cdn.discordapp.com/attachments/790062825796141077/790075328466911272/ZOA3.gif",
            "https://cdn.discordapp.com/attachments/790062825796141077/790075355247149066/ZO4.gif",
            "https://tenor.com/view/weeekly-musical-group-soojin-monday-zoa-gif-17658497"]

    @commands.command()
    async def weeekly(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Weeekly | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "soojin":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Soojin :heart:')
                await ctx.send(random.choice(self.bot.weeekly_soojin_gif))
                await ctx.message.delete()
        elif arg == "jiyoon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jiyoon :heart:')
                await ctx.send(random.choice(self.bot.weeekly_jiyoon_gif))
                await ctx.message.delete()
        elif arg == "monday":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Monday :heart:')
                await ctx.send(random.choice(self.bot.weeekly_monday_gif))
                await ctx.message.delete()
        elif arg == "soeun":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Soeun :heart:')
                await ctx.send(random.choice(self.bot.weeekly_soeun_gif))
                await ctx.message.delete()
        elif arg == "jaehee":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jaehee :heart:')
                await ctx.send(random.choice(self.bot.weeekly_jaehee_gif))
                await ctx.message.delete()
        elif arg == "jihan":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jihan :heart:')
                await ctx.send(random.choice(self.bot.weeekly_jihan_gif))
                await ctx.message.delete()
        elif arg == "zoa":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Zoa :heart:')
                await ctx.send(random.choice(self.bot.weeekly_zoa_gif))
                await ctx.message.delete()

    @commands.command()
    async def wsoojin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Soojin :heart:')
                await ctx.send(random.choice(self.bot.weeekly_soojin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Soojin :heart:')
            await ctx.send(random.choice(self.bot.weeekly_soojin_gif))
            await ctx.message.delete()

    @commands.command()
    async def jiyoon(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jiyoon :heart:')
                await ctx.send(random.choice(self.bot.weeekly_jiyoon_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jiyoon :heart:')
            await ctx.send(random.choice(self.bot.weeekly_jiyoon_gif))
            await ctx.message.delete()

    @commands.command()
    async def monday(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Monday :heart:')
                await ctx.send(random.choice(self.bot.weeekly_monday_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Monday :heart:')
            await ctx.send(random.choice(self.bot.weeekly_monday_gif))
            await ctx.message.delete()

    @commands.command()
    async def soeun(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Soeun :heart:')
                await ctx.send(random.choice(self.bot.weeekly_soeun_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Soeun :heart:')
            await ctx.send(random.choice(self.bot.weeekly_soeun_gif))
            await ctx.message.delete()

    @commands.command()
    async def jaehee(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jaehee :heart:')
                await ctx.send(random.choice(self.bot.weeekly_jaehee_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jaehee :heart:')
            await ctx.send(random.choice(self.bot.weeekly_jaehee_gif))
            await ctx.message.delete()

    @commands.command()
    async def jihan(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jihan :heart:')
                await ctx.send(random.choice(self.bot.weeekly_jihan_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jihan :heart:')
            await ctx.send(random.choice(self.bot.weeekly_jihan_gif))
            await ctx.message.delete()

    @commands.command()
    async def zoa(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Zoa :heart:')
                await ctx.send(random.choice(self.bot.weeekly_zoa_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Zoa :heart:')
            await ctx.send(random.choice(self.bot.weeekly_zoa_gif))
            await ctx.message.delete()

def setup(client):
    client.add_cog(weeekly(client))