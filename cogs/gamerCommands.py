import discord, random, os
from discord.ext import commands
from datetime import datetime

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.logs
logs = 786515662214397973
#.luminary bot-commands
kbotcom = 764610881513324574

#//people
muffin = 488423352206229505
gareth = 389897179701182465
mae = 492769416610840586
aster = 495714786823241728

class gamerPings(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.dream_gif = ["https://tenor.com/view/dream-george-not-found-sapnap-speedrunning-manhunt-gif-18187566",
            "https://tenor.com/view/minecraft-dream-gif-18394858",
            "https://tenor.com/view/popipo-dream-scrundy-pundy-technoblade-sapnap-gif-18226411",
            "https://tenor.com/view/dream-dreamwastaken-minecraft-desert-dance-gif-18987175",
            "https://tenor.com/view/dream-dreamwastaken-minecraft-gif-18176440",
            "https://tenor.com/view/dream-team-minecraft-love-dream-sapnap-gif-18710509"]

        self.food_gif = ["https://gfycat.com/uncomfortablesafebarbet",
            "https://tenor.com/view/jenniekim-gif-18818029",
            "https://tenor.com/view/tipton2109-nct-nct-mark-mark-lee-regular-gif-13173755",
            "https://tenor.com/view/sakura-miyawaki-sakura-izone-%E3%81%95%E3%81%8F%E3%82%89-%E5%AE%AE%E8%84%87%E5%92%B2%E8%89%AF-gif-14974458",
            "https://tenor.com/view/jisoo-food-blackpink-kpop-eating-gif-9473818",
            "https://tenor.com/view/hwasa-lollipop-kpop-be-calm-beautiful-day-gif-18873828",
            "https://tenor.com/view/lalisa-manoban-lisa-blackpink-lollipop-kpop-gif-17772815",
            "https://tenor.com/view/seulgi-kang-seulgi-red-velvet-cute-bear-gif-16728717",
            "https://tenor.com/view/wheein-mamamoo-eating-eggs-eating-egg-idol-gif-18928054",
            "https://tenor.com/view/mamamoo-hwasa-ahn-hye-jin-vocalist-rapper-gif-17583679",
            "https://tenor.com/view/hwasa-eat-eating-ramen-hot-gif-12261725",
            "https://tenor.com/view/mamamoo-solar-eating-pole-bibimbap-gif-16227163",
            "https://tenor.com/view/izone-hyewon-eating-gif-13780770",
            "https://tenor.com/view/chou-tzuyu-kpop-gif-11360919",
            "https://tenor.com/view/toosie-slide-cute-eat-jennie-jennie-kim-gif-16780128",
            "https://media.giphy.com/media/disxZ6CKe4b9wbFhhT/giphy.gif",
            "https://tenor.com/view/mamamoo-wheein-strawberry-yum-gif-7596438",
            "https://tenor.com/view/jo-yuri-yuri-iz-one-cute-eating-gif-14800422",
            "https://gfycat.com/miserableslipperygartersnake",
            "https://gfycat.com/aridpitifulchipmunk",
            "https://gfycat.com/zealousunsightlyhumpbackwhale",
            "https://gfycat.com/vaguefreshflickertailsquirrel",
            "https://tenor.com/view/mark-mark-lee-nct-cold-eating-gif-14683790",
            "https://gfycat.com/unconsciousweirdfishingcat",
            "https://tenor.com/view/yeeun-jang-clc-not-yummy-gif-13252749",
            "https://tenor.com/view/yum-delicious-cheng-xiao-yummy-gif-12031986",
            "https://gfycat.com/flamboyantunlinedisabellinewheatear",
            "https://gfycat.com/limpingunrulygrasshopper",
            "https://gfycat.com/sentimentalmadeupgrayfox",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378241817608192/image3.gif",
            "https://tenor.com/view/soyeon-senorita-g-idle-cute-kpop-kpop-girl-group-gif-15338342",
            "https://tenor.com/view/shuhua-yeh-shuhua-shuhua-gidle-shuhua-idle-gidle-gif-19200395",
            "https://tenor.com/view/moonbyul-lunch-tang-hulu-cutie-mamamoo-gif-17053045",
            "https://tenor.com/view/hotel-del-luna-iu-eating-chew-bite-gif-17750091",
            "https://tenor.com/view/delicious-cant-stop-unstoppable-eating-again-gif-17375580",
            "https://tenor.com/view/solar-solarsido-mamamoo-eating-gif-14246383",
            "https://tenor.com/view/hitomi-honda-hitomi-%ED%9E%88%ED%86%A0%EB%AF%B8-%ED%98%BC%EB%8B%A4%ED%9E%88%ED%86%A0%EB%AF%B8-wow-gif-14017107",
            "https://tenor.com/view/nct-nct127-jaehyun-coffee-work-gif-12640382",
            "https://tenor.com/view/mamamoo-moonbyul-solar-moonsun-veggies-gif-7724635",
            "https://tenor.com/view/moonbyul-gif-7446949",
            "https://gfycat.com/longadmiredindianspinyloach",
            "https://tenor.com/view/hyojung-gif-19800693",
            "https://tenor.com/view/hyojung-gif-19857822",
            "https://tenor.com/view/oh-my-girl-omg-kpop-cute-pretty-gif-17578691",
            "https://gfycat.com/harmlesssecondappaloosa",
            "https://gfycat.com/evendismalamphibian",
            "https://tenor.com/view/chuu-loona-kim-jiwoo-loonatheworld-kpop-gif-gif-19449093",
            "https://tenor.com/view/wayv-nct-xiao-xiaojun-xiao-de-jun-gif-17708611",
            "https://tenor.com/view/jungkook-eating-jungkook-cute-jungkook-hot-jungkook-bts-jungkookie-gif-19814145",
            "https://cdn.discordapp.com/attachments/800224391258439721/800565546701160458/f1fc5f292c3132ff952b3b50e952698b.gif",
            "https://gfycat.com/soggyaccomplishedcolt-heejin-loona",
            "https://gfycat.com/agilefamiliariberianmidwifetoad",
            "https://gfycat.com/closefreshbantamrooster-yeojin-loona",
            "https://gfycat.com/admiredharshgrebe-yeojin-loona",
            "https://gfycat.com/blackshockingazurevasesponge-yeojin-loona",
            "https://gfycat.com/honoredcluelessleveret-yeojin-loona",
            "https://gfycat.com/faintcookedgreatwhiteshark-yeojin-loona",
            "https://gfycat.com/breakableequatorialcod-loona-yves-chuu",
            "https://gfycat.com/flusteredremarkablegnat-kim-lip",
            "https://gfycat.com/insecurepastanhinga-jinsoul-loona",
            "https://gfycat.com/helpfulwholedoctorfish-jinsoul-loona-chuu",
            "https://gfycat.com/handmadedisastrousdipper-loona-yves",
            "https://gfycat.com/flimsypiercingdugong",
            "https://gfycat.com/cavernousforcefulcicada-loona-gowon",
            "https://gfycat.com/delectableminiaturefurseal-gowon-loona",
            "https://gfycat.com/clutteredrewardingbackswimmer",
            "https://gfycat.com/breakabletotalkingbird-olivia-hye-choerry-jinsoul-loona",
            "https://gfycat.com/accomplisheduniformleafbird-loona-chuu",
            "https://gfycat.com/angelicsandybobolink-loona-chuu",
            "https://gfycat.com/backwhiteafricanparadiseflycatcher",
            "https://gfycat.com/fearlesspeskybrownbear",
            "https://gfycat.com/failingmammothatlasmoth-loona-chuu",
            "https://gfycat.com/impracticalpotablebunting-loona-chuu",
            "https://gfycat.com/colorlessgargantuandinosaur",
            "https://gfycat.com/harmfulperfumedhake-loona-chuu",
            "https://gfycat.com/ignorantsilverbumblebee-dating-class-loona-chuu",
            "https://cdn.discordapp.com/attachments/802261212846882826/802263665729863700/image0.gif",
            "https://cdn.discordapp.com/attachments/798320383539412992/806345491176620072/image0.gif",
            "https://gfycat.com/quarterlyinexperiencedanura",
            "https://64.media.tumblr.com/3629e5aed89ff2a1aa94a51a9ac0396d/ba269b895e46fb77-2d/s400x600/766afd4caedc073d6001eb909116fe2c0fea4c4d.gif",
            "https://gfycat.com/tartpastellangur",
            "https://cdn.discordapp.com/attachments/485095951480913935/810817528095309844/MV_SOYOU_X_IZONE___ZEROATTITUDE_FeatpH-1.gif",
            "https://gfycat.com/ampleadeptadmiralbutterfly",
            "https://gfycat.com/leansleepyindigowingedparrot",
            "https://gfycat.com/simplejealoushornedtoad",
            "https://64.media.tumblr.com/911ae07c047c16b4b61b9b71ecd29a61/7290f64bf1c77ddd-dc/s250x400/903498bd7d758c0308db075034b7f432b5ba8366.gif",
            "https://64.media.tumblr.com/81c6a572ba6f49481b1ec7ad8d1cc9f4/7290f64bf1c77ddd-2d/s250x400/25fe40f7704f40d63a4f0ddd1c7d0a4f42608344.gif",
            "https://64.media.tumblr.com/58aac89283e92150e9135a7c07948efc/f4d925f44e07bc74-fe/s400x600/0d68b0aca7ebce4842245dd522008f41ee1a67b9.gif",
            "https://64.media.tumblr.com/26195c752ead6f20c38191f1fbe8c29f/9cb1c0cb6ff1dcd4-92/s250x400/36634e195d411ccc5f93137e5560aadd6306cc84.gif",
            "https://64.media.tumblr.com/e7098e2f708c07b5cafce6a83e67bf56/9cb1c0cb6ff1dcd4-36/s250x400/71ed86c087e50fb3e68350a20ad6811a5af92221.gif",
            "https://64.media.tumblr.com/2c489910af03d86217a11d4766682d41/7cccc6538fb782ed-70/s400x600/d8d7d3ae140f15148cf90b8cbb85fe1a6ac2f733.gif",
            "https://gfycat.com/actualaccurateayeaye",
            "https://gfycat.com/blindfabulousamericanbadger",
            "https://gfycat.com/poshadventurousequine",
            "https://gfycat.com/evergreenforsakenimperatorangel",
            "https://gfycat.com/immaterialcourageousblueandgoldmackaw",
            "https://gfycat.com/flatspicyeyelashpitviper",
            "https://gfycat.com/sleepyamusedgharial",
            "https://gfycat.com/dependableannualamazondolphin",
            "https://gfycat.com/whimsicalsimilarannashummingbird",
            "https://gfycat.com/silkyparchedgrayreefshark",
            "https://gfycat.com/weeklyshabbyindianskimmer",
            "https://gfycat.com/bestcompassionateleafwing",
            "https://tenor.com/view/chungha-chungha-eat-chungha-staring-chungha-look-stare-gif-19318960",
            "https://tenor.com/view/taemin-shinee-kpop-korean-ice-cream-gif-7371003",
            "https://gfycat.com/eagerembarrassedgrouper-blackpink-rose-kpop",
            "https://gfycat.com/everlastingnaivecrow-24365-with-blackpink-kpop-rose",
            "https://gfycat.com/understatedabandoneddarwinsfox-blackpink-jennie",
            "https://gfycat.com/blissfulimpartialcobra-blackpink-adorable-jennie-cute",
            "https://gfycat.com/acidicunknownblacklab-beauty",
            "https://thumbs.gfycat.com/TartBabyishHorse-max-1mb.gif",
            "https://tenor.com/view/sip-tea-sips-tea-sipping-tea-tea-not-my-problem-gif-17953668",
            "https://gfycat.com/cheeryfatherlyjerboa-oh-my-girl-kpop-yooa-dsl",
            "https://gfycat.com/completefixedbaldeagle-lee-yongbok-stray-kids-lee-felix-adorable-kpop",
            "https://tenor.com/view/han-gif-13343941",
            "https://tenor.com/view/ka-wanna-one-kang-daniel-kang-daniel-danirl-ori-cat-wannable-kpop-gif-12633990",
            "https://tenor.com/view/kpop-bts-jin-food-eating-gif-4896466",
            "https://tenor.com/view/changmin-tvxq-max-shim-changmin-kpop-gif-16896910",
            "https://tenor.com/view/jimin-bts-kpop-kpop-idol-food-gif-7314625",
            "https://tenor.com/view/%EC%97%90%EB%A6%AD%EB%82%A8-%EB%82%A8%EC%9C%A4%EB%8F%84-eric-nam-kpop-eat-gif-18362142",
            "https://tenor.com/view/somi-vitasom-gif-8958750",
            "https://tenor.com/view/somi-eating-food-gif-8958728",
            "https://tenor.com/view/somi-abyan-gif-18258549",
            "https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-soobin-gif-16784698",
            "https://tenor.com/view/yeonjun-eating-yeonjun-sanapinkhair-gif-18606067",
            "https://tenor.com/view/txt-beomgyu-eating-sweet-cute-gif-14481352",
            "https://tenor.com/view/sookai-soobin-hueningkai-kai-hyuka-gif-18364963",
            "https://gfycat.com/farawaydecentbluewhale-weki-meki-yoojung-food-kpop",
            "https://gfycat.com/poisedsoftafricanrockpython",
            "https://gfycat.com/achinghiddenislandcanary",
            "https://gfycat.com/creepyposhjackal-fromis9-chaeyoung-lee-chaeyoung-fromis-9-idol",
            "https://gfycat.com/infantileimpeccablehammerkop-chaeyoungs-challenge-channel-9-love-bomb",
            "https://gfycat.com/belatedunevenlemming-fromis9",
            "https://64.media.tumblr.com/f29c4f88c563ac00b6f794948fff42f8/tumblr_po5zevs5IE1y42eufo8_r1_400.gif",
            "https://tenor.com/view/sunwoo-the-boyz-tbz-sunwoo-sunwooeating-sunu-gif-18876590",
            "https://tenor.com/view/kai-exo-ice-cream-eat-happy-gif-5037456",
            "https://gfycat.com/happybasicgermanwirehairedpointer",
            "https://gfycat.com/lineartarteagle",
            "https://tenor.com/view/younghoon-chanhee-the-boyz-tbz-tbz-younghoon-gif-18984986",
            "https://pa1.narvii.com/6652/c0a9b4ac7dee8693aaf70678c5d80e29de8d618c_hq.gif",
            "https://64.media.tumblr.com/730a29363f90d4d7dacfc55189765149/tumblr_oz5wckrDOQ1vkvtego7_r1_500.gif",
            "https://i.pinimg.com/originals/e0/3d/33/e03d339a2aaeff48160dec2e88ef0ac0.gif",
            "https://64.media.tumblr.com/9411c9fd3166072b172037c355f39d9c/tumblr_oz5wckrDOQ1vkvtego5_r1_500.gif",
            "https://media1.tenor.com/images/e2c72ab7088c41687ffa8104ab4890b7/tenor.gif?itemid=6042730",
            "https://tenor.com/view/txt-yeonjun-eating-bleuiz-gif-19716063",
            "https://tenor.com/view/seulgicfm-yeonjun-eating-gif-19467105",
            "https://gfycat.com/enragedlimpingivorybilledwoodpecker-battle-trip-weki-meki-yoojung-bulgogi-korean-food",
            "https://gfycat.com/poisedsoftafricanrockpython",
            "https://gfycat.com/thindefinitecarpenterant-weki-meki-wekimeki-yoojung-weme",
            "https://data.whicdn.com/images/306259352/original.gif",
            "https://thumbs.gfycat.com/SeveralInferiorGroundhog-size_restricted.gif",
            "https://i.pinimg.com/originals/39/c3/84/39c384b96c6b1fffa5426ed7a1e43cca.gif",
            "https://i.pinimg.com/originals/66/0f/fa/660ffa490c7cd211ae258448d74ae7f7.gif",
            "https://data.whicdn.com/images/273506482/original.gif",
            "https://i.pinimg.com/originals/38/66/71/386671ad789942f2ebfe47913247cd12.gif",
            "https://i.pinimg.com/originals/35/e0/a1/35e0a1a1613a019d4de3b53d2d5f18b7.gif",
            "https://i.pinimg.com/originals/41/31/34/4131340b5b9422311286b0e572fc4546.gif",
            "https://gfycat.com/excitablescratchyicelandichorse-chaeyeon-izone-nako",
            "https://tenor.com/view/angai313-snsd-soshi-girls-generation-tiffany-young-gif-20028381",
            "https://gfycat.com/powerlesshighkatydid",
            "https://cdn1.diodeo.kr/cdn/webzine/2019/11/29/20191129121516_zkgagfdu.gif",
            "https://gfycat.com/fakedaringkiskadee",
            "https://gfycat.com/activebriskamericanwarmblood",
            "https://gfycat.com/spectacularkaleidoscopicboubou",
            "https://gfycat.com/ethicalwildindianjackal",
            "https://gfycat.com/grimornerygermanwirehairedpointer",
            "https://gfycat.com/inconsequentialrecentcrow",
            "https://gfycat.com/SnoopyTimelyHogget",
            "https://gfycat.com/GiftedLoathsomeAlpinegoat",
            "https://gfycat.com/PrestigiousTidyEuropeanfiresalamander",
            "https://gfycat.com/aromaticdimwittedglassfrog",
            "https://gfycat.com/ImpressionableEducatedEider",
            "https://gfycat.com/ChillyZanyGalapagosmockingbird",
            "https://gfycat.com/HilariousJoyfulBushsqueaker",
            "https://gfycat.com/YellowishHonorableKinkajou",
            "https://gfycat.com/AcrobaticMeagerAmericanquarterhorse",
            "https://gfycat.com/euphoricfeistykookaburra",
            "https://gfycat.com/quickfixedindianhare",
            "https://tenor.com/view/yeri-red-velvet-gif-11323706",
            "https://gfycat.com/RecklessRewardingEidolonhelvum",
            "https://gfycat.com/UnhappyBadBeetle",
            "https://tenor.com/view/crystal-clear-yeeun-korean-cute-gif-16805024",
            "https://tenor.com/view/kwon-eunbin-eunbin-clc-maknae-cube-entertainment-gif-17697064",
            "https://tenor.com/view/cute-yujin-clc-hi-wave-gif-13944583",
            "https://tenor.com/view/clc-elkie-hungry-eating-gif-13944518",
            "https://i.pinimg.com/originals/5a/b6/6c/5ab66c4e8d4607b8a34a272bafdf80f7.gif",
            "https://data.whicdn.com/images/319081662/original.gif",
            "https://d.wattpad.com/story_parts/727104930/images/159ab7d3f4edc87d40297965869.gif",
            "https://data.whicdn.com/images/349284985/original.gif",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-nt-natty-natty_gif-gif-19360528",
            "https://gfycat.com/improbablemerryegg",
            "https://gfycat.com/lastingmeaslydodo",
            "https://gfycat.com/compassionateoccasionalborderterrier",
            "https://gfycat.com/frigidinconsequentialbandicoot",
            "https://gfycat.com/scalysmallcopperbutterfly",
            "https://gfycat.com/silkyhealthyadeliepenguin",
            "https://64.media.tumblr.com/4c8ccb5971f27489d6612f009f14085f/302e44f76695bfda-07/s540x810/888e5bc69d9e083c6abde2229d9b998f5b3a1db9.gif",
            "https://tenor.com/view/loona-chuu-kpop-gif-20917460"]

        self.monke = ["https://www.youtube.com/watch?v=PipzizkF-SY",
            "https://www.youtube.com/watch?v=-JUhUI_KvUI",
            "https://www.youtube.com/watch?v=05sJVEwZuZ4",
            "https://www.youtube.com/watch?v=2EKKMof_Ywg",
            "https://www.youtube.com/watch?time_continue=5&v=-a57_IOKpjM&feature=emb_logo"]

        self.tuna_wrong = ["Tina",
            "Yuna",
            "Putuna",
            "Tanu",
            "Natu",
            "Utah",
            "Yuta",
            "Runa",
            "Robotuna",
            "Tetanus",
            "Toupe",
            "Toonami",
            "Toothpaste",
            "Toonie",
            "2na",
            "Attituna",
            "Toilet Lid",
            "Nuna",
            "Toque",
            "Tube",
            "Tulips",
            "Turina",
            ":sparkles:TUNAAA:sparkles:",
            "Forgetuna"]

        self.paul_wrong = ["Pual",
            "Anpaul"]

    @commands.command()
    async def food(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [food] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to #bot-commands', delete_after=2)
        else:
            # await ctx.send(f'Aster is the best :smiling_face_with_3_hearts:')
            await ctx.send(random.choice(self.food_gif))

    @commands.command()
    async def screm(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [screm] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send('https://tenor.com/view/loona-loona-hyunjin-hyunjin-kim-hyunjin-loona-aeong-gif-18902504')
        await ctx.message.delete()

    @commands.command()
    async def weakado(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [weakado] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'<@259409277482041344> fiesta good \nhttps://www.youtube.com/watch?v=eDEFolvLn0A')
        await ctx.message.delete()

    @commands.command()
    async def veery(self,ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [veery] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'https://cdn.discordapp.com/attachments/735713250989309984/779101391871934484/veery_good.mp3')
        await ctx.message.delete()

    @commands.command()
    async def ren(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [ren] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'I love you <@749085760354910280>')

    @commands.command()
    async def muffin(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Muffin] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'<@!{ctx.author.id}> :heart: you <@488423352206229505>')

    @commands.command()
    async def aster(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Aster] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'<@{ctx.author.id}> :heart: you <@{aster}>!')

    @commands.command()
    async def god(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [G O D] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'<@!{ctx.author.id}> says stop being sus <@573974040679809044>')

    @commands.command()
    async def tuna(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Tuna] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'*{random.choice(self.tuna_wrong)}')

    @commands.command()
    async def paul(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Paul] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'*{random.choice(self.paul_wrong)}')

    @commands.command()
    async def nomi(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Nomi] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'<:nomiVERYbuffbackwards:818618947293282364><:neck:816367879209091113><:nomiVERYbuff:817139078641745940>')

    @commands.command()
    async def llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if ctx.author.id == muffin or ctx.author.id == gareth or ctx.author.id == mae:            
            embed=discord.Embed(
                    title = 'llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch',
                    description = '🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿',
                    colour = discord.Color.from_rgb(0,173,54))
            embed.set_footer(text="What happened on the fishing trip?")
            embed.add_field(name='Llanymawddwy:', value=f'```\nFfion\nFfion\nFfion\nFfion\nFfion\nFfion```', inline=True)
            embed.add_field(name='Llanrhychwyn:', value=f'```\nFfion\nFfion\nFfion\nFfion\nFfion\nFfion```', inline=True)
            embed.add_field(name='Llanbrynmair:', value=f'```\nFfion\nFfion\nFfion\nFfion\nFfion\nFfion```', inline=True)
            embed.add_field(name='Pontrhydfendigaid:', value=f'```\nFfion\nFfion\nFfion\nFfion\nFfion\nFfion```', inline=True)
            embed.add_field(name='Pontnewynydd:', value=f'```\nFfion\nFfion\nFfion\nFfion\nFfion\nFfion```', inline=True)
            embed.add_field(name='Pontrhydygroes:', value=f'```\nFfion\nFfion\nFfion\nFfion\nFfion\nFfion```', inline=True)
            await ctx.send(embed=embed)
            await ctx.message.delete()

    @commands.command()
    async def caillou(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Caillou] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'Hey, {ctx.author.name} are you a short little bald white boy on a television kids show?\nBecause youre Caillou-te')
        await ctx.message.delete()

    @commands.command()
    async def pickupline(self, ctx, *, name=f'Bae Suzy Is the Best'):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Pickupline] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if name == "Bae Suzy Is the Best":
            person = ctx.author.name
        else:
            person = name
        number = random.randint(1,4)
        if number == 1:
            await ctx.send(f'Hey, {person} are you a short little bald white boy on a television kids show?\nBecause youre Caillou-te')
        # elif number == 2:
        #     await ctx.send(f'If you are the us police can I be systematic racism?\nBecause I think we\'d be naturally together')
        elif number == 3:
            await ctx.send(f'Hey, {person}, are you Bae Suzy?\nBecause you could literally punch me and I\'d be thankful')
        elif number == 4:
            await ctx.send(f'Hey, {person},  are you hawaiin bread rolls?\nBecause I love your buns')
        elif number == 2:
            await ctx.send(f'Hey, {person}, are you Jo Yuri?\nBecause, Jo, Yuri-lly pretty')
        else:
            await ctx.send(f'{person}, please report this to @muffin521#9280, or in the support server: https://discord.gg/Ntk9Jp26yx')

        
def setup(client):
    client.add_cog(gamerPings(client))