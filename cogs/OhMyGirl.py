import discord, random
from discord.ext import commands
from datetime import datetime

#//servers
luminary = 758468592957521972

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

class OhMyGirl(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.ohmygirl_arin_gif = ["https://gfycat.com/rapidregalkingsnake-oh-my-girl-arin-kpop",
            "http://gfycat.com/GorgeousThinGrayreefshark",
            "https://gfycat.com/regulartidycrow",
            "https://gfycat.com/frenchbrowngalapagosdove",
            "https://gfycat.com/wholeillustriousboar",
            "https://gfycat.com/frigidsmoothbaleenwhale",
            "https://tenor.com/view/arin-gif-19615783",
            "https://tenor.com/view/arin-omg-oh-my-girl-confused-maknae-gif-11167451",
            "https://tenor.com/view/arin-oh-nari-oh-my-girl-kpop-when-crush-is-flirting-with-other-girl-gif-18284767",
            "https://tenor.com/view/arin-dance-ohmygirl-mylove-nui-gif-19089552",
            "https://tenor.com/view/%EC%95%84%EB%A6%B0-%EC%98%A4%EB%A7%88%EC%9D%B4%EA%B1%B8-arin-maknae-ohmygirl-gif-18617575",
            "https://tenor.com/view/ohmygirl-arinohmygirl-arin-gif-19590171",
            "https://tenor.com/view/arin-ohmygirl-gif-7348565",
            "https://tenor.com/view/arin-ohmygirl-gif-7348613",
            "https://tenor.com/view/arin-arinohmygirl-ohmygirl-gif-19590570",
            "https://tenor.com/view/arin-kpop-oh-nari-ohmygirl-%EC%95%84%EB%A6%B0-gif-18284837",
            "https://tenor.com/view/arinohmygirl-arin-ohmygirl-gif-19590229",
            "https://tenor.com/view/arinohmygirl-arin-ohmygirl-gif-19590295",
            "https://tenor.com/view/arinohmygirl-arin-ohmygirl-gif-19590311",
            "https://tenor.com/view/arin-ohmygirl-arinohmygirl-gif-19590617",
            "https://tenor.com/view/arinohmygirl-arin-ohmygirl-kpop-gif-19590712",
            "https://tenor.com/view/oh-my-girl-omg-kpop-cute-pretty-gif-17578691",
            "https://tenor.com/view/arin-ohmygirl-gif-19627547",
            "https://tenor.com/view/arin-ohmygirl-gif-19627552",
            "https://tenor.com/view/arin-oh-my-girl-k-pop-cute-gif-10864594",
            "https://tenor.com/view/arin-oh-na-ri-oh-my-girl-girls-world-kpop-gif-18284697",
            "https://tenor.com/view/arin-oh-my-girl-fresh-look-%EC%95%84%EB%A6%B0-%EC%98%A4%EB%A7%88%EC%9D%B4%EA%B1%B8-gif-18617383",
            "https://tenor.com/view/arin-oh-my-girl-%EC%95%84%EB%A6%B0-%EC%98%A4%EB%A7%88%EC%9D%B4%EA%B1%B8%EC%95%84%EB%A6%B0-kpop-gif-19649272",
            "https://tenor.com/view/%EC%95%84%EB%A6%B0-%EC%B5%9C%EC%95%84%EB%A6%B0-arin-oh-my-girl-maknae-gif-19834825",
            "https://tenor.com/view/arin-dane-arin-gif-19063881",
            "https://tenor.com/view/arin-gif-19615781",
            "https://tenor.com/view/arin-choi-arin-oh-my-girl-maknae-gif-19835052",
            "https://tenor.com/view/arin-approved-oh-my-girl-oh-my-girl-arin-arin-choiarin-gif-7566702",
            "https://tenor.com/view/%EC%82%B4%EC%A7%9D%EC%84%A4%EB%A0%9C%EC%96%B4-%EC%98%A4%EB%A7%88%EC%9D%B4%EA%B1%B8-%EC%95%84%EB%A6%B0-%EC%82%B4%EC%A7%9D-%EC%84%A4%EB%A0%9C%EC%96%B4-gif-18599815",
            "https://tenor.com/view/arin-gif-18197837",
            "https://tenor.com/view/arin-gif-19615785",
            "https://tenor.com/view/arin-gif-19588473",
            "https://tenor.com/view/%EC%95%84%EB%A6%B0-%EC%98%A4%EB%A7%88%EC%9D%B4%EA%B1%B8%EC%95%84%EB%A6%B0-arin-ohmygirl-arin-kpop-gif-18295336",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19768503",
            "https://tenor.com/view/oh-my-girl-arin-gif-19488436",
            "https://giphy.com/gifs/O7AeKvp0MupNY3NT9p",
            "https://giphy.com/gifs/Jsxp4ocCylbpDnJS4D",
            "https://giphy.com/gifs/O4ijB9LRCEoooUPEkI",
            "https://giphy.com/gifs/LXcTNZZQUA3BKGJATM",
            "https://giphy.com/gifs/vUd4g8HpiqPhq8d8S2",
            "https://giphy.com/gifs/OSqLtOHD6CzhXHHSyb",
            "https://gfycat.com/neglectedspitefulasianwaterbuffalo",
            "https://gfycat.com/compassionatealivelangur-oh-my-girl-kpop-arin-omg",
            "https://gfycat.com/consciousjitteryinexpectatumpleco",
            "https://giphy.com/gifs/adBnV0HzCbW5ppwzVB",
            "https://giphy.com/gifs/RDVsYATtSE2sb2meBR",
            "https://giphy.com/gifs/7QelThWYjD5IaSG0TU",
            "https://giphy.com/gifs/g1xNeIilxCkqwoXHhK",
            "https://giphy.com/gifs/K1TrJ6rrXOyzNBO93g",
            "https://gfycat.com/spitefulfairkillerwhale",
            "https://gfycat.com/classicnearincatern",
            "https://gfycat.com/eagerindolentcorydorascatfish",
            "https://gfycat.com/scalyportlyheifer",
            "https://gfycat.com/legalunrealisticjumpingbean",
            "https://gfycat.com/disastrousflimsyharvestmouse",
            "https://gfycat.com/eminentsinglefinnishspitz",
            "https://gfycat.com/aridmilkygemsbuck",
            "https://gfycat.com/poisedbouncybronco",
            "https://gfycat.com/unrulyeuphoricchinesecrocodilelizard",
            "https://64.media.tumblr.com/018b87a68cce96964a13a700abd3488c/f37e3274107337e8-37/s540x810/b5a77c492cc8543723f295c9e2c5d4da69b08a51.gif",
            "https://64.media.tumblr.com/b43bbd47f9c320c99779977d17ac378d/f37e3274107337e8-36/s540x810/2759b1f398f66bbeebe859fb986eb9a2478a2724.gif",
            "https://64.media.tumblr.com/7d5c53110b464ab6685882fe369ea59d/f37e3274107337e8-27/s540x810/acea612b4c489a7a0588f0e6d6cdde266c987b8f.gif",
            "https://giphy.com/gifs/byH9qA1V3yFBkUaiD6",
            "https://giphy.com/gifs/DCK1grB526enocS3qi",
            "https://giphy.com/gifs/KqqQ8P2La1zPMQYpzb",
            "https://giphy.com/gifs/tMTvYkJbMc9vOm46RZ",
            "https://giphy.com/gifs/WhuA4kk8SKGnR1AUGE",
            "https://giphy.com/gifs/zlPmeB2uzWndDhAvB9",
            "https://giphy.com/gifs/yRRyuQzbLZfEugzcGA",
            "https://giphy.com/gifs/a9GVnFn5XOuNlChKc7",
            "https://giphy.com/gifs/zHCTzu1rH4h9BIQxnf",
            "https://giphy.com/gifs/jo8ix68QT4mVtfnlCC",
            "https://giphy.com/gifs/xUQqxdL8XW2tWtouLZ",
            "https://giphy.com/gifs/yUFeO68Wozdqi2zsV1",
            "https://giphy.com/gifs/z0KqFF7l4eD0Aou7Gm",
            "https://giphy.com/gifs/FwftfqTHKI6KBU6iZI",
            "https://giphy.com/gifs/zNheh7uj9dFrVXSCtw",
            "https://giphy.com/gifs/vCWQls41L7WKf3emip",
            "https://giphy.com/gifs/y5crJmBABvbxDMwbpd",
            "https://gfycat.com/illegaldishonestaracari",
            "https://gfycat.com/spitefulimpishhog",
            "https://gfycat.com/carefulgrossgangesdolphin",
            "https://gfycat.com/zigzagclassiciceblueredtopzebra",
            "https://gfycat.com/immaterialsnoopydikkops",
            "https://64.media.tumblr.com/2c8668a4224b322595453a1f91759a13/a55ee6c002ff1f31-b9/s400x600/bf876da40efee5d09fc7ba0ac08f08cf171fbdaa.gif",
            "https://64.media.tumblr.com/067dc7dec45491c2729c5a315d4e61e3/a55ee6c002ff1f31-0e/s400x600/6f9a7673339747b19f3ab81b172d5a2a6f35e3c0.gif"]

        self.bot.ohmygirl_binnie_gif = ["https://gfycat.com/sadlonegalapagosdove",
            "https://tenor.com/view/oh-my-girl-kpop-hi-wave-binnie-gif-15821110",
            "https://tenor.com/view/oh-my-girl-nods-binnie-gif-15516237",
            "https://tenor.com/view/oh-my-girl-binnie-smiliing-thumbs-up-okay-gif-6023652",
            "https://tenor.com/view/oh-my-girl-binnie-headset-cute-smile-gif-15422340",
            "https://tenor.com/view/oh-my-girl-binnie-heart-cute-pretty-gif-15486924",
            "https://tenor.com/view/oh-my-girl-binnie-cute-smile-pretty-gif-15486918",
            "https://tenor.com/view/oh-my-girl-binnie-so-cute-cute-pretty-gif-15534812",
            "https://tenor.com/view/oh-my-girl-binnie-cute-smile-kpop-gif-15586122",
            "https://tenor.com/view/oh-my-girl-binnie-smile-cute-eyeglasses-gif-15586120",
            "https://tenor.com/view/oh-my-girl-binnie-party-hat-eating-hungry-gif-15813573",
            "https://tenor.com/view/oh-my-girl-binnie-what-gif-16233447",
            "https://tenor.com/view/oh-my-girl-binnie-laugh-gif-16233448",
            "https://tenor.com/view/oh-my-girl-binnie-heart-cute-gif-16233454",
            "https://tenor.com/view/oh-my-girl-binnie-shower-sing-gif-16233451",
            "https://tenor.com/view/binnie-oh-my-girl-kpop-cute-gif-14728577",
            "https://tenor.com/view/oh-my-girl-binnie-oh-my-gif-15422337",
            "https://tenor.com/view/bae-yoobin-binnie-binnie-oh-my-girl-dance-gif-15125077",
            "https://tenor.com/view/binnie-binnie-oh-my-girl-bae-yoobin-kpop-windy-gif-15131354",
            "https://tenor.com/view/binnie-binnie-oh-my-girl-bae-yoobin-peace-sign-kpop-gif-15131355",
            "https://tenor.com/view/binnie-binnie-oh-my-girl-bae-yoobin-me-kpop-gif-15131357",
            "https://tenor.com/view/oh-my-girl-binnie-cute-short-hair-happy-gif-15586118",
            "https://tenor.com/view/oh-my-girl-binnie-laugh-happy-cute-gif-15813570",
            "https://tenor.com/view/oh-my-girl-binnie-dance-cool-moves-gif-15856553",
            "https://tenor.com/view/oh-my-girl-binnie-wave-hi-cute-gif-15856563",
            "https://gfycat.com/freshreadyindianjackal",
            "https://gfycat.com/misguidedbarearmyant",
            "https://gfycat.com/paledishonestbrocketdeer/",
            "https://64.media.tumblr.com/56573e5b71572dcd62a1ee0f4e72a77c/7f5c9251cbed597c-b4/s540x810/1bfda25339a28c2d75da17fb03ad1b5a3be6445f.gif",
            "https://gfycat.com/memorablesmoothfurseal",
            "https://gfycat.com/vacantsimplistichyracotherium",
            "https://gfycat.com/decentleafyhornbill"]

        self.bot.ohmygirl_hyojung_gif = ["https://tenor.com/view/oh-my-girl-cute-girl-smile-illusion-gif-16725606",
            "https://tenor.com/view/lol-rofl-laughing-laugh-oh-my-girl-gif-14647344",
            "https://tenor.com/view/hyojung-oh-my-girl-kpop-candy-cute-gif-15174724",
            "https://tenor.com/view/hyo-jung-ohmygirl-two-hyo-jungs-gif-11362670",
            "https://tenor.com/view/hyojung-gif-17985829",
            "https://tenor.com/view/hyojung-choihyojung-oh-my-girl-candyleader-leader-gif-19591309",
            "https://tenor.com/view/choihyojung-hyojung-ohmygirl-candyleader-gif-19591317",
            "https://tenor.com/view/hyojung-gif-19591387",
            "https://tenor.com/view/hyojung-gif-19591416",
            "https://tenor.com/view/%ED%9A%A8%EC%A0%95-hyojung-gif-19600566",
            "https://tenor.com/view/%ED%9A%A8%EC%A0%95-hyojung-gif-19600428",
            "https://tenor.com/view/hyojung-%ED%9A%A8%EC%A0%95-gif-19639358",
            "https://tenor.com/view/hyojung-%ED%9A%A8%EC%A0%95-gif-19703279",
            "https://tenor.com/view/%ED%9A%A8%EC%A0%95-hyojung-gif-19703281",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19768489",
            "https://tenor.com/view/%ED%9A%A8%EC%A0%95-hyojung-gif-19703302",
            "https://tenor.com/view/%ED%9A%A8%EC%A0%95-hyojung-gif-19790779",
            "https://tenor.com/view/%ED%9A%A8%EC%A0%95-hyojung-gif-19790850",
            "https://tenor.com/view/hyojung-gif-19800689",
            "https://tenor.com/view/hyojung-gif-19800690",
            "https://tenor.com/view/hyojung-gif-19800691",
            "https://tenor.com/view/hyojung-gif-19800693",
            "https://tenor.com/view/hyojung-gif-19800694",
            "https://tenor.com/view/hyojung-gif-19800695",
            "https://tenor.com/view/hyojung-gif-19857821",
            "https://tenor.com/view/hyojung-gif-19857822",
            "https://tenor.com/view/choi-hyojung-hyojung-gif-19591487",
            "https://tenor.com/view/hyojung-gif-19857823",
            "https://gfycat.com/forcefuldisfiguredbluejay",
            "https://64.media.tumblr.com/af5d84772db5def9ba542ef3130e6ab8/657de7c7f2a01662-58/s540x810/ab2e72587d473d5bcc6bb4a6eb933cc8483e78da.gif",
            "https://64.media.tumblr.com/452915363cf265f9f551664d00002f52/657de7c7f2a01662-ab/s540x810/4288fb50131941c4afb9ab60f96d92a3dff20b74.gif",
            "https://64.media.tumblr.com/5e61f7799a4b8eceefb9912538716092/657de7c7f2a01662-aa/s540x810/2d3d704bed0422b5aa0189ba4156ce57cda1e4e8.gif"]

        self.bot.ohmygirl_jiho_gif = ["https://gfycat.com/velvetywildcowbird",
            "https://tenor.com/view/jiho-omg-oh-my-girl-kim-jiho-kpop-gif-17349420",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19796935",
            "https://tenor.com/view/oh-my-girl-jiho-kim-jiho-kpop-bye-gif-16936859",
            "https://tenor.com/view/oh-my-girl-jiho-pew-pew-gif-14581615",
            "https://tenor.com/view/oh-my-girl-kpop-jiho-gif-13994116",
            "https://tenor.com/view/kpop-oh-my-girl-kim-jiho-jiho-pretty-gif-17096348",
            "https://tenor.com/view/oh-my-girl-jiho-kim-jiho-kpop-kawaii-gif-16936836",
            "https://tenor.com/view/jiho-omg-oh-my-girl-kim-jiho-kpop-gif-17349426",
            "https://tenor.com/view/jiho-omg-oh-my-girl-kim-jiho-kpop-gif-17349428",
            "https://tenor.com/view/jiho-omg-oh-my-girl-kim-jiho-kpop-gif-17349421",
            "https://tenor.com/view/kpop-oh-my-girl-kim-jiho-jiho-pretty-gif-17096350",
            "https://tenor.com/view/kim-jiho-jiho-omg-oh-my-girl-kpop-gif-17514374",
            "https://tenor.com/view/jiho-kim-jiho-oh-my-girl-dancing-dance-gif-15912862",
            "https://tenor.com/view/kim-jiho-jiho-omg-oh-my-girl-kpop-gif-17514371",
            "https://tenor.com/view/jiho-kim-jiho-oh-my-girl-k-pop-gif-11085667",
            "https://tenor.com/view/oh-my-girl-jiho-clap-applause-gif-14581662",
            "https://tenor.com/view/oh-my-girl-jiho-princess-korean-smile-gif-14581638",
            "https://tenor.com/view/kpop-oh-my-girl-jiho-singing-gif-13982656",
            "https://tenor.com/view/jiho-oh-my-girl-kpop-binnie-gif-15174709",
            "https://tenor.com/view/jiho-oh-my-girl-bye-cute-gif-14786179",
            "https://tenor.com/view/jiho-oh-my-girl-kpop-gif-11085635",
            "https://tenor.com/view/jiho-ohmygirl-gif-19507110",
            "https://gfycat.com/nastyverifiableanole",
            "https://gfycat.com/assuredboldhyena",
            "https://gfycat.com/sparsebarecreature",
            "https://gfycat.com/optimisticagreeableindianpalmsquirrel",
            "https://gfycat.com/gaseoussoupyarcticwolf",
            "https://gfycat.com/fluiduncommonaurochs",
            "https://gfycat.com/energeticweakblackbuck",
            "https://gfycat.com/evenicydrongo-dun-dun-dance-oh-my-girl-jiho-kpop//",
            "https://gfycat.com/wealthyseriousivorybilledwoodpecker//",
            "https://64.media.tumblr.com/65d3e362b8187cfa22dd222c70aa8f42/e0329000673f1249-70/s540x810/42950510ffb8626eb631c302f98c0480fb3c1a9c.gif",
            "https://64.media.tumblr.com/e06dd5b2218d85ff6f2f42974df7d8b0/e0329000673f1249-31/s540x810/efd70f1046a2e9b38faac47acfdf59dc809b5c74.gif",
            "https://64.media.tumblr.com/9ad975d04bee722734975b101fc85738/e0329000673f1249-08/s540x810/bce8470e5b270be323d3fa4c9dccf7c1525e42ba.gif",
            "https://64.media.tumblr.com/6d1c314867e7c7163d90d60572a8ad82/fc35c79a2e846ef9-5c/s540x810/72e97dcbdec6f2718e96f20dd77b128595bc9c5c.gif",
            "https://64.media.tumblr.com/92a0c8f9a255ff78772222a23d7ba7de/fc35c79a2e846ef9-ec/s540x810/cba3cd5c87def72c0a039ca79a10927d3cffe946.gif",
            "https://64.media.tumblr.com/ffac9139951a66f853287b51400088e2/0cafe4e17e71ece3-34/s400x600/8f5d2fcb01b62c6fa5f23872e63b70c15ea56f8c.gif",
            "https://64.media.tumblr.com/c377397c9ae563d0ff468f77baac7b5f/0cafe4e17e71ece3-be/s400x600/bc534b2ced84594ddd054e4ad2631aa3300b04f2.gif",
            "https://64.media.tumblr.com/620e90734f3b96b6997431d87465fded/0cafe4e17e71ece3-c7/s400x600/3619ce9a41a90de01f7031b92430b860b6bdcf16.gif",
            "https://64.media.tumblr.com/d8652208ce2a7501d3e9981c9123378b/0cafe4e17e71ece3-ee/s400x600/d17bf14bc4d5d990463ca03edf4c5c65caea26f0.gif",
            "https://gfycat.com/fickletestyangelfish",
            "https://64.media.tumblr.com/6613d565e264a905276fc91935490722/a88452058becac78-0d/s400x600/01f17d1f2950419a70349b195d120942dac4ea1a.gif",
            "https://64.media.tumblr.com/624fd1603bc5356d4a388ec53c6e3e07/a88452058becac78-3a/s400x600/ef798bef1febbad6680575fed521542e4e044657.gif",
            "https://64.media.tumblr.com/2fe011813b2acc931996cf413cb0dfaa/a88452058becac78-94/s400x600/9114967c724004d4f003ddfc4e539208796776de.gif",
            "https://64.media.tumblr.com/520c601a814c7096391c6b5b4c89c6db/a88452058becac78-c0/s400x600/35ba4e52b555df781b15285b9e3cba7767cd1c2a.gif",
            "https://gfycat.com/selfreliantvainabyssiniangroundhornbill",
            "https://gfycat.com/disfiguredanotherindusriverdolphin"]

        self.bot.ohmygirl_mimi_gif = ["https://tenor.com/view/mimi-oh-my-girl-rap-forehead-mic-gif-15514487",
            "https://tenor.com/view/ohmygirl-mimi-gif-19477876",
            "https://tenor.com/view/ohmygirl-mimi-gif-19477868",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19796894",
            "https://tenor.com/view/oh-my-girl-mimi-wink-smile-gif-16233449",
            "https://tenor.com/view/mimi-mihyun-oh-my-girl-blonde-kpop-gif-15149089",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19796931",
            "https://tenor.com/view/mimi-oh-my-girl-cute-kiss-gif-15401382",
            "https://tenor.com/view/ohmygirl-mimi-gif-6083158",
            "https://tenor.com/view/mimi-ohmygirl-windyday-gif-6083154",
            "https://tenor.com/view/ohmygirl-mimi-gif-6083155",
            "https://tenor.com/view/mimi-birthday-mimi-mimi-omg-mimi-oh-my-girl-oh-my-girl-gif-19911544",
            "https://tenor.com/view/mimi-mimi-oh-my-girl-omg-oh-my-girl-mimi-kim-mihyun-gif-19911077",
            "https://gfycat.com/anyfaintcaterpillar",
            "https://gfycat.com/belovedzestyfoxterrier",
            "https://gfycat.com/apprehensivewelltodoirishredandwhitesetter",
            "https://gfycat.com/barefearfulgermanshepherd",
            "https://gfycat.com/livelyagonizingleafwing-oh-my-girl-mimi",
            "https://gfycat.com/athleticadolescentindianelephant",
            "https://gfycat.com/fewgloomyaustralianshelduck",
            "https://gfycat.com/magnificentidenticalaffenpinscher-oh-my-girl-mimi",
            'https://gfycat.com/periodicdentaladdax-oh-my-girl-mimi',
            "https://gfycat.com/bitterhonoredafricangroundhornbill-oh-my-girl-supadupa-arin-kpop-vlog",
            "https://gfycat.com/elatedvapidbarb-gdragon-cover-oh-my-girl-mdromeda-omaigeol-kpop",
            "https://gfycat.com/uniquemessykangaroo-oh-my-girl-behind-bungee-omaigeol-kpop-vlog",
            "https://gfycat.com/maturewaryfoxhound-oh-my-girl-dolphin-fancam-mimi-kpop",
            "https://gfycat.com/homelysomedugong-weekly-idol-oh-my-girl-variety-kpop-omaigeol-mimi",
            "https://gfycat.com/equallargeblueshark-the-fifth-season-oh-my-girl-aesthetics-ssfwl",
            "https://gfycat.com/hugeplastichypsilophodon-weekly-idol-oh-my-girl-variety-kpop-omaigeol-mimi",
            "https://gfycat.com/fortunateamazinghoiho-oh-my-girl-ssfwl-kpop-mimi",
            "https://gfycat.com/palerevolvingguineapig",
            "https://gfycat.com/glamorousweirdamericanbobtail",
            "https://gfycat.com/unsightlyfancybluejay",
            "https://gfycat.com/clutteredimpartialindianspinyloach",
            "https://gfycat.com/meatyshychickadee",
            "https://gfycat.com/inferioroddballivorybilledwoodpecker",
            "https://gfycat.com/impishreadybronco",
            "https://64.media.tumblr.com/c54beb1ea5d14bad80c77d4b426c5e61/8cf2e822f5e0d778-76/s400x600/f1af1f06f9df32823af30d0fe1fdbd721e5550ef.gif",
            "https://64.media.tumblr.com/b5fb74f0e86c17b584df4d5bb4895ba0/8cf2e822f5e0d778-6c/s400x600/41029163986e09b9169b9633dd3b89c17be3ddb6.gif",
            "https://64.media.tumblr.com/c4f1307e239ee7e1c7b2e73b80e43385/8cf2e822f5e0d778-10/s400x600/8490a3809738e6836928d8ccf62dbd45deb4cf66.gif/"]

        self.bot.ohmygirl_seunghee_gif = ["https://tenor.com/view/aww-jiggle-ohmygirl-pout-korean-gif-18118579",
            "https://gfycat.com/bountifulbronzekarakul",
            "https://gfycat.com/demandingnauticalankolewatusi",
            "https://gfycat.com/specificmammothimago",
            "https://gfycat.com/memorableweticelandicsheepdog",
            "https://gfycat.com/belatedfrighteningamericancrow",
            "https://tenor.com/view/seunghee-ohmygirl-gif-7956413",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19796891",
            "https://tenor.com/view/seunghee-oh-my-girl-bungee-oh-my-girl-bungee-kpop-gif-14748328",
            "https://tenor.com/view/oh-my-girl-seunghee-cute-gif-15318622",
            "https://tenor.com/view/oh-my-girl-seunghee-binnie-what-shocked-gif-16233453",
            "https://tenor.com/view/oh-my-girl-seunghee-cute-smirk-kpop-gif-15813574",
            "https://gfycat.com/farinsignificantguanaco",
            "https://gfycat.com/allsimilardodobird",
            "https://gfycat.com/bountifulickyleveret",
            "https://gfycat.com/physicalpassionatedarwinsfox",
            "https://gfycat.com/jealousmildbobolink",
            "https://gfycat.com/gargantuanshimmeringgraysquirrel",
            "https://gfycat.com/solidcompetentaustraliankestrel"]

        self.bot.ohmygirl_yooa_gif = ["https://gfycat.com/querulousangelicarctichare-yooa",
            "https://media.discordapp.net/attachments/643623059541983242/770648857595084832/2ac60c3d-e2fd-4649-beca-88c8cc046231.gif",
            "https://media.discordapp.net/attachments/643623059541983242/765810697668919306/a86f6994-2d5b-4e53-99d4-a9e97afe702c.gif",
            "https://media.discordapp.net/attachments/643623059541983242/762172786579472424/743ee0e1-bed3-47cd-b0df-009f52f49e24.gif",
            "https://tenor.com/view/yooa-oh-my-girl-pose-gif-13089630",
            "https://tenor.com/view/yooa-oh-my-girl-swing-gif-13089628",
            "https://tenor.com/view/yooa-oh-my-girl-windy-gif-14668696",
            "https://tenor.com/view/oh-my-girl-kpop-yooa-gif-14589516",
            "https://tenor.com/view/yooa-kpop-oh-my-girl-stare-bored-gif-14719310",
            "https://tenor.com/view/yooa-oh-my-girl-no-gif-16116013",
            "https://tenor.com/view/yooa-oh-my-girl-yes-cute-gif-16116022",
            "https://tenor.com/view/love-ent-dance-moves-cute-kpop-gif-16763464",
            "https://tenor.com/view/yooa-yoo-shiah-oh-my-girl-cute-model-gif-17136236",
            "https://tenor.com/view/cupid-yooa-yoo-shiah-shasha-gif-17230832",
            "https://tenor.com/view/yooa-oh-my-girl-gif-18411900",
            "https://tenor.com/view/%EC%82%B4%EC%A7%9D%EC%84%A4%EB%A0%9C%EC%96%B4-%EC%9C%A0%EC%95%84-%EC%98%A4%EB%A7%88%EC%9D%B4%EA%B1%B8-%EC%82%B4%EC%A7%9D-%EC%84%A4%EB%A0%9C%EC%96%B4-gif-18599365",
            "https://tenor.com/view/yooa-ohmygirl-gif-18677966",
            "https://tenor.com/view/yooa-bon-voya-bon-voyage-oh-my-girl-yen-gif-19129387",
            "https://tenor.com/view/yooa-oh-my-girl-dance-gif-19129508",
            "https://tenor.com/view/yooa-ohmygirl-kick-gif-19367595",
            "https://tenor.com/view/yooa-%EC%9C%A0%EC%95%84-gif-19536364",
            "https://tenor.com/view/yooa-gif-19800697",
            "https://tenor.com/view/yooa-gif-19800699",
            "https://tenor.com/view/yooa-gif-19800700",
            "https://tenor.com/view/yooa-gif-19845605",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19846776",
            "https://tenor.com/view/yooa-gif-9766588",
            "https://tenor.com/view/yooa-gif-19864148",
            "https://tenor.com/view/yooa-oh-my-girl-yoo-shiah-kpop-cute-gif-17057394",
            "https://tenor.com/view/yooa-oh-my-girl-cute-gif-13089631",
            "https://tenor.com/view/oh-my-girl-yooa-yoo-yeonjoo-yoo-shiah-kpop-gif-16995123",
            "https://tenor.com/view/yooa-gif-9815748",
            "https://gfycat.com/pointedagitatedbeauceron",
            "https://gfycat.com/talkativefrightenedekaltadeta",
            "https://gfycat.com/passionateweirdacornweevil",
            "https://gfycat.com/frailinfantilealbertosaurus",
            "https://gfycat.com/caringfinishedcurlew",
            "https://cdn.discordapp.com/attachments/643623059541983242/760833049712656444/8301befb-9751-4549-b05b-e63db5493a08.gif",
            "https://gfycat.com/unevendistantindianspinyloach-oh-my-girl-yooa",
            "https://gfycat.com/whoppingloathsomecanary-beauty",
            "https://tenor.com/view/yooa-gif-19800700",
            "https://gfycat.com/anyresponsiblecrow-oh-my-girl-yooa",
            "https://gfycat.com/cheeryfatherlyjerboa-oh-my-girl-kpop-yooa-dsl",
            "https://gfycat.com/bigheartedvapidleafcutterant-oh-my-girl",
            "https://gfycat.com/drearyunrulycomet",
            "https://gfycat.com/dearcelebratedcottonmouth",
            "https://gfycat.com/importantpowerfulgalapagosdove-oh-my-girl-yooa-omaigeol",
            "https://gfycat.com/defenselesselatedgermanspaniel",
            "https://gfycat.com/hideousaltruistichuman",
            "https://gfycat.com/homelyflawlessblacknorwegianelkhound",
            "https://64.media.tumblr.com/0e014b44fc8c8bdeb9444086658d6d21/d0f3d42d1f3f1ba4-d2/s400x600/8e817fc1d9fd3fb6e79c5c569680f91b8d9d0220.gif",
            "https://64.media.tumblr.com/d9d7081bd422f162f3a2521946a6d45a/d0f3d42d1f3f1ba4-66/s400x600/e7d8683acc1f5ee082efc371cefa24d2d88671d3.gif",
            "https://64.media.tumblr.com/eed0a420a6252ea8a8e42612eb03f219/d0f3d42d1f3f1ba4-76/s400x600/274505b2488cb5c5ef28c9ce2816c1cb159ccc07.gif",
            "https://64.media.tumblr.com/86c45e3b051becbab65b26d7941631a3/d0f3d42d1f3f1ba4-a5/s400x600/7e6fc93569315d8bfaf39ab0edd4f509a3732941.gif"]

    @commands.command()
    async def oh(self, ctx, my, girl, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Oh My Girl {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if my == "my" and girl == "girl":
            if arg == "arin":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Arin :heart:')
                await ctx.send(random.choice(self.bot.ohmygirl_arin_gif))
                await ctx.message.delete()
            elif arg == "binnie":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Binnie :heart:')
                await ctx.send(random.choice(self.bot.ohmygirl_binnie_gif))
                await ctx.message.delete()
            elif arg == "hyojung":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Hyojung :heart:')
                await ctx.send(random.choice(self.bot.ohmygirl_hyojung_gif))
                await ctx.message.delete()
            elif arg == "jiho":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jiho :heart:')
                await ctx.send(random.choice(self.bot.ohmygirl_jiho_gif))
                await ctx.message.delete()
            elif arg == "mimi":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Mimi :heart:')
                await ctx.send(random.choice(self.bot.ohmygirl_mimi_gif))
                await ctx.message.delete()
            elif arg == "seunghee":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Seunghee :heart:')
                await ctx.send(random.choice(self.bot.ohmygirl_seunghee_gif))
                await ctx.message.delete()
            elif arg == "yooa":
                await ctx.send(f'<@!{ctx.author.id}> is talking about YooA :heart:')
                await ctx.send(random.choice(self.bot.ohmygirl_yooa_gif))
                await ctx.message.delete()


def setup(client):
    client.add_cog(OhMyGirl(client))