import discord, random
from discord.ext import commands

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

class CherryBullet(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.jiwon_gif = ["https://tenor.com/view/jiwon-cherrybullet-gif-19267608",
            "https://tenor.com/view/jiwon-cherrybullet-gif-19267631",
            "https://tenor.com/view/jiwon-cherrybullet-gif-19267645",
            "https://tenor.com/view/jiwon-cherrybullet-gif-19267642",
            "https://tenor.com/view/jiwon-cherrybullet-gif-19267587",
            "https://tenor.com/view/jiwon-cherry-bullet-pose-kpop-pretty-gif-16634902",
            "https://tenor.com/view/jiwon-cherrybullet-gif-19267648",
            "https://tenor.com/view/cherry-bullet-jiwon-may-kpop-cute-gif-16641928",
            "https://gfycat.com/neglectedgrandioseimperatorangel",
            "https://gfycat.com/immaculateidealisticarabianhorse",
            "https://gfycat.com/untidybravefattaileddunnart"]

        self.bot.yuju_gif = ["https://tenor.com/view/yuju-cherry-bullet-kpop-huh-suprised-gif-17717737",
            "https://tenor.com/view/yuju-cherry-bullet-kpop-huh-suprised-gif-17717737",
            "https://tenor.com/view/cherry-bullet-yuju-pretty-girl-smiling-gif-16634873",
            "https://tenor.com/view/cherry-bullet-yuju-cherry-bullet-smile-kpop-cute-gif-17717767",
            "https://tenor.com/view/cherry-bullet-yuju-kpop-dancing-cute-gif-17717719",
            "https://tenor.com/view/yuju-cherry-bullet-kpop-cute-smile-gif-16634882",
            "https://tenor.com/view/yuju-cherry-bullet-kpop-cute-pretty-gif-17717763",
            "https://tenor.com/view/yuju-cherry-bullet-yuju-smile-heart-cute-gif-17717728",
            "https://tenor.com/view/cherry-bullet-yuju-yuju-cherry-bullet-gif-15959991",
            "https://tenor.com/view/cherry-bullet-yuju-cute-gif-15054827"]

    @commands.command()
    async def jiwon(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jiwon :heart:')
                await ctx.send(random.choice(self.bot.jiwon_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jiwon :heart:')
            await ctx.send(random.choice(self.bot.jiwon_gif))
            await ctx.message.delete()

    @commands.command()
    async def yuju(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yuju :heart:')
                await ctx.send(random.choice(self.bot.yuju_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yuju :heart:')
            await ctx.send(random.choice(self.bot.yuju_gif))
            await ctx.message.delete()
        

def setup(client):
    client.add_cog(CherryBullet(client))