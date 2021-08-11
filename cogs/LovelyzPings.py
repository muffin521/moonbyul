import discord, random
from discord.ext import commands
from discord.utils import get
from datetime import datetime

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

class Lovelyz(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.yein_gif = ["https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-yein-%EC%98%88%EC%9D%B8-gif-18419239",
            "https://tenor.com/view/lovelyz-yein-%EC%98%88%EC%9D%B8-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kpop-gif-16459793",
            "https://tenor.com/view/lovelyz-kpop-yein-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EC%98%88%EC%9D%B8-gif-18588376",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-yein-%EC%98%88%EC%9D%B8-gif-18213767",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-yein-%EC%98%88%EC%9D%B8-gif-18213757",
            "https://tenor.com/view/lovelyz-kpop-yein-eat-it-gif-16074106",
            "https://tenor.com/view/lovelyz-kpop-kei-mijoo-yein-gif-18565694",
            "https://tenor.com/view/yein-blow-a-bubble-bubble-gum-gum-lovelyz-gif-11607390",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-yein-kpop-%EC%98%88%EC%9D%B8-gif-16459879",
            "https://tenor.com/view/lovelyz-lvlz-jung-yein-yein-gorani-gif-16341215",
            "https://tenor.com/view/yein-lovelyz-kpop-girlgroup-fight-gif-18292941",
            "https://media.discordapp.net/attachments/170383062633283584/755514607308636260/ecd790977d987c6bc0db74a80ca893fb.gif",
            "https://gfycat.com/quarterlymerrydingo",
            "https://gfycat.com/oldfashionedspiritedbluefish",
            "https://gfycat.com/uncomfortablesafebarbet",
            "https://tenor.com/view/yein-lovelyz-oblivate-gif-18541914",
            "https://tenor.com/view/yein-lovelyz-oblivate-gif-18541915",
            "https://gfycat.com/sparserawdiplodocus",
            "https://gfycat.com/lavishteemingalligatorgar",
            "https://tenor.com/view/%EC%A0%95%EC%98%88%EC%9D%B8-gif-18273271",
            "https://64.media.tumblr.com/7bac418da7c214b5552321ab22e6c9a6/tumblr_on1lm2PtUI1u2hx1xo2_250.gif",
            "https://64.media.tumblr.com/2c0f24d093d4d738e7352cc49a72c4a3/tumblr_on1lm2PtUI1u2hx1xo1_250.gif",
            "https://64.media.tumblr.com/7ae5715dfcff2e435738aa9e838b13b4/tumblr_on1lm2PtUI1u2hx1xo3_250.gif",
            "https://64.media.tumblr.com/5760843aee437e19bf9e0c347641ae45/tumblr_on1lm2PtUI1u2hx1xo4_250.gif",
            "https://64.media.tumblr.com/a2fc12eaceb217dd5188a0a782e93926/tumblr_pac8grvbVc1qg5nyao4_250.gif",
            "https://64.media.tumblr.com/3b10be3529bcf979edc392ee21578de0/tumblr_pac8grvbVc1qg5nyao1_250.gif",
            "https://64.media.tumblr.com/e37b01d1506a0fc553fac35fcad1b4be/tumblr_pac8grvbVc1qg5nyao2_250.gif",
            "https://64.media.tumblr.com/b36e915e93d21f61c543ef6b84363205/tumblr_pac8grvbVc1qg5nyao3_250.gif",
            "https://64.media.tumblr.com/addbc52d5bd793fe3e07d53adcc9938e/tumblr_nz81snqROl1u2hx1xo1_250.gif",
            "https://64.media.tumblr.com/78a1c9da70be314a88539cd0943f8d28/tumblr_nz81snqROl1u2hx1xo2_250.gif",
            "https://64.media.tumblr.com/d482c635d22186ccffea0064d4eab483/tumblr_nz81snqROl1u2hx1xo3_250.gif",
            "https://64.media.tumblr.com/12a23a658c750ae1913123dc4fd7e960/tumblr_nz81snqROl1u2hx1xo4_250.gif"]

        self.bot.kei_gif = ["https://tenor.com/view/lovelyz-kpop-kei-heart-%eb%9f%ac%eb%b8%94%eb%a6%ac%ec%a6%88-gif-18565559",
            "https://tenor.com/view/obliviate-lovelyz-lovelyzkei-kimjiyeon-kei-gif-18226419",
            "https://media.discordapp.net/attachments/448355257383387138/738587515237302312/254A623658B808590C.gif",
            "https://media.discordapp.net/attachments/448355257383387138/738587871904137266/99998A3F5C5A9C4553.gif",
            "https://tenor.com/view/lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kei-%EC%BC%80%EC%9D%B4-gif-16303444",
            "https://tenor.com/view/lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kei-%EC%BC%80%EC%9D%B4-gif-16303756",
            "https://tenor.com/view/kei-kpop-i-go-lovelyz-over-and-over-gif-15309714",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kpop-lovelyz-%EC%BC%80%EC%9D%B4-kei-gif-18182587",
            "https://tenor.com/view/kpop-lovelyz-kei-i-go-lovelinus-gif-15336273",
            "https://tenor.com/view/kpop-korean-lovelyz-kei-gif-10760158",
            "https://tenor.com/view/lovelyz-kei-delicous-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-16496984",
            "https://tenor.com/view/lovelyz-kei-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EC%BC%80%EC%9D%B4-kpop-gif-16516714",
            "https://tenor.com/view/lovelyz-kei-kim-jiyeon-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-16626147",
            "https://tenor.com/view/kpop-lovelyz-kei-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EC%BC%80%EC%9D%B4-gif-18225963",
            "https://tenor.com/view/lovelyz-kei-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EC%BC%80%EC%9D%B4-gif-18588396",
            "https://tenor.com/view/kei-lovelyz-adorable-braid-gif-18525447",
            "https://tenor.com/view/kpop-korean-lovelyz-kei-gif-10760160",
            "https://tenor.com/view/lovelyz-kei-mijoo-kiss-kpop-gif-16318978",
            "https://tenor.com/view/lovelyz-lovelyz-kei-kei-kim-kei-kim-jiyeon-gif-16341360",
            "https://tenor.com/view/lovelyz-kei-will-kpop-gif-14248063",
            "https://tenor.com/view/lovelyz-kei-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EC%BC%80%EC%9D%B4-gif-19103729",
            "https://gfycat.com/DesertedThatJohndory",
            "https://gfycat.com/UntriedDearEskimodog",
            "https://gfycat.com/ScaryBoldElk",
            "https://gfycat.com/DirectBlackandwhiteDonkey",
            "https://gfycat.com/DecimalFirstAmazonparrot",
            "https://64.media.tumblr.com/5e08f8ea60fc430718c695a02eaa9444/0d44540f3e406b4e-15/s250x400/e33591360a9c9fd35ee9451cecffdaf092f00855.gif",
            "https://64.media.tumblr.com/77040b818b0972726a4413a3e00163b7/0d44540f3e406b4e-73/s250x400/faa5763813bf25e8627819962d0cb708c3a6c40a.gif",
            "https://64.media.tumblr.com/bade8501183e5cc290a8bb115616bbd7/0d44540f3e406b4e-5b/s250x400/572d2f2e9f900ab5756d468b68a27c2a1d483645.gif",
            "https://64.media.tumblr.com/6dccf0f9207f1e2106c926d4c3f6ad5f/0d44540f3e406b4e-43/s250x400/5970d284f1e9f7a8549d7b12291173dcd3c63f8e.gif",
            "https://64.media.tumblr.com/3752008bc0fde05d5b72e0123a56d23b/e47debddbf25a2fe-b4/s250x400/2f787ea54f1040de36876c650e8e9eb24659f63f.gif",
            "https://64.media.tumblr.com/c56d4dd21f1b5fa64181b41daa8731af/e47debddbf25a2fe-54/s250x400/4443118ca2da3cab1c7f808b578a12776276a169.gif",
            "https://64.media.tumblr.com/dc9abfc7ad5b7eaf6cc3da217e66c7e3/e47debddbf25a2fe-fe/s250x400/d132369e9ed95514c6b42542735a427a8f9b9ddb.gif",
            "https://64.media.tumblr.com/6bd8ad7d7fc42e198b0ee7ae8245be4d/e47debddbf25a2fe-e1/s250x400/17afa8e99233b3bd25bf673183e2e3a763b0537a.gif"]

        self.bot.lovelyz_jisoo_gif = ["https://tenor.com/view/lovelyz-jisoo-oblivate-gif-18570444",
            "https://tenor.com/view/lovelyz-jisoo-oblivate-gif-18570439",
            "https://tenor.com/view/lovelyz-jisoo-smile-kpop-laugh-gif-16210760",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-jisoo-cute-gif-18419265",
            "https://tenor.com/view/lovelyz-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kpop-%EC%A7%80%EC%88%98-jisoo-gif-18243268",
            "https://tenor.com/view/lovelyz-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kpop-%EC%A7%80%EC%88%98-jisoo-gif-18243275",
            "https://tenor.com/view/jisoo-lovelyz-kpop-taking-picture-smile-gif-16278240",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-jisoo-wink-gif-18419268",
            "https://tenor.com/view/lovelyz-oblivate-jisoo-gif-18570448",
            "https://tenor.com/view/lovelyz-oblivate-jisoo-gif-18570440",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-jisoo-%EC%A7%80%EC%88%98-gif-18588384",
            "https://gfycat.com/familiarfluidcrossbill/",
            "https://gfycat.com/leftaffectionateibadanmalimbe/",
            "https://gfycat.com/loathsomehonoredchinesecrocodilelizard/",
            "https://gfycat.com/poshsilentleonberger/",
            "https://gfycat.com/poshsilentleonberger/",
            "https://gfycat.com/dimsimplisticewe",
            "https://gfycat.com/clutteredcandidhectorsdolphin",
            "https://gfycat.com/separateforkedbirdofparadise",
            "https://gfycat.com/jampackedsimplistickillifish",
            "https://gfycat.com/shortshortadder",
            "https://gfycat.com/diligentcandidhairstreak",
            "https://gfycat.com/foolishuncommonhuia",
            "https://gfycat.com/ickymaleamericanratsnake",
            "https://gfycat.com/entirevalidblueandgoldmackaw",
            "https://gfycat.com/soulfulwillingjaguarundi",
            "https://gfycat.com/warmangryjerboa",
            "https://gfycat.com/unhappycompetentbasilisk",
            "https://gfycat.com/untimelywarmheartedbug",
            "https://gfycat.com/completeinfantilealaskankleekai",
            "https://gfycat.com/grotesquemisguidedauk",
            "https://gfycat.com/BogusSadCoqui",
            "https://gfycat.com/PrestigiousGroundedBeardedcollie",
            "https://gfycat.com/reasonableentiredegu",
            "https://gfycat.com/happybasicgermanwirehairedpointer",
            "https://gfycat.com/lineartarteagle",
            "https://gfycat.com/hugeoldemeraldtreeskink",
            "https://gfycat.com/earlyuncommonindianpangolin",
            "https://gfycat.com/zealoussnivelingitaliangreyhound",
            "https://gfycat.com/IdolizedRightBlacknorwegianelkhound/",
            "https://gfycat.com/MatureMinorJackrabbit/",
            "https://gfycat.com/famousimpracticalfeline",
            "https://gfycat.com/enlightenedmeatygordonsetter",
            "https://gfycat.com/greatgreedyleonberger",
            "https://gfycat.com/grandrepentanthellbender",
            "https://gfycat.com/fortunatequarterlybuzzard",
            "https://gfycat.com/ringedhopefuleft",
            "https://gfycat.com/fondslowarthropods",
            "https://gfycat.com/ablesparklingbarasingha",
            "https://gfycat.com/highbogusermine",
            "https://gfycat.com/orderlydirectanglerfish",
            "https://gfycat.com/unfinishedeachgrackle",
            "https://gfycat.com/periodicnearcatbird",
            "https://gfycat.com/tediousunfinishedjaguar"]

        self.bot.babysoul_gif = ["https://tenor.com/view/lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EB%B2%A0%EC%9D%B4%EB%B9%84%EC%86%8C%EC%9A%B8-babysoul-gif-18331417",
            "https://tenor.com/view/kpop-lovelyz-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EB%B2%A0%EC%9D%B4%EB%B9%84%EC%86%8C%EC%9A%B8-babysoul-gif-18062427",
            "https://tenor.com/view/lovelyz-kpop-babysoul-mijoo-kiss-gif-16319206",
            "https://tenor.com/view/lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-babysoul-%EB%B2%A0%EC%9D%B4%EB%B9%84%EC%86%8C%EC%9A%B8-gif-16303603",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EB%B2%A0%EC%9D%B4%EB%B9%84%EC%86%8C%EC%9A%B8-babysoul-lovelyz-kpop-gif-18230362",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-babysoul-hi-gif-18419259",
            "https://tenor.com/view/lovelyz-babysoul-wow-kpop-gif-16074100",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EB%B2%A0%EC%9D%B4%EB%B9%84%EC%86%8C%EC%9A%B8-babysoul-lovelyz-kpop-gif-18230373",
            "https://tenor.com/view/lovelyz-jisoo-baby-soul-kpop-like-gif-16412292",
            "https://imgur.com/Cgao0Gu",
            "https://64.media.tumblr.com/4808e6d8449ca957597526cd0b31ad61/tumblr_orijmxXI6c1qg5nyao1_250.gif",
            "https://64.media.tumblr.com/cdc92fb1f87b4799973ecc5ece33070c/tumblr_orijmxXI6c1qg5nyao3_250.gif",
            "https://64.media.tumblr.com/4e5c852231496020fe304a36ff7a13a3/tumblr_orijmxXI6c1qg5nyao4_250.gif",
            "https://64.media.tumblr.com/77d9907fcc4636242861358272f54227/tumblr_orijmxXI6c1qg5nyao2_250.gif",
            "https://64.media.tumblr.com/912e392fb3d45d904921443b76f928a3/tumblr_ombgh2Wn0x1qg5nyao1_250.gif",
            "https://64.media.tumblr.com/c336a46c0f312c9fea8f347fc662ab00/tumblr_ombgh2Wn0x1qg5nyao3_250.gif",
            "https://64.media.tumblr.com/e54c4df0c1e449f6cdb5fd94a79f0b9c/tumblr_ombgh2Wn0x1qg5nyao2_250.gif",
            "https://64.media.tumblr.com/ce2a2787d54c21c10cfc3df72b881920/tumblr_ombgh2Wn0x1qg5nyao4_250.gif",
            "https://64.media.tumblr.com/32509db4027f6aa3b2d6fff447d84dde/tumblr_p0hs7tsocx1qg5nyao3_250.gif",
            "https://64.media.tumblr.com/49c9bdd3889ec556629dd4097b4696b9/tumblr_p0hs7tsocx1qg5nyao4_250.gif",
            "https://64.media.tumblr.com/ddcf5c3748bca5491c4a2ba6c1a0341a/tumblr_p0hs7tsocx1qg5nyao5_250.gif",
            "https://64.media.tumblr.com/cad53d0adf4f1ad41ea399279370f870/tumblr_p0hs7tsocx1qg5nyao2_250.gif"]

        self.bot.mijoo_gif = ["https://tenor.com/view/mijoo-wink-finger-heart-hearts-flying-gif-13440816",
            "https://tenor.com/view/mijoo-dancing-spin-gif-13440825",
            "https://tenor.com/view/lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-mijoo-%EB%AF%B8%EC%A3%BC-gif-16303580",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kpop-lovelyz-%EB%AF%B8%EC%A3%BC-mijoo-gif-18182571",
            "https://tenor.com/view/mijoo-kpop-lovelyz-%EB%AF%B8%EC%A3%BC-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-18213669",
            "https://tenor.com/view/lovelyz-mijoo-gif-18622921",
            "https://tenor.com/view/lovelyz-mijoo-gif-18622925",
            "https://tenor.com/view/lovelyz-mijoo-kpop-kei-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-19038372",
            "https://tenor.com/view/lovelyz-mijoo-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-focus-gif-19103728",
            "https://tenor.com/view/mijoo-lovelyz-kpop-asian-cute-gif-9068562",
            "https://tenor.com/view/mijoo-mijoo-wdzwm-lovelyz-walk-walking-gif-19219992",
            "https://tenor.com/view/lovelyz-mijoo-gif-18622927",
            "https://tenor.com/view/lovelyz-lee-mijoo-beautiful-beauty-gif-14322042",
            "https://tenor.com/view/mijoo-pose-gif-13440814",
            "https://tenor.com/view/lovelyz-lee-mijoo-mijoo-kpop-pretty-gif-16341282",
            "https://64.media.tumblr.com/370158992295ecc3fec32e2b4f671753/18690c252bf2865b-e4/s250x400/2abf67d98d6531c5cf587ee8a1efbde261b81ad5.gif",
            "https://64.media.tumblr.com/84e3daf669fc07f0619d9b73e7226cd6/18690c252bf2865b-de/s250x400/2054b8cd53390e0b514393adacdc854a35910499.gif",
            "https://64.media.tumblr.com/b88e506035ecb19e252f33572d7343f1/18690c252bf2865b-e3/s250x400/36d853d824b286d1d94373388ac462fec9de98cd.gif",
            "https://64.media.tumblr.com/f816e0deb0eebd3f5cf05bd352825669/18690c252bf2865b-54/s250x400/2deb4dc5a8bcc50eb0cf43f8f9da6c0625452002.gif",
            "https://64.media.tumblr.com/69102285f6a63429ac3648d0facec466/6f48ce840c131b9b-44/s250x400/3e2965e18252f6bc10b88938557d1df62974eee9.gif",
            "https://64.media.tumblr.com/3748b0a66154ff8569d933503dc631bf/6f48ce840c131b9b-78/s250x400/195f8bcf9996cff0430547a7fd9c7a2f5fa9702e.gif",
            "https://64.media.tumblr.com/1a9f6d3da7218a1ba1a59747774b33e3/6f48ce840c131b9b-aa/s250x400/2f943a59a6d42b36881099a312fc70650b23e02d.gif",
            "https://64.media.tumblr.com/570ba14da4facde6e17cd0608214f9e5/6f48ce840c131b9b-f9/s250x400/84221d7551fd6c6d1f083016f1e5a646faa34d19.gif",
            "https://64.media.tumblr.com/0cdd67b40628ba6e2a60c759650f3fb0/b5660292707323fb-6e/s250x400/72bde4be289ba11362c1902cdab841e9a67f1a72.gif",
            "https://64.media.tumblr.com/cf25de7c41b04721745fb56806226f7c/b5660292707323fb-ea/s250x400/c7e0cda5a43e8ee33051acfc136abe191cb8685d.gif",
            "https://64.media.tumblr.com/75313dd56cf15451395f9e42b5c6045f/b5660292707323fb-11/s250x400/a7e480845fa6666559790d86b7e0202577e31eac.gif",
            "https://64.media.tumblr.com/28685e7fd05f28d12686416501708954/b5660292707323fb-96/s250x400/2910aa4775471c88304e5a6dabbf56c7feba1eff.gif",
            "https://64.media.tumblr.com/6b735824ea9bb3a03a06a5c9dc3a359d/fe08a977db08bb1d-b9/s250x400/31339f84d5ab9546c0c38016722c485942d76dc4.gif",
            "https://64.media.tumblr.com/72b3ae942786f1f06b17920e89a2d029/fe08a977db08bb1d-82/s250x400/ff1d754db3f027f971b99f40d4cec0d7ddb055cf.gif",
            "https://64.media.tumblr.com/f25a67c4c2dfee9990383360a85bf54d/fe08a977db08bb1d-45/s250x400/67d05adde73e5728453414e47157d2fac6b6a495.gif",
            "https://64.media.tumblr.com/6a62607c6d5baf409ba3d926b76d40b9/fe08a977db08bb1d-98/s250x400/687f775d7028d2de2e755eeaae307f797e7c4307.gif"]

        self.bot.jiae_gif = ["https://tenor.com/view/lovelyz-jiae-kpop-wait-cute-gif-16204526",
            "https://tenor.com/view/lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-jiae-%EC%A7%80%EC%95%A0-gif-16303788",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-jiae-kpop-%EC%A7%80%EC%95%A0-gif-16459876",
            "https://tenor.com/view/lovelyz-jiae-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EC%A7%80%EC%95%A0-gif-17339573",
            "https://tenor.com/view/kpop-%EC%A7%80%EC%95%A0-jiae-lovelyz-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-18243238",
            "https://tenor.com/view/kpop-%EC%A7%80%EC%95%A0-jiae-lovelyz-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-18243242",
            "https://tenor.com/view/kpop-%EC%A7%80%EC%95%A0-jiae-lovelyz-gif-18243246",
            "https://tenor.com/view/jiae-lovelyz-gif-19181488",
            "https://tenor.com/view/jiae-lovelyz-kpop-twinkle-yoo-jiae-gif-15899150",
            "https://tenor.com/view/lovelyz-jiae-yoo-jiae-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-17339578",
            "https://tenor.com/view/lovelyz-yoo-jiae-jiae-lovelyz-jiae-kpop-gif-16673424",
            "https://tenor.com/view/lovelyz-yoo-jiae-jiae-lovelyz-jiae-kpop-gif-16673446",
            "https://tenor.com/view/lovelyz-jiae-yoo-jiae-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-17339578",
            "https://64.media.tumblr.com/a8009975ac7f76f877ccdd00b1a10108/tumblr_pac8qbMI4k1qg5nyao4_r1_250.gif",
            "https://64.media.tumblr.com/7cb8025f6fa0ecb97d9fd9446400e3d0/tumblr_pac8qbMI4k1qg5nyao1_250.gif",
            "https://64.media.tumblr.com/c0e7d9dccb17e28958b95662b9ca9d42/tumblr_pac8qbMI4k1qg5nyao2_250.gif",
            "https://64.media.tumblr.com/c9808a6350e682c511c170b3e20d1810/tumblr_pac8qbMI4k1qg5nyao3_r1_250.gif",
            "https://64.media.tumblr.com/88ce5ac7451f289b43380dbafda1d88f/tumblr_p8mrqlMolB1rwup2io2_250.gif",
            "https://64.media.tumblr.com/ca8893821421d0fc38fc15b47e35d16a/tumblr_p8mrqlMolB1rwup2io1_250.gif",
            "https://64.media.tumblr.com/c206b9b412d2042714e36e8be77fd92c/tumblr_p8ilagsDf11qg5nyao2_250.gif",
            "https://64.media.tumblr.com/3c529194c45c0bbcafa8bf913c184422/tumblr_p8ilagsDf11qg5nyao1_250.gif",
            "https://64.media.tumblr.com/995d4503b2c45e678846e692f0ccb5b2/tumblr_p7vdznr0oV1qg5nyao4_r1_250.gif",
            "https://64.media.tumblr.com/005ea65a093a1d30d91ea1cef572af49/tumblr_p7vdznr0oV1qg5nyao2_r1_250.gif",
            "https://64.media.tumblr.com/4c17f6f32116e30501ad4f236398ccd0/tumblr_p7vdznr0oV1qg5nyao3_r2_250.gif",
            "https://64.media.tumblr.com/98a2a0adeeaaed24e9c8421fa2a01783/tumblr_p7vdznr0oV1qg5nyao1_250.gif"]

        self.bot.lovelyz_jin_gif = ["https://tenor.com/view/lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-jin-%EB%AA%85%EC%9D%80-gif-16303377",
            "https://tenor.com/view/sugarman3-%EC%8A%88%EA%B0%80%EB%A7%A83-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-%EB%B0%95%EB%AA%85%EC%9D%80-gif-15800266",
            "https://tenor.com/view/lovelyz-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-jin-kpop-%EB%AA%85%EC%9D%80-gif-18588391",
            "https://tenor.com/view/kpop-jin-lovelyz-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EB%AA%85%EC%9D%80-gif-18240324",
            "https://tenor.com/view/kpop-jin-lovelyz-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EB%AA%85%EC%9D%80-gif-18240328",
            "https://tenor.com/view/lovelyz-jin-kpop-cute-pretty-gif-15958211",
            "https://tenor.com/view/lovelyz-jin-kpop-ooh-gif-15998320",
            "https://tenor.com/view/kpop-lovelyz-jin-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EB%AA%85%EC%9D%80-gif-18230835",
            "https://tenor.com/view/lovelyz-jin-baby-talking-cute-should-be-like-gif-16057160",
            "https://tenor.com/view/lovelyz-jin-heart-pretty-cute-gif-16057166",
            "https://gfycat.com/FakeMilkyAbyssiniangroundhornbill",
            "https://64.media.tumblr.com/11c887d75f9ba38ffb2567b0313e2459/8237ca7f37450cd7-9e/s400x600/8d7ebdd11a86412b4723ffeb68979486075cee29.gif",
            "https://64.media.tumblr.com/5d11658d5520584ea8ecbb56ac37b68e/8237ca7f37450cd7-fd/s400x600/41b5d93e0d6ee65fdf2d8bb6bd9ceb028ea88929.gif",
            "https://64.media.tumblr.com/95c9653f1a038cfcb93834a09e5c2b27/8237ca7f37450cd7-66/s400x600/506db396b8149ddd349dd0c6c4572404b904dc9e.gif",
            "https://64.media.tumblr.com/0da3c1e965a9a22edd6ca3254d31bdd2/5725f316137930e8-c5/s250x400/3a3508d5b492f48b8722a5a518f10e9bb0d8e7e6.gif"]

        self.bot.sujeong_gif = ["https://tenor.com/view/sujeong-lovelyz-ryu-sujeong-gif-13815496",
            "https://tenor.com/view/%EB%A5%98%EC%88%98%EC%A0%95-lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-sujeong-gif-18225977",
            "https://tenor.com/view/sujeon-sujeong-lovelyz-mijoo-babysoul-gif-18201454",
            "https://tenor.com/view/%EB%A5%98%EC%88%98%EC%A0%95-lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-sujeong-gif-18225979",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-sujeong-%EB%A5%98%EC%88%98%EC%A0%95-gif-18419231",
            "https://tenor.com/view/lovelyz-sujeong-gif-18601629",
            "https://tenor.com/view/sujeong-ryusujeong-lovelyz-lovelyzgif-sujeonggif-gif-19038286",
            "https://tenor.com/view/lovelyz-lovelyzsujeong-ryusujeong-obliviate-unforgettable-gif-18226595",
            "https://tenor.com/view/lovelyz-sujeong-gif-18601631",
            "https://tenor.com/view/lovelyz-mijoo-kpop-sujeong-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-19038398",
            "https://tenor.com/view/sujeong-lovelyz-ryu-sujeong-gif-13815502",
            "https://tenor.com/view/lvlz-lovelyz-ryu-sujeong-sujeong-kpop-gif-16341229",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-sujeong-kpop-%EB%A5%98%EC%88%98%EC%A0%95-gif-17312055",
            "https://tenor.com/view/lovelyz-sujeong-kpop-%EB%A5%98%EC%88%98%EC%A0%95-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-17312104",
            "https://tenor.com/view/sujeong-lovelyz-ryu-sujeong-gif-13815500",
            "https://tenor.com/view/sujeong-lovelyz-ryu-sujeong-gif-13815496",
            "https://gfycat.com/infinitetallindochinahogdeer",
            "https://gfycat.com/whoppingglossychamois",
            "https://gfycat.com/unpleasantoptimistichoneyeater",
            "https://gfycat.com/coldelectricbluetonguelizard",
            "https://64.media.tumblr.com/e04e6663d75499bed946033a8d07d6dd/37d9d64d01f702f3-4e/s250x400/9f9b4fdfa581251b8bb87c123e8a28ee3990d6d4.gif",
            "https://64.media.tumblr.com/712342847f2e81314848a910f442dd44/37d9d64d01f702f3-87/s250x400/261394c96f29820a86f5ca3084935a698b425ec0.gif",
            "https://64.media.tumblr.com/d8097807d9d361e61f56170baca700ad/37d9d64d01f702f3-75/s250x400/bbb86823ef3ccd4cbc50d0be010af88064f69027.gif",
            "https://64.media.tumblr.com/2edd80f3ddc10ddcd824b7f0312375c2/37d9d64d01f702f3-af/s250x400/be7b74024208dabc9d273ff7f9080868ce3d09e9.gif",
            "https://64.media.tumblr.com/47d407bd38bdee9d08859bbed0b51667/802d203639dff8e9-02/s250x400/d6879d8197a7773a26f9d98232f798edcdf7d539.gif",
            "https://64.media.tumblr.com/bbcd652181e9f83286f6f26967b39447/802d203639dff8e9-2f/s250x400/7c40466ffd461884b7c3e39c50a4e4cd5e245206.gif",
            "https://64.media.tumblr.com/92dfdfe4e821fa200564bb9329f405ae/802d203639dff8e9-38/s250x400/9c70281e158dc51e4a788d2e8c033ae04d28ed0f.gif",
            "https://64.media.tumblr.com/3fcae949fd66a318660f9ed927782eb6/802d203639dff8e9-56/s250x400/e9c3484c067cd3d0937387dcf0d02248222be00c.gif",
            "https://64.media.tumblr.com/087a8087034d5cfab97df1ee587ee3f6/3f8e50176a55c007-a7/s250x400/329643a58d43dd04b2cf142e071e3334b0dc1e4c.gif",
            "https://64.media.tumblr.com/fb01f8785a4c542b7d578c533fe3cbf2/3f8e50176a55c007-6a/s250x400/f2d74d6b8ac2c63e23762036fc99124344e629cb.gif",
            "https://64.media.tumblr.com/0d2ae30c4215ef6d5f26f2a586781066/3d63c5fc2c0571e5-db/s250x400/5f26d6efa2130a8cc8645c76d37432afacbfed33.gif",
            "https://64.media.tumblr.com/f2b7afdee93b9d418d830019e0908289/3d63c5fc2c0571e5-1e/s250x400/9e4f1cf0feb6ce0f1496a83777baf0fa85ce1ddf.gif",
            "https://64.media.tumblr.com/33f12691731e60458b2b2f24ffd804ce/3d63c5fc2c0571e5-a0/s250x400/dd89869072c96282814a0836d8da4222c0f32fa8.gif",
            "https://64.media.tumblr.com/a917242021f59baea115b39312173b55/3d63c5fc2c0571e5-74/s250x400/a54e4f620027c41a072cd516ebfb373d86dc6757.gif"]

    @commands.command()
    async def lovelyz(self, ctx, *, arg="nope"):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Lovelyz {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "yein":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Lovelyz Yein :white_heart:')
                await ctx.send(random.choice(self.bot.yein_gif))
                await ctx.message.delete()
        elif arg == "kei":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Kei <:keiheart:785792014657912842>')
                await ctx.send(random.choice(self.bot.kei_gif))
                await ctx.message.delete()
        elif arg == "jisoo":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jisoo :white_heart:')
                await ctx.send(random.choice(self.bot.lovelyz_jisoo_gif))
                await ctx.message.delete()
        elif arg == "baby soul" or arg =="babysoul":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Baby Soul :purple_heart:')
                await ctx.send(random.choice(self.bot.babysoul_gif))
                await ctx.message.delete()
        elif arg == "mijoo":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Mijoo :heart:')
                await ctx.send(random.choice(self.bot.mijoo_gif))
                await ctx.message.delete()
        elif arg == "jiae":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jiae :white_heart:')
                await ctx.send(random.choice(self.bot.jiae_gif))
                await ctx.message.delete()
        elif arg == "jin":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jin :white_heart::black_heart:')
                await ctx.send(random.choice(self.bot.lovelyz_jin_gif))
                await ctx.message.delete()
        elif arg == "sujeong":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Sujeong <:keiheart:785792014657912842>')
                await ctx.send(random.choice(self.bot.sujeong_gif))
                await ctx.message.delete()

   

def setup(client):
    client.add_cog(Lovelyz(client))