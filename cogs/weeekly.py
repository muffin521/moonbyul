import discord, random
from discord.ext import commands
from datetime import datetime

#//servers
luminary = 758468592957521972

class weeekly(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.weeekly_soojin_gif = ["https://tenor.com/view/soojin-soojinweeekly-weeekly-weeeklysoojin-rookie2020-gif-19217007",
            "https://cdn.discordapp.com/attachments/790062429866426368/790074792190541834/SOOJIN1.gif",
            "https://tenor.com/view/weeeklysoojin-weeekly-soojin-gif-19216994",
            "https://tenor.com/view/boss-puppy-lee-soojin-soojin-weeekly-sv-gif-18790774",
            "https://tenor.com/view/weeekly-soojin-lee-soojin-kpop-cute-gif-17374750",
            "https://tenor.com/view/soojin-weeekly-pat-gif-18049939",
            "https://tenor.com/view/weeeklysoojin-gif-19217520",
            "https://tenor.com/view/weeekly-soojin-weeekly-soojin-no-money-weeekly-no-momey-gif-18802164",
            "https://gfycat.com/arcticfeistyindianpalmsquirrel",
            "https://gfycat.com/abandonedunrealisticichthyostega",
            "https://gfycat.com/physicaloilyabyssiniangroundhornbill",
            "https://gfycat.com/bonyadmirablegalapagosdove",
            "https://gfycat.com/largeoldfashionedhydra",
            "https://gfycat.com/tidymildamericanquarterhorse",
            "https://gfycat.com/compassionatehilariouscomet",
            "https://gfycat.com/anchoredcommonirukandjijellyfish",
            "https://gfycat.com/tiredvibrantgopher",
            "https://gfycat.com/memorablearcticafricanjacana",
            "https://gfycat.com/meatyspryaustralianshelduck",
            "https://gfycat.com/talkativetedioushoneybadger",
            "https://gfycat.com/loathsomehideousalpineroadguidetigerbeetle",
            "https://gfycat.com/entireradiantfirefly",
            "https://gfycat.com/niftyaltruisticacaciarat",
            "https://gfycat.com/frankimpracticalbittern",
            "https://gfycat.com/delayedoblongarabianoryx",
            "https://gfycat.com/absolutedarlingcleanerwrasse",
            "https://gfycat.com/fantasticmarvelousgroundbeetle",
            "https://gfycat.com/grimyearnestjackal",
            "https://gfycat.com/whirlwindsanecatfish",
            "https://gfycat.com/insignificantflatbichonfrise",
            "https://gfycat.com/deadeverygodwit",
            "https://gfycat.com/welcomethesehackee"]

        self.bot.weeekly_jiyoon_gif = ["https://cdn.discordapp.com/attachments/790062585054625873/790074833609949214/JIYOON4.gif",
            "https://cdn.discordapp.com/attachments/790062585054625873/790074875695071292/JIYOON3.gif",
            "https://cdn.discordapp.com/attachments/790062585054625873/790074900815282207/JIYOON2.gif",
            "https://cdn.discordapp.com/attachments/790062585054625873/790074926430027836/JIYOON1.gif",
            "https://tenor.com/view/jiyoon-weeekly-gif-18604350",
            "https://tenor.com/view/jiyoon-weeekly-cute-pretty-gif-17532953",
            "https://tenor.com/view/weeekly-weeekly-jiyoon-jiyoon-gif-18127931",
            "https://tenor.com/view/pretty-jiyoon-weeekly-smile-weeekly-jiyoon-gif-18128574",
            "https://tenor.com/view/weeekly-jiyoon-jiyoon-weeekly-cute-gif-18128670",
            "https://tenor.com/view/shocked-jiyoon-weeekly-weeekly-jiyoon-weeekly-shocked-gif-18226642",
            "https://tenor.com/view/jiyoon-weeekly-weeekly-jiyoon-shin-jiyoon-gif-19422209",
            "https://gfycat.com/weepyreflectinggalapagostortoise",
            "https://gfycat.com/harshoffensivegelada",
            "https://gfycat.com/personaldearestboto",
            "https://gfycat.com/sadpinkfairyfly",
            "https://gfycat.com/sophisticatedwelldocumentedaxolotl",
            "https://gfycat.com/failinggrotesquebird",
            "https://gfycat.com/bleakadmiredbarebirdbat",
            "https://gfycat.com/crazyfrighteneddachshund",
            "https://gfycat.com/whitesimilarfrillneckedlizard",
            "https://gfycat.com/negligibleimpartialdamselfly",
            "https://gfycat.com/defenselesshandsomeichneumonfly",
            "https://gfycat.com/deficientidleindigowingedparrot",
            "https://gfycat.com/miniaturedangerousgourami",
            "https://gfycat.com/filthyhorriblefanworms",
            "https://gfycat.com/wellmadefoolishdipper",
            "https://gfycat.com/sandyflippantarchaeopteryx",
            "https://gfycat.com/scornfulbigheartedastarte",
            "https://gfycat.com/fearfulrepulsivehermitcrab",
            "https://gfycat.com/slowunawaregordonsetter",
            "https://gfycat.com/delirioussinglefoxterrier",
            "https://gfycat.com/detailedplushcopperhead",
            "https://gfycat.com/flimsysilverclownanemonefish",
            "https://gfycat.com/courageousfocusedafricanparadiseflycatcher",
            "https://gfycat.com/aggravatinghappygoluckyiriomotecat",
            "https://gfycat.com/amusingopenbison",
            "https://gfycat.com/belovedwickedinexpectatumpleco",
            "https://gfycat.com/demandinglankyboubou",
            "https://gfycat.com/acclaimedrequiredbassethound",
            "https://gfycat.com/glumbleakgrosbeak",
            "https://gfycat.com/lastingsinglehuman",
            "https://gfycat.com/handmaderingedhornet",
            "https://gfycat.com/uncomfortablecompetentarcticduck",
            "https://gfycat.com/immediatetartamericanwigeon"]

        self.bot.weeekly_monday_gif = ["https://cdn.discordapp.com/attachments/790062662905102346/790074986702438450/MONDAY1.gif",
            "https://tenor.com/view/weeekly-soojin-monday-jiyoon-soeun-gif-18168556",
            "https://tenor.com/view/monday-weeekly-laugh-kpop-cute-gif-17478647",
            "https://tenor.com/view/weeekly-monday-weeekly-monday-playm-gif-18227541",
            "https://tenor.com/view/monday-weeekly-smirk-gif-18059513",
            "https://gfycat.com/animatedvigilantglowworm",
            "https://gfycat.com/shallowgraveeyelashpitviper",
            "https://gfycat.com/oddshadowyfinnishspitz",
            "https://gfycat.com/actualuglyaurochs",
            "https://gfycat.com/excitablelimpingabyssiniangroundhornbill",
            "https://gfycat.com/infamousinborncowbird",
            "https://gfycat.com/lastingyoungborer",
            "https://gfycat.com/rashfocusedhawaiianmonkseal",
            "https://gfycat.com/hotnicebengaltiger",
            "https://gfycat.com/unpleasanthighbangeltiger",
            "https://gfycat.com/baggypitifulbuckeyebutterfly",
            "https://gfycat.com/nervoussinglearchaeocete",
            "https://gfycat.com/innocentincomparablekillerwhale",
            "https://gfycat.com/fasthopefulcommabutterfly",
            "https://gfycat.com/difficultlonelyhackee",
            "https://gfycat.com/fairmemorablecats",
            "https://gfycat.com/coarseremorsefulcrane",
            "https://gfycat.com/knobbycrazyequestrian",
            "https://gfycat.com/digitaleleganthart",
            "https://gfycat.com/craftygraydragon",
            "https://gfycat.com/remarkablecarefreegrayling",
            "https://64.media.tumblr.com/697568b168bbb34e383b6456ccab1e36/3b992ee99ba8744a-7e/s250x400/4d0f8a1ad490a02f9f471a7cb1463d40f64feb56.gif",
            "https://64.media.tumblr.com/f1a6cb66b98b82d7c8c75a586825ded3/726f527e77a5de0a-9d/s250x400/ecddf386e1e65d3d456fb6b4ea6e2e305176a5f3.gif",
            "https://64.media.tumblr.com/44fd422c9cd9eaf939b602dd2af91043/ea558dbe5decee97-9d/s250x400/d42fbcc58e71afd8c0d4772d91707b2d03fbbff6.gif",
            "https://64.media.tumblr.com/acd91d295e6a022130ad16fb7cbe3eeb/0bba36126509207e-c2/s250x400/0ab251356f085eb53170ce1d4f2e5e606ff6142a.gif",
            "https://gfycat.com/angryrightferret",
            "https://gfycat.com/vibrantcourageousbufeo",
            "https://gfycat.com/scaryinsecurecony",
            "https://gfycat.com/silkyaggressivecornsnake",
            "https://gfycat.com/distortedspotlessbull"]

        self.bot.weeekly_soeun_gif = ["https://tenor.com/view/weeekly-soeun-weeekly-soeun-gif-18130042",
            "https://tenor.com/view/weeekly-weeekly-jiyoon-weeekly-soeun-soeun-jiyoon-gif-18216326",
            "https://tenor.com/view/weeekly-weeekly-soeun-soeun-playm-entertainment-playm-gif-18087242",
            "https://gfycat.com/anguishedoffbeatarcticwolf",
            "https://gfycat.com/apprehensiveshowydiplodocus",
            "https://gfycat.com/aptcostlyflea",
            "https://gfycat.com/assuredrapidgavial",
            "https://gfycat.com/brownoddballkiwi",
            "https://gfycat.com/conventionaldisastrousfoxhound",
            "https://gfycat.com/adorableoilyhyrax",
            "https://gfycat.com/ecstaticactualbird",
            "https://gfycat.com/angryacrobatichairstreak",
            "https://gfycat.com/flatcostlyinvisiblerail",
            "https://gfycat.com/clearfrenchindianabat",
            "https://gfycat.com/generousfaithfularcticduck",
            "https://gfycat.com/chillyfrequentamericankestrel",
            "https://gfycat.com/repentantdearhalibut",
            "https://gfycat.com/silkyidenticalchafer",
            "https://gfycat.com/delayedmassivefinch",
            "https://gfycat.com/illegalanxiousdassie",
            "https://gfycat.com/singleevergreenbandicoot",
            "https://gfycat.com/thickethicaladder",
            "https://gfycat.com/colorfulgaseoushyena",
            "https://gfycat.com/plasticallindianpalmsquirrel",
            "https://gfycat.com/respectfulangrycottonmouth",
            "https://gfycat.com/bigheartedbiodegradableduck",
            "https://gfycat.com/essentialcriminalhoopoe",
            "https://gfycat.com/practicalorangecolt",
            "https://gfycat.com/veneratedpossiblegavial"]

        self.bot.weeekly_jaehee_gif = ["https://cdn.discordapp.com/attachments/790062758556336128/790075085779894273/JAEHEE1.gif",
            "https://tenor.com/view/weeekly-jaehee-weeekly-jaehee-jaehee-sad-weeekly-jaehee-sad-gif-18217735",
            "https://tenor.com/view/jaehee-weeekly-weeekly-jaehee-weeekly-think-jaehee-think-gif-19422471",
            "https://tenor.com/view/jaehee-weeekly-weeekly-jaehee-weeekly-jaehee-cute-jaehee-cute-gif-18217794",
            "https://tenor.com/view/weeekly-jaehee-weeekly-jaehee-jaehee-heart-weeekly-heart-gif-18849380",
            "https://gfycat.com/aromatichighleveljerboa",
            "https://gfycat.com/ampleadeptadmiralbutterfly",
            "https://gfycat.com/appropriateearnestgoldenretriever",
            "https://gfycat.com/bestunconsciousdartfrog",
            "https://gfycat.com/unknownaptcondor",
            "https://gfycat.com/deficienteachkilldeer",
            "https://gfycat.com/rapidrealisticcrustacean",
            "https://gfycat.com/unlineddelightfulkudu",
            "https://gfycat.com/oblonghatefulcuscus",
            "https://gfycat.com/sanebrokenbullfrog",
            "https://gfycat.com/peskyquestionableegret",
            "https://gfycat.com/disloyaloblonggoosefish",
            "https://gfycat.com/distantlastingcobra",
            "https://gfycat.com/hardsafebarracuda",
            "https://gfycat.com/serpentinehairyafricanbushviper",
            "https://gfycat.com/shadyconfusedaegeancat",
            "https://gfycat.com/absolutetiredeuropeanpolecat",
            "https://gfycat.com/distanthugeeider",
            "https://gfycat.com/disloyalgloriouseider",
            "https://gfycat.com/yellowheftyhapuku",
            "https://gfycat.com/necessaryuntimelycanadagoose"]

        self.bot.weeekly_jihan_gif = ["https://cdn.discordapp.com/attachments/790062796150407209/790075153744658442/JIHAN3.gif",
            "https://cdn.discordapp.com/attachments/790062796150407209/790075171691692032/JIHAN2.gif",
            "https://cdn.discordapp.com/attachments/790062796150407209/790075206399950908/JIHAN1.gif",
            "https://tenor.com/view/jihan-weeekly-weeekly-jihan-han-jihyo-kpop-gif-18464277",
            "https://tenor.com/view/weeekly-jihan-weeekly-jihan-cute-gif-18128616",
            "https://tenor.com/view/weeekly-jihan-weeekly-jihan-jihyo-weeekly-jihyo-gif-18860644",
            "https://gfycat.com/anyrealkingbird",
            "https://gfycat.com/enormouslonelyflamingo",
            "https://gfycat.com/bittervigilantamoeba",
            "https://gfycat.com/ajarbelovedindianpalmsquirrel",
            "https://gfycat.com/grippingspeedydinosaur",
            "https://gfycat.com/splendidloathsomegelding",
            "https://gfycat.com/euphoricwhimsicaldungenesscrab",
            "https://gfycat.com/sophisticatedcourteousleafhopper",
            "https://gfycat.com/complicatedaromaticbrownbutterfly",
            "https://gfycat.com/amusedbitesizedhairstreakbutterfly",
            "https://gfycat.com/brokengratefulcowbird",
            "https://gfycat.com/bossydemandingchamois",
            "https://gfycat.com/completeincredibleafricanporcupine",
            "https://gfycat.com/harshscientificalligatorsnappingturtle",
            "https://gfycat.com/unfitconcernedfeline",
            "https://gfycat.com/measlyshowyfish",
            "https://gfycat.com/thirstyspectacularlamb",
            "https://gfycat.com/serpentinehairyafricanbushviper",
            "https://gfycat.com/lightheartedsplendidfairyfly",
            "https://gfycat.com/negligibleteemingfirebelliedtoad",
            "https://gfycat.com/smoggygiftedilsamochadegu",
            "https://gfycat.com/gentleapprehensivekiwi",
            "https://gfycat.com/alivesilverbasenji",
            "https://gfycat.com/groundeduntriedkingbird",
            "https://gfycat.com/incompatiblefavoriteamazonparrot",
            "https://gfycat.com/leansleepyindigowingedparrot",
            "https://gfycat.com/enchantednegativehorse",
            "https://gfycat.com/simplejealoushornedtoad",
            "https://gfycat.com/leadinghiddenindiancow",
            "https://gfycat.com/tiredagreeableastrangiacoral",
            "https://gfycat.com/lankysnarlingbream",
            "https://gfycat.com/deepwarmhearteddiscus",
            "https://gfycat.com/abandonedmassivegangesdolphin",
            "https://gfycat.com/accomplishedfatharrierhawk",
            "https://gfycat.com/kaleidoscopicwhimsicalbassethound",
            "https://gfycat.com/fluffyyellowbarnowl",
            "https://gfycat.com/sparsepoliteinexpectatumpleco",
            "https://gfycat.com/secondhandsecondarydavidstiger",
            "https://gfycat.com/euphoricfabulouscleanerwrasse",
            "https://gfycat.com/wholepoliticalbrownbutterfly",
            "https://gfycat.com/paltryclutteredcusimanse",
            "https://gfycat.com/sphericalinferiorfritillarybutterfly",
            "https://tenor.com/view/weeekly-jihan-gif-20926965",
            "https://tenor.com/view/jihan-weeekly-gif-20911075"]

        self.bot.weeekly_zoa_gif = ["https://cdn.discordapp.com/attachments/790062825796141077/790075277409255512/ZOA1.gif",
            "https://cdn.discordapp.com/attachments/790062825796141077/790075317947203634/ZOA2.gif",
            "https://cdn.discordapp.com/attachments/790062825796141077/790075328466911272/ZOA3.gif",
            "https://cdn.discordapp.com/attachments/790062825796141077/790075355247149066/ZO4.gif",
            "https://tenor.com/view/weeekly-musical-group-soojin-monday-zoa-gif-17658497",
            "https://gfycat.com/enormoussandyboto",
            "https://gfycat.com/imperturbableflusteredarmednylonshrimp",
            "https://gfycat.com/snoopysingleindianpalmsquirrel",
            "https://gfycat.com/flawlessentirebarbet-weeekly-kpop-zoa-wikeulri",
            "https://gfycat.com/importanthelpfulgrayreefshark",
            "https://gfycat.com/temptinguncomfortableechidna",
            "https://gfycat.com/canineplainarrowworm",
            "https://gfycat.com/boringappropriatecollie",
            "https://gfycat.com/dentalimmaterialantlion",
            "https://gfycat.com/circularsomeavians",
            "https://gfycat.com/pepperybossydachshund",
            "https://gfycat.com/fairmemorablecats",
            "https://gfycat.com/coldmaturegermanshepherd",
            "https://gfycat.com/equatorialsleepyfieldspaniel",
            "https://gfycat.com/fatdeadlydog",
            "https://gfycat.com/candidwarmheartedgreyhounddog",
            "https://gfycat.com/grizzledboguseasternnewt",
            "https://gfycat.com/icyklutzyelephantbeetle",
            "https://gfycat.com/ignorantdefiantfrogmouth",
            "https://gfycat.com/madeupshamefulcarpenterant",
            "https://gfycat.com/peacefulplayfulcuckoo",
            "https://gfycat.com/informalmedicalbobolink",
            "https://gfycat.com/inferiorlastingangelwingmussel"]

    @commands.command()
    async def weeekly(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Weeekly {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "soojin":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Soojin :heart:')
            await ctx.send(random.choice(self.bot.weeekly_soojin_gif))
            await ctx.message.delete()
        elif arg == "jiyoon":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jiyoon :heart:')
            await ctx.send(random.choice(self.bot.weeekly_jiyoon_gif))
            await ctx.message.delete()
        elif arg == "monday":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Monday :heart:')
            await ctx.send(random.choice(self.bot.weeekly_monday_gif))
            await ctx.message.delete()
        elif arg == "soeun":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Soeun :heart:')
            await ctx.send(random.choice(self.bot.weeekly_soeun_gif))
            await ctx.message.delete()
        elif arg == "jaehee":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jaehee :heart:')
            await ctx.send(random.choice(self.bot.weeekly_jaehee_gif))
            await ctx.message.delete()
        elif arg == "jihan":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jihan :heart:')
            await ctx.send(random.choice(self.bot.weeekly_jihan_gif))
            await ctx.message.delete()
        elif arg == "zoa":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Zoa :heart:')
            await ctx.send(random.choice(self.bot.weeekly_zoa_gif))
            await ctx.message.delete()

def setup(client):
    client.add_cog(weeekly(client))