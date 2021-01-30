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
lulu = 721653307998994453
princessuwu = 716841614185857086
k8 = 573974040679809044

class BTSPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.v_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781374550419439626/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374550906503188/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374551534600212/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374552059543592/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374552461934622/image4.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374552924094494/image5.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374553388613632/image6.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374553905168405/image7.gif",
            "https://tenor.com/view/kim-taehyung-taehyung-bts-bts-v-hot-gif-14822919",
            "https://tenor.com/view/bts-done-taehyung-tired-sleepy-gif-16117979",
            "https://tenor.com/view/taehyung-kim-taehyung-smile-tae-gucci-boy-gif-16369645",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-v-kim-taehyung-gif-17104113",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-v-kim-taehyung-gif-16658106",
            "https://tenor.com/view/taehyung-kpop-oppa-cute-smile-gif-8626038",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-v-kim-taehyung-gif-16993427",
            "https://tenor.com/view/taehyung-bts-cute-handsome-looking-gif-16986526",
            "https://tenor.com/view/taehyung-peace-cute-gif-19086526",
            "https://tenor.com/view/taehyung-kim-taehyung-tae-tae-tae-vante-gif-18345939",
            "https://cdn.discordapp.com/attachments/802261119900975144/802262897426300938/image0.gif",
            "https://cdn.discordapp.com/attachments/802261119900975144/802262897828429832/image1.gif",
            "https://cdn.discordapp.com/attachments/802261119900975144/802262898168430642/image2.gif",
            "https://cdn.discordapp.com/attachments/802261119900975144/804199746004058132/18173ea3-c36c-481c-aa3b-25250410ee13.gif",
            "https://cdn.discordapp.com/attachments/802261119900975144/804199746615902208/33dddf33-0c7a-46f0-a422-0471ab3770ec.gif",
            "https://cdn.discordapp.com/attachments/802261119900975144/804199747287908372/7d19ad2d-e5d3-454d-94c9-eeaadc1f4653.gif",
            "https://cdn.discordapp.com/attachments/802261119900975144/804199747992027156/164814c4-9b1b-4566-af3c-57280518ac2f.gif",
            "https://cdn.discordapp.com/attachments/802261119900975144/804199748491411487/00e1d541-b699-48c3-a136-780c2bf6d212.gif",
            "https://cdn.discordapp.com/attachments/802261119900975144/804199748868374528/ab711ed3-074b-4235-8f40-813caf457da3.gif",
            "https://cdn.discordapp.com/attachments/802261119900975144/804202993083875328/BTS-V-1.gif",
            "https://cdn.discordapp.com/attachments/802261119900975144/804202993636474920/BTS-V-16.gif",
            "https://cdn.discordapp.com/attachments/802261119900975144/804202994282790923/download_7.gif",
            "https://cdn.discordapp.com/attachments/802261119900975144/804202994941820948/BTS-V-14-1.gif",
            "https://cdn.discordapp.com/attachments/802261119900975144/804202995523911680/BTS-V-1-1.gif",
            "https://cdn.discordapp.com/attachments/802261119900975144/804202996422148116/BTS-V-12.gif"]

        self.bot.suga_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781376996051517460/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376997473255434/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376998244483112/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376998852788224/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377281868300318/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377282270035987/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377283252158484/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377284031905842/image3.gif",
            "https://tenor.com/view/bts-suga-kpop-uwu-big-baby-boi-gif-12988023",
            "https://tenor.com/view/bts-suga-cute-smile-kpop-gif-13230684",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-suga-suga-gif-17096216",
            "https://tenor.com/view/bts-suga-laugh-smile-gif-14696728",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-suga-suga-gif-9734489",
            "https://tenor.com/view/bts-suga-kpop-cute-smirk-gif-6231660",
            "https://tenor.com/view/haha-yoongi-nod-gif-12218918",
            "https://tenor.com/view/bts-nod-cheeks-cute-yoongi-gif-14760712",
            "https://tenor.com/view/bts-min-yoongi-run-gif-13961845",
            "https://tenor.com/view/bts-beautiful-shy-blush-teeth-gif-19573947",
            "https://tenor.com/view/yoongi-sad-cute-face-gif-19211545",
            "https://tenor.com/view/bts-yoongi-smile-gif-15454873",
            "https://tenor.com/view/bts-yoongi-funny-gif-14760711",
            "https://cdn.discordapp.com/attachments/802261156571774976/802262255545614346/image0.gif",
            "https://cdn.discordapp.com/attachments/802261156571774976/802262256049192960/image1.gif",
            "https://cdn.discordapp.com/attachments/802261156571774976/802262256545038376/image2.gif"]

        self.bot.jhope_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781376181487796224/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376182888431616/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376183551918090/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376184256430100/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376185291767838/image4.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376186805649408/image5.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781376187368472626/image6.gif",
            "https://tenor.com/view/jhope-bts-gif-12584763",
            "https://tenor.com/view/bts-jhope-hoseok-jung-gif-14371797",
            "https://tenor.com/view/jhope-hobi-yes-hoseok-gif-16178897",
            "https://tenor.com/view/jhope-jhopebts-btsjhope-hobi-bts-gif-18149405",
            "https://tenor.com/view/jhope-heart-%EB%B0%A9%ED%83%84-%EC%A0%9C%EC%9D%B4%ED%99%89-%EB%B0%A9%ED%83%84%EC%86%8C%EB%85%84%EB%8B%A8-gif-10577474",
            "https://tenor.com/view/jhope-stare-serious-gif-12853415",
            "https://cdn.discordapp.com/attachments/802261179409104896/802263201810350100/image0.gif",
            "https://cdn.discordapp.com/attachments/802261179409104896/804204203597365278/J-Hope-3.gif",
            "https://cdn.discordapp.com/attachments/802261179409104896/804204204524568596/J-Hope-10.gif",
            'https://cdn.discordapp.com/attachments/802261179409104896/804204205103513670/download-5.gif',
            "https://cdn.discordapp.com/attachments/802261179409104896/804204205895188561/hsstaygold2.gif",
            "https://cdn.discordapp.com/attachments/802261179409104896/804205035810455552/a2a43f71-aa27-4367-ac91-32b89e027275.gif",
            "https://cdn.discordapp.com/attachments/802261179409104896/804516918106128434/0d71444d-acc6-43ce-8b23-c4ee903fbf07.gif",
            "https://cdn.discordapp.com/attachments/802261179409104896/804516918476013578/f217981b-880a-4327-bace-b8356719faa2.gif"]

        self.bot.jungkook_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781375454966972426/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375486843551775/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375522592129024/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375594725376000/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375595178491904/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375596798279710/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375705270583306/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375706437255178/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781375707854012416/image2.gif",
            "https://tenor.com/view/kiss-jungkook-gif-18806916",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-jungkook-jungkook-gif-15708420",
            "https://tenor.com/view/jungkook-long-hair-sexy-jungkook-bts-bts-gif-14761886",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-jungkook-jeon-jungkook-gif-17601596",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-jungkook-jungkook-gif-17106990",
            "https://tenor.com/view/bts-jungkook-chocchipkookies-eyes-gif-12784010",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-kpop-cute-gif-16693216",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-jungkook-jungkook-gif-15708420",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-jungkook-jeon-jungkook-gif-17817086",
            "https://tenor.com/view/hot-lip-biting-jungkook-bts-gif-10836246",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-beyond-the-scene-jungkook-gif-13078096",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-jungkook-jungkook-gif-16110608",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-kpop-jungkook-gif-5256088",
            "https://tenor.com/view/idonotown-madeby-g6-jeon-jungkook-bts-mots-gif-18778490",
            "https://tenor.com/view/bts-fake-love-live-jungkook-abs-gif-11902712",
            "https://tenor.com/view/sexy-hot-long-hair-smile-jeon-jungkook-gif-15404281",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-jungkook-jungkook-gif-16637371",
            "https://tenor.com/view/jungkook-jeon-bts-bangtan-boys-gif-9324526",
            "https://tenor.com/view/jungkook-bts-hot-long-hair-tongue-out-gif-14761906",
            "https://tenor.com/view/jungkook-bts-hot-long-hair-tongue-out-gif-14761906",
            "https://tenor.com/view/jungkook-bts-sexy-gif-7362447",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-jungkook-jungkook-gif-17106990",
            "https://tenor.com/view/jungkookhot-bts-gif-19349411",
            "https://tenor.com/view/hot-jungkook-bts-bangtan-army-gif-19425882",
            "https://tenor.com/view/bts-jungkook-gif-13715171",
            "https://tenor.com/view/jungkook-bts-hot-kookie-gif-9478037",
            "https://tenor.com/view/jungkook-jeon-jungkook-jeongguk-kookie-jk-gif-19174064",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-jungkook-jungkook-gif-16637371",
            "https://tenor.com/view/jungkook-hot-jeon-gif-18835307",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-jungkook-jungkook-gif-17106984",
            "https://tenor.com/view/bts-hot-sexy-kpop-korea-gif-13912305",
            "https://tenor.com/view/bts-jungkook-hot-gif-19446454",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-bts-jungkook-jungkook-gif-15927284",
            "https://tenor.com/view/jungkook-bts-hot-gif-19349412",
            "https://tenor.com/view/bts-jungkook-sexy-hot-sexy-jungkook-gif-12854189",
            "https://tenor.com/view/jk-jungkook-bts-sexy-concert-gif-14157549",
            "https://tenor.com/view/dangerous-bts-mama-2018-kpop-gif-13083680",
            "https://tenor.com/view/bts-jungkook-sexy-gif-11254424",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-jungkook-jeon-jungkook-gif-17243965",
            "https://tenor.com/view/jungkook-idols-sexy-bts-dance-gif-13632132",
            "https://tenor.com/view/jungkook-sexy-sexy-dance-sexy-man-gif-15613580",
            "https://tenor.com/view/bts-bts-jungkook-jungkook-jungkook-hot-kpop-gif-12181387",
            "https://tenor.com/view/bts-jungkook-sexy-gif-5184803",
            "https://tenor.com/view/jungkook-jeon-jungkook-bts-jeon-sexy-gif-13654678",
            "https://tenor.com/view/hot-sexy-bts-jungkook-stare-gif-13983979",
            "https://tenor.com/view/jungkook-sexy-sexy-dance-sexy-man-gif-15613580",
            "https://tenor.com/view/evil-jungkook-burning-hands-up-gif-12559556",
            "https://tenor.com/view/bts-jungkook-sexy-gif-11254449",
            "https://tenor.com/view/jungkook-bts-sexy-gif-11038770",
            "https://tenor.com/view/jungkook-bts-hot-sexy-dance-gif-12004953",
            "https://tenor.com/view/jungkook-bts-hot-long-hair-tongue-out-gif-14761906",
            "https://tenor.com/view/jungkook-jeon-jungkook-jungkook-jeon-bts-bangtan-boys-gif-5149930",
            "https://gfycat.com/anguishedcarefreegodwit",
            "https://gfycat.com/repulsivehotamericanwarmblood",
            "https://gfycat.com/evendismalamphibian",
            "https://tenor.com/view/jeon-jungkook-bts-jungkook-jungkook-bts-youre-dead-gif-17246646",
            "https://tenor.com/view/jungkook-jeon-jungkook-jungkook-jeon-bts-bangtan-boys-gif-5204531",
            "https://tenor.com/view/jungkook-jeon-jungkook-jeongguk-jk-kookie-gif-18346698",
            "https://tenor.com/view/smile-giggle-smiling-bts-jeon-jungkook-gif-15821321",
            "https://cdn.discordapp.com/attachments/802261212846882826/802263665729863700/image0.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/802263666191106088/image1.gif",
            "https://cdn.discordapp.com/attachments/797701519582691369/804194729176727612/10d49af0-f5a9-4cbf-a697-76880137a228.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804196764805496862/786e128f-5d64-471c-bc58-fe85b89f0b96.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804196765376053339/304e79db-3ed0-4f26-ba2a-3f5e881933e6.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804196765758652476/fd8e1773-be1a-4e0c-93a6-120a5db61912.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804196766194073630/85601e43-a80a-41e3-bb5d-5041c5e82be9.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804196766680350720/3ca1ba61-e06e-4f47-93ff-f74ed325c76a.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804198636639485972/Tumblr_l_383021191996233.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804198637164953630/Tumblr_l_383037442704567.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804198637680066570/Tumblr_l_383093118244450.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804198638132920370/Tumblr_l_383105686357518.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804198638753415189/Tumblr_l_383127170315464.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804201653347549184/OldfashionedQueasyDragonfly-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804201653896085504/AccurateForthrightBass-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804201654781870080/HarmoniousZealousCow-size_restricted.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804201655360815134/Jungkook_2.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804208038373752852/ezgif.com-gif-maker_5.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804208039351681034/jktfma20_2.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/804208430440906763/jktfma20_4.gif"]

        self.bot.btsjin_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781378238282727464/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378239204556810/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378240916619264/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378241817608192/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378242749005904/image4.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378361071108106/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378361943261194/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378363729510430/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378364875210812/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378548342587402/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781379997059121192/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781379997788274698/image1.gif",
            "https://cdn.discordapp.com/attachments/802261241128419348/802264122678837319/image0.gif",
            "https://cdn.discordapp.com/attachments/802261241128419348/802264122954874920/image1.gif",
            "https://cdn.discordapp.com/attachments/802261241128419348/804515701653897288/191027_SYS_.gif"]

        self.bot.jimin_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781377634956345383/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377635636609044/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377636190519296/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377637137645578/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377637863391262/image4.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377786698661888/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377787608301568/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377788585181184/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377789689200640/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781377790510760006/image4.gif",
            "https://cdn.discordapp.com/attachments/802261268165689365/802264596152713276/image0.gif",
            "https://cdn.discordapp.com/attachments/802261268165689365/802264596425605146/image1.gif",
            "https://cdn.discordapp.com/attachments/802261268165689365/802264596734803978/image2.gif",
            "https://cdn.discordapp.com/attachments/802261268165689365/802264597213216818/image3.gif",
            "https://cdn.discordapp.com/attachments/802261268165689365/802264597749956648/image4.gif"]

        self.bot.rm_gif = ["https://cdn.discordapp.com/attachments/781312260118806529/781374090497753098/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374226607112252/image0.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374227605225482/image1.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374228132790323/image2.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374228456275968/image3.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374229014511646/image4.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374229836333086/image5.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374230364160030/image6.gif",
            "https://cdn.discordapp.com/attachments/781312260118806529/781374230952411136/image7.gif",
            "https://tenor.com/view/namjoon-bts-bangtan-boys-bangtan-sonyeondan-kpop-gif-12559453",
            "https://tenor.com/view/namjoon-kim-namjoon-rm-joonie-gif-18400460",
            "https://tenor.com/view/rap-monster-kpop-bts-heart-silly-gif-8137935",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-rap-monster-kim-namjoon-gif-17774036",
            "https://tenor.com/view/namjoon-rm-kim-namjoon-joonie-smile-gif-18345522",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-rap-monster-kim-namjoon-gif-17848085",
            "https://tenor.com/view/bts-rm-kpop-smile-namjoon-gif-16911179",
            "https://tenor.com/view/bts-nam-joon-rap-monster-gif-9813314",
            "https://tenor.com/view/bts-bangtan-boys-bangtan-sonyeondan-rap-monster-kim-namjoon-gif-17848254",
            "https://tenor.com/view/bts-rm-namjoon-gif-18205004",
            "https://tenor.com/view/bts-kim-nam-joon-aesthetic-rm-gif-15168245",
            "https://tenor.com/view/namjoon-bts-kpop-walk-gif-12559450",
            "https://tenor.com/view/kim-namjoon-bts-rm-laugh-lol-gif-10964941",
            "https://tenor.com/view/bts-heart-rm-cute-namjoon-gif-13444506",
            "https://cdn.discordapp.com/attachments/802261293565607946/802265083274330182/image0.gif",
            "https://cdn.discordapp.com/attachments/802261293565607946/802265172085178408/image0.gif",
            "https://cdn.discordapp.com/attachments/802261293565607946/802265426444681226/image0.gif",
            "https://cdn.discordapp.com/attachments/802261293565607946/802265426942754876/image1.gif",
            "https://cdn.discordapp.com/attachments/802261293565607946/802265427291406376/image2.gif",
            "https://cdn.discordapp.com/attachments/802261293565607946/802265427618168892/image3.gif",
            "https://cdn.discordapp.com/attachments/802261293565607946/802265427942178866/image4.gif",
            "https://cdn.discordapp.com/attachments/802261293565607946/802265834181230612/image0.gif",
            "https://cdn.discordapp.com/attachments/802261293565607946/802265834864377886/image1.gif"]

    @commands.command()
    async def bts(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [BTS {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "v" or arg == "taehyung" or arg == "kim taehyung":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about V :heart:')
                    await ctx.send(random.choice(self.bot.v_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about V :heart:')
                await ctx.send(random.choice(self.bot.v_gif))
                await ctx.message.delete()
        elif arg == "suga":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Suga :heart:')
                    await ctx.send(random.choice(self.bot.suga_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Suga :heart:')
                await ctx.send(random.choice(self.bot.suga_gif))
                await ctx.message.delete()
        elif arg == "jhope" or arg == "j-hope" or arg == "j hope":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about J-Hope :heart:')
                    await ctx.send(random.choice(self.bot.jhope_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about J-Hope :heart:')
                await ctx.send(random.choice(self.bot.jhope_gif))
                await ctx.message.delete()
        elif arg == "jungkook" or arg == "k8":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@{k8}>, <@!{ctx.author.id}> is talking about Jungkook :heart:')
                    await ctx.send(random.choice(self.bot.jungkook_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jungkook :heart:')
                await ctx.send(random.choice(self.bot.jungkook_gif))
                await ctx.message.delete()
        elif arg == "jin":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jin :heart:')
                    await ctx.send(random.choice(self.bot.btsjin_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jin :heart:')
                await ctx.send(random.choice(self.bot.btsjin_gif))
                await ctx.message.delete()
        elif arg == "jimin":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jimin :heart:')
                    await ctx.send(random.choice(self.bot.jimin_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jimin :heart:')
                await ctx.send(random.choice(self.bot.jimin_gif))
                await ctx.message.delete()
        elif arg == "rm" or arg == "namjoon":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about RM :heart:')
                    await ctx.send(random.choice(self.bot.rm_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about RM :heart:')
                await ctx.send(random.choice(self.bot.rm_gif))
                await ctx.message.delete()

    @commands.command()
    async def v(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about V :heart:')
                await ctx.send(random.choice(self.bot.v_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about V :heart:')
            await ctx.send(random.choice(self.bot.v_gif))
            await ctx.message.delete()

    @commands.command()
    async def suga(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Suga :heart:')
                await ctx.send(random.choice(self.bot.suga_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Suga :heart:')
            await ctx.send(random.choice(self.bot.suga_gif))
            await ctx.message.delete()

    @commands.command(aliases = ['j-hope'])
    async def jhope(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about J-Hope :heart:')
                await ctx.send(random.choice(self.bot.jhope_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about J-Hope :heart:')
            await ctx.send(random.choice(self.bot.jhope_gif))
            await ctx.message.delete()

    @commands.command(aliases = ["k8"])
    async def jungkook(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@{k8}>, <@!{ctx.author.id}> is talking about Jungkook :heart:')
                await ctx.send(random.choice(self.bot.jungkook_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jungkook :heart:')
            await ctx.send(random.choice(self.bot.jungkook_gif))
            await ctx.message.delete()

    @commands.command()
    async def jin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jin :heart:')
                await ctx.send(random.choice(self.bot.btsjin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jin :heart:')
            await ctx.send(random.choice(self.bot.btsjin_gif))
            await ctx.message.delete()

    @commands.command()
    async def jimin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jimin :heart:')
                await ctx.send(random.choice(self.bot.jimin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jimin :heart:')
            await ctx.send(random.choice(self.bot.jimin_gif))
            await ctx.message.delete()

    @commands.command(aliases = ['namjoon'])
    async def rm(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about RM :heart:')
                await ctx.send(random.choice(self.bot.rm_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about RM :heart:')
            await ctx.send(random.choice(self.bot.rm_gif))
            await ctx.message.delete()

def setup(client):
    client.add_cog(BTSPings(client))