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

class ItzyPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.itzy_yeji_gif = ["https://tenor.com/view/yeji-itzy-jyp-entertainment-kpop-cute-gif-16653975",
            "https://tenor.com/view/yeji-yeji-itzy-hwang-yeji-gif-18718150",
            "https://tenor.com/view/yeji-hwang-yeji-itzy-wink-salute-gif-17307566",
            "https://tenor.com/view/yeji-itzy-jyp-entertainment-kpop-cute-gif-16653970",
            "https://tenor.com/view/hwang-yeji-yeji-itzy-jyp-entertainment-kpop-gif-16652420",
            "https://tenor.com/view/kpop-itzy-yeji-cute-icy-gif-14653975",
            "https://tenor.com/view/itzy-yeji-itzy-yeji-hwang-yeji-kpop-gif-18379032",
            "https://gfycat.com/spotlessillinformedhyrax-itzy-yeji",
            "https://gfycat.com/repulsiveillegalcopepod-beauty",
            "https://gfycat.com/fittingrecenterin-itzy-yeji",
            "https://gfycat.com/courageousringedchipmunk-itzy",
            "https://gfycat.com/fittingrecenterin-itzy-yeji",
            "https://gfycat.com/courageousringedchipmunk-itzy",
            "https://gfycat.com/happygoluckyfatherlyamericancrayfish-itzy",
            "https://gfycat.com/familiarfelinecub-itzy-yeji",
            "https://gfycat.com/annualpastelchimneyswift-itzy-yeji",
            "https://gfycat.com/qualifiedspiritedchamois-itzy-yeji",
            "https://gfycat.com/immaculatequestionablediplodocus-yeji-itzy",
            "https://gfycat.com/terrificzestyglobefish-yeji-itzy",
            "https://gfycat.com/freshactualbeardeddragon-yeji-itzy",
            "https://gfycat.com/heavyelementarybadger-itzy",
            "https://gfycat.com/oddballheavenlybackswimmer-beauty",
            "https://gfycat.com/alivepartialaustrianpinscher-beauty",
            "https://gfycat.com/selfassuredfavorablefrigatebird-yeji-itzy",
            "https://gfycat.com/emotionalgeneralcollardlizard-itzy-yeji",
            "https://gfycat.com/mildwelcomeblackrussianterrier-beauty",
            "https://gfycat.com/essentialsizzlingbasilisk-beauty",
            "https://gfycat.com/linedunsightlyaquaticleech-beauty",
            "https://gfycat.com/adorablecompetentaphid-itzy-yeji",
            "https://gfycat.com/adorableincomparableduiker-yeji-itzy",
            "https://gfycat.com/ajardigitalacouchi-itzy-yeji",
            "https://gfycat.com/allcommonemperorshrimp-itzy-yeji",
            "https://gfycat.com/ambitiousdiscretealbacoretuna-beauty",
            "https://gfycat.com/amusingimperturbablekingsnake-itzy-yeji",
            "https://gfycat.com/anyvainladybug-itzy-yeji-beauty",
            "https://gfycat.com/thoroughsparklingbee-hwang-yeji-itzy-jype-kpop",
            "https://gfycat.com/babyishmeatyarcticduck-itzy-yeji",
            "https://gfycat.com/alivenippyislandcanary-yeji-itzy",
            "https://gfycat.com/aggravatingbarrencatfish-gidle-itzy-yeji",
            "https://gfycat.com/blackrespectfulindiancow-kpics-yeji-itzy",
            "https://gfycat.com/belatedweeasianpiedstarling-itzy-yeji",
            "https://gfycat.com/badmisguidedichthyostega-vlive-itzy-yeji",
            "https://gfycat.com/fatherlyorneryarcticduck-vlive-itzy-yeji",
            "https://gfycat.com/forsakenshadowyjaguar-hwang-yeji-itzy-jype-kpop",
            "https://gfycat.com/grandblankclownanemonefish-yeji-itzy",
            "https://gfycat.com/equaldecentdeinonychus-hwang-yeji-itzy-kpop-jyp",
            "https://gfycat.com/acceptablegargantuanchihuahua",
            "https://gfycat.com/appropriatefamiliaradouri-jyp-entertainment-itzy-chaeryeong",
            "https://gfycat.com/beautifulpleasedgoshawk",
            "https://gfycat.com/aptsmugisabellineshrike-adorable-cute-itzy-kpop-yeji",
            "https://gfycat.com/bestneglectedantbear-beauty",
            "https://gfycat.com/boringharmlesscero-itzy-reality-issji-rieolriti-issji-bihaindeu-issji-issji",
            "https://gfycat.com/bleakrelievedblackbird-itzy-yeji",
            "https://gfycat.com/boguspaltrygharial",
            "https://gfycat.com/blushingslowangora-yeji",
            "https://gfycat.com/bravequestionablekodiakbear-itzy-wannabe-kuro-gurokami-hwang-yeji-itzy-yeji",
            "https://gfycat.com/charmingkindlybinturong-itzy-yeji",
            "https://gfycat.com/grippingdentalauk-hwang-yeji-itzy-jype-kpop",
            "https://gfycat.com/daringdiscretedinosaur-itzy-yeji",
            "https://gfycat.com/newslipperyfirefly-yeji-itzy",
            "https://gfycat.com/dirtyfatdikkops-leader-smile-yeji-itzy-kpop-cute",
            "https://gfycat.com/minorwelltodocamel-hwang-yeji-itzy-yeji-kpop-idol-kuro",
            "https://gfycat.com/criminalalertcony-beauty",
            "https://gfycat.com/talkativerigidcopperbutterfly-beauty",
            "https://gfycat.com/kindheartedslimdegus-hwang-yeji-itzy-jype-kpop",
            "https://gfycat.com/ripelastingibadanmalimbe-itzy-yeji",
            "https://gfycat.com/safenaturalharlequinbug-kuro-gurokami-hwang-yeji-itzy-yeji-idol-kpop",
            "https://gfycat.com/nimbleimpracticalbonobo-hwangyeji-itzy-issji"]

        self.bot.itzy_ryujin_gif = ["https://tenor.com/view/ryujin-%EB%A5%98%EC%A7%84-itzy-shinryujin-gif-14922418",
            "https://tenor.com/view/ryujin-dance-moves-shake-it-pretty-gif-16723839",
            "https://tenor.com/view/ryujin-itzy-blow-kiss-shinryujin-gif-14437581",
            "https://tenor.com/view/itzy-ryujin-shin-ryujin-kpop-pretty-gif-15639935",
            "https://tenor.com/view/ryujin-itzy-shin-ryujin-kpop-cute-gif-16653996",
            "https://tenor.com/view/itzy-ryujin-gif-18137656",
            "https://tenor.com/view/itzy-jyp-entertainment-shin-ryujin-ryujin-main-rapper-gif-16721301",
            "https://tenor.com/view/ryujin-itzy-gif-18835542",
            "https://gfycat.com/cluelesshonestgalapagosmockingbird-ryujin-itzy",
            "https://gfycat.com/pinkacidicamericanbulldog-beauty",
            "https://gfycat.com/majestichardtofindgartersnake-ryujin-itzy",
            "https://gfycat.com/seriouseasygoingambushbug-beauty",
            "https://gfycat.com/tanboringcarpenterant-ryujin-itzy",
            "https://gfycat.com/liquidregalindianhare-ryujin-itzy",
            "https://gfycat.com/euphoricsnoopygilamonster-ryujin-itzy",
            "https://gfycat.com/prestigioussnivelingandeancondor-ryujin-itzy",
            "https://gfycat.com/newpitifulcockroach-ryujin-itzy",
            "https://gfycat.com/negligibleinformalhapuka-ryujin-itzy",
            "https://gfycat.com/vacantwillinggnat-ryujin-itzy",
            "https://gfycat.com/terrificjoyoushagfish-ryujin-itzy",
            "https://gfycat.com/negativedefenselessgalapagospenguin-beauty",
            "https://gfycat.com/orderlycluelessbats-ryujin-itzy",
            "https://gfycat.com/detailedartisticgoitered-ryujin",
            "https://gfycat.com/granularadorablekatydid-itzy",
            "https://gfycat.com/jubilantcharmingbunting-beauty",
            "https://gfycat.com/infamousdefinitivebudgie-ryujin-itzy",
            "https://gfycat.com/farflungcloseamazondolphin-ryujin-itzy",
            "https://gfycat.com/entireunfinishedcivet-ryujin-itzy",
            "https://gfycat.com/acidicwetarmyant-ryujin-itzy",
            "https://gfycat.com/shockinggrimafricanelephant-ryujin-itzy",
            "https://gfycat.com/adoreddrearybackswimmer-ryujin-itzy-wave",
            "https://gfycat.com/adolescentshinyhapuka-ryujin-itzy",
            "https://gfycat.com/ambitiousconcernedbagworm-beauty",
            "https://gfycat.com/meekdefiantherculesbeetle-ryujin-itzy",
            "https://gfycat.com/vigilantperiodiceel-ryujin-itzy",
            "https://gfycat.com/betterfairanophelesmosquito-ryujin-itzy",
            "https://gfycat.com/lightdevotedbison-ryujin-itzy",
            "https://gfycat.com/pleaseduniqueblackbuck",
            "https://gfycat.com/femaledrearykouprey-ryujin-itzy",
            "https://gfycat.com/friendlyvaguefrilledlizard-ryujin-itzy",
            "https://gfycat.com/generalphonycassowary-ryujin-itzy",
            "https://gfycat.com/grandioseellipticalleafbird-ryujin-itzy",
            "https://gfycat.com/granularpassionategalago-ryujin-itzy",
            "https://gfycat.com/granularmalefowl-ryujin-itzy",
            "https://gfycat.com/acidicwetarmyant-ryujin-itzy",
            "https://gfycat.com/beautifulwellmadedassie-chareyoung-minnie-ryujin-soojin-gidle",
            "https://gfycat.com/allsmuggalapagosalbatross-ryujin-itzy",
            "https://gfycat.com/bigheartedchiefeastsiberianlaika-ryujin-itzy",
            "https://gfycat.com/animatedcompetentarthropods-shin-ryujin-not-shy-itzy",
            "https://gfycat.com/flatbrieflemur-ryujin-itzy-wave",
            "https://gfycat.com/thoseflashybigmouthbass-ryujin-kpics-itzy",
            "https://gfycat.com/frenchheartydunnart-ryujin-itzy",
            "https://gfycat.com/handsomeadorablebinturong-shin-ryujin-not-shy-itzy",
            "https://gfycat.com/frigidcookedarmadillo-beauty",
            "https://gfycat.com/barrencompetentaustraliankelpie-ryujin-itzy",
            "https://gfycat.com/compassionateindolentamericancrow-itzy-pics-ryujin-oreo-beauty",
            "https://gfycat.com/concernedmetallicghostshrimp-ryujin-itzy",
            "https://gfycat.com/concernedagedhamadryad",
            "https://gfycat.com/blaringfatherlyapisdorsatalaboriosa-ryujin-itzy",
            "https://gfycat.com/artisticslimyibis",
            "https://gfycat.com/barrenkaleidoscopicicefish-ryujin-itzy",
            "https://gfycat.com/bowedclumsycheetah-ryujin-itzy",
            "https://gfycat.com/desertedspottedleafbird-beauty"]

        self.bot.itzy_chaeryeong_gif = ["https://tenor.com/view/itzy-chaeryeong-chaer-kpop-wannabe-gif-16689232",
            "https://tenor.com/view/chaeryeong-chaeryeong-itzy-lee-chaeryeong-gif-18568144",
            "https://tenor.com/view/chaeryeong-chaeryeong-itzy-itzy-gif-18553550",
            "https://tenor.com/view/chaeryeong-chaeryeong-itzy-itzy-chaeryeong-itzy-lee-chaeryeong-gif-13767624",
            "https://tenor.com/view/chaeryeong-chaeryeong-itzy-lee-chaeryeong-gif-18743380",
            "https://tenor.com/view/chaeryeong-chaeryeong-itzy-lee-chaeryeong-gif-18909774",
            "https://tenor.com/view/chaeryeong-chaeryeong-itzy-lee-chaeryeong-not-shy-gif-18568206",
            "https://media.discordapp.net/attachments/797701519582691369/804520744892497931/download-1.gif",
            "https://gfycat.com/klutzyunevengraywolf-chaeryeong-itzy",
            "https://gfycat.com/colossalimpishharpyeagle-chaeryeong-itzy",
            "https://gfycat.com/yellowdiscreteafricanpiedkingfisher-chaeryeong-itzy",
            "https://gfycat.com/yearlyangryblackbird-itzy",
            "https://gfycat.com/scarycookedankole-chaeryeong-itzy",
            "https://gfycat.com/disloyalwelltodohound",
            "https://gfycat.com/angryfatherlydegus-chaeryeong-itzy",
            "https://gfycat.com/commonbreakableafricanelephant-chaeryeong-itzy",
            "https://gfycat.com/crispgaseousgarpike-beauty",
            "https://gfycat.com/officialalienatedeuropeanpolecat-chaeryoung-itzy",
            "https://gfycat.com/boguscriminalharrier-chaeryeong-itzy",
            "https://gfycat.com/beneficialrashicefish-chaeryeong-itzy",
            "https://gfycat.com/celebratedsatisfiedballpython-chaeryeong-itzy",
            "https://gfycat.com/creativeelatedbichonfrise",
            "https://gfycat.com/creepyblaringagama",
            "https://gfycat.com/vainpeskychickadee-chaeryeong-itzy",
            "https://gfycat.com/delicioussnarlingcalf-chaeryeong-itzy",
            "https://gfycat.com/deadclevergoldenmantledgroundsquirrel-chaeryeong",
            "https://gfycat.com/achinggoldenguanaco-chaeryeong-itzy",
            "https://gfycat.com/diligentsophisticatedlarva-chaeryeong-itzy",
            "https://gfycat.com/costlyhairychafer-itzy",
            "https://gfycat.com/athletictimelyafricancivet-itzy-lia",
            "https://gfycat.com/brilliantharmlessjohndory-chaeryeong-itzy",
            "https://gfycat.com/enchantingthesehornedtoad-itzy",
            "https://gfycat.com/esteemedbackballpython-beauty",
            "https://gfycat.com/foolhardywillingcanvasback-chaeryeong-itzy",
            "https://gfycat.com/flickeringcomplexfrilledlizard-chaeryeong-itzy",
            "https://gfycat.com/giganticmemorablehammerheadshark-chaeryeong-itzy",
            "https://gfycat.com/glossybonygangesdolphin-beauty",
            "https://gfycat.com/freshcoarsecanadagoose-chaeryeong-itzy",
            "https://gfycat.com/barefrigidamurminnow-chaeryeong-itzy",
            "https://gfycat.com/bleaknauticalglowworm-chaeryeong-itzy",
            "https://gfycat.com/brightfirstdrongo-itzy-chaeryeong-korean-idol-kpop-lee",
            "https://gfycat.com/deadthankfulboutu-chaeryeong-mechabear-itzy-kpop",
            "https://gfycat.com/demandingclutteredkangaroo-chaeryeong-itzy",
            "https://gfycat.com/clutteredfavorabledairycow",
            "https://gfycat.com/failingblankeskimodog",
            "https://gfycat.com/fastlastinggalapagossealion-chaeryeong-itzy",
            "https://gfycat.com/firstaridape-beauty",
            "https://gfycat.com/apprehensivefemininehectorsdolphin-chaeryeong-itzy-cute-kpop",
            "https://gfycat.com/glisteningwindingclam-itzy",
            "https://gfycat.com/greatunfinisheddragon-chaeryeong-itzy",
            "https://gfycat.com/disfiguredaccurateafricangroundhornbill-chaeryeong-itzy",
            "https://gfycat.com/giganticcoolcaecilian-itzy",
            "https://gfycat.com/hugerealindianrockpython-chaeryeong-gidle-itzy",
            "https://gfycat.com/imaginaryanguishedequestrian-chaeryeong-itzy",
            "https://gfycat.com/frankunimportantgallinule-lee-chaeryeong-comeback-not-shy-midzy-itzy-kpop",
            "https://gfycat.com/ficklebelatedfallowdeer-chaeryeong-itzy",
            "https://gfycat.com/flatlastbluewhale-chaeryeong-adorable-cute-itzy-kpop",
            "https://gfycat.com/klutzykindheartedfallowdeer-beauty",
            "https://gfycat.com/fixedharshgraywolf-chaeryeong-itzy",
            "https://gfycat.com/beneficialrashicefish-chaeryeong-itzy",
            "https://gfycat.com/goodnaturedsecondamericanwirehair-chaeryeong-itzy",
            "https://gfycat.com/queasyscentedblackmamba-chaeryeong-itzy",
            "https://gfycat.com/rapidselfassuredakitainu-beauty",
            "https://gfycat.com/safearomaticgerenuk-beauty",
            "https://gfycat.com/uniformcleverkatydid-chaeryeong-itzy",
            "https://gfycat.com/vibrantwhitegrizzlybear-chaeryeong-adorable-cute-itzy-kpop",
            "https://gfycat.com/sentimentalglamoroushartebeest-sana-twice-kpop",
            "https://gfycat.com/odduntimelycorydorascatfish-chaeryeong-itzy",
            "https://gfycat.com/plaingoldenelectriceel-chaeryeong-itzy",
            "https://gfycat.com/scarcehastycanadagoose",
            "https://gfycat.com/carelesswellgroomedaffenpinscher-chaeryeong-itzy",
            "https://gfycat.com/enchantingthesehornedtoad-itzy",
            "https://gfycat.com/amazingsomegander",
            "https://gfycat.com/forsakentalkativecob-chaeryeong-itzy",
            "https://gfycat.com/hopefulmajorfrilledlizard-chaeryeong-itzy",
            "https://gfycat.com/icyfrequentagama-chaeryeong-itzy",
            "https://gfycat.com/ignorantunkemptbluemorphobutterfly-itzy-chaeryeong-idol-radio-kpop",
            "https://gfycat.com/ajaradoredhypsilophodon-chaeryeong-itzy",
            "https://gfycat.com/anyopenleafhopper-chaeryeong-itzy",
            "https://gfycat.com/frigidfrayedichthyosaurs-chaeryeong-tieriyon-cute-itzy-kpop",
            "https://gfycat.com/glummasculinebobolink",
            "https://gfycat.com/gloriouslawfulafricangoldencat-2tzy-hello-2021-chaeryeong-itzy-kpop",
            "https://gfycat.com/impishenormousarctichare-itzy-chaeryeong-gap-crush-kpop-idol",
            "https://gfycat.com/thirstydefiantdungenesscrab-chaeryeong-itzy",
            "https://gfycat.com/innocentfrenchcurlew",
            "https://gfycat.com/jaggedeminentadder",
            "https://gfycat.com/lastinglazyherring",
            "https://gfycat.com/rewardinginsistentarrowcrab-beauty",
            "https://gfycat.com/angelicdeliriousalbatross",
            "https://gfycat.com/ambitiousvibrantfunnelweaverspider"]

        self.bot.itzy_yuna_gif = ["https://tenor.com/view/yuna-yuna-itzy-itzy-yuna-shin-yuna-itzy-gif-13910454",
            "https://tenor.com/view/yuna-yuna-itzy-shin-yuna-gif-18719264",
            "https://tenor.com/view/yuna-shin-yuna-yuna-itzy-itzy-yuna-itzy-gif-13835000",
            "https://tenor.com/view/yuna-yuna-itzy-shin-yuna-gif-18829861",
            "https://tenor.com/view/yuna-shin-yuna-yuna-shin-gif-18387313",
            "https://tenor.com/view/itzy-yuna-gif-19088943",
            "https://tenor.com/view/yuna-gif-18390135",
            "https://gfycat.com/forsakeninbornflyinglemur-itzy-yuna",
            "https://gfycat.com/illustrioussoggygrub-itzy-yuna",
            "https://gfycat.com/gloomyweirdicefish-itzy",
            "https://gfycat.com/cleverhastyayeaye-itzy",
            "https://gfycat.com/blaringbiodegradablealbino-yuna",
            "https://gfycat.com/repentantnarroweuropeanpolecat-itzy",
            "https://gfycat.com/scarceblushingcrocodile-itzy-yuna",
            "https://gfycat.com/glumweecapybara-itzy-yuna",
            "https://gfycat.com/bogusweirdhoki-itzy-yuna",
            "https://gfycat.com/respectfuldescriptivegrayling-itzy-yuna",
            "https://gfycat.com/opulentuncomfortablehorse-itzy-yuna",
            "https://gfycat.com/meekexhaustedamericansaddlebred-itzy-yuna",
            "https://gfycat.com/snarlingsingleagama-itzy-yuna",
            "https://gfycat.com/abandonedsilkybassethound",
            "https://gfycat.com/acidicbestfrogmouth-itzy",
            "https://gfycat.com/agonizingfortunatehawk-itzy-kpop-yuna",
            "https://gfycat.com/demandingelderlyatlanticbluetang-itzy-yuna",
            "https://gfycat.com/feistyconcernedatlanticbluetang-itzy",
            "https://gfycat.com/angryofficialindigobunting",
            "https://gfycat.com/enchantedmajorkiskadee",
            "https://gfycat.com/agilebreakablebarasinga",
            "https://gfycat.com/thriftylavishbarasingha-itzy",
            "https://gfycat.com/identicalessentialcapeghostfrog-session-photo-itzy-yuna-kpop",
            "https://gfycat.com/slipperylinedafricanaugurbuzzard-beauty",
            "https://gfycat.com/keyfluffybassethound",
            "https://gfycat.com/deadyelloweeve",
            "https://gfycat.com/diligentbeneficialborderterrier-k-pop-mnet-mpd-aidol-empidi-kpab-m2-emnes-emtu",
            "https://gfycat.com/contentincomparableafricancivet-itzy",
            "https://gfycat.com/contentregalbluemorphobutterfly-itzy",
            "https://gfycat.com/crispvictoriousdowitcher",
            "https://gfycat.com/farthreadbaregordonsetter",
            "https://gfycat.com/imaginativecheerygalapagossealion",
            "https://gfycat.com/infantilecheerylaughingthrush",
            "https://gfycat.com/frankwildcorydorascatfish",
            "https://gfycat.com/onlygorgeousaxisdeer",
            "https://gfycat.com/ashamedunimportantblackrhino-itzy-yuna",
            "https://gfycat.com/detailedteeminggeese-elope",
            "https://gfycat.com/variablekinddipper",
            "https://gfycat.com/composedsoreakitainu-yuna-itzy-kpop",
            "https://gfycat.com/amazingquarterlybassethound",
            "https://gfycat.com/creamypalatablecorydorascatfish",
            "https://gfycat.com/disguisedfoolhardycuckoo",
            "https://gfycat.com/hotquaintguillemot",
            "https://gfycat.com/illfirsthandabalone-beauty",
            "https://gfycat.com/impolitetangangesdolphin",
            "https://gfycat.com/incrediblelikableapatosaur-yuna-itzy",
            "https://gfycat.com/needyslimydragon",
            "https://gfycat.com/parchedidleibis",
            "https://gfycat.com/polishedadoredinsect",
            "https://gfycat.com/pertinentessentialatlanticspadefish",
            "https://gfycat.com/likelydaringdorado",
            "https://gfycat.com/inferiortiredkoi",
            "https://gfycat.com/lavishvigorousaustraliancattledog",
            "https://gfycat.com/generouswebbedargali",
            "https://gfycat.com/illnaughtyelephantbeetle-itzy-issji-beauty",
            "https://gfycat.com/untriedsickatlasmoth",
            "https://gfycat.com/ancienthardcaterpillar-yuna-itzy",
            "https://gfycat.com/newuniqueblackandtancoonhound-yuna-itzy",
            "https://gfycat.com/gorgeousamazingisopod-190825-yuna-itzy",
            "https://gfycat.com/wavyunfinisheddodo-itzy-yuna",
            "https://gfycat.com/hilariousshorttermfairybluebird-celebrity-itzy-kpop-yuna-beauty",
            "https://gfycat.com/physicalcomfortableamericankestrel-yuna-itzy",
            "https://gfycat.com/quarterlypoorjay-yuna-itzy-kpop",
            "https://gfycat.com/disgustingnippybeardeddragon-elope",
            "https://gfycat.com/braveboringbluemorphobutterfly",
            "https://gfycat.com/gloomyunsteadyclownanemonefish-itzy-yuna",
            "https://gfycat.com/absoluteboringicefish"]

        self.bot.itzy_lia_gif = ["https://tenor.com/view/kpop-lia-strawberry-itzy-cute-gif-16770693",
            "https://tenor.com/view/lia-liaitzy-itzylia-itzy-gif-18066742",
            "https://tenor.com/view/lia-itzy-choi-jisu-pretty-model-gif-17200845",
            "https://tenor.com/view/itzy-lia-itzy-lia-kpop-cute-gif-17092840",
            "https://tenor.com/view/lia-liaitzy-itzylia-itzy-gif-18066804",
            "https://tenor.com/view/itzy-itzy-lia-lia-%EB%A6%AC%EC%95%84-%EC%9E%88%EC%A7%80-gif-18073067",
            "https://tenor.com/view/liaitzy-itzy-lia-gif-18066766",
            "https://gfycat.com/silkymadeupchrysomelid-itzy-lia",
            "https://gfycat.com/aptthankfulantarcticgiantpetrel-mechabear-kpop-itzy-lia",
            "https://gfycat.com/advancedoffensivecardinal-mechabear-kpop-itzy-lia",
            "https://gfycat.com/cheerfulpaleamericanbadger-mechabear-kpop-itzy-lia",
            "https://gfycat.com/vainvastivorybackedwoodswallow-itzy",
            "https://gfycat.com/bothorderlygermanshorthairedpointer",
            "https://gfycat.com/charmingdisfiguredgermanpinscher-mechabear-kpop-itzy",
            "https://gfycat.com/definitegloomylark",
            "https://gfycat.com/linearsoupyguppy",
            "https://gfycat.com/scornfulseveralfrenchbulldog",
            "https://gfycat.com/aggravatingplasticaracari-beauty",
            "https://gfycat.com/adoredlargedartfrog",
            "https://gfycat.com/accomplishedbewitchedbernesemountaindog",
            "https://gfycat.com/delectabledecimaldrake-beauty",
            "https://gfycat.com/opulentthisinsect",
            "https://gfycat.com/easygoinghalfgrunion-itzy-lia",
            "https://gfycat.com/enchantingjubilantgermanshorthairedpointer-itzy",
            "https://gfycat.com/sophisticatedagilecavy-itzy-kpop-lia",
            "https://gfycat.com/vastthankfularabianwildcat-itzy-kpop-lia",
            "https://gfycat.com/backchiefaustralianshelduck",
            "https://gfycat.com/confusedhonoredchital-itzy-lia-beauty",
            "https://gfycat.com/basicpasteladouri-itzy-lia",
            "https://gfycat.com/adventurousagilecrocodile-itzy-lia",
            "https://gfycat.com/disfiguredsleepyakitainu-itzy-lia",
            "https://gfycat.com/fatalembarrassedblobfish",
            "https://gfycat.com/waterywideleopard-itzy-lia",
            "https://gfycat.com/dismalcompassionatefeline-mechabear-itzy-kpop-lia",
            "https://gfycat.com/livefloweryelephantseal-itzy-lia",
            "https://gfycat.com/nauticalhomelyhydra-itzy-lia",
            "https://gfycat.com/meandistantbluegill-choi-jisu-comeback-not-shy-midzy-itzy-kpop-lia",
            "https://gfycat.com/onlyphysicalbluebottlejellyfish",
            "https://gfycat.com/snarlinglightheartedblackpanther",
            "https://gfycat.com/peskygracefulbernesemountaindog",
            "https://gfycat.com/discretebasicchihuahua-itzy-kpop-lia",
            "https://gfycat.com/blissfulkeyblobfish-itzy-lia",
            "https://gfycat.com/tensefarawayflatfish-itzy-lia",
            "https://gfycat.com/welltodomemorablehare-itzy-lia",
            "https://gfycat.com/untidyfearfulazurewingedmagpie-itzy-lia",
            "https://gfycat.com/chiefsmugaardwolf-itzy-lia",
            "https://gfycat.com/coarsegoodasianelephant-itzy-lia",
            "https://gfycat.com/costlylastbumblebee-itzy-lia",
            "https://gfycat.com/misguidedagedhartebeest-itzy-lia",
            "https://gfycat.com/regalwindyimperialeagle-itzy-lia",
            "https://gfycat.com/poisedfalsecoral-fancam-k-pop-mnet-itzy-mpd-lia-aidol-empidi",
            "https://gfycat.com/unhappygentlekid-dalla-dalla-itzy-kpop-lia",
            "https://gfycat.com/apprehensivephysicalfattaileddunnart-wannabe-fancam-itzy-kpop-lia",
            "https://gfycat.com/carelessboringafricanpiedkingfisher-itzy",
            "https://gfycat.com/politewelloffbonobo",
            "https://gfycat.com/disguisedgreatkoala-itzy-lia",
            "https://gfycat.com/elatedpossiblehomalocephale-itzy-lia",
            "https://gfycat.com/fabulousquaintannashummingbird-itzy-lia",
            "https://gfycat.com/evilcloudykiwi-itzy-lia",
            "https://gfycat.com/exhaustedyearlygalapagoshawk-itzy-lia",
            "https://gfycat.com/fewcarefreehoiho-cute-itzy-kpop-hot-lia-beauty",
            "https://gfycat.com/cooperativenarrowgnat-itzy-lia",
            "https://gfycat.com/flakygloriousantbear-itzy-lia",
            "https://gfycat.com/firstshabbyguernseycow-itzy-lia",
            "https://gfycat.com/flamboyantslipperydowitcher-beauty",
            "https://gfycat.com/frequentsomberinsect",
            "https://gfycat.com/creepyacrobaticcob-itzy-lia"]

    @commands.command()
    async def itzy(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Itzy {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "yeji":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yeji :heart:')
                await ctx.send(random.choice(self.bot.itzy_yeji_gif))
                await ctx.message.delete()
        elif arg == "ryujin":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Ryujin :heart:')
                await ctx.send(random.choice(self.bot.itzy_ryujin_gif))
                await ctx.message.delete()
        elif arg == "chaeryeong":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chaeryeong :heart:')
                await ctx.send(random.choice(self.bot.itzy_chaeryeong_gif))
                await ctx.message.delete()
        elif arg == "yuna":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yuna :heart:')
                await ctx.send(random.choice(self.bot.itzy_yuna_gif))
                await ctx.message.delete()
        elif arg == "lia":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Lia :heart:')
                await ctx.send(random.choice(self.bot.itzy_lia_gif))
                await ctx.message.delete()

def setup(client):
    client.add_cog(ItzyPings(client))