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
            "https://cdn.discordapp.com/attachments/802261119900975144/804202996422148116/BTS-V-12.gif",
            "https://64.media.tumblr.com/daf2ec37ac4afbcd92504a902040c729/tumblr_p349yiUmfo1r6mvzao1_540.gif",
            "https://64.media.tumblr.com/79bdeda28ada702bfd02db6367b15dbd/tumblr_ppr3djVot41tc8b5go1_540.gif",
            "https://64.media.tumblr.com/60f78123f02e45de350c776bf147725b/tumblr_pu6fb4y6IG1uimmhbo1_r1_540.gif",
            "https://64.media.tumblr.com/9708a2350cc0f60e5c1db12feeb4b386/433f918020b737e6-2d/s540x810/cceeaa26a67b9d2e708804c0cc4714a8826b3308.gif",
            "https://64.media.tumblr.com/e553bcf844d5d7772034e14b16a8c3f6/tumblr_pklyafMcga1rngqpbo1_540.gif",
            "https://64.media.tumblr.com/343a0602f70b086670c0e25347bbd198/tumblr_paliulki171x2uzv6o1_540.gif",
            "https://64.media.tumblr.com/847ff08b7797fe0ba03204dab7f72729/tumblr_p6hmcwir7A1u676ufo1_400.gif",
            "https://64.media.tumblr.com/a45d63901ca97a623145d2e5adc3894d/1f6cad928b737662-13/s540x810/3cae35fbc49c95539a663aee0c456fe3cb51b8e7.gif",
            "https://64.media.tumblr.com/cb8ddf0bc44cb4eeb01e438113264d50/tumblr_phmmi77nUC1tc8b5go2_r1_540.gif",
            "https://64.media.tumblr.com/fd27cd113adddcd86d5b54d956fe5975/0d8559b6074d5bd5-73/s540x810/502cd3834153cbe50b146e418e1abc95e5e3b117.gif",
            "https://64.media.tumblr.com/7b9d2c95b2585adca2ed6e661285a46b/5635be10542d6ed9-50/s540x810/d14e5fe5b6edbd2d9f72100b42509caa616fae67.gif",
            "https://64.media.tumblr.com/68c6007ca144e2687cba1406e9609482/4b28710d5c64949f-ee/s540x810/3375215c9750542c8e41cf5be0707535370fc38b.gif",
            "https://64.media.tumblr.com/7fbbac46de6dd4ce9019fd31de202141/tumblr_p3r29tJ0S71whwf5vo1_540.gif",
            "https://64.media.tumblr.com/32026c01d43ccc9e5bfee97d23db6d8c/e9d723ca1fc7b8fd-be/s540x810/62fd5f64c46ddc0ab24d34833d0f3b0f7f07c186.gif",
            "https://64.media.tumblr.com/820c035b3c45dc95cb8e909482c6750a/tumblr_px8l1eNSSF1v1vsi5o1_540.gif",
            "https://64.media.tumblr.com/89c0c496488fd935b1051bfa9c94631f/1818c5e4cbd91a12-c2/s540x810/a4e214161104e34fea2d9bd165d9013c0f8ca119.gif",
            "https://64.media.tumblr.com/5fb78dc223ed043ca441c70686d2ab81/tumblr_p1wlx2Ep4y1whwf5vo1_500.gif",
            "https://64.media.tumblr.com/3ea00548c2d0795f6bd63be0eb2564e3/tumblr_pywh2sPd461ub8hyjo2_540.gif",
            "https://64.media.tumblr.com/a8ebb79400d00a9a9ae276842073ce46/tumblr_p4o59iYLZU1u6jyp2o1_400.gif",
            "https://64.media.tumblr.com/119824cdb628c2911c9283992d646487/tumblr_piwi4yHQfO1qdr4a5o1_540.gif",
            "https://64.media.tumblr.com/9343c97eea0fef4508d023ad220fd44e/4ed33310b98cb311-d4/s540x810/80b02b5097eb981d1e768732fb0adf7ec1ee641f.gif"]

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
            "https://cdn.discordapp.com/attachments/802261156571774976/802262256545038376/image2.gif",
            "https://64.media.tumblr.com/573935fd54028aa81c12651ca137f25d/tumblr_peubm08hu11w15kmho1_540.gif",
            "https://64.media.tumblr.com/1da00fe7fe0d7eae717a533e9e4f1240/tumblr_paqregEEAN1ws9xlgo2_540.gif",
            "https://64.media.tumblr.com/14a3d19d748a02fad1f084fb6b9d9b43/tumblr_p54nr5RSYt1tbd5x7o1_540.gif",
            "https://64.media.tumblr.com/3429bf99a724f95e2f46d81615b7a97d/tumblr_p98mp2zffx1wyj9zbo1_540.gif",
            "https://64.media.tumblr.com/0651d13c2c0b8416abcbd868081f7028/tumblr_pauq2pSqD71xrc7meo1_540.gif",
            "https://64.media.tumblr.com/0cfa258148570d43e03e8635eaf03373/8dd4dbedf932166e-35/s540x810/272454ae0676497cde56085f9cef5ad624dc3575.gif",
            "https://64.media.tumblr.com/a75486d39cdd023ecbcce48d2094d5ec/tumblr_pu5wubjmPt1tbd5x7o2_540.gif",
            "https://64.media.tumblr.com/c623b06bcf96f713386a51de204291cc/5da2ea4682de9a20-3e/s540x810/3514d29855b4a31b73de3059360ce75cee3f48e8.gif",
            "https://64.media.tumblr.com/b4ec1f800a192a837a10c9f974222667/tumblr_parp5zhsQS1qe8wvfo1_r1_540.gif",
            "https://64.media.tumblr.com/fc8700ef163cd795501bf875a9f5b936/tumblr_p8q4ubU6fw1r6mvzao1_540.gif",
            "https://64.media.tumblr.com/b9c20d1d8af4005d2a806d399f5eda5c/tumblr_p71r7liZK21wh0enxo1_500.gif",
            "https://64.media.tumblr.com/d26ed84599af169b8168f8f1e053cc05/72c78a62afc3c570-ff/s540x810/b7ad92aa19a996ed8837841c58a3f9ed9a92e2a1.gif",
            "https://64.media.tumblr.com/6026bbd1521ccca48ab07736e8d2c746/tumblr_p478ehIS2P1tc8b5go1_540.gif",
            "https://64.media.tumblr.com/14959b9d7e62f8cbfc92d67e3bf98169/60582a615f3ab05d-f1/s540x810/8c18d4cba2ec868c36ef082153dc97bacc0fb3ad.gif",
            "https://64.media.tumblr.com/50f1e60ca97cc159dc7f00fb2cd57b2f/tumblr_p8xdfc0HnW1ub8hyjo2_540.gif",
            "https://64.media.tumblr.com/d4be14309e9befb15090f5062db5c9e3/8fe318d8d3623db2-7e/s540x810/da3a809b5c4f760aecfeeaf9b519ef5db133db93.gif",
            "https://64.media.tumblr.com/d98e05208eab36071c57225ec1eee8ca/4d48a1ed9b8b993f-97/s540x810/f3bf9f87dc5d61900d996ab3ca47d13e9813cb96.gif",
            "https://64.media.tumblr.com/2b755086b188dc84502ab0c860633331/tumblr_pon2fz58WV1vp2fqjo1_r1_540.gif",
            "https://64.media.tumblr.com/67718a6d0fde6862ec6f1a93c97ebaa2/tumblr_ppp94mScJb1rbs18co1_540.gif",
            "https://64.media.tumblr.com/9751ca383b85f2ae95645378e2926b04/64d5a23ed3a11792-98/s540x810/08d2632e406b41650043d8ff036e043c81b01751.gif",
            "https://64.media.tumblr.com/028725590e2c9d9fc9121232e306d0ef/tumblr_pjo5k6z3oj1xhs2z6o1_640.gif",
            "https://64.media.tumblr.com/473ca5f45544b6aaecb27ba1169fb601/c5dbefa69553614a-b3/s540x810/ec1e1876db7a08e335e1117a993473aa6d01ef95.gif"]

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
            "https://cdn.discordapp.com/attachments/802261179409104896/804516918476013578/f217981b-880a-4327-bace-b8356719faa2.gif",
            "https://64.media.tumblr.com/10ad495640131cd128bd0e08eca588db/08368596fc8cd542-d5/s540x810/1a14e500666bcb5f25618cc49272fe77099da6c3.gif",
            "https://64.media.tumblr.com/47f9dea8806ba0cb6d896dd2a7c9dac8/7a1a2e04e7f3d833-51/s400x600/c410ceedd29212f3f99fb74d7a182bdfd08e8737.gif",
            "https://64.media.tumblr.com/4a1e3ce53c4bbb7a2a728650de10bfde/fb9c36ba6ceeae2a-bd/s400x600/b3c9aaa03a3d1e9bd192531edb08deb9152c5179.gif",
            "https://64.media.tumblr.com/ced5085643a7cc6f8031e169d6c2dc53/39b7ffc06635c335-99/s540x810/1f0c89b052f9d9ea200e5deed178841f8411e850.gif",
            "https://64.media.tumblr.com/55835ef646e5d46e06a5eedb967ef0e2/39b7ffc06635c335-ed/s540x810/15385fa8b7386e73788b5715e85853f01c274ac7.gif",
            "https://64.media.tumblr.com/ba11b2f7a58b59bcdd0aec3f7cc30400/fe2e602575910010-a0/s400x600/1da257d4144f6df2cc196722a6129b1596b9a970.gif",
            "https://64.media.tumblr.com/ee3ae1b6e55532ca1036b65cd7896449/972a6f719c48f15a-9c/s400x600/b774195981f9b50e799cc2fd711bc261a9a8dbc4.gif",
            "https://64.media.tumblr.com/4669b41f2cc33e89916c14cb5c092adc/05a96815b51efb65-65/s250x400/523e66200fb0b22292cb29871519b5178be00686.gif",
            "https://64.media.tumblr.com/75a49d7034ed2ee80dfed7fc48026414/cfc0751a21756c75-d5/s540x810/a39cbca597ba7c5e80cd6acff4deb9e083506f56.gif",
            "https://i.pinimg.com/originals/3b/a2/6d/3ba26d418d53f653b04f1986fdb9dd0b.gif",
            "https://data.whicdn.com/images/338204049/original.gif",
            "https://64.media.tumblr.com/5b5345d82f74053698cfbf4b73f7e493/a951f8524ce2887a-ff/s540x810/fba11b885d4e108390a18022761f0e60e2f570eb.gif",
            "https://64.media.tumblr.com/0a667f19a96273856ae7c75795e79f64/6ef4daff3dc864ab-4d/s540x810/28a83acb24782736bdbd6543e00f78681f30cd0c.gif",
            "https://64.media.tumblr.com/8f98542c1536e29d5c7b049e760dfda7/83808592136226f3-47/s540x810/57791966ab8536ddc87e20de5eb7e2286cccbfd5.gif",
            "https://64.media.tumblr.com/b54771312ba9bd8cd89b551ebf55ecd0/1eb0ffc8be16e217-3e/s400x600/828f0e562d82846839286c44bee02fc9add70fde.gif",
            "https://64.media.tumblr.com/0e6a233639173360a02d3953f9ea7a02/613bc76ddc617381-d0/s540x810/f8095b9cf9a143b9e93f473975d3280d581a8d42.gif",
            "https://64.media.tumblr.com/8c45870e1d5eb6b4d29e7e1c9c67acb0/acf81bfd61d12a1a-c1/s540x810/20cc577b78112f0b47679865a2396b3a20e4c472.gif",
            "https://64.media.tumblr.com/7f30de541ce5bf5d4b0c044a28cbcb18/tumblr_inline_p2fd4fxUAm1uip2hn_540.gif",
            "https://data.whicdn.com/images/324424436/original.gif"]

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
            "https://cdn.discordapp.com/attachments/802261212846882826/804208430440906763/jktfma20_4.gif",
            "https://cdn.discordapp.com/attachments/802261212846882826/806236242458050560/02014.gif",
            "https://tenor.com/view/jungkook-bts-jungkook-blond-hair-jungkook2021-jungkook-gda2021-gif-19910003",
            "https://tenor.com/view/bts-jungkook-kookie-blonde-suit-gif-19977768",
            "https://tenor.com/view/bts-jungkook-suit-blonde-blonde-jungkook-gif-19915179",
            "https://gfycat.com/daringdefiantbass",
            "https://gfycat.com/chubbyredflyingfish",
            "https://gfycat.com/immediatelazyattwatersprairiechicken",
            "https://gfycat.com/aggressiveadorablebudgie",
            "https://gfycat.com/flimsydazzlingheifer",
            "https://64.media.tumblr.com/4734914580e63447469c06193cafb584/tumblr_p9qqaoS2qP1qagqqso1_540.gif",
            "https://64.media.tumblr.com/53052595666be5570850566630255f6a/tumblr_pdrl0956MR1whlmf0o2_r1_500.gif",
            "https://64.media.tumblr.com/fc13f96c73beb89df8f6eba5b45a33b0/tumblr_pbsx3nqO5I1whlmf0o1_r1_400.gif",
            "https://64.media.tumblr.com/a7dfae2a62d97f59269b5aab1c50762d/tumblr_pq4jo2msGy1uwrgdlo1_540.gif",
            "https://64.media.tumblr.com/9deb82bf51253ddf10c227f659b57842/b4b75987b78370df-59/s540x810/75cc6eb3c3e4494ed7425762dd53ed69a0df294f.gif",
            "https://64.media.tumblr.com/7fa3f85ae94aa3bc6a27a0d6e22ec3ea/35ac364575296589-dc/s540x810/039d34f647ddc2f59615c6c294df6b3645e6ebf6.gif",
            "https://64.media.tumblr.com/68aedb907bed5128563c7ddc6a02b9a9/13230845a8a88e55-ef/s540x810/e93e8251d551ac44444075e884d187bd53829cd5.gif",
            "https://64.media.tumblr.com/5f9816308d8d271a7ead0c77b1988062/4bc9acfa88c9c3ab-79/s540x810/25a0f8a5a8323aa3043f8ae88df6fd815c28a1a6.gif",
            "https://64.media.tumblr.com/ad9a761b5a5c78bd2c1f48b5ed4891c2/0347cb026a9b4dbc-04/s540x810/a947651bfc3b64b205a8343d943a603be4257863.gif",
            "https://64.media.tumblr.com/4b6ef5460da3ca5d866178c3e0b292bf/tumblr_puw8vi2Xiy1xm38xzo1_540.gif",
            "https://64.media.tumblr.com/e2f9d776bed161624f1a0fd201d51a06/07133c9333e322b9-2f/s540x810/1a02bf46e839d4f5b656fbaedba15503084894a2.gif",
            "https://64.media.tumblr.com/c8e1793b410239a76bbd1a3801fea081/be93406a59b29084-6b/s540x810/4e9298143a6cf98d9d16b522fe4a796855992480.gif",
            "https://64.media.tumblr.com/6ce81b177b569483bcc10bb4f3026360/tumblr_ph6tbiWqKw1x3f5gao1_540.gif",
            "https://64.media.tumblr.com/249608e9a3b8c4d92ee9a6ea7eea2c9e/tumblr_pq46nfJlt11us7sgvo1_540.gif",
            "https://64.media.tumblr.com/ac9d91807bf987f22cc00e8f37607934/tumblr_pw34rzSB781ub8hyjo2_540.gif",
            "https://64.media.tumblr.com/78b9a2d673cdb8da84d6bc69c76c1696/2380afb7f0f90573-7d/s500x750/5b2bdd30f3c0f34d98a18bd0b62de6976fd4e57e.gif",
            "https://i.pinimg.com/originals/25/fc/28/25fc28218a1e65ab2abba0779f3dde0b.gif",
            "https://media1.tenor.com/images/1886e9365c41b28a7c392a4bad6f617f/tenor.gif?itemid=14858820",
            "https://64.media.tumblr.com/f5404d1d33b6ad81dd569f2a2d47af87/df89c8eb6c8e526d-7b/s500x750/3b64fdef9a66c387b67d3928f038af8a22f5d78d.gif",
            "https://data.whicdn.com/images/336751984/original.gif",
            "https://media1.giphy.com/media/12x70SAod4GvC/giphy.gif",
            "https://i.pinimg.com/originals/e3/7f/06/e37f061c576f27766c91b11600de4b7b.gif",
            "https://data.whicdn.com/images/352878015/original.gif",
            "https://data.whicdn.com/images/352882854/original.gif",
            "https://pa1.narvii.com/6372/b26f770c2717bbe502b7d3f56aeb23dc9fda9a94_hq.gif",
            "https://tenor.com/view/jungkook-eat-jungkook-chew-jungkook-jeon-jungkook-jungkook-cute-gif-20020604",
            "https://tenor.com/view/jungkook-kookie-kpop-bts-bangtan-boys-gif-18817421",
            "https://64.media.tumblr.com/647e55dd3376ec882737d2a17f7770c3/c46644d74b01d397-e6/s400x600/69ba3a07478578db0e6830ab55afcc4213a9fd21.gif",
            "https://64.media.tumblr.com/4ae11f41afbd5ad242366b23d04e7668/7c3a71662f962ab4-3c/s540x810/fd299d705db60ec776441ab5f9c82074d411faed.gif",
            "https://64.media.tumblr.com/c7a46e55861d68b85ce31c0e9046f792/1d0fce4a5b31fac8-f4/s400x600/c2421ccdba965a42405949e8b516c1c83ccafbb5.gif",
            "https://64.media.tumblr.com/aac1ad1dbb48e65452b3b07457e746a3/c40b71b71857ce8c-36/s540x810/a1cf2cd865b7d640a5d3b270c9a302124c1b1adc.gif",
            "https://64.media.tumblr.com/46190774616f16d9f8fb6386ae6e3269/2380afb7f0f90573-61/s640x960/6ef909c62a707628251402bf997d8be122b2c5a1.gif",
            "https://64.media.tumblr.com/131b6265e49701c67a895ad6f4a521ae/d059989d2f60b0ba-c5/s540x810/4fae0a8dc5838445c1fd2aef145347931d38afa5.gif",
            "https://64.media.tumblr.com/575c1419ea4e0a42d7d6578c80534a79/1c2ee168832e7dd4-21/s250x400/c13ae1b9607effdba198b593716dc322bec7ab2b.gif",
            "https://64.media.tumblr.com/79169cbfa20cd05fb2c970bc16451b25/d358ccc5f0bb6329-73/s540x810/b210d61bf6cf4abf8ce4ba5b7972b78c6881bd08.gif",
            "https://64.media.tumblr.com/e93a552ab20a48821eb3ae9fbcd0a8d2/d358ccc5f0bb6329-65/s540x810/54057a364fc64a85fa882f28a70bde474b2b5bc8.gif",
            "https://64.media.tumblr.com/2427817ab338258c06354abb497d2bab/6d7cfb9403b0e690-bb/s540x810/e05ef82229139ea0aca0eb7516053c874e66db70.gif",
            "https://64.media.tumblr.com/5517f4fb1016a9614ad17ba385d41769/9cf39987c089e2a0-d9/s250x400/9d5f2bc3187a3a4338e4c78bbfaf859da765d405.gif",
            "https://64.media.tumblr.com/949c54d12492a4d4c24b9b039c256dc2/tumblr_px4w6y2B391xjlnrvo2_540.gif",
            "https://64.media.tumblr.com/1b29144f7fa0c8ce68c764c1035ca705/tumblr_px7kf5XZU01vmvwc7o2_400.gif",
            "https://64.media.tumblr.com/462bcd2471eae045132e4dd3c02035ad/tumblr_pv3qo5NJfg1yo6elfo3_640.gif",
            "https://64.media.tumblr.com/80a2cca7779347becce46853da58a7b5/tumblr_puck4p8bqW1xjlnrvo2_540.gif",
            "https://64.media.tumblr.com/5b22ae14ae721541414083b2062b0786/tumblr_p8xqdhWyFf1wq9bfzo1_540.gif",
            "https://64.media.tumblr.com/0497958a18494569b8902425d885e932/tumblr_psxsd9kE3w1ru9tmso1_540.gif",
            "https://64.media.tumblr.com/2169a11d0e58834e7849e1db9370dab0/883385de219ffd5a-56/s540x810/47d48e2845dac091b3aa5587520874dc42fb28a2.gif",
            "https://64.media.tumblr.com/bbb286a0124f69eaba45ffd2e9cfdffe/a0d1b4bb40f22aae-47/s540x810/31d7e8c725a9161a7eddd56ead20afbdefe343d1.gif",
            "https://64.media.tumblr.com/4b9f2ac139673e4adab1565e5c395c58/tumblr_pw3lplIVlR1vp7ks6o1_400.gif"]

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
            "https://cdn.discordapp.com/attachments/802261241128419348/804515701653897288/191027_SYS_.gif",
            "https://64.media.tumblr.com/84bdfa41f7ecc60dee20f93a372a8fdb/tumblr_pxtj0eMRyD1qehiaao1_540.gif",
            "https://64.media.tumblr.com/9cb49391fd1426aeb738c71ae19fba98/tumblr_pup6bl33wU1qehiaao1_540.gif",
            "https://64.media.tumblr.com/5c536bd1fe7ff32c679f107c4c63f80e/tumblr_p84bqyzpX81vozc1eo1_540.gif",
            "https://64.media.tumblr.com/6582907f6f7f36c5b4a527a8b364e911/4ab967a543f1be89-23/s540x810/546c9a8a354e6af293439673750268803cb111de.gif",
            "https://64.media.tumblr.com/a360aa1bba0868ae111b321a63052f19/tumblr_psj2q5vr3n1qehiaao1_r1_400.gif",
            "https://64.media.tumblr.com/fb47f261307397313dfc92771c075665/f4e967692750c869-d2/s540x810/436f5419c393b24e3b7ad72bb7be0783a6b70be8.gif",
            "https://64.media.tumblr.com/f86fd1902f32e1496304b4bcedcba6d6/tumblr_p671g44HsR1whlmf0o1_500.gif",
            "https://64.media.tumblr.com/53fdf99b7922bc227100c24bd3f34bac/tumblr_pup3wpr8Bv1qehiaao1_r1_540.gif",
            "https://64.media.tumblr.com/09e8523c16f8640c425ad072f6cef7b2/eaaaf46db1de916b-79/s540x810/47d27f942215667f0ce161da98ee0b5bde34bee0.gif",
            "https://64.media.tumblr.com/2c761b7d1fc4cdc753e674f0bcd5d875/tumblr_ptnvd8iiUh1qdyg4co1_540.gif",
            "https://64.media.tumblr.com/907e0a93e4b723708efbc45c0e54a470/tumblr_pumgeyHqq31vozc1eo1_540.gif",
            "https://64.media.tumblr.com/856aa198450a929eefe6de3839c32d06/80bfec0fc7a6d740-c4/s540x810/67543732abdb55b1a7541869726f0a82da54badf.gif",
            "https://64.media.tumblr.com/a93abe4b281a2c63da81195ebcb9be87/2c3dc15a38107310-69/s540x810/68f61c46b4dd5ca90c718e117f89255b172a67be.gif",
            "https://64.media.tumblr.com/d6bb7d2c962f2a95d61c59a5a7cc361e/b5e20cd61c5aee4e-87/s540x810/2898c4ce6a2fe7b62543927efd64713e5943cad2.gif",
            "https://64.media.tumblr.com/e136a2b3e6382cad0f688b519e729e83/f4e37d8c6b08f2ba-12/s540x810/66320ef6c7ddefdb0e3a66f08a07de6f37b6fc69.gif",
            "https://64.media.tumblr.com/3c956df3af8ab0d127a3137172284a55/tumblr_ps83dnR25R1rbs18co1_540.gif",
            "https://64.media.tumblr.com/bcef216b8ce4596e636e82dcf3fab558/tumblr_p83zaxxwOl1wuxr5oo1_540.gif",
            "https://64.media.tumblr.com/1829f870b85716e68801ea004ef830ad/f5d9eb467b85a6c9-5d/s540x810/7c19958ca24ae4bdc4cdae35392b9bc4d5bf06e0.gif",
            "https://64.media.tumblr.com/70b3204f059a4cd86690c3ca7c6354ef/cf8df6a5ed3bc9fe-fa/s540x810/b9caac310d078d4475b70afb44a4a3e7ea44f4fd.gif",
            "https://64.media.tumblr.com/d2cda4a19dfd95f29b1f98378933c22f/adff4bbd87793e46-4d/s540x810/27e2337623f80495e94c1f3a8d5b3cac30a7ffb7.gif",
            "https://64.media.tumblr.com/78e9797c2b4886b427db29b83925b963/tumblr_p6w6e590OV1wjkazmo2_r1_540.gif",
            "https://64.media.tumblr.com/d448dd1730f2e5a8956613ce4f60dff8/tumblr_p9oobuibAK1qehiaao2_r2_540.gif",
            "https://64.media.tumblr.com/47ae285b682f4e63e8d53cb114ab7050/be8d9d30781b5cc5-53/s540x810/86f40c9c845a804654a0c7358b3d1b105fe366c4.gif",
            "https://64.media.tumblr.com/64bd8395a63e1c04c5168ff69927337b/b4fe8a888f31756f-31/s540x810/08a8a95afc7c5b5fcac6cd6468f8c8e2077cee50.gif",
            "https://64.media.tumblr.com/164d90ab9d6f6dc6a8d7f24a39271505/33dc4eb3970ec962-32/s540x810/8a5d0b4e18bfff61bdfbc566bf9ed3e0d959fc35.gif",
            "https://64.media.tumblr.com/ff5a974c9ef454ef905e5f8fc05a2993/tumblr_pv27lxrnn51y1mmkno1_540.gif"]

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
            "https://cdn.discordapp.com/attachments/802261268165689365/802264597749956648/image4.gif",
            "https://64.media.tumblr.com/c272d6b78d0ff56853ba7eac888ab516/tumblr_ptem837dGO1w15kmho1_540.gif",
            "https://64.media.tumblr.com/cfe421660e676a08ebae4da425618384/tumblr_pufbwznuqo1x5679go2_540.gif",
            "https://64.media.tumblr.com/92b715be56969e766385fce03f71c1ab/tumblr_p6py2y8Wfo1vuwqjbo1_540.gif",
            "https://64.media.tumblr.com/0c55973f94ede7943e880793cfcf620e/tumblr_p9zfaw7C751wpcmcoo1_500.gif",
            "https://64.media.tumblr.com/b188fcbe143621cb77ba6bf6327e9a9d/tumblr_ph6t2e4GH41ru9tmso2_r1_540.gif",
            "https://64.media.tumblr.com/de13d76504c1016bd2ff86038184f3c5/tumblr_p7lkytF45D1vgc7hvo1_540.gif",
            "https://64.media.tumblr.com/22ae80d86a9f2ab482569ed779da7daa/86ea2f4ea4f342a7-a4/s540x810/bad02aa11f2a649d6a8df7ce6abaa1080240d498.gif",
            "https://64.media.tumblr.com/56bf7c696bd0a886a078c82421e14e04/tumblr_pqqaaemhbJ1rngqpbo1_540.gif",
            "https://64.media.tumblr.com/97774de74f5466a6e9f6305ef4c95768/tumblr_pn4op3lM4L1vxche8o2_r1_540.gif",
            "https://64.media.tumblr.com/f2682f013bd0ca867f9342bf0566b349/tumblr_p95u2kRnPV1wpcmcoo1_500.gif",
            "https://64.media.tumblr.com/1e5fa5a7012f66b75c50545489542d57/4cde8015d92be6ce-5f/s540x810/f23b07cf23796e1745438e4aa34d5e812b428b1e.gif",
            "https://64.media.tumblr.com/98df99d0d845e2ac48dbbcd0ad4f1619/tumblr_pxlmp4j9tz1s5te9uo1_540.gif",
            "https://64.media.tumblr.com/03dcfff8ce1371c318ec94d01238b312/tumblr_p7wno9oHb81qj2459o1_540.gif",
            "https://64.media.tumblr.com/f423072a0c2bd8f7a37df76f64a17a8d/tumblr_pqj9a3OgVl1xm38xzo1_540.gif",
            "https://64.media.tumblr.com/0c36a2a2b3f45f7f465543248720544c/8c38a3ab16a57766-9c/s540x810/ede8a95b0b642d6768c2d01a38613a1b466d4309.gif",
            "https://64.media.tumblr.com/8e55b137408d505e80d00dfae48a68a8/6f25ceb3636d23cb-9d/s540x810/4e476014049a40e5778a8bf47b4c82281af61b51.gif",
            "https://64.media.tumblr.com/731cd527f208b61ccb9ad3f4c3ddfda4/f24f53911c01f41f-66/s540x810/7c36d69a88b7487a7fac9c8c3d249a5ff85e51af.gif",
            "https://64.media.tumblr.com/a73c484faf7d5ab2c5d1a6d3a0a58ae8/9c05aebff38ce26b-d4/s540x810/c607328e769a26246693b2e5b10145ba18add7d1.gif",
            "https://64.media.tumblr.com/2e41199d9bc04db807f33f06163a6b66/tumblr_p4uclgL7SX1wah8boo1_400.gif",
            "https://64.media.tumblr.com/4a6ea7e7c59dc3ebb2463f38c12b446e/d912c0425cdfdd41-42/s540x810/65c3a6d75a8cb79cf7c7f3f68d4f2a5a461cca14.gif",
            "https://64.media.tumblr.com/f649e9e64a7c9c10c89b88d357c4be98/185a7c39317be954-5d/s540x810/03e4417ad76efe554fc9fa042bb6ccff80041d8f.gif",
            "https://64.media.tumblr.com/f7b7a00d62a000838dcefb9c093f0927/fdbed0b2637a9087-05/s540x810/25a6b22e3e437a096adc004e3fb4f88f3b97735d.gif",
            "https://64.media.tumblr.com/7aade933fc68c1ac65e1aa27d6e549bc/0b0dee2e26ed93fd-70/s540x810/e6a43bbfcbb1c196ae2dda88339aa9c78733737c.gif",
            "https://64.media.tumblr.com/292300fcead0966eef473b8025c06cc4/tumblr_pyfn40pqLv1whlmf0o1_500.gif",
            "https://64.media.tumblr.com/aa6257bc3c28075230caa944ff76ccf8/tumblr_pu2m110fwW1r99c4io1_540.gif",
            "https://64.media.tumblr.com/80fcfdec22bd93ba3e5a5fae81c10752/b3f11bf3bea64ca6-b1/s540x810/293ea1fb2da6ea9d89a9598e7888494fc6585c8e.gif",
            "https://64.media.tumblr.com/1a610482ed476e16a67eef42534d9806/tumblr_pkg8ljuBNN1wkdbt1o1_540.gif",
            "https://64.media.tumblr.com/cb339cfbf832681503e99d4940100f07/2d3bbc901d176af5-76/s540x810/a3a9c5b2a96ce3949b4aebd51c02dfb8a168d7f4.gif",
            "https://64.media.tumblr.com/5fbeadb9495c51c5486664a0628c410a/efe544124fe7d1c5-a3/s540x810/d3677a064678c3d8daab1a43c36599b3c7cb2613.gif",
            "https://64.media.tumblr.com/4ac5790361b9d17c83395e0f99d852c3/tumblr_p9ch9sAXX31wpcmcoo1_500.gif",
            "https://64.media.tumblr.com/d7c93f4cb47511a03c6fd11e36cef577/49428ec5f115e2c4-03/s540x810/264433ccde4f6655edcf2393e5d035e09837f7d5.gif",
            "https://64.media.tumblr.com/dce8c85daa3fd6817bd8e226f8d92be0/1fb6c573665ce64a-2a/s500x750/04efd260c90707ce459de39ff76bcfb1746140ba.gif",
            "https://64.media.tumblr.com/2554f4598922d25aadd6a1c9764cce2a/tumblr_plkv06s8ih1vxche8o1_540.gif",
            "https://64.media.tumblr.com/bbfbc69d2e86e5e5d4ac928f47feb396/e11865263da45290-4d/s540x810/5e2426d1cda6bec4f33363f30b53bf30443d5bd4.gif",
            "https://64.media.tumblr.com/38689479bba39e655217dca9e87b67cf/tumblr_paixxxsPz61wpcmcoo1_500.gif",
            "https://64.media.tumblr.com/e7c372fc42ecca8d3c64c39e619ec128/098bb4e2dd047846-ce/s540x810/bb30ebecd4b6310da47d37a1e74a1e0867b8c0e1.gif",
            "https://64.media.tumblr.com/1bf7a6a17b0ea94977e211dee9b880e4/tumblr_pa98cqm1U01wpcmcoo1_400.gif",
            "https://64.media.tumblr.com/4b2de9c20d2c9ed3f85711ad4c1214c0/tumblr_p1ubx5J8X51qj2459o7_250.gif",
            "https://64.media.tumblr.com/85a51cc1f5162789a615ac1201cc7e3f/tumblr_pow6sqhI4J1x62phvo3_400.gif"]

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
            "https://cdn.discordapp.com/attachments/802261293565607946/802265834864377886/image1.gif",
            "https://64.media.tumblr.com/6a9aa66285775d1183203f1a07597b60/f665725e063163d6-58/s540x810/e40bc36b5171a92ca283e1380cf4546be266130b.gif",
            "https://64.media.tumblr.com/9e1a3b6ee4fd1a2e6da06da589d1be9c/tumblr_p3vukfcIiD1vozc1eo1_540.gif",
            "https://64.media.tumblr.com/0a082471d2efe8ad17e2bab6f6f48514/tumblr_pntxcf4Dyf1rzcklqo1_540.gif",
            "https://64.media.tumblr.com/b88888e78ea44b946015bd8a06848a6b/tumblr_puroztwc2T1tc8b5go2_r1_540.gif",
            "https://64.media.tumblr.com/0d6796fe1d219d3aeb0afd639b2874ff/381ab6ddb731ea72-0d/s540x810/b80b330ac2bd84fb39f784fbc8de4887a96cf45e.gif",
            "https://64.media.tumblr.com/aaac1c68e9a1e4e9fec6b0dd9f941aa6/f8ffd08825714bc4-f0/s540x810/47daf3b2f590e987e651e7ef19d8e1b4a8f57467.gif",
            "https://64.media.tumblr.com/469d4c985b726b7832f39d715a57da08/4b6a75c175091c81-5d/s540x810/26300f6efd2581f48aedbd17284cc846c6a85edc.gif",
            "https://64.media.tumblr.com/9605b23db8afc8c5700281a1885965e1/tumblr_pvnfdrcKIq1ub8hyjo2_540.gif",
            "https://64.media.tumblr.com/3039a39c625792823727d01b960d529d/62cbd2dfb32d37dd-96/s540x810/634ae36705769282d912b61595771cafebc70751.gif",
            "https://64.media.tumblr.com/baeb5a40dc18a88f6c45311b9dbecf0b/6e0debbf81196521-33/s540x810/0c9756e75031830e6d97b0c204c69973d6926520.gif",
            "https://64.media.tumblr.com/37055e04bd1cc1a2a20f9e690e11da4f/f9186fa1fd50cfb9-02/s540x810/314191b7726f5095764ceca266b9fde560b74ac8.gif",
            "https://64.media.tumblr.com/19832d81bd3a80223bc37ca78903aa64/tumblr_pjvl1tchua1rzcklqo1_540.gif",
            "https://64.media.tumblr.com/704def8f35eed5ccbde52f3e249ac6e2/55ea1480f09bb0f8-e8/s540x810/07e99daa97486ea04d5f02908602a33d541f9e01.gif",
            "https://64.media.tumblr.com/3b19ffd00bf00a61b347ea277dcd76da/tumblr_pggcu1uOGi1w15kmho1_540.gif",
            "https://64.media.tumblr.com/898c3c0328c2f8faf72109fa1e5b51bb/858016a7ea9c9127-40/s540x810/7d17f4865c06f259de971b98e4c39157a96465f8.gif"]

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

    # @commands.command()
    # async def v(self, ctx):
    #     if ctx.guild.id == luminary:
    #         if ctx.channel.id == kbotcom:
    #             await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about V :heart:')
    #             await ctx.send(random.choice(self.bot.v_gif))
    #             await ctx.message.delete()
    #         else:
    #             await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
    #             await ctx.message.delete()
    #     else:
    #         await ctx.send(f'<@!{ctx.author.id}> is talking about V :heart:')
    #         await ctx.send(random.choice(self.bot.v_gif))
    #         await ctx.message.delete()

    # @commands.command()
    # async def suga(self, ctx):
    #     if ctx.guild.id == luminary:
    #         if ctx.channel.id == kbotcom:
    #             await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Suga :heart:')
    #             await ctx.send(random.choice(self.bot.suga_gif))
    #             await ctx.message.delete()
    #         else:
    #             await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
    #             await ctx.message.delete()
    #     else:
    #         await ctx.send(f'<@!{ctx.author.id}> is talking about Suga :heart:')
    #         await ctx.send(random.choice(self.bot.suga_gif))
    #         await ctx.message.delete()

    # @commands.command(aliases = ['j-hope'])
    # async def jhope(self, ctx):
    #     if ctx.guild.id == luminary:
    #         if ctx.channel.id == kbotcom:
    #             await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about J-Hope :heart:')
    #             await ctx.send(random.choice(self.bot.jhope_gif))
    #             await ctx.message.delete()
    #         else:
    #             await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
    #             await ctx.message.delete()
    #     else:
    #         await ctx.send(f'<@!{ctx.author.id}> is talking about J-Hope :heart:')
    #         await ctx.send(random.choice(self.bot.jhope_gif))
    #         await ctx.message.delete()

    # @commands.command(aliases = ["k8"])
    # async def jungkook(self, ctx):
    #     if ctx.guild.id == luminary:
    #         if ctx.channel.id == kbotcom:
    #             await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@{k8}>, <@!{ctx.author.id}> is talking about Jungkook :heart:')
    #             await ctx.send(random.choice(self.bot.jungkook_gif))
    #             await ctx.message.delete()
    #         else:
    #             await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
    #             await ctx.message.delete()
    #     else:
    #         await ctx.send(f'<@!{ctx.author.id}> is talking about Jungkook :heart:')
    #         await ctx.send(random.choice(self.bot.jungkook_gif))
    #         await ctx.message.delete()

    # @commands.command()
    # async def jin(self, ctx):
    #     if ctx.guild.id == luminary:
    #         if ctx.channel.id == kbotcom:
    #             await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jin :heart:')
    #             await ctx.send(random.choice(self.bot.btsjin_gif))
    #             await ctx.message.delete()
    #         else:
    #             await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
    #             await ctx.message.delete()
    #     else:
    #         await ctx.send(f'<@!{ctx.author.id}> is talking about Jin :heart:')
    #         await ctx.send(random.choice(self.bot.btsjin_gif))
    #         await ctx.message.delete()

    # @commands.command()
    # async def jimin(self, ctx):
    #     if ctx.guild.id == luminary:
    #         if ctx.channel.id == kbotcom:
    #             await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about Jimin :heart:')
    #             await ctx.send(random.choice(self.bot.jimin_gif))
    #             await ctx.message.delete()
    #         else:
    #             await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
    #             await ctx.message.delete()
    #     else:
    #         await ctx.send(f'<@!{ctx.author.id}> is talking about Jimin :heart:')
    #         await ctx.send(random.choice(self.bot.jimin_gif))
    #         await ctx.message.delete()

    # @commands.command(aliases = ['namjoon'])
    # async def rm(self, ctx):
    #     if ctx.guild.id == luminary:
    #         if ctx.channel.id == kbotcom:
    #             await ctx.send(f'<@{lulu}>, <@{princessuwu}>, <@!{ctx.author.id}> is talking about RM :heart:')
    #             await ctx.send(random.choice(self.bot.rm_gif))
    #             await ctx.message.delete()
    #         else:
    #             await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
    #             await ctx.message.delete()
    #     else:
    #         await ctx.send(f'<@!{ctx.author.id}> is talking about RM :heart:')
    #         await ctx.send(random.choice(self.bot.rm_gif))
    #         await ctx.message.delete()

def setup(client):
    client.add_cog(BTSPings(client))