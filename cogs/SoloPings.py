import discord, random
from discord.ext import commands
from datetime import datetime

#//servers
luminary = 758468592957521972

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

class SoloPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.natty_gif = ["https://thumbs.gfycat.com/BlankBlaringAmurratsnake-size_restricted.gif",
            "https://thumbs.gfycat.com/ScholarlyUnitedCutworm-max-1mb.gif",
            "https://media.giphy.com/media/f7Xr9BVORnb0vDEraT/giphy.gif",
            "https://giphy.com/gifs/jpEGzlpjwOn1RK0qlZ",
            "https://tenor.com/view/natty-schoolidol-gif-9239469",
            "https://giphy.com/gifs/vOzalSmlR1cVr535rb",
            "https://giphy.com/gifs/AWcuiZbziFmwuc0uQW",
            "https://giphy.com/gifs/sksJILJA9Ab0HiOIIp",
            "https://giphy.com/gifs/hL7aBcWxpzp0VrljNu",
            "https://tenor.com/view/dance-nt-natty-natty_gif-%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-gif-19179900",
            "https://tenor.com/view/%EB%82%98%EB%9D%A0-%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-nt-natty-natty_gif-gif-19177703",
            "https://tenor.com/view/%EB%82%98%EB%9D%A0-%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-nt-natty-natty_gif-gif-19359163",
            "https://tenor.com/view/%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-%EB%82%98%EB%9D%A0-nt-natty-natty-teddybear-gif-19176290",
            "https://tenor.com/view/%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-nt-natty-natty_gif-opps-gif-19266831",
            "https://tenor.com/view/%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-%EB%82%98%EB%9D%A0-nt-natty-natty-teddybear-gif-19176299",
            "https://tenor.com/view/%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-%EB%82%98%EB%9D%A0-nt-natty-natty_gif-gif-19360526",
            "https://tenor.com/view/%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-%EB%82%98%EB%9D%A0-bye-nt-natty-gif-19176192",
            "https://tenor.com/view/nt-natty-natty-teddybear-natty_gif-heart-gif-19176286",
            "https://tenor.com/view/%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-%EB%82%98%EB%9D%A0-dance-nt-natty-gif-19280113",
            "https://tenor.com/view/nt-natty-natty-teddybear-natty_gif-%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-gif-19176185",
            "https://tenor.com/view/nt-natty-wink-natty-teddybear-natty_gif-gif-19176296",
            "https://tenor.com/view/%EB%82%98%EB%9D%A0-%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-nt-natty-natty-teddybear-gif-19176182",
            "https://tenor.com/view/%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-%EB%82%98%EB%9D%A0-nt-natty-natty-teddybear-gif-19176295"]

        self.bot.alexa_gif = ["https://tenor.com/view/no-ahhhh-emotions-ai-trooper-alexa-gif-18362239",
            "https://tenor.com/view/alexa-alexa-kpop-wink-cute-wink-alex-christine-gif-18426203",
            "https://tenor.com/view/sunlight-alexa-alexa-kpop-villain-alexa-villain-gif-18426653",
            "https://tenor.com/view/alexa-kpop-alexa-dance-do-or-die-alexazblabel-gif-18228202",
            "https://tenor.com/view/millenasia-millenesia-project-alexa-alexa-kpop-bale-bale-kpop-gif-18240233",
            "https://tenor.com/view/okay-ok-what-is-it-say-alexa-gif-18669905",
            "https://tenor.com/view/alexa-kpop-alexa-quadratic-equation-maths-alex-christine-gif-19114670",
            "https://tenor.com/view/shocked-shocking-unbelievable-villian-alexa-gif-18776700",
            "https://tenor.com/view/alexa-alexa-kpop-alexa-universe-rule-the-world-alexa-alexa-rule-the-world-gif-18285902",
            "https://tenor.com/view/alexa-kpop-alexa-dance-do-or-die-alexazblabel-gif-18228202",
            "https://tenor.com/view/alexa-kpop-alexa-alexa-zb-label-slay-queen-queen-gif-18882229",
            "https://tenor.com/view/what-laugh-what-what-laugh-laughs-alexa-gif-18240700",
            "https://tenor.com/view/robot-sci-fi-eyes-dance-dancing-gif-18295515",
            "https://tenor.com/view/ale-xa-alexa-kpop-alexa-revolution-revolution-eye-gif-19636140",
            "https://tenor.com/view/naruto-naruto-run-run-kpop-kpop-naruto-run-gif-19538817",
            "https://tenor.com/view/alexa-alexa-universe-alexa-kpop-bomb-bomb-rock-version-gif-18239851",
            "https://tenor.com/view/bts-dna-alexa-kpop-sonnet-son-gif-19204918",
            "https://tenor.com/view/ok-alexa-alexa-kpop-kpop-alex-christine-gif-19759905",
            "https://tenor.com/view/pat-alexa-alexa-kpop-alexa-cute-cute-gif-19636159",
            "https://tenor.com/view/one-girl-army-alexa-alexa-kpop-revolution-come-and-join-the-revolution-gif-19115866",
            "https://tenor.com/view/ai-ai-alexa-hand-fracture-alexa-alexa-kpop-gif-19143065",
            "https://tenor.com/view/alexa-alexa-kpop-alexa-universe-rule-the-world-alexa-alexa-rule-the-world-gif-18285902",
            "https://tenor.com/view/alexa-alexa-revolution-revolution-alexa-is-the-revolution-one-girl-army-gif-19105379",
            "https://tenor.com/view/alexa-kpop-alexa-alexa-zb-label-zanybros-revolution-gif-18882682",
            "https://tenor.com/view/alexa-happy-birthday-alexa-alexa-kpop-alexa-birthday-birthday-gif-19471506",
            "https://64.media.tumblr.com/a74a6728f3108973754f58017d733213/6f028fef11c855b4-ef/s500x750/caded6a1a90f6c0e5ec6893b2e3d1c87cac14f94.gif",
            "https://64.media.tumblr.com/06d3a167ac284a37e2ff7887dec98e5f/6f028fef11c855b4-c9/s500x750/485462a727744ce689548cb2cb30c60c58b42cd5.gif",
            "https://64.media.tumblr.com/3f314c61bc40c05fa3e62115b94caec1/6f028fef11c855b4-ad/s500x750/f2a276ed006aefad76d76f522b66011210071585.gif",
            "https://i.pinimg.com/originals/c8/49/4c/c8494c0e2b93694446e704a720ead114.gif",
            "https://i.pinimg.com/originals/3d/72/86/3d7286747d73a620bfc67153b7b58cef.gif",
            "https://i.pinimg.com/originals/da/5e/3c/da5e3c9e3c74d409d738acbad785ead3.gif",
            "https://i.pinimg.com/originals/da/2b/81/da2b810b30e8d49815f819672b294607.gif"]

        self.bot.chungha_gif = ["https://tenor.com/view/kiss-love-chunga-korean-gif-11126096",
            "https://tenor.com/view/chungha-gif-18541917",
            "https://tenor.com/view/chungha-stare-smokey-eyes-gif-14390425",
            "https://tenor.com/view/chungha-gif-14681679",
            "https://tenor.com/view/kim-chungha-chungha-cute-smile-gif-13261337",
            "https://tenor.com/view/kim-chungha-chungha-cute-gorgeous-smile-gif-12547851",
            "https://tenor.com/view/kim-chungha-chungha-wink-sexy-gif-12547847",
            "https://tenor.com/view/chungha-kim-chungha-kpop-pretty-cute-gif-16653910",
            "https://tenor.com/view/rae-chungha-fancam-play-kpop-gif-18963908",
            "https://tenor.com/view/chungha-kim-chungha-kpop-cute-pretty-gif-16521270",
            "https://cdn.discordapp.com/attachments/804451692677693511/804476336596189224/28dbe575-9912-42d1-b0b3-5587b9497611.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804476337687232562/5434f2dd-3451-4e03-acba-4b7173b9756e.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804476338383224852/70790a1a-abaf-458d-a928-ef26e5b60639.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804476339124961334/3f52be7c-6a6c-4b0b-825e-0cc081408292.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804476339818201088/9df541bb-b9dc-4663-a837-1b2b5492cc49.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804476340489027604/b6b26137-fc43-4d99-bf2b-5d56dda8b622.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804476340803076136/81b317a3-e646-40a5-89e0-94ec83aea104.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804476341248458772/18a5b8bb-7f87-4bd4-839a-ee0da92d85ce.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804476341831335996/233c5359-4aef-4238-be4b-103468477ea6.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804476342468345886/404b4c75-d266-407e-a3be-f438c12843ab.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804477693944397876/b587e429-5724-4099-8456-708441b41d6a.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804477694677876776/b97e2e06-50a1-491c-8406-b8e6a27909c5.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804477695257346138/b3d802ac-6f02-4672-937c-bf2d17027aa2.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804477695941541918/23122ccf-f352-423a-9321-b85f7de3e100.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804477696444596254/c1116be5-5547-49a0-98c1-4402b2634385.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804477696859439145/a1fb77f7-c0a9-477e-8712-2d147d4034d0.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804477697362362368/56434886-d12e-49e0-962b-75dbc006a587.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804477697896087582/3098ada8-176d-4cc7-a8bb-267af97d60cc.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804477699430547496/b0fc597f-0ac1-43df-8af5-e9ff3dbc596f.gif",
            "https://cdn.discordapp.com/attachments/804451692677693511/804477699891527720/db501538-9150-4428-a7d5-209888cce00e.gif",
            "https://64.media.tumblr.com/ceb281a838bf89bee827a7ba61ce00fa/9a13826b46307259-c1/s540x810/00e0b3643d72bacc6ac798383d435132689284f2.gif",
            "https://64.media.tumblr.com/450d2de39b2f923757a6c670c4c585a7/73c4dfe08b926a30-d8/s400x600/bef0d427c69bdf5f4a95f741f5cd4f0fbef27c34.gif",
            "https://64.media.tumblr.com/50fb4bc127f691524d6f1cff2aa518ed/7cafdf91d086b09d-12/s400x600/266b6e6e194b5e8c8ccd766615dcc1a88837a888.gif",
            "https://64.media.tumblr.com/f21f48ffcef8c2bc903841f7e603aa4b/479c6aa3c0d1aef7-a5/s400x600/37e3af7f8b33222855a1de8a74df59a68a7c3525.gif",
            "https://64.media.tumblr.com/709faead3e611a97ecffd6d2b68f7913/7ae1ef65d09f0de4-ff/s400x600/1c3a3b453f754e2d499c887799ecdccf9c29788c.gif",
            "https://64.media.tumblr.com/6af4fb0d0848774a8ecfba0f7c073430/1d14a4a538c2095a-f0/s400x600/a47880934c52357cf24499400c30403acb499074.gif",
            "https://64.media.tumblr.com/b78ab8e07cc0d47f520d94a88ab3c49d/af7cee881d5fecac-f3/s250x400/41a87cdca5fe569ee5d5286d1798597d0f11d212.gif",
            "https://64.media.tumblr.com/aec19a270a09eb4e901b76c2e3807dea/tumblr_pkpbxbYhDS1xkto34o1_r1_400.gif",
            "https://64.media.tumblr.com/5c93b325d55333f746f7db8a66cda773/tumblr_p3j2exURUl1tkcvkjo6_250.gif",
            "https://64.media.tumblr.com/bd7eeceb614e1d8080e54f4f3355d195/4e1c15cbcd941152-a6/s400x600/d053cfd910e7b8dff86ff5158b4ef0febc8da970.gif",
            "https://64.media.tumblr.com/649d36111e5693fb38a4be6fc756bd2c/tumblr_plnfu7fmm81sq4dzzo2_250.gif",
            "https://64.media.tumblr.com/53337dd1df7e8576fa827d3f3635b12d/tumblr_pl75btdU1V1rwdw1wo6_250.gif",
            "https://64.media.tumblr.com/f83edab890c80579d17302d57e8c63bc/tumblr_pjwop9sTkD1swg2mjo1_250.gif",
            "https://64.media.tumblr.com/e8087df1bc67a782af4ed290e332dd18/tumblr_pbrewuqYfa1tkcvkjo2_400.gif",
            "https://64.media.tumblr.com/0facf3fede68d080217cc7306c2a7856/c52f8bc2eae22946-80/s400x600/3be992b1fb86436206b2557df464f6c054aa3914.gif",
            "https://64.media.tumblr.com/c14beb8e90e1b8f852562d12f768b7dc/2533bd52329a6eec-bf/s400x600/95f2267777c96b7b5126cdf2823b421614a54682.gif",
            "https://64.media.tumblr.com/46278f01fd37e7e44cd5ad4e8ab92dff/2533bd52329a6eec-a7/s400x600/f10c0cd92b868e78aa4dd33ce91a8020c4e0fb90.gif",
            "https://64.media.tumblr.com/e23d7cb7f40273b2309b944680a5a9dc/tumblr_pn3skyViLA1w8gxaso3_250.gif",
            "https://64.media.tumblr.com/da2fd031461f2d889bb3f9f8a10a2666/tumblr_piwzmdosoc1xx74t1o4_250.gif",
            "https://tenor.com/view/chungha-chungha-eat-chungha-staring-chungha-look-stare-gif-19318960",
            "https://tenor.com/view/chungha-kim-chungha-kpop-cute-pretty-gif-16521258",
            "https://tenor.com/view/kim-chungha-chungha-smile-cute-gif-13261334",
            "https://tenor.com/view/chungha-kim-chungha-kpop-cute-pretty-gif-16521273",
            "https://gfycat.com/ablefailingcreature",
            "https://gfycat.com/adorablemeatyaphid",
            "https://gfycat.com/gloriousmeageraxolotl-chung-ha",
            "https://gfycat.com/informalphonyibadanmalimbe"]

        self.bot.iu_gif = ["https://tenor.com/view/iu-fighting-cute-celeb-alarm-gif-16215337",
            "https://tenor.com/view/iu-meh-cute-annoyed-gif-14687766",
            "https://tenor.com/view/iu-lee-jieun-cute-cf-pout-gif-16660666",
            "https://tenor.com/view/iu-cindy-cute-producers-smile-gif-17223449",
            "https://tenor.com/view/iu-hairflip-gif-11159215",
            "https://tenor.com/view/iu-iu-heart-%EC%95%84%EC%9D%B4%EC%9C%A0-heart-gif-18994163",
            "https://tenor.com/view/iu-badass-hotel-del-luna-jang-man-wol-gif-14912690",
            "https://tenor.com/view/iu-jang-man-wol-pensive-hotel-del-luna-drama-gif-16047677",
            "https://tenor.com/view/cute-clapping-happy-funny-fun-gif-17239556",
            "https://gfycat.com/smallshadyalbatross",
            "https://gfycat.com/linedequalgoa",
            "https://gfycat.com/knobbydelectableindiancow-wisewords-iutv",
            "https://gfycat.com/adolescentwaterygalapagosmockingbird",
            "https://tenor.com/view/iu-lee-ji-eun-gif-11126094",
            "https://tenor.com/view/%EC%97%90%EC%9E%87-%EC%9D%B4%EC%A7%80%EC%9D%80-hello-positive-vibes-iu-gif-17116417",
            "https://tenor.com/view/iuxsuga-iu-eight-%EC%9D%B4%EC%A7%80%EC%9D%80-smile-iu-gif-17116404",
            "https://tenor.com/view/iu-lee-ji-eun-kpop-korean-hae-soo-gif-16549021",
            "https://tenor.com/view/iu-lee-ji-eun-kpop-korean-pretty-gif-15906983",
            "https://tenor.com/view/iu-bbibbi-lee-jieun-pretty-beautiful-gif-15740850",
            "https://tenor.com/view/iu-laugh-cute-anniversary-jieun-gif-18576961",
            "https://tenor.com/view/iu-iu-cute-iu-blueming-iu-girl-group-iu-love-poem-gif-15592264",
            "https://tenor.com/view/iu-iu-cute-iu-blueming-iu-girl-group-iu-love-poem-gif-15592209",
            "https://tenor.com/view/iu-soda-drinks-lee-ji-eun-unnie-angel-gif-18087723",
            "https://tenor.com/view/iu-lee-ji-eun-kpop-pretty-cute-gif-17417749",
            "https://tenor.com/view/good-job-well-done-daebak-awesome-thumb-up-gif-17648286",
            "https://tenor.com/view/iu-lee-ji-eun-kpop-cute-pretty-gif-17923363",
            "https://tenor.com/view/iu-lee-ji-eun-kpop-pretty-cute-gif-17845103",
            "https://tenor.com/view/hotel-del-luna-iu-eating-chew-bite-gif-17750091",
            "https://tenor.com/view/bye-annyeong-see-ya-see-you-see-you-tomorrow-gif-17648285",
            "https://tenor.com/view/delicious-cant-stop-unstoppable-eating-again-gif-17375580",
            "https://tenor.com/view/iu-lee-ji-eun-wink-cute-pretty-gif-17535138",
            "https://tenor.com/view/iu-lee-ji-eun-kpop-pretty-cute-gif-17417717",
            "https://tenor.com/view/iu-lee-jieun-cute-cf-pout-gif-16660666",
            "https://tenor.com/view/iu-lee-jieun-kpop-pretty-cute-gif-17078417",
            "https://tenor.com/view/iu-wink-cute-celebrity-album-gif-20152965",
            "https://tenor.com/view/iu-celebrity-dance-album-jieun-gif-20152802",
            "https://tenor.com/view/iu-celebrity-red-dress-album-gif-20152803",
            "https://gfycat.com/adorablekeychinchilla",
            "https://gfycat.com/alertredamethystsunbird",
            "https://gfycat.com/aggravatingparchedchupacabra",
            "https://i.pinimg.com/originals/ee/04/03/ee04037e3aafeb682eb6706c4ee952c5.gif",
            "https://tenor.com/view/box-hide-face-asian-girl-gif-4641619",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495812380262410/IU_gif_17.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495818738303026/IU_gif_14.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495851109285928/IU_gif_2.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495871330156565/IU_gif_15.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495876153606154/IU_gif_1.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495876175495208/IU_gif_13.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495888611737620/IU_gif_19.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495889303273476/IU_gif_16.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495905950466058/IU_gif_9.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495923427606538/IU_gif_6.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495928561434674/IU_gif_8.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495935339429908/IU_gif_7.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495941794594826/IU_gif_4.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495957233565706/IU_gif_5.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495958107160596/IU_gif_18.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495970651668490/IU_gif_11.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/818495971238740029/IU_gif_12.gif"]

        self.bot.somi_gif = ["https://tenor.com/view/jeon-somi-ioi-pout-thinking-gif-14321378",
            "https://tenor.com/view/jeon-somi-ioi-fake-smile-laugh-gif-14321383",
            "https://tenor.com/view/somi-somsom-silly-tongue-wacky-gif-9002693",
            "https://tenor.com/view/somi-vitasom-smile-happy-rwar-gif-8960237",
            "https://tenor.com/view/somi-vitasom-%EC%A0%84%EC%86%8C%EB%AF%B8-%ED%98%BC%ED%98%88-gif-8958800",
            "https://tenor.com/view/jeon-somi-ioi-stare-hmmp-hmp-gif-14321391",
            "https://tenor.com/view/jeon-so-mi-gif-8389636",
            "https://tenor.com/view/somi-jeon-somi-what-you-waiting-for-somi-comeback-somi-teaser-gif-17861737",
            "https://tenor.com/view/somi-vitasom-gif-8958750",
            "https://tenor.com/view/somi-eating-food-gif-8958728",
            "https://tenor.com/view/somi-abyan-gif-18258549"]

        self.bot.yukika_gif = ["https://tenor.com/view/yukika-cute-yukika-cute-yukika-being-cute-gif-18862414",
            "https://tenor.com/view/yukika-japanese-soul-lady-gif-18312979",
            "https://tenor.com/view/yukika-japanese-soul-lady-gif-18313007",
            "https://tenor.com/view/yukika-mixnine-fist-gif-14017170",
            "https://tenor.com/view/yukika-wave-hello-gif-14017162",
            "https://tenor.com/view/yukika-hswcix-gif-19442465",
            "https://tenor.com/view/yukika-gif-19463874",
            "https://tenor.com/view/yukika-japanese-soul-lady-gif-18312979",
            "https://gfycat.com/SpiffyFavoriteArmyworm",
            "https://gfycat.com/RigidSphericalEuropeanfiresalamander",
            "https://i.pinimg.com/originals/0b/0b/31/0b0b315c176117a296910d69bcf41146.gif",
            "https://i.pinimg.com/originals/3b/26/f6/3b26f68951c1c5576628e0e8015e8c12.gif",
            "https://i.pinimg.com/originals/6b/bd/5d/6bbd5d27369192d5a71a79aa13e911a5.gif",
            "https://i.pinimg.com/originals/6a/e7/bd/6ae7bd9b715bf85a507f7f6dbbe8aa3f.gif",
            "https://i.pinimg.com/originals/c1/8e/77/c18e777ba3fe27b6d3965fe6f7551122.gif",
            "https://64.media.tumblr.com/278d65f119fd70c1f243bf97e209b013/tumblr_pnof7z2O2W1vbuvbno4_250.gif",
            "https://1.bp.blogspot.com/-k8KSOGed53Y/XxWqknMHmpI/AAAAAAABUlQ/kAQMBRUCZToIBM-bykS4LaGKe_QC2ZJeACLcBGAsYHQ/s1600/Honeycam%2B10796.gif",
            "https://64.media.tumblr.com/31ad864e8991c877bb429cf82702ce89/97727d9235cf894a-84/s500x750/263b3d9c4b5ee56f5f2679a9e912c905a4a6186e.gif",
            "https://thumbs.gfycat.com/InfantileFloweryIridescentshark-size_restricted.gif",
            "https://thumbs.gfycat.com/RequiredAngelicLark-max-1mb.gif",
            "https://gfycat.com/belatedwaryaplomadofalcon",
            "https://gfycat.com/definitearcticcommongonolek",
            "https://gfycat.com/pessimisticlategrebe",
            "https://gfycat.com/agiletanaustraliankelpie",
            "https://gfycat.com/rectangularskeletalatlanticblackgoby",
            "https://gfycat.com/impartialillamethystinepython",
            "https://gfycat.com/biodegradableinsignificantarchaeocete",
            "https://gfycat.com/scratchyniceeft",
            "https://gfycat.com/educatedclutteredcougar",
            "https://gfycat.com/givingbowedblackandtancoonhound",
            "https://gfycat.com/blackfemininekagu",
            "https://gfycat.com/lazyunimportanthoiho",
            "https://gfycat.com/fondwanhydra",
            "https://gfycat.com/organicforsakenhapuku",
            "https://gfycat.com/dimgreedyafricangroundhornbill",
            "https://gfycat.com/niftyunacceptablehoneyeater",
            "https://gfycat.com/frayedtidyarawana"]

        self.bot.taemin_gif = ["https://media.discordapp.net/attachments/753987619733504000/758815646162616350/ezgif-3-69847282811c.gif",
            "https://tenor.com/view/lee-taemin-taemin-move-stare-gif-14254226",
            "https://tenor.com/view/taemin-shinee-kpop-shirtless-concert-gif-5097931",
            "https://tenor.com/view/shinee-taemin-kpop-gif-7235119",
            "https://tenor.com/view/taemin-lee-taemin-shinee-taemin-shinee-taemin-want-gif-15037342",
            "https://tenor.com/view/shinee-kpop-taemin-hmpf-pout-gif-11162331",
            "https://tenor.com/view/lee-taemin-taemin-shinee-kpop-cute-gif-16445806",
            "https://tenor.com/view/lee-taemin-taemin-lee-shinee-serious-taemin-shinee-gif-15134301",
            "https://tenor.com/view/taemin-tae-gif-18347164",
            "https://tenor.com/view/taemin-korean-kpop-gif-10431117",
            "https://tenor.com/view/taemin-idea-shinee-superm-kpop-gif-19128665",
            "https://tenor.com/view/taemin-idea-shinee-superm-kpop-gif-19128560",
            "https://tenor.com/view/taemin-idea-kpop-shinee-superm-gif-19128548",
            "https://tenor.com/view/taemin-shinee-superm-idea-kpop-gif-19128613",
            "https://tenor.com/view/taemin-shinee-superm-idea-mv-gif-19128526",
            "https://tenor.com/view/taemin-shinee-superm-idea-kpop-gif-19128572",
            "https://tenor.com/view/taemin-shinee-superm-dance-idea-gif-19128635",
            "https://tenor.com/view/taemin-shinee-superm-comeback-idea-gif-19128539",
            "https://tenor.com/view/taemin-shinee-kpop-snorting-lee-gif-17506772",
            "https://tenor.com/view/shinee-taemin-kpop-heart-cute-gif-9591707",
            "https://tenor.com/view/shinee-taemin-kpop-love-hearts-gif-11162284",
            "https://gfycat.com/acclaimedcoarsegorilla",
            "https://tenor.com/view/cry-taemin-shinee-gif-7394551",
            "https://tenor.com/view/taemin-shinee-sleepy-tired-sleep-gif-10995497",
            "https://tenor.com/view/taemin-shinee-kpop-korean-ice-cream-gif-7371003",
            "https://tenor.com/view/lee-taemin-shinee-taemin-taemin-smile-gif-14850280",
            "https://tenor.com/view/taemin-tae-gif-18422308",
            "https://tenor.com/view/shinee-move-taemin-lee-taemin-dance-gif-16006886",
            "https://tenor.com/view/shinee-taemin-lee-taemin-taemin-gif-14850283",
            "https://tenor.com/view/taetaemin-gif-18433463",
            "https://tenor.com/view/taemin-tae-gif-18422310",
            "https://tenor.com/view/taemin-shinee-okay-smile-smiling-gif-8173054",
            "https://tenor.com/view/taemin-sexy-taemin-tae-gif-18346817",
            "https://tenor.com/view/taemin-tae-gif-18368806",
            "https://tenor.com/view/taemin-shinee-lee-taemin-superm-kpop-gif-16653977",
            "https://tenor.com/view/taemin-gif-20067233",
            "https://tenor.com/view/taemin-heart-gif-19902456",
            "https://tenor.com/view/taemin-bored-gif-19902443",
            "https://tenor.com/view/taemin-you-gif-19902437",
            "https://tenor.com/view/faeteez-shinee-taemin-taemin-eating-taemin-cute-gif-19946084",
            "https://tenor.com/view/faeteez-taemin-taemin-cute-taemin-hot-shinee-gif-19943749",
            "https://cdn.discordapp.com/attachments/811453123267657739/812084794740572200/5c1110a3-d35d-4970-8f70-d1c2397bad7c.gif",
            "https://cdn.discordapp.com/attachments/811453123267657739/812085464135761920/6eb3220e-aa85-415b-b31b-c3e80ab42088.gif",
            "https://cdn.discordapp.com/attachments/811453123267657739/812085950640291860/7ecc87fd-31ca-4d7a-8612-9d8f93a707c3.gif",
            "https://tenor.com/view/hug-big-for-you-jonghyun-gif-13110586",
            "https://tenor.com/view/shinee-excuse-me-miss-j-onghyun-taemin-dance-gif-17047724",
            "https://cdn.discordapp.com/attachments/811453123267657739/818295123707953162/9cd4e263-6389-49b2-a7c6-5b2f7aaab95e.gif",
            "https://cdn.discordapp.com/attachments/811453123267657739/818296348042067978/16c7c180-328a-470d-b19e-8e0a86491144.gif",
            "https://cdn.discordapp.com/attachments/811453123267657739/818522280513503272/Tumblr_l_1093819102434770.gif",
            "https://cdn.discordapp.com/attachments/811453123267657739/818522934837772328/Tumblr_l_1093984449994811.gif",
            "https://cdn.discordapp.com/attachments/811453123267657739/818523168313573416/Tumblr_l_1094056768268794.gif"]

        self.bot.woodz_gif = ["https://tenor.com/view/cho-seungyoun-seungyoun-jo-seung-yeon-seung-yeon-%EC%8A%B9%EC%97%B0-gif-14259988",
            "https://tenor.com/view/woodz-uniq-choseungyoun-gif-20298646",
            "https://tenor.com/view/woodz-seungyoun-gif-19678841",
            "https://tenor.com/view/x1-seungyeon-cute-gif-14910337",
            "https://gfycat.com/forthrightwildgrizzlybear",
            "https://giphy.com/gifs/woodz-cho-seungyeon-Yk8F6KMxYL3kDl1wSj",
            "https://giphy.com/gifs/seungyeon-woodz-OZHIe9YchxD17vEVIt",
            "https://gfycat.com/affectionateslightgourami-cho-seungyoun-woodz",
            "https://gfycat.com/phonywastefulandeancondor-cho-seungyoun-producex101",
            "https://gfycat.com/shadowyaccomplishedbackswimmer",
            "https://gfycat.com/jubilantvibrantfirefly-cho-seungyoun-woodz-x1",
            "https://gfycat.com/cleanblueamericanblackvulture-seungyoun-thinking-avocado-woodz-green-cute",
            "https://tenor.com/view/xone-x1-seungyoun-cho-seungyoun-arrow-gif-15377389",
            "https://tenor.com/view/x1-xone-seungyoun-hello-kpop-gif-15377418",
            "https://tenor.com/view/xone-x1-seungyoun-laugh-gif-15377395",
            "https://tenor.com/view/xone-x1-seungyoun-peace-gif-15377387"]

        self.bot.kriswu_gif = ["https://64.media.tumblr.com/391969724e74ff6a203059569633fdcf/9d72462f982a6a15-f1/s400x600/74b495fe0c7095f638efb254fae8adaa92ee06ad.gif",
            "https://64.media.tumblr.com/922086f55a81ce5f8376ef7d105b6c7e/547ebc0250338952-d5/s400x600/770217db43bc7df459e12d6a40eb7e5a17b1bd54.gif",
            "https://64.media.tumblr.com/d74fc18aeb8e1ff7d26f4f342b6e78e8/547ebc0250338952-33/s400x600/8f77216763b215d7d0b282df1261bf98f5cad3b2.gif",
            "https://64.media.tumblr.com/4e8bc01a9ac9ad69e067dde2d6585026/tumblr_p4a11411bs1sqc1zfo2_540.gif",
            "https://64.media.tumblr.com/cb5f7354b92af5b8aa071397d63d1c4b/tumblr_pq0zkfLzEU1r3hdhfo6_r1_540.gif",
            "https://64.media.tumblr.com/2b7ef69e7202955034ca33c55152aeb7/tumblr_phtbb1EOnF1tvfa7io5_r1_540.gif",
            "https://64.media.tumblr.com/318125773472498f76ea8a42b92e9d8f/tumblr_p2px5engzF1vbs9hno8_r1_400.gif",
            "https://data.whicdn.com/images/260211507/original.gif",
            "https://data.whicdn.com/images/260500068/original.gif",
            "https://64.media.tumblr.com/8e8a2f0855a04fd77606ab3064cf7b3f/04598c1cb73fcf7d-75/s540x810/8315b10ae131eb6cde32044a7356bdd86ea4b8c0.gif",
            "https://64.media.tumblr.com/214706888b0057936b0e55b584c52212/tumblr_oo5yx2cBd31vjibn5o5_400.gif",
            "https://64.media.tumblr.com/01fddbb408950d87eb4c7ec40cfd9ed9/tumblr_p3pyazNlvA1vbs9hno1_400.gif",
            "https://cdn.discordapp.com/attachments/804189492516093992/812081442632237116/0b8d4c0c-b032-4546-8547-fa7b5fe915e5.gif",
            "https://cdn.discordapp.com/attachments/804189492516093992/812081760938098698/0ca6d1e2-219e-44b4-9e14-17c2dd6061e0.gif",
            "https://cdn.discordapp.com/attachments/804189492516093992/812081802613227580/0d60b216-9e10-47b2-9183-306939984f45.gif",
            "https://cdn.discordapp.com/attachments/804189492516093992/812082270231330886/1acc5c59-0073-46de-a84c-3f04bb85f669.gif",
            "https://cdn.discordapp.com/attachments/804189492516093992/812083117564756018/2ea6aa9c-122e-4798-a6ba-cbae4c1ba0f6.gif",
            "https://cdn.discordapp.com/attachments/804189492516093992/812083417125486652/3bd63f5d-5a4b-4dfe-9c8e-9d16a694263a.gif",
            "https://cdn.discordapp.com/attachments/804189492516093992/812084310681059368/4e283de4-96da-43ca-8404-4d9ddbec8af1.gif",
            "https://cdn.discordapp.com/attachments/804189492516093992/812084503689297920/5a4bc271-9655-4d22-8f21-37fdca40d937.gif",
            "https://cdn.discordapp.com/attachments/804189492516093992/812084968426962955/5de46fb7-e8e1-495a-ac45-24d4a1194b7b.gif",
            "https://cdn.discordapp.com/attachments/804189492516093992/812085067316199454/5fe3b55a-759a-45a3-8441-d5f7d0f11e44.gif",
            "https://cdn.discordapp.com/attachments/804189492516093992/812085915672379412/7e379d69-d8a1-415e-93e5-4ffb27ec3c14.gif",
            "https://cdn.discordapp.com/attachments/804189492516093992/812086086046187550/08b7b665-1158-4cfe-944f-c0da6bd241c2.gif",
            "https://giphy.com/gifs/kriswu-kris-wu-tough-pill-4QER6SJweUz7B6bitC",
            "https://giphy.com/gifs/kriswu-november-rain-kris-wu-29oeKjE5c1oC56pWso",
            "https://giphy.com/gifs/interscope-kris-wu-like-that-vvJmqePcGPGfnAhKYO",
            "https://giphy.com/gifs/coffee-kriswu-chuang2020-l10O6D2H1bFjUcCu2c",
            "https://giphy.com/gifs/wetv-kriswu-chuang2020-kYRDnIP2F7eh9k2ZYZ",
            "https://cdn.discordapp.com/attachments/804189492516093992/818296160144982046/13f8bb8e-9a59-4519-bed5-072ccd10ad5e.gif",
            "https://cdn.discordapp.com/attachments/804189492516093992/818296748123357184/21fa83d6-a68b-4e2c-bf01-1f65ca592e2f.gif"]

        self.bot.luhan_gif = ["https://cdn.discordapp.com/attachments/804189463277469716/812084025320669184/4c01a4b2-8fb5-453f-88df-dd52103e2962.gif",
            "https://giphy.com/gifs/mv-luhan-promises-MBheKRryjmyfx7AKpu",
            "https://giphy.com/gifs/coffee-luhan-kriswu-V2Tl1qJswgh1dmELaY",
            "https://giphy.com/gifs/luhan-behindthescenes-oncall-wHmM5DiZvHHllIANU7",
            "https://giphy.com/gifs/lu-han-3ohjV5U2Qi5tve1wQM",
            "https://giphy.com/gifs/lu-han-3ohjV3oP3edo6sg8ww"]

        self.bot.tao_gif = ["https://giphy.com/gifs/tao-huangzitao-mv-on-wetv-L54xNewWz7VAFwhr4a",
            "https://giphy.com/gifs/dancing-tao-chuang2020-9BYTToQ0KU2JwgdUwH",
            "https://giphy.com/gifs/tao-cpop-theroad-nqoEziPAzo3SWrXhxh",
            "https://giphy.com/gifs/tao-chuang2020-huangzitao-lk7z31XJJJ9VOIMswX",
            "https://giphy.com/gifs/tao-huangzitao-pandacostume-x3kC8px73ShsEgFQyn",
            "https://cdn.discordapp.com/attachments/804188466488279040/813121046349742090/Tumblr_l_420797878791611.gif",
            "https://cdn.discordapp.com/attachments/804188466488279040/813121046751346758/Tumblr_l_420796468318330.gif",
            "https://cdn.discordapp.com/attachments/804188466488279040/813121259600216064/Tumblr_l_420856488625651.gif"]

        self.bot.kangdaniel_gif = ["https://giphy.com/gifs/daniel-wannaone-springbreeze-t8XajwFT6rnwCOLtA3",
            "https://giphy.com/gifs/daniel-wanna-one-kang-3fivne1HaeeQZAqku9",
            "https://giphy.com/gifs/daniel-wanna-one-kang-pzGIx6tzXxua2iiROq",
            "https://giphy.com/gifs/kang-daniel-3o6fJeCcEB4wU833mU",
            "https://giphy.com/gifs/kang-daniel-l4pTrAKUcihuT7nJ6",
            "https://giphy.com/gifs/wanna-one-kang-daniel-kpop-2vmfW4gMn05QAhATKk",
            "https://tenor.com/view/daniel-kang-cute-heart-gif-12998497",
            "https://tenor.com/view/kang-daniel-cute-handsome-make-face-rabbit-teeth-gif-10832990",
            "https://tenor.com/view/wanna-one-wannable-kang-daniel-gif-11507783",
            "https://tenor.com/view/kang-daniel-wanna-one-cry-smile-cute-gif-10327956",
            "https://tenor.com/view/produce101-kangdaniel-produce101season2-gif-8446224",
            "https://tenor.com/view/kang-daniel-sexy-dance-dance-gif-14259959",
            "https://tenor.com/view/kangdaniel-gif-18175160",
            "https://tenor.com/view/%EA%B0%95%EB%8B%A4%EB%8B%88%EC%97%98-%EA%B0%95%EC%9D%98%EA%B1%B4-%EC%86%90%ED%95%98%ED%8A%B8-%ED%95%98%ED%8A%B8-%EB%AF%B8%EC%86%8C-gif-11346968",
            "https://tenor.com/view/%EA%B0%95%EB%8B%A4%EB%8B%88%EC%97%98-%EB%B8%8C%EC%9D%B4-%ED%8F%AC%EC%A6%88-%EB%AF%B8%EC%86%8C-%EA%B7%80%EC%97%AC%EC%9A%B4-gif-11346998",
            "https://tenor.com/view/ka-wanna-one-kang-daniel-kang-daniel-danirl-ori-cat-wannable-kpop-gif-12633990",
            "https://tenor.com/view/kang-daniel-hair-flip-fresh-im-pretty-smile-gif-10418383",
            "https://tenor.com/view/good-night-kiss-love-gif-12598323",
            "https://tenor.com/view/wanna-one-kang-daniel-dance-kang-daniel-danirl-ori-cat-wannable-kpop-gif-12633988",
            "https://tenor.com/view/kang-daniel-daniel-daniel-kang-wanna-one-kang-daniel-my-beloved-gif-19780561",
            "https://tenor.com/view/kang-daniel-cute-%EA%B0%95%EB%8B%A4%EB%8B%88%EC%97%98-%E5%A7%9C%E4%B8%B9%E5%B0%BC%E5%B0%94-daniel-kang-gif-14259804",
            "https://tenor.com/view/kang-daniel-wannaone-gif-10413734",
            "https://tenor.com/view/wanna-one-kang-daniel-smile-kang-daniel-danirl-ori-cat-wannable-kpop-gif-12633998"]

        self.bot.sunmi_gif = ["https://gfycat.com/aggressiveobeseannelida-miya-ne-sunmi-cute-kpop-hot",
            "https://gfycat.com/adorablespotlesscockatiel",
            "https://gfycat.com/bestselfassurediriomotecat-sunmi",
            "https://gfycat.com/clearelaborateamphiuma-lee-sunmi-gashina-heroine-siren-vlive",
            "https://gfycat.com/creamydevotedhippopotamus",
            "https://gfycat.com/frailagreeableairedaleterrier",
            "https://gfycat.com/querulouscomfortablehypacrosaurus",
            "https://gfycat.com/sameorganicgoldenmantledgroundsquirrel-sunmi",
            "https://gfycat.com/handyremotebovine-pporappippam-sunmi-kpop-solo",
            "https://gfycat.com/webbeddefensiveblesbok",
            "https://gfycat.com/valuablefarandeancondor",
            "https://gfycat.com/cheerynastyguillemot-lalalay-sunmi",
            "https://gfycat.com/crazycommoncranefly",
            "https://gfycat.com/delayedhonestandeancat-sunmi",
            "https://gfycat.com/flatshowygrizzlybear",
            "https://gfycat.com/diligentmilkyfeline-sunmi",
            "https://gfycat.com/heartyserpentinebull",
            "https://gfycat.com/glamorousantiquecuckoo-sunmi",
            "https://gfycat.com/generousaliveaztecant",
            "https://gfycat.com/equatorialthornyhammerheadbird-lee-sunmi-miyayeah-korean-miyane-kpop",
            "https://gfycat.com/equatorialcapitaladdax-lalalay-sunmi",
            "https://gfycat.com/inconsequentialvainblacklab",
            "https://64.media.tumblr.com/9887e85fe7153210e1eb4952d5f24ddb/77fe2d58c321773c-ad/s2048x3072_c0,7778,100000,91944/d288e1e039ce0a72f0f6cd4e75f89bab8d7bd85b.gif"]

        self.bot.yubin_gif = ["https://78.media.tumblr.com/be13e6f73e9b9ca358fa421432a2c83a/tumblr_p9v2d7MMvM1wfmyhto2_540.gif",
            "https://78.media.tumblr.com/76b2b0202c1563bd6839030659e147d1/tumblr_p9v2d7MMvM1wfmyhto3_540.gif",
            "https://gfycat.com/timelybriefbarebirdbat-wonder-girls-kpics",
            "https://gfycat.com/browncolorfuladmiralbutterfly-kpopgfys-europe",
            "https://gfycat.com/aromaticelasticankolewatusi",
            "https://64.media.tumblr.com/370eff3f3bd7edbdfeb9820517d2437b/tumblr_pkgrqcEiBN1xy0u4ko7_400.gifv",
            "https://i.pinimg.com/originals/5d/c5/d5/5dc5d582c2b37126c3f4718aac1e66bf.gif",
            "https://78.media.tumblr.com/99f335d067f425e4b4fe3e78a881fd8a/tumblr_p9seia7vdb1urmyjyo6_r1_500.gif",
            "https://66.media.tumblr.com/ecf1fdfddfe263763122163dcc6d7d12/tumblr_pitu6iy92L1sy8x5ho1_500.gif"]

        self.bot.rothy_gif = ["https://gfycat.com/actualfreeasianlion-k-culture-korean-music-mv-music-video-k-pop-kpop-myubi-myujigbidio",
            "https://gfycat.com/ashamedclosedgallinule-beauty",
            "https://gfycat.com/baggysleepydiplodocus-beauty",
            "https://gfycat.com/coldsilveramethystinepython",
            "https://gfycat.com/desertedcoarseiberianchiffchaff-beauty",
            "https://gfycat.com/smoothniceamazondolphin",
            "https://gfycat.com/belatedcolorlessdoe-rothy",
            "https://gfycat.com/uncommondisastrousdegu",
            "https://gfycat.com/artisticpepperyeidolonhelvum",
            "https://gfycat.com/calculatingcourageouscardinal",
            "https://gfycat.com/coordinatedblushingdevilfish-beauty-small-kpop-cute",
            "https://gfycat.com/colorfulbreakableibisbill",
            "https://gfycat.com/weakspryaustraliankelpie",
            "https://gfycat.com/feistyunhealthyconey",
            "https://gfycat.com/velvetyfrankgrayreefshark-mechabear-kpop",
            "https://gfycat.com/thinhonorablebeardedcollie-rothy-kpop-bee",
            "https://gfycat.com/dapperverifiableape-rothy-kpop-bee",
            "https://gfycat.com/decimalrigidinexpectatumpleco",
            "https://gfycat.com/decisiverecentabalone-mechabear-rothy-kpop",
            "https://gfycat.com/incredibletallgrayfox-mechabear-rothy-kpop",
            "https://gfycat.com/infinitegroundedargali",
            "https://gfycat.com/rectangularhotherculesbeetle",
            "https://gfycat.com/realisticembarrassedcoypu",
            "https://gfycat.com/thatrapidherald-rothy-kpop-bee",
            "https://gfycat.com/pinkloneeskimodog-rothy-kpop-bee",
            "https://gfycat.com/giganticliveindianglassfish-mechabear-singer-rothy-kpop",
            "https://gfycat.com/actualrealherring-rothy-kpop-bee",
            "https://gfycat.com/sophisticateddisastrousargentineruddyduck-mechabear-kpop",
            "https://gfycat.com/terribletemptingearthworm-mechabear-kpop",
            "https://gfycat.com/uneveninfamouseelelephant-rothy",
            "https://gfycat.com/acrobaticenragediberianmidwifetoad",
            "https://gfycat.com/impeccabletartfalcon",
            "https://gfycat.com/wellinformedbrilliantazurevase-mechabear-kpop",
            "https://gfycat.com/chillyshrillhydra",
            "https://gfycat.com/faintspeedyboto-rothy-kpop-bee",
            "https://gfycat.com/slowfatindigobunting-mechabear-kpop",
            "https://gfycat.com/welltodoquarrelsomegoldenmantledgroundsquirrel",
            "https://thumbs.gfycat.com/FamousColdDalmatian-max-1mb.gif",
            "https://pa1.narvii.com/6944/3f03a00960e34cc4f88c0601573d3cca2e009ca7r1-268-350_hq.gif",
            "https://64.media.tumblr.com/684d6f0050c76f36c7dc7102b390611a/tumblr_psv1p683G81y48sr6o1_250.gif",
            "https://64.media.tumblr.com/124f8c7a70a4056680b555d1c0d810e7/tumblr_p9ncynsmSq1uk0y4po5_400.gif",
            "https://thumbs.gfycat.com/VigorousThirdCommongonolek-size_restricted.gif",
            "https://64.media.tumblr.com/7ee4e1873a142f4bdeb6c29c181b9318/fcb6a1a1200701c2-65/s400x600/502810f4f4514b3afd73dfb215ab92ba7a48885c.gif",
            "https://64.media.tumblr.com/2adf593ba0efc9e237663c37e63a4c65/tumblr_psp3pb1NFb1xw84pqo3_250.gif",
            "https://imgur.com/YQFIcie",
            "https://imgur.com/8yc402e"]

        self.bot.hyuna_gif = ["https://tenor.com/view/hyuna-lipnhip-gif-10531483",
            "https://tenor.com/view/kpop-soloist-hyuna-wink-smile-gif-15591705",
            "https://tenor.com/view/hyuna-gif-8262788",
            "https://tenor.com/view/kpop-soloist-khh-hyuna-flip-hair-gif-14692978",
            "https://tenor.com/view/kim-hyuna-hyuna-kpop-wonder-girls-bleh-gif-15063282",
            "https://tenor.com/view/hyuna-kpop-fix-hair-gif-13407251",
            "https://tenor.com/view/kim-hyuna-hyuna-kpop-wonder-girls-tired-gif-15063284",
            "https://cdn.discordapp.com/attachments/807685485144178698/807686829544833084/image0.gif",
            "https://gfycat.com/AlarmedBronzeAndalusianhorse",
            "https://data.whicdn.com/images/302898652/original.gif",
            "https://i.pinimg.com/originals/f7/20/12/f72012fa70cf4671a70c45108637aa62.gif",
            "https://data.whicdn.com/images/298835380/original.gif",
            "https://64.media.tumblr.com/cd8345ca5b35caf1f319ea4dda66ba34/84b4f8c7f683452d-03/s500x750/86690aaf7587bd9c37ce44b269c043ab49692d6d.gif",
            "https://thumbs.gfycat.com/DevotedTartEgret-size_restricted.gif",
            "https://s12.favim.com/gif_previews/7/717/7171/71716/7171698.gif",
            "http://25.media.tumblr.com/88e10afee358cb33d10d904ab6bcc1cf/tumblr_mi8yi3tRb81qbcw96o2_250.gif",
            "http://24.media.tumblr.com/tumblr_mc9t4cna3D1rhhm87o1_500.gif",
            "https://64.media.tumblr.com/43ff84183a76645d4202548070fb6917/tumblr_inline_pk09j0Lw5g1r0vev1_640.gif",
            "https://0.soompi.io/wp-content/uploads/2017/12/09042558/hyuna-crazy.gif",
            "https://i.gifer.com/LFZI.gif",
            "https://media.tenor.com/images/6bcc2f35d849e5a14d5649fe86ffce3a/tenor.gif",
            "https://64.media.tumblr.com/5bec5c4efea21163e5bebc0f3d8770a2/bf48312292811850-93/s540x810/8738dafe77f0838358fe597d0ab592d4ccf5c9d6.gif",
            "https://data.whicdn.com/images/317165671/original.gif",
            "https://64.media.tumblr.com/6006fc102d0a577e110435b293dd6e16/tumblr_oy0yj6bRvZ1r7qnpao3_400.gif",
            "https://pa1.narvii.com/5744/62ad0a5f193311ebb6a841fdacae47aef07a3dae_hq.gif",
            "https://gifimage.net/wp-content/uploads/2017/10/hyuna-gif-11.gif",
            "https://67.media.tumblr.com/8f1ddb4561bb2978018a24cbb2698b52/tumblr_n9fbf9ooBD1tf6m14o1_500.gif",
            "https://64.media.tumblr.com/e836abd0355235060122f72172f090d6/08276495afa80047-be/s540x810/e53cf49edc9dc3efb14ddebbec66d253dd08a86b.gif",
            "https://64.media.tumblr.com/d4fca770bdd36f64c7590d6c9b0fe072/08276495afa80047-9a/s540x810/1c523dab114ee68d659b4299b4f99c3b56828437.gif",
            "https://64.media.tumblr.com/9febc49bab550b5028dddbdb30424380/26663c1041777db4-8f/s540x810/f925a30ef6b0d00ad09babcd0ae762140d719bd8.gif",
            "https://64.media.tumblr.com/e21ce025a6f6bc589abb81b9cb5e9d3d/26663c1041777db4-5b/s540x810/d41a7d0c57cf086158d5fe6686756926877d57ee.gif",
            "https://64.media.tumblr.com/36ae348900c3619aee82fafcef083031/e594d7e906c544b3-f2/s540x810/3fbdc76c0abca6258f5d7773e55f2889a00472de.gif",
            "https://64.media.tumblr.com/72ebf4168757db6aa672e52d00b79261/1a3cc3a9a1f6c780-1b/s540x810/7122fa841ef33887f9a4d6b480960da03e87ac76.gif",
            "https://64.media.tumblr.com/5d01e4447e247a53cc7d9752ed20698c/914952c0dcacdc5c-ce/s400x600/a508f6f846f01d80a49ecb4794b129ab18f2b27f.gif",
            "https://64.media.tumblr.com/1a8eeb197bf1c467de6762b21fcdac3d/e160b9226f0547d2-37/s540x810/928ab1dd0be8c98845cb7238100cf1b30e42861d.gif",
            "https://64.media.tumblr.com/404b43eef586e6ac10ca81151461c7b7/02dd6157928776bb-9e/s400x600/bdaedaa1ff7b5613c94e62f9188e1c6e78083db4.gif",
            "https://64.media.tumblr.com/930ec1f773c35af161f3f3ed54a77abc/c0a06dfaf48d12c1-0e/s400x600/bef69586c43dd5ceead5ab2ba3609f12654870bb.gif",
            "https://64.media.tumblr.com/56bae0d6d9cf4df0d74415d0e992f0f2/c0a06dfaf48d12c1-be/s400x600/a7b99b16ed9e7588af269dc3900a948e69582ac1.gif",
            "https://64.media.tumblr.com/afc1f4ca2487ddfba95607d5904e42c7/c0a06dfaf48d12c1-08/s400x600/7a8a5b7b9d9c9aca9ac1ef8645c1abc681ea729f.gif",
            "https://64.media.tumblr.com/de9de3d0cec2e2c3c673bd734cc3f64d/c0a06dfaf48d12c1-9c/s400x600/1008bac1aab53efbf005c9e073eb5442318ef18b.gif",
            "https://64.media.tumblr.com/10b89178fa90fb6fed5a9cd052c75f05/6610ad9bd320d8c4-59/s540x810/bdf2a871a88a02b0e933b6cec9bb0256c27fdb1d.gif",
            "https://64.media.tumblr.com/8bb07a1989d1473c3c361850db0dce3c/6610ad9bd320d8c4-5e/s540x810/1e18b1e5225c449e1c6e4cc5bdd1afd62468ab0e.gif",
            "https://64.media.tumblr.com/028cca5de183e0a0e8273bd082017fd4/6610ad9bd320d8c4-0c/s540x810/0789ca4bc9c1f2529d2c3293072869ed1bc4be17.gif",
            "https://64.media.tumblr.com/8f0dfed017387c170e20228eba7015f1/58e45ff6d37fb9e8-57/s540x810/862d5d4da4f12b43d27da95b5f0f021331c3f4f5.gif",
            "https://64.media.tumblr.com/d18139ac3fa018769d7323ad235a87de/9d91507a0a73417c-02/s400x600/1407f2517a3d944dc7d129f81a9c36d6c581a2f4.gif",
            "https://64.media.tumblr.com/e7868c7f17bf647e3e801e265717701b/c783e07b4a9a2f4c-07/s540x810/fd2838ca224e1a2416f0b7a632f687a25308f8bb.gif",
            "https://64.media.tumblr.com/82bdc84f41f36c594102871b243d0236/c783e07b4a9a2f4c-a0/s540x810/8412ed29c3ea72cb8070b0159ef8a03786908e56.gif",
            "https://64.media.tumblr.com/8406c3f1768a6faac1c6954e921cf18c/c783e07b4a9a2f4c-36/s540x810/3d3e92156b1cdd1bf1c81525fd129e6657eb787d.gif",
            "https://64.media.tumblr.com/5ec003e2d80668d19cc83e797f583b7c/471ded0fdfbbb88f-89/s540x810/e2a10d4d2eff8bee310c1cf095a26e981f6fd13b.gif",
            "https://64.media.tumblr.com/0453d2a7a04965200d5f4ca75bddb9ba/471ded0fdfbbb88f-35/s540x810/fa868508fa1b5f2e2b35f35b037f2627e8a73567.gif",
            "https://64.media.tumblr.com/4adae640b0a3f8f34e4404f724a4a5ae/bf505a7169d86a31-39/s400x600/d41a93d052e31138ad9633be8c356c929d8e401b.gif",
            "https://64.media.tumblr.com/ae1421ecf2b52a263a0c1f54cd764083/bf505a7169d86a31-d1/s400x600/a62188c608d2c4b5030a2f2d103c6089888befaa.gif",
            "https://64.media.tumblr.com/926b25a1335fd4a69d9dafd52491ed6a/3dfcbe16e22b7ea0-66/s400x600/448fe2a885bb9d49d1acb32edfb0b20f4f405729.gif",
            "https://64.media.tumblr.com/0961329165a8226342e9257c43f66487/bf505a7169d86a31-ba/s400x600/82adb7a3e899195666cbf5d4e17675371d65cdd9.gif",
            "https://64.media.tumblr.com/05b791a75b0be45d6406b86bb52c4de8/4417d615d52bc49a-44/s400x600/179553aa94554834e1db0771e5e643c96c267f09.gif",
            "https://64.media.tumblr.com/b27430d05c10e2326ec64006ed93a7e2/6bf05373b8ea88fe-a4/s400x600/c745d70a92a57dbe920791960aa3333c1bf25461.gif",
            "https://64.media.tumblr.com/cdec832fda8bdbb438805cec91bf5cde/de720c64d877c65f-72/s400x600/4d83a6639e4d5805fcf04c0d083ed4880dd83bd2.gif",
            "https://64.media.tumblr.com/787a8027f119242c5e915b9d0ccb1aba/de720c64d877c65f-a3/s400x600/5958deb7bd9f0acdd1859307d370c4ac1d60a7b9.gif",
            "https://64.media.tumblr.com/12f1c42fb98bdba447a04206fa28632c/tumblr_p3v0v4l3JZ1r7qnpao4_400.gif"]

        self.bot.boa_gif = ["https://cdn.discordapp.com/attachments/813116899822665808/813118089570811904/Tumblr_l_420116355437913.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813118089918152745/Tumblr_l_420117988260047.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813118090253566023/Tumblr_l_420125337303118.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813118092116885574/Tumblr_l_420122076119838.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813118493699604520/Tumblr_l_420216199901573.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813118494538334223/Tumblr_l_420212653551105.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813118495746949150/Tumblr_l_420209104378554.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813118496182763540/Tumblr_l_420206990517826.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813118856288665641/Tumblr_l_420277069443789.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813118856880586792/Tumblr_l_420278151235247.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813118873184239626/Tumblr_l_420286365829827.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813118874622230569/Tumblr_l_420289408967690.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813119023494856714/Tumblr_l_420349276899647.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813119024091234304/Tumblr_l_420346529622929.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813119024786440262/Tumblr_l_420344129463451.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813119049570451496/Tumblr_l_420329229533509.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813119129842090004/Tumblr_l_420369074636618.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813119240571322398/Tumblr_l_420386390240362.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813119549930995772/Tumblr_l_420455539961690.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813119550773002250/Tumblr_l_420451611661639.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813119573380956180/Tumblr_l_420417323903319.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813119573984411649/Tumblr_l_420416088638632.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813119698228609104/Tumblr_l_420505971332712.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813119698791170088/Tumblr_l_420508241829222.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813120035555246120/Tumblr_l_420588109321379.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813120036121739326/Tumblr_l_420586021987213.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813120036670668820/Tumblr_l_420583558405130.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813120037158256670/Tumblr_l_420581844671641.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813120181681127464/Tumblr_l_420624675734333.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813120182251683844/Tumblr_l_420622339580741.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813120182918709258/Tumblr_l_420620569739908.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813120250731561000/Tumblr_l_420641163717452.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813120383070109736/Tumblr_l_420668274104733.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813120384102301757/Tumblr_l_420671929983013.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813120384941293599/Tumblr_l_420665368888172.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813120504608063538/Tumblr_l_420701262942637.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813120505376014336/Tumblr_l_420703912102845.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813120593414848553/Tumblr_l_420723207013098.gif",
            "https://cdn.discordapp.com/attachments/813116899822665808/813120594190008380/Tumblr_l_420724838336170.gif"]

    @commands.command()
    async def natty(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Natty | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Natty :teddy_bear:')
                await ctx.send(random.choice(self.bot.natty_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Natty :teddy_bear:')
            await ctx.send(random.choice(self.bot.natty_gif))
            await ctx.message.delete()

    @commands.command()
    async def alexa(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [AleXa | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about AleXa :blue_heart:')
                await ctx.send(random.choice(self.bot.alexa_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about AleXa :blue_heart:')
            await ctx.send(random.choice(self.bot.alexa_gif))
            await ctx.message.delete()

    @commands.command(aliases = ['chung'])
    async def chungha(self, ctx, arg="ha"):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Chung Ha | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "ha":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Chung Ha :heart:')
                    await ctx.send(random.choice(self.bot.chungha_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chung Ha :heart:')
                await ctx.send(random.choice(self.bot.chungha_gif))
                await ctx.message.delete()

    @commands.command()
    async def iu(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [IU | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about IU <:blueming:787451831478910996>')
                await ctx.send(random.choice(self.bot.iu_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about IU <:blueming:787451831478910996>')
            await ctx.send(random.choice(self.bot.iu_gif))
            await ctx.message.delete()

    @commands.command()
    async def somi(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Somi | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Somi :heart:')
                await ctx.send(random.choice(self.bot.somi_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Somi :heart:')
            await ctx.send(random.choice(self.bot.somi_gif))
            await ctx.message.delete()

    @commands.command()
    async def yukika(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Yukika | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yukika :heart:')
                await ctx.send(random.choice(self.bot.yukika_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yukika :heart:')
            await ctx.send(random.choice(self.bot.yukika_gif))
            await ctx.message.delete()

    @commands.command()
    async def taemin(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Taemin | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Taemin :baby::cheese:')
            await ctx.send(random.choice(self.bot.taemin_gif))
            await ctx.message.delete()

    @commands.command()
    async def woodz(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [WOODZ | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary and channel != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about WOODZ :heart:')
            await ctx.send(random.choice(self.bot.woodz_gif))
            await ctx.message.delete()

    @commands.command()
    async def kris(self, ctx, arg = "wu"):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Kris Wu | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "wu":
            if ctx.guild.id == luminary and channel != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Kris Wu :heart:')
                await ctx.send(random.choice(self.bot.kriswu_gif))
                await ctx.message.delete()

    @commands.command()
    async def luhan(self, ctx): 
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Luhan | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary and channel != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Luhan :heart:')
            await ctx.send(random.choice(self.bot.luhan_gif))
            await ctx.message.delete()

    @commands.command()
    async def tao(self, ctx): 
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Tao | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary and channel != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Tao :heart:')
            await ctx.send(random.choice(self.bot.tao_gif))
            await ctx.message.delete()

    @commands.command()
    async def kang(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Kang Daniel | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "daniel":
            if ctx.guild.id == luminary and channel != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Kang Daniel :heart:')
                await ctx.send(random.choice(self.bot.kangdaniel_gif))
                await ctx.message.delete()

    @commands.command()
    async def sunmi(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Sunmi] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary and channel != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Sunmi :heart:')
            await ctx.send(random.choice(self.bot.sunmi_gif))
            await ctx.message.delete()

    @commands.command()
    async def yubin(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Yubin | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary and channel != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yubin :heart:')
            await ctx.send(random.choice(self.bot.yubin_gif))
            await ctx.message.delete()

    @commands.command()
    async def rothy(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Rothy | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary and channel != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Rothy :heart:')
            await ctx.send(random.choice(self.bot.rothy_gif))
            await ctx.message.delete()

    @commands.command()
    async def hyuna(self, ctx):
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Hyuna :heart:')
            await ctx.send(random.choice(self.bot.hyuna_gif))
            await ctx.message.delete()
    
    @commands.command()
    async def boa(self, ctx):
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about BoA :heart:')
            await ctx.send(random.choice(self.bot.boa_gif))
            await ctx.message.delete()


def setup(client):
    client.add_cog(SoloPings(client))