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
ple = 416903886968979466
mae = 492769416610840586

class PlePings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        #8
        self.bot.kiki_gif = ["https://tenor.com/view/xu-kiki-xu-jiaqi-7senses-the9-snh48-gif-17740947",
            "https://tenor.com/view/xu-jiaqi-kiki-7senses-snh48-slide-gif-17754236",
            "https://tenor.com/view/xu-jiaqi-pretty-cute-kiki-7senses-gif-17837322",
            "https://tenor.com/view/xu-jiaqi-kiki-7senses-snh48-smile-gif-17946346",
            "https://tenor.com/view/xu-jiaqi-kiki-7senses-snh48-smile-gif-17946344",
            "https://tenor.com/view/xu-jiaqi-kiki-xu-7senses-the9-snh48-gif-17754440",
            "https://tenor.com/view/xu-jiaqi-snh48-kiki-7senses-hat-gif-15001516",
            "https://tenor.com/view/kiki-xu-jiaqi-mama-mama-kiki-xu-jiaqi-dance-gif-17098415"]


    #kiki command for ple and mae
    @commands.command()
    async def kiki(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{ple}>, <@{mae}>, <@!{ctx.author.id}> is talking about Kiki')
                await ctx.send(random.choice(self.bot.kiki_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@416903886968979466>, <@492769416610840586>, <@!{ctx.author.id}> is talking about Kiki')
            await ctx.send(random.choice(self.bot.kiki_gif))
            await ctx.message.delete()


def setup(client):
    client.add_cog(PlePings(client))