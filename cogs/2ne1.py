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
k8 = 573974040679809044

class twoneone(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.cl_gif = ["https://media.discordapp.net/attachments/771238115255255060/785288565273788426/image2.gif",
            "https://media.discordapp.net/attachments/771238115255255060/785288564912160819/image1.gif",
            "https://media.discordapp.net/attachments/771238115255255060/785288541785161758/image0.gif",
            "https://tenor.com/view/cl-hello-bitches-group-show-gif-14566826",
            "https://tenor.com/view/2ne1-cl-chaelin-chaerin-chaelin-lee-gif-7177115",
            "https://tenor.com/view/cl-kpop-performance-singer-gif-14566821",
            "https://tenor.com/view/cl-2ne1-rapper-korean-k-pop-gif-9210983",
            "https://tenor.com/view/2ne1-hello-kpop-hi-gif-14032003",
            "https://tenor.com/view/2ne1-chaelin-cl-chaelin-lee-mocking-gif-7177330",
            "https://tenor.com/view/2ne1-dara-minzy-bom-cl-gif-5103125",
            "https://cdn.discordapp.com/attachments/703871901411573850/795765505129840650/iu.gif",
            "https://cdn.discordapp.com/attachments/703871901411573850/795765936542973972/image0.gif"]

        self.bot.dara_gif = ["https://tenor.com/view/dara-sandarapark-sandara-2ne1-yg-gif-5071907",
            "https://tenor.com/view/dara-sandara-sandara-park-kpop-2ne1-gif-19666838",
            "https://tenor.com/view/dara-sandara-sandara-park-christmas-2ne1-gif-19697500",
            "https://tenor.com/view/dara-sandarapark-sandara-2ne1-kpop-gif-5071924",
            "https://tenor.com/view/dara-sandara-sandarapark-2ne1-kpop-gif-5071937",
            "https://tenor.com/view/sandara-dara-sandara-park-2ne1-gif-19091348",
            "https://tenor.com/view/sandara-dara-sandara-park-2ne1-gif-19313220",
            "https://tenor.com/view/sandara-dara-sandara-park-2ne1-gif-19313227",
            "https://tenor.com/view/sandara-dara-sandara-park-2ne1-gif-19313230",
            "https://tenor.com/view/sandara-park-dara-sandara-2ne1-gif-19182492",
            "https://tenor.com/view/sandara-park-dara-sandara-2ne1-gif-19182590",
            "https://tenor.com/view/sandara-sandara-park-dara-2ne1-idol-league-gif-19103825",
            "https://tenor.com/view/sandara-sandara-park-dara-2ne1-2ne1dara-gif-19091237",
            "https://tenor.com/view/sandara-park-sandara-dara-2ne1-gif-19182284",
            "https://tenor.com/view/sandara-para-sandara-dara-2ne1-gif-19182374",
            "https://tenor.com/view/sandara-dara-2ne1-pentagon-hongseok-gif-19182561",
            "https://tenor.com/view/sandara-sandara-park-dara-2ne1-gif-19182477",
            "https://tenor.com/view/sandara-dara-sandara-park-2ne1-gif-19313221",
            "https://tenor.com/view/sandara-park-kpop-dara-2ne1-gif-19194618",
            "https://tenor.com/view/nodding-%EC%82%B0%EB%8B%A4%EB%9D%BC%EB%B0%95-mnet-asian-music-awards-rhythm-artist-reaction-gif-19237338",
            "https://tenor.com/view/k-pop-korean-2ne1-sandara-dara-gif-5071999",
            "https://tenor.com/view/sandara-dara-sandara-park-2ne1-kpop-gif-19051398",
            "https://tenor.com/view/omg-oh-my-god-kpop-gif-5427305"]

        self.bot.parkbom_gif = ["https://cdn.discordapp.com/attachments/703871901411573850/795766103766466570/image1.gif",
            "https://cdn.discordapp.com/attachments/703871901411573850/795766103010836510/image0.gif"]

        self.bot.minzy_gif = [""]

        self.bot.twoneone_gif = ["https://cdn.discordapp.com/attachments/703871901411573850/795766230652944444/image0.gif"]

    @commands.command(aliases = ['2ne1'])
    async def twoneone(self, ctx, arg="2ne1"):
        if arg == "cl":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{k8}>, <@!{ctx.author.id}> is talking about CL :cherries: ')
                    await ctx.send(random.choice(self.bot.cl_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about CL :cherries:')
                await ctx.send(random.choice(self.bot.cl_gif))
                await ctx.message.delete()
        elif arg == "dara":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Dara :heart: ')
                await ctx.send(random.choice(self.bot.dara_gif))
                await ctx.message.delete()
        else:
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about 2NE1 :heart: ')
                await ctx.send(random.choice(self.bot.twoneone_gif))
                await ctx.message.delete()


    @commands.command()
    async def dara(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Dara :heart: ')
                await ctx.send(random.choice(self.bot.dara_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Dara :heart: ')
            await ctx.send(random.choice(self.bot.dara_gif))
            await ctx.message.delete()

def setup(client):
    client.add_cog(twoneone(client))