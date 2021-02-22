import discord, random, datetime
from discord.ext import commands
from datetime import datetime

        #= P1Harmony
        #= VAV

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

#//people

class BGS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    #. Astro
        self.bot.astro_eunwoo_gif = ["https://tenor.com/view/true-beauty-lee-suho-suho-chasuho-jugyeong-gif-19661654",
            "https://tenor.com/view/cha-eunwoo-roach-cha-eunwoo-gif-19550271",
            "https://tenor.com/view/cha-eunwoo-eunwoo-stare-handsome-astro-gif-16286163",
            "https://tenor.com/view/astro-eunwoo-cha-eunwoo-eunwoo-heart-eunwoo-seet-gif-13439107",
            "https://tenor.com/view/eunwoo-astro-eunwoo-cha-eunwoo-eunwoo-cute-eunwoo-smile-gif-17176423",
            "https://tenor.com/view/lee-dongmin-cha-eunwoo-astro-kpop-cute-gif-17756922",
            "https://tenor.com/view/my-love-gangnam-beauty-astro-eunwoo-sip-gif-15279166",
            "https://tenor.com/view/cha-eunwoo-eunwoo-true-beauty-suho-lee-suho-gif-20007285",
            "https://tenor.com/view/cha-eun-woo-finger-gun-hearts-wink-gif-15107507",
            "https://tenor.com/view/eunwoo-dongmin-gif-9221444",
            "https://tenor.com/view/cha-eunwoo-roach-cha-eunwoo-gif-19550268",
            "https://tenor.com/view/true-beauty-lee-suho-chasuho-cha-eunwoo-teamsuho-gif-19646580",
            "https://tenor.com/view/astro-astro-eunwoo-eunwoo-cha-eun-woo-lee-dong-min-gif-14735333"]

        self.bot.astro_mj_gif = ["https://tenor.com/view/astro-mj-astro-astro-mj-kim-myung-jun-astro-astro-kim-myung-jun-gif-13439109",
            "https://tenor.com/view/%EC%95%84%EC%8A%A4%ED%8A%B8%EB%A1%9C-astro-kpop-astro-cute-astro-mj-gif-17176436",
            "https://tenor.com/view/astro-astro-mj-astro-kpop-kpop-aegyo-gif-17183095",
            "https://tenor.com/view/astro-astro-mj-sign-of-the-cross-pray-astro-mj-pray-gif-14735521",
            "https://tenor.com/view/%EC%95%84%EC%8A%A4%ED%8A%B8%EB%A1%9C-astro-kpop-astro-cute-astro-mj-gif-17176426",
            "https://tenor.com/view/rocky-astro-rocky-astro-eunwoo-astro-jinjin-astro-gif-17380951",
            "https://tenor.com/view/mj-astro-excited-eunwoo-happy-gif-17381113"]
    #. The Boyz
        self.bot.theboyz_kevin_gif = ["https://tenor.com/view/the-boyz-kevin-cute-kpop-peace-out-gif-12754924",
            "https://tenor.com/view/kevin-moon-kevin-tbz-tbz-the-boyz-kevin-gif-20137479",
            "https://tenor.com/view/kevin-moon-the-boyz-the-boyz-kevin-canadian-singer-handsome-gif-17250561",
            "https://tenor.com/view/kevin-the-boyz-hearts-k-pop-gif-9986684",
            "https://tenor.com/view/tbz-the-boyz-kevin-moon-kevin-heart-gif-17895708",
            "https://64.media.tumblr.com/44aa777eb289bb136471aca0328c06eb/tumblr_pnr6fpPREm1y76lgdo4_250.gif",
            "https://64.media.tumblr.com/dab0e901caa12feae6ce06388a10bee9/tumblr_pqpf3ypgeN1wmcsy5o2_250.gif",
            "https://64.media.tumblr.com/bc1b14d49511dc2492baadf4c890a136/tumblr_pnr6fpPREm1y76lgdo8_250.gif",
            "https://64.media.tumblr.com/24425f03695c86bb43573fd4970f4489/tumblr_pnr6fpPREm1y76lgdo1_250.gif",
            "https://64.media.tumblr.com/d5af6183784a011c7125f1ed874529a3/tumblr_pjyoqwXydm1xk8jydo3_250.gif",
            "https://64.media.tumblr.com/fecf7ab54b06c8007e225826d4fc503f/tumblr_pmmmgdUDLa1wvslp2o3_250.gif"]

        self.bot.theboyz_sangyeon_gif = ["https://tenor.com/view/%EB%8D%94%EB%B3%B4%EC%9D%B4%EC%A6%88-the-boyz-sangyeon-lee-sangyeon-kpop-gif-16153887",
            "https://tenor.com/view/the-boyz-tbz-sangyeon-lee-sangyeon-handsome-gif-17895565",
            "https://tenor.com/view/the-boyz-sangyeon-kpop-cute-handsome-gif-17604516",
            "https://tenor.com/view/the-boyz-sangyeon-hearts-kpop-finger-guns-gif-14026292",
            "https://tenor.com/view/sangyeon-tbz-the-boyz-kpop-cute-gif-17552021",
            "https://tenor.com/view/relieved-the-boyz-sangyeon-kpop-gif-13991870",
            "https://tenor.com/view/the-boyz-sangyeon-what-kpop-gif-14784836",
            "https://tenor.com/view/the-boyz-tbz-sangyeon-lee-sangyeon-handsome-gif-17895538",
            "https://tenor.com/view/%EB%8D%94%EB%B3%B4%EC%9D%B4%EC%A6%88-the-boyz-sangyeon-lee-sangyeon-kpop-gif-17746977",
            "https://tenor.com/view/%EB%8D%94%EB%B3%B4%EC%9D%B4%EC%A6%88-the-boyz-sangyeon-lee-sangyeon-kpop-gif-17746979",
            "https://tenor.com/view/the-boyz-tbz-sangyeon-lee-sangyeon-handsome-gif-17895603",
            "https://tenor.com/view/deobi-the-boyz-sangyeon-lee-sangyeon-the-b-gif-17301901",
            "https://tenor.com/view/sangyeon-tbz-sangyeon-the-boyz-the-boyz-sangyeon-kpop-gif-17450017"]

        self.bot.theboyz_jacob_gif = ["https://tenor.com/view/love-checkmate-rtk-saranghae-heart-gif-17642238",
            "https://tenor.com/view/jacob-bae-the-boyz-kpop-smile-heart-gif-16668362",
            "https://tenor.com/view/the-boyz-gif-18316667",
            "https://tenor.com/view/handsome-happy-the-boyz-jacob-cute-gif-17913930",
            "https://tenor.com/view/lovely-handsome-nature-sexy-the-boyz-gif-17824817",
            "https://tenor.com/view/the-boyz-jacob-what-gif-14110430",
            "https://tenor.com/view/tbz-the-boyz-jacob-the-boyz-jacob-gif-20000867",
            "https://tenor.com/view/jacob-jacob-bae-the-boyz-jacob-chewing-gif-18152180",
            "https://tenor.com/view/jacob-tbz-the-boyz-tbz-jacob-concerned-gif-19257327",
            "https://tenor.com/view/the-boyz-tbz-jacob-jacob-bae-%EC%A0%9C%EC%9D%B4%EC%BD%A5-gif-18256941",
            "https://tenor.com/view/the-boyz-jacob-thumbs-up-approved-kpop-gif-12754961",
            "https://tenor.com/view/jacob-bae-the-boyz-the-boyz-jacob-tbzjmn-jacobaethings-gif-19686943"]

        self.bot.theboyz_younghoon_gif = ["https://tenor.com/view/kcon-%EC%BC%80%EC%9D%B4%EC%BD%98-m-countdown-%EC%97%A0%EC%B9%B4-mnet-gif-14815018",
            "https://tenor.com/view/%EB%8D%94%EB%B3%B4%EC%9D%B4%EC%A6%88-the-boyz-younghoon-kim-younghoon-kpop-gif-17717610",
            "https://tenor.com/view/younghoon-the-boyz-kim-younghoon-smile-kpop-gif-17566430",
            "https://tenor.com/view/younghoon-the-boyz-younghoon-theboyz-kpop-cute-gif-17893813",
            "https://tenor.com/view/younghoon-the-boyz-kim-younghoon-kpop-cute-gif-17471797",
            "https://tenor.com/view/kpop-the-boyz-younghoon-shocked-shook-gif-11648955",
            "https://tenor.com/view/the-boyz-younghoon-happy-love-kpop-gif-11679670",
            "https://tenor.com/view/the-boyz-younghoon-kim-younghoon-playful-cute-gif-17540287",
            "https://tenor.com/view/younghoon-the-boyz-tbz-gif-19303453",
            "https://tenor.com/view/younghoon-the-boyz-kim-younghoon-kpop-cute-gif-17490371",
            "https://tenor.com/view/%EB%8D%94%EB%B3%B4%EC%9D%B4%EC%A6%88-the-boyz-younghoon-kim-younghoon-kpop-gif-17717615",
            "https://tenor.com/view/the-boyz-younghoon-kim-younghoon-kpop-handsome-gif-15713938",
            "https://tenor.com/view/younghoon-chanhee-the-boyz-tbz-tbz-younghoon-gif-18984986"]

        self.bot.theboyz_hyunjae_gif = ["https://tenor.com/view/hyunjae-hyunjae-the-boyz-stare-look-cute-gif-17364449",
            "https://tenor.com/view/the-boyz-hyunjae-cute-kpop-gif-14056530",
            "https://tenor.com/view/thanks-love-handsome-road-to-kingdom-the-boyz-gif-17641817",
            "https://tenor.com/view/hyunjae-the-boyz-hyunjae-lee-hyunjae-jaehyun-lee-jaehyun-gif-17562612",
            "https://tenor.com/view/hyunjae-lee-hyunjae-the-boyz-hyunjae-kpop-handsome-gif-17714293",
            "https://tenor.com/view/tbz-the-boyz-hyunjae-jaehyun-heart-gif-17863032",
            "https://tenor.com/view/hyunjae-the-boyz-kiss-tbz-gif-19725512",
            "https://tenor.com/view/hyunjae-lee-jaehyun-hyunjae-the-boyz-tbz-the-boyz-gif-20343497",
            "https://tenor.com/view/hyunjae-the-boyz-hyunjae-tbz-the-boyz-gif-20127794",
            "https://tenor.com/view/hyunjae-the-boyz-jaehyun-lee-tbz-clapping-gif-17780663",
            "https://tenor.com/view/tbz-the-boyz-jaehyun-hyunjae-cat-gif-17862602",
            "https://tenor.com/view/tbz-the-boyz-smile-hyunjae-jaehyun-gif-17862596",
            "https://tenor.com/view/%EB%8D%94%EB%B3%B4%EC%9D%B4%EC%A6%88-the-boyz-hyunjae-lee-jaehyun-kpop-gif-16153899"]

        self.bot.theboyz_juyeon_gif = ["https://tenor.com/view/juyeon-catboy-tbz-the-boyz-juyeon-catboy-gif-18125362",
            "https://tenor.com/view/juyeon-lee-juyeon-the-boyz-tbz-gif-19039721",
            "https://tenor.com/view/juyeon-lee-juyeon-juyeon-funny-the-boyz-juyeon-gif-20130970",
            "https://tenor.com/view/juyeon-the-boyz-kpop-cute-handsome-gif-16642843",
            "https://tenor.com/view/juyeon-the-boyz-the-boyz-juyeon-juyeongoes-to-jungle-juyeon-at-airport-gif-13118344",
            "https://64.media.tumblr.com/4cfdd6d3bda585b531a8f91e5c09e9af/72a09f02cbb75b6b-1c/s500x750/2ae4679ff1a0e25caef1217d7ccdc843e1687aca.gif",
            "https://64.media.tumblr.com/54d901b7760873dffbd3e2ca0398c48f/72a09f02cbb75b6b-f2/s500x750/1154250ded49f83d8d87982a68faf2073ec3c360.gif",
            "https://64.media.tumblr.com/6b45e4fc75a96b17b4f476d43bf28fd2/44e2f4a779345e33-36/s250x400/e4803e27c08a38163595d8415d0f01f66875d2c6.gif",
            "https://64.media.tumblr.com/987a75b71d5b2e22f1de303e7c6a7d37/44e2f4a779345e33-d0/s250x400/59b060a4fa804d7261f04cb2eb1401ac61d160b8.gif",
            "https://64.media.tumblr.com/8df6f96a0ba9d8b75115d97a7877c8d0/fb2141e86ef4000c-4c/s500x750/ddba9518fd34bed3e406d0540f917aa263802501.gif",
            "https://64.media.tumblr.com/d1f917363f7233b9839b4c1f04157a19/2a95678bbf1d6ff7-0c/s250x400/8feeab15f6438bf1952286110fc4ec239e7e7f00.gif",
            "https://64.media.tumblr.com/27cda92df9e2733e9141c9b07e688ad8/3bc76cabf7f13e6f-99/s250x400/f1e88a311f3343532e09ae936b031ce6136d3477.gif"]

        self.bot.theboyz_new_gif = ["https://tenor.com/view/chanhee-the-boyz-kpop-new-the-boyz-new-gif-17717658",
            "https://tenor.com/view/chanhee-thumbs-up-supportive-the-boyz-tbz-gif-18955020",
            "https://tenor.com/view/the-boyz-new-the-boyz-choi-chanhee-main-vocalist-kpop-gif-17665942",
            "https://tenor.com/view/kpop-the-boyz-chanhee-new-fairy-gif-12653054",
            "https://tenor.com/view/the-boyz-new-new-the-boyz-choi-chanhee-main-vocalist-gif-17717620",
            "https://64.media.tumblr.com/51cd41167c5a80d1a4d56de90810a84c/tumblr_p93qg00PK91xsj5gko5_r6_250.gif",
            "https://tenor.com/view/choi-chanhee-new-the-boyz-the-boyz-gif-18810551",
            "https://tenor.com/view/chanhee-the-boyz-new-the-boyz-gif-18009008",
            "https://tenor.com/view/kiss-the-boyz-chanhee-new-nyu-gif-16642851",
            "https://tenor.com/view/the-boyz-new-choi-chanhee-main-vocalist-kpop-gif-16028891",
            "https://tenor.com/view/choi-chanhee-new-the-boyz-the-boyz-gif-18810545",
            "https://tenor.com/view/chanhee-new-the-boyz-the-boyz-gif-18009021",
            "https://tenor.com/view/chanhee-choi-new-the-boyz-the-boyz-gif-18810536",
            "https://tenor.com/view/choi-chanhee-new-the-boyz-the-boyz-gif-18810560"]

        self.bot.theboyz_q_gif = ["https://tenor.com/view/the-boyz-gif-18316665",
            "https://tenor.com/view/changmin-ji-changmin-the-boyz-tbz-jungyuz-gif-19256496",
            "https://tenor.com/view/the-boyz-q-hello-k-pop-pop-up-gif-9987755",
            "https://tenor.com/view/tbz-the-boyz-ji-changmin-changmin-the-boyz-q-gif-19561766",
            "https://tenor.com/view/tbz-changmin-tbz-changmin-changmin-punching-gif-20013911",
            "https://64.media.tumblr.com/c36c76330267bd3a4df0f9e1b805f76e/tumblr_po5zevs5IE1y42eufo2_r1_400.gif",
            "https://64.media.tumblr.com/c35178030c6ed074083bf15ce83e1436/tumblr_po5zevs5IE1y42eufo5_r1_400.gif",
            "https://64.media.tumblr.com/f29c4f88c563ac00b6f794948fff42f8/tumblr_po5zevs5IE1y42eufo8_r1_400.gif",
            "https://64.media.tumblr.com/7d2fc9da65fa6acc563b46d7885722e8/26c9eab069e66d8b-32/s400x600/7b36659e6c4d53962a61887c61f01e71a2d7c4ce.gif",
            "https://64.media.tumblr.com/f14f0321bff988298e2c62d23356c650/26c9eab069e66d8b-9c/s400x600/c950ae3798a75a8671b628f2b0623a3d7454c8fd.gif",
            "https://64.media.tumblr.com/69f62b2fdcc28e8282202f59678d096f/tumblr_pnvw0hjWy71y1b23io5_r1_250.gif",
            "https://64.media.tumblr.com/cadc3cb4876dce4e0b33eda21217205d/tumblr_pnvw0hjWy71y1b23io3_r1_250.gif",
            "https://64.media.tumblr.com/cdddc8e353eeda792a75b90ebf122186/tumblr_pnvw0hjWy71y1b23io9_r1_250.gif",
            "https://64.media.tumblr.com/e053111b09e23bcf957c22518815ff0b/tumblr_pnvw0hjWy71y1b23io8_r1_250.gif",
            "https://64.media.tumblr.com/03d4ac6b8e72804cd6e633b919078440/9e20d1180588f38f-fe/s400x600/3e9010f5025f699ff70ae5798293bd2c62934c43.gif",
            "https://64.media.tumblr.com/5776bec959f1841d173767fb4e3647d3/tumblr_posood16Xp1wy5yr0o5_r1_250.gif",
            "https://64.media.tumblr.com/064cfd7a12cacfa82b56672d5ac1fb5a/tumblr_posood16Xp1wy5yr0o4_r1_250.gif",
            "https://64.media.tumblr.com/c213c25e5f75b80946f19b94f6a94bd3/tumblr_posood16Xp1wy5yr0o3_250.gif",
            "https://64.media.tumblr.com/008cba5cadd1990179913cfdb00fd1fd/tumblr_posood16Xp1wy5yr0o1_250.gif"]

        self.bot.theboyz_haknyeon_gif = ["https://tenor.com/view/hak-haknyeon-tbz-bye-goodbye-gif-19756941",
            "https://tenor.com/view/the-boyz-haknyeon-smiles-happy-kpop-gif-14110324",
            "https://tenor.com/view/handsome-ju-haknyeon-haknyeon-the-boyz-fighting-gif-17641846",
            "https://tenor.com/view/ju-haknyeon-haknyeon-the-boyz-%EB%8D%94%EB%B3%B4%EC%9D%B4%EC%A6%88-handsome-gif-17717602",
            "https://tenor.com/view/the-boyz-haknyeon-hello-there-kpop-juhaknyeon-gif-12730844",
            "https://64.media.tumblr.com/a3d46d24d322f425651b063aa7a48f44/6fcc58052d07fa49-66/s500x750/c7990e4fba9d44e17bf0bc62f3e10cc365862b2e.gif",
            "https://64.media.tumblr.com/6b4d63210df23b83e1d409b2bfdd544d/tumblr_pjux0nhjO81s7m4tc_250.gif",
            "https://64.media.tumblr.com/56d137b7c33ec7e5051730b4115547e3/tumblr_pjux0gyjv41s7m4tc_250.gif",
            "https://64.media.tumblr.com/2d7f4f8687eb1888a2c06c8085f094d1/tumblr_p93qg00PK91xsj5gko3_r5_250.gif",
            "https://64.media.tumblr.com/3323207580d278b8ac9fe5a4e7c2ce43/4be0cd247b5c938f-6c/s500x750/c4576327eac21e017a703db2edc756d275043c7d.gif",
            "https://64.media.tumblr.com/f9da20e9f6976400e96f97b3e3079925/tumblr_pwosvhI7J61ytb771o7_250.gif",
            "https://64.media.tumblr.com/88422061b3c901b056d8c11a53bc4f31/2af42dbe1d769b2e-60/s250x400/270ed86bfb6a516954abee78b0dc56b163421b35.gif"]

        self.bot.theboyz_sunwoo_gif = ["https://tenor.com/view/sunwoo-the-boyz-kim-sunwoo-gif-18352599",
            "https://tenor.com/view/the-boyz-sunwoo-heart-love-you-kpop-gif-14056446",
            "https://tenor.com/view/sunwoo-sunwoo-aesthetic-sunwoo-pfp-sunwoo-pretty-pretty-guy-gif-20187252",
            "https://tenor.com/view/sunwoo-kim-sunwoo-the-boyz-tbz-gif-19358958",
            "https://tenor.com/view/sunwoo-the-boyz-tbz-kpop-the-boyz-sunwoo-gif-19272813",
            "https://tenor.com/view/sunwoo-imitating-kevin-sunwoo-tbz-the-boyz-gif-20224449",
            "https://tenor.com/view/tbz-the-boyz-sunwoo-kim-sunwoo-amazed-gif-17863040",
            "https://tenor.com/view/sunwoo-kim-sunwoo-tbzhour-tbz-the-boyz-gif-18439976",
            "https://tenor.com/view/sunwoo-the-boyz-kim-sunwoo-dance-gif-20085120",
            "https://tenor.com/view/sunwoo-kim-sunwoo-the-boyz-tbz-kpop-gif-17323830",
            "https://tenor.com/view/sunwoo-the-boyz-kim-sunwoo-gif-18352599",
            "https://tenor.com/view/sunwoo-the-boyz-tbz-sunwoo-sunwooeating-sunu-gif-18876590",
            "https://tenor.com/view/sunu-tbz-the-boyz-sunwoo-sunwoo-dancing-gif-18742384",
            "https://tenor.com/view/sunwoo-gif-19843755"]

        self.bot.theboyz_eric_gif = ["https://tenor.com/view/handsome-sexy-the-boyz-eric-oh-gif-17891020",
            "https://tenor.com/view/tbz-the-boyz-eric-sohn-kpop-theb-gif-17972062",
            "https://tenor.com/view/eric-eric-sohn-the-boyz-peace-sign-handsome-gif-17035217",
            "https://tenor.com/view/eric-sohn-the-boyz-cute-handsome-gif-16668468",
            "https://tenor.com/view/eric-eric-sohn-the-boyz-gif-19230384",
            "https://64.media.tumblr.com/95b25ce20f1cdf168070441ef1c29b74/e9e653d9bfc8ac38-c5/s400x600/d307d9fac675db33b2a10e05231eb668a1634642.gif",
            "https://64.media.tumblr.com/93b1431eb25904b9691c210a882bce43/tumblr_pc3pstbPmn1wl9leto1_500.gif",
            "https://64.media.tumblr.com/7b9a2974a647251392242ebcb9d09e48/tumblr_pc3pstbPmn1wl9leto3_500.gif",
            "https://64.media.tumblr.com/6fbcb642a43a132a875602a65939b5b3/e998b5ccbcda60c8-46/s400x600/3c1b514c5ec2318f3145c13aa2e1e019cb6ab377.gif",
            "https://64.media.tumblr.com/381526bd27e2d5f9cea04aade321758c/e998b5ccbcda60c8-f7/s400x600/6ed1ef89936b9ca8a054b072d85506da8c7514dd.gif",
            "https://64.media.tumblr.com/cd74a9a4c46928e9fbd9b93c49b74510/e998b5ccbcda60c8-f1/s400x600/4d001dc896dba21aebc8bb273831db18b911e0bf.gif",
            "https://64.media.tumblr.com/604c5181e22070e59c6268b70903ba81/e998b5ccbcda60c8-3a/s400x600/e12abae14a0b72cd4b7d15b84b7127e09b2d07cc.gif",
            "https://64.media.tumblr.com/7aec5bfbc06447681f841bcbbaa310e3/e998b5ccbcda60c8-9d/s400x600/930cf2e43f9bec8f98225b2a1107d647a19012bc.gif",
            "https://64.media.tumblr.com/91e5e74812755b47e790194d9c133c4c/98f9f54f13a26e30-47/s540x810/04515506f5468320cdfabd141f14ead9528957fd.gif"]
    #. P1Harmony
        self.bot.p1harmony_intak_gif = ["https://cdn.discordapp.com/attachments/800206337073479690/800261657557074000/image0.gif",
            "https://cdn.discordapp.com/attachments/800206337073479690/800261657880166400/image1.gif",
            "https://cdn.discordapp.com/attachments/800206337073479690/800261658508394516/image2.gif",
            "https://cdn.discordapp.com/attachments/800206337073479690/800261658890731550/image3.gif",
            "https://cdn.discordapp.com/attachments/800206337073479690/800261758714380358/image0.gif",
            "https://cdn.discordapp.com/attachments/800206337073479690/800261759302500392/image1.gif"]

        self.bot.p1harmony_jiung_gif = ["https://cdn.discordapp.com/attachments/800206376210661406/800262168904859668/image0.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262169299910686/image1.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262170029195304/image2.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262170419396628/image3.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262170691764244/image4.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262170952466452/image5.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262218733322270/image0.gif",
            "https://tenor.com/view/jiung-choi-jiung-p1h-p1harmony-gif-20392814",
            "https://tenor.com/view/jiung-p1h-p1harmony-choi-jiung-gif-20392787",
            "https://tenor.com/view/jiung-choi-jiung-p1h-p1harmony-gif-20392855"]

        self.bot.p1harmony_jongseob_gif = ["https://cdn.discordapp.com/attachments/800206414597455872/800262445016809472/image0.gif",
            "https://cdn.discordapp.com/attachments/800206414597455872/800262445314211850/image1.gif",
            "https://cdn.discordapp.com/attachments/800206414597455872/800262554202931261/image0.gif",
            "https://cdn.discordapp.com/attachments/800206414597455872/800262587488534558/image0.gif",
            "https://cdn.discordapp.com/attachments/800206414597455872/800262610305024040/image0.gif",
            "https://tenor.com/view/jongseob-p1h-gif-19927056"]

        self.bot.p1harmony_keeho_gif = ["https://cdn.discordapp.com/attachments/800206480837574666/800262794280304661/image0.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800262794531569684/image1.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800262795144724480/image2.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800262795446845460/image3.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800262908646522880/image0.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800262909077749760/image1.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800262909682253845/image2.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800262909984505856/image3.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800263019380342804/image0.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800263019929665566/image1.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800263020420005908/image2.gif",
            "https://tenor.com/view/keeho-mini-heart-%E0%B8%A1%E0%B8%B4%E0%B8%99%E0%B8%B4%E0%B8%AE%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B8%97-%E0%B8%81%E0%B8%B5%E0%B9%82%E0%B8%AE-p1h-gif-19524452"]

        self.bot.p1harmony_soul_gif = ["https://cdn.discordapp.com/attachments/800206684193685504/800263221390213170/image0.gif",
            "https://cdn.discordapp.com/attachments/800206684193685504/800263221792473088/image1.gif",
            "https://cdn.discordapp.com/attachments/800206684193685504/800263222166814730/image2.gif",
            "https://cdn.discordapp.com/attachments/800206684193685504/800263222514810880/image3.gif",
            "https://cdn.discordapp.com/attachments/800206684193685504/800263223194550272/image4.gif",
            "https://cdn.discordapp.com/attachments/800206684193685504/800263416635588658/image0.gif",
            "https://cdn.discordapp.com/attachments/800206684193685504/800263417167609886/image1.gif",
            "https://cdn.discordapp.com/attachments/800206684193685504/800263417604079636/image2.gif",
            "https://cdn.discordapp.com/attachments/800206684193685504/800263460730437632/image0.gif"]

        self.bot.p1harmony_theo_gif = ["https://cdn.discordapp.com/attachments/800206797604519936/800263698639487016/image0.gif",
            "https://cdn.discordapp.com/attachments/800206797604519936/800263825638293504/image0.gif",
            "https://cdn.discordapp.com/attachments/800206797604519936/800263826138202113/image1.gif",
            "https://cdn.discordapp.com/attachments/800206797604519936/800263827073007616/image2.gif",
            "https://cdn.discordapp.com/attachments/800206797604519936/800263827786432512/image3.gif",
            "https://cdn.discordapp.com/attachments/800206797604519936/800264225443676210/image0.gif",
            "https://cdn.discordapp.com/attachments/800206797604519936/800264226001387540/image1.gif",
            "https://cdn.discordapp.com/attachments/800206797604519936/800264226445852693/image2.gif",
            "https://cdn.discordapp.com/attachments/800206797604519936/800264279206264842/image0.gif"]
    #. SF9
        self.bot.sf9_chani_gif = ["https://cdn.discordapp.com/attachments/805178530279325697/805179888738893834/image0.gif",
            "https://cdn.discordapp.com/attachments/805178530279325697/805179889082564638/image1.gif",
            "https://cdn.discordapp.com/attachments/805178530279325697/805179889438818344/image2.gif",
            "https://cdn.discordapp.com/attachments/805178530279325697/805179889777901588/image3.gif",
            "https://cdn.discordapp.com/attachments/805178530279325697/805179975459405864/image0.gif",
            "https://cdn.discordapp.com/attachments/805178530279325697/805179975766245398/image1.gif",
            "https://cdn.discordapp.com/attachments/805178530279325697/805179976176369734/image2.gif",
            "https://cdn.discordapp.com/attachments/805178530279325697/805179976558706709/image3.gif",
            "https://cdn.discordapp.com/attachments/805178530279325697/805180143311257620/image0.gif",
            "https://cdn.discordapp.com/attachments/805178530279325697/805180143618228224/image1.gif",
            "https://cdn.discordapp.com/attachments/805178530279325697/805180144061906994/image2.gif",
            "https://cdn.discordapp.com/attachments/805178530279325697/805180235477024868/image0.gif",
            "https://cdn.discordapp.com/attachments/805178530279325697/805180235838259220/image1.gif",
            "https://cdn.discordapp.com/attachments/805178530279325697/805180236332269619/image2.gif",
            "https://cdn.discordapp.com/attachments/805178530279325697/805180236706742342/image3.gif"]

        self.bot.sf9_dawon_gif = ["https://cdn.discordapp.com/attachments/805178602554392576/805180404285177866/image0.gif",
            "https://cdn.discordapp.com/attachments/805178602554392576/805180404848001096/image1.gif",
            "https://cdn.discordapp.com/attachments/805178602554392576/805180405199798303/image2.gif",
            "https://cdn.discordapp.com/attachments/805178602554392576/805180445070589962/image0.gif",
            "https://cdn.discordapp.com/attachments/805178602554392576/805180493120667668/image0.gif",
            "https://cdn.discordapp.com/attachments/805178602554392576/805180493581516850/image1.gif",
            "https://cdn.discordapp.com/attachments/805178602554392576/805180573881466880/image0.gif",
            "https://cdn.discordapp.com/attachments/805178602554392576/805180573881466880/image0.gif",
            "https://cdn.discordapp.com/attachments/805178602554392576/805180656875208734/image1.gif",
            "https://cdn.discordapp.com/attachments/805178602554392576/805180659764953088/image2.gif"]

        self.bot.sf9_hwiyoung_gif = ["https://cdn.discordapp.com/attachments/805178727222083635/805180828538896394/image0.gif",
            "https://cdn.discordapp.com/attachments/805178727222083635/805180828845998100/image1.gif",
            "https://cdn.discordapp.com/attachments/805178727222083635/805180829252583475/image2.gif",
            "https://cdn.discordapp.com/attachments/805178727222083635/805180921502236732/image0.gif",
            "https://cdn.discordapp.com/attachments/805178727222083635/805180922025476116/image1.gif",
            "https://cdn.discordapp.com/attachments/805178727222083635/805180922424721408/image2.gif",
            "https://cdn.discordapp.com/attachments/805178727222083635/805181042301861888/image0.gif",
            "https://cdn.discordapp.com/attachments/805178727222083635/805181042724962324/image1.gif",
            "https://cdn.discordapp.com/attachments/805178727222083635/805181043102580826/image2.gif",
            "https://cdn.discordapp.com/attachments/805178727222083635/805181131498061824/image1.gif",
            "https://cdn.discordapp.com/attachments/805178727222083635/805181131984994314/image2.gif",
            "https://cdn.discordapp.com/attachments/805178727222083635/805181235239714906/image0.gif",
            "https://cdn.discordapp.com/attachments/805178727222083635/805181235621920798/image1.gif"]

        self.bot.sf9_inseong_gif = ["https://cdn.discordapp.com/attachments/805178651799977994/805181416026406962/image0.gif",
            "https://cdn.discordapp.com/attachments/805178651799977994/805181416702738492/image1.gif",
            "https://cdn.discordapp.com/attachments/805178651799977994/805181417331097611/image2.gif",
            "https://cdn.discordapp.com/attachments/805178651799977994/805181556821590056/image0.gif",
            "https://cdn.discordapp.com/attachments/805178651799977994/805181557085437972/image1.gif",
            "https://cdn.discordapp.com/attachments/805178651799977994/805181557434351626/image2.gif",
            "https://cdn.discordapp.com/attachments/805178651799977994/805181669496586250/image0.gif",
            "https://cdn.discordapp.com/attachments/805178651799977994/805181669841436692/image1.gif",
            "https://cdn.discordapp.com/attachments/805178651799977994/805181670168330250/image2.gif",
            "https://cdn.discordapp.com/attachments/805178651799977994/805181754066862100/image0.gif",
            "https://cdn.discordapp.com/attachments/805178651799977994/805181754410532874/image1.gif",
            "https://cdn.discordapp.com/attachments/805178651799977994/805181754674643004/image2.gif"]

        self.bot.sf9_jaeyoon_gif = ["https://cdn.discordapp.com/attachments/805178776748163082/805181897784295454/image0.gif",
            "https://cdn.discordapp.com/attachments/805178776748163082/805181898053517312/image1.gif",
            "https://cdn.discordapp.com/attachments/805178776748163082/805181984241483786/image0.gif",
            "https://cdn.discordapp.com/attachments/805178776748163082/805181984736936006/image1.gif",
            "https://cdn.discordapp.com/attachments/805178776748163082/805181985152303155/image2.gif",
            "https://cdn.discordapp.com/attachments/805178776748163082/805182076529541150/image0.gif",
            "https://cdn.discordapp.com/attachments/805178776748163082/805182077472866314/image2.gif",
            "https://cdn.discordapp.com/attachments/805178776748163082/805182129638080533/image0.gif",
            "https://cdn.discordapp.com/attachments/805178776748163082/805182129956323358/image1.gif"]

        self.bot.sf9_rowoon_gif = ["https://cdn.discordapp.com/attachments/805178992180199434/805182259409715260/image0.gif",
            "https://cdn.discordapp.com/attachments/805178992180199434/805182259958251580/image1.gif",
            "https://cdn.discordapp.com/attachments/805178992180199434/805182362165051392/image0.gif",
            "https://cdn.discordapp.com/attachments/805178992180199434/805182362659848212/image1.gif",
            "https://cdn.discordapp.com/attachments/805178992180199434/805182362991984680/image2.gif",
            "https://cdn.discordapp.com/attachments/805178992180199434/805182460564471818/image0.gif",
            "https://cdn.discordapp.com/attachments/805178992180199434/805182460890841128/image1.gif",
            "https://cdn.discordapp.com/attachments/805178992180199434/805182461230972959/image2.gif",
            "https://cdn.discordapp.com/attachments/805178992180199434/805182557951492147/image0.gif",
            "https://cdn.discordapp.com/attachments/805178992180199434/805182558526242856/image1.gif",
            "https://cdn.discordapp.com/attachments/805178992180199434/805182559012388864/image2.gif",
            "https://cdn.discordapp.com/attachments/805178992180199434/805182662767280209/image0.gif",
            "https://cdn.discordapp.com/attachments/805178992180199434/805182663136116796/image1.gif"]

        self.bot.sf9_taeyang_gif = ["https://cdn.discordapp.com/attachments/805179023558049852/805183900115533834/image0.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805183900594208781/image1.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805183901035266068/image2.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805184055095721994/image0.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805184055535599616/image1.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805184055838244944/image2.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805184156941680650/image0.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805184157441196102/image1.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805184158094721084/image2.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805184389406916618/image0.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805184391181631558/image1.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805184391596212284/image2.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805184492918538271/image0.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805184493295108106/image1.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805184493731446824/image2.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805184556482691122/image0.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805184556780093460/image1.gif",
            "https://cdn.discordapp.com/attachments/805179023558049852/805184557057703976/image2.gif",
            "https://tenor.com/view/yoo-taeyang-yangie-sf9-gif-18417580",
            "https://tenor.com/view/taeyang-sf9-sexy-dance-kpop-gif-12405955",
            "https://tenor.com/view/yoo-taeyang-sf9-hot-cute-dance-gif-14364411"]

        self.bot.sf9_youngbin_gif = ["https://cdn.discordapp.com/attachments/805179056093003816/805184741627133982/image0.gif",
            "https://cdn.discordapp.com/attachments/805179056093003816/805184742206734336/image1.gif",
            "https://cdn.discordapp.com/attachments/805179056093003816/805184742487490600/image2.gif",
            "https://cdn.discordapp.com/attachments/805179056093003816/805184983063986186/image0.gif",
            "https://cdn.discordapp.com/attachments/805179056093003816/805184983362437120/image1.gif",
            "https://cdn.discordapp.com/attachments/805179056093003816/805184993319714856/image0.gif",
            "https://cdn.discordapp.com/attachments/805179056093003816/805184993705197598/image1.gif",
            "https://cdn.discordapp.com/attachments/805179056093003816/805184994141536316/image2.gif",
            "https://cdn.discordapp.com/attachments/805179056093003816/805185046897885214/image0.gif",
            "https://cdn.discordapp.com/attachments/805179056093003816/805185047295950928/image1.gif"]

        self.bot.sf9_zuho_gif = ["https://cdn.discordapp.com/attachments/805179084044632115/805185277941383228/image0.gif",
            "https://cdn.discordapp.com/attachments/805179084044632115/805185362817056818/image0.gif",
            "https://cdn.discordapp.com/attachments/805179084044632115/805185505503346738/image0.gif",
            "https://cdn.discordapp.com/attachments/805179084044632115/805185506123317248/image1.gif",
            "https://cdn.discordapp.com/attachments/805179084044632115/805185506992062484/image2.gif",
            "https://cdn.discordapp.com/attachments/805179084044632115/805185588843118612/image0.gif",
            "https://cdn.discordapp.com/attachments/805179084044632115/805185589228863508/image1.gif",
            "https://cdn.discordapp.com/attachments/805179084044632115/805185589619327016/image2.gif",
            "https://cdn.discordapp.com/attachments/805179084044632115/805185677062570024/image0.gif",
            "https://cdn.discordapp.com/attachments/805179084044632115/805185677905100860/image1.gif",
            "https://cdn.discordapp.com/attachments/805179084044632115/805185678777384990/image2.gif",
            "https://cdn.discordapp.com/attachments/805179084044632115/805185691482849370/image0.gif"]
    #. VAV
        self.bot.vav_ace_gif = ["https://cdn.discordapp.com/attachments/796980132748722196/800508491717410846/image0.gif",
            "https://cdn.discordapp.com/attachments/796980132748722196/800508492192284682/image1.gif",
            "https://cdn.discordapp.com/attachments/796980132748722196/800508492661522442/image2.gif",
            "https://tenor.com/view/vav-ace-vav-ace-wooyoung-jang-wooyoung-gif-14503997",
            "https://tenor.com/view/vav-vav-ace-ace-wooyoung-jang-wooyoung-gif-14504066",
            "https://tenor.com/view/ace-wooyoung-jang-wooyoung-vav-vav-ace-gif-14503646",
            "https://tenor.com/view/ace-vav-vav-ace-wooyoung-jang-wooyoung-gif-14504374"]

        self.bot.vav_ayno_gif = ["https://cdn.discordapp.com/attachments/796980245760442378/800509463751819264/image0.gif",
            "https://cdn.discordapp.com/attachments/796980245760442378/800509464452399104/image1.gif",
            "https://cdn.discordapp.com/attachments/796980245760442378/800509464863965226/image2.gif",
            "https://tenor.com/view/vav-ayno-vav-ayno-ayno-vav-noh-yoonho-gif-15149242",
            "https://tenor.com/view/vav-ayno-vav-ayno-ayno-vav-noh-yoonho-gif-15434939",
            "https://tenor.com/view/vav-vav-ayno-ayno-noh-yoonho-yoonho-gif-14504494",
            "https://tenor.com/view/ayno-vav-vav-ayno-yoonho-noh-yoonho-gif-14504008"]

        self.bot.vav_baron_gif = ["https://cdn.discordapp.com/attachments/796980316736716831/800508768936394812/image1.gif",
            "https://tenor.com/view/baron-vav-vav-baron-vav-vav-baron-chunghyeop-gif-14503918",
            "https://tenor.com/view/baron-vav-vav-baron-vav-senorita-senorita-gif-14504156",
            "https://tenor.com/view/baron-vav-vav-baron-choi-chunghyeop-chunghyeop-gif-14504811",
            "https://tenor.com/view/baron-chunghyeop-choi-chunghyeop-vav-baron-thrilla-killa-gif-14503573",
            "https://tenor.com/view/baron-chunghyeop-choi-chunghyeop-vav-baron-thrilla-killa-gif-14503569"]

        self.bot.vav_jacob_gif = ["https://cdn.discordapp.com/attachments/796980439843602472/800508869553029200/image0.gif",
            "https://cdn.discordapp.com/attachments/796980439843602472/800508870204063764/image1.gif",
            "https://cdn.discordapp.com/attachments/796980439843602472/800508870556123166/image2.gif",
            "https://tenor.com/view/vav-jacob-jang-peng-rapper-vocalist-gif-17750522",
            "https://tenor.com/view/vav-jacob-vav-jacob-jacob-vav-zhang-peng-gif-15434946",
            "https://tenor.com/view/vav-jacob-vav-jacob-zhang-peng-gif-14504218",
            "https://tenor.com/view/vav-jacob-jang-peng-rapper-vocalist-gif-17750525"]

        self.bot.vav_lou_gif = ["https://cdn.discordapp.com/attachments/796980537432211456/800508974705147914/image0.gif",
            "https://cdn.discordapp.com/attachments/796980537432211456/800509040115056700/image0.gif",
            "https://tenor.com/view/vav-vav-lou-kim-hosung-hosung-lou-vav-gif-15149237",
            "https://tenor.com/view/vav-lou-vav-lou-kim-hosung-hosung-gif-14504275",
            "https://tenor.com/view/lou-vav-vav-lou-kim-hosung-hosung-gif-14504776",
            "https://tenor.com/view/vav-lou-vav-lou-hosung-kim-hosung-gif-14504107"]

        self.bot.vav_stvan_gif = ["https://cdn.discordapp.com/attachments/796980615927824464/800509156338434098/image0.gif",
            "https://cdn.discordapp.com/attachments/796980615927824464/800509156817764382/image1.gif",
            "https://tenor.com/view/st-van-vav-st-van-vav-kpop-lemon-gif-14797336",
            "https://tenor.com/view/stvan-geumhyuk-lee-geumhyuk-vav-st-van-vav-gif-14504733",
            "https://tenor.com/view/kcon2019japan-kcon-%EC%BC%80%EC%9D%B4%EC%BD%98-you-pointing-gif-14557924",
            "https://tenor.com/view/vav-stvan-lee-geumhyuk-geumhyuk-gif-16078577"]

        self.bot.vav_ziu_gif = ["https://cdn.discordapp.com/attachments/796980674002944020/800509274710999050/image0.gif",
            "https://cdn.discordapp.com/attachments/796980674002944020/800509275356397589/image1.gif",
            "https://cdn.discordapp.com/attachments/796980674002944020/800509750101278761/image0.gif",
            "https://tenor.com/view/ziu-vav-vav-ziu-heejun-park-heejun-gif-14504326",
            "https://tenor.com/view/ziu-vav-park-heejun-vav-ziu-vav-heejun-gif-14503691",
            "https://tenor.com/view/ziu-park-heejun-heejun-vav-vav-ziu-gif-14504182",
            "https://tenor.com/view/ziu-vav-vav-ziu-heejun-park-heejun-gif-14504018",
            "https://tenor.com/view/ziu-heejun-park-heejun-vav-vav-ziu-gif-14503557",
            "https://tenor.com/view/vav-ziu-vav-ziu-park-heejun-heejun-gif-14504226"]

    #.gif end

    @commands.command(aliases = ['p1h'])
    async def p1harmony(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [P1Harmony {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "intak":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Intak :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_intak_gif))
                await ctx.message.delete()
        elif arg == "jiung":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jiung :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_jiung_gif))
                await ctx.message.delete()
        elif arg == "jongseob":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jongseob :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_jongseob_gif))
                await ctx.message.delete()
        elif arg == "keeho":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Keeho :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_keeho_gif))
                await ctx.message.delete()
        elif arg == "soul":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Soul :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_soul_gif))
                await ctx.message.delete()
        elif arg == "theo":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Theo :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_theo_gif))
                await ctx.message.delete()

    @commands.command()
    async def the(self, ctx, boyz="boyz", *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [The Boyz {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "kevin":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Kevin :heart:')
                await ctx.send(random.choice(self.bot.theboyz_kevin_gif))
                await ctx.message.delete()
        elif arg == "sangyeon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Sangyeon :heart:')
                await ctx.send(random.choice(self.bot.theboyz_sangyeon_gif))
                await ctx.message.delete()
        elif arg == "jacob":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jacob :heart:')
                await ctx.send(random.choice(self.bot.theboyz_jacob_gif))
                await ctx.message.delete()
        elif arg == "younghoon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Younghoon :heart:')
                await ctx.send(random.choice(self.bot.theboyz_younghoon_gif))
                await ctx.message.delete()
        elif arg == "hyunjae":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Hyunjae :heart:')
                await ctx.send(random.choice(self.bot.theboyz_hyunjae_gif))
                await ctx.message.delete()
        elif arg == "juyeon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Juyeon :heart:')
                await ctx.send(random.choice(self.bot.theboyz_juyeon_gif))
                await ctx.message.delete()
        elif arg == "new":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about New :heart:')
                await ctx.send(random.choice(self.bot.theboyz_new_gif))
                await ctx.message.delete()
        elif arg == "q":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Q :heart:')
                await ctx.send(random.choice(self.bot.theboyz_q_gif))
                await ctx.message.delete()
        elif arg == "haknyeon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Haknyeon :heart:')
                await ctx.send(random.choice(self.bot.theboyz_haknyeon_gif))
                await ctx.message.delete()
        elif arg == "sunwoo":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Sunwoo :heart:')
                await ctx.send(random.choice(self.bot.theboyz_sunwoo_gif))
                await ctx.message.delete()
        elif arg == "eric":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Eric :heart:')
                await ctx.send(random.choice(self.bot.theboyz_eric_gif))
                await ctx.message.delete()

    @commands.command()
    async def sf9(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [SF9 {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "chani":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chani :heart:')
                await ctx.send(random.choice(self.bot.sf9_chani_gif))
                await ctx.message.delete()
        elif arg == "dawon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Dawon :heart:')
                await ctx.send(random.choice(self.bot.sf9_dawon_gif))
                await ctx.message.delete()
        elif arg == "hwiyoung":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Hwiyoung :heart:')
                await ctx.send(random.choice(self.bot.sf9_hwiyoung_gif))
                await ctx.message.delete()
        elif arg == "inseong":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Inseong :heart:')
                await ctx.send(random.choice(self.bot.sf9_inseong_gif))
                await ctx.message.delete()
        elif arg == "jaeyoon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jaeyoon :heart:')
                await ctx.send(random.choice(self.bot.sf9_jaeyoon_gif))
                await ctx.message.delete()
        elif arg == "rowoon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Rowoon :heart:')
                await ctx.send(random.choice(self.bot.sf9_rowoon_gif))
                await ctx.message.delete()
        elif arg == "taeyang" or arg == "yoo taeyang":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yoo Taeyang :heart:')
                await ctx.send(random.choice(self.bot.sf9_taeyang_gif))
                await ctx.message.delete()
        elif arg == "youngbin":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Youngbin :heart:')
                await ctx.send(random.choice(self.bot.sf9_youngbin_gif))
                await ctx.message.delete()
        elif arg == "zuho":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Zuho :heart:')
                await ctx.send(random.choice(self.bot.sf9_zuho_gif))
                await ctx.message.delete()

    @commands.command()
    async def vav(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [VAV {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "ace":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Ace :heart:')
                await ctx.send(random.choice(self.bot.vav_ace_gif))
                await ctx.message.delete()
        elif arg == "ayno":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Ayno :heart:')
                await ctx.send(random.choice(self.bot.vav_ayno_gif))
                await ctx.message.delete()
        elif arg == "baron":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Baron :heart:')
                await ctx.send(random.choice(self.bot.vav_baron_gif))
                await ctx.message.delete()
        elif arg == "jacob":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jacob :heart:')
                await ctx.send(random.choice(self.bot.vav_jacob_gif))
                await ctx.message.delete()
        elif arg == "lou":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Lou :heart:')
                await ctx.send(random.choice(self.bot.vav_lou_gif))
                await ctx.message.delete()
        elif arg == "st. van" or arg == "stvan" or arg == "st van" or arg == "st.van":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about St. Van :heart:')
                await ctx.send(random.choice(self.bot.vav_stvan_gif))
                await ctx.message.delete()
        elif arg == "ziu":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Ziu :heart:')
                await ctx.send(random.choice(self.bot.vav_ziu_gif))
                await ctx.message.delete()

    @commands.command()
    async def astro(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Astro {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "eunwoo":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Eunwoo :heart:')
                await ctx.send(random.choice(self.bot.astro_eunwoo_gif))
                await ctx.message.delete()
        elif arg == "mj":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about MJ :heart:')
                await ctx.send(random.choice(self.bot.astro_mj_gif))
                await ctx.message.delete()

def setup(client):
    client.add_cog(BGS(client))