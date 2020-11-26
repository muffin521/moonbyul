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
ari = 633823096541020170
stanley = 727312020717830264
rith = 346724857725059075
masa = 725138411823956079
mae = 492769416610840586
agus = 683791381667250208

class MamamooPings(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.moonbyul_gif = ["https://tenor.com/view/moonbyul-kiss-for-the-fans-happy-smile-gif-7468790",
            "https://tenor.com/view/moonbyul-mamamoo-kpop-laugh-gif-7498808",
            "https://tenor.com/view/korean-girl-fierce-look-cute-gif-17473484",
            "https://tenor.com/view/moonbyul-mamamoo-wanna-be-myself-look-at-me-gif-18404578",
            "https://gfycat.com/detailedjointcorydorascatfish",
            "https://imgur.com/ITQcDC9,"
            "https://gfycat.com/smallenviousbovine",
            "https://media.discordapp.net/attachments/758493180030222397/772229955408101376/messy_byul.gif",
            "https://tenor.com/view/mamamoo-moonbyul-moon-byul-yi-rapper-vocalist-gif-15907147",
            "https://tenor.com/view/mamamoo-moonbyul-gleam-hot-glasses-gif-14619424",
            "https://gfycat.com/ethicalimpuredore",
            "https://gfycat.com/smallenviousbovine",
            "https://gfycat.com/marvelousbiggermanshepherd",
            "https://media.discordapp.net/attachments/167744664315625474/749825327957803068/image0.gif",
            "https://media.discordapp.net/attachments/167744664315625474/749825322588962856/image0.gif",
            "https://media.discordapp.net/attachments/167744664315625474/749825307342536744/image0.gif",
            "https://media.discordapp.net/attachments/167744664315625474/751497807789293618/image0.gif",
            "https://media.discordapp.net/attachments/167744664315625474/751492639492407376/image0.gif",
            "https://media.discordapp.net/attachments/167744664315625474/772528671637897216/image0.gif",
            "https://media.discordapp.net/attachments/167744664315625474/773125206017310750/image0.gif",
            "https://media.discordapp.net/attachments/167744664315625474/773129547335991306/image0.gif",
            "https://media.discordapp.net/attachments/167744664315625474/773180414344429578/201103_AYA_M_2.gif",
            "https://media.discordapp.net/attachments/167744664315625474/773211622604537927/img.gif",
            "https://gfycat.com/giddyharmfulafricangroundhornbill",
            "https://gfycat.com/alarmedcreamyalligatorgar",
            "https://gfycat.com/blackgrandiosebream",
            "https://media.discordapp.net/attachments/167744664315625474/775116649656483860/image0.gif",
            "https://media.discordapp.net/attachments/167744664315625474/775116427949768704/image0.gif",
            "https://media.discordapp.net/attachments/167744664315625474/774564485608374272/img1.daumcdn-1.gif",
            "https://gfycat.com/velvetyshowyfritillarybutterfly",
            "https://64.media.tumblr.com/315bd4a1a9c57792b107a5a4d8fe5b3a/152e17b7ae0f40a5-f6/s400x600/35818e427e4d07882d6dbf9f5e887f043811e8bc.gif",
            "https://tenor.com/view/moonbyul-mamamoo-moonbyul-lip-bite-gif-18784084",
            "https://tenor.com/view/moonbyul-mamamoo-hip-dancing-gif-15607334",
            "https://tenor.com/view/mamamoo-moonbyul-gleam-hot-blonde-gif-14619453",
            "https://tenor.com/view/mamamoo-moonbyul-tongue-lalala-dirty-mind-gif-7618771",
            "https://tenor.com/view/moonbyul-moon-byulyi-sassy-gif-14686097",
            "https://tenor.com/view/mamamoo-moonbyul-gif-18784089",
            "https://tenor.com/view/moonbyul-mamamoo-shot-gun-aya-gif-19031623",
            "https://tenor.com/view/mamamoo-moonbyul-funny-serious-charmander-gif-7724697",
            "https://media.discordapp.net/attachments/762143545053806592/776173375050874941/moonbyul_gaze.gif"]

        self.wheein_gif = ["https://media.discordapp.net/attachments/167744692820246528/767418260395130890/99B40A445F8C65582A.gif",
            "https://media.discordapp.net/attachments/167744692820246528/768433005726531594/download_1.gif",
            "https://gfycat.com/grotesqueicyelephantbeetle",
            "https://gfycat.com/webbedevergreenaustraliankelpie",
            "https://gfycat.com/victoriousamazingdunnart",
            "https://imgur.com/cjBytNP",
            "https://media.discordapp.net/attachments/167744692820246528/773125249562574888/image0.gif",
            "https://gfycat.com/elasticimpressivelice",
            "https://tenor.com/view/mamamoo-wheein-heart-kpop-dance-gif-16331749",
            "https://data.whicdn.com/images/323781631/original.gif",
            "https://static.apester.com/user-images/cb/cb60802a9e5ff8aa501df36ddfa56cce.gif",
            "https://data.whicdn.com/images/323064141/original.gif",
            "https://pa1.narvii.com/7083/ecf8e6d546d434772c62f1485b8de8ce10e8b1fbr1-640-359_hq.gif",
            "https://i.pinimg.com/originals/f7/13/1e/f7131e54e31f00206b78f3f6bd10b9c7.gif",
            "https://gfycat.com/softlinearindianrhinoceros",
            "https://gfycat.com/cornyoccasionalgoldeneye"]

        self.solar_gif = ["https://tenor.com/view/solar-mamamoo-shirt-rip-gif-15962906",
            "https://tenor.com/view/mamamoo-solar-kim-yong-sun-leader-vocalist-gif-17148597",
            "https://thumbs.gfycat.com/BlushingForsakenHog-size_restricted.gif",
            "https://i.pinimg.com/originals/63/48/e7/6348e736198b7fa88976143cbbcc1306.gif",
            "https://gfycat.com/idledesertedgarpike",
            "https://64.media.tumblr.com/cef48702b84c88559fd0bc81585ced80/55be70cf0784d2b1-e8/s400x600/9c83f4358008622c0043b7f458985b3534a34c6c.gif",
            "https://gfycat.com/ickysentimentalapisdorsatalaboriosa-gamsungcamping-jumping-solar",
            "https://64.media.tumblr.com/b147638b503dd8d508aee744fa649e23/55be70cf0784d2b1-f0/s400x600/34c75ab760909bbca6b84c28d29c490535402db5.gif",
            "https://gfycat.com/oddballdimwittedconure-gamsungcamping-solar-dance-aya",
            "https://gfycat.com/emotionalbewitchedinvisiblerail-gamsungcamping-solar-dance-aya",
            "https://gfycat.com/samedimpledfairybluebird-gamsungcamping-excited-solar",
            "https://gfycat.com/snivelingappropriatebaiji-gamsungcamping-wakingup-solar",
            "https://gfycat.com/freshtepidanemoneshrimp",
            "https://gfycat.com/bouncycarelesskodiakbear",
            "https://media.discordapp.net/attachments/167744620724355072/773132112336519168/image0.gif",
            "https://media.discordapp.net/attachments/167744620724355072/773132319971213353/image0.gif",
            "https://tenor.com/view/mamamoo-solar-deal-with-it-check-smile-gif-5516677",
            "https://tenor.com/view/mamamoo-aya-solar-gif-19089175"]

        self.hwasa_gif = ["https://gfycat.com/sourvengefulgrouse",
            "https://gfycat.com/deliciousforkedcaribou",
            "https://media.discordapp.net/attachments/167744709178032128/753624139041865858/200910-1.gif",
            "https://media.discordapp.net/attachments/167744709178032128/753624178334105631/download_2.gif",
            "https://media.discordapp.net/attachments/167744709178032128/753624203151933470/img.gif",
            "https://gfycat.com/secretgoldenbrahmancow",
            "https://gfycat.com/friendlydemandingbunting",
            "https://gfycat.com/sorrowfulunpleasantgander",
            "https://media.discordapp.net/attachments/167744709178032128/767438895083814922/999CC9445F8C755605.gif",
            "https://media.discordapp.net/attachments/167744709178032128/767438897328160769/9937BA4D5F8C60A101.gif",
            "https://thumbs.gfycat.com/MeaslyUnacceptableBlackfish-mobile.mp4",
            "https://media.discordapp.net/attachments/167744709178032128/768047289360318464/HwasaPigtails.gif",
            "https://media.discordapp.net/attachments/167744709178032128/768088661052358656/2010202.gif",
            "https://media.discordapp.net/attachments/167744709178032128/768430278451789824/download.gif",
            "https://thumbs.gfycat.com/ClearcutRecklessAmericanriverotter-mobile.mp4",
            "https://thumbs.gfycat.com/HairyAnnualFinnishspitz-mobile.mp4",
            "https://thumbs.gfycat.com/GrimGregariousHake-mobile.mp4",
            "https://imgur.com/rJKOqUq",
            "https://media.discordapp.net/attachments/167744709178032128/771608627810271242/download_3.gif",
            "https://gfycat.com/keenbitesizedcygnet",
            "https://64.media.tumblr.com/d7f70c81e0877cb8fd032c403f84917e/160d394ff4b0e412-d4/s400x600/b92faebca2aa4278a8522a1d007b275afd39f4f6.gif",
            "https://media.discordapp.net/attachments/167744709178032128/773211638064742430/img_1.gif",
            "https://media.discordapp.net/attachments/167744709178032128/773125270394896415/image0.gif",
            "https://media.discordapp.net/attachments/167744709178032128/773180286397579284/201103_AYA_H_2.gif",
            "https://media.discordapp.net/attachments/167744709178032128/772528706110881842/image0.gif",
            "https://gfycat.com/zestycornyballpython",
            "https://gfycat.com/metallicthunderouskagu",
            "https://gfycat.com/jampackedboweddutchshepherddog",
            "https://tenor.com/view/mamamoo-kpop-gif-7220709"]

        self.mamamoo_gif = ["https://tenor.com/view/mamamoo-mamamoo-waggy-solar-moonbyul-hwasa-gif-18116888",
            "https://tenor.com/view/mememoo-dc-mamamoo-dream-concert-mamamoo-mememoo-kpop-gif-17921327",
            "https://tenor.com/view/gogobebe-mamamoo-dance-clap-kpop-gif-13821772",
            "https://tenor.com/view/gogobebe-mamamoo-dance-kpop-gif-13821774",
            "https://tenor.com/view/mamamoo-mamamoo-andar-hwasa-moonbyul-solar-gif-18784083",
            "https://tenor.com/view/mamamoo-enter-group-entrance-mad-gif-17822927",
            "https://tenor.com/view/mamamoo-hwasa-gif-18909833",
            "https://tenor.com/view/mamamoo-gogobebe-newspaper-relax-read-gif-13827608",
            "https://tenor.com/view/white-wind-fan-sign-mamamoo-power-gif-13790850",
            "https://tenor.com/view/mamamoo-dance-rehearsal-silly-studio-gif-5048210",
            "https://tenor.com/view/mamamoo-dance-hip-bridge-kpop-gif-17777457",
            "https://tenor.com/view/mamamoo-finger-guns-kpop-dance-gif-12784101",
            "https://tenor.com/view/mamamoo-gleam-hot-stuff-glasses-gif-14619637",
            "https://tenor.com/view/mamamoo-mamamoo-teletubbies-mamamoo-teletubbies-bow-gif-18784086"]

    #moonbyul command for meeee
    @commands.command()
    async def moonbyul(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Moonbyul :heart:')
                await ctx.send(random.choice(self.moonbyul_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Moonbyul :heart:')
            await ctx.send(random.choice(self.moonbyul_gif))
            await ctx.message.delete()

    #wheein command for me and stanley and rith and masa and agus
    @commands.command()
    async def wheein(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@{stanley}>, <@{rith}>, <@{masa}>, <@{agus}> <@!{ctx.author.id}> is talking about Wheein :white_heart:')
                await ctx.send(random.choice(self.wheein_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Wheein :white_heart:')
            await ctx.send(random.choice(self.wheein_gif))
            await ctx.message.delete()
    
    #solar command for me and mae
    @commands.command()
    async def solar(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@{mae}>, <@!{ctx.author.id}> is talking about Solar :blue_heart:')
                await ctx.send(random.choice(self.solar_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Solar :blue_heart:')
            await ctx.send(random.choice(self.solar_gif))
            await ctx.message.delete()

    #hwasa command for me
    @commands.command()
    async def hwasa(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Hwasa :yellow_heart:')
                await ctx.send(random.choice(self.hwasa_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Hwasa :yellow_heart:')
            await ctx.send(random.choice(self.hwasa_gif))
            await ctx.message.delete()

    #mamamoo command
    @commands.command()
    async def mamamoo(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Mamamoo :green_heart:')
                await ctx.send(random.choice(self.mamamoo_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Mamamoo :green_heart:')
            await ctx.send(random.choice(self.mamamoo_gif))
            await ctx.message.delete()



def setup(client):
    client.add_cog(MamamooPings(client))