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
muffin = 488423352206229505

class PurpleKiss(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.yuki_gif = ["https://gfycat.com/slipperydecisiveindianspinyloach-purple-kiss-purple-kss-kpop-yuki",
            "https://gfycat.com/waterloggedwatchfulasianconstablebutterfly",
            "https://gfycat.com/tamegloomyamphibian",
            "https://gfycat.com/snivelingfatalgangesdolphin",
            "https://gfycat.com/definitivedeterminedantlion",
            "https://gfycat.com/glaringglitteringdore",
            "https://tenor.com/view/yuki-purple-kiss-gif-19356715",
            "https://tenor.com/view/yuki-hamster-laughing-cute-purple-kiss-gif-19603707",
            "https://cdn.discordapp.com/attachments/547946757594677268/806562700624396298/image0.gif",
            "https://cdn.discordapp.com/attachments/547946757594677268/806562701023248404/image1.gif",
            "https://cdn.discordapp.com/attachments/547946757594677268/806572183647813662/image0.gif",
            "https://cdn.discordapp.com/attachments/547946757594677268/806572210495553588/image0.gif",
            "https://cdn.discordapp.com/attachments/547946757594677268/806682389069037638/image0.gif",
            "https://tenor.com/view/mori-koyuki-yuki-purple-kiss-mworikoyuki-gif-20125374"]

        self.bot.nagoeun_gif = ["https://gfycat.com/BiodegradableBackClam",
            "https://gfycat.com/FrightenedQuarrelsomeHare",
            "https://gfycat.com/PortlySillyAnemone",
            "https://gfycat.com/HonorableSorrowfulHypacrosaurus",
            "https://gfycat.com/AdmiredWeightyGlowworm",
            "https://gfycat.com/LavishSneakyIcelandicsheepdog",
            "https://media.discordapp.net/attachments/762508629680586775/783175861875638302/goeun_heart_gif.gif",
            "https://gfycat.com/whitegoldenbirdofparadise",
            "https://gfycat.com/heartfelthelpfulgrayfox",
            "https://gfycat.com/glisteninguncommonilladopsis",
            "https://gfycat.com/smugraregreendarnerdragonfly",
            "https://gfycat.com/evenperkyfiddlercrab",
            "https://gfycat.com/enragedsoftenglishpointer",
            "https://media.discordapp.net/attachments/547900536565924104/740000852214808772/20200803_201852.gif",
            "https://media.discordapp.net/attachments/547900536565924104/739996247850483863/20200803_200002.gif",
            "https://media.discordapp.net/attachments/547946725592137728/740189250909372516/20200804_082123.gif",
            "https://media.discordapp.net/attachments/547946725592137728/739990286976942100/20200803_193527.gif",
            "https://tenor.com/view/purple-kiss-na-goeun-goeun-purplekiss-goeun-dancing-gif-17914994",
            "https://tenor.com/view/go-eun-chaein-purple-kiss-gif-19356750",
            "https://tenor.com/view/goeun-purplekiss-purple_kiss-nagoeun-gif-19540241",
            "https://tenor.com/view/goeun-nagoeun-purple-kiss-purple_kiss-gif-19673140",
            "https://tenor.com/view/eunnie-line-eunseo-dosie-goeun-eunseong-gif-19614430",
            "https://tenor.com/view/goeun-nagoeun-purplekiss-purple_kiss-gif-19614340",
            "https://tenor.com/view/goeun-nagoeun-purplekiss-purple_kiss-gif-19614407",
            "https://cdn.discordapp.com/attachments/547946725592137728/806563805344956486/image0.gif",
            "https://cdn.discordapp.com/attachments/547946725592137728/806563851112939548/image0.gif",
            "https://cdn.discordapp.com/attachments/547946725592137728/806563909406163005/image0.gif",
            "https://cdn.discordapp.com/attachments/547946725592137728/806566140317925476/image0.gif",
            "https://cdn.discordapp.com/attachments/547946725592137728/806570760381530122/image0.gif",
            "https://cdn.discordapp.com/attachments/547946725592137728/806597242801750046/PURPLE_KISS_Can_We_Talk_Again_MV.gif",
            "https://cdn.discordapp.com/attachments/547946725592137728/806603169541914644/PURPLE_KISS_Can_We_Talk_Again_MV_1.gif",
            "https://cdn.discordapp.com/attachments/547946725592137728/806682296023121950/image0.gif"]

        self.bot.jieun_gif = ["https://gfycat.com/ComposedPlayfulAmethystgemclam",
            "https://gfycat.com/VastDistantAnophelesmosquito",
            "https://gfycat.com/PitifulPleasedCassowary",
            "https://gfycat.com/BabyishFrankAttwatersprairiechicken",
            "https://gfycat.com/RarePleasedJunebug",
            "https://cdn.discordapp.com/attachments/547946709758509076/740189208232198184/20200804_081400.gif",
            "https://gfycat.com/contentorderlygibbon",
            "https://gfycat.com/elasticblankaustralianshelduck",
            "https://gfycat.com/exemplarybiodegradablelemur",
            "https://cdn.discordapp.com/attachments/547946709758509076/797576874980147200/Jieun.gif",
            "https://tenor.com/view/purple-kiss-park-jieun-gif-19609803",
            "https://gfycat.com/aridfoolishbarnswallow",
            "https://cdn.discordapp.com/attachments/547946709758509076/806564005195284541/image0.gif",
            "https://cdn.discordapp.com/attachments/547946709758509076/806564005799133184/image1.gif",
            "https://cdn.discordapp.com/attachments/547946709758509076/806567003711602708/image0.gif",
            "https://cdn.discordapp.com/attachments/547946709758509076/806682264355733504/image0.gif"]

        self.bot.dosie_gif = ["https://gfycat.com/ShorttermAgonizingIriomotecat",
            "https://gfycat.com/ReflectingPessimisticGalapagosalbatross",
            "https://gfycat.com/QuestionableImpracticalClingfish",
            "https://gfycat.com/ImpartialHonoredBangeltiger",
            "https://gfycat.com/ImprobableWatchfulKillifish",
            "https://cdn.discordapp.com/attachments/547946748811935755/740189265610408026/20200804_082421.gif",
            "https://tenor.com/view/eunnie-line-eunseo-dosie-goeun-eunseong-gif-19614430",
            "https://cdn.discordapp.com/attachments/547946748811935755/806563373672169492/image0.gif",
            "https://cdn.discordapp.com/attachments/547946748811935755/806563374472626177/image1.gif",
            "https://cdn.discordapp.com/attachments/547946748811935755/806563422388486144/image0.gif",
            "https://cdn.discordapp.com/attachments/547946748811935755/806572101648646174/image0.gif",
            "https://cdn.discordapp.com/attachments/547946748811935755/806682321117380658/image0.gif"]
        
        self.bot.ireh_gif = ["https://gfycat.com/OpenEnchantedArcherfish",
            "https://gfycat.com/MediumScentedGeese",
            "https://gfycat.com/RelievedThirdBoaconstrictor",
            "https://gfycat.com/ShinyWhimsicalBlackbird",
            "https://gfycat.com/TheseAbsoluteFossa",
            "https://cdn.discordapp.com/attachments/680370499297345549/740189290876633168/20200804_080935.gif",
            "https://tenor.com/view/purple-kiss-gif-19356837",
            "https://tenor.com/view/ireh-purple-kiss-seoyoung-gif-19356698",
            "https://tenor.com/view/ireh-purple-kiss-gif-19356772",
            "https://tenor.com/view/purple-kiss-ireh-chaein-dosie-gif-19356828",
            "https://tenor.com/view/ireh-purple-kiss-gif-19356800",
            "https://cdn.discordapp.com/attachments/680370499297345549/797591178387783740/Ireh.gif",
            "https://tenor.com/view/done-ireh-purple-kiss-rbw-gif-19603737",
            "https://cdn.discordapp.com/attachments/680370499297345549/806562940525346816/image0.gif",
            "https://cdn.discordapp.com/attachments/680370499297345549/806562941431447602/image1.gif",
            "https://cdn.discordapp.com/attachments/680370499297345549/806682353052811264/image0.gif"]

        self.bot.chaein_gif = ["https://gfycat.com/filthyforkedfirecrest",
            "https://gfycat.com/miserablejealousbengaltiger",
            "https://gfycat.com/wateryecstaticamazonparrot",
            "https://gfycat.com/easymistyflea",
            "https://gfycat.com/shrillglisteninggalapagospenguin",
            "https://gfycat.com/slightampledaddylonglegs",
            "https://gfycat.com/negligibleglumeagle",
            "https://cdn.discordapp.com/attachments/663392215929716737/740189333776236564/20200804_080507.gif",
            "https://gfycat.com/deadverifiableabyssiniancat",
            "https://gfycat.com/excitablekaleidoscopicgadwall",
            "https://gfycat.com/cloudyraggedarchaeocete",
            "https://gfycat.com/accomplishedtastyarmednylonshrimp",
            "https://gfycat.com/lamegrouchyharborseal",
            "https://tenor.com/view/chaein-purple-kiss-chaeyoung-gif-19298314",
            "https://tenor.com/view/chaein-purple-kiss-my-heart-skip-a-beat-gif-19356315",
            "https://tenor.com/view/chaein-purple-kiss-gif-19356429",
            "https://tenor.com/view/chaein-purple-kiss-lee-chaeyoung-gif-19356652",
            "https://tenor.com/view/purple-kiss-gif-19356669",
            "https://tenor.com/view/go-eun-chaein-purple-kiss-gif-19356750",
            "https://tenor.com/view/chaein-purple-kiss-gif-19356764",
            "https://gfycat.com/indolentrecentaphid",
            "https://cdn.discordapp.com/attachments/663392215929716737/806562479089647696/image0.gif",
            "https://cdn.discordapp.com/attachments/663392215929716737/806562494847123496/image0.gif",
            "https://cdn.discordapp.com/attachments/663392215929716737/806572368968810536/image0.gif",
            "https://cdn.discordapp.com/attachments/663392215929716737/806682412150947870/image0.gif"]

        self.bot.swan_gif = ["https://gfycat.com/favoritewhoppingblueshark",
            "https://gfycat.com/babyishbelatedanaconda",
            "https://gfycat.com/adoredscrawnyleveret",
            "https://gfycat.com/forsakendishonestgrayreefshark",
            "https://gfycat.com/failingimpressionableirishdraughthorse",
            "https://cdn.discordapp.com/attachments/547946771968557076/740189347369844766/20200804_081816.gif",
            "https://cdn.discordapp.com/attachments/547900536565924104/791258374724386836/SwanPurple.gif",
            "https://cdn.discordapp.com/attachments/547946771968557076/806562262226960404/image0.gif",
            "https://cdn.discordapp.com/attachments/547946771968557076/806562330199851038/image0.gif",
            "https://cdn.discordapp.com/attachments/547946771968557076/806562308004380743/image0.gif",
            "https://cdn.discordapp.com/attachments/547946771968557076/806562366539563088/image0.gif",
            "https://cdn.discordapp.com/attachments/547946771968557076/806566967233871872/image0.gif",
            "https://cdn.discordapp.com/attachments/547946771968557076/806682442730700850/image0.gif"]

        self.bot.purplekiss_gif = ["https://cdn.discordapp.com/attachments/547946619845345280/806564359551582208/image0.gif",
            "https://cdn.discordapp.com/attachments/547946619845345280/806571926235250728/image0.gif",
            "https://cdn.discordapp.com/attachments/547946619845345280/806572758691217448/image0.gif"]

        self.bot.pk_teasers = ["https://www.youtube.com/watch?v=k15XyaoIP0E"] #.yuki

    @commands.command()
    async def purple(self, ctx, kiss, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Purple Kiss {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if kiss == "kiss" or kiss == "k!ss":
            if arg == "yuki":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Yuki :heart:')
                        await ctx.send(random.choice(self.bot.yuki_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Yuki :heart:')
                    await ctx.send(random.choice(self.bot.yuki_gif))
                    await ctx.message.delete()
            elif arg == "na goeun" or arg == "goeun" or arg == "nagoeun":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Na Goeun :heart:')
                        await ctx.send(random.choice(self.bot.nagoeun_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Na Goeun :heart:')
                    await ctx.send(random.choice(self.bot.nagoeun_gif))
                    await ctx.message.delete()
            elif arg == "jieun" or arg == "park jieun":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Park Jieun :heart:')
                        await ctx.send(random.choice(self.bot.jieun_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Jieun :heart:')
                    await ctx.send(random.choice(self.bot.jieun_gif))
                    await ctx.message.delete()
            elif arg == "dosie":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Dosie :heart:')
                        await ctx.send(random.choice(self.bot.dosie_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Dosie :heart:')
                    await ctx.send(random.choice(self.bot.dosie_gif))
                    await ctx.message.delete()
            elif arg == "ireh":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Ireh :heart:')
                        await ctx.send(random.choice(self.bot.ireh_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Ireh :heart:')
                    await ctx.send(random.choice(self.bot.ireh_gif))
                    await ctx.message.delete()
            elif arg == "chaein":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Chaein :heart:')
                        await ctx.send(random.choice(self.bot.chaein_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Chaein :heart:')
                    await ctx.send(random.choice(self.bot.chaein_gif))
                    await ctx.message.delete()
            elif arg == "swan":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Swan :heart:')
                        await ctx.send(random.choice(self.bot.swan_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Swan :heart:')
                    await ctx.send(random.choice(self.bot.swan_gif))
                    await ctx.message.delete()
            elif arg == "teaser":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is watching a Purple K!ss member trailer :purple_heart:') 
                    await ctx.send(random.choice(self.bot.pk_teasers))
                    await ctx.message.delete()


    @commands.command()
    async def yuki(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Yuki :heart:')
                await ctx.send(random.choice(self.bot.yuki_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yuki :heart:')
            await ctx.send(random.choice(self.bot.yuki_gif))
            await ctx.message.delete()

    @commands.command(aliases = ['nagoeun', 'na'])
    async def goeun(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Na Goeun :heart:')
                await ctx.send(random.choice(self.bot.nagoeun_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Na Goeun :heart:')
            await ctx.send(random.choice(self.bot.nagoeun_gif))
            await ctx.message.delete()

    @commands.command()
    async def jieun(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Park Jieun :heart:')
                await ctx.send(random.choice(self.bot.jieun_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jieun :heart:')
            await ctx.send(random.choice(self.bot.jieun_gif))
            await ctx.message.delete()

    @commands.command()
    async def dosie(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Dosie :heart:')
                await ctx.send(random.choice(self.bot.dosie_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Dosie :heart:')
            await ctx.send(random.choice(self.bot.dosie_gif))
            await ctx.message.delete()

    @commands.command()
    async def ireh(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Ireh :heart:')
                await ctx.send(random.choice(self.bot.ireh_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Ireh :heart:')
            await ctx.send(random.choice(self.bot.ireh_gif))
            await ctx.message.delete()

    @commands.command()
    async def chaein(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Chaein :heart:')
                await ctx.send(random.choice(self.bot.chaein_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Chaein :heart:')
            await ctx.send(random.choice(self.bot.chaein_gif))
            await ctx.message.delete()

    @commands.command()
    async def swan(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Swan :heart:')
                await ctx.send(random.choice(self.bot.swan_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Swan :heart:')
            await ctx.send(random.choice(self.bot.swan_gif))
            await ctx.message.delete()

def setup(client):
    client.add_cog(PurpleKiss(client))