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
weakado = 259409277482041344

class everglow(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

        self.bot.eu_gif = ["https://tenor.com/view/eu-everglow-gif-18228811",
            "https://tenor.com/view/everglow-cute-aesthetic-kpop-gif-19189917",
            "https://tenor.com/view/everglow-eu-cute-gif-18070457",
            "https://tenor.com/view/everglow-eu-park-jiwon-leader-kpop-gif-16259144",
            "https://tenor.com/view/eu-everglow-gif-18601722",
            "https://tenor.com/view/eu-everglow-gif-18228815",
            "https://tenor.com/view/eu-everglow-gif-18891279",
            "https://tenor.com/view/everglow-eu-par-jiwon-leader-kpop-gif-16227322",
            "https://tenor.com/view/everglow-kpop-pretty-cute-beautiful-gif-15571693",
            "https://thumbs.gfycat.com/FalseElatedCoral-size_restricted.gif",
            "https://thumbs.gfycat.com/ElasticScarceJuliabutterfly-max-1mb.gif",
            "https://64.media.tumblr.com/9d6a7be34f7ef0ffd193b12d4fe28d3a/eeb3ab3561741b16-9e/s250x400/f26297555b2b8ac9b2a034f2136392bb963642e2.gif",
            "https://media1.tenor.com/images/72c5ddf23f98d80ed357fd28def87239/tenor.gif?itemid=18891254",
            "https://thumbs.gfycat.com/BronzeElaborateHorsemouse-size_restricted.gif",
            "https://64.media.tumblr.com/066025fff278af4c2cb175e7fcea4890/tumblr_pq5bgmFBWH1xu6x27o6_250.gif",
            "https://thumbs.gfycat.com/BountifulDismalGeese-size_restricted.gif",
            "https://i.pinimg.com/originals/c9/4e/ef/c94eef99cd50feb39e19cc30d280b06a.gif"]

        self.bot.mia_gif = ["https://tenor.com/view/everglow-mia-blow-kiss-kpop-cute-gif-15818623",
            "https://tenor.com/view/everglowmia-salute-gif-18117807",
            "https://tenor.com/view/everglow-mia-pretty-photoshoot-kpop-gif-15789180",
            "https://tenor.com/view/ginkoro-gif-17994290",
            "https://tenor.com/view/mia-everglow-pretty-windy-kpop-gif-16262724",
            "https://tenor.com/view/everglow-kpop-pretty-beautiful-cute-gif-15571739",
            "https://tenor.com/view/mia-everglow-kpop-kpop-girl-group-kpop-singer-gif-15341399",
            "https://tenor.com/view/everglow-kpop-cute-pretty-beautiful-gif-15562411",
            "https://tenor.com/view/everglow-dance-cute-smile-mic-gif-15070516",
            "https://tenor.com/view/everglow-mia-smile-gif-18564778",
            "https://tenor.com/view/mia-everglow-gif-18670931",
            "https://i.pinimg.com/originals/f1/6f/c3/f16fc3829dd7d3d9df745dd154d53985.gif",
            "https://data.whicdn.com/images/334270987/original.gif",
            "https://i.pinimg.com/originals/b6/34/e1/b634e133d78338397fa1bbc15683c176.gif",
            "https://thumbs.gfycat.com/ContentSophisticatedIcelandicsheepdog-size_restricted.gif",
            "https://data.whicdn.com/images/334423726/original.gif",
            "https://i.pinimg.com/originals/51/4d/64/514d6412dac9ae99ee2038ab4b8adabc.gif",
            "https://media1.tenor.com/images/ec591ac4b90c1e8d0e85e92494499b61/tenor.gif?itemid=15789180",
            "https://media1.tenor.com/images/021efdee4b60591d8c34edbddf3804a2/tenor.gif?itemid=15975958",
            "https://thumbs.gfycat.com/PlaintiveCornyGrub-size_restricted.gif",
            "https://media1.tenor.com/images/d0637588528a111f417ee46c8fd43fbd/tenor.gif?itemid=19351269",
            "https://i1.wp.com/66.media.tumblr.com/2f80e3d288b8430175fd168f69ec3744/tumblr_pwwb4rtFsr1ysegfdo2_400.gif?w=817&ssl=1",
            "https://thumbs.gfycat.com/ImperturbableAmusingAdmiralbutterfly-size_restricted.gif",
            "https://i.pinimg.com/originals/78/5b/06/785b06125d90ad657a6277210b254356.gif",
            "https://64.media.tumblr.com/65f6ee73fd449bb1bd94c895c6d75852/tumblr_pxk0rb7XHG1ud83y5o4_250.gif",
            "https://64.media.tumblr.com/8acfa453a5c44c7f9b702d729b17e199/tumblr_pxk0rb7XHG1ud83y5o1_250.gif",
            "https://64.media.tumblr.com/2a4c18fda810e3685f669f8c1f1c8107/cfb284170e1e5f20-1a/s400x600/b0014c7059ce389f1422dca1097f722b569e44f3.gif",
            "https://64.media.tumblr.com/fe476f085781ecc3cce317304438919b/dcd85241d73f3b61-cd/s500x750/6dade2304c8ff2d75c3346bbadeaf9927e205b2b.gif",
            "https://data.whicdn.com/images/327894135/original.gif"]

        self.bot.yiren_gif = ["https://tenor.com/view/yireon-hearts-wishing-wish-produce48-gif-11924127",
            "https://tenor.com/view/love-you-more-wink-side-eye-flirt-smile-gif-16944406",
            "https://tenor.com/view/%E7%8E%8B%E6%80%A1%E4%BA%BAwang-yiren-cute-kpop-smile-gif-16236336",
            "https://tenor.com/view/wang-yiren-everglow-kpop-cute-sad-gif-16526333",
            "https://tenor.com/view/everglow-yiren-wang-yiren-maknae-rapper-gif-15970519",
            "https://tenor.com/view/wang-yiren-everglow-kpop-fierce-gif-15559282",
            "https://tenor.com/view/%E7%8E%8B%E6%80%A1%E4%BA%BAwang-yiren-cute-kpop-smile-gif-16236336",
            "https://tenor.com/view/kpop-chinese-wang-yiren-everglow-smile-gif-15558804",
            "https://tenor.com/view/everglow-yiren-wang-yiren-kpop-cute-gif-16554167",
            "https://tenor.com/view/wang-yiren-everglow-kpop-cute-pretty-gif-15559396",
            "https://tenor.com/view/%E7%8E%8B%E6%80%A1%E4%BA%BA-wang-yiren-cute-pretty-kpop-gif-16236334",
            "https://tenor.com/view/everglow-yiren-wang-yiren-maknae-rapper-gif-16264216",
            "https://tenor.com/view/everglow-kpop-cute-pretty-beautiful-gif-15972795",
            "https://tenor.com/view/everglow-yiren-wang-yiren-kpop-cute-gif-16554171",
            "https://tenor.com/view/everglow-yiren-wang-yiren-maknae-rapper-gif-15907156",
            "https://tenor.com/view/everglow-gif-16227422",
            "https://tenor.com/view/everglow-cute-pretty-kpop-gif-15916228",
            "https://tenor.com/view/yiren-everglow-la-di-da-kpop-stone-music-gif-18570277",
            "https://i.pinimg.com/originals/24/10/9f/24109f9fe75952a3bb9d2f0fd4d41aad.gif",
            "https://i.pinimg.com/originals/e1/a4/cd/e1a4cdf99838c26606098b29190515bc.gif",
            "https://64.media.tumblr.com/133640a79bebe080e05b338bb37f4ffa/tumblr_puhq9yY9St1y7u46jo1_400.gif",
            "https://i.pinimg.com/originals/63/4e/38/634e38f65be867048f979d875a14db37.gif",
            "https://66.media.tumblr.com/ed94cc9b741a46453a23f7a4af881081/e9a342724868a080-ba/s400x600/e32a1bd680c02325174d1f838ce223dba77acb7f.gif",
            "https://2.bp.blogspot.com/-D1TMN_qy0g0/XJDKEHyP8nI/AAAAAAAArBw/GDQvYQiHueQmlQWai_5rZRb46yFu1BhNQCLcBGAs/s1600/GGULBEST_3.gif",
            "https://data.whicdn.com/images/328330998/original.gif",
            "https://i.pinimg.com/originals/5a/46/ea/5a46eaeb02651fd7e0845f6bebc8dc3b.gif",
            "https://i.pinimg.com/originals/58/1b/0e/581b0efcf8e03ff20ae5a1da8d7dd99a.gif",
            "https://data.whicdn.com/images/328438061/original.gif",
            "https://i.pinimg.com/originals/3f/be/57/3fbe57ded4f6fce5ab767e6d4453a6b3.gif",
            "https://data.whicdn.com/images/337982215/original.gif",
            "https://i.pinimg.com/originals/3e/d3/22/3ed3225fe1a08fa8e0f5c17d0dbc563e.gif",
            "https://thumbs.gfycat.com/AggressiveClearFurseal-small.gif",
            "https://64.media.tumblr.com/ce5dac98a67f8dd2aee1139802c37597/b970932cd7a6ece6-41/s400x600/2551268ca24140da59660d3337a7df9f433a3e11.gif",
            "https://64.media.tumblr.com/fc06ceb76e6151b5c21df51433d0ec03/b970932cd7a6ece6-63/s400x600/41968fadc476cf4d9adb5e1dc0ec4c173be5685c.gif",
            "https://64.media.tumblr.com/15df0abec6cc94e74c9c812388499be4/b970932cd7a6ece6-7b/s400x600/e1043e44fdc9dbe0889e35443020ec8f9cf91cf8.gif",
            "https://64.media.tumblr.com/bcbcf3baf07bc118ffddc6cd1f9ca9fc/b970932cd7a6ece6-3c/s400x600/2c16af59af7b89f01066c301318dd4953939f993.gif",
            "https://64.media.tumblr.com/155feaf1fd02d2d8ca4941c15257e837/414e84a471956061-86/s540x810/6c40127040ffe59345f4f2609feaa86a94eb7fa8.gif",
            "https://64.media.tumblr.com/d75f6010f8e18f2d81ae9e71e51877ab/6e174d2842779d1e-22/s500x750/172521706dfe50802d1782068d7beb18182d798f.gif",
            "https://i1.wp.com/66.media.tumblr.com/5e1f511a48c45960fbfec9443c5db094/tumblr_pokrzjB06D1xu9y0io1_400.gif?w=817&ssl=1",
            "https://thumbs.gfycat.com/SardonicDangerousIslandwhistler-size_restricted.gif",
            "https://64.media.tumblr.com/62a42f6b38f8191b2de2334d0063d4f6/tumblr_pokhc7r9U71was9wjo7_540.gif",
            "https://i1.wp.com/66.media.tumblr.com/c1421fb20f45818d60f00d86337ac403/tumblr_pqckg2Sf451y48sr6o3_250.gif?w=817&ssl=1",
            "https://media1.tenor.com/images/5f3572ccc6c821798a5ce4d34a0dee78/tenor.gif?itemid=15907156",
            "https://64.media.tumblr.com/55415f65d60630541f9a552e94a436b1/85525da4f1f1752e-3e/s400x600/673c619536314c5d9c0a511cb4d7460bdab44b75.gif"]

        self.bot.aisha_gif = ["https://tenor.com/view/everglow-aisha-heo-yoorim-lead-rapper-kpop-gif-16271018",
            "https://tenor.com/view/everglow-aisha-heo-yoorim-lead-rapper-kpop-gif-16264245",
            "https://tenor.com/view/aisha-everglow-gif-18934290",
            "https://tenor.com/view/everglow-aisha-heo-yoorim-lead-rapper-kpop-gif-16220721",
            "https://tenor.com/view/everglow-aisha-heo-yoorim-lead-rapper-kpop-gif-15907107",
            "https://tenor.com/view/everglow-aisha-heo-yoorim-lead-rapper-kpop-gif-15970488",
            "https://tenor.com/view/everglow-dance-kpop-wink-gif-15789124",
            "https://tenor.com/view/everglow-everglow-la-di-da-yiren-aisha-shiyeon-gif-19326454",
            "https://tenor.com/view/everglow-aisha-heo-yoorim-lead-rapper-kpop-gif-16271021",
            "https://tenor.com/view/everglow-aisha-heo-yoorim-lead-rapper-kpop-gif-16259147",
            "https://tenor.com/view/everglow-aisha-heo-yoorim-lead-rapper-kpop-gif-16271022",
            "https://gfycat.com/adorableaccurateamericanshorthair-mechabear-everglow-aisha-kpop",
            "https://gfycat.com/affectionatepresentagouti",
            "https://gfycat.com/thirdcolorlessbasil-everglow-aisha-essa-sosu",
            "https://gfycat.com/bestbluejapanesebeetle",
            "https://gfycat.com/deafeningcomplicatedkarakul-everglow-aisha-beauty",
            "https://gfycat.com/caringcalmcottontail-everglow-aisha",
            "https://gfycat.com/indelibleserpentinegoldfish-everglow",
            "https://gfycat.com/perkywelloffeel-everglow-secret48-aisha",
            "https://gfycat.com/comfortablehalfcaudata-beauty",
            "https://gfycat.com/acidicunknownblacklab-beauty",
            "https://gfycat.com/bewitchedunhealthyblacknorwegianelkhound",
            "https://gfycat.com/bitesizedcrazycarp-mechabear-everglow-kpop",
            "https://gfycat.com/blaringonlyimperatorangel-mechabear-everglow-aisha-kpop",
            "https://gfycat.com/adorablegiddyalaskanhusky",
            "https://gfycat.com/capitalearnestchrysalis-mechabear-everglow-kpop",
            "https://gfycat.com/cavernousmerrykestrel-beautiful-everglow-pretty-beauty-kpop-cute",
            "https://gfycat.com/dentalcharmingchrysomelid",
            "https://gfycat.com/bruisedinconsequentialfoal-beauty",
            "https://gfycat.com/caringfrighteningenglishpointer-mechabear-everglow-kpop",
            "https://gfycat.com/chillyillheterodontosaurus-mechabear-everglow-kpop",
            "https://gfycat.com/chillyillheterodontosaurus-mechabear-everglow-kpop",
            "https://gfycat.com/assurednicecaiman-everglow",
            "https://gfycat.com/coordinatedrigidibizanhound-beauty",
            "https://gfycat.com/consciousverifiableamericancrayfish-everglow-beauty-dance-adios-giant-kpop-tall",
            "https://gfycat.com/daringrealisticgalago-mechabear-everglow-kpop",
            "https://gfycat.com/completethoroughhairstreakbutterfly",
            "https://gfycat.com/whimsicalunfoldedcero-beauty",
            "https://gfycat.com/deadhonorablechanticleer-beauty",
            "https://gfycat.com/deliciousperiodicleafbird",
            "https://gfycat.com/distantjaggedbillygoat-everglow-kpop",
            "https://gfycat.com/eminentwaterydiamondbackrattlesnake-mechabear-everglow-kpop",
            "https://gfycat.com/downrighttintedhorseshoebat-mechabear-everglow-kpop-cute",
            "https://gfycat.com/flashygraciousleopardseal-mechabear-everglow-kpop",
            "https://gfycat.com/faroffmellowhippopotamus",
            "https://gfycat.com/idioticdetailedbarnswallow-mechabear-everglow-aisha-kpop",
            "https://gfycat.com/linedthickkiskadee-mechabear-everglow-kpop",
            "https://gfycat.com/mealyfatalimperialeagle-mechabear-everglow-kpop",
            "https://gfycat.com/melodicelegantcricket",
            "https://gfycat.com/poshspryhalcyon-mechabear-everglow-aisha-kpop",
            "https://gfycat.com/readynegligibleicelandichorse-mechabear-everglow-aisha-kpop",
            "https://gfycat.com/speedychillyfattaileddunnart-everglow-ebeogeulrou-girlgroup-aisha-kpop",
            "https://gfycat.com/reliableidealisticjackal",
            "https://gfycat.com/secondaryantiqueadamsstaghornedbeetle",
            "https://gfycat.com/victoriousradiantdugong-mechabear-everglow-cottiny-kpop",
            "https://gfycat.com/caringcalmcottontail-everglow-aisha",
            "https://gfycat.com/whimsicalsaltydalmatian-beauty",
            "https://gfycat.com/fearfulopulentkinglet-mechabear-everglow-aisha-kpop",
            "https://gfycat.com/repentantgrizzledalligatorgar-everglow-beauty-orange-aisha-dance-giant-kpop-asia",
            "https://gfycat.com/ordinarywholejumpingbean",
            "https://gfycat.com/diligentspiffyhen-mechabear-everglow-kpop",
            "https://gfycat.com/homelyraggedkissingbug-everglow",
            "https://gfycat.com/dependentfakedrafthorse-everglow",
            "https://gfycat.com/adorableaccurateamericanshorthair-mechabear-everglow-aisha-kpop",
            "https://gfycat.com/elementaryamusedgossamerwingedbutterfly",
            "https://gfycat.com/heftywanbarb",
            "https://gfycat.com/unluckykeengraysquirrel-everglow-aisha",
            "https://gfycat.com/antiqueshortivorybilledwoodpecker",
            "https://gfycat.com/lonetintedharrier-beauty",
            "https://gfycat.com/jovialmaleindianrockpython",
            "https://gfycat.com/disguisedfelineindochinahogdeer-everglow-aisha-kpop",
            "https://gfycat.com/massivebelateddairycow",
            "https://gfycat.com/nextcoldchrysalis",
            "https://gfycat.com/openaromaticbobcat",
            "https://gfycat.com/loathsomelinedafricanporcupine-everglow-aisha",
            "https://gfycat.com/serenefluffycapybara",
            "https://gfycat.com/sparklingsneakyanchovy",
            "https://gfycat.com/impishpresentcapeghostfrog-everglow-dun-dun-everglow-aisha-kuro-gurokami",
            "https://gfycat.com/sillysoftgrouper-beauty",
            "https://gfycat.com/uniquemiserablegoldenretriever-mechabear-everglow-aisha-kpop",
            "https://gfycat.com/idealisticrespectfulalligator-everglow",
            "https://gfycat.com/blackclearatlanticblackgoby-everglow-lalalay-aisha-ebeogeulrou",
            "https://gfycat.com/angryhighlevelibadanmalimbe-k-culture-korean-music-mv-music-video-k-pop-kpop-myubi-myujigbidio",
            "https://gfycat.com/selfreliantdopeyduck-k-culture-korean-music-mv-music-video-k-pop-kpop-myubi-myujigbidio",
            "https://gfycat.com/detailedquerulouskakapo-mechabear-everglow-aisha-kpop",
            "https://gfycat.com/feistyallcrow-mechabear-everglow-aisha-kpop",
            "https://gfycat.com/compassionatejollyguillemot-mechabear-everglow-aisha-kpop",
            "https://gfycat.com/consideratefickleamericanlobster-mechabear-everglow-aisha-kpop",
            "https://gfycat.com/temptingshygoral",
            "https://gfycat.com/revolvingtintedamurstarfish",
            "https://gfycat.com/vigorousmilkybasenji-everglow-aisha-kpop",
            "https://gfycat.com/unfortunatequickamericanpainthorse-aisha",
            "https://gfycat.com/alarminghalfafricanporcupine",
            "https://gfycat.com/shimmeringagileanchovy-everglow-aisha",
            "https://gfycat.com/mellowdisguisedfruitfly-beauty",
            "https://gfycat.com/thirstyanchoredjerboa-everglow-aisha-kpop",
            "https://gfycat.com/unlinedthirstyfallowdeer-everglow-aisha-kpop",
            "https://gfycat.com/scaryaccomplishedharborseal-afterschoolclub-simplykpop-arirangtv",
            "https://gfycat.com/bronzedeafeningamericangoldfinch-everglow-aisha-kpop",
            "https://gfycat.com/wavyachinggnatcatcher",
            "https://gfycat.com/decimalpiercingdobermanpinscher",
            "https://gfycat.com/beautifulcluelessirishsetter-girlgroup-everglow-aisha-kpop",
            "https://gfycat.com/educatedwaterychimneyswift-everglow-aisha-kpop",
            "https://gfycat.com/electricplayfulamericanwirehair",
            "https://gfycat.com/forthrightmenacinghen",
            "https://gfycat.com/fortunatealarmingiaerismetalmark-mechabear-everglow-kpop",
            "https://gfycat.com/impressiveembarrassedhoverfly",
            "https://gfycat.com/vacantvaguebasil-everglow-aisha",
            "https://gfycat.com/gloomycheeryastarte",
            "https://gfycat.com/detailedvictoriousiraniangroundjay-beauty",
            "https://gfycat.com/limpimaginativebluegill",
            "https://gfycat.com/gargantuanshimmeringchimpanzee-mechabear-everglow-kpop",
            "https://gfycat.com/lastvacantbrocketdeer",
            "https://gfycat.com/medicalblushingagama",
            "https://gfycat.com/filthycandidduckbillcat-everglow-aisha-kpop",
            "https://gfycat.com/heartydecimaldegu-beauty",
            "https://gfycat.com/groundedfailinggeese-everglow-aisha-kpop-onda",
            "https://gfycat.com/linedthickkiskadee-mechabear-everglow-kpop",
            "https://gfycat.com/limiteddampbullmastiff-mechabear-everglow-aisha-kpop",
            "https://gfycat.com/meanlightgermanwirehairedpointer-mechabear-everglow-kpop",
            "https://gfycat.com/serenenegativedutchsmoushond-beauty",
            "https://gfycat.com/needyexcitableblackrhino",
            "https://gfycat.com/radianthonestimperialeagle-beauty",
            "https://gfycat.com/piercingcookedkitty",
            "https://gfycat.com/scareddecisiveghostshrimp-everglow-aisha",
            "https://gfycat.com/secondhandsingleadeliepenguin",
            "https://gfycat.com/welloffchillyjackrabbit-beauty",
            "https://gfycat.com/faruniquefairyfly",
            "https://gfycat.com/playfulmelodicavians",
            "https://gfycat.com/disfiguredequatorialkitfox-everglow-aihsa",
            "https://gfycat.com/bluecornyheterodontosaurus-yuki-kashiwagi",
            "https://gfycat.com/concernedmeandrongo-everglow-aisha",
            "https://gfycat.com/goldenvictoriousindianskimmer",
            "https://gfycat.com/lastingkeydoctorfish-everglow-aisha-kpop",
            "https://gfycat.com/chillymammothfritillarybutterfly-mechabear-everglow-aisha-kpop",
            "https://gfycat.com/obviousenviousisabellinewheatear",
            "https://gfycat.com/aridcomposedbellsnake-idol-league-svsrglow-everglow-la-di-da-aisha-kpop",
            "https://gfycat.com/weeklybreakableboto",
            "https://gfycat.com/gaseousfelineblacknorwegianelkhound-everglow-fansign-fancam-aisha-bongbongsyokolra",
            "https://gfycat.com/closeprestigiousguineafowl",
            "https://gfycat.com/infatuatedchillydunnart",
            "https://gfycat.com/teemingpessimisticarrowworm-everglow-aisha-kpop",
            "https://data.whicdn.com/images/327889658/original.gif"]

        self.bot.onda_gif = ["https://tenor.com/view/everglow-onda-jo-serim-vocalist-kpop-gif-15970349",
            "https://tenor.com/view/everglow-onda-jo-serim-vocalist-kpop-gif-16263345",
            "https://tenor.com/view/everglow-cute-pretty-kpop-smile-gif-15818709",
            "https://tenor.com/view/everglow-onda-jo-serim-vocalist-kpop-gif-16481547",
            "https://tenor.com/view/everglow-onda-gif-18337504",
            "https://tenor.com/view/everglow-finger-gun-cute-wink-kpop-gif-15970368",
            "https://tenor.com/view/everglow-onda-jo-serim-vocalist-kpop-gif-16194399",
            "https://tenor.com/view/onda-everglow-gif-18337507",
            "https://tenor.com/view/everglow-onda-gif-18337506",
            "https://tenor.com/view/everglow-onda-onda-everglow-gif-19501054",
            "https://gfycat.com/amusedspryicterinewarbler-girlgroup-everglow-kpop-onda",
            "https://gfycat.com/bigheartedregalbluejay-everglow-essa-onda-sosu",
            "https://gfycat.com/arctichandmadeasiantrumpetfish-everglow-onda",
            "https://gfycat.com/blindgraveinchworm-k-culture-korean-music-mv-music-video-k-pop-kpop-myubi-myujigbidio",
            "https://gfycat.com/briefdirectalbacoretuna",
            "https://gfycat.com/fardeepgrayling-everglow-onda",
            "https://gfycat.com/orneryfabulousastrangiacoral",
            "https://gfycat.com/thickacademicflyinglemur-everglow",
            "https://gfycat.com/appropriatedearestdowitcher-everglow-onda-kuro-gurokami-jo-serim-kpop-idol",
            "https://gfycat.com/ablewetamericanquarterhorse-everglow-onda-kuro-gurokami-jo-serim-kpop-idol",
            "https://gfycat.com/belatedevergreenirukandjijellyfish",
            "https://gfycat.com/chillywarmduckbillplatypus",
            "https://gfycat.com/definitewickedcollie",
            "https://gfycat.com/frayedidenticalleveret",
            "https://thumbs.gfycat.com/FirmEmotionalBangeltiger-size_restricted.gif",
            "https://thumbs.gfycat.com/JollyDetailedBuffalo-size_restricted.gif",
            "https://i.pinimg.com/originals/3a/09/98/3a0998b31224c921f44460ea7ac452b0.gif",
            "https://media1.tenor.com/images/3117066bc006d142b6f3b6c0cad5c48d/tenor.gif?itemid=16481573",
            "https://data.whicdn.com/images/334557397/original.gif",
            "https://d.wattpad.com/story_parts/781040295/images/15fce16d3016ea69918258632648.gif",
            "https://66.media.tumblr.com/0c17e1710b7117f5c10347de3a1276b7/tumblr_pwo0y45B5J1yoiwkxo6_250.gif",
            "https://thumbs.gfycat.com/FreePlaintiveIndiancow-size_restricted.gif",
            "https://cdn140.picsart.com/327499246039201.gif",
            "https://i.pinimg.com/originals/3d/d0/b7/3dd0b7848292e40ada873b869cb16495.gif",
            "https://data.whicdn.com/images/327890348/original.gif"]

        self.bot.sihyeon_gif = ["https://tenor.com/view/everglow-sihyeon-kim-sihyeon-face-of-the-group-rapper-gif-16281910",
            "https://tenor.com/view/everglow-sihyeon-kim-sihyeon-face-of-the-group-rapper-gif-16481660",
            "https://tenor.com/view/everglow-kim-sihyeon-sihyeon-playing-with-hair-kpop-gif-15818759",
            "https://tenor.com/view/everglow-sihyeon-kim-sihyeon-face-of-the-group-rapper-gif-15907131",
            "https://tenor.com/view/everglow-sihyeon-kim-sihyeon-face-of-the-group-rapper-gif-16281918",
            "https://tenor.com/view/everglow-sihyeon-kim-sihyeon-face-of-the-group-rapper-gif-15970364",
            "https://tenor.com/view/everglow-kim-sihyeon-sihyeon-kpop-pretty-gif-15818626",
            "https://tenor.com/view/everglow-cute-pretty-sihyeon-kpop-gif-15600838",
            "https://tenor.com/view/everglow-sihyeon-kim-sihyeon-face-of-the-group-rapper-gif-16281904",
            "https://tenor.com/view/everglow-sihyeon-kim-sihyeon-face-of-the-group-rapper-gif-16221390",
            "https://tenor.com/view/everglow-sihyeon-kim-sihyeon-face-of-the-group-rapper-gif-16220701",
            "https://data.whicdn.com/images/327894169/original.gif",
            "https://media1.tenor.com/images/f52c8fb073467c30e4af5f99dca62550/tenor.gif?itemid=14397714",
            "https://3.bp.blogspot.com/-Pwj4l0iaOOs/XLkn59NmO9I/AAAAAAAAt7c/g9S_chYb22MXZmdzvy4jvOzCcudYQ4uagCLcBGAs/s1600/ggulbest_42-55.gif",
            "https://64.media.tumblr.com/49f9b61500910cbe63783c690c692ea8/tumblr_povyd6RQ2c1y7u46jo2_250.gif",
            "https://thumbs.gfycat.com/AbsoluteAchingBronco-max-1mb.gif",
            "https://thumbs.gfycat.com/ClassicForkedBuck-size_restricted.gif",
            "https://data.whicdn.com/images/328119815/original.gif",
            "https://i.pinimg.com/originals/9b/2a/13/9b2a1302f606a5462303835570eba3cc.gif",
            "https://i.pinimg.com/originals/87/92/f7/8792f759688f09976bd0f960f0c66a56.gif",
            "https://64.media.tumblr.com/6166079e2c580273e45d4085fe98e692/e63e3caed8ddace3-92/s400x600/641ef2bdb81be95dd948cc06596c1984282ed690.gif",
            "https://i.pinimg.com/originals/92/17/32/9217329cf0102f05b3358eb134bd3521.gif",
            "https://64.media.tumblr.com/24da1c98bcd91ae8cc1b59fb1f8820f7/af28a343421fda8d-61/s400x600/73165a9eb25eb9ee88d82500394e5de5ac4a8dbb.gif",
            "https://data.whicdn.com/images/340103695/original.gif",
            "https://thumbs.gfycat.com/CalculatingGrayAuklet-max-1mb.gif",
            "https://i.pinimg.com/originals/f1/8f/ce/f18fce22dcae94f7067064beedcac38c.gif",
            "https://media1.tenor.com/images/ae640f30dfe35e3ca5bb750e4119833d/tenor.gif?itemid=18818089",
            "https://64.media.tumblr.com/32aec67f6667e7947939a88d1e403582/95b88aeae5a3b2ac-ae/s640x960/d1b4498daf69acd16bd248e5d85ec57da27d175a.gif",
            "https://pa1.narvii.com/7642/1eb53c160d77d07ce214a3714bd884a2e81ca94cr1-381-498_hq.gif",
            "https://media1.tenor.com/images/1ce6222ab99171102d1c80ea12eb24ea/tenor.gif?itemid=16227320",
            "https://64.media.tumblr.com/6294b76403c665fb2ea26c6743c7a38a/tumblr_pzkxlklMKd1y80u3fo1_250.gif",
            "https://thumbs.gfycat.com/AbsoluteAchingBronco-max-1mb.gif",
            "https://i.pinimg.com/originals/b5/91/1d/b5911d185e4e60eca87a5f8470cccda1.gif",
            "https://thumbs.gfycat.com/FluidBlackIrishwolfhound-max-1mb.gif",
            "https://media1.tenor.com/images/d3f0fff90eb1ed8a8d0e4cc4a33e6f1e/tenor.gif?itemid=16281917",
            "https://thumbs.gfycat.com/TartBabyishHorse-max-1mb.gif",
            "https://i.pinimg.com/originals/27/01/87/2701875b81d057365886d114f64c5eeb.gif",
            "https://thumbs.gfycat.com/AgileVerifiableBeaver-size_restricted.gif",
            "https://64.media.tumblr.com/1819ba1ced1d4f9b236106401e20409c/tumblr_pq6oug8iwh1ui9xsvo2_250.gif",
            "https://1.bp.blogspot.com/-JUA9q671nm8/Xn0TiuSah9I/AAAAAAAANCU/2IWgPgKjvCs88FUE2eTdlubehsD1zUnOACLcBGAsYHQ/s1600/tumblr_dac21be8d01703f645d43558cdc11528_15ba696c_540.gif"]

    @commands.command()
    async def everglow(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Everglow {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "eu" or arg == "e:u":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about E:U :heart: ')
                await ctx.send(random.choice(self.bot.eu_gif))
                await ctx.message.delete()
        elif arg =="mia":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Mia :heart: ')
                await ctx.send(random.choice(self.bot.mia_gif))
                await ctx.message.delete()
        elif arg == "yiren":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{weakado}>, <@!{ctx.author.id}> is talking about Yiren :orange_heart:')
                    await ctx.send(random.choice(self.bot.yiren_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yiren :orange_heart:')
                await ctx.send(random.choice(self.bot.yiren_gif))
                await ctx.message.delete()
        elif arg == "aisha":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Aisha :heart: ')
                await ctx.send(random.choice(self.bot.aisha_gif))
                await ctx.message.delete()
        elif arg == "onda":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Onda :heart: ')
                await ctx.send(random.choice(self.bot.onda_gif))
                await ctx.message.delete()
        elif arg == "sihyeon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Sihyeon :heart: ')
                await ctx.send(random.choice(self.bot.sihyeon_gif))
                await ctx.message.delete()

   

def setup(client):
    client.add_cog(everglow(client))