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
            "https://tenor.com/view/%E0%B8%99%E0%B8%B1%E0%B8%95%E0%B8%95%E0%B8%B5%E0%B9%89-%EB%82%98%EB%9D%A0-nt-natty-natty-teddybear-gif-19176295",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-nt-bye-natty-gif-19685641",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-nt-natty-natty_gif-gif-19685636",
            "https://tenor.com/view/%eb%82%98%eb%9d%a0-nt-natty-natty_gif-clap-gif-19970078",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-nt-natty-natty_gif-gif-19650162",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%94%b0-nt-no-natty-gif-19650164",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-nt-natty-natty_gif-%eb%82%98%eb%9d%a0-gif-19577440",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-nt-natty-natty_gif-%eb%82%98%eb%9d%a0-gif-19577433",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-nt-natty-natty_gif-%eb%82%98%eb%9d%a0-gif-19577415",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-nt-natty-natty_gif-gif-19541134",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-nt-natty-natty_gif-gif-19541136",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-nt-natty-natty_gif-gif-19360528",
            "https://tenor.com/view/%eb%82%98%eb%9d%a0-%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-nt-natty-natty_gif-gif-19359281",
            "https://tenor.com/view/%eb%82%98%eb%94%b0-%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-nt-natty-natty_gif-gif-19359278",
            "https://tenor.com/view/%eb%82%98%eb%9d%a0-%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-nt-natty-natty_gif-gif-19352210",
            "https://tenor.com/view/nt-natty-natty_gif-fighting-cute-gif-19352209",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-nt-natty-natty_gif-gif-19291994",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-nt-natty-natty_gif-gif-19312129",
            "https://tenor.com/view/nt-natty-natty_gif-blow-akiss-%eb%82%98%eb%9d%a0-gif-19312127",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-nt-natty-natty_gif-gif-19359162",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-bye-nt-natty-gif-19280116",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-nt-natty-natty_gif-gif-19280119",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-dance-nt-natty-gif-19280120",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-nt-natty-natty_gif-gif-19280115",
            "https://tenor.com/view/boo-nt-natty-natty_gif-%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-gif-19241978",
            "https://tenor.com/view/%eb%82%98%eb%9d%a0-%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-nt-natty-natty_gif-gif-19241979",
            "https://tenor.com/view/heart-nt-natty-love-natty_gif-gif-19241980",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-scratch-nt-natty-gif-19241977",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-nt-natty-natty_gif-gif-19255321",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-natty-nt-cat-scratch-gif-19231828",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-nt-natty-natty-teddybear-natty_gif-gif-19231839",
            "https://tenor.com/view/%eb%82%98%eb%9d%a0-nt-natty-natty_gif-%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-gif-19231832",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-nt-natty-love-heart-gif-19240579",
            "https://tenor.com/view/%eb%82%98%eb%9d%a0-%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-nt-natty-natty_gif-gif-19240582",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-nt-natty-natty-teddybear-gif-19177404",
            "https://tenor.com/view/nt-natty-natty-teddybear-natty_gif-%eb%82%98%eb%9d%a0-gif-19177405",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-nt-natty-natty-teddybear-gif-19177409",
            "https://tenor.com/view/%eb%82%98%eb%9d%a0-%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-natty-natty_gif-nt-gif-19177696",
            "https://tenor.com/view/%eb%82%98%eb%9d%a0-%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-woo-nt-natty-gif-19177698",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-shooting-nt-natty-gif-19176293",
            "https://tenor.com/view/nt-natty-natty-teddybear-natty_gif-heart-gif-19176286",
            "https://tenor.com/view/nt-natty-natty-teddybear-natty_gif-%eb%82%98%eb%9d%a0-gif-19176292",
            "https://tenor.com/view/nt-natty-natty-teddybear-natty_gif-%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-gif-19176185",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-bye-nt-natty-gif-19176192",
            "https://tenor.com/view/wsmud-gif-19171813",
            "https://tenor.com/view/natty-nt-natty-teddybear-%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-gif-19176171",
            "https://tenor.com/view/natty-nt-natty-teddybear-natty_gif-hi-gif-19176174",
            "https://tenor.com/view/%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-%eb%82%98%eb%9d%a0-natty-nt-natty-teddybear-gif-19171785",
            "https://tenor.com/view/%eb%82%98%eb%9d%a0-%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-shooting-nt-natty-gif-19176180",
            "https://tenor.com/view/%eb%82%98%eb%9d%a0-%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-bye-nt-natty-gif-19359165",
            "https://tenor.com/view/%eb%82%98%eb%9d%a0-%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-nt-natty-natty_gif-gif-19359164",
            "https://tenor.com/view/%eb%82%98%eb%9d%a0-%e0%b8%99%e0%b8%b1%e0%b8%95%e0%b8%95%e0%b8%b5%e0%b9%89-nt-natty-natty_gif-gif-19359169"]

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
            "https://i.pinimg.com/originals/da/2b/81/da2b810b30e8d49815f819672b294607.gif",
            "https://tenor.com/view/alexa-alexa-kpop-hot-gif-20061317",
            "https://tenor.com/view/alexa-alexa-kpop-hot-gif-20061219"]

        self.bot.bibi_gif = ["https://64.media.tumblr.com/fe935921a3bb38f4a764ef6e5cdc06fc/66ded068a298711d-25/s400x600/3f00593e2945ccf51f8976308a8acd0d0361852c.gif",
            "https://64.media.tumblr.com/b617f1c4c7ca33fce24db4f3bcfba52d/66ded068a298711d-93/s540x810/c9ac609ce52f3c7319987d26517188d37b20b175.gif",
            "https://64.media.tumblr.com/7ef03513a88a01d105647663de5771a3/66ded068a298711d-8c/s540x810/36d1a732154b959e673ba689b93f949fab078c11.gif",
            "https://64.media.tumblr.com/feedb8a26e64f90eefdf77df3bf7c8ed/66ded068a298711d-5f/s540x810/5dbdfee8c7eadba5647d05bc5573fd3ec0213219.gif",
            "https://64.media.tumblr.com/7baf1b51337a176bee91d3a55fe12497/66ded068a298711d-34/s540x810/82cba07dbdb36f7b15368a0e7e94fe5df8773477.gif",
            "https://64.media.tumblr.com/98b3b0a2f2fff0c31d6b703e36ca5892/87835b0d4b809db5-b4/s540x810/6e474af3b664b520dbcc7245d422c88c4378ad7b.gif",
            "https://64.media.tumblr.com/0007c8c3decf4d5e417208cadbe66a9c/87835b0d4b809db5-2b/s540x810/0b0ab7578bb837359026dd877419f36e09e59f37.gif",
            "https://64.media.tumblr.com/03748d4ab3a4e5a2a805f2cffea217c6/f13e22d250c95ec7-ea/s400x600/7bead345f83f62b29e81118ce1e4e218740c5574.gif",
            "https://64.media.tumblr.com/200d478a112d94aeceb9673743e56ec1/f13e22d250c95ec7-38/s400x600/b66334a37c48971091e37cd6156f9339bef24c6c.gif",
            "https://64.media.tumblr.com/9ed80ed640ad6fd6a579f9b3d58ba7fe/f13e22d250c95ec7-f3/s400x600/798759080286f2cbfdd9f6a390908142fc4c8619.gif",
            "https://64.media.tumblr.com/aaf24978cd897ba5e0cd4d84c5b86bd4/f13e22d250c95ec7-53/s400x600/8481381cfbf7630de48a0214c124a0f803d16518.gif",
            "https://64.media.tumblr.com/8f09a29618188955861b002abe746b06/b2b30253ef8be92f-3e/s400x600/3d870bc40f40138df8bbd7105127a9bee3ecb743.gif",
            "https://64.media.tumblr.com/7dfab4eced496540fb7ad3a5cbbee33f/b2b30253ef8be92f-5a/s400x600/517d43d762429e2522c981f5e6a1a65ae8f79bb6.gif",
            "https://64.media.tumblr.com/c75b11fbb2af817daae21d7aba65bb5a/b2b30253ef8be92f-9b/s400x600/79f444f43b705fc190b8871b9e853c5a2156a72d.gif",
            "https://64.media.tumblr.com/13d434b09e885db11daa2aefe8737faa/b2b30253ef8be92f-df/s400x600/885ca66e634600706e9622bf56fb6b86c7ab8778.gif",
            "https://64.media.tumblr.com/a0543603276df9695ffbf5bdd3edc8f3/1f48e60676dd6b55-a5/s540x810/3a796b20d87ba7605ae0b8ec17129336be38185a.gif",
            "https://64.media.tumblr.com/2968ecc58d5cc0d702a0c296a58712ff/1f48e60676dd6b55-6b/s540x810/4fc391ab1a25381d0db160c3ad0a92ff767b0603.gif",
            "https://64.media.tumblr.com/c4c797aea718437d44ef17a555f70607/311dc7742d9f620d-43/s540x810/c78bca98ef9395291e257154c3927ed434ad7938.gif",
            "https://64.media.tumblr.com/b96a4c9a5162158307233b938644d2ee/311dc7742d9f620d-f9/s540x810/1c46d90677ad4b35e270ee0b5c633868a488fa90.gif",
            "https://64.media.tumblr.com/f92ab24e38f6430736dec9cbd843e48f/311dc7742d9f620d-b8/s540x810/31884284b19d3d57f52a794db3d20c66a79b8bcd.gif",
            "https://64.media.tumblr.com/5eca3ba24eeb6709cf0a4e4136aa4282/311dc7742d9f620d-33/s540x810/a0ea311021d2804f5197aee5e292e0edb97019b3.gif",
            "https://64.media.tumblr.com/e1e55dc9e4ed90d861f704db99be2a82/311dc7742d9f620d-86/s540x810/c22459f870ab40f3a44004ae5d470e9d8c2ef733.gif",
            "https://64.media.tumblr.com/784dabf59cc6a2df6e752a4c87854495/311dc7742d9f620d-f1/s540x810/fa8fd211764494b275c46dffb4c2278edecf0916.gif",
            "https://64.media.tumblr.com/7ff8d06becac3db12f143469806c1f34/311dc7742d9f620d-be/s540x810/6251b1e17a66a7ae7c4a0753b8953c50b18af4a8.gif",
            "https://64.media.tumblr.com/05cedc146e099361e26ddd671308d7bd/311dc7742d9f620d-af/s540x810/70c367f19cb89e01775da37b7645f1f6eb12eebd.gif",
            "https://64.media.tumblr.com/86483d8fd0167d93c75283eb348b03ee/d3b2939d7f591917-df/s540x810/1e9b4099f9b8227454cc66ae705b1599e706c335.gif",
            "https://64.media.tumblr.com/d4b384f1db57119dc5f342a9eb22ea02/d3b2939d7f591917-61/s540x810/e736b40454ec6d5b1bccb4ba61540e950a9e0f4b.gif",
            "https://64.media.tumblr.com/92c6637e67391105bbee68cacdf1e1d3/40804eaddf5fdf8b-21/s540x810/69802817e12298e9ccccb2b148785f5d95660af4.gif",
            "https://64.media.tumblr.com/f74d0705a967cbb102dc5aa3afb95bac/40804eaddf5fdf8b-25/s540x810/ab5dd26ede83aa8d122800490e9bc4ebaa813da2.gif",
            "https://64.media.tumblr.com/3fa0066cfa9d17e275114dbd80bd1445/919f19f1adcb743f-b1/s540x810/137cd7869bf161384f14f8950f87d748b7751c77.gif",
            "https://64.media.tumblr.com/d280ecad7a1f1e62c88d87b859d863cc/919f19f1adcb743f-da/s540x810/6759c73fb87ee980200bff484eac082cc382bf4d.gif",
            "https://64.media.tumblr.com/e60a570e28c539885bf87671af8eae51/919f19f1adcb743f-0d/s540x810/55004d048c8992807334e9c184d1d5b9cdd07cda.gif",
            "https://64.media.tumblr.com/f9bd1b77ff7819691aab3d46d5a87875/919f19f1adcb743f-8d/s540x810/52a684a274d0a5a177473f04958270e57206b964.gif",
            "https://64.media.tumblr.com/a62da1c59844b48bd3ed890d85ca625e/919f19f1adcb743f-e4/s540x810/9d45e9ceba76466b1b867e55e7e0291e8b5da987.gif",
            "https://64.media.tumblr.com/f66a84e9e146a7df43ed39a3d46124c1/d0f0c7f9a15fa36d-d8/s400x600/8674fbed1346a13beea728831bbf8be958d57566.gif",
            "https://64.media.tumblr.com/0c7de649fac09786aa7a1cac7bb66497/d0f0c7f9a15fa36d-56/s400x600/0b147eb296d6bd0ddfd71f5316180e1ae87704a2.gif",
            "https://64.media.tumblr.com/075ba76e4d9a2a7da9224e40eaf42a80/d0f0c7f9a15fa36d-9b/s400x600/97af7a3678e149733b6063b9ad1f6a90d2a7ba17.gif",
            "https://64.media.tumblr.com/7baf7dfe06672f2c624c925a520d595c/d0f0c7f9a15fa36d-f7/s400x600/7d42c738fc451ce8f89bf418ee745de73ed3a63e.gif",
            "https://64.media.tumblr.com/d4de7663717c9ea952ddd069e0b982e5/75c1af4a077f47de-d0/s540x810/8d2a9811105025745c7eca6aee139bda3f71d553.gif",
            "https://64.media.tumblr.com/21d64dd21bd5409a2a04e5954509735f/75c1af4a077f47de-54/s540x810/4a4b0dc8695e21557154b810b0f0c0a10ab6d1cb.gif",
            "https://64.media.tumblr.com/18167b45882dbb57705eb113312a6708/fa962715906c9c8f-a1/s540x810/fe127145df25c00e4b45ac534bdcf07bafe74565.gif",
            "https://64.media.tumblr.com/1c26e408a206f9049ccb5d89281b4c26/fa962715906c9c8f-46/s540x810/a219154ac478fd5a36b324eb3b09b01e9c50c40c.gif",
            "https://64.media.tumblr.com/2ce8aa2383778d19fa076fc594eefe2d/tumblr_ptb1aj4dbn1ulafmao3_r1_400.gif",
            "https://64.media.tumblr.com/ba2c25461ccd57da69656264800c37ed/tumblr_ptb1aj4dbn1ulafmao2_r1_400.gif",
            "https://64.media.tumblr.com/f3d165562d705100083a62e21f1c6bb7/67a88b0245cf643f-78/s540x810/b740e3e99835b12f05119150072e6510293f771f.gif",
            "https://64.media.tumblr.com/105a6adcfeed6a92f0e425f5d6aebf9e/67a88b0245cf643f-ba/s540x810/a22771fb4a10e4589c15c3ecafbc224071304b73.gif",
            "https://64.media.tumblr.com/360910f15699ed0f4912929b3a1e3968/c1ea3b671c7b2340-b0/s540x810/8b2ab5e7ac420ff77c677012a5d8ef09ebb27c4f.gif",
            "https://64.media.tumblr.com/328f685413ea9ed1c73ba19bba8c5645/c1ea3b671c7b2340-4e/s540x810/a7e5990c0488d67ad25a15da86bb7d2e096d25ab.gif",
            "https://64.media.tumblr.com/995a7f4ebddfbb4c2ffcd9ebe69ef643/4a9dbe1dc9cfc751-34/s540x810/70f6224ed7f959bb8ff0d7e0e17098c4b1fbcecc.gif",
            "https://64.media.tumblr.com/b7ea4e68e798e5f9674d953c7d107a60/4a9dbe1dc9cfc751-fc/s540x810/0c3767de37e939644d56784b335de5d5b5a5f11f.gif",
            "https://64.media.tumblr.com/2b1652c1ec915c1047cb1cfb2984ed5d/4a9dbe1dc9cfc751-d0/s540x810/341daac258663bead6b62c8d1562f859f673740e.gif",
            "https://64.media.tumblr.com/cfc329dbec27efc4856c4942ac4a5840/11398e4c8acdecd2-16/s540x810/be2b4699c5098827ce81e58d0921d496dc723030.gif",
            "https://64.media.tumblr.com/f36dccdc7da73a407929e052e59fe78f/11398e4c8acdecd2-6e/s540x810/69636cc6747f7fc30aed91b951e83385eda5f9f1.gif",
            "https://64.media.tumblr.com/5314149129ef533975e70b4c4315706e/11398e4c8acdecd2-2f/s540x810/5291b9807ef257fcb29dd1006a27e7e91c96a9ee.gif",
            "https://64.media.tumblr.com/2aec72e9941c5c8a5dba9539fe34b1c9/ec804971ce5b1b96-50/s540x810/e79a7b01a110abc1de928749649a2fdff8bfe42c.gif",
            "https://64.media.tumblr.com/03952e92b2731bea3943c6d9734700c4/ec804971ce5b1b96-e1/s540x810/88a5c1319fefde59444ddb7b000347f78a8eea8e.gif",
            "https://64.media.tumblr.com/0645844eb251334aad2fc0712348ec38/tumblr_puuz44kBCF1r7qnpao8_400.gif",
            "https://64.media.tumblr.com/7943c35e15e3252d470e2747e4351190/tumblr_puuz44kBCF1r7qnpao6_400.gif",
            "https://64.media.tumblr.com/a5a2cb4454b346a9ebb5b37706ca9a4b/tumblr_puuz44kBCF1r7qnpao7_400.gif",
            "https://64.media.tumblr.com/3651d8ad82e18f6e8d67e3366382e18a/tumblr_puuz44kBCF1r7qnpao4_400.gif",
            "https://64.media.tumblr.com/b666fb0293e99cf97faa68f4126d32d6/e94f8e325b1991d2-95/s540x810/b933ae2a3dd76796cab74486921dd899d327b30e.gif",
            "https://64.media.tumblr.com/f078c96208a1e1b949fc6366348a3e3b/e94f8e325b1991d2-9e/s540x810/dd8ce82451a60973938de8a361dc5f698da418cf.gif",
            "https://64.media.tumblr.com/58d9430b839cbb5e780403c2cde9d57f/e94f8e325b1991d2-02/s540x810/efb2492a521f5c472ca1e67bae9f7ed1e9b98d9f.gif",
            "https://64.media.tumblr.com/87f95d80a839f1c5043fbfb525cdd4e5/695435ad264a6b5b-b0/s500x750/56fe6e6d6d3bc37190050e1f697ea39b390a8536.gif",
            "https://64.media.tumblr.com/a144d95d45b52d90647a263d081caa53/695435ad264a6b5b-da/s500x750/2240c8ef4b2e5649c810ae0a83fd6cbe1f131400.gif",
            "https://64.media.tumblr.com/7753bc3f9a095c0ae856eb032aac1865/695435ad264a6b5b-f6/s500x750/e73b792838df7744a71e9a3d02af52f9264b071a.gif",
            "https://64.media.tumblr.com/a489346b6db467f6f6e94a9fd769b554/d5f840af5b62dede-40/s540x810/fe6412327a3179730c4c3af4d7b2a7f3571a05ae.gif",
            "https://64.media.tumblr.com/897ce0617fe2ffbc427b5ecd1bba98ca/d5f840af5b62dede-53/s540x810/53080bbc162b67e0817b9eb6dd7f7d1fb780c5f2.gif",
            "https://64.media.tumblr.com/f80222665678961e142ddaeb29e084a9/6c7274f9dd0896ac-df/s400x600/ba5948e1e5c993fedf69299b4350ae9f69cd1d06.gif",
            "https://64.media.tumblr.com/c4426f24caa8461825992b42e49572fa/6c7274f9dd0896ac-62/s400x600/f272831538dcc16a9b9d67991a79edea56307a19.gif",
            "https://64.media.tumblr.com/84a0af20b89f3f5932355e62f5b14459/6c7274f9dd0896ac-59/s400x600/0dd7992cc81d80fe78c4bee71659b89f338c7f49.gif",
            "https://64.media.tumblr.com/baa23db4115cdc15130e8bb13de3d919/6c7274f9dd0896ac-46/s400x600/9ac4301032add87f127ed224b035948ec7e0eb4e.gif",
            "https://64.media.tumblr.com/ead4ee71d74091f609de5fa5802f0911/6c7274f9dd0896ac-1c/s400x600/8546948ef674d6441988d8f08f664a021c4e317e.gif",
            "https://64.media.tumblr.com/5380cc664a6d83ea8e35b82f144cc4b4/e0ec9f88f6d7671a-bb/s400x600/e13eca88b93f46f895752f0e3651af3d041c2349.gif",
            "https://64.media.tumblr.com/b8d726e68d83a42b85d78d376841db01/e0ec9f88f6d7671a-e0/s400x600/2d0e4ff54bcf24bbc79ba6d8a91cc8f5bcb1933f.gif",
            "https://64.media.tumblr.com/1a1311687d7ca6dd743fe768ea326a62/e0ec9f88f6d7671a-f6/s400x600/f4e329c972d4bd1e28fe724dd1dc637bfa1326d2.gif",
            "https://64.media.tumblr.com/a09e38cee604e1fd8a1991d5c44cebf0/e0ec9f88f6d7671a-e7/s400x600/10d48cf07adf7159cd33b313094542adff2e0a86.gif",
            "https://64.media.tumblr.com/dfd74e43a2fb00b365f98ae5dba461ad/64c8339d789d1b34-1c/s400x600/636d3f784a9ee2fb4eeb1905ceed533147a24349.gif",
            "https://64.media.tumblr.com/6a0240bd94cb1cdb718995c374899d03/64c8339d789d1b34-e2/s400x600/ba641b4971c52e88c420536cf53defedcd237416.gif",
            "https://64.media.tumblr.com/a6a69589247674c5ef44a304870d5fd6/64c8339d789d1b34-3e/s400x600/e2734386b0e33da40457f2d01707e0763aaf5921.gif",
            "https://64.media.tumblr.com/04d609362d0c9149272cbf608bdd42a6/64c8339d789d1b34-d3/s400x600/644608d9ba3da702207345fff5f0b78d56a98728.gif",
            "https://64.media.tumblr.com/3126ce1a159a2b42f5093fcb1a00cf8f/tumblr_pth6vvBul01yq00uqo1_400.gif",
            "https://64.media.tumblr.com/4d72bac17cfcb7d2e4a322548ef5b98a/tumblr_pth6vvBul01yq00uqo4_400.gif",
            "https://64.media.tumblr.com/dfc2faa2232897521bb0c3a43df98128/tumblr_pth6vvBul01yq00uqo3_400.gif",
            "https://64.media.tumblr.com/e7e7a79575e90d7d273ee3008a9d28b8/tumblr_pth6vvBul01yq00uqo2_400.gif",
            "https://64.media.tumblr.com/409de26d86dbbc4cc87fad35a5457331/104ab2164c994af1-7d/s400x600/87ffc493b38dc31ee8c8aba41519e65bfd2e4015.gif",
            "https://64.media.tumblr.com/31ba3c0c5b68ca6d3397ccb5eadc4f2f/104ab2164c994af1-fe/s400x600/b9281c4aeb5ae351d88b4823bc749aaebf974ba0.gif",
            "https://64.media.tumblr.com/0004372d8b39ba4753fbc446f45db485/878b7916af5b2aa0-83/s250x400/7de750bcd2cb09da18d7d83042b02760b8a4e9c7.gif",
            "https://64.media.tumblr.com/c3209658067f340973a07705a8a96ddf/878b7916af5b2aa0-63/s250x400/78ff7a87a14d685b0ed6b82dfec7a9d6fd2492da.gif",
            "https://64.media.tumblr.com/e8c74e8a554cec98301ee6d50163c3e4/878b7916af5b2aa0-58/s250x400/6d670644770c4d1f484876acbe71851168ff93ab.gif",
            "https://64.media.tumblr.com/f39abb689aab2b537895522820339625/31c7ddec741521bc-1d/s250x400/df23f5dda4c85ecccee5c0906cdcb3f89de6d729.gif",
            "https://64.media.tumblr.com/e2ce85b929330611f5148c9f0f721ce6/31c7ddec741521bc-5b/s250x400/786202fe97253c9b868497f2439b43c3d1775c65.gif",
            "https://64.media.tumblr.com/54bc10ee1b75f36c5171072fa8b33471/31c7ddec741521bc-80/s250x400/cec8571c808052e23324f2cb2b66f74dd083c837.gif",
            "https://64.media.tumblr.com/d6314891c428cdfb013ae02018bed096/31c7ddec741521bc-81/s250x400/62a485894bb087a196d9e2f90f5dfa2fdfacd6a4.gif",
            "https://64.media.tumblr.com/01385648eb2e8e89ce4bb63276699d8c/9b5210992a03391d-7d/s400x600/79a27cd0525ae75cdfec4efcd87d7ccf29b4188d.gif",
            "https://64.media.tumblr.com/7bc04c8ba72e73f7204344e23cc66474/9b5210992a03391d-2d/s400x600/b7cd42af10d1096769c9dde6009c1b62a31c971e.gif",
            "https://64.media.tumblr.com/f4d54b9b43ac171bd526a0552a0570fa/9b5210992a03391d-a7/s400x600/a76db0cdfa83734c29423c0adcd07ad4347c7449.gif",
            "https://64.media.tumblr.com/29f8839cd1458eecd3c5ee79884163c4/tumblr_ptuyezFLuF1rcpaiyo2_400.gif",
            "https://64.media.tumblr.com/c9075e385ea29113c7b45b3abe2ac083/tumblr_ptuyezFLuF1rcpaiyo3_400.gif",
            "https://64.media.tumblr.com/569bd6696ae00ba63ff49d809240a1a0/tumblr_ptuyezFLuF1rcpaiyo1_400.gif",
            "https://64.media.tumblr.com/3859f08f808e12daff9753b89b90a351/0b5235ebfc7b900f-8d/s400x600/c40c490297fc987d64301db024c557e52a5c89a7.gif",
            "https://64.media.tumblr.com/fcb687717ee917c1423656bf7518af62/0b5235ebfc7b900f-ac/s400x600/84f8187f7664c09d8e8383f61f76cd6719206040.gif",
            "https://64.media.tumblr.com/649e2598de950afece307c2842beb35a/0b5235ebfc7b900f-e0/s400x600/f1e73e64d12e0ccd26aaf77dc69b4c2ca5def5a2.gif",
            "https://64.media.tumblr.com/6f584910dfb3a5428537c84a91e25f19/0b5235ebfc7b900f-9d/s400x600/e253f7882fa7421fcf9cd55d9540ac27ff21080a.gif",
            "https://64.media.tumblr.com/c2d950e2f259204f38291c34e91c4d48/5031edce8f9dad94-69/s250x400/fdf0b78c0ec882dc825e11ce5fee81c9b5d9d70d.gif",
            "https://64.media.tumblr.com/581d554e8a8a9c76fea95bdeec484f8a/5031edce8f9dad94-a8/s250x400/714933a7129cff2a4b5714e39b52e1cc55347b96.gif",
            "https://64.media.tumblr.com/d0d300a0a8f5adc58324d31d0fc04a8b/3960c0c9acf92016-85/s400x600/92f8002df201c98c47683c4caace986619556ac9.gif",
            "https://64.media.tumblr.com/d9a97224b446b6b7dc7c431887914cf3/3960c0c9acf92016-a1/s400x600/4b6e00b9d8efaecef2d7ca172e451acaae876717.gif",
            "https://64.media.tumblr.com/d4b795a53db0ea09806cafeafdc3f56a/3960c0c9acf92016-4a/s400x600/363dff4468c49608228b4e48e9c1cb49a51ae74d.gif",
            "https://64.media.tumblr.com/8812f7d8c5ecc70b51aba367536a4498/3960c0c9acf92016-5e/s400x600/441512515a203482a6adeedac40068e7849d6fb3.gif",
            "https://64.media.tumblr.com/60c89f7a94f0287aff2e0acf973273db/3960c0c9acf92016-e9/s400x600/cabb2180e35536c91e84d06266e8bb9056bfd12e.gif",
            "https://gfycat.com/ancientqueasyhornet-girlshighmystery-migraine-bibi",
            "https://gfycat.com/definitiveeachfantail-bibi-kpop",
            "https://gfycat.com/disgustingbigindianelephant-bibi-kpop",
            "https://gfycat.com/sarcasticvigilantgermanshepherd-showterview-shakehead-bibi",
            "https://gfycat.com/blondscalybedlingtonterrier-girlshighmystery",
            "https://gfycat.com/cheerfulpleaseddarklingbeetle-girlshighmystery-celebrate-success-bibi",
            "https://gfycat.com/forkedfluffybaldeagle-girlshighmystery-realize-bibi-wow",
            "https://gfycat.com/admirableseveralanura-nakedbibi",
            "https://gfycat.com/deepfamiliarbarnswallow-bibi",
            "https://tenor.com/view/bibi-kpop-kimhyungseo-solo-artist-gif-21440120",
            "https://tenor.com/view/bibi-kpop-kimhyungseo-solo-artist-gif-21440117",
            "https://tenor.com/view/bibi-kpop-kimhyungseo-solo-artist-gif-21440119",
            "https://tenor.com/view/bibi-kpop-kimhyungseo-solo-artist-gif-21440121",
            "https://tenor.com/view/bibi-kpop-kimhyungseo-solo-artist-gif-21440121",
            "https://tenor.com/view/bibi-kpop-kimhyungseo-solo-artist-gif-21440107",
            "https://tenor.com/view/bibi-kpop-kimhyungseo-solo-artist-gif-20673069",
            "https://tenor.com/view/bibi-kpop-kimhyungseo-solo-artist-gif-20672903",
            "https://tenor.com/view/bibi-kpop-kimhyungseo-solo-artist-gif-20673051",
            "https://tenor.com/view/bibi-kpop-kimhyungseo-solo-artist-gif-20672674",
            "https://tenor.com/view/bibi-kpop-kimhyungseo-solo-artist-gif-20672866",
            "https://tenor.com/view/bibi-kpop-kimhyungseo-solo-artist-gif-20672800",
            "https://64.media.tumblr.com/648fdacc3a122e1998fb90b336560398/d940cbb5154d9bd1-02/s400x600/d7b49b2a805c703220350f3d974135b62a941fe9.gif",
            "https://64.media.tumblr.com/d8cae72a9473b17e51d53f48d145fc81/d940cbb5154d9bd1-61/s400x600/f0ca1ef72faa13f2817874b150f194183ce27d9b.gif",
            "https://64.media.tumblr.com/4a25bf5631e1233f2e23a1f22f0dde34/d940cbb5154d9bd1-78/s400x600/fa04cedfe15f154d5f4c99d63dc1416747ce4f93.gif",
            "https://64.media.tumblr.com/f2a020bfdbd6ac23fd26e47595ac1642/d940cbb5154d9bd1-79/s400x600/34015bbc6f787127063e5617769f6b71a3693938.gif"]

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
            "https://gfycat.com/informalphonyibadanmalimbe",
            "https://tenor.com/view/chungha-chungha-laugh-gif-20578476",
            "https://tenor.com/view/chungha-chungha-queen-gif-20585036",
            "https://tenor.com/view/chungha-chungha-confused-chungha-cute-gif-20579005",
            "https://tenor.com/view/chungha-chungha-reaction-chungha-confused-gif-20584791",
            "https://tenor.com/view/bicycle-chungha-gif-20812716",
            "https://tenor.com/view/bicycle-chungha-gif-20812725",
            "https://tenor.com/view/bicycle-chungha-gif-20812723",
            "https://tenor.com/view/bicycle-chungha-gif-20812721",
            "https://tenor.com/view/bicycle-chungha-gif-20664649",
            "https://tenor.com/view/bicycle-chungha-gif-20664650",
            "https://tenor.com/view/bicycle-chungha-gif-20664651",
            "https://tenor.com/view/bicycle-chungha-gif-20664641",
            "https://tenor.com/view/bicycle-chungha-gif-20571302",
            "https://tenor.com/view/bicycle-chungha-gif-20571304",
            "https://tenor.com/view/bicycle-chungha-gif-20571301",
            "https://tenor.com/view/bicycle-chungha-gif-20571309",
            "https://tenor.com/view/bicycle-chungha-gif-20571300",
            "https://64.media.tumblr.com/14378a981dff39455b5f23dc7534cf7d/cca5cf699050b10b-a8/s400x600/3a8190102f8f1a9562e523731b60b84b6b9cf1ea.gif",
            "https://64.media.tumblr.com/b7e3f665a2ce83f335fe3eafc8caccf9/cca5cf699050b10b-3d/s400x600/bd8aa72929efd41bd1d9e6bc4087b85829022b02.gif",
            "https://64.media.tumblr.com/d690811cc9008219db0ac9dfe3d35c28/cca5cf699050b10b-c3/s400x600/9db9171dc613f0ce4cc898d6efc141146316706a.gif",
            "https://64.media.tumblr.com/e94d125b0e37f7ce6eb2ed0cc49008b2/ede58d2c5899af9b-7e/s400x600/69d023adc3f127ba834e333669f6f68a53fd0d7f.gif",
            "https://64.media.tumblr.com/ef3a37e4d552f463937c6b2d5692e87c/ede58d2c5899af9b-d4/s400x600/48952efaea8a89cbfcdbbcff581b10698cfddbe1.gif",
            "https://64.media.tumblr.com/faa6e1c09c8244636408dff26f49a248/ede58d2c5899af9b-3b/s400x600/89748ac3d98537fe6e0d8af7a2924cc44d59713b.gif",
            "https://64.media.tumblr.com/32fef4240380165a6b2d699cdf7c4973/ede58d2c5899af9b-c2/s400x600/d89cf786a384637d418c9a8f1f1fd5461968728b.gif",
            "https://64.media.tumblr.com/4346c7687471a5da56bc0e2559142ede/3bf2921f885ec4bd-05/s400x600/f2d5c3a06c6e421487a601fe8bb2c76a223d70d5.gif",
            "https://64.media.tumblr.com/15bdc81e5657163ab72b9067e617e659/3bf2921f885ec4bd-7b/s400x600/2b9c4ae4a3638e0d07bec6c169c2ed19cbfd302e.gif",
            "https://64.media.tumblr.com/89acfd3308851580f4a51499f251590e/3bf2921f885ec4bd-af/s400x600/82a616ae24c02c712d8aa630a5e73ba035a9ace6.gif",
            "https://64.media.tumblr.com/c6e39d73e6099962b7d38dc9cfafea5a/3bf2921f885ec4bd-30/s400x600/64b37323bb8d36044cb163fa451baecabfe17bd1.gif",
            "https://64.media.tumblr.com/886627de51f9b937106c888bc27980df/ba572ba57f113c85-3c/s250x400/40adbc93e7301cf624188535b8a0b6f786ddfbcb.gif",
            "https://64.media.tumblr.com/ad68759b3da457fa0dd68f895f9db174/ba572ba57f113c85-2b/s250x400/90a9c0b87c5d61bbf6cfe23025373a4f6bff68ad.gif",
            "https://64.media.tumblr.com/ba50d598db1d8c84e118e9604623cb7d/ba572ba57f113c85-71/s250x400/fb7a974e38c04c5d0d1f3b389ecfc2bded380cc2.gif",
            "https://64.media.tumblr.com/2d662a701e93e8ad9fe998c2e16164ff/ba572ba57f113c85-08/s250x400/4e3e7445c07d0a434102347f1d49f292065059cf.gif",
            "https://64.media.tumblr.com/8a1db4ef3ae30f076363127df7b5f1d8/ba572ba57f113c85-45/s250x400/fb9ce1d85be69d9b9cef208032c71add45b27dd7.gif",
            "https://64.media.tumblr.com/b90037d1632acb54e9e4cb059c6a0ff6/df586dea4d19211d-65/s400x600/8bc861bfe0541765169368532b57f8f768ad1907.gif",
            "https://64.media.tumblr.com/8833368b09b90466ed7034a4d90dab67/df586dea4d19211d-f3/s400x600/b94d3a92a67ebaefcb7bffe81d453a87335519c5.gif",
            "https://64.media.tumblr.com/f1e13f57e5ba960a95d789959ff11c36/df586dea4d19211d-97/s400x600/302ae62caeaf7f7eb3adc2403b33ffdabc8d7875.gif",
            "https://64.media.tumblr.com/2e2ce96bf487ceb14f1eb2e8a9d7376c/df586dea4d19211d-52/s400x600/55a0b8337aba5066bfc471180bd8b7c5815bfa1d.gif",
            "https://64.media.tumblr.com/82010e7558a524828cc549c76c67652e/faa54863ccd3e678-8e/s400x600/c460158aa397603ca86016b85aca9ae8afbd5822.gif",
            "https://64.media.tumblr.com/9dd48c7660be1072e8120d60cbf6d2b0/faa54863ccd3e678-07/s400x600/25162d86053f9ec7e58ed020f67276c442df2dc6.gif",
            "https://64.media.tumblr.com/47193a9c7bfdf8404c7dcdd18399b46f/faa54863ccd3e678-22/s400x600/3a2cc7639f55778786a747e93f671cd817060247.gif",
            "https://64.media.tumblr.com/5016a799ed9897b0ff357f9a8941eb88/faa54863ccd3e678-6a/s400x600/650d6310cd0dc9c8f518de01aa830e455dae8b74.gif",
            "https://64.media.tumblr.com/10f676a9d32cfc8cabb529172243de48/0463c88a7b17fb32-ee/s250x400/56a2b5de44d088d4338ee4440095e093c1c05284.gif",
            "https://64.media.tumblr.com/e60dfcc51bd1c679bbcd88474144ca5b/0463c88a7b17fb32-cf/s250x400/a83b7fa0e500f2cef6e654f5ae9094033711e795.gif",
            "https://64.media.tumblr.com/4bf1df0400b46c31cd8279ff6185da85/0463c88a7b17fb32-b7/s250x400/39649eee8e54dfd473d498bd5db8312da1db248b.gif",
            "https://64.media.tumblr.com/b9a1e31c9b5807c807b372e4db8e866a/0463c88a7b17fb32-86/s250x400/71c0d31891a864893c7a7cea671ee1d8f7c74e01.gif",
            "https://64.media.tumblr.com/80729498f8e45d758d8e8544a04a069c/92ab95404777cb91-c4/s250x400/ce7d6750a7ac66f30202c828183229b518a2a1af.gif",
            "https://64.media.tumblr.com/2379b5d2845820f5cab3a064b0bd0a0d/92ab95404777cb91-21/s250x400/008b885021ff92c50991824e1dac6541cb3ef7f0.gif",
            "https://64.media.tumblr.com/9880bb0ecf4ede96084f99e4c397b5f5/92ab95404777cb91-ef/s250x400/48309ef5f9215c78fd3009b7bf62383bd7bb3082.gif",
            "https://64.media.tumblr.com/856a9aa0b4ab8278a1dce6ba09d147ff/92ab95404777cb91-8f/s250x400/173c26deaea01b7bb47e29a8f449e1631a36cd3d.gif",
            "https://64.media.tumblr.com/d06a2f0756eae45664b727f8dd518630/b8d78ff55638aaf9-36/s250x400/b45531d6757d761a48a2f244bb74aa770e085f9f.gif",
            "https://64.media.tumblr.com/0d6615900ae3f12e23f1a01178cba62d/b8d78ff55638aaf9-f7/s250x400/334da258ba43179b301d83bfbe5706b483fb88fd.gif",
            "https://64.media.tumblr.com/9abaa6deac76969843e264e511e22b2a/b8d78ff55638aaf9-bf/s250x400/e1ed05e444394546b296cbcd92ee4789b8517ed1.gif",
            "https://64.media.tumblr.com/67528b008bd0ba93e092c727e81e7251/b8d78ff55638aaf9-f9/s250x400/6be4a33f93f6c5c2caa31baedd832d8c713a5542.gif",
            "https://64.media.tumblr.com/b2f5ebe9c216de41bfc02c1877fd4af4/adfa9bfe3e336125-61/s400x600/a511a8309ac4a3338c6aef90140196d701f20c6c.gif",
            "https://64.media.tumblr.com/452316f5dcde853ea0e57a7f72b67b6d/adfa9bfe3e336125-d4/s400x600/d38a1f82af79cb443d37aa7753bb0d39d64f7c66.gif",
            "https://64.media.tumblr.com/0eebda22e1763c2d649c772125796bed/adfa9bfe3e336125-6f/s400x600/bb0d9c4d86d593892867ce8d47ee5c9210df6f5e.gif",
            "https://64.media.tumblr.com/bd03b116ac4728d21cde8b84cac0de4c/adfa9bfe3e336125-e2/s400x600/2dd6105c597872f7f2310693a734b91b9ba8c066.gif"]

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
            "https://cdn.discordapp.com/attachments/811821296425893918/818495971238740029/IU_gif_12.gif",
            "https://tenor.com/view/iu-lilac-dance-gif-20886109",
            "https://tenor.com/view/iu-spring-iu-lilac-iu-wave-gif-20893891",
            "https://tenor.com/view/iu-spring-iu-lilac-gif-20893892",
            "https://tenor.com/view/iu-lilac-5thalbum-affandra-gif-20891087",
            "https://tenor.com/view/iu-tease-sexy-lilac-iu-dance-gif-20863448",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-20865533",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-20865524",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-20865532",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-20865530",
            "https://tenor.com/view/iu-face-flu-lilac-teaser-gif-20704718",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-20865522",
            "https://tenor.com/view/iu-fall-flu-lilac-teaser-gif-20704712",
            "https://tenor.com/view/iu-kick-action-lilac-teaser-gif-20782405",
            "https://tenor.com/view/iu-flu-teaser-fall-lilac-gif-20710354",
            "https://tenor.com/view/iu-gif-20714643",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-21018240",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-21018241",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-21018227",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-21018229",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-21018200",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-21018199",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-21018201",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-21018194",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-21018202",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-21018193",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-21018192",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-21018188",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-21018195",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-20915459",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-20915452",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-20915456",
            "https://tenor.com/view/coin-iu-leejieun-lilac-kpop-gif-21018239",
            "https://cdn.discordapp.com/attachments/811821296425893918/846854358742466603/IU_gif_77.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/846854408993374259/IU_gif_72.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/846854413099991060/IU_gif_76.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/846854435724197928/IU_gif_73.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/846854441479176222/IU_gif_74.gif",
            "https://cdn.discordapp.com/attachments/811821296425893918/846854467029827594/IU_gif_71.gif"]

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
            "https://tenor.com/view/somi-abyan-gif-18258549",
            "https://gfycat.com/adolescentwellmadeheron-somi",
            "https://gfycat.com/agonizingimaginativeabyssiniangroundhornbill-ioi-somi",
            "https://gfycat.com/ancientorderlyafricanwildcat-beauty",
            "https://gfycat.com/betteruglygrub-somi",
            "https://gfycat.com/actualpopularbeaver-yg-entertainment-the-black-label",
            "https://gfycat.com/apprehensiveskinnycats-somi-ioi",
            "https://gfycat.com/actualbetteracornweevil-somi-kpop",
            "https://gfycat.com/coldlavishhartebeest",
            "https://gfycat.com/earlyremotedingo",
            "https://gfycat.com/eachbossygoa-dream-girls-somi-ioi",
            "https://gfycat.com/enchantedagedakitainu",
            "https://64.media.tumblr.com/c5edb143284fee680c030ef36eb0735d/tumblr_pt5j65vtAY1sk2kqwo3_250.gif",
            "https://64.media.tumblr.com/a3f0eb2f77c5ebddb8fc298f217e97a2/tumblr_pt5j65vtAY1sk2kqwo4_250.gif",
            "https://64.media.tumblr.com/a49977070f4aed9cb8ff703658d9c930/tumblr_pt5j65vtAY1sk2kqwo1_250.gif",
            "https://64.media.tumblr.com/5bd67a97bb16578a25a21e7697dfc155/tumblr_pt5j65vtAY1sk2kqwo2_250.gif",
            "https://gfycat.com/braveshamelessiaerismetalmark",
            "https://gfycat.com/jaggedpoliticalbagworm",
            "https://gfycat.com/conventionalgiantcutworm",
            "https://gfycat.com/requiredmediumhoneycreeper",
            "https://gfycat.com/kindlytendereagle",
            "https://gfycat.com/thickglaringgreyhounddog"]

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
            "https://gfycat.com/frayedtidyarawana",
            "https://tenor.com/view/yukika-teramotoyukika-gif-20491754",
            "https://tenor.com/view/yukika-cat-catgirl-yukikat-teramotoyukika-gif-20489944",
            "https://tenor.com/view/yukika-yukikaloops-pretty-cute-glowing-gif-20488886",
            "https://tenor.com/view/yukika-yukikaloops-hi-waving-pretty-gif-20488862",
            "https://tenor.com/view/yukika-yukikaloops-dog-namu-cute-gif-20488854",
            "https://tenor.com/view/yukika-yukikat-luckittykika-teramotoyukika-gif-20495815",
            "https://64.media.tumblr.com/d652c63e15141dcbc022dc258d8feed8/891e0e97749fe613-5e/s540x810/893cc4c866c4b9fd5fb62ed832efdd6af963fbe4.gif",
            "https://64.media.tumblr.com/44a84e31c2b1a75c410d73e4fd3d7631/891e0e97749fe613-5e/s540x810/bd3e27475d4385e2879ff3d51937ce5e3da1e39d.gif",
            "https://64.media.tumblr.com/8eb1a5db2cb91ba88e67c5fb968fe6f1/891e0e97749fe613-e3/s540x810/6b8bb663f1701b45ce7e639ce44e7302108c34fb.gif",
            "https://64.media.tumblr.com/0a1d8d4197a069fd79bc7ab8f0f84f13/891e0e97749fe613-fb/s540x810/31c0836c050677691f54dfe1f613aaec0b4e6b54.gif",
            "https://64.media.tumblr.com/d0f909ae1ec8e1b115740845b7d31665/891e0e97749fe613-16/s540x810/4b1ae6b00b52ec6cb85e20b2ba91cd42b4478165.gif",
            "https://64.media.tumblr.com/8ef4b36cad1eac50beec1b9729b395b8/4f59ea81aaa5627a-b5/s400x600/ddfdc47af678b3c44e2a7b6d228f7687d42106c0.gif",
            "https://64.media.tumblr.com/ae47e091e3189bf132b7f8f76ee4bc7d/4f59ea81aaa5627a-8d/s400x600/4c08e1e07f769ae93fc55ac5fde62b115aac1c2d.gif",
            "https://64.media.tumblr.com/2c86fe6e1b219c186ef66b95493caec2/4f59ea81aaa5627a-27/s400x600/fe230d0fb1dc94e728f4d4e75ba60f348ab81b51.gif",
            "https://64.media.tumblr.com/b59062652d96096267d074f5aface4c9/4f59ea81aaa5627a-af/s400x600/6e5facac2babad5b21291af6fd6c43c880f9442f.gif",
            "https://64.media.tumblr.com/8b0faf1d8ac5748932010b7ae74119d3/6dfe3564501a723b-10/s400x600/2fbc2edeb4ebd71bdf15e64ad5671aea3b1024c7.gif",
            "https://64.media.tumblr.com/95ede5660ecf84f63d3c3bd70435bb9c/6dfe3564501a723b-3e/s400x600/610e1196ebf6cdeb8c62d1e3e1665b029a9ac54a.gif",
            "https://64.media.tumblr.com/c6dd6c9eb2e156f76aca8e5da0c52e3a/6dfe3564501a723b-04/s400x600/56e42f54854bdf31f1de6b45eec083cc84af3ed3.gif",
            "https://64.media.tumblr.com/50e1bcd0849406b49b3e185881b8fea0/6dfe3564501a723b-5d/s400x600/afd35ea8f774294ba8bd312c95d190f7399d9379.gif",
            "https://64.media.tumblr.com/31ad864e8991c877bb429cf82702ce89/97727d9235cf894a-84/s540x810/da17e0ce62b00030974212f334d7d734f19e5e07.gif",
            "https://64.media.tumblr.com/912927efced4712d78b26eea1cad9dee/97727d9235cf894a-2f/s400x600/21f813fb364f4583803fe6099e1898dfe898e8b9.gif",
            "https://64.media.tumblr.com/190a8219b4e923b6fe67e0c94fc2494d/249ef32673feba2a-cf/s540x810/131c13a921edcc8d1214047bf724c11b23f8a064.gif",
            "https://64.media.tumblr.com/1044881ee347573fbceaf457c58b0ee5/249ef32673feba2a-10/s540x810/6ea5a0cc294e7521ce1dd453fb49c1c208f2952f.gif",
            "https://64.media.tumblr.com/9d8e30129f4427f4ac816aa25c0213a6/f86a9593a9def222-95/s250x400/d49684a484ad831ed51dee4294220aa162ae67a5.gif",
            "https://64.media.tumblr.com/573d9481ccd8ac8baccd4d539534fb19/f86a9593a9def222-f0/s250x400/0d3cf7850497fb6834fe9df611b2e341375e0508.gif",
            "https://64.media.tumblr.com/a9cb4cb632dffe5c003f8f1595b0aa53/f86a9593a9def222-90/s250x400/8a0aeef33afcfa014f2ef434a88965ba904f8a00.gif",
            "https://64.media.tumblr.com/b80695f4346bb56ab62a35628d2d6b4f/f86a9593a9def222-a3/s250x400/96c2c3bccfb8a42b8b9b10603204d76d5ad9d7fb.gif",
            "https://64.media.tumblr.com/ade7300b93d9265d9503594341979092/832d367adaaed37d-9f/s400x600/7fb52f01e3d981646d3fd5f070da53896edd7f65.gif",
            "https://64.media.tumblr.com/6b90c40d8109bc0225dc0588a1045038/832d367adaaed37d-19/s400x600/d89a4c3bc0b60834a7d909690ea710d72cb7bbbf.gif",
            "https://64.media.tumblr.com/72b33f116216c889f83dc498aede2feb/832d367adaaed37d-40/s400x600/f13b4813e5851e45e2808d4bacad332bbc58a2d5.gif",
            "https://64.media.tumblr.com/0a8987c852bbd799eee5436c164d9ff8/b4b1b80a255b1c16-a3/s250x400/272c981ea8fa7de259c4b337cff64a1836c7c8de.gif",
            "https://64.media.tumblr.com/c8c76ee0603cdd931651f81a55a6bbab/b4b1b80a255b1c16-7f/s250x400/d3d49f12fcb270826c8d8a5d3c2c025a4844dfa8.gif",
            "https://64.media.tumblr.com/93ab72032967b7e17279a8d777b8067f/b4b1b80a255b1c16-da/s250x400/a6f40949136d7c7157d9fdcb872afc00c15f3623.gif",
            "https://64.media.tumblr.com/7d586f09fd73dabd95183b0c6f860ec3/b4b1b80a255b1c16-04/s250x400/29075f7a35d2cf9f5c2736604af328064c68a7ee.gif",
            "https://64.media.tumblr.com/9ee3292fe976271d80865720b54129a0/6184d7c4bef747d5-6d/s400x600/db79a4bf8ac774b0dbca8484b6b4fb3f033b71c5.gif",
            "https://64.media.tumblr.com/8a84ee7429b872e3693556c93a3882b6/6184d7c4bef747d5-53/s400x600/e63a342ad49021cccfd277cdd4b18eb6b870adb6.gif",
            "https://64.media.tumblr.com/8297e6b74d2ca3ea9947ec37e94d77d6/7a60febfdb4378ef-cb/s250x400/0607267beb0ed5bbc86949c77b21b2572a5f9fe0.gif",
            "https://64.media.tumblr.com/94356cd80fbbd637815bfe656eef4829/7a60febfdb4378ef-68/s250x400/cf114e5afbcc12edb6b319ec277da14acffa1296.gif",
            "https://64.media.tumblr.com/f5b5f2301deef1a24f7ffa0db14c9e1f/7a60febfdb4378ef-7b/s250x400/6c1d274c4c3f2ac8cb6f46bd0b3ec07072f71786.gif",
            "https://64.media.tumblr.com/3d0b8791eae3617d8a9e4565b2308985/7a60febfdb4378ef-67/s250x400/4433a2784e76b15a900da51680cbd606fcf5f697.gif",
            "https://64.media.tumblr.com/7a2c0a5875d087d5b5a534dedf116344/863e1a5842ad8ef9-c9/s400x600/b408b26ca8e924a4da1f56e90a407a31d132b4f7.gif",
            "https://64.media.tumblr.com/4120b348399de6c95e076ad1bc73a359/863e1a5842ad8ef9-92/s400x600/02bfeae36dd695844a7ffe977f251414504a4b65.gif",
            "https://64.media.tumblr.com/c1dfa47c0252d4c7c85b086322e6ee47/863e1a5842ad8ef9-d8/s400x600/369e4e614726d77642044a525a7eb2d982e39c24.gif",
            "https://64.media.tumblr.com/891067654be8b2adb70c9becef22818d/aad2c669660d95ee-b8/s400x600/fe9d8042edbf9850f451b1687beeacfd10fee619.gif",
            "https://64.media.tumblr.com/6bb8c598d59fb21dfc66199f7dd7363f/aad2c669660d95ee-ea/s400x600/3e0423e82a48f09881f2534a6663e7f54d4eb095.gif",
            "https://64.media.tumblr.com/9af164d7c4dd5dde43a333109a3ef670/1416544829d72e37-34/s400x600/df1f742e5b55d6162c3feb9b6caef41c54c00019.gif",
            "https://64.media.tumblr.com/7cfd395f9d458e13dd6066d0b99432fd/1416544829d72e37-78/s400x600/9223d35b5f9806c61c0c0bfa370c11b750c9d4c3.gif",
            "https://64.media.tumblr.com/133c7c6d612e74d2642d594720e5b63b/1416544829d72e37-9f/s400x600/b983ad832c7eba8d760a16491fc96331788eb7c4.gif",
            "https://64.media.tumblr.com/c426f3f7459c406bda1842b30ed5e76b/1416544829d72e37-73/s400x600/f8f3ab45f4aff12a73665bd518cb432dc80b061f.gif",
            "https://64.media.tumblr.com/bd03c6529046e1b5f6c34b5ec20a8665/1416544829d72e37-f5/s400x600/ed6c4e70ec89fa2bd4a8db4d62e405f230406ed4.gif",
            "https://64.media.tumblr.com/65db6246c21f4bc622a2142db0ab106b/1416544829d72e37-d8/s400x600/3437ef8060cade80788826b305d0ba10ceb8fbbd.gif",
            "https://64.media.tumblr.com/dbfe68ffdd34aff3e0cc0ae97784abf0/tumblr_ppvg1cajcW1rph7i9o1_250.gif",
            "https://64.media.tumblr.com/8a9eb97f0ba90ba737b394e3186743b7/tumblr_ppvg1cajcW1rph7i9o2_r1_250.gif",
            "https://64.media.tumblr.com/bfbaff0566b1e0859e538b448cb25786/tumblr_ppvg1cajcW1rph7i9o3_r1_250.gif",
            "https://64.media.tumblr.com/afcc38b07e73a07e02154c8f2c38ad4a/tumblr_ppvg1cajcW1rph7i9o4_r2_250.gif",
            "https://64.media.tumblr.com/15253d599aa30b72d47fe30a6b10dc09/0343d07c7aec6a73-b5/s400x600/a3da913e14492096248dae8811e3e89a6a5f0533.gif",
            "https://64.media.tumblr.com/5a69ffe7e5c6dfc48c3d49e77781845f/0343d07c7aec6a73-13/s400x600/881e351463f4a2b1a0fcab22c83bf1440a66f71e.gif",
            "https://64.media.tumblr.com/15253d599aa30b72d47fe30a6b10dc09/0343d07c7aec6a73-b5/s400x600/a3da913e14492096248dae8811e3e89a6a5f0533.gif",
            "https://64.media.tumblr.com/36194e37400fa7bd89925b5ac647d0b6/0343d07c7aec6a73-2a/s400x600/3b5b963022460ec12bbcbcf50803b3d643658d7e.gif",
            "https://64.media.tumblr.com/ef2cb147b3affa20f9a56a3440cce634/0343d07c7aec6a73-3f/s400x600/03851aea6b04a313e7b943c1d8863a4cd2a0028e.gif",
            "https://64.media.tumblr.com/0cdfe41ad7a10ddd229cc4546594ece9/b6212fba85434d30-5e/s400x600/d6fb5b74d57d25019c8a8262427edeae1cfae39e.gif",
            "https://64.media.tumblr.com/a37d0dd086d938379017969282ea717d/b6212fba85434d30-68/s400x600/c65c94b34dc34f06e6cfb9b8ebe3120b64914e42.gif",
            "https://64.media.tumblr.com/e39ec65e3709db8f655f12714ef0d284/tumblr_pnp3u0SOUe1vqz8a1o4_250.gif",
            "https://64.media.tumblr.com/78925d0fd154640620c69a864861f190/tumblr_pnp3u0SOUe1vqz8a1o2_250.gif",
            "https://64.media.tumblr.com/9e1ba8f63498c15c715fa16e6983fa77/tumblr_pnp3u0SOUe1vqz8a1o1_250.gif",
            "https://64.media.tumblr.com/4783bed0365949f0b3c9e9ba4a799492/tumblr_pnp3u0SOUe1vqz8a1o3_250.gif",
            "https://64.media.tumblr.com/7cd06eb1322cc4bd9e23934857600c5e/f990f02ee287f105-d7/s250x400/e184948eb80c55f82d45ee32b18243a8a2fb1539.gif",
            "https://64.media.tumblr.com/459c92d6a86e6afd027b257cdf3dd319/f990f02ee287f105-f3/s250x400/3b9e20122e48e16477e4d56b2921e451489f0b83.gif",
            "https://64.media.tumblr.com/0eba894612a48a75689c9268605a01ca/f990f02ee287f105-e0/s250x400/bb296626f4679e8208dca83effce4417dd20c9f5.gif",
            "https://64.media.tumblr.com/6bf5698d58126f7e2f18e9db03f3e26c/7c4632993a61018d-64/s400x600/885ca4d800654c686590b99771dfb0c2a7d3e481.gif",
            "https://64.media.tumblr.com/372a88c98d875a0f93671a7b29dbf1b2/7c4632993a61018d-88/s400x600/ac7a446f69af0d4b7bbe1203e29e8702a453df82.gif",
            "https://64.media.tumblr.com/e8b2882ff3252614f7fb75c6430df977/7c4632993a61018d-78/s400x600/bdb71eec516fc2dcfc446898fa785930e98b9f82.gif",
            "https://64.media.tumblr.com/cdb01bb9ac0b0189d193cfbee235c02d/tumblr_ppiehs4z4E1rph7i9o1_250.gif",
            "https://64.media.tumblr.com/232e113a4a965aa290eefa5f1dcc89ba/tumblr_ppiehs4z4E1rph7i9o2_r1_250.gif",
            "https://64.media.tumblr.com/f7cdbd2cd1ec41142b4fa34bccf965a1/tumblr_ppiehs4z4E1rph7i9o3_r1_250.gif",
            "https://64.media.tumblr.com/7711d2de590f3c525111097c9459c42e/tumblr_ppiehs4z4E1rph7i9o4_r2_250.gif",
            "https://64.media.tumblr.com/a1bb0a7a5001c10a246323723776e331/c0d004412503ade9-90/s400x600/e5454b0bed0be8855de9f5d875bb028a7f1b89b7.gif",
            "https://64.media.tumblr.com/49599af8dce59ded12928c1161ffd50d/c0d004412503ade9-34/s400x600/0adb65efa58a48a511cb3ea482a7818ccb126138.gif",
            "https://64.media.tumblr.com/d13a97907925111742499c4782c95909/c0d004412503ade9-cb/s400x600/c7e2841788fe4d58a6824ac1867a28764618bdd2.gif",
            "https://64.media.tumblr.com/22e4bfbd56818fb0fb847b0101681af6/7d68156996be946a-3d/s250x400/dd5870c7cca0dda0a040bf71b5016ba3faf4b009.gif",
            "https://64.media.tumblr.com/1034f1d9111bc2ba074034a0742bda31/7d68156996be946a-59/s250x400/05a7cf22e11af4f6d04717a88111940bee1d32eb.gif",
            "https://64.media.tumblr.com/a616bd50fe80cf2028c2395c4ff75dfb/tumblr_oucjkxt8zk1tlw45io1_250.gif",
            "https://64.media.tumblr.com/1f36ad4a4cda0855cd128355b181786f/tumblr_oucjkxt8zk1tlw45io2_250.gif",
            "https://64.media.tumblr.com/988d1b570f0d00e935ddb8e624d22d80/tumblr_oucjkxt8zk1tlw45io3_250.gif",
            "https://64.media.tumblr.com/e4c428bdeb54d561fa1ece75ae0a3b8c/277084eaa238bab8-28/s250x400/4853e43f48793c55d31ed0ff6d86431b274e10c9.gif",
            "https://64.media.tumblr.com/bc5459a7ecc7ee14800341da5d61f976/277084eaa238bab8-de/s250x400/78b80bb2d977e9653a39f81fa3c507a4b347981a.gif",
            "https://64.media.tumblr.com/f137ed1e4aedb57e70c0de2176df5e41/277084eaa238bab8-6e/s250x400/d6b8e67c82a834e7a74dfb181dace7c1ce5d49d6.gif",
            "https://64.media.tumblr.com/7f2e42f8028b8179f55b7e3ee85ece06/277084eaa238bab8-a7/s250x400/dee5c5b1efa9d2a4247a00b445c5998ee381e0e0.gif",
            "https://64.media.tumblr.com/d236cb9647fc479db97b49687772c0cc/e82126ff0a278bd0-29/s250x400/096c515d587b31b97ff62c71a12a4ab8d28b8a4f.gif",
            "https://64.media.tumblr.com/0abce6dddf4b448c6b0b9a691b10df19/e82126ff0a278bd0-ed/s250x400/08d19e7a7b0d100c0167a99fe44ede596f84881a.gif",
            "https://64.media.tumblr.com/6daef20bef451038d4ec306d8a08f205/e82126ff0a278bd0-62/s250x400/17e81dc27253b414f943b9571d775a280960befd.gif",
            "https://64.media.tumblr.com/4910da7737a51754ebf120b2bb31e19c/e82126ff0a278bd0-fc/s250x400/1a5e41c1e9d62b6e7cd3311f6ffac01d845cae34.gif",
            "https://64.media.tumblr.com/23828a608b7e98be118df4eed3cfd7cb/8554246666e88c40-61/s400x600/b71d5d5c6a434a439953d29847b0d555f35cd6ca.gif",
            "https://64.media.tumblr.com/749a9bb6689a4fda4d45d0613ae65567/8554246666e88c40-dc/s400x600/964028a98b9294fcbd9bf92b19742848a06ce04b.gif"]

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
            "https://cdn.discordapp.com/attachments/811453123267657739/818523168313573416/Tumblr_l_1094056768268794.gif",
            "https://64.media.tumblr.com/3e3d6667894ec560a7742c71462c42be/b4b4b1a3499b8e57-94/s540x810/05a5fcea697da9e1f24d07e1d50b719d27a3fd86.gif",
            "https://64.media.tumblr.com/cd587723a8e6c8f0c82fb3667941f602/b4b4b1a3499b8e57-38/s540x810/eb905b1d5be3de13c5b10d404972ef1e470f3ca8.gif",
            "https://64.media.tumblr.com/f71e764822619a3a5d41c86717e02412/b4b4b1a3499b8e57-fe/s540x810/64f3a887780acd23e1626de494300a902264141a.gif",
            "https://64.media.tumblr.com/ea13d1fad6b3ad66c15b727e1e2f437e/b4b4b1a3499b8e57-dc/s540x810/894cd1ca8f60b8b9cc955324253549d49deea53e.gif"]

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
            "https://tenor.com/view/xone-x1-seungyoun-peace-gif-15377387",
            "https://64.media.tumblr.com/05c15a536618fccbfc23701916cf635d/e62e647a4c6a481e-8b/s400x600/eec9b580827b823ca4859a34b0c4de496848ce21.gif",
            "https://64.media.tumblr.com/a390ccf054cc7e8340eed2bcadf31f6a/e62e647a4c6a481e-e0/s400x600/fadfd32bad0d0bdc1027eb55380e99b0b3cb1fac.gif",
            "https://64.media.tumblr.com/8857d3856291a01e23dfa7c3fe6a016b/654e6a6445fb0a33-a5/s400x600/ca68fa05c76d3cac2d91ef41edc0caaf21735b80.gif",
            "https://64.media.tumblr.com/31fa3a7a912b521423fae5470c596f9f/28eb35a8a0bc54f4-a4/s250x400/dad202adc4c4d88d050cf16c3aed0ac8640c8e75.gif",
            "https://64.media.tumblr.com/93e9955bd1c4c3883b4b36c785625a7c/f2c7e2baabcf778d-be/s250x400/0f09971e38af5ab5b252c5cc68c709e6ae8bf526.gif",
            "https://64.media.tumblr.com/9a66d5bbabe96d99b2fed4aaa5048081/d13fcae86a66afe0-f7/s400x600/1312feea1c9146c59894fcb3436f31e35d4b4194.gif"]

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
            "https://64.media.tumblr.com/9887e85fe7153210e1eb4952d5f24ddb/77fe2d58c321773c-ad/s2048x3072_c0,7778,100000,91944/d288e1e039ce0a72f0f6cd4e75f89bab8d7bd85b.gif",
            "https://tenor.com/view/tail-sunmi-gif-20691845",
            "https://tenor.com/view/tail-sunmi-gif-20691847",
            "https://tenor.com/view/tail-sunmi-gif-20691842",
            "https://tenor.com/view/tail-sunmi-gif-20691843",
            "https://tenor.com/view/tail-sunmi-gif-20664865",
            "https://tenor.com/view/tail-sunmi-gif-20664868",
            "https://tenor.com/view/tail-sunmi-gif-20664866",
            "https://tenor.com/view/tail-sunmi-gif-20664867",
            "https://tenor.com/view/tail-sunmi-gif-20662008",
            "https://tenor.com/view/tail-sunmi-gif-20662010",
            "https://tenor.com/view/tail-sunmi-gif-20662011",
            "https://tenor.com/view/tail-sunmi-gif-20662484",
            "https://tenor.com/view/tail-sunmi-gif-20571086",
            "https://tenor.com/view/tail-sunmi-gif-20571093",
            "https://tenor.com/view/tail-sunmi-gif-20571092",
            "https://tenor.com/view/tail-sunmi-gif-20571107",
            "https://tenor.com/view/tail-sunmi-gif-20571073",
            "https://tenor.com/view/tail-sunmi-gif-20571059",
            "https://tenor.com/view/tail-sunmi-gif-20571055",
            "https://tenor.com/view/tail-sunmi-gif-20571054",
            "https://tenor.com/view/tail-sunmi-gif-20571065",
            "https://tenor.com/view/tail-sunmi-gif-20571050",
            "https://tenor.com/view/tail-sunmi-gif-20570995",
            "https://tenor.com/view/tail-sunmi-gif-20570994",
            "https://tenor.com/view/tail-sunmi-gif-20570991",
            "https://tenor.com/view/tail-sunmi-gif-20570992",
            "https://tenor.com/view/tail-sunmi-gif-20570982",
            "https://tenor.com/view/tail-sunmi-gif-20553810",
            "https://tenor.com/view/tail-sunmi-gif-20553812",
            "https://tenor.com/view/tail-sunmi-gif-20553809",
            "https://tenor.com/view/tail-sunmi-gif-20553814",
            "https://tenor.com/view/tail-sunmi-gif-20553813",
            "https://tenor.com/view/tail-sunmi-gif-20553804",
            "https://tenor.com/view/tail-sunmi-gif-20553798",
            "https://tenor.com/view/tail-sunmi-gif-20553807",
            "https://tenor.com/view/tail-sunmi-gif-20553802",
            "https://tenor.com/view/tail-sunmi-gif-20553795",
            "https://tenor.com/view/tail-sunmi-gif-20553706",
            "https://tenor.com/view/tail-sunmi-gif-20553704",
            "https://tenor.com/view/tail-sunmi-gif-20553700",
            "https://tenor.com/view/tail-sunmi-gif-20553696",
            "https://tenor.com/view/tail-sunmi-gif-20553694",
            "https://tenor.com/view/tail-sunmi-gif-20553682",
            "https://tenor.com/view/tail-sunmi-gif-20553674",
            "https://tenor.com/view/tail-sunmi-gif-20553672",
            "https://tenor.com/view/tail-sunmi-gif-20553673",
            "https://tenor.com/view/tail-sunmi-gif-20553670",
            "https://64.media.tumblr.com/8a1685eb090b63d9aaa1a8661298295d/92f0ec383187a3cb-58/s400x600/83597cabcaa7dbb6b5b61ede3c51937012039e4f.gif",
            "https://64.media.tumblr.com/9623cba1e775610ed190e3a70f698c88/92f0ec383187a3cb-5f/s400x600/0506fd9d8e40f50f184634691d3d0656dde625db.gif",
            "https://64.media.tumblr.com/105d73290722d37f3682c6d5430ffd0e/92f0ec383187a3cb-57/s400x600/0dc2fe26357da136ebc6e574dc4a06e4af1809be.gif",
            "https://64.media.tumblr.com/0be867c1a311e6cc7a5caf2e9bd87008/92f0ec383187a3cb-96/s400x600/437609d125d02fc0b0487a3bab1f449c613ffd14.gif"]

        self.bot.yubin_gif = ["https://78.media.tumblr.com/be13e6f73e9b9ca358fa421432a2c83a/tumblr_p9v2d7MMvM1wfmyhto2_540.gif",
            "https://78.media.tumblr.com/76b2b0202c1563bd6839030659e147d1/tumblr_p9v2d7MMvM1wfmyhto3_540.gif",
            "https://gfycat.com/timelybriefbarebirdbat-wonder-girls-kpics",
            "https://gfycat.com/browncolorfuladmiralbutterfly-kpopgfys-europe",
            "https://gfycat.com/aromaticelasticankolewatusi",
            "https://64.media.tumblr.com/370eff3f3bd7edbdfeb9820517d2437b/tumblr_pkgrqcEiBN1xy0u4ko7_400.gifv",
            "https://i.pinimg.com/originals/5d/c5/d5/5dc5d582c2b37126c3f4718aac1e66bf.gif",
            "https://78.media.tumblr.com/99f335d067f425e4b4fe3e78a881fd8a/tumblr_p9seia7vdb1urmyjyo6_r1_500.gif",
            "https://66.media.tumblr.com/ecf1fdfddfe263763122163dcc6d7d12/tumblr_pitu6iy92L1sy8x5ho1_500.gif",
            "https://tenor.com/view/yubin-perfume-endingfairy-gif-20339216",
            "https://tenor.com/view/wonder-girls-yubin-yoobin-kim-gif-20583965",
            "https://tenor.com/view/yubin-perfume-mv-fume-greendress-gif-20339215",
            "https://tenor.com/view/yubin-perfume-mv-greendress-fume-gif-20339213",
            "https://64.media.tumblr.com/6bd612c7a1e6150aa2d99d12ae67eef4/a7a0f8edc802e652-69/s500x750/cb652ff048e30c17f1d69a7f4b92f9ebdfce130e.gif",
            "https://64.media.tumblr.com/719a23aa47400e06f38abdc3b87ed6a3/tumblr_pjdxkuHqOD1vjco6so3_540.gif",
            "https://64.media.tumblr.com/9dcb388c8f5ecc9b7ab57a858e0bd90f/tumblr_parjqdGKC61tkqb9oo2_r2_250.gif",
            "https://64.media.tumblr.com/f025224f508eda25bc856a8d5bfc2fab/tumblr_parjqdGKC61tkqb9oo9_r1_250.gif",
            "https://64.media.tumblr.com/8bdbdaa3a89e029895771bd5f3737398/tumblr_parjqdGKC61tkqb9oo1_r2_250.gif",
            "https://64.media.tumblr.com/e3ffd6674d2dd47399e3d0f02bc22929/tumblr_parjqdGKC61tkqb9oo4_r1_250.gif",
            "https://64.media.tumblr.com/5ed9d44ae71606f88cc306c49637f0a9/tumblr_parjqdGKC61tkqb9oo5_250.gif",
            "https://64.media.tumblr.com/ad9980fb7a4c8a415481d4b3ca92df4c/tumblr_parjqdGKC61tkqb9oo7_r4_250.gif",
            "https://64.media.tumblr.com/cbeb61d0586b2790e69eb12edfdb6e56/tumblr_parjqdGKC61tkqb9oo8_r3_250.gif",
            "https://64.media.tumblr.com/0f7dcc397a2ac49d45683f3db78ecdb7/tumblr_parjqdGKC61tkqb9oo3_250.gif",
            "https://64.media.tumblr.com/de588b219772b6b2a60ad1f86781c51d/tumblr_parjqdGKC61tkqb9oo6_r1_250.gif",
            "https://64.media.tumblr.com/4e5c1ecf4fe095f3e03b19dfded63931/tumblr_piujbu504W1vfcnxjo1_540.gif",
            "https://64.media.tumblr.com/9971c3ac3f25257cab621082c08949a0/tumblr_piujbu504W1vfcnxjo3_540.gif",
            "https://64.media.tumblr.com/6470df63b28c2e4e125cf502cf3f4d4a/tumblr_piujbu504W1vfcnxjo2_540.gif",
            "https://64.media.tumblr.com/7a8339f5f4452971d46c09a91996b7a9/tumblr_piujbu504W1vfcnxjo5_540.gif",
            "https://64.media.tumblr.com/540782d9a2490ff01e5117e3c1969bcd/tumblr_piq4tcqzwC1r7qnpao1_540.gif",
            "https://64.media.tumblr.com/37cf7115a98860958ee29fc4ac4eebce/tumblr_piq4tcqzwC1r7qnpao2_540.gif",
            "https://64.media.tumblr.com/165c522636d6723661416f82ba377936/tumblr_p9zaxdWiIP1wjqhtxo3_400.gif",
            "https://64.media.tumblr.com/2db30dc38cc69a36b938f3411398e650/tumblr_p9zaxdWiIP1wjqhtxo1_400.gif",
            "https://64.media.tumblr.com/94a6fd9e716d1b75228d40ca08247bed/tumblr_p9zaxdWiIP1wjqhtxo4_400.gif",
            "https://64.media.tumblr.com/8a77b6db138cf407a38f419e201c4319/tumblr_p9zaxdWiIP1wjqhtxo2_400.gif",
            "https://64.media.tumblr.com/a73bffbdc8499088b091fbc937348dda/tumblr_p8imufCaTA1uu2l2ko6_r1_250.gif",
            "https://64.media.tumblr.com/b97560cc6cab30ee1e0e56fffb572262/tumblr_p8imufCaTA1uu2l2ko1_250.gif",
            "https://64.media.tumblr.com/6b16d180d5290f8f1240d30de15b3391/tumblr_p8imufCaTA1uu2l2ko2_250.gif",
            "https://64.media.tumblr.com/c490309900077b146d360293aa78f5d9/tumblr_p8imufCaTA1uu2l2ko8_r1_250.gif",
            "https://64.media.tumblr.com/bdebbdc4dc4f87d8816d3b1ab79c6d1b/tumblr_p8imufCaTA1uu2l2ko5_r1_250.gif",
            "https://64.media.tumblr.com/b9bdf80503df3d73a7bad3173126f602/tumblr_pj10ygL4D71wefkb5o3_r1_250.gif",
            "https://64.media.tumblr.com/fea13fc2e41ebaf9b8e72dd1af483afa/tumblr_pj10ygL4D71wefkb5o2_250.gif",
            "https://64.media.tumblr.com/3b96927e85265226d9e911d61a3ee7e6/tumblr_pj10ygL4D71wefkb5o8_r1_250.gif",
            "https://64.media.tumblr.com/dcac0d27f3ececdf7f48d569431cbefa/tumblr_psyfsroVsb1wj66x5o1_400.gif",
            "https://64.media.tumblr.com/de41f50e96442eafeb6dd09c6fa5919a/tumblr_psyfsroVsb1wj66x5o5_400.gif",
            "https://64.media.tumblr.com/482dbd281825cc7dde83589ea79f2f90/aa10432ec6efbfc5-97/s540x810/decaecd2174d17ffcc14cc786445dace50dd1d1d.gif",
            "https://64.media.tumblr.com/d44abbb9a526d6812edb6836c3a1ed9d/aa10432ec6efbfc5-08/s540x810/01e734aa19780756ad718cec1b7468b57acf279c.gif",
            "https://64.media.tumblr.com/821b955333cc368f124766ef2c396dc9/tumblr_pjh4isweUD1wefkb5o2_400.gif",
            "https://64.media.tumblr.com/93a5e8d4fca8e62b78b2ccba8665b3d0/tumblr_pjh4isweUD1wefkb5o4_400.gif",
            "https://64.media.tumblr.com/f605979bdb0e9bd9a1fd6fc86566eeca/tumblr_pjh4isweUD1wefkb5o3_400.gif",
            "https://64.media.tumblr.com/8aad176f7310b50087d88aeaf5f3ef24/b405f924744683e6-a2/s400x600/d8d50d6b3be6b1cef71ef099af452cbebcfdd9fb.gif",
            "https://64.media.tumblr.com/7884c458eb5a9a20bdefaa4a1c59d862/b405f924744683e6-fd/s400x600/5cbcd4234cddf7238d3f84ff66640d1d153f78c7.gif",
            "https://64.media.tumblr.com/b627cb33abe5820c8f46f8d534ac1249/b405f924744683e6-7e/s400x600/9b55da018a7a42803eff2c798668fc9fb9bd5166.gif",
            "https://64.media.tumblr.com/b627cb33abe5820c8f46f8d534ac1249/b405f924744683e6-7e/s400x600/9b55da018a7a42803eff2c798668fc9fb9bd5166.gif",
            "https://64.media.tumblr.com/ba508f96cd71224634d3125cb183950f/d7b20a6342a8e62e-6a/s250x400/5d02a0d4d0702da1bc598779740caf14a9273028.gif",
            "https://64.media.tumblr.com/6a80982fc9514c6a24c48f9fe0661e91/d7b20a6342a8e62e-5f/s250x400/855089d5b50d75a7c37e65aaa477751a9e9b7353.gif",
            "https://64.media.tumblr.com/ba46e0d92b7719622691921823420c78/d7b20a6342a8e62e-9e/s250x400/498d6005d794369dd839ae5cad7b947648943d87.gif",
            "https://64.media.tumblr.com/fc33764181dae4de72f7642a666c5e47/d7b20a6342a8e62e-1b/s250x400/13dbae84b5b21fe2f33c3352deb9df60b18bb1cf.gif",
            "https://64.media.tumblr.com/f59504957a2a73c5d452434f593577b9/d7b20a6342a8e62e-b1/s250x400/5eadb6a4a9a316aa67c42a42fe9cd727027f2734.gif",
            "https://64.media.tumblr.com/e41cbe3e0dc20dd167c4c1d3ba90d883/8a38d661c790bb56-f6/s540x810/286167207399df1ac90bc418ddd7e4c54eb0f953.gif",
            "https://64.media.tumblr.com/f56fddcf807a76b64658e8b653ed37dd/8a38d661c790bb56-0d/s540x810/c3c424d90ddd04a57d853b26842fe8284235085e.gif",
            "https://64.media.tumblr.com/1ef97ebc1a9429e3dc7f4b8d3e5defee/8a38d661c790bb56-75/s540x810/84682ed2fc6031a5a5405f88ce1a9456a79b5c8c.gif",
            "https://64.media.tumblr.com/83ee2f88635074a991d467901e917a53/tumblr_pa4b72ud9U1tqqj2xo5_400.gif",
            "https://64.media.tumblr.com/0cb252f30b84dfc40798077d5d2cf43f/tumblr_pa4b72ud9U1tqqj2xo6_400.gif",
            "https://64.media.tumblr.com/9e0b3c5763d88fdc1847740c146fb87a/0840ca8d5ac8e6d5-cd/s540x810/98fca942cb48f0b8449c31fdf310bcffb98acb38.gif",
            "https://64.media.tumblr.com/462f9fdf5ea8f1a519ee9b1621830b71/0840ca8d5ac8e6d5-87/s540x810/3a57d412507e3bb2758142cae19ee4b89785bcbd.gif",
            "https://64.media.tumblr.com/c23171eb552d4cf0e6c74db00e6e1d4a/0840ca8d5ac8e6d5-03/s540x810/659cb0ba8ea0a6520a0017253d835bb0b4de89bc.gif",
            "https://64.media.tumblr.com/f80239a160d2030058f04e5556e0f33f/5586f72372612583-d2/s540x810/bca9f63ba42ab38880fa1f9d67ff2adada1963d4.gif",
            "https://64.media.tumblr.com/222dcc78523f9edc46faa1d86378efc9/0840ca8d5ac8e6d5-bb/s540x810/197a6da951976263e697fab28b160ce937b1d4d9.gif",
            "https://64.media.tumblr.com/aae7446ef30cdd0d5a57f38eff37adfc/e917aa559b757042-b5/s400x600/fc9ce14511c4cbb6d45109bb8a65be11d3432986.gif",
            "https://64.media.tumblr.com/8bed04993e8d59de929fc868a01dae15/e917aa559b757042-65/s400x600/9aa3fbbe0380f2648af3da6e9408e337431a359d.gif",
            "https://64.media.tumblr.com/ee5b437beaa0aa6c7a87261142c73a91/e917aa559b757042-2a/s400x600/123c767b20a2de52381f6c5ad18386854cf0d73b.gif",
            "https://64.media.tumblr.com/91fe53dac588e11643f06e6a496dc816/e917aa559b757042-ff/s250x400/89e430c7dd72167d81440a9703ed94559080f6bd.gif",
            "https://64.media.tumblr.com/26d4f85f60d4644ec89ec801b3290edc/8087094633724917-e8/s400x600/3d7ea1664b685d91dcdcaecf0232e6b156300ea9.gif",
            "https://64.media.tumblr.com/7199d077d38e8d0147500aad36a64923/48aa14c44ee32fa0-26/s250x400/94a6b65dcddc8ecbd96cc82221e7a39f7c732fe2.gif",
            "https://64.media.tumblr.com/5f9e03160e879d47f940e8a54df7c0d3/48aa14c44ee32fa0-59/s250x400/c648be6df0ab5efa29d24de7bc11b6ccc696dbc5.gif",
            "https://64.media.tumblr.com/05eed5c7983faf59e9d81bb1bc35b0c9/49acf9fe73ee13b8-44/s400x600/7534ccfed8bda807993b82cac0cd6160223e1a4f.gif",
            "https://64.media.tumblr.com/9221ea029db7f21f0ca38750a5975331/49acf9fe73ee13b8-a4/s400x600/1a06cb50f4728ec6f0fdfbfaada10fb036fc6f90.gif",
            "https://64.media.tumblr.com/37752739656b38fdadae504566edd19e/tumblr_paxxyv7tqJ1xoxm6to3_250.gif",
            "https://64.media.tumblr.com/6610eb26ec8812d021cedef7dbdce693/d2f462b06daa34b8-86/s250x400/c9eefe9796a59cd3cf06c6a6a9ecab76e07fb131.gif",
            "https://64.media.tumblr.com/bbcd330d6050c5e1005b84014cd074e9/8652348fd4d93c24-93/s250x400/7b38ed513113992a908c7d37936f1f0fdeef807a.gif",
            "https://64.media.tumblr.com/d1a01acc48cb929cc8680e41818454fb/8652348fd4d93c24-e7/s250x400/3d944838a78d53737d67bc2067cb454e2f227a4e.gif",
            "https://64.media.tumblr.com/7eeeec9d09a6bdb8444be7b025e04712/8652348fd4d93c24-7f/s250x400/ec72535df360759ab17e87f4737de04a3bfd6661.gif",
            "https://64.media.tumblr.com/b491dc082b3036942d5d49f6e267ea2f/8652348fd4d93c24-af/s250x400/d30a11aeba10f348c6b34f814e1276aa6d9dedb9.gif",
            "https://64.media.tumblr.com/6610eb26ec8812d021cedef7dbdce693/d2f462b06daa34b8-86/s250x400/c9eefe9796a59cd3cf06c6a6a9ecab76e07fb131.gif",
            "https://64.media.tumblr.com/9e7b8e8508aa77df91f5bdc6cf079acb/e20c6466d9ad1c9a-a4/s250x400/dc5bc8152be33019c99de868ffa5db080993d5b4.gif",
            "https://64.media.tumblr.com/b1b78261c77dbc31db3f331ae9a73565/e20c6466d9ad1c9a-7d/s250x400/960009e8c66e9d1125a634de730ba1016b981e17.gif",
            "https://64.media.tumblr.com/065221b3c591a4e575a3bab3562915ca/e20c6466d9ad1c9a-5b/s250x400/afda2af77b2b47e05bb9e45b7764f0658e9173ec.gif",
            "https://64.media.tumblr.com/5a0f72f4699ba83ad1a5da3e56ebab0f/tumblr_pca48e5Ag11s8qgb9o1_400.gif",
            "https://64.media.tumblr.com/ff21343af494a4ce77c533e9e9794bfa/tumblr_pca48e5Ag11s8qgb9o2_400.gif",
            "https://64.media.tumblr.com/bbf2133c80df493240f72b714bbdf35b/a04bd0c925c53687-28/s400x600/7fec11d8d797d7b9bdcf93a2246af448087d283a.gif",
            "https://64.media.tumblr.com/5ec77b8a37270dcfec95d63d3a9ee116/a04bd0c925c53687-ed/s400x600/e02481d5b1c7ae3dab5635440bfdacf327998814.gif",
            "https://64.media.tumblr.com/8a6dd500aba1b1a8a0916c5768a4dd52/a04bd0c925c53687-f6/s400x600/d2dd2a2f664373c1778432a050de0f7910a050dc.gif",
            "https://64.media.tumblr.com/4fb1cba14722941f2cb50c87756d3b70/a04bd0c925c53687-af/s400x600/d86a280c1646ae6ae9cf2887665cc153f529fec6.gif",
            "https://64.media.tumblr.com/3e7159fb1c2a6b2813358e240fddbacf/a04bd0c925c53687-47/s400x600/cbbfca5f7e4015b178b784c152426990ec91fe01.gif"]

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
            "https://imgur.com/8yc402e",
            "https://imgur.com/kF5xpEy"]

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
            "https://64.media.tumblr.com/12f1c42fb98bdba447a04206fa28632c/tumblr_p3v0v4l3JZ1r7qnpao4_400.gif",
            "https://tenor.com/view/hyuna-kimhyuna-gif-20664503",
            "https://tenor.com/view/hyuna-kimhyuna-gif-20664507",
            "https://tenor.com/view/hyuna-kimhyuna-gif-20664506",
            "https://tenor.com/view/hyuna-kimhyuna-gif-20664498",
            "https://tenor.com/view/hyuna-kimhyuna-gif-20247793",
            "https://tenor.com/view/hyuna-kimhyuna-gif-20247790",
            "https://tenor.com/view/hyuna-kimhyuna-gif-20247791",
            "https://64.media.tumblr.com/a5dfbbb980532bea01395f7f83c4a28e/2b61901fc448f201-71/s400x600/de5b81cb3b3de4264e36796a8504b64e442f22c1.gif",
            "https://64.media.tumblr.com/69640ffde7d0b61b4dd1a95c430d0094/2b61901fc448f201-ba/s400x600/a639d835d3c133be7ed5dcab460dc893cf6dd041.gif",
            "https://64.media.tumblr.com/0780b2f72c55b2dc3a2dcd88b600acf0/2b61901fc448f201-26/s400x600/3460ccf07eb2434aceb5fac7ad4d01cccb0f16f2.gif",
            "https://64.media.tumblr.com/90c8918bdd84debb8d16c97148b5758e/d40b98620c42cf51-e2/s540x810/d8db373da85005e6cc05619466f5e5e01bb46de5.gif",
            "https://64.media.tumblr.com/df53228a9e14022ec9de00718e92a440/e180ef74f054ac23-31/s400x600/0aa3c9f063e634acaef6fca967a9c148362ab53c.gif",
            "https://64.media.tumblr.com/b95cb0c9794e054a607721b1dd0539db/0e5631aa16170d68-3b/s400x600/fa181b10c74806f990cc23a439f93739924409fb.gif",
            "https://64.media.tumblr.com/dfac82e10bdef94d382158c1623c36e4/0e5631aa16170d68-3c/s400x600/e6e78aba7a3e078840e50489737ff6099fdd3858.gif",
            "https://64.media.tumblr.com/ee9aed63fbe543ec4130bde4f0a9f7c4/0e5631aa16170d68-6d/s400x600/d813671d05353d8bbf688cdfeda1bd348afd2620.gif",
            "https://64.media.tumblr.com/16e40a4cf62d18b2453fa448ad0faef3/0e5631aa16170d68-ae/s400x600/e69954cbffe7e7d2021edef160bd0ea5bec430e8.gif"]

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

        self.bot.wonho_gif = ["https://64.media.tumblr.com/94717f668d0ca5c0033afa4be55b8413/cb11f567c6ef0d4e-7c/s400x600/84ef55ccbd7ff32aa6025aad251989e316df55ac.gif",
            "https://64.media.tumblr.com/b98a63347d447a4fbc16da7736ff53c7/cb11f567c6ef0d4e-a0/s400x600/b39320bac50db08def53026f90ddcac4b163560b.gif",
            "https://64.media.tumblr.com/6215c88e03444519d311fa76516a446a/337faab67081e317-1e/s400x600/dd778e260c28fce860db9a6cd735e2da6f17ab0a.gif",
            "https://64.media.tumblr.com/1ea057a919bfa788f0e50769e6ab7eb5/9f04c6eb4183e454-10/s400x600/f58936b268c9a9eaaa82fb6afb4f32d3ef8234d0.gif",
            "https://64.media.tumblr.com/90b46d5417b52f970ceae13e3b37145b/9f04c6eb4183e454-a0/s400x600/5f52e94ea635e80031f0ef41b3c3532e660dbec0.gif",
            "https://64.media.tumblr.com/fbeb4be3e6227229245404b75f07a5a7/a551376b5fd21d62-e8/s400x600/be84c7d75fbff064e83e7381ac9da43820a7b396.gif",
            "https://64.media.tumblr.com/ec79071f2240d8d1e1f23cb884b67466/d85a77e580d193f4-03/s250x400/522529141a08a7cd8fd3f97054b8d91063bb4461.gif",
            "https://64.media.tumblr.com/0ee04c33db0bfb9a778df9501e73bccd/ef9cc29e7319e8b1-61/s400x600/1805e35e8aefeaa5947021dedf283990e6faf4a8.gif",
            "https://64.media.tumblr.com/742b0a7b0560ea55e7b8f386fe442329/7a032a6e70a304af-12/s400x600/012303bb760045e5e76dabeb7dec389f3b1b90fc.gif",
            "https://64.media.tumblr.com/ffaaecf990c206b2ba65bd901db95e5c/c980b478726d6d35-68/s400x600/9992684a148b82f7ecdd6f6c1c237ce8e68a11c8.gif",
            "https://64.media.tumblr.com/b96d0058ccf7865f77d3b00871a243eb/1304454b8871260b-b0/s400x600/b081a88335cf3806e9b3bd437162989ae1a737b8.gif",
            "https://64.media.tumblr.com/86fcc5938d79ff85e89ea34fac7a1145/cf3390246c8a7a94-09/s400x600/f7c12c25dcb9de85b1a75d4c3db05e405104064d.gif"]

        self.bot.dpr_ian_gif = ["https://cdn.discordapp.com/attachments/822327229782163467/822444412117450782/Tumblr_l_74660478524225.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822444412742271006/Tumblr_l_74657508304799.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822444413535911986/Tumblr_l_74639893616056.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822444414181310505/Tumblr_l_74637252741473.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822444680661958656/Tumblr_l_74635869279755.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822444681006678056/Tumblr_l_74632187474548.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822444757489811456/Tumblr_l_74603737831278.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822444757812510750/Tumblr_l_74602237755081.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822444758101786674/Tumblr_l_74600914694769.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822444758449389568/Tumblr_l_74599275184665.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822827193963905064/Tumblr_l_285379373589415.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822827345148117002/Tumblr_l_285426918051428.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822827345639243776/Tumblr_l_285426053656272.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822827345970331688/Tumblr_l_285425318229137.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822827346344149032/Tumblr_l_285425323959814.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822827366065242132/Tumblr_l_285420651423410.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822827366497517598/Tumblr_l_285418040497473.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822827550039867412/Tumblr_l_285470898798026.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822827550518149160/Tumblr_l_285470519728339.gif",
            "https://64.media.tumblr.com/479128a926ac5b91c912493a52b472fa/tumblr_poozc6CIrc1qb69o4_400.gif",
            "https://64.media.tumblr.com/00ff77e1a6b20e83276fec99d2a0cca5/2afb16606e59d3f1-b2/s400x600/83c2b0f336dd6233814d3652d7e1045df55a6b39.gif",
            "https://64.media.tumblr.com/0acb924493e324dbb1f35130656a272c/2afb16606e59d3f1-58/s400x600/5a96aa61dc683460aa536e0d9c95f8ca78cc1e07.gif",
            "https://64.media.tumblr.com/c5b6dcd02c6ba104ef2b015e164db8f7/tumblr_pet8gfIJ331x6d8igo4_250.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/823542532558159932/Ian_gif_9.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/823542546399494175/Ian_gif_10.gif",
            "https://cdn.discordapp.com/attachments/822327229782163467/822444411115405322/Tumblr_l_74662172219016.gif"]

    @commands.command()
    async def natty(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Natty] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about Natty :teddy_bear:')
        await ctx.send(random.choice(self.bot.natty_gif))
        await ctx.message.delete()

    @commands.command()
    async def alexa(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [AleXa] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about AleXa :blue_heart:')
        await ctx.send(random.choice(self.bot.alexa_gif))
        await ctx.message.delete()

    @commands.command()
    async def bibi(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [BIBI] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about BIBI :heart:')
        await ctx.send(random.choice(self.bot.bibi_gif))
        await ctx.message.delete()

    @commands.command(aliases = ['chung'])
    async def chungha(self, ctx, arg="ha"):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Chung Ha] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "ha":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Chung Ha :heart:')
            await ctx.send(random.choice(self.bot.chungha_gif))
            await ctx.message.delete()

    @commands.command()
    async def iu(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [IU] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about IU <:blueming:787451831478910996>')
        await ctx.send(random.choice(self.bot.iu_gif))
        await ctx.message.delete()

    @commands.command()
    async def somi(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Somi] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about Somi :heart:')
        await ctx.send(random.choice(self.bot.somi_gif))
        await ctx.message.delete()

    @commands.command()
    async def yukika(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Yukika] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about Yukika :heart:')
        await ctx.send(random.choice(self.bot.yukika_gif))
        await ctx.message.delete()

    @commands.command()
    async def taemin(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Taemin] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about Taemin :baby::cheese:')
        await ctx.send(random.choice(self.bot.taemin_gif))
        await ctx.message.delete()

    @commands.command()
    async def woodz(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [WOODZ] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about WOODZ :heart:')
        await ctx.send(random.choice(self.bot.woodz_gif))
        await ctx.message.delete()

    @commands.command()
    async def kris(self, ctx, arg = "wu"):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Kris Wu] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "wu":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Kris Wu :heart:')
            await ctx.send(random.choice(self.bot.kriswu_gif))
            await ctx.message.delete()

    @commands.command()
    async def luhan(self, ctx): 
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Luhan] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about Luhan :heart:')
        await ctx.send(random.choice(self.bot.luhan_gif))
        await ctx.message.delete()

    @commands.command(alises = ['xitao', 'ztao'])
    async def tao(self, ctx): 
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Tao] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about Tao :heart:')
        await ctx.send(random.choice(self.bot.tao_gif))
        await ctx.message.delete()

    @commands.command()
    async def kang(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Kang Daniel] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "daniel":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Kang Daniel :heart:')
            await ctx.send(random.choice(self.bot.kangdaniel_gif))
            await ctx.message.delete()

    @commands.command()
    async def sunmi(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Sunmi] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about Sunmi :heart:')
        await ctx.send(random.choice(self.bot.sunmi_gif))
        await ctx.message.delete()

    @commands.command()
    async def yubin(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Yubin] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about Yubin :heart:')
        await ctx.send(random.choice(self.bot.yubin_gif))
        await ctx.message.delete()

    @commands.command()
    async def rothy(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Rothy] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about Rothy :heart:')
        await ctx.send(random.choice(self.bot.rothy_gif))
        await ctx.message.delete()

    @commands.command()
    async def hyuna(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Hyuna] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about Hyuna :heart:')
        await ctx.send(random.choice(self.bot.hyuna_gif))
        await ctx.message.delete()
    
    @commands.command()
    async def boa(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [BoA] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about BoA :heart:')
        await ctx.send(random.choice(self.bot.boa_gif))
        await ctx.message.delete()

    @commands.command()
    async def wonho(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Wonho] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about Wonho :heart:')
        await ctx.send(random.choice(self.bot.wonho_gif))
        await ctx.message.delete()

    @commands.command()
    async def dpr(self, ctx, dprMan = "ian"):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [DPR Ian] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        #. end of logs
        await ctx.send(f'<@!{ctx.author.id}> is talking about DPR Ian :heart:')
        await ctx.send(random.choice(self.bot.dpr_ian_gif))
        await ctx.message.delete()

def setup(client):
    client.add_cog(SoloPings(client))