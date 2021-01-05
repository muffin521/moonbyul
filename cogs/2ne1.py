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
            "https://cdn.discordapp.com/attachments/703871901411573850/795765936542973972/image0.gif",
            "https://cdn.discordapp.com/attachments/703871901411573850/795773049114460170/iu-1.gif",
            "https://cdn.discordapp.com/attachments/703871901411573850/795773274193002496/iu-4.gif",
            "https://i.makeagif.com/media/10-01-2015/qGFLrI.gif",
            "https://cdn.discordapp.com/attachments/703871901411573850/795779083686248489/iu-13.gif",
            "https://tenor.com/view/smile-%EC%94%A8%EC%97%98-mnet-asian-music-awards-winner-award-acceptance-speech-gif-19237320",
            "https://tenor.com/view/cl-kpop-lee-chaelin-2ne1-gif-19502722",
            "https://tenor.com/view/cl-2ne1-i-am-the-best-bat-ready-to-fight-gif-14343853",
            "https://tenor.com/view/cl-2ne1-kpop-gif-7398496"]

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
            "https://tenor.com/view/omg-oh-my-god-kpop-gif-5427305",
            "https://cdn.discordapp.com/attachments/703871901411573850/795773065274589214/iu-7.gif",
            "https://cdn.discordapp.com/attachments/703871901411573850/795774289742659644/iu-14.gif",
            "https://i.makeagif.com/media/10-01-2015/qGFLrI.gif",
            "https://cdn.discordapp.com/attachments/703871901411573850/795779150849769532/iu-19.gif",
            "https://cdn.discordapp.com/attachments/302268299729829888/795826916824317962/image0.gif"]

        self.bot.parkbom_gif = ["https://cdn.discordapp.com/attachments/703871901411573850/795766103766466570/image1.gif",
            "https://cdn.discordapp.com/attachments/703871901411573850/795766103010836510/image0.gif",
            "https://cdn.discordapp.com/attachments/703871901411573850/795772912208445440/iu-11.gif",
            "https://cdn.discordapp.com/attachments/703871901411573850/795773065274589214/iu-7.gif",
            "https://cdn.discordapp.com/attachments/703871901411573850/795773104982982697/iu-10.gif",
            "https://cdn.discordapp.com/attachments/703871901411573850/795773240948555846/iu-3.gif",
            "https://i.makeagif.com/media/10-01-2015/qGFLrI.gif",
            "https://tenor.com/view/clap-bom-2ne1-kpop-happy-gif-5427306",
            "https://tenor.com/view/park-bom-bom-2ne1-korean-k-pop-gif-10711083",
            "https://tenor.com/view/park-bom-bom-2ne1-korean-k-pop-gif-10711108",
            "https://tenor.com/view/poodle-waking-the-dog-walk-it-out-black-boots-leather-boots-gif-19633759",
            "https://tenor.com/view/parkbom-bom-2ne1-kpop-gif-5071942",
            "https://tenor.com/view/park-bom-kpop-korean-hallyu-korean-group-gif-10743495",
            "https://tenor.com/view/park-bom-kpop-gif-10743564",
            "https://tenor.com/view/hairfilp-kpop-sassy-i-dont-care-gif-4299716",
            "https://tenor.com/view/park-bom-bom-2ne1-korean-k-pop-gif-10711082",
            "https://tenor.com/view/elusive-elusivecaution-gif-19734281",
            "https://tenor.com/view/kpop-2ne1-park-bom-dance-stage-gif-4835748",
            "https://tenor.com/view/cute-baby-korean-k-pop-gif-11564235",
            "https://tenor.com/view/2015mama-mama-moment-performance-music-kpop-gif-19227329",
            "https://tenor.com/view/gif-gif-19492358",
            "https://tenor.com/view/k-pop-korean-2ne1-bom-park-park-bom-gif-4848962",
            "https://tenor.com/view/park-bom-singer-kpop-cute-pretty-gif-16199257",
            "https://tenor.com/view/park-bom-selfie-2ne1-pout-kpop-gif-16272494",
            "https://tenor.com/view/park-bom-bom-dan%C3%A7ando-park-bom-dan%C3%A7ando-park-bom-dan%C3%A7ando-loira-dancing-gif-17924647",
            "https://tenor.com/view/park-bom-bom-2ne1-korean-k-pop-gif-10711068",
            "https://tenor.com/view/parkbom-bom-2ne1-yg-kpop-gif-5071909",
            "https://cdn.discordapp.com/attachments/302268299729829888/795826916824317962/image0.gif"]

        self.bot.minzy_gif = ["https://tenor.com/view/minzy-2ne1-yg-kong-smile-gif-12482219",
            "https://tenor.com/view/dance-moves-split-kpop-minzy-2ne1-gif-13861313",
            "https://tenor.com/view/2015mama-mama-moment-performance-music-kpop-gif-19237043",
            "https://tenor.com/view/minzy-2ne1-k-pop-korean-surprised-gif-9415044",
            "https://tenor.com/view/minzy-kpop-korean-2ne1-gif-10711124",
            "https://tenor.com/view/gong-minji-headbang-headbanging-dance-dancing-gif-12501580",
            "https://tenor.com/view/minjilangmalakas-boast-minjimalakas-minzylangmalakas-gif-19315676",
            "https://tenor.com/view/minzy-2ne1-2ne1minzy-kongminjy-k-pop-gif-9852303",
            "https://cdn.discordapp.com/attachments/703871901411573850/795779043529195530/iu-8.gif"]

        self.bot.twoneone_gif = ["https://cdn.discordapp.com/attachments/703871901411573850/795766230652944444/image0.gif",
            "https://tenor.com/view/gong-minji-headbang-headbanging-dance-dancing-gif-12501580",
            "https://tenor.com/view/2010mama-mama-moment-%ED%88%AC%EC%95%A0%EB%8B%88%EC%9B%90-2ne1-performance-gif-19226161",
            "https://tenor.com/view/2009mama-mama-moment-%ED%88%AC%EC%95%A0%EB%8B%88%EC%9B%90-2ne1-music-gif-19227595",
            "https://tenor.com/view/2011mama-mama-moment-%ED%88%AC%EC%95%A0%EB%8B%88%EC%9B%90-2ne1-performance-gif-19226797",
            "https://tenor.com/view/2011mama-mama-moment-%ED%88%AC%EC%95%A0%EB%8B%88%EC%9B%90-2ne1-winner-gif-19226800",
            "https://tenor.com/view/2ne1-camera-posing-pose-gif-4991259",
            "https://tenor.com/view/2ne1-kpop-korean-dance-moves-gif-10518831",
            "https://tenor.com/view/2ne1-gif-11836282",
            "https://cdn.discordapp.com/attachments/703871901411573850/795773017350864976/iu-6.gif",
            "https://cdn.discordapp.com/attachments/703871901411573850/795773372318351390/iu-2.gif",
            "https://cdn.discordapp.com/attachments/302268759140335617/795816068119658536/say_what_2ne1.gif"]

    @commands.command(aliases = ['2ne1'])
    async def twoneone(self, ctx, *, arg="2ne1"):
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
                await ctx.send(f'<@!{ctx.author.id}> is talking about Dara :heart:')
                await ctx.send(random.choice(self.bot.dara_gif))
                await ctx.message.delete()
        elif arg == "park bom" or arg == "bom":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Park Bom :corn:')
                await ctx.send(random.choice(self.bot.parkbom_gif))
                await ctx.message.delete()
        elif arg == "minzy" or arg == "minji":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Minzy :corn:')
                await ctx.send(random.choice(self.bot.minzy_gif))
                await ctx.message.delete()
        else:
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about 2NE1 :heart:')
                await ctx.send(random.choice(self.bot.twoneone_gif))
                await ctx.message.delete()

def setup(client):
    client.add_cog(twoneone(client))