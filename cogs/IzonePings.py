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
weakado = 259409277482041344
jat = 236787566530134017
k8 = 573974040679809044
agus = 683791381667250208
mae = 492769416610840586
cronus = 186533260803833858
luke = 150742733743587328

class IzonePings(commands.Cog):

#saku command is special for now bc i cant be asked to fix em rn

    def __init__(self, bot):
        self.bot = bot

        self.bot.sakura_gif = ["https://tenor.com/view/sakura-miyawaki-sakura-izone-%E3%81%95%E3%81%8F%E3%82%89-%E5%AE%AE%E8%84%87%E5%92%B2%E8%89%AF-gif-14974458",
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
            "https://tenor.com/view/sakura-fiesta-sakura-miyawaki-sakura-sakura-angry-hkt48sakura-gif-16419142",
            "https://gfycat.com/handsomesaltycapybara",
            "https://gfycat.com/grouchytautarcherfish",
            "https://gfycat.com/barrenhonoreddavidstiger",
            "https://gfycat.com/revolvingshrillacouchi",
            "https://gfycat.com/blackandwhitegoodnaturedcockatiel",
            "https://gfycat.com/fewclosedaxolotl",
            "https://gfycat.com/nextilliterateelephantseal",
            "https://gfycat.com/scentedinsidiousfruitfly",
            "https://gfycat.com/glisteningleafyleafhopper",
            "https://gfycat.com/colossalfarawaylamb",
            "https://gfycat.com/leftlavishargali",
            "https://gfycat.com/vaguesnappyenglishpointer",
            "https://gfycat.com/deadobedientdeinonychus",
            "https://tenor.com/view/izone-sakura-yuri-cute-gif-15886887",
            "https://tenor.com/view/sakura-miyawaki-izone-nekkoya-produce48-smile-gif-13510047",
            "https://gfycat.com/entirejampackedfairybluebird",
            "https://gfycat.com/tediousfarflungbighornsheep",
            "https://gfycat.com/fatherlywiltedharborseal",
            "https://gfycat.com/ringedfaithfulbison",
            "https://gfycat.com/basicnaivebeaver",
            "https://gfycat.com/handsomesaltycapybara",
            "https://gfycat.com/soggywarmgeese",
            "https://gfycat.com/freshfarflunglcont",
            "https://gfycat.com/silverhatefulatlanticsharpnosepuffer",
            "https://gfycat.com/oldqualifiedleafcutterant",
            "https://gfycat.com/vigilantobviousantbear",
            "https://gfycat.com/kaleidoscopicjaggedamoeba",
            "https://gfycat.com/incomparablehighlevelamericanwarmblood",
            "https://gfycat.com/embellishedcelebratedgopher",
            "https://gfycat.com/daringseparatefattaileddunnart",
            "https://gfycat.com/ancientlegalcrane",
            "https://gfycat.com/weightynauticalbufeo",
            "https://gfycat.com/totalforkedbushsqueaker",
            "https://gfycat.com/weightynauticalbufeo",
            "https://gfycat.com/weakcheerfulcurlew",
            "https://gfycat.com/qualifiedfittingfulmar",
            "https://gfycat.com/capitalklutzyamericanshorthair",
            "https://tenor.com/view/sakura-kpop-la-vie-en-rose-gif-gif-15101462",
            "https://gfycat.com/ancientlegalcrane",
            "https://gfycat.com/weightynauticalbufeo"]

        self.bot.yuri_gif = ["https://tenor.com/view/iz-one-jo-yuri-cute-tilt-kpop-gif-16502904",
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
            "https://media.discordapp.net/attachments/724107459265953835/770832512620036157/image2.gif",
            "https://tenor.com/view/sakura-miyawaki-sakura-izone-jo-yuri-yuri-gif-18738707",
            "https://tenor.com/view/izone-yuri-kpop-cute-happy-gif-16325829",
            "https://cdn.discordapp.com/attachments/704248706269970488/776652835617898516/image0.gif",
            "https://tenor.com/view/izone-sakura-yuri-cute-gif-15886887",
            "https://gfycat.com/untriedshadowyeelelephant",
            "https://gfycat.com/nippypersonalbullmastiff",
            "https://gfycat.com/conscioushilariouscanvasback",
            "https://gfycat.com/eachlinearafricanfisheagle",
            "https://gfycat.com/welloffselfassuredfinnishspitz",
            "https://gfycat.com/sophisticatedslipperyasiaticlesserfreshwaterclam",
            "https://gfycat.com/idealisticappropriateafricanrockpython",
            "https://gfycat.com/nextpeacefuljaeger",
            "https://gfycat.com/niftyagitatedindianringneckparakeet",
            "https://gfycat.com/anxiousgloriousestuarinecrocodile",
            "https://gfycat.com/deliriousidioticfennecfox",
            "https://gfycat.com/maturequeasyafghanhound",
            "https://gfycat.com/totalunevenelephant",
            "https://tenor.com/view/jo-yuri-yuri-izone-yuri-fiesta-cute-gif-19457732",
            "https://media.discordapp.net/attachments/444028614925877249/782987382609412126/24AA599A-5264-4A81-8A42-06EAF6CC565E.gif",
            "https://gfycat.com/enchantingdeadlyconey",
            "https://media.discordapp.net/attachments/735713250989309984/782439245087506493/image0.gif",
            "https://tenor.com/view/jo-yuri-yuri-pinch-gif-13398933",
            "https://tenor.com/view/singing-performance-iz-one-yuri-jo-yuri-gif-17890516",
            "https://gfycat.com/greatimaginarygadwall",
            "https://gfycat.com/anxiousgloriousestuarinecrocodile",
            "https://gfycat.com/gratefulmildfallowdeer",
            "https://gfycat.com/grotesqueagreeablecuttlefish",
            "https://gfycat.com/freshcontentdavidstiger",
            "https://gfycat.com/hotmellowamericanbittern",
            "https://gfycat.com/deafeningdapperhumpbackwhale",
            "https://gfycat.com/deepforkedbass",
            "https://gfycat.com/shockednaughtygypsymoth",
            "https://gfycat.com/measlylightblacklab",
            "https://gfycat.com/medicallameafricanmolesnake",
            "https://gfycat.com/defiantmediocreisabellineshrike",
            "https://gfycat.com/fluffyspeedydrafthorse",
            "https://gfycat.com/vibrantaltruisticarabianhorse",
            "https://gfycat.com/shadyquestionabledunlin",
            "https://gfycat.com/easyrightbumblebee",
            "https://gfycat.com/scientificmeagergrebe",
            "https://gfycat.com/boilingjointbongo",
            "https://gfycat.com/dentalevenbat",
            "https://gfycat.com/validsamebilby",
            "https://gfycat.com/generouscolossalhousefly",
            "https://gfycat.com/rawcomfortablebighornsheep",
            "https://gfycat.com/dizzyspecificchuckwalla",
            "https://gfycat.com/welltodoapprehensivebug",
            "https://gfycat.com/remotewellinformedbass",
            "https://gfycat.com/insidiousfemaleauk",
            "https://gfycat.com/yellowelectrichoki",
            "https://gfycat.com/optimalweepybangeltiger",
            "https://gfycat.com/giganticincrediblecranefly",
            "https://gfycat.com/consciousdistortedargentinehornedfrog",
            "https://gfycat.com/jitteryimpureemeraldtreeskink",
            "https://gfycat.com/cookedsatisfiedhorseshoecrab",
            "https://gfycat.com/ShockedRapidIguanodon",
            "https://gfycat.com/shinyscaryamericanratsnake",
            "https://gfycat.com/elatedtartbighorn",
            "https://tenor.com/view/jo-yuri-yuri-izone-produce48-babieyuri-gif-13815492",
            "https://tenor.com/view/iz-one-jo-yuri-dancing-kpop-cute-gif-16129481",
            "https://gfycat.com/gratefulenergetichaddock",
            "https://gfycat.com/limitedwetichthyosaurs",
            "https://gfycat.com/coldbriskdragonfly",
            "https://gfycat.com/enchantingdeadlyconey",
            "https://gfycat.com/inborndistantalleycat",
            "https://gfycat.com/elaboratedetailedgangesdolphin",
            "https://cdn.discordapp.com/attachments/785329655388438531/788612427167563776/image0.gif",
            "https://gfycat.com/harshclosedblueshark",
            "https://gfycat.com/ficklethoughtfuldavidstiger",
            "https://cdn.discordapp.com/attachments/762508629680586775/789295589254758440/image0.gif",
            "https://gfycat.com/tenderimmaculategenet",
            "https://gfycat.com/heartywellwornhamster",
            "https://tenor.com/view/yuri-jo-yuri-izone-angy-gif-18738700"]

        self.bot.chaeyeon_gif = ["https://tenor.com/view/lee-chaeyeon-chaeyeon-chaeyeon-izone-smile-cute-gif-15840463",
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
            "https://media.discordapp.net/attachments/498138615415701524/780998564901552128/hyewonbonk.gif",
            "https://gfycat.com/imperfectwealthyislandwhistler",
            "https://gfycat.com/creepycleancanine",
            "https://tenor.com/view/izone-jang-wonyoung-miyawaki-sakura-jo-yuri-choi-yena-gif-17514952",
            "https://tenor.com/view/panorama-mv-izone-chaeyeonvrs-chaeyeon-gif-19460367",
            "https://gfycat.com/imperfectwealthyislandwhistler",
            "https://tenor.com/view/chaeyeon-lee-chaeyeon-izone-chaeyeon-izone-gif-14243671",
            "https://gfycat.com/forcefulfailingbluewhale-chaeyeon-surprise-izone-hyewon-minju-aijeuweon",
            "https://gfycat.com/bossyweteasternnewt",
            "https://gfycat.com/goldengreatguillemot",
            "https://gfycat.com/grossrichhairstreak",
            "https://gfycat.com/liveshortcopperhead",
            "https://gfycat.com/fittingloneaxolotl",
            "https://gfycat.com/blaringunlawfulblackfish",
            "https://gfycat.com/rightprestigiousborzoi",
            "https://gfycat.com/oblongwhisperedantbear"]

        self.bot.minju_gif = ["https://gfycat.com/lawfulickykodiakbear",
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
            "https://gfycat.com/impressionabledenseaffenpinscher",
            "https://gfycat.com/kindrequiredbooby/",
            "https://tenor.com/view/izone-minju-pretty-gif-14587149"]

        self.bot.wonyoung_gif = ["https://gfycat.com/illfatedjollyamericanwigeon",
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

        self.bot.hyewon_gif = ["https://tenor.com/view/izone-izone-hyewon-kang-hyewon-kcon-hyewon-kwangbae-gif-18839326",
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
            "https://tenor.com/view/hyewon-smile-pretty-gif-13780756",
            "https://media.discordapp.net/attachments/762508629680586775/786025895642267648/image0.gif",
            "https://gfycat.com/easylividcrab",
            "https://gfycat.com/negligibleimpossiblebackswimmer",
            "https://gfycat.com/thatdiligentcottontail",
            "https://gfycat.com/tinydefinitebelugawhale",
            "https://gfycat.com/sharpessentialarmednylonshrimp"]

        self.bot.chaewon_gif = ["https://gfycat.com/imaginarysickgoldenmantledgroundsquirrel",
            "https://gfycat.com/loathsomecommonamericancicada",
            "https://gfycat.com/imaginarysickgoldenmantledgroundsquirrel",
            "https://gfycat.com/pettygraciousdamselfly",
            "https://gfycat.com/aridpitifulchipmunk",
            "https://tenor.com/view/izone-chaewon-cute-smile-dimple-gif-15892640",
            "https://tenor.com/view/go-chaewon-chaewon-izone-chaewon-gif-18780582",
            "https://tenor.com/view/chaewon-nunu-nana-chaewon-nunu-nana-chaewon-dancing-gif-18593237",
            "https://tenor.com/view/izone-kim-chaewon-gif-18706592",
            "https://tenor.com/view/iz-one-jang-wonyoung-miyawaki-sakura-jo-yuri-choi-yena-gif-16110670",
            "https://gfycat.com/greendeficientanophelesmosquito",
            "https://blog.kakaocdn.net/dn/b9nMMY/btqQt4Lgstw/3CSWKVNGGfqdkLkyIgRqK1/img.gif",
            "https://gfycat.com/adorableidealatlanticspadefish",
            "https://gfycat.com/sharpessentialarmednylonshrimp",
            "https://gfycat.com/meekathleticgalapagosdove",
            "https://gfycat.com/costlyenchantedhornshark",
            "https://gfycat.com/costlyenchantedhornshark",
            "https://gfycat.com/responsiblelankyiggypops",
            "https://gfycat.com/variableunhappyborderterrier",
            "https://gfycat.com/potablewearyhellbender",
            "https://gfycat.com/tanhonesticelandicsheepdog",
            "https://gfycat.com/infinitenewanchovy"]

        self.bot.yujin_gif = ["https://tenor.com/view/ahn-yujin-cute-smile-gif-12316779",
            "https://tenor.com/view/an-yujin-bunny-cute-gif-13315682",
            "https://tenor.com/view/ahn-yujin-produce48-gif-12305976",
            "https://tenor.com/view/izone-yujin-gangsta-kpop-danger-gif-18438443",
            "https://tenor.com/view/yujin-an-yujin-izone-yujin-gif-18185002",
            "https://tenor.com/view/izone-yujin-ahn-yujin-lead-vocalist-lead-dancer-gif-17789677",
            "https://tenor.com/view/yujin-wink-izone-yujin-an-yujin-gif-18185000",
            "https://tenor.com/view/yujin-izone-yujin-an-yujin-gif-18184999",
            "https://tenor.com/view/yujin-yujin-laugh-yujin-izone-gif-19287696"]

        self.bot.yena_gif = ["https://tenor.com/view/rykkura-yena-cute-big-mouth-gif-16891786",
            "https://tenor.com/view/yena-choi-pretty-smile-kpop-gif-13596533",
            "https://tenor.com/view/izone-yena-yena-izone-yena-mirotic-gif-18216289",
            "https://tenor.com/view/choi-yena-yena-produce48-iz-one-juice-gif-15620870",
            "https://tenor.com/view/izone-izone-yena-choi-yena-izone-choi-yena-gif-19117524",
            "https://tenor.com/view/izone-choi-yena-kpop-cute-dance-gif-16540553",
            "https://tenor.com/view/yena-choi-yena-izone-izone-yena-fiesta-gif-18734350",
            "https://tenor.com/view/izone-yena-choi-yena-kpop-produce48-gif-19471725",
            "https://tenor.com/view/iz-one-iz-one-yena-yena-choi-yena-pretty-gif-15713414",
            "https://tenor.com/view/choi-yena-cute-silly-heart-izone-gif-13827415",
            "https://gfycat.com/respectfulaptbichonfrise"]

        self.bot.eunbi_gif = ["https://gfycat.com/illbowedguineapig",
            "https://gfycat.com/defiantmediocrearrowana",
            "https://gfycat.com/welcomepaleinchworm",
            "https://gfycat.com/tatteredpracticalalligatorgar",
            "https://gfycat.com/lankylargecanary",
            "https://tenor.com/view/izone-eunbi-cute-gif-15958774",
            "https://cdn.discordapp.com/attachments/485105297522688000/485852325395693568/eunbikazoo.gif",
            "https://cdn.discordapp.com/attachments/745090438427574385/785811922707546143/image0.gif",
            "https://cdn.discordapp.com/attachments/745090438427574385/785811950428356668/image0.gif",
            "https://cdn.discordapp.com/attachments/745090438427574385/785812017676156948/image0.gif",
            "https://cdn.discordapp.com/attachments/745090438427574385/785812039507116042/image0.gif",
            "https://gfycat.com/fewinsistentdromedary",
            "https://gfycat.com/revolvingaltruisticflatcoatretriever",
            "https://gfycat.com/marvelousmenacingamericanwarmblood",
            "https://gfycat.com/revolvingmajorfinnishspitz"]

        self.bot.nako_gif = ["https://tenor.com/view/rabbitnako-nako-nakorabbit-yabuki-yabuki-nako-gif-12814937",
            "https://tenor.com/view/iz-one-iz-one-nako-nako-nako-yabuki-pretty-gif-17724933",
            "https://tenor.com/view/izone-nako-nako-izone-nako-izone-gif-14398301",
            "https://tenor.com/view/nako-cute-kawaii-smile-gif-13731820",
            "https://tenor.com/view/izone-nako-nako-izone-nako-izone-gif-14398294",
            "https://tenor.com/view/iz-one-iz-one-nako-nako-nako-yabuki-pretty-gif-16463654",
            "https://tenor.com/view/izone-nako-nako-izone-nako-izone-gif-14398291",
            "https://tenor.com/view/kpop-izone-nako-nako-izone-happy-chuckle-gif-14398760"]

        self.bot.hitomi_gif = ["https://tenor.com/view/hitomi-honda-hitomi-%ED%9E%88%ED%86%A0%EB%AF%B8-%ED%98%BC%EB%8B%A4%ED%9E%88%ED%86%A0%EB%AF%B8-wow-gif-14017107",
            "https://tenor.com/view/%ED%98%BC%EB%8B%A4%ED%9E%88%ED%86%A0%EB%AF%B8-%ED%9E%88%ED%86%A0%EB%AF%B8-izone-hitomi-hitomi-honda-gif-16717168",
            "https://tenor.com/view/izone-hitomi-honda-hitomi-cant-hear-you-kpop-gif-17682854",
            "https://tenor.com/view/%ED%98%BC%EB%8B%A4%ED%9E%88%ED%86%A0%EB%AF%B8-%ED%9E%88%ED%86%A0%EB%AF%B8-hitomi-honda-hitomi-heart-gif-14161599",
            "https://tenor.com/view/%ED%98%BC%EB%8B%A4%ED%9E%88%ED%86%A0%EB%AF%B8-honda-hitomi-hitomi-%ED%9E%88%ED%86%A0%EB%AF%B8-iz-one-gif-17401631",
            "https://tenor.com/view/%ED%98%BC%EB%8B%A4%ED%9E%88%ED%86%A0%EB%AF%B8-%ED%9E%88%ED%86%A0%EB%AF%B8-izone-hitomi-hitomi-honda-gif-17151675",
            "https://tenor.com/view/%ED%98%BC%EB%8B%A4%ED%9E%88%ED%86%A0%EB%AF%B8-%ED%9E%88%ED%86%A0%EB%AF%B8-hitomi-honda-hitomi-huh-gif-16831035",
            "https://tenor.com/view/%ED%98%BC%EB%8B%A4%ED%9E%88%ED%86%A0%EB%AF%B8-%ED%9E%88%ED%86%A0%EB%AF%B8-hitomi-honda-hitomi-pretty-gif-16831042",
            "https://tenor.com/view/hitomi-honda-hitomi-%ED%98%BC%EB%8B%A4%ED%9E%88%ED%86%A0%EB%AF%B8-%ED%9E%88%ED%86%A0%EB%AF%B8-cute-gif-13981234"]


    @commands.command(aliases = ['saku', 'kkura']) #used to be purple_heart
    async def sakura(self, ctx):
        if (ctx.channel.id == kbotcom and ctx.guild.id == luminary) or ctx.guild.id == jst or ctx.guild.id == sadboi:
            await ctx.send(f'<@{weakado}>, <@!{ctx.author.id}> is talking about Sakura <:sakuraheart:787552522130554891>')
            await ctx.send(random.choice(self.bot.sakura_gif))
            await ctx.message.delete()
        elif ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Sakura <:sakuraheart:787552522130554891>')
            await ctx.send(random.choice(self.bot.sakura_gif))
            await ctx.message.delete()

    @commands.command() #used to be heart
    async def yuri(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{jat}>, <@{k8}>, <@!{ctx.author.id}> is talking about Yuri <:yuriheart:787552578447474689>')
                await ctx.send(random.choice(self.bot.yuri_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yuri <:yuriheart:787552578447474689>')
            await ctx.send(random.choice(self.bot.yuri_gif))
            await ctx.message.delete()

    @commands.command() #used to be white_heart
    async def chaeyeon(self, ctx):
        if ctx.guild.id == jst:
            await ctx.send(f'<@{luke}>, <@!{ctx.author.id}> is talking about Chaeyeon <:chaeyeonheart:787552459517722625>')
            await ctx.send(random.choice(self.bot.chaeyeon_gif))
            await ctx.message.delete()
        elif ctx.channel.id != 764610881513324574 and ctx.guild.id == 758468592957521972:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Chaeyeon <:chaeyeonheart:787552459517722625>')
            await ctx.send(random.choice(self.bot.chaeyeon_gif))
            await ctx.message.delete()

    @commands.command() #used to be frog
    async def minju(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{mae}>, <@{cronus}>, <@!{ctx.author.id}> is talking about Minju <:minjuheart:787553396734951454>')
                await ctx.send(random.choice(self.bot.minju_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Minju <:minjuheart:787553396734951454>')
            await ctx.send(random.choice(self.bot.minju_gif))
            await ctx.message.delete()

    @commands.command() #used to be rabbit
    async def wonyoung(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{mae}>, <@!{ctx.author.id}> is talking about Wonyoung <:wonyoungheart:787552538907115571>')
                await ctx.send(random.choice(self.bot.wonyoung_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Wonyoung <:wonyoungheart:787552538907115571>')
            await ctx.send(random.choice(self.bot.wonyoung_gif))
            await ctx.message.delete()

    @commands.command() #used to be cake
    async def hyewon(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{agus}>, <@!{ctx.author.id}> is talking about Hyewon <:hyewonheart:787552503121313832>')
                await ctx.send(random.choice(self.bot.hyewon_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Hyewon <:hyewonheart:787552503121313832>')
            await ctx.send(random.choice(self.bot.hyewon_gif))
            await ctx.message.delete()

    @commands.command() #used to be woman_fairy
    async def chaewon(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{agus}>, <@!{ctx.author.id}> is talking about Chaewon <:chaewonheart:787552449631879168>')
                await ctx.send(random.choice(self.bot.chaewon_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Chaewon <:chaewonheart:787552449631879168>')
            await ctx.send(random.choice(self.bot.chaewon_gif))
            await ctx.message.delete()

    @commands.command() #used to be woman_fairy
    async def yujin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yujin <:yujinheart:787552565322711080>')
                await ctx.send(random.choice(self.bot.yujin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yujin <:yujinheart:787552565322711080>')
            await ctx.send(random.choice(self.bot.yujin_gif))
            await ctx.message.delete()

    @commands.command() #used to be yellow_heart
    async def yena(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yena <:yenaheart:787552551834353695> ')
                await ctx.send(random.choice(self.bot.yena_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yena <:yenaheart:787552551834353695> ')
            await ctx.send(random.choice(self.bot.yena_gif))
            await ctx.message.delete()

    @commands.command() #used to be purple_heart
    async def eunbi(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Eunbi <:eunbiheart:787552473815973909>')
                await ctx.send(random.choice(self.bot.eunbi_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Eunbi <:eunbiheart:787552473815973909>')
            await ctx.send(random.choice(self.bot.eunbi_gif))
            await ctx.message.delete()

    @commands.command()
    async def nako(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{k8}>, <@!{ctx.author.id}> is talking about Nako <:nakoheart:787542480690216981>')
                await ctx.send(random.choice(self.bot.nako_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Nako <:nakoheart:787542480690216981>')
            await ctx.send(random.choice(self.bot.nako_gif))
            await ctx.message.delete()

    @commands.command() #used to be strawberry
    async def hitomi(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{k8}>, <@!{ctx.author.id}> is talking about Hitomi <:hitomiheart:787552489569517578>')
                await ctx.send(random.choice(self.bot.hitomi_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Hitomi <:hitomiheart:787552489569517578>')
            await ctx.send(random.choice(self.bot.hitomi_gif))
            await ctx.message.delete()


def setup(client):
    client.add_cog(IzonePings(client))