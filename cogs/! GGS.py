import discord, random, datetime
from discord.ext import commands
from datetime import datetime

        #= Dreamcatcher

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

#//people
k8 = 2

class GGS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bot.logs = 786515662214397973
    #. apink
        self.bot.apink_bomi_gif = ["https://tenor.com/view/yoon-bomi-one-one-more-time-chance-again-gif-13724908",
            "https://tenor.com/view/yoon-bomi-play-recorder-musical-instrument-flutes-gif-11868145",
            "https://tenor.com/view/thanks-thank-you-apink-bomi-yoon-gif-9243373",
            "https://tenor.com/view/bomi-apink-bomi-apink-bomi-apink-im-so-sick-im-so-sick-gif-14772262"]

        self.bot.apink_chorong_gif = ["https://tenor.com/view/chorong-gif-7780924",
            "https://tenor.com/view/nevermind-thegodbomi-chorong-apink-laughs-gif-20131482"]
        
        self.bot.apink_eunji_gif = ["https://tenor.com/view/apink-girl-group-sing-music-kpop-gif-5669042",
            "https://tenor.com/view/apink-eunji-gif-18881050",
            "https://cdn.discordapp.com/attachments/800205891365371915/808932802892005396/eunji_1.gif",
            "https://cdn.discordapp.com/attachments/800205891365371915/808932957683318804/eunji_2.gif",
            "https://giphy.com/gifs/0vFsUFprMMN3SodOCn",
            "https://tenor.com/view/apink-girl-group-sing-music-kpop-gif-5669042",
            "https://tenor.com/view/apink-eunji-gif-18881046"]

        self.bot.apink_hayoung_gif = ["https://tenor.com/view/hayoung-shrug-idgaf-not-my-problem-not-my-business-gif-10589324",
            "https://tenor.com/view/hayoung-apink-hayoung-apink-gif-18814544"]

        self.bot.apink_naeun_gif = ["https://tenor.com/view/naeun-apink-gif-18574437",
            "https://tenor.com/view/apink-son-naeun-nhicatung-kpop-korean-gif-5486987"]

        self.bot.apink_namjoo_gif = ["https://tenor.com/view/apink-kim-namjoo-k-pop-korean-gif-10024790",
            "https://tenor.com/view/namjoo-apink-oop-and-i-oop-namjoo-cover-mouth-gif-19379187"]
    #. dreamcatcher
        self.bot.dreamcatcher_jiu_gif = ["https://tenor.com/view/onex-1x-jiu-hawt-kim-minji-hawt-jiu-gif-18812596",
            "https://cdn.discordapp.com/attachments/771238115255255060/785294061996605470/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/785294063871721472/image3.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506214181896230/FreshAnimatedGrizzlybear-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506140445114408/9060e6f5755986b8bad6707d28f55649.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800508431282470952/original_4.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800509445779882014/MediocreNegligibleBlacknorwegianelkhound-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800509989127061544/o6MpBX.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513124603920414/BossyForkedCreature-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513181625352192/tenor_10.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513274918469662/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513325955284992/e2b8b6fa04a1bf097c86b109517b57eb782bfdc9_hq.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513381790515210/c4ac99d86111b96375050c1677352adaf58e39ff.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513440396869652/NauticalGranularBufeo-small.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513493702541323/original_1.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513585008214026/tenor_8.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513755678900224/tumblr_a357a008e837857bf59e87b82d20876b_21f50875_250.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513826377695262/tumblr_061717b27912f6ef3d1a15c86aea2f54_8b77746a_540.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513877405073438/tenor-2.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513938458542110/tumblr_op8ssqIAi81tmc4fuo1_400.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800514030656553000/tumblr_okcn65yiNA1ue8w9eo1_400.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800514172197666856/a809c032f560b7c8563bdf59d6dcac1d9eb3bb91.gif"]

        self.bot.dreamcatcher_dami_gif = ["https://tenor.com/view/dreamcatcher-%EB%93%9C%EB%A6%BC%EC%BA%90%EC%B3%90-dami-cute-dance-gif-12255241",
            "https://tenor.com/view/dami-dreamcatcher-dcboca-gif-18178539",
            "https://tenor.com/view/dreamcatcher-dami-gif-18622933",
            "https://tenor.com/view/dreamcatcher-dami-full-moon-dreamcatcher-dami-arrow-gif-18971647",
            "https://tenor.com/view/lee-yubin-dami-dreamcatcher-meemoy-boca-gif-18893268",
            "https://tenor.com/view/dami-zombie-dreamcatcher-lee-yubin-boca-gif-18882718",
            "https://tenor.com/view/dami-dreamcatcher-boca-dc-dcboca-gif-18201110",
            "https://tenor.com/view/dreamcatcher-cute-yoohyeon-dami-gif-12143809",
            "https://tenor.com/view/dami-kwave-sexy-dance-dreamcatcher-gif-12249892",
            "https://tenor.com/view/dami-dami-dreamcatcher-dreamcatcher-dance-gif-13832007",
            "https://tenor.com/view/dreamcatcher-dami-lee-yoobin-kpop-pretty-gif-15563905",
            "https://tenor.com/view/dami-dami-dreamcatcher-dreamcatcher-cute-smile-gif-13831991",
            "https://tenor.com/view/dreamcatcher-dami-lee-yubin-main-rapper-lead-dancer-gif-17558548",
            "https://tenor.com/view/dami-dami-dreamcatcher-dreamcatcher-sexy-dance-gif-13832025",
            "https://tenor.com/view/dami-dreamcatcher-boca-dcboca-dc-gif-18229330",
            "https://tenor.com/view/dreamcatcher-su-a-kim-bora-dami-havana-gif-12130542",
            "https://tenor.com/view/dreamcatcher-su-a-kim-bora-dami-havana-gif-12130543",
            "https://tenor.com/view/dream-catcher-kpop-girl-group-piri-insomnia-gif-16831355",
            "https://tenor.com/view/king-kong-dreamcatcher-dami-lee-yubin-main-rapper-gif-15879177",
            "https://tenor.com/view/kpop-dream-catcher-dami-chewing-gif-15563908",
            "https://tenor.com/view/dreamcatcher-dami-lee-yoobin-kpop-pretty-gif-15563904",
            "https://tenor.com/view/dream-catcher-lee-yubin-cute-dami-kpop-gif-17900509",
            "https://tenor.com/view/dami-dream-catcher-cute-wave-kpop-gif-15515589",
            "https://tenor.com/view/dami-dreamcatcher-smile-happy-cute-gif-11972846",
            "https://tenor.com/view/dami-dreamcatcher-boca-dcboca-kpop-gif-18229558",
            "https://tenor.com/view/dami-dreamcatcher-boca-dcboca-kpop-gif-18229536",
            "https://tenor.com/view/dreamcatcher-dami-lee-yubin-main-rapper-lead-dancer-gif-17720409",
            "https://tenor.com/view/dreamcatcher-dami-lee-yubin-kpop-pretty-gif-15811393",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507388138094592/e1f635f10fdd9ee970a96f767392a0ee.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800509691888533565/e9e4ab22e4b8f52a38d5981b1b75ffc6.gif",
            "https://cdn.discordapp.com/attachments/795581963229462538/800511798431449099/50a753848cc3ebb4400b78043bca728801d1969b_hq.gif"]

        self.bot.dreamcatcher_gahyeon_gif = ["https://tenor.com/view/onex-1x-dreamcatcher-dreamcatcher-gahyeon-gahyeon-kiss-gif-18704085",
            "https://cdn.discordapp.com/attachments/795584752127311873/800511696837148692/0cabae4a0b98cd2e26eb345427b06a71.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800511398278725642/6de9c8d3afbd2726b0704a564872a2cb520f06c1.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800511277725646858/025260ecb02d38a465081e352ab48905.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800511176147730432/20145a59ad912ee0cd1953c7f30e527045c811f4r1-744-412_hq.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800510635116724254/AllDisfiguredAlaskanhusky-max-1mb.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800510565239881768/ggulbest_41-38.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800510489813712966/603ec6f2b5c15b1ea58f10f1b143c22a.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800510418731794472/YearlyGlumDeviltasmanian-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800510369445183528/151adfdb7d9eea18650426598180.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800510323903299604/original_2.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800509989127061544/o6MpBX.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800509840983851028/tenor_6.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800509691888533565/e9e4ab22e4b8f52a38d5981b1b75ffc6.gif"]

        self.bot.dreamcatcher_handong_gif = ["https://tenor.com/view/dreamcatcher-handong-gif-18881069",
            "https://cdn.discordapp.com/attachments/795585170974834728/800503987455524914/97ebb09a06e49b03cd687ede3b1f5d0e.gif",
            "https://cdn.discordapp.com/attachments/795584572405317683/800512953438830602/tumblr_omnvp00YI21vc5dxto1_500.gif",
            "https://tenor.com/view/handong-dreamcatcher-yoohyeon-hug-handong-dreamcatcher-gif-19121213",
            "https://tenor.com/view/handong-dreamcatcher-dreamcatcher-handong-gif-14876335",
            "https://tenor.com/view/handong-dreamcatcher-performance-dance-kpop-gif-17568347",
            "https://tenor.com/view/dream-catcher-handong-kpop-dongie-pose-gif-17305836"]

        self.bot.dreamcatcher_siyeon_gif = ["https://tenor.com/view/dreamcatcher-siyeon-lee-siyeon-vocalist-kpop-gif-17254566",
            "https://cdn.discordapp.com/attachments/786714676506394654/800514172197666856/a809c032f560b7c8563bdf59d6dcac1d9eb3bb91.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800509445779882014/MediocreNegligibleBlacknorwegianelkhound-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506038264397824/eff2cf3317f8af127c647b7b91ec5f80a5eb3841.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800508665831620668/rep.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800508431282470952/original_4.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800508354044755988/AmusingNippyAyeaye-max-1mb.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800508225841659904/7e8de75c4c5329438fefe0c193b8043c.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800508154046578698/PleasantShyAnemonecrab-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507793970692156/GlisteningDentalAkitainu-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507737543802900/FarflungFantasticAfricanmolesnake-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507691516559380/tumblr_460bb80ebf2bb74f682300bffc29296b_9098afbc_400.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507636205486080/tumblr_ec92eca1315fc072017cb3a1de5c73ba_11b40bd2_500.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507591414382612/def0b0bac64dd7cc446e494acf83c758.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507553628028928/c4aa723c71b44cf7b2274b75597e42c7.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507503959212082/3b4e993c34068851caa30282abd68740.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507388138094592/e1f635f10fdd9ee970a96f767392a0ee.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507323546075167/tumblr_pz298hlbDc1rqb6hgo4_400.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800507255593762819/b4de5eed6d285cf70435b46dc43f2761.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506140445114408/9060e6f5755986b8bad6707d28f55649.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506214181896230/FreshAnimatedGrizzlybear-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505747473301554/dreamcatcher-really-really-gif.gif"]

        self.bot.dreamcatcher_sua_gif = ["https://tenor.com/view/dreamcatcher-dreamcatcher-sua-sua-sua-funny-look-around-gif-19331893",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505148002402344/7eae1402c662ce572a78374227c36adbd0cd2bea.gif",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505310154063902/7d415f7c8e7591afd7811dc050dd1307.gif",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505362964545556/fb621cde8599cbe403bb7805cd76ed2c4468c26e_hq.gif",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505451984715807/0c2ba2e5eb17280c29f3baaad6efd557e589ed20_00.gif",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505541452627998/98e8162b6405ba504659e3bb934306d1cb69612d.gif",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505698009481216/dd01008a098143dbd16761cdf736bd1b.gif",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505747473301554/dreamcatcher-really-really-gif.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800508225841659904/7e8de75c4c5329438fefe0c193b8043c.gif",
            "https://cdn.discordapp.com/attachments/795584572405317683/800512953438830602/tumblr_omnvp00YI21vc5dxto1_500.gif",
            "https://cdn.discordapp.com/attachments/786714676506394654/800514172197666856/a809c032f560b7c8563bdf59d6dcac1d9eb3bb91.gif",
            "https://tenor.com/view/dreamcatcher-%EB%93%9C%EB%A6%BC%EC%BA%90%EC%B3%90-sua-dance-gif-12255205",
            "https://tenor.com/view/%EB%93%9C%EB%A6%BC%EC%BA%90%EC%B3%90-dreamcatcher-sua-kim-bora-gif-19962764",
            "https://tenor.com/view/dreamcatcher-sua-happy-smile-cheer-gif-19961384",
            "https://tenor.com/view/dreamcatcher-sua-shake-smile-gif-18573306",
            "https://tenor.com/view/dreamcatcher-sua-dance-dancing-gif-18573310",
            "https://tenor.com/view/dreamcatcher-sua-gif-18981876",
            "https://tenor.com/view/dreamcatcher-sua-angry-cloverfield-found-footage-gif-18573314",
            "https://tenor.com/view/dreamcatcher-sua-ji-u-annoyed-smile-gif-18573311"]

        self.bot.dreamcatcher_yoohyeon_gif = ["https://tenor.com/view/yoohyeon-dream-catcher-heart-shape-cute-kpop-gif-16952098",
            "https://tenor.com/view/yoohyeon-in-fear-yoohyeon-kim-yoohyeon-dreamcatcher-yoohyeon-dreamcatcher-gif-19500039",
            "https://cdn.discordapp.com/attachments/786714676506394654/800513181625352192/tenor_10.gif",
            "https://cdn.discordapp.com/attachments/795584752127311873/800510418731794472/YearlyGlumDeviltasmanian-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585001663365130/800509445779882014/MediocreNegligibleBlacknorwegianelkhound-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585074450923530/800505747473301554/dreamcatcher-really-really-gif.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506297907806219/tumblr_p8ib2x5eOu1rqb6hgo1_r1_500.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506214181896230/FreshAnimatedGrizzlybear-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506140445114408/9060e6f5755986b8bad6707d28f55649.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800506038264397824/eff2cf3317f8af127c647b7b91ec5f80a5eb3841.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800505015278108672/Yoohyeon-Yoohyeon-in-2019-Dream-catcher-Girl-group-.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800504883765444659/The-DreamCatcher-Thread-InJapan-Page-1624-Groups-.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800504782334853150/ggulbest_38-33.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800504671268503572/Dreamcatcher-Gif-Thread_-e_oeeSzes_el-allkpop-Forums.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800504561776984114/ba7019804d112e6e649bac4c09c09dbf.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800504498493325372/b7f7cebe82b631415bc3c4d2b6e14c38.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800504277146796103/77ac81500e0bf2af4bfcd472adb00763.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800504188906897418/AliveTotalIbadanmalimbe-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/795585170974834728/800503987455524914/97ebb09a06e49b03cd687ede3b1f5d0e.gif"]
    #. weki meki
        self.bot.wekimeki_doyeon_gif = ["https://tenor.com/view/doyeon-wekimeki-gif-18867883",
            "https://cdn.discordapp.com/attachments/800224052312277003/800555413023752212/45071c5422735c1e97f162ec1cf15cbf.gif",
            "https://tenor.com/view/doyeon-wekimeki-gif-18867880",
            "https://tenor.com/view/cover-eyes-kim-doyeon-doyeon-weki-meki-kpop-gif-17688928",
            "https://tenor.com/view/doyeon-cry-produce101-hurt-kpop-gif-10276415",
            "https://tenor.com/view/kim-doyeon-hair-flip-ioi-flirt-smile-gif-9869521",
            "https://tenor.com/view/kpop-dazzle-weki-meki-kim-doyeon-music-video-gif-16419083",
            "https://tenor.com/view/kim-doyeon-gif-19253844",
            "https://tenor.com/view/doyeon-kim-doyeon-weki-meki-weki-meki-doyeon-doyeon-weki-meki-gif-20108425",
            "https://tenor.com/view/doyeon-gif-9952856",
            "https://tenor.com/view/%EA%B9%80%EB%8F%84%EC%97%B0-gif-18181702",
            "https://tenor.com/view/doyeon-wekimeki-cool-gif-18963359",
            "https://tenor.com/view/wekimeki-doyeon-gif-18847477",
            "https://tenor.com/view/wekimeki-doyeon-gif-18847492",
            "https://tenor.com/view/wekimeki-doyeon-gif-18908062",
            "https://tenor.com/view/doyeon-wekimeki-cool-gif-18963344",
            "https://tenor.com/view/doyeon-wekimeki-gif-10344450",
            "https://tenor.com/view/doyeon-wekimeki-gif-10344452",
            "https://tenor.com/view/doyeon-kim-wekimeki-gif-20189589",
            "https://tenor.com/view/doyeon-wekimeki-gif-18867880",
            "https://tenor.com/view/wekimeki-doyeon-tongue-gif-19035974",
            "https://tenor.com/view/doyeon-kim-wekimeki-gif-20189587"]

        self.bot.wekimeki_elly_gif = ["https://tenor.com/view/elly-weki-meki-heart-gif-14294213",
            "https://cdn.discordapp.com/attachments/800224106384982027/800557668783357962/original.gif",
            "https://cdn.discordapp.com/attachments/800224106384982027/800567657220931645/tumblr_4d924f0ebbeed200cd494b3a3fb9fb57_da9d32c0_400.gif",
            "https://tenor.com/view/elly-weki-meki-oopsy-kpop-mv-gif-17589261",
            "https://tenor.com/view/elly-haerim-hi-hello-wave-gif-16426946",
            "https://gfycat.com/DisguisedKindlyHedgehog",
            "https://gfycat.com/UnrulyMiserableHake"]

        self.bot.wekimeki_lua_gif = ["https://cdn.discordapp.com/attachments/800224194482274345/801694025346187274/original_1.gif",
            "https://cdn.discordapp.com/attachments/800224194482274345/800560199026606100/7a212bf86037a492f5355889a2441032.gif",
            "https://gfycat.com/DeafeningSillyCanadagoose",
            "https://tenor.com/view/birthday-flowers-hair-green-kpop-gif-18736777",
            "https://tenor.com/view/lua-weki-meki-girl-kpop-music-video-gif-17688814",
            "https://tenor.com/view/kpop-dazzle-weki-meki-lua-cute-gif-16419326",
            "https://tenor.com/view/kpop-dazzle-weki-meki-dance-gif-16912848",
            "https://gfycat.com/AshamedGreedyJanenschia",
            "https://cdn.discordapp.com/attachments/800224194482274345/801700137004564481/giphy.gif"]

        self.bot.wekimeki_lucy_gif = ["https://gfycat.com/alarmedclutteredbobwhite",
            "https://cdn.discordapp.com/attachments/800224232759754772/800562065613914152/tenor.gif",
            "https://tenor.com/view/kpop-oopsy-weki-meki-lucy-music-video-gif-17518247",
            "https://gfycat.com/advancedplainfalcon-weki-meki-noh-lucy",
            "https://cdn.discordapp.com/attachments/800224232759754772/801697123807526912/NastyMisguidedClownanemonefish-max-1mb.gif",
            "https://tenor.com/view/wekimeki-lucy-cool-gif-18868364",
            "https://cdn.discordapp.com/attachments/800224232759754772/801698382091124776/tumblr_p4eoesUwmM1wisj25o3_540.gif",
            "https://gfycat.com/confuseddependableconch-mechabear-weki-meki-kpop-lucy"]

        self.bot.wekimeki_rina_gif = ["https://tenor.com/view/rina-weki-meki-kpop-gif-14709543",
            "https://cdn.discordapp.com/attachments/800224289810677821/800562573548191744/dd1e1c2491e3eb9d912ccd214e33145c.gif",
            "https://tenor.com/view/rina-weki-meki-idol-kpop-gif-14916651",
            "https://tenor.com/view/rina-weki-meki-kpop-cute-pretty-gif-15735688",
            "https://tenor.com/view/rina-weki-meki-kpop-cute-gif-16587745",
            "https://tenor.com/view/rina-weki-meki-kpop-fierce-gif-15517942",
            "https://gfycat.com/AdolescentPinkBug",
            "https://tenor.com/view/rina-weki-meki-kpop-gif-18219670",
            "https://gfycat.com/AgileGiddyIberiannase"]

        self.bot.wekimeki_sei_gif = ["https://tenor.com/view/wekimeki-sei-gif-18891261",
            "https://tenor.com/view/wekimeki-sei-gif-18891289",
            "https://tenor.com/view/wekimeki-sei-gif-19169813",
            "https://tenor.com/view/weki-meki-sei-weki-meki-sei-sei-weki-meki-my-beloved-gif-19859712",
            "https://tenor.com/view/sei-tiki-taka-choreography-weki-meki-dance-gif-15955302",
            "https://tenor.com/view/kpop-sei-diamond-dazzle-weki-meki-gif-16418938",
            "https://cdn.discordapp.com/attachments/800224316888973312/800574717760634950/c3498028cb5f5671e98f8212ca00bc33.gif",
            "https://cdn.discordapp.com/attachments/800224316888973312/800562983633027122/tenor-1.gif",
            "https://gfycat.com/DiscreteGrimyCurassow",
            "https://gfycat.com/DefiniteGraveHarrier",
            "https://gfycat.com/TatteredGregariousFlyingfox",
            "https://gfycat.com/ClutteredNeighboringAlabamamapturtle",
            "https://gfycat.com/MisguidedRichGangesdolphin"]

        self.bot.wekimeki_suyeon_gif = ["https://tenor.com/view/wave-hi-hello-kpop-happy-gif-16968572",
            "https://tenor.com/view/kpop-crush-suyeon-weki-meki-music-video-gif-16268466",
            "https://tenor.com/view/surprised-oopsy-oops-oopsie-weki-meki-gif-18170395",
            "https://tenor.com/view/kpop-weki-meki-suyeon-ji-suyeon-weki-meki-suyeon-gif-18712771",
            "https://cdn.discordapp.com/attachments/800224361935274004/800565729052459098/4e45b67529977ec2941e3c3dcd853ec6.gif",
            "https://giphy.com/gifs/KPopSource-mv-weki-meki-oopsy-ZD23n6SRWsI9jUHGeq"]

        self.bot.wekimeki_yoojung_gif = ["https://tenor.com/view/yoojung-choi-yoodaeng-daeng-choiyoojung-gif-19404386",
            "https://tenor.com/view/umm-um-yoojung-gif-8099931",
            "https://tenor.com/view/yoojung-choiyoojung-weki-meki-love-heart-gif-13589327",
            "https://tenor.com/view/choi-yoojung-yoodaeng-weki-meki-cute-baby-gif-13444237",
            "https://gfycat.com/WeepyCleverKakarikis",
            "https://cdn.discordapp.com/attachments/800224391258439721/800565546701160458/f1fc5f292c3132ff952b3b50e952698b.gif",
            "https://tenor.com/view/weki-meki-yoojung-choi-yoo-jung-gif-18765076",
            "https://giphy.com/gifs/KPopSource-mv-weki-meki-oopsy-XGaOrWHVVR669VXprf",
            "https://tenor.com/view/choiyoojung-wekimeki-gif-13666421"]
    #. wjsn
        self.bot.wjsn_bona_gif = ["https://tenor.com/view/wjsn-bona-heart-gif-9368960",
            "https://tenor.com/view/wjsn-bona-gif-9369544",
            "https://tenor.com/view/wjsn-bona-gif-9369542",
            "https://tenor.com/view/wjsn-bona-gif-9369548",
            "https://tenor.com/view/bona-wjsn-cute-heart-gif-14540847",
            "https://tenor.com/view/wjsn-bona-gif-9368967",
            "https://tenor.com/view/wjsn-bona-gif-9369345",
            "https://tenor.com/view/kpop-wjsn-cosmic-girls-eating-bona-gif-18586148"]

        self.bot.wjsn_cheng_xiao_gif = ["https://tenor.com/view/surprised-shocked-cheng-xiao-gif-12031984",
            "https://tenor.com/view/cheng-xiao-heart-heart-shape-love-shape-gif-12031978",
            "https://tenor.com/view/cheng-xiao-not-bad-good-gif-12031989",
            "https://tenor.com/view/cheng-xiao-wjsn-gif-5896151",
            "https://tenor.com/view/chengxiao-cheng-xiao-wjsn-cosmic-gif-5176863",
            "https://tenor.com/view/cheng-xiao-wjsn-gif-19293644",
            "https://tenor.com/view/cheng-xiao-wjsn-gif-5896142",
            "https://tenor.com/view/cheng-xiao-wjsn-jump-flip-gif-5896127",
            "https://tenor.com/view/cheng-xiao-wjsn-wink-gif-5896145",
            "https://tenor.com/view/chengxiao-cheng-xiao-wjsn-cosmicgirls-gif-10710829"]

        self.bot.wjsn_dawon_gif = ["https://tenor.com/view/dawon-you-wjsn-pointing-akorp-gif-10023897",
            "https://tenor.com/view/kpop-wjsn-cosmic-girls-dawon-gif-18585918",
            "https://tenor.com/view/kpop-wjsn-cosmic-girls-dawon-heart-gif-18585940",
            "https://tenor.com/view/dawon-wjsn-cosmic-girls-cosmic-girls-gif-9760986",
            "https://tenor.com/view/kpop-wjsn-cosmic-girls-dawon-gif-18585910"]

        self.bot.wjsn_dayoung_gif = ["https://tenor.com/view/im-dayoung-dayoung-wjsn-cosmic-girls-gif-14794012",
            "https://tenor.com/view/im-dayoung-dayoung-wjsn-cosmic-girls-gif-14794019",
            "https://tenor.com/view/im-dayoung-dayoung-wjsn-cosmic-girls-gif-14794050",
            "https://tenor.com/view/im-dayoung-dayoung-wjsn-cosmic-girls-gif-14799931",
            "https://tenor.com/view/im-dayoung-dayoung-wjsn-cosmic-girls-gif-14794023",
            "https://tenor.com/view/im-dayoung-dayoung-wjsn-cosmic-girls-gif-14794085"]

        self.bot.wjsn_eunseo_gif = ["https://tenor.com/view/wjsn-cosmic-girls-eunseo-gif-18627810",
            "https://tenor.com/view/wjsn-cosmic-girls-kpop-eunseo-bunny-gif-18627757",
            "https://tenor.com/view/wjsn-cosmic-girls-eunseo-gif-18627819",
            "https://tenor.com/view/kpop-wjsn-cosmic-girls-eunseo-kiss-gif-18628222",
            "https://tenor.com/view/wjsn-wjsn-eunseo-eunseo-eunseo-butterfly-wjsn-eunseo-butterfly-gif-17455382"]

        self.bot.wjsn_exy_gif = ["https://tenor.com/view/exy-wjsn-kpop-cosmic-girls-kiss-gif-17356005",
            "https://tenor.com/view/exy-wjsn-kpop-cosmic-girls-good-job-gif-17356001",
            "https://tenor.com/view/yukziu-wjsn-exy-gif-19126649",
            "https://tenor.com/view/wjsn-cosmic-girls-exy-cute-gif-15481223",
            "https://tenor.com/view/wjsn-cosmic-girls-exy-chu-so-jung-kpop-gif-15479801"]

        self.bot.wjsn_luda_gif = ["https://tenor.com/view/luda-wjsn-gif-18881057",
            "https://tenor.com/view/luda-wjsn-cosmic-girls-cosmic-girls-gif-9534362",
            "https://tenor.com/view/luda-wink-wjsn-kpop-gif-14322078",
            "https://tenor.com/view/luda-witch-spell-cute-wjsn-gif-19920488",
            "https://tenor.com/view/luda-wjsn-gif-18881052"]

        self.bot.wjsn_seola_gif = ["https://tenor.com/view/wjsn-seola-cosmicgirls-kpop-gif-7837800",
            "https://tenor.com/view/kpop-wjsn-seola-heart-love-gif-18585890",
            "https://tenor.com/view/wjsn-seola-cosmicgirls-kpop-gif-7837797",
            "https://tenor.com/view/wjsn-seola-cosmicgirls-luda-exy-gif-7962940"]

        self.bot.wjsn_soobin_gif = ["https://tenor.com/view/soobin-wjsn-k-pop-korean-gif-9989530",
            "https://tenor.com/view/kpop-cosmic-girls-wjsn-soobin-gif-18586007",
            "https://tenor.com/view/kpop-cosmic-girls-wjsn-soobin-gif-18586011",
            "https://tenor.com/view/wjsn-cosmic-girls-kpop-soobin-kiss-gif-18586034",
            "https://tenor.com/view/wjsn-cosmic-girls-kpop-soobin-gif-18586040"]

        self.bot.wjsn_yeonjung_gif = ["https://tenor.com/view/yeonjung-cosmic-girls-wjsn-ioi-produce-gif-9932084",
            "https://tenor.com/view/kcon2019japan-kcon-%EC%BC%80%EC%9D%B4%EC%BD%98-singing-high-note-gif-14562921",
            "https://tenor.com/view/%EC%9A%B0%EC%A3%BC%EC%86%8C%EB%85%80-%EC%9C%A0%EC%97%B0%EC%A0%95-%EC%97%B0%EC%A0%95-stare-serious-gif-15594348",
            "https://gfycat.com/shamefulthoughtfulappaloosa-wjsn-yeonjung-beauty",
            "https://thumbs.gfycat.com/FarawayWeakKatydid-mobile.mp4",
            "https://64.media.tumblr.com/e661656f4c0a69df2a743de2746b4582/71a9721563887da6-59/s400x600/ea04cfe446f86cea085c362cd095f490e7d6f94e.gif"]

        self.bot.wjsn_yeoreum_gif = ["https://tenor.com/view/yeoreum-wjsn-gif-18828859",
            "https://tenor.com/view/yeoreum-wjsn-gif-19302984",
            "https://tenor.com/view/wjsn-la-la-love-yeoreum-lee-yeoreum-dancing-gif-17952511",
            "https://tenor.com/view/%EC%97%AC%EB%A6%84-%EC%9D%B4%EC%97%AC%EB%A6%84-yorm-wjsn-yeoreum-gif-19970067",
            "https://tenor.com/view/wjsn-yeoreum-gif-18829843"]

        self.bot.wjsn_mei_qi_gif = ["https://tenor.com/view/meng-mei-qi-cell-phone-cry-call-hold-back-tears-gif-11918655",
            "https://tenor.com/view/meiqi-laughing-wjsn-lmao-lol-gif-10022964",
            "https://tenor.com/view/meng-meiqi-%E7%81%AB%E7%AE%AD%E5%B0%91%E5%A5%B3101-rocket-girls-gif-19971810",
            "https://tenor.com/view/meng-meiqi-%E7%81%AB%E7%AE%AD%E5%B0%91%E5%A5%B3101-hjsn-gif-19971908",
            "https://tenor.com/view/meng-mei-qi-come-on-lets-party-wink-gif-11918640"]

        self.bot.wjsn_xuan_yi_gif = ["https://tenor.com/view/kpop-wjsn-cosmic-girls-xuan-yi-gif-19038371",
            "https://tenor.com/view/kpop-wjsn-cosmic-girls-xuan-yi-kiss-gif-19038397",
            "https://tenor.com/view/xuanyi-wjsn-cosmic-girls-gif-10949761",
            "https://tenor.com/view/xuanyi-cosmic-girls-wjsn-gif-10304350",
            "https://tenor.com/view/xuan-yi-wjsn-k-pop-cosmic-girls-gif-11474789"]
    #. end of gifs

    @commands.command()
    async def apink(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Apink {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "eunji":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Eunji :heart:') 
                await ctx.send(random.choice(self.bot.apink_eunji_gif))
                await ctx.message.delete()

    @commands.command(aliases = ['dream'])
    async def dreamcatcher(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Dreamcatcher {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "jiu" or arg == "catcher jiu":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{k8}>, <@!{ctx.author.id}> is talking about JiU :rabbit: ')
                    await ctx.send(random.choice(self.bot.dreamcatcher_jiu_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about JiU :rabbit:')
                await ctx.send(random.choice(self.bot.dreamcatcher_jiu_gif))
                await ctx.message.delete()
        elif arg == "dami" or arg == "catcher dami":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Dami :heart:') 
                await ctx.send(random.choice(self.bot.dreamcatcher_dami_gif))
                await ctx.message.delete()
        elif arg == "gahyeon" or arg == "catcher gahyeon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Gahyeon :heart:') 
                await ctx.send(random.choice(self.bot.dreamcatcher_gahyeon_gif))
                await ctx.message.delete()
        elif arg == "handong" or arg == "catcher handong":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Handong :heart:') 
                await ctx.send(random.choice(self.bot.dreamcatcher_handong_gif))
                await ctx.message.delete()
        elif arg == "siyeon" or arg == "catcher siyeon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Siyeon :heart:') 
                await ctx.send(random.choice(self.bot.dreamcatcher_siyeon_gif))
                await ctx.message.delete()
        elif arg == "sua" or arg == "catcher sua":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about SuA :heart:') 
                await ctx.send(random.choice(self.bot.dreamcatcher_sua_gif))
                await ctx.message.delete()
        elif arg == "yoohyeon" or arg == "catcher yoohyeon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Yoohyeon :heart:') 
                await ctx.send(random.choice(self.bot.dreamcatcher_yoohyeon_gif))
                await ctx.message.delete()

    @commands.command()
    async def weki(self, ctx, meki, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Weki Meki {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if meki == "meki":
            if arg == "doyeon":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Doyeon :heart:') 
                    await ctx.send(random.choice(self.bot.wekimeki_doyeon_gif))
                    await ctx.message.delete()
            elif arg == "elly":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Elly :heart:') 
                    await ctx.send(random.choice(self.bot.wekimeki_elly_gif))
                    await ctx.message.delete()
            elif arg == "lua":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Lua :heart:') 
                    await ctx.send(random.choice(self.bot.wekimeki_lua_gif))
                    await ctx.message.delete()
            elif arg == "lucy":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Lucy :heart:') 
                    await ctx.send(random.choice(self.bot.wekimeki_lucy_gif))
                    await ctx.message.delete()
            elif arg == "rina":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Rina :heart:') 
                    await ctx.send(random.choice(self.bot.wekimeki_rina_gif))
                    await ctx.message.delete()
            elif arg == "sei":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Sei :heart:') 
                    await ctx.send(random.choice(self.bot.wekimeki_sei_gif))
                    await ctx.message.delete()
            elif arg == "suyeon":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Suyeon :heart:') 
                    await ctx.send(random.choice(self.bot.wekimeki_suyeon_gif))
                    await ctx.message.delete()
            elif arg == "yoojung":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Yoojung :heart:') 
                    await ctx.send(random.choice(self.bot.wekimeki_yoojung_gif))
                    await ctx.message.delete()

    @commands.command()
    async def wjsn(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [WJSN {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "bona":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Bona :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_bona_gif))
                await ctx.message.delete()
        elif arg == "cheng xiao":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Cheng Xiao :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_cheng_xiao_gif))
                await ctx.message.delete()
        elif arg == "dawon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Dawon :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_dawon_gif))
                await ctx.message.delete()
        elif arg == "dayoung":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Dayoung :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_dayoung_gif))
                await ctx.message.delete()
        elif arg == "eunseo":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Eunseo :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_eunseo_gif))
                await ctx.message.delete()
        elif arg == "exy":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Exy :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_exy_gif))
                await ctx.message.delete()
        elif arg == "luda":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Luda :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_luda_gif))
                await ctx.message.delete()
        elif arg == "seola":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Seola :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_seola_gif))
                await ctx.message.delete()
        elif arg == "soobin":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Soobin :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_soobin_gif))
                await ctx.message.delete()
        elif arg == "yeonjung":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Yeonjung :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_yeonjung_gif))
                await ctx.message.delete()
        elif arg == "yeoreum":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Yeoreum :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_yeoreum_gif))
                await ctx.message.delete()
        elif arg == "mei qi":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Mei Qi :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_mei_qi_gif))
                await ctx.message.delete()
        elif arg == "xuan qi":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Xuan Yi :heart:') 
                await ctx.send(random.choice(self.bot.wjsn_xuan_yi_gif))
                await ctx.message.delete()

    

    

def setup(client):
    client.add_cog(GGS(client))