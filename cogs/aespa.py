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
k8 = 573974040679809044
mae = 492769416610840586
rith = 346724857725059075

class aespaPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.giselle_gif = ["https://cdn.discordapp.com/attachments/771238115255255060/781338667973214208/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338668513886208/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338669524975616/image2.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338670694531072/image3.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338671202304087/image4.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338671714271282/image5.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338672481173514/image6.gif",
            "https://gfycat.com/badtepidhyracotherium",
            "https://gfycat.com/adeptwellgroomedhorse",
            "https://gfycat.com/thankfulmammothamericanindianhorse",
            "https://gfycat.com/craftythinibex",
            "https://gfycat.com/knobbyimpressionablefennecfox",
            "https://gfycat.com/imaginaryoldfashionedbrahmancow",
            "https://gfycat.com/aridenchantingegret",
            "https://gfycat.com/imperfectthoroughladybug",
            "https://gfycat.com/periodicillegaleasternglasslizard",
            "https://gfycat.com/unlawfulshamefulbabirusa",
            "https://gfycat.com/likelyreadykinkajou",
            "https://gfycat.com/livelybigheartedamericantoad",
            "https://gfycat.com/specificinfatuateddikkops",
            "https://gfycat.com/wickedgrizzledchrysomelid",
            "https://gfycat.com/thatnecessarycolt",
            "https://gfycat.com/defenselesseverlastingguppy",
            "https://gfycat.com/gentledecimalgalapagosdove",
            "https://gfycat.com/untriedblankdoe",
            "https://gfycat.com/lankyfatherlyamericanredsquirrel",
            "https://gfycat.com/enragedlazycowrie",
            "https://gfycat.com/disguisedcreamykiwi",
            "https://gfycat.com/scornfulequalharlequinbug",
            "https://gfycat.com/nervouseasygoingandeancondor",
            "https://gfycat.com/weehideousaddax",
            "https://gfycat.com/warmheartedrequiredcirriped",
            "https://gfycat.com/fancytalkativefairyfly",
            "https://gfycat.com/unripegraciousivorygull-giselle-aespa",
            "https://gfycat.com/badtepidhyracotherium-giselle-aespa",
            "https://gfycat.com/blissfulcleankoi-giselle-aespa",
            "https://gfycat.com/forsakensophisticatedacornwoodpecker-aespa-giselle-black-mamba-girl-group-kpop-aeri",
            "https://gfycat.com/violetpointlesscolt-giselle-aespa",
            "https://gfycat.com/samesoggyaddax-giselle-aespa",
            "https://gfycat.com/yearlyfemininelemming-giselle-aespa",
            "https://gfycat.com/bewitchedmediocreindianelephant",
            "https://gfycat.com/thisshabbyhumpbackwhale",
            "https://gfycat.com/immediateyellowindianrockpython",
            "https://gfycat.com/likelyscarydormouse",
            "https://gfycat.com/goodnaturedimmensecentipede"]

        self.bot.winter_gif = ["https://tenor.com/view/aespa-archive_aespa-winter-aespa-winter-winter-aespa-gif-19207739",
            "https://tenor.com/view/aespa-winter-aespa-winter-aespa-kim-minjeong-kim-minjeong-gif-19029912",
            "https://tenor.com/view/aespa-%EC%97%90%EC%8A%A4%ED%8C%8C-%EC%9C%88%ED%84%B0-winter-gif-19207490",
            "https://tenor.com/view/archive_aespa-aespa-winter-aespa-winter-minjeong-gif-19138516",
            "https://tenor.com/view/winter-aespa-aespa-gif-19226090",
            "https://tenor.com/view/winter-aespa-aespa-gif-19323697",
            "https://cdn.discordapp.com/attachments/771238115255255060/781388912189898752/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781388912873832473/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781388914480513064/image2.gif",
            "https://gfycat.com/gloriousenergetickoala",
            "https://gfycat.com/achinglargecicada",
            "https://gfycat.com/blondunkemptchipmunk",
            "https://gfycat.com/blindanimatedborderterrier",
            "https://gfycat.com/bigcheerfuliberiannase",
            "https://gfycat.com/fancyshydrongo",
            "https://gfycat.com/phonydeficientcomet",
            "https://gfycat.com/scrawnyfarflungkilldeer",
            "https://gfycat.com/testyjovialchicken",
            "https://gfycat.com/acclaimedclearhatchetfish",
            "https://gfycat.com/healthyimaginativekillerwhale",
            "https://gfycat.com/clutteredtenseamericanblackvulture",
            "https://gfycat.com/definitiverapidbuckeyebutterfly",
            "https://gfycat.com/snarlingpastglobefish",
            "https://gfycat.com/directpettygermanshepherd",
            "https://gfycat.com/maleindelibleaxolotl",
            "https://gfycat.com/hastysparsedeermouse",
            "https://gfycat.com/heartfeltquarrelsomeekaltadeta",
            "https://gfycat.com/bleakdistanthare",
            "https://gfycat.com/cluelessbowedbarnowl"]

        self.bot.ningning_gif = ["https://cdn.discordapp.com/attachments/747275528993636424/781391569986125824/7226125c-1e30-4c1d-b3a9-f6a71db55fad.gif",
            "https://cdn.discordapp.com/attachments/747275528993636424/781391570829836308/3ee3defb-5472-48b9-b5ef-743984c6996d.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782482430879596544/giphy_1.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782482991351463966/tenor_1.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782482998293430302/tenor.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782483030086385714/MediumFlickeringFrogmouth-max-1mb.gif",
            "https://tenor.com/view/ningning-aespa-crying-shaking-fist-gif-19355492",
            "https://tenor.com/view/aespa-giselle-karina-ningning-winter-gif-19293865",
            "https://gfycat.com/opulentamusinggalago",
            "https://gfycat.com/pointedoldafghanhound",
            "https://gfycat.com/slipperyblackandwhiteacornweevil",
            "https://gfycat.com/inexperiencedimperturbablebluejay",
            "https://gfycat.com/fragrantenlightenedgerenuk",
            "https://gfycat.com/glumhighlevelindianabat",
            "https://gfycat.com/understatedacceptableargentinehornedfrog",
            "https://gfycat.com/flippantpresentivorygull",
            "https://gfycat.com/easygoingfixedafghanhound",
            "https://gfycat.com/educateddearestcob",
            "https://gfycat.com/peacefulredargentineruddyduck",
            "https://gfycat.com/consciousnextamericanbulldog",
            "https://gfycat.com/brownimpossibleasianconstablebutterfly",
            "https://gfycat.com/unlawfulgreatlark",
            "https://gfycat.com/practicalfancyantarcticfurseal",
            "https://gfycat.com/specificvastbear",
            "https://tenor.com/view/black-mamba-aespa-ningning-aespa-ningning-kpop-gif-19881136",
            "https://tenor.com/view/aespa-ningning-aespa-ningning-archive_aespa-archive-aespa-gif-19196653",
            "https://tenor.com/view/ning-ning-yizhuo-ningning-yizhuo-aespa-gif-19000866"]

        self.bot.karina_gif = ["https://cdn.discordapp.com/attachments/772980032086999090/782482078616125470/giphy.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782482080427671552/20201028144417-7ae7.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782482084324966430/giphy1.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782482084869832724/tumblr_0cac220cdb85f9cf71d97263a7935097_de5c9738_540.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782482091320803328/original.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782482091656871956/HardRemorsefulFlicker-size_restricted.gif",
            "https://gfycat.com/tightharmfularizonaalligatorlizard",
            "https://gfycat.com/antiquesarcasticeyas",
            "https://gfycat.com/mildweehake",
            "https://gfycat.com/jovialcrazycoral",
            "https://gfycat.com/shabbysarcasticharborseal",
            "https://gfycat.com/fancyunfitgalago",
            "https://gfycat.com/distinctneatcutworm",
            "https://gfycat.com/gracefulperfectbasilisk",
            "https://gfycat.com/disguisedcomposedbunny",
            "https://gfycat.com/bronzehighlevelharrierhawk",
            "https://gfycat.com/ultimateweirdhapuku",
            "https://gfycat.com/shinyfewazurevasesponge",
            "https://gfycat.com/eagerscrawnykob",
            "https://gfycat.com/gaseoussprycentipede",
            "https://gfycat.com/slushyinsignificantboto",
            "https://gfycat.com/heartfeltwickedarchaeocete",
            "https://gfycat.com/tenseadorablegreendarnerdragonfly",
            "https://gfycat.com/portlyblandanophelesmosquito",
            "https://gfycat.com/blackdisfiguredgourami",
            "https://gfycat.com/alienatednaughtycapybara",
            "https://gfycat.com/thosetandamselfly"]

    @commands.command()
    async def aespa(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [aespa {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "giselle":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{k8}>, <@{rith}> <@!{ctx.author.id}> is talking about Giselle :crescent_moon: ')
                    await ctx.send(random.choice(self.bot.giselle_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Giselle :crescent_moon:')
                await ctx.send(random.choice(self.bot.giselle_gif))
                await ctx.message.delete()
        elif arg == "winter":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{k8}>, <@{mae}>, <@{rith}> <@!{ctx.author.id}> is talking about Winter :star: ')
                    await ctx.send(random.choice(self.bot.winter_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Winter :star:')
                await ctx.send(random.choice(self.bot.winter_gif))
                await ctx.message.delete()
        elif arg == "ningning" or arg == "ning ning":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{k8}>, <@{mae}>, <@{rith}> <@!{ctx.author.id}> is talking about Ningning :star: ')
                    await ctx.send(random.choice(self.bot.ningning_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Ningning :star:')
                await ctx.send(random.choice(self.bot.ningning_gif))
                await ctx.message.delete()
        elif arg == "karina":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Karnia :star: ')
                    await ctx.send(random.choice(self.bot.karina_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Karina :star:')
                await ctx.send(random.choice(self.bot.karina_gif))
                await ctx.message.delete()


def setup(client):
    client.add_cog(aespaPings(client))
