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
mae = 492769416610840586

class MaePings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        #10
        self.bot.krystal_gif = ["https://tenor.com/view/krystal-gif-18548219",
            "https://tenor.com/view/krystal-jung-fx-sunglasses-cute-gif-17279699",
            "https://tenor.com/view/krystal-fx-gif-5547157",
            "https://tenor.com/view/krystal-jung-jung-soojung-fx-krystal-smile-gif-14392248",
            "https://tenor.com/view/krystal-jung-soo-jung-vampire-neck-bite-gif-14254218",
            "https://tenor.com/view/soo-jung-krystal-jung-pretty-serious-gif-14167646",
            "https://tenor.com/view/krystal-jung-pose-photo-shoot-blank-stare-gif-9466254",
            "https://tenor.com/view/fx-jung-soojung-kpop-krystal-krystal-jung-gif-16701717",
            "https://tenor.com/view/rum-pum-pum-pum-pink-tape-rppp-fx-krystal-gif-17115324",
            "https://tenor.com/view/krystal-jung-jung-soojung-fx-krystal-tip-hat-gif-14392249"]

        #11
        self.bot.jessica_gif = ["https://tenor.com/view/snsd-girls-generation-jessica-jung-kpop-cute-gif-16854092",
            "https://tenor.com/view/jessica-jung-kpop-ginkoro-jessica-wonderland-gif-18005874",
            "https://tenor.com/view/jessica-jessica-jung-pose-mic-take-skirt-off-gif-15862312",
            "https://tenor.com/view/snsd-igab-igot-aboy-kpop-jessica-gif-13432098",
            "https://tenor.com/view/jessica-jung-snsd-girls-generation-gg-gif-11280338",
            "https://tenor.com/view/jessica-jung-fly-with-jess-sica-gif-5744343",
            "https://tenor.com/view/jessica-jung-my-decade-our-decade-summer-storm-jung-soo-yeon-gif-9421185",
            "https://tenor.com/view/jessica-jessica-jung-my-decade-our-decade-summer-storm-gif-9421192",
            "https://tenor.com/view/jessica-jessica-jung-my-decade-our-decade-summer-storm-gif-9421198",
            "https://tenor.com/view/jessica-jessica-jung-my-decade-our-decade-summer-storm-gif-9421190",
            "https://tenor.com/view/snsd-girlsgeneration-sone-jessica-jung-jessica-gif-6144824"]


    @commands.command()
    async def krystal(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{mae}>, <@!{ctx.author.id}> is talking about Krystal :gem:')
                await ctx.send(random.choice(self.bot.krystal_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Krystal :gem:')
            await ctx.send(random.choice(self.bot.krystal_gif))
            await ctx.message.delete()

    @commands.command()
    async def jessica(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{mae}>, <@!{ctx.author.id}> is talking about Jessica :smiling_face_with_3_hearts:')
                await ctx.send(random.choice(self.bot.jessica_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jessica :smiling_face_with_3_hearts:')
            await ctx.send(random.choice(self.bot.jessica_gif))
            await ctx.message.delete()


def setup(client):
    client.add_cog(MaePings(client))