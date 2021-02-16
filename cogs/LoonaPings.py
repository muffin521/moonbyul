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
            "https://gfycat.com/soggyaccomplishedcolt-heejin-loona",
            "https://64.media.tumblr.com/5b1d89794f8fb7ec157a967fc57dae4c/11df3289bef670cf-3f/s540x810/7eb817fe3e857dc48634a690475de968e831d06e.gif",
            "https://64.media.tumblr.com/046a1772c940e5bbf72824deef9c36dd/tumblr_pdod1hFf5T1xz3wjso1_540.gif",
            "https://64.media.tumblr.com/0158edb212e4ca85f7b4c671860d6869/tumblr_pdr9lcavsM1xngi2eo1_540.gif",
            "https://64.media.tumblr.com/d4904439859bc45ac47bdd2a7255e465/0577459ed623d016-fb/s540x810/7870be5313748ec92675a5e79bc3e9271cbe664d.gif",
            "https://64.media.tumblr.com/f76927b476c0d97d03d4f60fd750fa43/2e98ba8ffb94100c-23/s400x600/a15226cc8f81e73337c555d9acf7688b7321a212.gif",
            "https://64.media.tumblr.com/547bb27636e57fa4057368189c85af02/27611b10d43dbd8f-12/s400x600/b042b7909c92a2a9a28e3b7a378c4ea20da9db13.gif",
            "https://64.media.tumblr.com/e1535ba7b5b8631bf72bf7f3e25a10ca/105d0645ae2a0bb2-15/s400x600/1c4686be69913c4c6595c9b27709728cd8bb4f20.gif",
            "https://64.media.tumblr.com/2044c4f724040780eda9354f26f7ea04/fc6944cce51c7c82-9b/s540x810/b5df49cc047d05191a7b14b159c76f8791e3294a.gif",
            "https://64.media.tumblr.com/3488630ff8f3816fdcee33be4e7d89b1/ff63d88461f57257-c9/s540x810/372fe45a40d5af7821f8b1029e8d938f11e3ed61.gif",
            "https://64.media.tumblr.com/2929dd210b94c1537d03aa891df44b31/5095f52731a2d3f0-e1/s400x600/4d3fd1c31db4c192a28d42d7cf9f25f6c4fc56a5.gif",
            "https://64.media.tumblr.com/0d8472e64dd5b7a97ae1a0d0523fa14a/5095f52731a2d3f0-d3/s400x600/96f05e9380c840461bbe8163b3035a3ee21dff1f.gif",
            "https://64.media.tumblr.com/f53738e0347fc9586f9712a205242850/5237caba0cec15c3-d0/s400x600/f26a2bac8a070bc97849adc6f93bf1bc09c2fef8.gif",
            "https://64.media.tumblr.com/55eff04bae07e29e533ffc17a2db65aa/acdf81e3f6b7d3d1-06/s400x600/5d95bb4ff970eb52a98ff21ccdb0eb7980e736bc.gif",
            "https://64.media.tumblr.com/91a9fd177f77d21906bfe7d310f19274/5e9024c89d22320d-cd/s540x810/ecf7dc7b01f425793a191e26395614633acef7de.gif",
            "https://64.media.tumblr.com/f02b162f52177097eb835f2ddbc02f76/2483c77e685659ba-6c/s540x810/b0e4f2e3955303d7ad4315422ad58fc3f24d522f.gif",
            "https://64.media.tumblr.com/241adc6e663a079d1bbb26cfcf1cd275/1329d2f9beca87c0-c0/s540x810/05abd5d1d027f32d7afac83ac523f18dc0736066.gif",
            "https://64.media.tumblr.com/2454608300c2cd211b02b5909df6f8a5/428d8ff68f592c75-7a/s400x600/22c2ddbf124487c0f6bda13a07fb8dc839452581.gif",
            "https://64.media.tumblr.com/1b37b6cfbe78f6fb5d15af49864299ad/b640b9402298518b-a3/s400x600/47df100d775326fc4ef0e28e6a3dbc9ebdd70d9a.gif",
            "https://64.media.tumblr.com/60f2f24cedf0680bc40b7131023721f6/b640b9402298518b-57/s400x600/67562c1793fc39acd943c24ce8bd60da0add06d2.gif",
            "https://64.media.tumblr.com/59bdba8c948e5f76f186e9d577c73668/5e9024c89d22320d-93/s540x810/f534551dae366ce5ec3375c5de112e0f91c8c587.gif"]

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
            "https://gfycat.com/cleananchoredgnatcatcher-hyunjin-loona",
            "https://64.media.tumblr.com/69e22bd1d15d487af0752bfba526eedc/341420aeb915599c-3a/s540x810/93752c932a9192d30cb4f59b1829c3361e916bb3.gif",
            "https://64.media.tumblr.com/27bda61c24e26d6b2b1f5c3deeebc8df/65ce3267c53bcd4d-35/s250x400/19cb1a71e415ffdfda61242e7f07198aae3600cc.gif",
            "https://64.media.tumblr.com/ebcbbd11d67f693ef59aad3a27c4dadf/27611b10d43dbd8f-2a/s400x600/cb024e4acc987aa8929e2651e675438127982136.gif",
            "https://64.media.tumblr.com/891e3d0f9657a59bc566ecc3171b6ec6/63941da99f0e36bc-e3/s540x810/cb8d6784f2be9d5f23abc4e3cb1ca446babf40d3.gif",
            "https://64.media.tumblr.com/f9498e2feec6934b2ba3acad668a4e8e/fe36d7066e14c251-cd/s400x600/df2ddee6c955a7cf58502a5d3eee01f3440115f8.gif",
            "https://64.media.tumblr.com/84c76b21c9a93a7455fbfa24535a9867/tumblr_pr5vxzmABP1w9jyl4o7_r1_540.gif",
            "https://64.media.tumblr.com/df50419f63c737a26677aa61b302c59c/00307bd16b155c11-66/s400x600/7a2be0ced07dffc8eb57aff20717f84336be8237.gif",
            "https://64.media.tumblr.com/63cdcc85eef5d58f5a80f2aec90290b5/85d84d596561cb73-89/s400x600/98dd8a7079b7b62e58cff42a8c8aa93ecb56dc8d.gif",
            "https://64.media.tumblr.com/6453d54dc3b93aca181b3e2425eb18c9/85d84d596561cb73-74/s400x600/cb53734a68a3dc4324dedb3d35f7bcd7c58b72e0.gif",
            "https://64.media.tumblr.com/833dea0d4c0ebaff607de7f692b38404/89003f6347ca9f7a-ed/s400x600/0df915fa740e1567daec524b3d50a45ee1441411.gif",
            "https://64.media.tumblr.com/ae902e5f721e780a8675f808e29c945b/0c723e1a75620cd7-e3/s250x400/e2eddf28cfed0aa4f48aa76ba95050bcb589ebcd.gif",
            "https://64.media.tumblr.com/e18181a6bae09d6b9424c6b389bfc397/50363b2caf4843fa-47/s540x810/2b90e025446260276175bcf53a837fce2512e37c.gif",
            "https://64.media.tumblr.com/0c3814183332664ed69dbc7bad646abf/tumblr_pvdabhky7T1u7licjo2_r1_400.gif",
            "https://64.media.tumblr.com/ca99290d3a612a4878c09569f4aad121/eb30ac7251477b5a-55/s400x600/68bd5dd83bcf19a0e6b7a0b54920b2aaec91653e.gif",
            "https://64.media.tumblr.com/abc682a440f694d3e7726501a956df4b/3807359875cc966a-4b/s400x600/a36495341c1550609bac4791188aeadd203e16c9.gif",
            "https://64.media.tumblr.com/54320d23005a55e6020c3bc6498bb900/921cfaed1f692f54-2f/s400x600/91ebf701913caddd40110e3ce0338f9553275a25.gif",
            "https://64.media.tumblr.com/59a1611753f502ecb68f908274286767/921cfaed1f692f54-5f/s400x600/6a7a23949ff6f478cbf9181dd9b3feb04504ab91.gif",
            "https://64.media.tumblr.com/6fd1994583841280741812f0ed43cd62/df728240c200cfb1-34/s250x400/d09dccec93ae467eee418950a9be548c4fa1862f.gif",
            "https://64.media.tumblr.com/34606ef911c52a62bdfabebb98fd2c4f/6c17c8f0f5434bfe-6a/s540x810/5e65b1f1de0be06f2f79dac71e3c0f6986f8b7f3.gif",
            "https://64.media.tumblr.com/009b2756df9e8fe811318df941102f23/6c17c8f0f5434bfe-a6/s540x810/bbcd50e2b7c131f07f502c9cf57e9abcdbfd0ff8.gif",
            "https://64.media.tumblr.com/b27c3ac84dc5566418a40e67e6857955/b89696adbc4a3780-8c/s400x600/de75338611bb622cbae9dc75185d128204ddfccc.gif",
            "https://64.media.tumblr.com/794ade2e926911cf721376398ba378f4/de3281721b6bcf8d-17/s540x810/30afbd1cec7fb205e2a1c9b36e2b0b5e04b5c0dd.gif",
            "https://64.media.tumblr.com/8176d5a852babc83dbb6ecd8b1f1aedf/49f6f0edee769e57-57/s400x600/3896b7d10f97239ee5c6158ab549a5af7c9c1fe1.gif",
            "https://64.media.tumblr.com/ef592a18c0ab092967a5eaa1f550fc5d/dfae9c3e33c7ad9e-b1/s540x810/d496b5c1fa7ae75fe4b3f20d1c7858a13b473b0d.gif",
            "https://64.media.tumblr.com/d00ec5c1177e1a0141017c38f3366b9a/tumblr_pzbhr2rE2y1w9jyl4o7_250.gif",
            "https://media.discordapp.net/attachments/485095951480913935/807851713281261628/tumblr_osmry567Q31r7fqv1o1_400.gif",
            "https://media.discordapp.net/attachments/485095951480913935/807851845183471657/TangibleMinorBeagle.gif"]

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
            "https://tenor.com/view/haseul-haseul-my-beloved-my-beloved-heart-loona-gif-19628816",
            "https://64.media.tumblr.com/1b2faaa368ce75f1d963a7d3292c6031/ebebdc3991f3e79b-9b/s400x600/739d660f70f030a65f5d060fef42c2c18e036b9b.gif",
            "https://64.media.tumblr.com/2d32f38f27032494ccb9ac690d64bba6/2d628aa61822724d-7a/s540x810/bf84b5c40e4c3d2d3f7e4c2e0583abfcf21eb4b5.gif",
            "https://64.media.tumblr.com/f53f27fb9aca9305a261ecbd57ee2235/2d42bcc04dcfe849-07/s400x600/0b3af7f2714c19effd839ac818dfd4c2d4524242.gif",
            "https://64.media.tumblr.com/2523095b8f838f6d3fd6888c5f36adba/c34f869190434afd-c2/s540x810/1bc72c4de4a73abbd1f452cd7fd2dfdb931ec2a7.gif",
            "https://64.media.tumblr.com/63879d943ce9230d01af9ca99bcf07e9/7cfbd9e998c34a96-a4/s540x810/81fccfc1b6154728f664a1dc3899ae61c1da3610.gif",
            "https://64.media.tumblr.com/181710688420074ea04186dc8d001304/3c549c71ab8d6d05-3b/s500x750/bddac402025f0eb3a259ff070d81b0eca02b92c0.gif",
            "https://64.media.tumblr.com/91bde97a8ee5d8887890c06e0ab5ceff/3c549c71ab8d6d05-10/s500x750/eb9d4d69ab499e4f1b341171e572080ebbb1ec50.gif",
            "https://tenor.com/view/loona-haseul-yes-nod-gif-15405788",
            "https://media.discordapp.net/attachments/485095951480913935/807852096622821426/tumblr_osa2azj2QB1wt6m3ho3_400.gif"]

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
            "https://gfycat.com/alienatedfatjoey-visucal-cam-christmas-special-loona-idalyisonyeo",
            "https://gfycat.com/littlecomposedamberpenshell-jinsoul-loona-gowon-vivi",
            "https://gfycat.com/shyoilyamericanlobster",
            "https://gfycat.com/limitedmiserlycrossbill",
            "https://gfycat.com/fakedistantasianconstablebutterfly",
            "https://gfycat.com/NeatValuableDipper"]

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
            "https://gfycat.com/costlyfreecurlew-loona-kim-lip-kim-jungeun-girl-group",
            "https://media.discordapp.net/attachments/485095951480913935/807852152960843826/5e3ee2302026d45ceee5010a03ff2b73fa5f2b09_hq.gif"]

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
            "https://gfycat.com/lastingwetamazontreeboa",
            "https://cdn.discordapp.com/attachments/430377179285553163/799058769757339658/dearb.gif",
            "https://cdn.discordapp.com/attachments/430377179285553163/799058909120823297/dear3.gif",
            "https://64.media.tumblr.com/2059ce4ef4286b202eac18cee98dbe36/e41ea9ccbe10b456-11/s540x810/11dba382aea8a844fb2fbd0eadfe842458359742.gif"]

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
            "https://64.media.tumblr.com/dba3e19e2b17bf90f76ecc5720bc1d3d/86ff17a81a7186f2-70/s250x400/13c923b7950a216fc61bf306fcfcdc4577857ff2.gif",
            "https://media.discordapp.net/attachments/725380066573418628/807066936055562280/Choerydance.gif"]
        
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
            "https://gfycat.com/coolshorttermarawana-loona-kpop-trkz-yves",
            "https://gfycat.com/skinnyforsakenconey",
            "https://64.media.tumblr.com/f16f2d585ece45f72770dc0d6728619a/0153a57216aa8878-d3/s400x600/8153efb331f2f51cec1e16abaed456fb92f8551b.gif",
            "https://64.media.tumblr.com/46a5826d484f3b939a5dac3688f600e9/5ada531d5238ca1e-42/s540x810/1803b1f3e9e45c65e88c6758d780b893b2e1aa0d.gif",
            "https://64.media.tumblr.com/8823e91f8c84df064978f44e4905c677/862beed2e27195b8-cb/s540x810/34afdf2f90a0555c80f1658b4e3cc3b56d5073a1.gif"]

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
            "https://gfycat.com/scrawnyenergeticgazelle-kimjiwoo-loonachuu-wink-yyxy-gimjiu",
            "https://gfycat.com/miserlywellinformedlaughingthrush",
            "https://gfycat.com/plainanxiousamericankestrel",
            "https://64.media.tumblr.com/a431f335902688e0679785be687236ab/3ac5e4dabc440c5d-98/s540x810/23aa9bc48b0e693ea0cb49bb43752520ca8b5043.gif",
            "https://64.media.tumblr.com/556103ba4a4af5e4191d5e96b7516c69/6ccb7142d438c095-98/s540x810/22f4953d63ee9173cf604e14cb0c15991eb87d47.gif"]

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
            "https://gfycat.com/finediscreteindianringneckparakeet-loona-gowon",
            "https://64.media.tumblr.com/1727d873e3f5f21e982415da01ac87fa/adaf8573d2f0918f-ff/s540x810/ea5101512af6b6b1cb31b0f0323f9e9ebe7343e3.gif"]

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
            "https://gfycat.com/allquaintleopardseal-loona-olivia-hye-beauty",
            "https://gfycat.com/skinnyforsakenconey",
            "https://gfycat.com/nervoussinglearchaeocete",
            "https://gfycat.com/fasthopefulcommabutterfly",
            "https://tenor.com/view/astro-mj-astro-astro-mj-kim-myung-jun-astro-astro-kim-myung-jun-gif-13439109"]

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
        elif arg == "olivia hye" or arg == "olivia" or arg == "olihye" or arg == "oliviahye":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Olivia Hye :wolf:')
                    await ctx.send(random.choice(self.bot.oliviahye_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()  
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Olivia Hye :wolf:')
                await ctx.send(random.choice(self.bot.oliviahye_gif))
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

   

def setup(client):
    client.add_cog(LoonaPings(client))


# #.1/3
#     @commands.command()
#     async def heejin(self, ctx):
#         if ctx.guild.id == luminary:
#             if ctx.channel.id == kbotcom:
#                 await ctx.send(f'<@{mae}>, <@{aeong}>, <@!{ctx.author.id}> is talking about Heejin :rabbit:')
#                 await ctx.send(random.choice(self.bot.heejin_gif))
#                 await ctx.message.delete()
#             else:
#                 await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
#                 await ctx.message.delete()
#         else:
#             await ctx.send(f'<@!{ctx.author.id}> is talking about Heejin :rabbit:')
#             await ctx.send(random.choice(self.bot.heejin_gif))
#             await ctx.message.delete()

#     @commands.command()
#     async def hyunjin(self, ctx):
#         if ctx.guild.id == luminary:
#             if ctx.channel.id == kbotcom:
#                 await ctx.send(f'<@{k8}>, <@{aeong}>, <@!{ctx.author.id}> is talking about Hyunjin :cat::bread:')
#                 await ctx.send(random.choice(self.bot.hyunjin_gif))
#                 await ctx.message.delete()
#             else:
#                 await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
#                 await ctx.message.delete()
#         else:
#             await ctx.send(f'<@!{ctx.author.id}> is talking about Hyunjin :cat::bread:')
#             await ctx.send(random.choice(self.bot.hyunjin_gif))
#             await ctx.message.delete()

#     @commands.command()
#     async def haseul(self, ctx):
#         if ctx.guild.id == luminary:
#             if ctx.channel.id == kbotcom:
#                 await ctx.send(f'<@{ctx.author.id}> is talking about Haseul :dove::green_heart:')
#                 await ctx.send(random.choice(self.bot.haseul_gif))
#                 await ctx.message.delete()
#             else:
#                 await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
#                 await ctx.message.delete()
#         else:
#             await ctx.send(f'<@{ctx.author.id}> is talking about Haseul :dove::green_heart:')
#             await ctx.send(random.choice(self.bot.haseul_gif))
#             await ctx.message.delete()

#     @commands.command()
#     async def vivi(self, ctx):
#         if ctx.guild.id == luminary:
#             if ctx.channel.id == kbotcom:
#                 await ctx.send(f'<@{manman}>, <@{ctx.author.id}> is talking about ViVi :deer:')
#                 await ctx.send(random.choice(self.bot.vivi_gif))
#                 await ctx.message.delete()
#             else:
#                 await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
#                 await ctx.message.delete()
#         else:
#             await ctx.send(f'<@{ctx.author.id}> is talking about ViVi :deer:')
#             await ctx.send(random.choice(self.bot.vivi_gif))
#             await ctx.message.delete()

#     @commands.command()
#     async def yeojin(self, ctx):
#         if ctx.guild.id == luminary:
#             if ctx.channel.id == kbotcom:
#                 await ctx.send(f'<@{ctx.author.id}> is talking about Yeojin :frog::orange_heart:')
#                 await ctx.send(random.choice(self.bot.yeojin_gif))
#                 await ctx.message.delete()
#             else:
#                 await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
#                 await ctx.message.delete()
#         else:
#             await ctx.send(f'<@{ctx.author.id}> is talking about Yeojin :frog::orange_heart:')
#             await ctx.send(random.choice(self.bot.yeojin_gif))
#             await ctx.message.delete()


# #.oec
#     @commands.command(aliases=['kim', 'lip', 'lippington', 'kimlip'])
#     async def lippie(self, ctx):
#         if ctx.guild.id == luminary:
#             if ctx.channel.id == kbotcom:
#                 await ctx.send(f'<@{stanley}>, <@!{ctx.author.id}> is talking about Kim Lip :owl:')
#                 await ctx.send(random.choice(self.bot.kimlip_gif))
#                 await ctx.message.delete()
#             else:
#                 await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=6)
#                 await ctx.message.delete()
#         else:
#             await ctx.send(f'<@!{ctx.author.id}> is talking about Kim Lip :owl:')
#             await ctx.send(random.choice(self.bot.kimlip_gif))
#             await ctx.message.delete()

#     @commands.command()
#     async def jinsoul(self, ctx):
#         if ctx.guild.id == luminary:
#             if ctx.channel.id == kbotcom:
#                 await ctx.send(f'<@{ctx.author.id}> is talking about Jinsoul :fish:')
#                 await ctx.send(random.choice(self.bot.jinsoul_gif))
#                 await ctx.message.delete()
#             else:
#                 await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
#                 await ctx.message.delete()
#         else:
#             await ctx.send(f'<@{ctx.author.id}> is talking about Jinsoul :fish:')
#             await ctx.send(random.choice(self.bot.jinsoul_gif))
#             await ctx.message.delete()

#     @commands.command()
#     async def choerry(self, ctx):
#         if ctx.guild.id == luminary:
#             if ctx.channel.id == kbotcom:
#                 await ctx.send(f'<@{rith}>, <@{ple}>, <@!{ctx.author.id}> is talking about Choerry :bat:')
#                 await ctx.send(random.choice(self.bot.choerry_gif))
#                 await ctx.message.delete()
#             else:
#                 await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
#                 await ctx.message.delete()            
#         else:
#             await ctx.send(f'<@!{ctx.author.id}> is talking about Choerry :bat:')
#             await ctx.send(random.choice(self.bot.choerry_gif))
#             await ctx.message.delete()
# #.yyxy
#     @commands.command()
#     async def yves(self, ctx):
#         if ctx.guild.id == luminary:
#             if ctx.channel.id == kbotcom:
#                 await ctx.send(f'<@!{ctx.author.id}> is talking about Yves :swan::apple:')
#                 await ctx.send(random.choice(self.bot.yves_gif))
#                 await ctx.message.delete()
#             else:
#                 await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
#                 await ctx.message.delete()            
#         else:
#             await ctx.send(f'<@!{ctx.author.id}> is talking about Yves :swan::apple:')
#             await ctx.send(random.choice(self.bot.yves_gif))
#             await ctx.message.delete()

    # @commands.command()
    # async def gowon(self, ctx):
    #     if ctx.guild.id == luminary:
    #         if ctx.channel.id == kbotcom:
    #             await ctx.send(f'<@{rith}>, <@{masa}>, <@!{ctx.author.id}> is talking about Go Won :butterfly::pineapple:')
    #             await ctx.send(random.choice(self.bot.gowon_gif))
    #             await ctx.message.delete()
    #         else:
    #             await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
    #             await ctx.message.delete()            
    #     else:
    #         await ctx.send(f'<@!{ctx.author.id}> is talking about Go Won :butterfly::pineapple:')
    #         await ctx.send(random.choice(self.bot.gowon_gif))
    #         await ctx.message.delete()

    # @commands.command(aliases = ['hyejoo', 'hye', 'olivia'])
    # async def oliviahye(self, ctx):
    #     if ctx.guild.id == luminary:
    #         if ctx.channel.id == kbotcom:
    #             await ctx.send(f'<@!{ctx.author.id}> is talking about Olivia Hye :wolf:')
    #             await ctx.send(random.choice(self.bot.oliviahye_gif))
    #             await ctx.message.delete()
    #         else:
    #             await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
    #             await ctx.message.delete()            
    #     else:
    #         await ctx.send(f'<@!{ctx.author.id}> is talking about Olivia Hye :wolf:')
    #         await ctx.send(random.choice(self.bot.oliviahye_gif))
    #         await ctx.message.delete()
 