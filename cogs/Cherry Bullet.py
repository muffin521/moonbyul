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
ple = 416903886968979466

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

        self.bot.chebulyuju_gif = ["https://tenor.com/view/yuju-cherry-bullet-kpop-huh-suprised-gif-17717737",
            "https://tenor.com/view/yuju-cherry-bullet-kpop-huh-suprised-gif-17717737",
            "https://tenor.com/view/cherry-bullet-yuju-pretty-girl-smiling-gif-16634873",
            "https://tenor.com/view/cherry-bullet-yuju-cherry-bullet-smile-kpop-cute-gif-17717767",
            "https://tenor.com/view/cherry-bullet-yuju-kpop-dancing-cute-gif-17717719",
            "https://tenor.com/view/yuju-cherry-bullet-kpop-cute-smile-gif-16634882",
            "https://tenor.com/view/yuju-cherry-bullet-kpop-cute-pretty-gif-17717763",
            "https://tenor.com/view/yuju-cherry-bullet-yuju-smile-heart-cute-gif-17717728",
            "https://tenor.com/view/cherry-bullet-yuju-yuju-cherry-bullet-gif-15959991",
            "https://tenor.com/view/cherry-bullet-yuju-cute-gif-15054827"]

        self.bot.chebulhaeyoon_gif = ["https://tenor.com/view/haeyoon-gif-19633020",
            "https://tenor.com/view/haeyoon-gif-19633021",
            "https://tenor.com/view/haeyoon-gif-19633019",
            "https://tenor.com/view/haeyoon-gif-19633018",
            "https://tenor.com/view/haeyoon-gif-19633017",
            "https://tenor.com/view/open-mouth-ahh-jawdrop-blank-cherrybullet-gif-14606312"]

        self.bot.chebulbora_gif = ["https://tenor.com/view/bora-chabul-gif-19633080",
            "https://tenor.com/view/bora-chebul-gif-19633077",
            "https://tenor.com/view/bora-chebul-gif-19633078",
            "https://tenor.com/view/bora-chebul-gif-19633079",
            "https://tenor.com/view/kcon2019japan-kcon-%EC%BC%80%EC%9D%B4%EC%BD%98-m-countdown-mnet-gif-14557828"]

    @commands.command()
    async def cherry(self, ctx, bullet, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Cherry Bullet {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if bullet == "bullet":
            if arg == "jiwon":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@{ple}>, <@!{ctx.author.id}> is talking about Jiwon :heart:')
                        await ctx.send(random.choice(self.bot.jiwon_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Jiwon :heart:')
                    await ctx.send(random.choice(self.bot.jiwon_gif))
                    await ctx.message.delete()
            elif arg == "yuju":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Yuju :heart:')
                    await ctx.send(random.choice(self.bot.chebulyuju_gif))
                    await ctx.message.delete()
            elif arg == "haeyoon":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Haeyoon :heart:')
                    await ctx.send(random.choice(self.bot.chebulhaeyoon_gif))
                    await ctx.message.delete()
            elif arg == "bora":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Bora :heart:')
                    await ctx.send(random.choice(self.bot.chebulbora_gif))
                    await ctx.message.delete()

    @commands.command()
    async def jiwon(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{ple}>, <@!{ctx.author.id}> is talking about Jiwon :heart:')
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
                await ctx.send(random.choice(self.bot.chebulyuju_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yuju :heart:')
            await ctx.send(random.choice(self.bot.chebulyuju_gif))
            await ctx.message.delete()
        
    @commands.command()
    async def haeyoon(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Haeyoon :heart:')
                await ctx.send(random.choice(self.bot.chebulhaeyoon_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Haeyeoon :heart:')
            await ctx.send(random.choice(self.bot.chebulhaeyoon_gif))
            await ctx.message.delete()

    @commands.command()
    async def bora(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Bora :heart:')
                await ctx.send(random.choice(self.bot.chebulbora_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Bora :heart:')
            await ctx.send(random.choice(self.bot.chebulbora_gif))
            await ctx.message.delete()


def setup(client):
    client.add_cog(CherryBullet(client))