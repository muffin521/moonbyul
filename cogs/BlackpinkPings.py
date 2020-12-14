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
muffin = 488423352206229505
gareth = 389897179701182465
jon = 109914198544240640
princessuwu = 716841614185857086

class BlackpinkPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        #25
        self.bot.rose_gif = ["https://tenor.com/view/blackpink-cute-ros%C3%A9-mini-heart-kpop-gif-14143584",
            "https://tenor.com/view/rose-blackpink-heart-sign-happy-smile-gif-11901224",
            "https://tenor.com/view/looking-let-me-see-ros%C3%A9-blackpink-rosie-gif-18118559",
            "https://tenor.com/view/blackpink-ros%C3%A9-dance-kpop-gif-14043692",
            "https://tenor.com/view/rose-blackpink-kpop-happy-smile-gif-16205441",
            "https://tenor.com/view/blackpink-gif-9219329",
            "https://tenor.com/view/rose-lovesickgirls-blackpink-kpop-thealbum-gif-18726475",
            "https://tenor.com/view/chipmunk-cute-puppy-cheeks-rose-rosie-gif-15623613",
            "https://tenor.com/view/rose-blackpink-ros%C3%A9-roseanne-cute-gif-16257627",
            "https://tenor.com/view/blackpink-rose-uwu-kpop-cute-gif-15402030",
            "https://tenor.com/view/lisa-smiling-black-pink-k-pop-cute-gif-9389777",
            "https://tenor.com/view/blackpink-blink-rose-boombayah-gif-11950271",
            "https://tenor.com/view/rose-kpop-blackpink-pairwork-recordwork-gif-14460401",
            "https://tenor.com/view/rose-jennie-black-pink-k-pop-pose-gif-9389644",
            "https://tenor.com/view/%E0%B9%82%E0%B8%A3%E0%B9%80%E0%B8%8B%E0%B9%88-clapping-cute-rose-blackpink-gif-15063856",
            "https://tenor.com/view/blackpink-rose-gif-18802619",
            "https://tenor.com/view/blackpink-rose-sexy-gif-19127868",
            "https://tenor.com/view/blackpink-rose-lovesick-girls-gif-18683755",
            "https://tenor.com/view/blackpink-roseanne-park-ros%C3%A9-surprised-gif-18344584",
            "https://tenor.com/view/blackpink-rose-gif-18802617",
            "https://tenor.com/view/rose-blackpink-balloons-cute-pretty-gif-15405146",
            "https://tenor.com/view/ros%C3%A9-kpop-blackpink-confused-gif-16895336",
            "https://tenor.com/view/blackpink-rose-heart-love-park-chae-young-gif-11783851",
            "https://tenor.com/view/blackpink-blink-rose-boombayah-gif-11950271",
            "https://tenor.com/view/blackpink-rose-gif-18530274"]

        #11
        self.bot.jennie_gif = ["https://tenor.com/view/blackpink-jennie-kpop-pretty-cute-gif-14797267",
            "https://tenor.com/view/jennie-blackpink-pretty-kpop-pose-gif-15947380",
            "https://tenor.com/view/jenniekim-gif-18818029",
            "https://tenor.com/view/blackpink-jennie-kiss-cute-gif-18818161",
            "https://tenor.com/view/blackpink-jennie-cute-smile-kpop-gif-14004531",
            "https://tenor.com/view/kiss-jennie-gif-14662350",
            "https://tenor.com/view/jennie-kim-blackpink-bed-jennie-kpop-gif-12627702",
            "https://tenor.com/view/jenny-jennie-kim-blackpink-cute-gif-12481536",
            "https://tenor.com/view/blackpink-jennie-kpop-saranghae-gif-14797258",
            "https://tenor.com/view/blackpink-jennie-jenniekim-jendeukkie-jenjen-gif-9256813",
            "https://tenor.com/view/jennie-blackpink-gif-14036697"]

        #7
        self.bot.lisa_gif = ["https://tenor.com/view/lalisa-manoban-lisa-blackpink-lollipop-kpop-gif-17772815",
            "https://tenor.com/view/lisa-smile-black-pink-kpop-cute-gif-16464316",
            "https://tenor.com/view/lisa-blackpink-cute-girl-gif-15983564",
            "https://tenor.com/view/hi-hello-wave-lisa-lalisa-gif-14924995",
            "https://tenor.com/view/lisa-lisa-blackpink-blackpink-blackpink-lisa-gif-18095773",
            "https://tenor.com/view/ayeah-ayeah-pointing-smile-cute-lisa-gif-16007292",
            "https://tenor.com/view/lisa-lalisa-lalisa-manoban-mentor-lisa-kpop-gif-17299890"]

        #7
        self.bot.jisoo_gif = ["https://tenor.com/view/jisoo-kimjisoo-visual-kpop-blackpink-gif-10720121",
            "https://tenor.com/view/blackpink-kpop-kim-jisoo-jisoo-lead-vocalist-gif-17967342",
            "https://tenor.com/view/blackpink-kpop-kim-jisoo-jisoo-lead-vocalist-gif-17944860",
            "https://tenor.com/view/jisoo-gif-18486243",
            "https://tenor.com/view/blackpink-kim-jisoo-why-what-the-gif-12589646",
            "https://tenor.com/view/jisoo-sexy-blackpink-kpop-gif-15419500",
            "https://tenor.com/view/jisoo-weekly-idol-blackpink-lisa-rose-gif-8481189"]

    @commands.command(aliases=['jendeukkie'])
    async def jennie(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@{gareth}>, <@{jon}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jennie :dumpling:')
                await ctx.send(random.choice(self.bot.jennie_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jennie :dumpling:')
            await ctx.send(random.choice(self.bot.jennie_gif))
            await ctx.message.delete()

    @commands.command(aliases=['rosé'])
    async def rose(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{gareth}>, <@{jon}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Rosé :rose:')
                await ctx.send(random.choice(self.bot.rose_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=6)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Rosé :rose:')
            await ctx.send(random.choice(self.bot.rose_gif))
            await ctx.message.delete()

    @commands.command()
    async def lisa(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{gareth}>, <@{jon}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Lisa :cat:')
                await ctx.send(random.choice(self.bot.lisa_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Lisa :cat:')
            await ctx.send(random.choice(self.bot.lisa_gif))
            await ctx.message.delete()

    @commands.command()
    async def jisoo(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{gareth}>, <@{jon}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jisoo :turtle: :rabbit2:')
                await ctx.send(random.choice(self.bot.jisoo_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jisoo :turtle: :rabbit2:')
            await ctx.send(random.choice(self.bot.jisoo_gif))
            await ctx.message.delete()


def setup(client):
    client.add_cog(BlackpinkPings(client))