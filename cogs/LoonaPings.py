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
mae = 492769416610840586
aeong = 542342961392779264
k8 = 573974040679809044
stanley = 727312020717830264
rith = 346724857725059075
ple = 416903886968979466
masa = 725138411823956079
manman = 320520067265724416


class LoonaPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.heejin_gif = ["https://tenor.com/view/%EC%9D%B4%EB%8B%AC%EC%9D%98%EC%86%8C%EB%85%80-%ED%9D%AC%EC%A7%84-loona-heejin-dancing-gif-15500748",
            "https://tenor.com/view/heejin-waving-hi-hello-smile-gif-16980677",
            "https://tenor.com/view/heejin-loona-gif-18855977",
            "https://tenor.com/view/heejin-loona-gif-18630598",
            "https://tenor.com/view/heejin-loona-gif-18892027",
            "https://tenor.com/view/loona-hee-jin-hello-smile-gif-14824756",
            "https://tenor.com/view/loona-heejin-cute-gif-8365491",
            "https://tenor.com/view/heejin-loona-nodding-sad-nodding-yeah-gif-16288849",
            "https://tenor.com/view/heejin-loona-gif-18855987",
            "https://tenor.com/view/heejin-loona-gif-18855973",
            "https://data.whicdn.com/images/301501979/original.gif",
            "https://gfycat.com/fatalneedydugong-heejin-loona",
            "https://gfycat.com/bonyickyemeraldtreeskink-heejin-loona",
            "https://gfycat.com/cloudyimpureeuropeanfiresalamander-heejin-loona",
            "https://gfycat.com/cluelessfixedbuckeyebutterfly",
            "https://gfycat.com/concernedmixedarieltoucan",
            "https://gfycat.com/defensiveessentialafricanwilddog-loona-heejin-jeon-heejin-kuro-gurokami-kpop-idol",
            "https://gfycat.com/amazingpreciousbarracuda-beauty",
            "https://gfycat.com/blackandwhitepiercinglemur-heejin-loona",
            "https://gfycat.com/carelessyawningacouchi-heejin-loona",
            "https://gfycat.com/cloudypeacefuldowitcher-heejin-loona-dogs",
            "https://gfycat.com/concretefarawayfattaileddunnart-loona-so-what-loona-heejin-jeon-heejin-kpop-idol",
            "https://gfycat.com/dirtyequatorialfrog",
            "https://gfycat.com/soggyaccomplishedcolt-heejin-loona"]

        self.bot.hyunjin_gif = ["https://cdn.discordapp.com/attachments/771238115255255060/771239029291221022/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239029982101534/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239030301786132/image2.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239030984933376/image3.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239031534649344/image4.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239032360271872/image5.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239033023496202/image6.gif",
            "https://tenor.com/view/hyunjin-hyunjin-cute-loona-hyunjin-loona-kpop-girl-gif-15567551",
            "https://cdn.discordapp.com/attachments/771238115255255060/771478311045955584/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771478314715447316/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771478316427378748/image2.gif",
            "https://tenor.com/view/k-im-hyunjin-loona-got-you-cute-pretty-gif-16467662",
            "https://tenor.com/view/loona-loona-hyunjin-hyunjin-kim-hyunjin-loona-aeong-gif-18902504",
            "https://cdn.discordapp.com/attachments/771238115255255060/777819042685779978/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/777819043649683476/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/777819045034065920/image2.gif",
            "https://tenor.com/view/breadjin-aeong-hyunjin-loona-bread-swap-gif-15633189",
            "https://gfycat.com/actualwarmheartedharpseal-hyunjin-loona-kpop",
            "https://gfycat.com/admirablezealousbighorn",
            "https://gfycat.com/agedcloseamurratsnake-beauty",
            "https://gfycat.com/agilefamiliariberianmidwifetoad",
            "https://gfycat.com/allblandabyssiniancat-beauty",
            "https://gfycat.com/calmbreakableafghanhound-hyunjin-loona",
            "https://gfycat.com/desertedperfectbelugawhale-hyunjin-loona-kpop",
            "https://gfycat.com/cleananchoredgnatcatcher-hyunjin-loona"]

        self.bot.haseul_gif = ["https://tenor.com/view/wiggle-kpop-haseul-ha-seul-gif-19167036",
            "https://tenor.com/view/ha-seul-highway-to-heaven-loona-cute-smile-gif-14669447",
            "https://tenor.com/view/haseul-loona-butterfly-dancing-kpop-gif-15567623",
            "https://tenor.com/view/let-me-in-haseul-loona-jo-haseul-music-video-gif-16481945",
            "https://tenor.com/view/hug-loona-kpop-love-haseul-gif-18585614",
            "https://tenor.com/view/ha-seul-laugh-loona-cute-gif-14669547",
            "https://tenor.com/view/loona-haseul-kpop-korean-you-gif-13811504",
            "https://tenor.com/view/haseul-loona-haseul-cute-haseul-kiss-blow-kiss-gif-15567594",
            "https://tenor.com/view/haseul-haseul-nope-yoghurt-loona-haseul-loona-gif-19296137",
            "https://tenor.com/view/loona-haseul-yes-nod-gif-15405788",
            "https://tenor.com/view/loona-haseul-kpop-gif-13775182",
            "https://gfycat.com/plasticequatorialeider",
            "https://tenor.com/view/haseul-loona-gif-11903461",
            "https://tenor.com/view/haseul-haseul-my-beloved-my-beloved-heart-loona-gif-19628816"]

        self.bot.vivi_gif = ["https://tenor.com/view/vivi-loona-gif-19076955",
            "https://tenor.com/view/vivi-loona-gif-19186243",
            "https://tenor.com/view/loona-vivi-cute-wong-kaahei-kpop-gif-17900498",
            "https://tenor.com/view/loona-vivi-gif-18868377",
            "https://tenor.com/view/loona-vivi-wong-gaahei-vocalist-rapper-gif-17025562",
            "https://tenor.com/view/loona-vivi-wong-gaahei-vocalist-rapper-gif-17025571",
            "https://tenor.com/view/vivi-loona-sad-gif-15189378",
            "https://tenor.com/view/loona-vivi-wong-gaahei-vocalist-rapper-gif-17025543",
            "https://tenor.com/view/vivi-loona-so-what-kpop-fierce-gif-16237781",
            "https://tenor.com/view/vivi-loona-disgust-gif-15189377",
            "https://tenor.com/view/kpop-loona-vivi-gif-18586099",
            "https://tenor.com/view/kpop-loona-vivi-shoulder-wiggle-gif-18586104",
            "https://media.discordapp.net/attachments/743512478411128834/778910394126565376/vivi_peekaboo.gif",
            "https://gfycat.com/amusedplaintiveherring-blockberrycreative-everday-i-need-you",
            "https://gfycat.com/jauntyglamorousbluetickcoonhound-iniseupeuri-innisfree-bibideukeurimitinteu-meikeueob-jepum",
            "https://gfycat.com/ashamedlonelyhammerkop-form-of-therapy-my-music-taste-deep-dive-loona",
            "https://gfycat.com/baggyshinyarizonaalligatorlizard-loona-1-3-korean-vivi-kpop",
            "https://gfycat.com/cheapplainhamster",
            "https://gfycat.com/esteemedflawlessaldabratortoise-loona-vivi",
            "https://gfycat.com/jitterysimplisticblacklab-loona-vivi",
            "https://gfycat.com/carefulglumcony-loona-kpop-vivi",
            "https://gfycat.com/hauntingslimblackwidowspider-loona-vivi",
            "https://gfycat.com/healthymajoraustraliankestrel-loona-vivi",
            "https://gfycat.com/liquidtotalbergerpicard-loona-kpop-vivi",
            "https://gfycat.com/lamehastyfattaileddunnart-blockberry-creative-weekly-poem-loona-vivi-kpop",
            "https://gfycat.com/naughtydopeylangur-visucal-cam-christmas-special-loona-idalyisonyeo",
            "https://gfycat.com/alienatedfatjoey-visucal-cam-christmas-special-loona-idalyisonyeo"]

        self.bot.yeojin_gif = ["https://tenor.com/view/yeojin-loona-star-gif-19239212",
            "https://tenor.com/view/glasses-loona-yeojin-cute-gif-14375086",
            "https://tenor.com/view/yeojin-loona-im-yeojin-gun-aim-gif-16706146",
            "https://tenor.com/view/kiss-later-loona-yeojin-im-yeojin-maknae-gif-17090973",
            "https://tenor.com/view/yeojin-loona-yeojin-loona-gif-18910341",
            "https://tenor.com/view/yeojin-loona-yeojin-loona-gif-18972277",
            "https://tenor.com/view/yeojin-loona-yeojin-loona-finger-guns-gif-19210631",
            "https://tenor.com/view/yeojin-loona-gif-11903465",
            "https://tenor.com/view/loona-yeojin-im-yeojin-maknae-vocalist-gif-16635624",
            "https://tenor.com/view/yeojin-cute-loona-frog-finger-guns-gif-14374690",
            "https://tenor.com/view/yeojin-wiggle-kpop-loona-dance-gif-17207445",
            "https://tenor.com/view/loona-dancing-yeojin-kpop-gif-18890861",
            "https://tenor.com/view/yeojin-loona-cute-yes-surprised-gif-14381686",
            "https://tenor.com/view/loona-dancing-yeojin-kpop-gif-18890861",
            "https://gfycat.com/beneficialevenanglerfish-yeojin-loona",
            "https://gfycat.com/disastrousserenebluebird-yeojin-loona",
            "https://gfycat.com/nicepotableanhinga-yeojin-loona",
            "https://gfycat.com/concernedearnestbushsqueaker-yeojin-loona",
            "https://gfycat.com/closefreshbantamrooster-yeojin-loona",
            "https://gfycat.com/handsomeoffensivedartfrog-yeojin-loona-asian-girl-kpop",
            "https://gfycat.com/admiredharshgrebe-yeojin-loona",
            "https://gfycat.com/poisedvengefulhousefly",
            "https://gfycat.com/exhaustedjollyfieldspaniel",
            "https://gfycat.com/hatefulblackantlion-yeojin-loona",
            "https://gfycat.com/blackshockingazurevasesponge-yeojin-loona",
            "https://gfycat.com/definitivegaseousbangeltiger-yeojin-loona",
            "https://gfycat.com/elegantneglectedkagu-yeojin-loona",
            "https://gfycat.com/honoredcluelessleveret-yeojin-loona",
            "https://gfycat.com/faintcookedgreatwhiteshark-yeojin-loona",
            "https://gfycat.com/ecstaticspotlessbufflehead-yeojin-loona",
            "https://gfycat.com/fairlikableappaloosa-yeojin-loona-gowon",
            "https://gfycat.com/marvelouspoorazurevasesponge-loona-yeojin-kuro-gurokami-im-yeojin-kpop-idol",
            "https://gfycat.com/breakableequatorialcod-loona-yves-chuu",
            "https://gfycat.com/hollowunequaledconey-loona-tv-yeojin-loopd-kpop",
            "https://gfycat.com/giftednimblebordercollie-idalyisonyeo",
            "https://gfycat.com/shamefulgregarioushummingbird-yeojin-loona",
            "https://gfycat.com/harmlesspitifulhoneybadger-elope",
            "https://gfycat.com/leanaffectionatedevilfish-karaoke-singing-loona-kpop-noraebang"]

        self.bot.kimlip_gif = ["https://thumbs.gfycat.com/CaringAlertHellbender-max-1mb.gif",
            "https://64.media.tumblr.com/632b50fcf95204b79d978049034e2f9f/tumblr_pe89snEig71x29wuzo4_250.gif",
            "https://i.pinimg.com/originals/b8/22/88/b82288fdc234bd0a50be07ae1ec212ef.gif",
            "https://thumbs.gfycat.com/WeeSillyAngelfish-max-1mb.gif",
            "https://media1.tenor.com/images/8cdb11b9b4a58c517215531156cc1812/tenor.gif?itemid=13802828",
            "https://i2.wp.com/66.media.tumblr.com/935a3a56a302380eeb10be67640a880a/b3f428ad85343842-de/s400x600/b31d01f30df1a8ac781460c8460f697e87c2e57d.gif?w=817&ssl=1",
            "https://64.media.tumblr.com/496da05c77ed58eac63f37cdd4bc7e9b/abfaa74408006212-71/s400x600/df7abdfe16b17d71598cab49b1202362b5ca4e61.gif",
            "https://i.pinimg.com/originals/15/41/f8/1541f83313271d2e8eb76220cbf43f24.gif",
            "https://data.whicdn.com/images/290426395/original.gif",
            "https://64.media.tumblr.com/151136f17e11dd8f80fe626d7fe685e4/tumblr_pdue0gd2P81somnmfo2_400.gif",
            "https://i.pinimg.com/originals/b6/26/68/b62668ab9b50797aa7418e16074de809.gif",
            "https://64.media.tumblr.com/0072acb65c1a86773f842628f748faaa/tumblr_pul162PtSc1xpl3u9o1_r1_250.gif",
            "https://64.media.tumblr.com/40ad336b08f95aa5490afeedf10df5c6/tumblr_p92066rl3z1w5jkuno5_r1_500.gif",
            "https://tenor.com/view/loona-kim-lip-lippie-halloween-tree-gif-19177056",
            "https://tenor.com/view/loona-kim-lip-loona-kim-lip-kpop-cone-lip-gif-16808895",
            "https://gfycat.com/informalyearlyhydra-beauty",
            "https://gfycat.com/ablebothguernseycow",
            "https://gfycat.com/artisticwealthyflyinglemur",
            "https://gfycat.com/boringnextguineafowl",
            "https://gfycat.com/caringuglydanishswedishfarmdog",
            "https://gfycat.com/flusteredremarkablegnat-kim-lip",
            "https://gfycat.com/ripegreenkingsnake-loona-kim-lip-kuro-gurokami-kimlip-kpop-idol",
            "https://gfycat.com/unimportantsparklingafricanpiedkingfisher-kim-lip-loona-beauty",
            "https://gfycat.com/tintedwelltodokitten-kimlip-loona",
            "https://gfycat.com/compassionatespicybellfrog-kim-lip",
            "https://gfycat.com/calmimpolitecommabutterfly-performance-butterfly-kim-lip-loona",
            "https://gfycat.com/courageousopenfoxhound",
            "https://gfycat.com/distanthighlamb-variety-show-survivors-kim-lip-kbs-2tv-loona-pool",
            "https://gfycat.com/silkydownrightlhasaapso",
            "https://gfycat.com/excellentfailinggardensnake-loona-kim-lip-kuro-gurokami-kimlip-kpop-idol",
            "https://gfycat.com/allheavyborderterrier-kim-lip-loona-kpop-trkz",
            "https://gfycat.com/amusingrectangularibadanmalimbe-performance-comeback-so-what-idalyi-sonyeo-loona",
            "https://gfycat.com/deadlybossyiraniangroundjay-kim-lip-loona",
            "https://gfycat.com/deafeningharmfulindianrhinoceros-kim-lip-idalyi-sonyeo-loona",
            "https://gfycat.com/klutzywelltodogodwit-kim-lip-loona-kpop-trkz",
            "https://gfycat.com/lawfulthesekoala",
            "https://gfycat.com/menacingdistantdobermanpinscher",
            "https://gfycat.com/leadingnewkakarikis",
            "https://gfycat.com/bigimpeccablekangaroo-loona-kimlip-kevin",
            "https://gfycat.com/costlyfreecurlew-loona-kim-lip-kim-jungeun-girl-group"]

        self.bot.jinsoul_gif = ["https://tenor.com/view/jinsoul-loona-whynot-gif-18990936",
            "https://tenor.com/view/loona-whynot-jinsoul-gif-19093071",
            "https://tenor.com/view/jinsoul-loona-gif-11882928",
            "https://tenor.com/view/jinsoul-loona-gif-11882987",
            "https://tenor.com/view/jinsoul-loona-sad-gif-11882910",
            "https://tenor.com/view/loona-jinsoul-hello-waving-gif-14339470",
            "https://tenor.com/view/loona-jinsoul-kpop-peace-sign-cute-gif-15163631",
            "https://tenor.com/view/jinsoul-kpop-korean-cute-loona-gif-16438129",
            "https://tenor.com/view/jinsoul-loonatic-jinsoul-loona-gif-18816324",
            "https://tenor.com/view/jinsoul-loona-loona-jinsoul-singing-in-the-rain-singing-gif-11527427",
            "https://tenor.com/view/jin-soul-loona-cute-kpop-smile-gif-15164534",
            "https://tenor.com/view/jinsoul-gif-18689085",
            "https://tenor.com/view/jinsoulloona-gif-18870191",
            "https://tenor.com/view/jinsoul-gif-18689119",
            "https://gfycat.com/advancedelementarychicken-beauty",
            "https://gfycat.com/dopeyunawareguernseycow",
            "https://gfycat.com/distantbountifulfritillarybutterfly-beauty",
            "https://gfycat.com/carefulfickleivorybackedwoodswallow",
            "https://gfycat.com/miniatureassuredeft",
            "https://gfycat.com/demandingmemorableerne",
            "https://gfycat.com/adoredincompleteasiandamselfly",
            "https://gfycat.com/politicalannualflatfish-odd-eye-circle-jinsoul-korean-loona",
            "https://gfycat.com/abandonedhonesthoverfly",
            "https://gfycat.com/hugewealthyaurochs-loona-jinsoul-loona-so-what-jung-jinsoul-kpop",
            "https://gfycat.com/rewardingpointeddouglasfirbarkbeetle-jinsoul-idalyi-sonyeo-loona-kpop-jinsol-beauty"
            "https://gfycat.com/pleasedwebbedeasternnewt",
            "https://gfycat.com/helpfulwholedoctorfish-jinsoul-loona-chuu",
            "https://gfycat.com/officialsameicefish-loona-jinsoul-jung-jinsoul-kpop-idol-kuro",
            "https://gfycat.com/thatelegantdove-jinsoul-loona",
            "https://gfycat.com/immediategeneralbadger-jinsoul-loona",
            "https://gfycat.com/firmspitefuldikkops-people-blogs-sing-a-soul-jinsoul",
            "https://gfycat.com/gentledecentkinglet-jinsoul-loona",
            "https://gfycat.com/regularimmensejabiru-jinsoul-loona-kpop",
            "https://gfycat.com/welldocumentedopulentarieltoucan-jinsoul-loona",
            "https://gfycat.com/agonizingincompatiblebluegill",
            "https://gfycat.com/bigheartedhalfbetafish-jinsoul-loona",
            "https://gfycat.com/agreeablecreativecuscus-jinsoul-loona",
            "https://gfycat.com/hospitableconstantauk",
            "https://gfycat.com/circularcrispairedale",
            "https://gfycat.com/clearcuthappygoluckyanaconda-loona-jinsoul",
            "https://gfycat.com/cheerfulmasculineaidi",
            "https://gfycat.com/feminineslowimpala",
            "https://gfycat.com/flatcooperativeblackandtancoonhound-jinsoul-loona",
            "https://gfycat.com/goodnaturedfantastichalicore",
            "https://gfycat.com/glumkindheartedfruitbat",
            "https://gfycat.com/demandingmemorableerne",
            "https://gfycat.com/gaseousslimyelephantseal",
            "https://gfycat.com/glassfinishedbernesemountaindog-jinsoul-loona-rain",
            "https://gfycat.com/grandioseshamelessjenny-jinsoul-loona",
            "https://gfycat.com/graywelloffguineafowl-blockberrycreative-jinsoul-kim-lip",
            "https://gfycat.com/smartsatisfiedelk",
            "https://gfycat.com/leadingpersonalbarnacle-jinsoul-loona",
            "https://gfycat.com/sparklingbabyisheuropeanpolecat-dog",
            "https://gfycat.com/thatelegantdove-jinsoul-loona",
            "https://gfycat.com/helpfulwholedoctorfish-jinsoul-loona-chuu",
            "https://gfycat.com/carefulcorruptgentoopenguin-loona-jinsoul-jung-jinsoul-kpop-idol",
            "https://gfycat.com/impeccableheartyamericanquarterhorse-jinsoul-loona",
            "https://gfycat.com/insecurepastanhinga-jinsoul-loona",
            "https://gfycat.com/lastingwetamazontreeboa"]

        self.bot.choerry_gif = ["https://tenor.com/view/choerry-loona-gif-18740424",
            "https://tenor.com/view/loona-choerry-kpop-cute-wave-gif-16635613",
            "https://tenor.com/view/choi-yerim-choerry-kpop-paper-loona-gif-17213985",
            "https://cdn.discordapp.com/attachments/747275528993636424/775111507486310450/4ab7d195-ce65-423a-a177-cb1f6a6a7648.gif",
            "https://media.discordapp.net/attachments/704248706269970488/775111463579942952/image0.gif",
            "https://cdn.discordapp.com/attachments/747275528993636424/775112055244980264/2010061.gif",
            "https://cdn.discordapp.com/attachments/747275528993636424/775112225965867048/2002192.gif",
            "https://gfycat.com/euphoricblackandwhitehorsechestnutleafminer",
            "https://gfycat.com/deficientcreamyguernseycow",
            "https://gfycat.com/fabulousequalauk-choerry-loona-kpop-trkz",
            "https://gfycat.com/secretunimportanteasternglasslizard-beauty",
            "https://gfycat.com/flatpartialichidna-beauty",
            "https://gfycat.com/bossyfrightenedhorsechestnutleafminer",
            "https://gfycat.com/dismalunripeiberianlynx-loona",
            "https://gfycat.com/querulousoldfashionedhousefly-choerry-loona",
            "https://gfycat.com/grossidleamericanbadger-choerry-yeojin-haseul-loona",
            "https://gfycat.com/heartfeltfrankdipper-choerry-loona",
            "https://gfycat.com/contentbrightazurevase-choerry-loona",
            "https://gfycat.com/mixedserenegoosefish-choerry-loona",
            "https://gfycat.com/adorablewastefulindochinesetiger-choerry-loona",
            "https://gfycat.com/baddamphawk-choerry-loona",
            "https://gfycat.com/feminineplushindochinahogdeer-beauty",
            "https://gfycat.com/naivecornyalligatorsnappingturtle-choerry-loona-kpop",
            "https://gfycat.com/lividcreamyaustralianfurseal-choerry-hi-high-loona",
            "https://gfycat.com/clearcutbaggyaphid-beauty",
            "https://gfycat.com/caninepolishedappaloosa",
            "https://gfycat.com/gloriouslegitimateacaciarat-beauty",
            "https://gfycat.com/gratefulbrieferin-beauty",
            "https://gfycat.com/nimbleplainhare-beauty",
            "https://imgur.com/gallery/BpD4gIY",
            "https://66.media.tumblr.com/5741bda68909721068fba61013aef9c3/75876dc8f5b2ef0a-47/s400x600/d853959d780f2aac90f4ef94ba0b5e49da4d0d65.gif",
            "https://66.media.tumblr.com/133ec1793299fc140783639957c561d9/75876dc8f5b2ef0a-24/s400x600/ee903ed8c236d65af427e9066e170c19259a2cfe.gif",
            "https://66.media.tumblr.com/5b69e8b5d1e556fe406dfa1c70268d3c/75876dc8f5b2ef0a-76/s400x600/855f178d6fb6850d2b552197ac393e42a918f6d9.gif",
            "https://i.pinimg.com/originals/5b/4b/0c/5b4b0c6e5e620a25101c8c849ce4b4d6.gif",
            "https://i.pinimg.com/originals/ba/a7/ea/baa7eaebd16ddc3b2490232523655347.gif",
            "https://64.media.tumblr.com/dba3e19e2b17bf90f76ecc5720bc1d3d/86ff17a81a7186f2-70/s250x400/13c923b7950a216fc61bf306fcfcdc4577857ff2.gif"]
        
        self.bot.yves_gif = ["https://tenor.com/view/yves-loona-fainting-jail-kpop-gif-18490526",
            "https://tenor.com/view/loona-whynot-yves-gif-18911743",
            "https://tenor.com/view/loona-yves-gif-19104615",
            "https://tenor.com/view/yves-loona-gif-19166650",
            "https://tenor.com/view/yves-loona-gif-19166651",
            "https://tenor.com/view/yves-loona-satellite-shy-yves-shy-gif-18451495",
            "https://tenor.com/view/yves-swan-so-what-gif-19050405",
            "https://tenor.com/view/yves-loona-finger-heart-love-gif-15189376",
            "https://tenor.com/view/yves-loona-nods-gif-11903464",
            "https://tenor.com/view/whynot-loona-yves-gif-19007216",
            "https://tenor.com/view/loona-yves-love-gif-14534865",
            "https://tenor.com/view/yves-loona-come-here-come-with-me-gif-16467667",
            "https://gfycat.com/academicvictorioushellbender-ha-sooyoung-kuro-gurokami-loona-yves-kpop-idol",
            "https://gfycat.com/academicclumsybighorn-loona-asian-yves-girl-kpop",
            "https://gfycat.com/afraidbreakableallensbigearedbat",
            "https://gfycat.com/annualgentleanhinga-idalyi-sonyeo-loona-yves-yyxy",
            "https://gfycat.com/darlinginfinitehypsilophodon-ha-sooyoung-kuro-gurokami-loona-yves-kpop-idol",
            "https://gfycat.com/basicparallellamb",
            "https://gfycat.com/bothbountifulblackrhino",
            "https://gfycat.com/deafeningperiodicazurevase-ha-sooyoung-loona-yves-kpop-idol",
            "https://gfycat.com/friendlyvibrantdog-ha-sooyoung-kuro-gurokami-loona-yves-kpop-idol",
            "https://gfycat.com/emptyickyemperorshrimp-ha-sooyoung-kuro-gurokami-loona-yves-kpop-idol",
            "https://gfycat.com/grandsandyglobefish-ha-sooyoung-kuro-gurokami-loona-yves-kpop-idol",
            "https://gfycat.com/equatorialilliteratefrenchbulldog-ha-sooyoung-kuro-gurokami-loona-yves-kpop-idol",
            "https://gfycat.com/hairygenuinehammerheadshark",
            "https://gfycat.com/joyfulamuseddromaeosaur-beauty",
            "https://gfycat.com/immenseheartylangur-ha-sooyoung-kuro-gurokami-loona-yves-kpop-idol",
            "https://gfycat.com/mammothfragrantkronosaurus-loona-yves",
            "https://gfycat.com/measlyquarrelsomeanophelesmosquito",
            "https://gfycat.com/cavernoussneakygenet",
            "https://gfycat.com/brownmagnificentdamselfly",
            "https://gfycat.com/delightfulfemininehare-loona-yves",
            "https://gfycat.com/cleanunacceptablefruitbat-loona-yves",
            "https://gfycat.com/dimwittedbackcrayfish-ha-sooyoung-kuro-gurokami-loona-yves-kpop-idol",
            "https://gfycat.com/handmadedisastrousdipper-loona-yves",
            "https://gfycat.com/femalegargantuanboaconstrictor-loona-yves",
            "https://gfycat.com/faintbreakablehornet",
            "https://gfycat.com/flimsypiercingdugong",
            "https://gfycat.com/advancedshowybudgie-blockberrycreative-loonatheworld",
            "https://gfycat.com/bossyearnestavians-full-moon-loona-sunmi-yves",
            "https://gfycat.com/fewplastickatydid",
            "https://gfycat.com/blushingdismalkakapo-digipedi-loona-yves-new",
            "https://gfycat.com/impartialdistantboto-loona-yves",
            "https://gfycat.com/vaguecookedchrysomelid-ha-sooyoung-kuro-gurokami-loona-yves-gap-crush",
            "https://gfycat.com/determinedscornfulastrangiacoral-loona-yves",
            "https://gfycat.com/imaginativescientificbat-loona-yves",
            "https://gfycat.com/fairbeautifulafricanbushviper",
            "https://gfycat.com/aptblaringapisdorsatalaboriosa-loona-yves",
            "https://gfycat.com/generalserenegannet-ha-sooyoung-kuro-gurokami-loona-yves-gap-crush",
            "https://gfycat.com/bruisedkeenarrowcrab-yves-beauty",
            "https://gfycat.com/givingedibleimpala-hyunjin-yeojin-heejin-loona-yves",
            "https://gfycat.com/famousradiantblesbok",
            "https://gfycat.com/coolfrailenglishpointer",
            "https://gfycat.com/gregariousdopeyjabiru-comeback-stage-the-show-so-what-loona",
            "https://gfycat.com/meatybrieffallowdeer",
            "https://gfycat.com/mixedbelovedakitainu-yves-loops",
            "https://gfycat.com/metallicfailingamurminnow-mechabear-loona-yves-kpop",
            "https://gfycat.com/unhappyshowyarthropods-beautiful-korean-loona-idalyisonyeo-yves",
            "https://gfycat.com/thatflippantarizonaalligatorlizard-beautiful-korean-loona-idalyisonyeo-yves",
            "https://gfycat.com/devotednaiveangora-ha-sooyoung-kuro-gurokami-loona-yves-kpop-idol",
            "https://gfycat.com/impassionedsmoggyharrierhawk-loona-yves",
            "https://gfycat.com/coolshorttermarawana-loona-kpop-trkz-yves"]

        self.bot.chuu_gif = ["https://tenor.com/view/chuu-loona-jiwoo-loona-chuu-heart-attack-gif-19200978",
            "https://tenor.com/view/fome-eat-hungry-snow-girl-gif-17723791",
            "https://tenor.com/view/chuu-heart-attack-arrow-gif-15516607",
            "https://tenor.com/view/chuu-chuu-heart-loona-loona-heart-kpop-girl-gif-15567590",
            "https://tenor.com/view/chuu-gif-18868429",
            "https://tenor.com/view/ooh-loona-fancy-chuu-kpop-gif-17090975",
            "https://tenor.com/view/chuu-chuu-loona-chuu-woah-woah-loona-gif-19236767",
            "https://tenor.com/view/kpop-loona-chuu-hi-happy-gif-18586089",
            "https://tenor.com/view/chuu-gif-18979392",
            "https://tenor.com/view/chuu-fire-chuu-fire-chaos-kpop-gif-17946860",
            "https://tenor.com/view/loona-kpop-korean-chuu-loona-chu-gif-12852146",
            "https://tenor.com/view/loona-chuu-happy-smile-aegyo-gif-16082308",
            "https://tenor.com/view/chuu-loonachuu-loona-stan-thumbs-up-gif-12784143",
            "https://tenor.com/view/chuu-loona-gif-18055139",
            "https://tenor.com/view/chuu-loona-hamburguer-heart-heart-untitled127-gif-13827374",
            "https://tenor.com/view/loona-chuu-yes-happy-smile-gif-14322751",
            "https://tenor.com/view/chuu-loona-ne-yes-cute-gif-14954652",
            "https://tenor.com/view/chuu-gif-18979395",
            "https://tenor.com/view/chuu-look-at-you-kim-jiwoo-girl-of-the-month-loonatheworld-gif-19440716",
            "https://tenor.com/view/chuu-loona-kim-jiwoo-loonatheworld-kpop-gif-gif-19449093",
            "https://tenor.com/view/loona-kim-ji-woo-chuu-drama-dating-class-gif-14113598",
            "https://gfycat.com/accomplisheduniformleafbird-loona-chuu",
            "https://gfycat.com/alarmedthirdakitainu-loona-chuu",
            "https://gfycat.com/adoredunkemptamericanblackvulture-loona-chuu",
            "https://gfycat.com/agitatedchillyelephant",
            "https://gfycat.com/alertfavorablefrog",
            "https://gfycat.com/angelicsandybobolink-loona-chuu",
            "https://gfycat.com/backwhiteafricanparadiseflycatcher",
            "https://gfycat.com/nearfailingaldabratortoise-chuu",
            "https://gfycat.com/bogusdeliriouskudu",
            "https://gfycat.com/willingmediocreilsamochadegu-loona-chuu-go-won",
            "https://gfycat.com/carefulharshkronosaurus",
            "https://gfycat.com/thunderousscratchykingbird-loona-chuu",
            "https://gfycat.com/majesticquarterlyferret-idalyi-sonyeo-loona-chuu-gimjiu-cyu",
            "https://gfycat.com/ethicalshortbuck-concert-fancam-loona-chuu-gsd-geolgeurub-aidol",
            "https://gfycat.com/dishonestimmaculatekingbird-dating-class-loona-chuu",
            "https://gfycat.com/unnaturalanchoredjenny-heart-loona-chuu",
            "https://gfycat.com/melodicthosebluefintuna",
            "https://gfycat.com/windingbountifulkissingbug-blockberrycreative-all-tags-haseul",
            "https://gfycat.com/cheerfulwillingbushbaby-loona-chuu",
            "https://gfycat.com/costlysimplisticaustraliancurlew-heejin-loona",
            "https://gfycat.com/decimalidenticalburro-loona-chuu-kim-jiwoo",
            "https://gfycat.com/severegoodnaturedagama-olivia-hye-jinsoul-loona-chuu-kpop",
            "https://gfycat.com/failingmammothatlasmoth-loona-chuu",
            "https://gfycat.com/fearlesspeskybrownbear",
            "https://gfycat.com/lavishadmiredgazelle",
            "https://gfycat.com/realisticgloriousarabianhorse",
            "https://gfycat.com/equalnaivebirdofparadise-reaction-loona-chuu-kpop",
            "https://gfycat.com/shockedgivingachillestang",
            "https://gfycat.com/singleplaintivebaleenwhale",
            "https://gfycat.com/practicalathleticarabianhorse",
            "https://gfycat.com/speedyloathsomeantarcticgiantpetrel-loona-chuu-kim-jiwoo-idol",
            "https://gfycat.com/filthycompetentfoal-heejin-loona-chuu",
            "https://gfycat.com/hoarsegreatgharial",
            "https://gfycat.com/greeneducatedlhasaapso-loona-chuu",
            "https://gfycat.com/icydetailedcow",
            "https://gfycat.com/ashamedimpurehoatzin",
            "https://gfycat.com/imaginaryklutzycrossbill-loona-chuu-kpop",
            "https://gfycat.com/impracticalpotablebunting-loona-chuu",
            "https://gfycat.com/crazyperiodicchafer-loona-so-what-kuro-gurokami-loona-chuu-kpop-idol",
            "https://gfycat.com/cluelesssadcavy-kuro-gurokami-loona-chuu-isac-2020-kim-jiwoo-fps",
            "https://gfycat.com/colorlessgargantuandinosaur",
            "https://gfycat.com/demandingajaralaskanhusky-butterfly-loona-2019-chuu",
            "https://gfycat.com/differentsimplistichuemul-mechabear-loona-chuu-kpop",
            "https://gfycat.com/difficultunawareelver-mechabear-loona-chuu-kpop",
            "https://gfycat.com/discreteactualcollie-fansign-loona-kpop-chuu",
            "https://gfycat.com/earnestthoroughguillemot-loona-chuu",
            "https://gfycat.com/flusteredsimilarbluejay",
            "https://gfycat.com/forsakenyearlykiskadee-loona-chuu-kpop",
            "https://gfycat.com/frequentdemandingichthyostega",
            "https://gfycat.com/gleefulbleakboutu-loona-chuu-kim-jiwoo-kpop-idol-kuro",
            "https://gfycat.com/glisteninggeneralalaskanhusky",
            "https://gfycat.com/handyhandsomeinganue-loona-chuu",
            "https://gfycat.com/harmfulperfumedhake-loona-chuu",
            "https://gfycat.com/heftyweebufflehead-loona-so-what-kuro-gurokami-loona-chuu-kpop-idol",
            "https://gfycat.com/hotmintyclam-loona-chuu",
            "https://gfycat.com/ignorantsilverbumblebee-dating-class-loona-chuu",
            "https://gfycat.com/insecuresimplistickingfisher-loona-chuu",
            "https://gfycat.com/impressionablenicedungbeetle-idalyi-sonyeo-tiktok-loona-loopd-kpop-idol-chuu",
            "https://gfycat.com/inferiorfreshguineafowl",
            "https://gfycat.com/indolentbrownacornwoodpecker-yeonyelivewebdeilri-loona-chuu",
            "https://gfycat.com/colorfulunhappygalapagostortoise-fancam-goyang-loona-chuu-kpop-yyxy",
            "https://gfycat.com/darksarcasticbassethound-loona-chuu",
            "https://gfycat.com/deafeningremarkablecrocodile-loona-chuu-yyxy-kpop",
            "https://gfycat.com/definitedamagedhousefly-loona-chuu-yyxy-kpop",
            "https://gfycat.com/definitivememorablearmedcrab-kuro-gurokami-loona-chuu-kim-jiwoo-celenbs-kpop",
            "https://gfycat.com/differentbossyblacklemur-kuro-gurokami-loona-chuu-kim-jiwoo-kpop-idol",
            "https://gfycat.com/lavishuntimelyeeve",
            "https://gfycat.com/goodnaturedunconsciousasianlion-beauty",
            "https://gfycat.com/goodnaturedlittlekakapo",
            "https://gfycat.com/watchfulgifteddingo-loona-so-what-kuro-gurokami-loona-chuu-kpop-idol",
            "https://gfycat.com/immenseyearlyankole",
            "https://gfycat.com/jaggedmassiveelephantbeetle-chuu-can-do-it-loona-kpop-ep-1",
            "https://gfycat.com/leadingrigidheron-heejin-loona-chuu",
            "https://gfycat.com/majesticaggravatinghylaeosaurus-loona-so-what-kuro-gurokami-loona-chuu-kpop-idol",
            "https://gfycat.com/melodicacceptableliger",
            "https://gfycat.com/recklessnimblefugu-loona-gowon-chuu",
            "https://gfycat.com/rectangularthisindianhare-loona-chuu",
            "https://gfycat.com/quarrelsomepaltrycoral",
            "https://gfycat.com/rigidanguishedantipodesgreenparakeet-loona-chuu-kpop-yawn",
            "https://gfycat.com/belatedrapidiggypops-loona-chuu-yyxy-kpop",
            "https://gfycat.com/scrawnyenergeticgazelle-kimjiwoo-loonachuu-wink-yyxy-gimjiu"]

        self.bot.gowon_gif = ["https://tenor.com/view/gowon-park-gowon-park-chaewon-loona-loona-gowon-gif-13191168",
            "https://tenor.com/view/loona-go-won-kpop-gif-14252120",
            "https://tenor.com/view/gowon-loona-gif-11903470",
            "https://tenor.com/view/loona-gowon-gif-18868391",
            "https://tenor.com/view/gowon-park-gowon-park-chaewon-loona-loona-gowon-gif-13184441",
            "https://tenor.com/view/gowon-flying-kiss-muah-red-lips-gif-13731778",
            "https://tenor.com/view/loona-gowon-kpop-gif-18738916",
            "https://tenor.com/view/loona-kpop-gowon-spoon-gif-18585817",
            "https://tenor.com/view/loona-kpop-gowon-cheek-squish-gif-18585812",
            "https://tenor.com/view/loona-gowon-dance-gif-12433093",
            "https://tenor.com/view/loona-gowon-gowon-loona-kpop-gif-18739724",
            "https://tenor.com/view/gowon-loona-gif-19126206",
            "https://tenor.com/view/loona-gowon-yawning-kpop-gif-18890935",
            "https://tenor.com/view/gowon-loona-gif-19126206",
            "https://gfycat.com/athletichugeauklet-beauty",
            "https://gfycat.com/beneficialthoughtfulkudu",
            "https://gfycat.com/bewitchedelegantairedaleterrier-go-won-loona-beauty",
            "https://gfycat.com/bitterfarconey-gowon-loona-kpop",
            "https://gfycat.com/negativewaterloggedlarva-butterfly-chaewon-loona-gowon",
            "https://gfycat.com/athleticuntidycero-gowon-loona",
            "https://gfycat.com/disfiguredleftcaimanlizard-park-chaewon-loona-gowon-kuro-gurokami-kpop-idol",
            "https://gfycat.com/braveorganicazurevase",
            "https://gfycat.com/deeprevolvingflicker-loona-gowon",
            "https://gfycat.com/biodegradableorangeafricanbushviper-jinsoul-loonatv-gowon-kpop",
            "https://gfycat.com/cavernousforcefulcicada-loona-gowon",
            "https://gfycat.com/redwarlikearmadillo-gowon-loona-asian-kiss-kpop-girl",
            "https://gfycat.com/brightdependentchimneyswift",
            "https://gfycat.com/acrobaticplaintivecricket-loona-gowon",
            "https://gfycat.com/calmmisguidedgoldfish-loona-gowon",
            "https://gfycat.com/advancedwhirlwindboubou-loona-gowon",
            "https://gfycat.com/boilingfluffyarcherfish",
            "https://gfycat.com/bitesizedharshantarcticfurseal-go-won-loona",
            "https://gfycat.com/allinformalcollie-loona-gowon",
            "https://gfycat.com/boringfittingharrierhawk-loona-gowon",
            "https://gfycat.com/capitalbossyfallowdeer-loona-gowon",
            "https://gfycat.com/charmingfortunateharpseal-loona-gowon",
            "https://gfycat.com/chiefsombergroundbeetle-loona-gowon",
            "https://gfycat.com/scentedposhindochinesetiger-beauty",
            "https://gfycat.com/eagerpoisedimperialeagle",
            "https://gfycat.com/colorfuladoredbream",
            "https://gfycat.com/delectableminiaturefurseal-gowon-loona",
            "https://gfycat.com/esteemednearisabellinewheatear-butterfly-go-won-loona",
            "https://gfycat.com/immensecommongander-beauty",
            "https://gfycat.com/impressiveyoungkoi-loona-go-won",
            "https://gfycat.com/requiredlankychinchilla-loona-gowon",
            "https://gfycat.com/insecurediscreteenglishsetter-loona-gowon",
            "https://gfycat.com/clutteredrewardingbackswimmer",
            "https://gfycat.com/costlyacclaimedharpseal-gowon-loona-2019-kpop",
            "https://gfycat.com/lastingtalkativeclam-loona-gowon",
            "https://gfycat.com/faintwholebug-beauty",
            "https://gfycat.com/pepperygorgeousamethystgemclam-gowon-k-pop-loona-idol",
            "https://gfycat.com/selfishunevendanishswedishfarmdog",
            "https://gfycat.com/grippinglinedeyra",
            "https://gfycat.com/forsakenrespectfulcrow-loona-gowon",
            "https://gfycat.com/severeinformalherald-loona-gowon",
            "https://gfycat.com/snivelinggloriousinsect",
            "https://gfycat.com/everyfancybellsnake-gowon-loona-beauty",
            "https://gfycat.com/wateryyellowbarb-gowon-loona-beauty",
            "https://gfycat.com/ecstaticterrificflounder-loona-gowon",
            "https://gfycat.com/educatedcompleteilsamochadegu-go-won-loona",
            "https://gfycat.com/entireunfoldedhalibut",
            "https://gfycat.com/faroffobedientfinnishspitz-loona-gowon",
            "https://gfycat.com/fineparchedlice-loona-gowon",
            "https://gfycat.com/finediscreteindianringneckparakeet-loona-gowon"]

        self.bot.oliviahye_gif = ["https://tenor.com/view/loona-olivia-hye-hyejoo-cute-beautiful-gif-16689725",
            "https://tenor.com/view/loona-olivia-hye-son-hyejoo-bunny-ears-bunny-gif-16778977",
            "https://tenor.com/view/olivia-hye-hyejoo-olivia-hey-loona-loona-olivia-hye-gif-16808778",
            "https://tenor.com/view/loona-olivia-hye-son-hyejoo-dancer-vocalist-gif-17147871",
            "https://tenor.com/view/kim-hyejoo-attempt-cute-olivia-fail-gif-17193603",
            "https://tenor.com/view/olivia-hye-hyejoo-loona-rae-butterfly-gif-18963804",
            "https://tenor.com/view/loona-olivia-hye-son-hyejoo-dancer-vocalist-gif-17696702",
            "https://tenor.com/view/olivia-hye-hyejoo-smile-pretty-cute-gif-15567631",
            "https://tenor.com/view/olivia-hye-son-hyejoo-loona-yyxy-puff-cheeks-gif-15633712",
            "https://tenor.com/view/olivia-hye-hyejoo-full-moon-loona-dancing-gif-15567587",
            "https://tenor.com/view/oliviahye-loona-olivia-loona-olivia-hyejoo-hyejoo-gif-16474426",
            "https://tenor.com/view/aliphobe-olivia-hye-loona-yyxy-hyejoo-gif-17860838",
            "https://tenor.com/view/oliviahye-gif-18868773",
            "https://tenor.com/view/loona-olivia-hye-pout-sad-gif-14917239",
            "https://tenor.com/view/olivia-hye-loona-hyejoo-peek-aboo-cute-gif-19532995",
            "https://cdn.discordapp.com/attachments/801512286879481926/801677200461922364/tenor-3.gif",
            "https://gfycat.com/ScientificContentCaterpillar",
            "https://cdn.discordapp.com/attachments/801512286879481926/801687284579041320/tenor-4.gif",
            "https://cdn.discordapp.com/attachments/801512286879481926/801689087936692224/fdd21e4910ff3f22437723e5b4d95261.gif",
            "https://cdn.discordapp.com/attachments/801512286879481926/801691398734610482/a0b5a78f63cd36c21e668669e1c727011a949f87r1-268-370_hq.gif",
            "https://gfycat.com/admirablelimpingflee-olivia-hye-loona",
            "https://gfycat.com/activeillinformedharborseal-olivia-hye-loona",
            "https://gfycat.com/activescholarlycockatiel-olivia-hye-loona",
            "https://gfycat.com/activeunfoldedcob",
            "https://gfycat.com/actualpiercinggrunion",
            "https://gfycat.com/afraidnarrowauk-olivia-hye-loona-choerry-beauty",
            "https://gfycat.com/adventurousbreakablebrontosaurus-olivia-hye-loona",
            "https://gfycat.com/ajarantiqueadamsstaghornedbeetle",
            "https://gfycat.com/allquaintleopardseal-loona-olivia-hye-beauty",
            "https://gfycat.com/agonizingleanbetafish-olivia-hye-loona-kpop",
            "https://gfycat.com/astonishingoptimalalligator-olivia-hye-loona",
            "https://gfycat.com/aridicychafer-olivia-hye-loona",
            "https://gfycat.com/aptshockedgemsbok-olivia-hye",
            "https://gfycat.com/baretotalayeaye-olivia-hye-loona",
            "https://gfycat.com/barewatchfulerin-olivia-hye-loona",
            "https://gfycat.com/boilingdefinitegar-olivia-hye-loona",
            "https://gfycat.com/carefulglamorousdutchshepherddog-olivia-hye-loona",
            "https://gfycat.com/chiefpoorduckling-miyuzitsukubideo-teaser-hallyu-1thek-kepotsupu",
            "https://gfycat.com/chiefnecessaryemperorshrimp-olivia-hye-so-what-loona-dance-kpop",
            "https://gfycat.com/agitatedtallhammerkop-hebeunjeudoeo-beauty",
            "https://gfycat.com/calculatingfaithfuljerboa-olivia-hye-loona",
            "https://gfycat.com/blushingunsightlyannelid-olivia-hye-loona",
            "https://gfycat.com/blackandwhiteunfinishedasp-loona-olivia-hye-kuro-gurokami-son-hyejoo-kpop",
            "https://gfycat.com/cheerfulcomfortableblackbear-olivia-hye-loona",
            "https://gfycat.com/circularangeliciaerismetalmark-olivia-hye-loona",
            "https://gfycat.com/enchantedimprobableghostshrimp-olivia-hye-loona",
            "https://gfycat.com/enchantingalertaphid-loona-olivia-hye",
            "https://gfycat.com/negativeheavenlyjuliabutterfly-olivia-hye-loona",
            "https://gfycat.com/jointinformalaustraliankelpie-olivia-hye-loona",
            "https://gfycat.com/infiniteflakygermanpinscher-olivia-hye-loona",
            "https://gfycat.com/parchedlamebrownbear-ollvla-hye",
            "https://gfycat.com/nippyimpressiveargusfish-olivia-hye",
            "https://gfycat.com/untimelyselfreliantekaltadeta-olivia-hye-loona",
            "https://gfycat.com/alienatedoilyborer-olivia-hye-loona",
            "https://gfycat.com/ajarickygerbil",
            "https://gfycat.com/abandonedenergeticaardwolf",
            "https://gfycat.com/anyfatleafbird-olivia-hye-loona",
            "https://gfycat.com/affectionateorderlyiberianbarbel",
            "https://gfycat.com/antiquedefiantkilldeer-olivia-hye-loona",
            "https://gfycat.com/alertmixedhadrosaurus-olivia-hye-loona",
            "https://gfycat.com/beautifulidolizedleafcutterant-olivia-hye-loona",
            "https://gfycat.com/aromatichonoredgrunion-olivia-hye-loona",
            "https://gfycat.com/angryultimatedormouse-beauty",
            "https://gfycat.com/ashamedhastychick-olivia-hye-loona",
            "https://gfycat.com/baddeafeningjunebug-olivia-hye-loona",
            "https://gfycat.com/baggydeadkilldeer",
            "https://gfycat.com/blackandwhiteunripekillifish-olivia-hye-loona",
            "https://gfycat.com/blanksimplebernesemountaindog-olivia-hye-loona",
            "https://gfycat.com/blushingsorrowfulfinwhale-loona",
            "https://gfycat.com/breakabletotalkingbird-olivia-hye-choerry-jinsoul-loona",
            "https://gfycat.com/calmanimatedfattaileddunnart-beauty",
            "https://gfycat.com/bareaccuratecardinal-olivia-hye-loona",
            "https://gfycat.com/homelymiserlybutterfly",
            "https://gfycat.com/carelessgleefulkawala",
            "https://gfycat.com/completevainamericanlobster-olivia-hye-heejin-loona",
            "https://gfycat.com/whimsicallatecutworm-olivia-hye-loona",
            "https://gfycat.com/breakableashamedchihuahua-olivia-hyem-gowon",
            "https://gfycat.com/brilliantbaggyicterinewarbler-olivia-hye-loona",
            "https://gfycat.com/carefulglamorousdutchshepherddog-olivia-hye-loona",
            "https://gfycat.com/hoarsewarmdove-olivia-hye-loona",
            "https://gfycat.com/disastroushideousleafcutterant-olivia-hye-stan-loona-oing",
            "https://gfycat.com/concernedembellishedgraysquirrel-olivia-hye-loona",
            "https://gfycat.com/circularangeliciaerismetalmark-olivia-hye-loona",
            "https://gfycat.com/colossalcavernousindigobunting-beauty",
            "https://gfycat.com/sophisticatedecstaticantarcticfurseal-olivia-hye-loona",
            "https://gfycat.com/tameincomparableconch-olivia-hye-loona-yves",
            "https://gfycat.com/unfitdapperghostshrimp",
            "https://gfycat.com/variableeverydegus",
            "https://gfycat.com/untriedglumbighornsheep-olivia-hye-loona",
            "https://gfycat.com/wickedunknownleafwing-olivia-hye-loona"]

        self.bot.chuuheart_gif = ["https://static.apester.com/user-images/cb/cb60802a9e5ff8aa501df36ddfa56cce.gif",
            "https://tenor.com/view/mamamoo-wheein-heart-kpop-dance-gif-16331749",
            "https://tenor.com/view/kpop-loona-chuu-heart-love-gif-18586088",
            "https://tenor.com/view/chuu-loona-hamburguer-heart-heart-untitled127-gif-13827374",
            "https://tenor.com/view/chuu-loona-chuu-loona-cute-kpop-gif-16242378",
            "https://media.discordapp.net/attachments/758500230386679848/775129870559870976/ezgif-7-864231320452.gif",
            "https://tenor.com/view/seulgi-kang-seulgi-red-velvet-cute-pretty-gif-16937522",
            "https://tenor.com/view/wendy-shon-son-seungwan-red-velvet-%ec%9b%ac%eb%94%94-%eb%a0%88%eb%93%9c%eb%b2%a8%eb%b2%b3-gif-16069063",
            "https://tenor.com/view/yoona-im-yoona-%ec%9c%a4%ec%95%84-snsd-girls-generation-gif-14170845",
            "https://tenor.com/view/heart-love-apple-heart-chuu-heart-da-vinki-gif-18549840",
            "https://tenor.com/view/sakura-izone-sakura-miyawaki-sakura-saku-chan-chaekura-kkura-gif-13532539",
            "https://cdn.discordapp.com/attachments/704248706269970488/776652835617898516/image0.gif",
            "https://tenor.com/view/yeeun-jang-yeeun-cute-clc-kpop-gif-17883335",
            "https://tenor.com/view/g-idle-yuqi-song-yuqi-kpop-cute-gif-17667093",
            "https://tenor.com/view/chuu-gif-18979395",
            "https://tenor.com/view/bang-chan-gif-18200044",
            "https://tenor.com/view/somin-kard-gif-18981833",
            "https://tenor.com/view/heart-kard-somin-gif-18981834",
            "https://gfycat.com/impressiveyoungkoi-loona-go-won",
            "https://gfycat.com/allquaintleopardseal-loona-olivia-hye-beauty"]

    @commands.command()
    async def loona(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Loona {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "heejin":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{mae}>, <@{aeong}>, <@!{ctx.author.id}> is talking about Heejin :rabbit:')
                    await ctx.send(random.choice(self.bot.heejin_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Heejin :rabbit:')
                await ctx.send(random.choice(self.bot.heejin_gif))
                await ctx.message.delete()
        elif arg == "hyunjin":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{k8}>, <@{aeong}>, <@!{ctx.author.id}> is talking about Hyunjin :cat::bread:')
                    await ctx.send(random.choice(self.bot.hyunjin_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Hyunjin :cat::bread:')
                await ctx.send(random.choice(self.bot.hyunjin_gif))
                await ctx.message.delete()
        elif arg == "haseul":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Haseul :dove::green_heart:')
                    await ctx.send(random.choice(self.bot.haseul_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Haseul :dove::green_heart:')
                await ctx.send(random.choice(self.bot.haseul_gif))
                await ctx.message.delete()
        elif arg == "vivi":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{manman}>, <@{ctx.author.id}> is talking about ViVi :deer:')
                    await ctx.send(random.choice(self.bot.vivi_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about ViVi :deer:')
                await ctx.send(random.choice(self.bot.vivi_gif))
                await ctx.message.delete()
        elif arg == "yeojin":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Yeojin :frog::orange_heart:')
                    await ctx.send(random.choice(self.bot.yeojin_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Yeojin :frog::orange_heart:')
                await ctx.send(random.choice(self.bot.yeojin_gif))
                await ctx.message.delete()
        elif arg == "kim lip":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{stanley}>, <@!{ctx.author.id}> is talking about Kim Lip :owl:')
                    await ctx.send(random.choice(self.bot.kimlip_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=6)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Kim Lip :owl:')
                await ctx.send(random.choice(self.bot.kimlip_gif))
                await ctx.message.delete()
        elif arg == "jinsoul":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Jinsoul :fish:')
                    await ctx.send(random.choice(self.bot.jinsoul_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Jinsoul :fish:')
                await ctx.send(random.choice(self.bot.jinsoul_gif))
                await ctx.message.delete()
        elif arg == "choerry":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{rith}>, <@{ple}>, <@!{ctx.author.id}> is talking about Choerry :bat:')
                    await ctx.send(random.choice(self.bot.choerry_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()            
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Choerry :bat:')
                await ctx.send(random.choice(self.bot.choerry_gif))
                await ctx.message.delete()
        elif arg == "yves":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Yves :swan::apple:')
                    await ctx.send(random.choice(self.bot.yves_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()            
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yves :swan::apple:')
                await ctx.send(random.choice(self.bot.yves_gif))
                await ctx.message.delete()
        elif arg == "chuu":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Chuu :penguin::strawberry:')
                    await ctx.send(random.choice(self.bot.chuu_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()            
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chuu :penguin::strawberry:')
                await ctx.send(random.choice(self.bot.chuu_gif))
                await ctx.message.delete()
        elif arg == "go won" or arg == "gowon":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{rith}>, <@{masa}>, <@!{ctx.author.id}> is talking about Go Won :butterfly::pineapple:')
                    await ctx.send(random.choice(self.bot.gowon_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()            
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Go Won :butterfly::pineapple:')
                await ctx.send(random.choice(self.bot.gowon_gif))
                await ctx.message.delete()
        elif arg == "oliva hye" or arg == "olivia" or arg == "olihye":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Olivia Hye :wolf:')
                    await ctx.send(random.choice(self.bot.oliviahye_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()            
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Olivia Hye :wolf:')
                await ctx.send(random.choice(self.bot.oliviahye_gif))
                await ctx.message.delete()



#.1/3
    @commands.command()
    async def heejin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{mae}>, <@{aeong}>, <@!{ctx.author.id}> is talking about Heejin :rabbit:')
                await ctx.send(random.choice(self.bot.heejin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Heejin :rabbit:')
            await ctx.send(random.choice(self.bot.heejin_gif))
            await ctx.message.delete()

    @commands.command()
    async def hyunjin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{k8}>, <@{aeong}>, <@!{ctx.author.id}> is talking about Hyunjin :cat::bread:')
                await ctx.send(random.choice(self.bot.hyunjin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Hyunjin :cat::bread:')
            await ctx.send(random.choice(self.bot.hyunjin_gif))
            await ctx.message.delete()

    @commands.command()
    async def haseul(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{ctx.author.id}> is talking about Haseul :dove::green_heart:')
                await ctx.send(random.choice(self.bot.haseul_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@{ctx.author.id}> is talking about Haseul :dove::green_heart:')
            await ctx.send(random.choice(self.bot.haseul_gif))
            await ctx.message.delete()

    @commands.command()
    async def vivi(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{manman}>, <@{ctx.author.id}> is talking about ViVi :deer:')
                await ctx.send(random.choice(self.bot.vivi_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@{ctx.author.id}> is talking about ViVi :deer:')
            await ctx.send(random.choice(self.bot.vivi_gif))
            await ctx.message.delete()

    @commands.command()
    async def yeojin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{ctx.author.id}> is talking about Yeojin :frog::orange_heart:')
                await ctx.send(random.choice(self.bot.yeojin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@{ctx.author.id}> is talking about Yeojin :frog::orange_heart:')
            await ctx.send(random.choice(self.bot.yeojin_gif))
            await ctx.message.delete()


#.oec
    @commands.command(aliases=['kim', 'lip', 'lippington', 'kimlip'])
    async def lippie(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{stanley}>, <@!{ctx.author.id}> is talking about Kim Lip :owl:')
                await ctx.send(random.choice(self.bot.kimlip_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=6)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Kim Lip :owl:')
            await ctx.send(random.choice(self.bot.kimlip_gif))
            await ctx.message.delete()

    @commands.command()
    async def jinsoul(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{ctx.author.id}> is talking about Jinsoul :fish:')
                await ctx.send(random.choice(self.bot.jinsoul_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@{ctx.author.id}> is talking about Jinsoul :fish:')
            await ctx.send(random.choice(self.bot.jinsoul_gif))
            await ctx.message.delete()

    @commands.command()
    async def choerry(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{rith}>, <@{ple}>, <@!{ctx.author.id}> is talking about Choerry :bat:')
                await ctx.send(random.choice(self.bot.choerry_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()            
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Choerry :bat:')
            await ctx.send(random.choice(self.bot.choerry_gif))
            await ctx.message.delete()


#.yyxy
    @commands.command()
    async def yves(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yves :swan::apple:')
                await ctx.send(random.choice(self.bot.yves_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()            
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yves :swan::apple:')
            await ctx.send(random.choice(self.bot.yves_gif))
            await ctx.message.delete()

    @commands.command()
    async def chuu(self, ctx, heart="normalloona"):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Chuu {heart}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if heart == "heart":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to #bot-commands', delete_after=2)
            else:
                await ctx.send(f'nyam')
                await ctx.send(random.choice(self.bot.chuuheart_gif))
        else:
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Chuu :penguin::strawberry:')
                    await ctx.send(random.choice(self.bot.chuu_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()            
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chuu :penguin::strawberry:')
                await ctx.send(random.choice(self.bot.chuu_gif))
                await ctx.message.delete()

    @commands.command()
    async def gowon(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{rith}>, <@{masa}>, <@!{ctx.author.id}> is talking about Go Won :butterfly::pineapple:')
                await ctx.send(random.choice(self.bot.gowon_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()            
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Go Won :butterfly::pineapple:')
            await ctx.send(random.choice(self.bot.gowon_gif))
            await ctx.message.delete()

    @commands.command(aliases = ['hyejoo', 'hye', 'olivia'])
    async def oliviahye(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Olivia Hye :wolf:')
                await ctx.send(random.choice(self.bot.oliviahye_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()            
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Olivia Hye :wolf:')
            await ctx.send(random.choice(self.bot.oliviahye_gif))
            await ctx.message.delete()
    
#
def setup(client):
    client.add_cog(LoonaPings(client))