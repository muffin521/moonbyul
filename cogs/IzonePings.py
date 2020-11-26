import discord, random
from discord.ext import commands

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

class IzonePings(commands.Cog):

#saku and yul commands are special for now bc i cant be asked to fix em rn

    def __init__(self, client):
        self.client = client

        self.sakura_gif = ["https://tenor.com/view/sakura-miyawaki-sakura-izone-%E3%81%95%E3%81%8F%E3%82%89-%E5%AE%AE%E8%84%87%E5%92%B2%E8%89%AF-gif-14974458",
            "https://gfycat.com/kindlyimmenseilladopsis",
            "https://tenor.com/view/miyawaki-sakura-izone-hkt48-cute-pretty-gif-17693002",
            "https://gfycat.com/bossycoldkite",
            "https://gfycat.com/gravespicybangeltiger",
            "https://gfycat.com/gleefulcostlybasil",
            "https://gfycat.com/rapidenragedborzoi",
            "https://tenor.com/view/izone-miyawaki-sakura-sakura-miyawaki-cute-dance-gif-18107682",
            "https://tenor.com/view/miyawaki-sakura-sakura-miyawaki-izone-sakura-izone-gif-17930135",
            "https://tenor.com/view/miyawaki-sakura-bounce-gif-18613999",
            "https://gfycat.com/bitterimpartialarmyant",
            "https://tenor.com/view/miyawakisakura-miyawaki-sakura-produce48-gif-11809360",
            "https://tenor.com/view/iz-one-iz-one-sakura-sakura-sakura-miyawaki-pretty-gif-16341190",
            "https://tenor.com/view/sakura-izone-wrestling-me-liking-josh-gif-17235397",
            "https://tenor.com/view/sakura-izone-sakura-miyawaki-sakura-saku-chan-chaekura-kkura-gif-13532539",
            "https://gfycat.com/similarscentedgrassspider",
            "https://tenor.com/view/miyawaki-sakura-gif-13854495",
            "https://gfycat.com/illegalfaithfulgrouse",
            "https://gfycat.com/achingflickeringbarbet",
            "https://tenor.com/view/sakura-welcome-iz-one-miyawaki-sakura-visual-vocalist-gif-17340067",
            "https://tenor.com/view/izone-sakura-miyawaki-miyawaki-sakura-sakura-izone-wink-gif-18000682",
            "https://tenor.com/view/sakura-izone-miyawaki-sakura-sakura-miyawaki-izone-gif-18260716",
            "https://tenor.com/view/sakura-miyawaki-sakura-izone-jo-yuri-yuri-gif-18738707",
            "https://tenor.com/view/crossed-eyes-sakura-miyawaki-akb48-izone-cute-gif-17460704",
            "https://tenor.com/view/iz-one-iz-one-sakura-sakura-sakura-miyawaki-pretty-gif-15555270",
            "https://tenor.com/view/izone-sakura-miyawaki-miyawaki-sakura-sakura-izone-wink-gif-18000682",
            "https://tenor.com/view/sakura-izone-miyawaki-sakura-sakura-miyawaki-izone-gif-18260716",
            "https://tenor.com/view/izone-sakura-miyawaki-miyawaki-sakura-sakura-izone-gif-18260944",
            "https://tenor.com/view/miyawaki-sakura-sakura-izone-sakura-miyawaki-laugh-gif-17930243",
            "https://gfycat.com/babyishacademicchicken",
            "https://tenor.com/view/izone-hkt-hkt48-sakura-miyawakisakura-gif-18979961",
            "https://tenor.com/view/iz-one-miyawaki-sakura-wink-flirty-gif-16449291",
            "https://gfycat.com/vaguefreshflickertailsquirrel",
            "https://gfycat.com/clumsywhirlwindhackee",
            "https://gfycat.com/regularthatfowl",
            "https://tenor.com/view/miyawaki-sakura-sakura-hkt48-akb48-woah-gif-12224930",
            "https://tenor.com/view/izone-miyawaki-sakura-miyawaki-sakura-kkura-gif-15064174",
            "https://tenor.com/view/izone-sakura-miyawaki-miyawaki-sakura-sakura-izone-gif-18260944"
            "https://tenor.com/view/sakura-miyawaki-wink-izone-produce48-gif-13510279",
            "https://tenor.com/view/sakura-miyawaki-izone-nekkoya-produce48-smile-gif-13510047",
            "https://tenor.com/view/sakura-miyawaki-miyawaki-sakura-izone-hkt48-gif-15041597",
            "https://tenor.com/view/sakura-miyawaki-izone-funny-gif-13510276",
            "https://tenor.com/view/sakura-fiesta-sakura-miyawaki-sakura-sakura-angry-hkt48sakura-gif-16419142"]

        self.yuri_gif = ["https://tenor.com/view/iz-one-jo-yuri-cute-tilt-kpop-gif-16502904",
            "https://tenor.com/view/joyuri-izone-cute-gif-12833269",
            "https://tenor.com/view/iz-one-jo-yuri-kpop-cute-pretty-gif-16499123",
            "https://tenor.com/view/jo-yuri-teeth-gif-18614001",
            "https://gfycat.com/snappyacrobaticjavalina",
            "https://media.discordapp.net/attachments/444028614925877249/765217464253808690/1602509920.gif",
            "https://media.discordapp.net/attachments/724107459265953835/770832512620036157/image2.gif",
            "https://media.discordapp.net/attachments/444028614925877249/766869102413217832/43125.gif",
            "https://gfycat.com/scrawnyornateblackrussianterrier",
            "https://gfycat.com/embellishedeverlastingborderterrier",
            "https://gfycat.com/handsomeexemplarygroundhog",
            "https://gfycat.com/gloriousraggedangora",
            "https://gfycat.com/disguisedshadowyicelandgull",
            "https://blog.kakaocdn.net/dn/nCshC/btqKlVhsTes/CSkCPJCDQH1LSUr8iqGZqk/img.gif",
            "https://gfycat.com/defiantmediocreisabellineshrike",
            "https://imgur.com/tKqF4PH",
            "https://tenor.com/view/iz-one-hyewon-yuri-kiss-gif-15407712",
            "https://tenor.com/view/iz-one-hyewon-yuri-kiss-gif-15407713",
            "https://tenor.com/view/izone-hyewon-yuri-eat-gif-16105614",
            "https://tenor.com/view/yuri-hye-won-gif-14054908",
            "https://tenor.com/view/iz-one-kang-hyewon-jo-yuri-kpop-korean-gif-16755891",
            "https://cdn.discordapp.com/attachments/647946252645826560/772328738062336020/zzzzzzzzzz.gif",
            "https://media.discordapp.net/attachments/724107459265953835/770832512620036157/image2.gif",
            "https://tenor.com/view/sakura-miyawaki-sakura-izone-jo-yuri-yuri-gif-18738707",
            "https://tenor.com/view/izone-yuri-kpop-cute-happy-gif-16325829",
            "https://cdn.discordapp.com/attachments/704248706269970488/776652835617898516/image0.gif"]

        #15
        self.chaeyeon_gif = ["https://tenor.com/view/lee-chaeyeon-chaeyeon-chaeyeon-izone-smile-cute-gif-15840463",
            "https://tenor.com/view/lee-chaeyeon-izone-gif-14157286",
            "https://tenor.com/view/iz-one-chaeyeon-smile-gif-15401792",
            "https://tenor.com/view/iz-one-chae-yeon-lee-chae-yeon-heart-rakarukri-gif-13456473",
            "https://gfycat.com/widebronzebuckeyebutterfly",
            "https://tenor.com/view/chaeyeon-lee-chaeyeon-izone-chaeyeon-izone-oh-yes-gif-14230918",
            "https://tenor.com/view/lee-chaeyeon-chaeyeon-izone-chaeyeon-gif-14723167",
            "https://tenor.com/view/lee-chaeyeon-chaeyeon-izone-chaeyeon-gif-14723103",
            "https://tenor.com/view/chaeyeon-lee-chaeyeon-izone-chaeyeon-gif-14231352",
            "https://media.discordapp.net/attachments/753744547174940804/762849008112369674/img-4.gif",
            "https://media.discordapp.net/attachments/753744547174940804/762849980078882846/ezgif-3-e15b68e1966c.gif",
            "https://media.discordapp.net/attachments/753744547174940804/762850577125998632/ezgif-4-71e107295746.gif",
            "https://media.discordapp.net/attachments/753744547174940804/762850996807794709/ezgif-3-6a400f15a85b.gif",
            "https://tenor.com/view/chaeyeon-16-shots-lee-hot-gif-18610218",
            "https://media.discordapp.net/attachments/498138615415701524/780998564901552128/hyewonbonk.gif"]

        #19
        self.minju_gif = ["https://gfycat.com/lawfulickykodiakbear",
            "https://gfycat.com/ancientcomplicatedbluefintuna",
            "https://gfycat.com/chubbyemptygalapagosmockingbird",
            "https://gfycat.com/delayedbitterarizonaalligatorlizard",
            "https://gfycat.com/enormoushairydeviltasmanian",
            "https://gfycat.com/colorfulgargantuanalligator",
            "https://tenor.com/view/minju-gif-18246598",
            "https://gfycat.com/NimbleElectricCanine/",
            "https://gfycat.com/FinishedJitteryBushsqueaker/",
            "https://gfycat.com/anchoredficklefirebelliedtoad",
            "https://gfycat.com/blissfulvacantannashummingbird/",
            "https://gfycat.com/SardonicObedientGuernseycow/",
            "https://gfycat.com/genuinegiddycopepod",
            "https://gfycat.com/raggedviciouskudu/",
            "https://tenor.com/view/minju-kim-minju-izone-gif-18645290",
            "https://tenor.com/view/rykkura-minguri-pretty-beautiful-cute-gif-16891660",
            "https://tenor.com/view/izone-izone-hyewon-kang-hyewon-kcon-hyewon-kwangbae-gif-18839326",
            "https://gfycat.com/impressionabledenseaffenpinscher",
            "https://gfycat.com/kindrequiredbooby/"]

        #17
        self.wonyoung_gif = ["https://gfycat.com/illfatedjollyamericanwigeon",
            "https://gfycat.com/finishedspecificagouti",
            "https://gfycat.com/saneplushbrownbutterfly",
            "https://gfycat.com/glisteningdeafeningcockatoo",
            "https://gfycat.com/tidyuniquedogwoodtwigborer",
            "https://gfycat.com/formalbitterbeagle",
            "https://gfycat.com/highsafebuckeyebutterfly",
            "https://gfycat.com/incredibleoilybantamrooster",
            "https://media.discordapp.net/attachments/753744810103275701/762303178779656202/ezgif-2-ae66e3afb989.gif",
            "https://media.discordapp.net/attachments/753744810103275701/762303571730628639/img_3.gif",
            "https://media.discordapp.net/attachments/753744810103275701/756618956810485910/ezgif-3-9a9fc5ccdfec.gif",
            "https://gfycat.com/quarrelsomeregulargiraffe",
            "https://gfycat.com/deliciousdecimalkestrel",
            "https://gfycat.com/unpleasantobesearthropods",
            "https://gfycat.com/naiveagonizingjavalina",
            "https://gfycat.com/annualalertasiandamselfly",
            "https://tenor.com/view/wonyoung-jang-wonyoung-iz-one-dance-gif-14625438"]

        #15
        self.hyewon_gif = ["https://tenor.com/view/izone-izone-hyewon-kang-hyewon-kcon-hyewon-kwangbae-gif-18839326",
            "https://tenor.com/view/hyewon-kang-hyewon-izone-izone-hyewon-beware-gif-18734334",
            "https://tenor.com/view/hyewon-kang-hyewon-iz-one-kwangbae-pretty-gif-17795566",
            "https://tenor.com/view/izone-hyewon-kang-hyewon-rapper-vocalist-gif-17788590",
            "https://tenor.com/view/izone-hyewon-kang-hyewon-rapper-vocalist-gif-17573956",
            "https://tenor.com/view/iz-one-iz-one-hyewon-hyewon-kang-hyewon-pretty-gif-16546594",
            "https://tenor.com/view/izone-hyewon-kang-hyewon-rapper-vocalist-gif-17795160",
            "https://tenor.com/view/sakura-izone-hyewon-gif-13814364",
            "https://tenor.com/view/izone-hyewon-cute-kpop-stare-gif-16129476",
            "https://tenor.com/view/iz-one-kwangbae-kangchan-kang-hyewon-hyewon-gif-14220838",
            "https://tenor.com/view/izone-izone-hyewon-kang-hyewon-izone-kwangbae-kwangbae-gif-19005616",
            "https://tenor.com/view/hyewon-kang-hyewon-izone-kwangbae-cute-gif-17795308",
            "https://tenor.com/view/hyewon-kang-hyewon-iz-one-kwangbae-pretty-gif-17795405",
            "https://tenor.com/view/hyewon-kang-hyewon-izone-wink-gif-14084171",
            "https://tenor.com/view/hyewon-smile-pretty-gif-13780756"]

    
    #sakura command for weakado
    @commands.command(aliases = ['saku', 'kkura'])
    async def sakura(self, ctx):
        if (ctx.channel.id == kbotcom and ctx.guild.id == luminary) or ctx.guild.id == jst or ctx.guild.id == sadboi:
            await ctx.send(f'<@259409277482041344>, <@!{ctx.author.id}> is talking about Sakura :purple_heart:')
            await ctx.send(random.choice(self.sakura_gif))
            await ctx.message.delete()
        elif ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Sakura :purple_heart:')
            await ctx.send(random.choice(self.sakura_gif))
            await ctx.message.delete()

    #yuri command for jat
    @commands.command()
    async def yuri(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@236787566530134017>, <@!{ctx.author.id}> is talking about Yuri :heart:')
                await ctx.send(random.choice(self.yuri_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yuri :heart:')
            await ctx.send(random.choice(self.yuri_gif))
            await ctx.message.delete()

    #chaeyeon command for luke
    @commands.command()
    async def chaeyeon(self, ctx):
        if ctx.guild.id == jst:
            await ctx.send(f'<@150742733743587328>, <@!{ctx.author.id}> is talking about Chaeyeon :white_heart:')
            await ctx.send(random.choice(self.chaeyeon_gif))
            await ctx.message.delete()
        elif ctx.channel.id != 764610881513324574 and ctx.guild.id == 758468592957521972:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Chaeyeon :white_heart:')
            await ctx.send(random.choice(self.chaeyeon_gif))
            await ctx.message.delete()

    #minju command for mae and cronus
    @commands.command()
    async def minju(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@492769416610840586>, <@186533260803833858>, <@!{ctx.author.id}> is talking about Minju :frog:')
                await ctx.send(random.choice(self.minju_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Minju :frog:')
            await ctx.send(random.choice(self.minju_gif))
            await ctx.message.delete()

    #wonyoung command for mae
    @commands.command()
    async def wonyoung(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@492769416610840586>, <@!{ctx.author.id}> is talking about Wonyoung :rabbit:')
                await ctx.send(random.choice(self.wonyoung_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Wonyoung :rabbit:')
            await ctx.send(random.choice(self.wonyoung_gif))
            await ctx.message.delete()

    #wonyoung command for agus
    @commands.command()
    async def hyewon(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@683791381667250208>, <@!{ctx.author.id}> is talking about Hyewon :cake:')
                await ctx.send(random.choice(self.hyewon_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Hyewon :cake:')
            await ctx.send(random.choice(self.hyewon_gif))
            await ctx.message.delete()



def setup(client):
    client.add_cog(IzonePings(client))