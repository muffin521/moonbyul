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


class weeekly(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.weeeklysoojin_gif = ["https://media.discordapp.net/attachments/782405901515751445/790061522478039041/SJ1.gif",
            "https://tenor.com/view/soojin-soojinweeekly-weeekly-weeeklysoojin-rookie2020-gif-19217007",
            "https://cdn.discordapp.com/attachments/790062429866426368/790074792190541834/SOOJIN1.gif"]

        self.bot.jiyoon_gif = ["https://media.discordapp.net/attachments/782405901515751445/790061610936958976/JY1.gif",
            "https://cdn.discordapp.com/attachments/790062585054625873/790074833609949214/JIYOON4.gif",
            "https://cdn.discordapp.com/attachments/790062585054625873/790074875695071292/JIYOON3.gif",
            "https://cdn.discordapp.com/attachments/790062585054625873/790074900815282207/JIYOON2.gif",
            "https://cdn.discordapp.com/attachments/790062585054625873/790074926430027836/JIYOON1.gif"]

        self.bot.monday_gif = ["https://media.discordapp.net/attachments/782405901515751445/790061529511886858/MD1.gif",
            "https://cdn.discordapp.com/attachments/790062662905102346/790074986702438450/MONDAY1.gif"]

        self.bot.seoun_gif = ["https://media.discordapp.net/attachments/782405901515751445/790061900464390144/SN1.gif",
            "https://media.discordapp.net/attachments/782405901515751445/790061824346161202/SN2.gif",
            "https://media.discordapp.net/attachments/782405901515751445/790061567625396224/SN3.gif"]

        self.bot.jaehee_gif = ["https://media.discordapp.net/attachments/782405901515751445/790061927333101588/JH1.gif",
            "https://media.discordapp.net/attachments/782405901515751445/790061542749372416/JH3.gif",
            "https://cdn.discordapp.com/attachments/790062758556336128/790075085779894273/JAEHEE1.gif"]

        self.bot.jihan_gif = ["https://media.discordapp.net/attachments/782405901515751445/790061636684611593/JH2.gif",
            "https://cdn.discordapp.com/attachments/790062796150407209/790075153744658442/JIHAN3.gif",
            "https://cdn.discordapp.com/attachments/790062796150407209/790075171691692032/JIHAN2.gif",
            "https://cdn.discordapp.com/attachments/790062796150407209/790075206399950908/JIHAN1.gif"]

        self.bot.zoa_gif = ["https://media.discordapp.net/attachments/782405901515751445/790061591798087690/ZA3.gif",
            "https://cdn.discordapp.com/attachments/790062825796141077/790075277409255512/ZOA1.gif",
            "https://cdn.discordapp.com/attachments/790062825796141077/790075317947203634/ZOA2.gif",
            "https://cdn.discordapp.com/attachments/790062825796141077/790075328466911272/ZOA3.gif",
            "https://cdn.discordapp.com/attachments/790062825796141077/790075355247149066/ZO4.gif"]

    @commands.command()
    async def wsoojin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Soojin :heart:')
                await ctx.send(random.choice(self.bot.weeeklysoojin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Soojin :heart:')
            await ctx.send(random.choice(self.bot.weeeklysoojin_gif))
            await ctx.message.delete()

    @commands.command()
    async def jiyoon(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jiyoon :heart:')
                await ctx.send(random.choice(self.bot.jiyoon_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jiyoon :heart:')
            await ctx.send(random.choice(self.bot.jiyoon_gif))
            await ctx.message.delete()

    @commands.command()
    async def monday(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Monday :heart:')
                await ctx.send(random.choice(self.bot.monday_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Monday :heart:')
            await ctx.send(random.choice(self.bot.monday_gif))
            await ctx.message.delete()

    @commands.command()
    async def soeun(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Soeun :heart:')
                await ctx.send(random.choice(self.bot.soeun_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Soeun :heart:')
            await ctx.send(random.choice(self.bot.soeun_gif))
            await ctx.message.delete()

    @commands.command()
    async def jaehee(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jaehee :heart:')
                await ctx.send(random.choice(self.bot.jaehee_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jaehee :heart:')
            await ctx.send(random.choice(self.bot.jaehee_gif))
            await ctx.message.delete()

    @commands.command()
    async def jihan(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jihan :heart:')
                await ctx.send(random.choice(self.bot.jihan_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jihan :heart:')
            await ctx.send(random.choice(self.bot.jihan_gif))
            await ctx.message.delete()

    @commands.command()
    async def zoa(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Zoa :heart:')
                await ctx.send(random.choice(self.bot.zoa_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Zoa :heart:')
            await ctx.send(random.choice(self.bot.zoa_gif))
            await ctx.message.delete()

def setup(client):
    client.add_cog(weeekly(client))