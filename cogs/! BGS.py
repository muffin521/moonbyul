import discord, random, datetime
from discord.ext import commands
from datetime import datetime
from typing import List

#//servers
luminary = 758468592957521972

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574



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
    #. Cravity
        self.bot.cravity_serim_gif = ["https://tenor.com/view/park-serim-cravity-starship-entertainment-break-all-the-rules-teaser-gif-16853031",
            "https://tenor.com/view/cravity-serim-park-serim-leader-rapper-gif-17969322",
            "https://tenor.com/view/serim-cravity-serim-park-serim-nervous-serim-gif-18679099",
            "https://tenor.com/view/cravity-serim-park-serim-leader-rapper-gif-17969326",
            "https://tenor.com/view/serim-park-serim-cravity-gif-17969342",
            "https://tenor.com/view/cravity-serim-park-serim-starship-entertainment-kpop-gif-16609570",
            "https://tenor.com/view/serim-park-serim-cravity-gif-17969345",
            "https://tenor.com/view/cravity-serim-park-serim-leader-rapper-gif-17969325",
            "https://tenor.com/view/cravity-serim-park-serim-leader-rapper-gif-17969321",
            "https://tenor.com/view/cravity-serim-park-serim-park-wonjin-gif-20152184",
            "https://tenor.com/view/cravity-starship-entertainment-%ED%81%AC%EB%9E%98%EB%B9%84%ED%8B%B0-kpop-gif-16902247",
            "https://tenor.com/view/park-serim-cravity-serim-gif-17969336",
            "https://tenor.com/view/serim-park-serim-cravity-gif-17969343",
            "https://tenor.com/view/cravity-serim-park-serim-leader-rapper-gif-17969327",
            "https://tenor.com/view/serim-park-serim-cravity-gif-17969340",
            "https://tenor.com/view/serim-park-serim-cravity-gif-17969349",
            "https://tenor.com/view/serim-cravity-parkserim-gif-20463805",
            "https://tenor.com/view/serim-cravity-parkserim-gif-20463809",
            "https://tenor.com/view/park-serim-serim-cravity-gif-17969284",
            "https://64.media.tumblr.com/79c05ab6c54f69c9248f6fe8b1512298/fded38ccaabae57f-49/s500x750/e44d1d611338e6090d9aa59b133854aeb7b92933.gif",
            "https://64.media.tumblr.com/4a0543f7bb55a220ee02d7d24ca66b34/f7491ee6926fd2bc-70/s400x600/f0ea1b31a17bcb2d1b7e06f70403175cf67d5dfb.gif",
            "https://i.pinimg.com/originals/31/d4/58/31d458df3408a1fbc6e1381007593f10.gif",
            "https://64.media.tumblr.com/6ec7d51e16053aa1abe9c09741e295cd/258e062d66926837-b8/s400x600/4fec97884b5bcf808caa503706b95a600dd28c19.gif",
            "https://64.media.tumblr.com/4b8eb16fc8a3a9e0cc7a2df1708edfc6/9f1511fea0329cb1-23/s400x600/13396b473eba71aaae4683cf2545ae6cefca2599.gif"]

        self.bot.cravity_allen_gif = ["https://tenor.com/view/cravity-allen-allen-ma-rapper-starship-entertainment-gif-16609568",
            "https://tenor.com/view/cravity-allen-allen-ma-rapper-starship-entertainment-gif-17437665",
            "https://tenor.com/view/cravity-allen-allen-ma-rapper-starship-entertainment-gif-16609572",
            "https://tenor.com/view/allen-ma-ma-allen-cravity-allen-cravity-allen-gif-18324779",
            "https://tenor.com/view/cravity-allen-kpop-gif-20503359",
            "https://tenor.com/view/allen-ma-cravity-starship-entertainment-break-all-the-rules-teaser-gif-16853025",
            "https://tenor.com/view/cravity-kpop-my-turn-allen-allen-ma-gif-20013025",
            "https://tenor.com/view/allen-cravity-gif-18595518",
            "https://tenor.com/view/allen-cravity-vicsgif-gif-19764935",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19768114",
            "https://tenor.com/view/cravity-allen-allen-ma-rapper-starship-entertainment-gif-16883683",
            "https://tenor.com/view/allen-allen-ma-cravity-twerk-twerking-gif-18512517",
            "https://64.media.tumblr.com/d7654f29f9808b3bfe36b673ae51f6d3/7f1e61f797a0e6b6-08/s540x810/92c67b022d12e03654e2cb5a5f2054b82c7ac86e.gif",
            "https://64.media.tumblr.com/8ca7f5a3e9841444afa829672e20b2d2/10831a9fb6f6373f-d6/s500x750/94a32d14c7be767fe9d7fb23a3109831886827f9.gif",
            "https://64.media.tumblr.com/8dd4549ff1dcf03080e2dabd03eaff82/ef0ad708c7fea194-ad/s500x750/a5b178c48a5d3667ac2eb23992343cf55f901282.gif",
            "https://64.media.tumblr.com/a41f0cd6cb6f83d56e0b2c2f36c8c979/cd9ef75316ec493c-a9/s540x810/06530900d6a8f30585f784a8053e2f3aa241386e.gif",
            "https://64.media.tumblr.com/66610b180b5c5a792acec64a24b3d94e/ef0ad708c7fea194-18/s500x750/dda88ce111f46c0ba33b3fa20c099887a0d2a89a.gif",
            "https://i.pinimg.com/originals/b8/eb/f9/b8ebf9e7b432f518b0ffd6665c5b0cc4.gif",
            "https://64.media.tumblr.com/514ba1b19705dbadba0cd5e48f4b8ed9/ef0ad708c7fea194-c6/s500x750/262ed7b7e91879c04024a2ee07cdc219bb08bf63.gif",
            "https://64.media.tumblr.com/313ebfc24c764619bd66f188aa929b89/ca02e3ab13aad0c6-0b/s640x960/85acc1f2157f18a33b1e6fd09cc77de625ad06d8.gif"]

        self.bot.cravity_jungmo_gif = ["https://tenor.com/view/jungmo-koo-jungmo-cravity-gif-17968742",
            "https://tenor.com/view/cravity-koo-jungmo-jungmo-gif-17968747",
            "https://tenor.com/view/jungmo-smirk-jungmo-cravity-%EC%A0%95%EB%AA%A8-cravity-jungmo-gif-19791538",
            "https://tenor.com/view/jungmo-fall-jungmo-%EC%A0%95%EB%AA%A8-cravity-cravity-jungmo-gif-19791531",
            "https://tenor.com/view/jungmo-cravity-cloud9-heart-kpop-gif-17562285",
            "https://tenor.com/view/jungmo-cravity-kpop-finger-heart-handsome-gif-17167742",
            "https://tenor.com/view/jungmo-jungmo-smile-jungmo-cute-jungmo-cravity-cravity-gif-18356279",
            "https://tenor.com/view/koo-jungmo-jungmo-cravity-gif-17968745",
            "https://tenor.com/view/jungmo-koo-jungmo-cravity-dab-dabbing-gif-18932200",
            "https://tenor.com/view/jungmo-smirk-cravity-cravity-jungmo-%EC%A0%95%EB%AA%A8-gif-19791529",
            "https://tenor.com/view/koo-jungmo-jungmo-cravity-gif-17969281",
            "https://tenor.com/view/cravity-starship-entertainment-%ED%81%AC%EB%9E%98%EB%B9%84%ED%8B%B0-kpop-gif-16902242",
            "https://tenor.com/view/koo-jungmo-jungmo-cravity-gif-17968748",
            "https://tenor.com/view/cravity-starship-entertainment-%ED%81%AC%EB%9E%98%EB%B9%84%ED%8B%B0-kpop-gif-16902248",
            "https://tenor.com/view/cravity-starship-entertainment-%ED%81%AC%EB%9E%98%EB%B9%84%ED%8B%B0-kpop-jungmoo-gif-16902235",
            "https://tenor.com/view/cravity-jungmo-gif-20503308",
            "https://tenor.com/view/jungmo-koo-cravity-kpop-gif-17998113",
            "https://tenor.com/view/cravity-starship-entertainment-%ED%81%AC%EB%9E%98%EB%B9%84%ED%8B%B0-kpop-jungmo-gif-16902236",
            "https://tenor.com/view/koo-jungmo-cravity-starship-entertainment-break-all-the-rules-teaser-gif-16853038",
            "https://tenor.com/view/cravity-starship-entertainment-%ED%81%AC%EB%9E%98%EB%B9%84%ED%8B%B0-kpop-smile-gif-16902231",
            "https://tenor.com/view/cravity-starship-entertainment-%ED%81%AC%EB%9E%98%EB%B9%84%ED%8B%B0-kpop-gif-16902245",
            "https://tenor.com/view/jeongmo-jungmo-koo-jeongmo-starship-produce-x101-gif-14407608",
            "https://tenor.com/view/koo-jeongmo-koo-jungmo-produce-x101-cute-gif-14543773",
            "https://tenor.com/view/jeongmo-jungmo-koo-jeongmo-koo-jungmo-goojeongmo-gif-14697789",
            "https://tenor.com/view/jeongmo-jungmo-koo-jeongmo-koo-jungmo-goojeongmo-gif-14697787",
            "https://tenor.com/view/jeongmo-jungmo-koo-jungmo-koo-jeongmo-produce-x101-gif-14407591",
            "https://tenor.com/view/cute-jungmo-koo-jeongmo-goo-jeongmo-koo-jungmo-gif-14357045",
            "https://tenor.com/view/jeongmo-koo-jeongmo-koo-jungmo-jungmo-produce-x101-gif-14543772",
            "https://64.media.tumblr.com/e2fb5446d0db6dcfdf377548e223cbf9/ccdf9243be5c2bc3-fe/s540x810/2fd7c40f70826ddb7b04f4b7dfdac8a6e79fb6ce.gif",
            "https://i.pinimg.com/originals/2e/9c/cd/2e9ccd41309402ebb3b58425ad516789.gif",
            "https://64.media.tumblr.com/b60e4cc04c16b0412a3455a4fca72dd5/2ea9f724fa44d14d-53/s400x600/b7d8c62280dbec071c2d984454679ecd0441861d.gif",
            "https://64.media.tumblr.com/64ade4718cc317650e3e7309a6255ff1/f7491ee6926fd2bc-13/s400x600/184e7e6e60ebad8d7729259ba36693cbf972950c.gif"]

        self.bot.cravity_woobin_gif = ["https://tenor.com/view/seo-woobin-woobin-cravity-starship-entertainment-break-all-the-rules-gif-16853030",
            "https://tenor.com/view/cravity-serim-allen-jungmo-woobin-gif-17558271",
            "https://tenor.com/view/cravity-kpop-my-turn-woobin-seo-woobin-gif-20013026",
            "https://tenor.com/view/woobin-cravity-kpop-seo-ruby-gif-20423137",
            "https://tenor.com/view/woobin-kpop-cravity-ruby-seo-gif-20422893",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19768111",
            "https://tenor.com/view/cravity-ruby-woobin-gif-19670304",
            "https://64.media.tumblr.com/bfa6a1222994e6bc0fb4392423c1e58e/42cff016837f9236-dd/s400x600/3fbaf5c171b0b272bbac44f8d5f184a7875c875d.gif",
            "https://thumbs.gfycat.com/SilverBraveCormorant-size_restricted.gif",
            "https://64.media.tumblr.com/575a4eab21c52a6301ebb0b61b8cda86/42cff016837f9236-0f/s250x400/bd5bc9ca1406d89b064e28f5c9ecaca8321880ee.gif",
            "https://64.media.tumblr.com/ac13578fcf62a2b6fde196d704494603/29b0efd8de9fb3b1-39/s500x750/ece01cdef112432933f9b2f30946cd17041d2e57.gif",
            "https://64.media.tumblr.com/934ba262f5a7f7fc2b752ba3d3d4b91f/29b0efd8de9fb3b1-8b/s500x750/2dc83a85ad5648c0d7ce1637df5e31c0aab83a65.gif",
            "https://64.media.tumblr.com/3e6ab99e3791c7a7beb78f5195be0749/29b0efd8de9fb3b1-f5/s500x750/53a749f8fbec7118829fbb1309d1408b2f954c34.gif",
            "https://64.media.tumblr.com/791f7b2223f6479e16de99ac463ce77f/dbfdac3e846b5e8b-be/s400x600/0add976fbe46e0e365a473890d3b9ed15baa3662.gif",
            "https://64.media.tumblr.com/0245cc028cb599ebd779e1fff1dc18f3/9aa23b09ef4b53ec-84/s400x600/120838587929880a5056d31110ed5b0331b2c2e4.gif",
            "https://64.media.tumblr.com/24d64f90da26582fd80ef74023d6416e/708bddfe8a7d9349-3b/s500x750/7d58da9cf74de6d043ae39262c1aa0613ce484a5.gif",
            "https://64.media.tumblr.com/07f1e4caebc32f35bd91fec5ea5845d4/99d6d2b1cb6e69bc-35/s400x600/39b366b489a8e16c6436120e6cf94742d72dfa1b.gif",
            "https://64.media.tumblr.com/d15bd66787dcfdf1beff2b4b6c58926e/10df00a9ff005afd-2f/s640x960/071973a889637e8743cc77b7d87b3ecdfa7d9d22.gif",
            "https://64.media.tumblr.com/5450d869d217cfcc5cea8671e644f5fe/b5ed03661f321267-e9/s250x400/8656698a5ea1f5ba2cbadb0c74a83aea5c8298af.gif",
            "https://64.media.tumblr.com/26bcda0bc9a8be85283f211453c0f814/2032db3ed624cdfc-7e/s500x750/35a7e8d216588ccb2082da80f104f0b6628ef172.gif",
            "https://64.media.tumblr.com/d726e83c1dc062f29c662d9d01f0ee88/2c7d2776a7f0407b-5a/s500x750/2ca6a11f2fb3a65976217e9295666d4f6c83e300.gif"]

        self.bot.cravity_wonjin_gif = ["https://tenor.com/view/cravity-wonjin-ham-won-jin-vocalist-starship-entertainment-gif-17966683",
            "https://tenor.com/view/cravity-wonjin-ham-won-jin-vocalist-starship-entertainment-gif-17966592",
            "https://tenor.com/view/cravity-wonjin-ham-won-jin-vocalist-starship-entertainment-gif-17966688",
            "https://tenor.com/view/cravity-wonjin-ham-won-jin-vocalist-starship-entertainment-gif-17966686",
            "https://tenor.com/view/cravity-wonjin-ham-won-jin-vocalist-starship-entertainment-gif-17966679",
            "https://tenor.com/view/wonjin-gif-18871967",
            "https://tenor.com/view/cravity-wonjin-ham-won-jin-vocalist-starship-entertainment-gif-17966703",
            "https://tenor.com/view/cravity-ham-wonjin-wonjin-kpop-cute-gif-16853023",
            "https://tenor.com/view/cravity-wonjin-ham-won-jin-vocalist-starship-entertainment-gif-17966596",
            "https://tenor.com/view/cravity-wonjin-ham-won-jin-vocalist-starship-entertainment-gif-17966603",
            "https://tenor.com/view/cravity-wonjin-ham-won-jin-starship-entertainment-kpop-gif-16609574",
            "https://tenor.com/view/%E0%B8%A7%E0%B8%AD%E0%B8%99%E0%B8%88%E0%B8%B4%E0%B8%99-what-sad-%E0%B9%80%E0%B8%A8%E0%B8%A3%E0%B9%89%E0%B8%B2-wonjin-gif-14805661",
            "https://tenor.com/view/cravity-wonjin-gif-19950389",
            "https://tenor.com/view/wonjin-cravity-kpop-thug-life-shades-gif-17664022",
            "https://tenor.com/view/ham-wonjin-produce-x101-cute-red-lips-gif-14806688",
            "https://tenor.com/view/cravity-wonjin-ham-won-jin-vocalist-starship-entertainment-gif-17966595",
            "https://tenor.com/view/wonjin-ham-wonjin-starship-starship-entertainment-gif-14351022",
            "https://tenor.com/view/ham-wonjin-sad-stare-gif-14806036",
            "https://tenor.com/view/cravity-wonjin-ham-won-jin-vocalist-starship-entertainment-gif-17966594",
            "https://tenor.com/view/ham-wonjin-cute-kpop-produce101-gif-14806594",
            "https://tenor.com/view/cravity-wonjin-ham-won-jin-vocalist-starship-entertainment-gif-17966598",
            "https://tenor.com/view/cravity-wonjin-ham-won-jin-vocalist-starship-entertainment-gif-17966693",
            "https://tenor.com/view/ham-wonjin-produce-x101-dance-gif-14806689",
            "https://tenor.com/view/ham-wonjin-kpop-produce101-gif-14806770",
            "https://thumbs.gfycat.com/NastyScarceIndri-max-1mb.gif",
            "https://64.media.tumblr.com/e04387682b6803dbe197165f58c4c0b9/2c7d2776a7f0407b-32/s1280x1920/b595c1af266c0527522dc209935423b4815ed422.gif",
            "https://blog.kakaocdn.net/dn/VPDFY/btq0iAHxxMO/iW99KifX9bDyeyow0ZqEd0/img.gif"]

        self.bot.cravity_minhee_gif = ["https://tenor.com/view/cravity-minhee-kang-minhee-tbzmoncraviteen-x1-gif-18931955",
            "https://tenor.com/view/cravity-minhee-kang-min-hee-starship-entertainment-kpop-gif-16609569",
            "https://tenor.com/view/x1-minhee-kpop-dance-gif-14841162",
            "https://tenor.com/view/minhee-cravity-minhee-dance-kang-minhee-x1-gif-18553675",
            "https://tenor.com/view/cravity-minhee-kang-min-hee-starship-entertainment-kpop-gif-16609571",
            "https://tenor.com/view/cravity-minhee-kang-min-hee-vocalist-starship-entertainment-gif-17659302",
            "https://tenor.com/view/minhee-cravity-starship-entertainment-%ED%81%AC%EB%9E%98%EB%B9%84%ED%8B%B0-kpop-gif-16902228",
            "https://tenor.com/view/cravity-minhee-kang-min-hee-vocalist-starship-entertainment-gif-17562245",
            "https://tenor.com/view/minhee-kang-minhee-cravity-gif-20355592",
            "https://tenor.com/view/cravity-starship-entertainment-%ED%81%AC%EB%9E%98%EB%B9%84%ED%8B%B0-kpop-minhee-gif-16902239",
            "https://tenor.com/view/minhee-kang-minhee-cravity-x1-gif-19974321",
            "https://tenor.com/view/kang-min-hee-cravity-min-hee-talking-cute-gif-17043118",
            "https://tenor.com/view/minhee-cravity-kikabae-gif-19444322",
            "https://tenor.com/view/minhee-kang-minhee-cravity-gif-19313838",
            "https://tenor.com/view/produce-x101-minhee-kang-minhee-surprised-gif-14594346",
            "https://tenor.com/view/x1-minhee-kang-minhee-kpop-gif-14841176",
            "https://tenor.com/view/minhee-cravity-smile-kang-minhee-x1-gif-19946460",
            "https://tenor.com/view/x1-minhee-kang-minhee-kpop-gif-14841155",
            "https://tenor.com/view/x1-minhee-kang-minhee-gif-14990590",
            "https://tenor.com/view/x1-minhee-kang-minhee-mini-kang-mini-gif-15046757",
            "https://tenor.com/view/produce-x101-minhee-kang-minhee-cute-smile-gif-14598580",
            "https://tenor.com/view/x1-one-it-minhee-kang-minhee-kpop-gif-14972843",
            "https://tenor.com/view/minhee-cravity-minhee-reaction-minhee-gif-minhee-cravity-gif-19389640",
            "https://tenor.com/view/minhee-kang-cravity-x1-jaemin-gif-17589371",
            "https://tenor.com/view/x1-one-it-minhee-kang-minhee-kpop-gif-14972848",
            "https://tenor.com/view/kang-minhee-produce-x101-produce-x-cute-dance-gif-14264523",
            "https://tenor.com/view/minhee-kang-cute-jaemin-woobin-gif-17589238",
            "https://tenor.com/view/x1-starship-kang-minhee-produce-x101-kpop-gif-14877975",
            "https://tenor.com/view/x1-minhee-kang-kpop-cute-gif-15471747",
            "https://tenor.com/view/x1-starship-kang-minhee-produce-x101-clapping-gif-14877978",
            "https://tenor.com/view/x1-starship-kang-minhee-minhee-produce-x101-gif-14877970",
            "https://tenor.com/view/starship-clap-smile-kang-minhee-produce-x101-gif-14520289",
            "https://tenor.com/view/cravity-kang-minhee-minhee-x1minhee-minhee-cravity-gif-18969870",
            "https://tenor.com/view/x1-minhee-kang-minhee-smile-cute-gif-14988961",
            "https://64.media.tumblr.com/1201bc690a47a947565e85318bbf0d53/dc3cf1cf4d15f595-ad/s2048x3072/63c269b0d0dd476698fd0d8cc0fb1fb4747a7790.gif",
            "https://64.media.tumblr.com/634fa4c5145db09ba655bcf89f724361/2e1b490040d16b4e-52/s540x810/f508bf975aa7ae26ea40a57cd69a67ce1b1b49d4.gif",
            "https://data.whicdn.com/images/335717726/original.gif"]

        self.bot.cravity_hyeongjun_gif = ["https://tenor.com/view/hyeongjun-cravity-song-hyeongjun-gif-20381325",
            "https://tenor.com/view/hyeongjun-song-hyeongjun-hyeongjun-cravity-cravity-hyeongjun-cravity-gif-18259085",
            "https://tenor.com/view/cravity-hyeongjun-song-hyeong-jun-vocalist-starship-entertainment-gif-16883679",
            "https://tenor.com/view/hyeongjun-song-hyeongjun-cravity-x1-gif-19974424",
            "https://tenor.com/view/cravity-song-hyeongjun-x1-kpop-cute-gif-16616306",
            "https://tenor.com/view/cravity-hyeongjun-song-hyeong-jun-vocalist-starship-entertainment-gif-16883678",
            "https://tenor.com/view/hyeongjun-kpop-cravity-gif-20503351",
            "https://tenor.com/view/song-hyeongjun-hyeongjun-hyeongjun-cravity-hyeongjun-x1-cravity-gif-18259098",
            "https://tenor.com/view/hyeongjun-cravity-song-hyeongjun-gif-20379960",
            "https://tenor.com/view/hyeongjun-song-hyeongjun-cravity-x1-gif-20352811",
            "https://tenor.com/view/hyeongjun-cravity-song-hyeongjun-gif-20325014",
            "https://tenor.com/view/hyeongjun-song-hyeongjun-cravity-x1-gif-19974353",
            "https://tenor.com/view/hyeongjun-song-hyeongjun-cravity-x1-gif-19922464",
            "https://tenor.com/view/x1-song-hyeongjun-cravity-starship-entertainment-break-all-the-rules-gif-16853028",
            "https://tenor.com/view/hyeongjun-%ED%81%AC%EB%9E%98%EB%B9%84%ED%8B%B0-%ED%98%95%EC%A4%80-%ED%81%AC%EB%9E%98%EB%B9%84%ED%8B%B0%ED%98%95%EC%A4%80-cravity-gif-19872346",
            "https://tenor.com/view/hyeongjun-cravity-x1-song-hyeongjun-gif-20314246",
            "https://tenor.com/view/hyeongjun-dancing-christmas-happy-hyeongjun-christmas-%ED%81%AC%EB%9E%98%EB%B9%84%ED%8B%B0-gif-19872226",
            "https://tenor.com/view/cravity-starship-entertainment-%ED%81%AC%EB%9E%98%EB%B9%84%ED%8B%B0-kpop-kiss-gif-16902232",
            "https://tenor.com/view/hyeongjun-cravity-confused-%ED%81%AC%EB%9E%98%EB%B9%84%ED%8B%B0-%ED%98%95%EC%A4%80-gif-19896368",
            "https://tenor.com/view/hyeongjun-song-hyeongjun-starship-entertainment-cravity-dance-gif-17712631",
            "https://tenor.com/view/cravity-hyeongjun-gif-19861360",
            "https://tenor.com/view/hyeongjun-cravity-gif-20390143",
            "https://tenor.com/view/cravity-hyeongjun-song-hyeong-jun-vocalist-starship-entertainment-gif-16883684",
            "https://tenor.com/view/cravity-song-hyeongjun-x1-kpop-cute-gif-16616304",
            "https://tenor.com/view/hyeongjun-hyungjun-song-hyeongjun-song-hyungjun-produce-x101-gif-14354307",
            "https://tenor.com/view/hyeongjun-cravity-song-hyeongjun-gif-20390266",
            "https://tenor.com/view/cravity-hyeongjun-song-hyeong-jun-vocalist-starship-entertainment-gif-17731121",
            "https://tenor.com/view/x1-hyeongjun-cute-gif-15046756",
            "https://tenor.com/view/hyeongjun-cravity-song-hyeongjun-x1-gif-20325044",
            "https://tenor.com/view/hyeongjun-song-cravity-x1-strawberrykyuns-gif-20561303",
            "https://tenor.com/view/hyeongjun-song-hyeongjun-cravity-x1-gif-19974395",
            "https://tenor.com/view/song-hyeongjun-song-hyungjun-starship-produce-x101-gif-14362980",
            "https://tenor.com/view/song-hyeongjun-x1-cravity-kpop-cute-gif-16972735",
            "https://tenor.com/view/x1-song-hyeongjun-hyeongjun-hyeongjun-cute-aegyo-gif-18878540"]

        self.bot.cravity_taeyoung_gif = ["https://tenor.com/view/taeyoung-cravity-kim-taeyoung-cute-gif-17966307",
            "https://tenor.com/view/cravity-taeyoung-kim-tae-young-vocalist-starship-entertainment-gif-17965646",
            "https://tenor.com/view/%ED%83%9C%EC%98%81-taeyoung-taeyoung-cravity-cravity-nadeull-gif-20098871",
            "https://tenor.com/view/kim-taeyoung-smile-cravity-x1-kpop-gif-16616302",
            "https://tenor.com/view/kim-taeyoung-smile-cravity-x1-kpop-gif-16616303",
            "https://tenor.com/view/cravity-taeyoung-kim-taeyoung-dog-kpop-gif-17965616",
            "https://tenor.com/view/taeyoung-kim-taeyoung-cravity-kpop-handsome-gif-17965611",
            "https://tenor.com/view/taeyoung-cravity-kim-taeyoung-kitty-cute-gif-17966304",
            "https://tenor.com/view/taeyoung-kim-taeyoung-cravity-kpop-handsome-gif-17965602",
            "https://tenor.com/view/cravity-taeyoung-kim-tae-young-vocalist-starship-entertainment-gif-16883681",
            "https://tenor.com/view/taeyoung-youngtae-my-turn-cravity-kim-taeyoung-gif-20038732",
            "https://tenor.com/view/cravity-taeyoung-gif-19853718",
            "https://tenor.com/view/kpop-cravity-my-turn-taeyoung-youngtae-gif-20012907",
            "https://tenor.com/view/taeyoung-kim-taeyoung-cravity-kpop-handsome-gif-17965608",
            "https://tenor.com/view/kim-taeyoung-taeyoung-cravity-kpop-handsome-gif-17965612",
            "https://tenor.com/view/cravity-taeyoung-cravity-taeyoung-gif-18440673",
            "https://tenor.com/view/taeyoung-youngtae-cravity-gif-19358980",
            "https://tenor.com/view/cravity-kpop-cloud9-kim-taeyoung-youngtae-gif-20656180",
            "https://tenor.com/view/taeyoung-taeyoung-cravity-taeyoung-heart-cravity-nadeull-gif-20098864",
            "https://tenor.com/view/kim-taeyoung-youngtae-taeyoung-cravity-cute-gif-20014222",
            "https://tenor.com/view/kpop-cravity-my-turn-taeyoung-youngtae-gif-20012915",
            "https://tenor.com/view/kim-taeyoung-cravity-starship-entertainment-break-all-the-rules-teaser-gif-16853029",
            "https://tenor.com/view/taeyoung-cravity-ending-fairy-my-turn-gif-20457170",
            "https://tenor.com/view/youngtae-taeyoung-cravity-shock-kimtaeyoung-gif-19935846",
            "https://tenor.com/view/cravity-taeyoung-gif-20379246"]

        self.bot.cravity_seongmin_gif = ["https://tenor.com/view/ahn-seongmin-seongmin-cravity-kpop-smile-gif-17964356",
            "https://tenor.com/view/cravity-seongmin-ahn-seong-min-vocalist-maknae-gif-17958501",
            "https://tenor.com/view/seungmin-cravity-ahn-seongmin-kpop-cute-gif-16616299",
            "https://tenor.com/view/cravity-seongmin-ahn-seong-min-vocalist-maknae-gif-17958504",
            "https://tenor.com/view/ahn-seongmin-seongmin-cravity-starship-entertainment-kpop-gif-16853027",
            "https://tenor.com/view/ahn-seongmin-seongmin-cravity-gif-17969278",
            "https://tenor.com/view/cravity-seongmin-ahn-seong-min-vocalist-maknae-gif-17519249",
            "https://tenor.com/view/cravity-seongmin-ahn-seong-min-vocalist-maknae-gif-17958332",
            "https://tenor.com/view/seongmin-ahn-seongmin-cravity-cute-kpop-gif-17964359",
            "https://tenor.com/view/cravity-seongmin-ahn-seong-min-vocalist-maknae-gif-17958499",
            "https://tenor.com/view/seongmin-ahn-seongmin-cravity-ottoke-song-cute-gif-16904162",
            "https://tenor.com/view/cravity-seongmin-ahn-seong-min-vocalist-maknae-gif-17958440",
            "https://tenor.com/view/cravity-kpop-cloud9-ahn-seongmin-seongmin-gif-20656198",
            "https://tenor.com/view/cravity-seongmin-ahn-seong-min-vocalist-maknae-gif-17958488",
            "https://tenor.com/view/cravity-seongmin-ahn-seong-min-vocalist-maknae-gif-17958485",
            "https://tenor.com/view/cravity-kpop-cloud9-ahn-seongmin-seongmin-gif-20656177",
            "https://tenor.com/view/cravity-kpop-my-turn-seongmin-ahn-seongmin-gif-20013023",
            "https://tenor.com/view/ahn-seongmin-cravity-starship-entertainment-break-all-the-rules-teaser-gif-16853037",
            "https://tenor.com/view/seongmin-luvity-cravity-gif-20048812",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19768137",
            "https://tenor.com/view/cravity-seongmin-reaction-gif-19651294",
            "https://tenor.com/view/seungmin-cravity-ahn-seongmin-kpop-cute-gif-16616300",
            "https://tenor.com/view/ahn-seongmin-cravity-seongmin-bunny-cute-gif-17964361",
            "https://tenor.com/view/ahn-seongmin-cravity-kpop-cute-handsome-gif-17602528",
            "https://tenor.com/view/cravity-seonglem-seongmin-hyeongjun-gif-20153978",
            "https://tenor.com/view/seongmin-ahn-seongmin-cravity-gif-19167335",
            "https://tenor.com/view/kpop-cravity-my-turn-seongmin-ahn-seongmin-gif-20012912",
            "https://tenor.com/view/seongmin-cravity-vicsgif-gif-20019573",
            "https://tenor.com/view/cravity-seongmin-ahn-seongmin-gif-19851238",
            "https://tenor.com/view/cravity-kpop-my-turn-seongmin-ahn-seongmin-gif-20013057",
            "https://tenor.com/view/cravity-serim-allen-jungmo-woobin-gif-17558276"]
    #. EXO
        self.bot.exo_kai_gif = ["https://tenor.com/view/kim-kai-gif-18024912",
            "https://tenor.com/view/exo-kai-remove-shirt-gif-15477423",
            "https://tenor.com/view/kai-exo-model-face-gif-14518959",
            "https://tenor.com/view/kim-kai-gif-18025227",
            "https://tenor.com/view/kai-exo-love-shot-wink-sexy-gif-13161566",
            "https://tenor.com/view/exo-kai-christmas-cute-gif-15886415",
            "https://tenor.com/view/andante-jongin-kai-shikyung-exo-gif-10119734",
            "https://tenor.com/view/andante-jongin-kai-shikyung-exo-gif-10119734",
            "https://tenor.com/view/exo-kai-pose-handsome-kpop-gif-15772262",
            "https://tenor.com/view/love-heart-kai-exo-jongin-gif-9375449",
            "https://tenor.com/view/kai-exo-cute-gif-9956739",
            "https://tenor.com/view/kai-exo-ice-cream-eat-happy-gif-5037456",
            "https://tenor.com/view/jongin-kai-exo-wave-smile-gif-9375409",
            "https://tenor.com/view/exo-exo-kai-kai-gif-19601027",
            "https://tenor.com/view/kai-cute-gif-19869019",
            "https://64.media.tumblr.com/92e08d3cb6d3d3bc0e4168bb419612b3/763b277c97095470-94/s540x810/4e14a0a57119d9098d6c732255e4c7f9641eb989.gif",
            "https://i.pinimg.com/originals/c1/21/00/c1210014d73646125320286d376d9481.gif",
            "http://24.media.tumblr.com/975e810f5f205c78fc1ede79d07f031c/tumblr_mvhgk5LZCh1sw49f8o1_250.gif",
            "https://64.media.tumblr.com/d3c2f8f17530183eab992e3d417845e7/f80f7fa8f526396e-f5/s540x810/8d5be1f75c0a65e9eda14c741bc39e28aa3339b2.gif",
            "https://64.media.tumblr.com/ed54af035d652061359bcea0ea3e1e69/714d0d354d12c79a-1d/s540x810/4d43b51d704674558af2f07ed0f8016af7acd0a9.gif",
            "https://64.media.tumblr.com/395e7749ceb5002fb3ac6784dab8391f/714d0d354d12c79a-86/s540x810/a59d8ad394200c267d09500fef57710e9c4b59f1.gif",
            "https://64.media.tumblr.com/8fd8b82bfdbd03b8ea90445f887110bc/714d0d354d12c79a-6c/s540x810/7a51e11fd94f44da634548783cd4664c25a474d1.gif",
            "https://64.media.tumblr.com/7d6ad5046cd79443507fa6b6f71fc872/d1392d13e10beb04-11/s400x600/df3409c1276202945e3727efd7ad133209454835.gif",
            "https://64.media.tumblr.com/f9f59657cb0ebd02f3272d8ff7538ac9/0b06977d0ecb28e7-7b/s400x600/aaebc99d799260be4290a134768635dbb0d7b8b4.gif",
            "https://64.media.tumblr.com/9f079963f9445fdefde540a7e52ec334/ce6c5067ef0a775e-ad/s250x400/af236c919c88b078ec08ed2fe78c5726c03e9315.gif",
            "https://64.media.tumblr.com/fd2ebd74bc8b6b9b48a24be4dcecfcaf/ade40244846bf0e6-83/s400x600/8ffee8971c56934db121beeccf59d10721975d4c.gif",
            "https://64.media.tumblr.com/83c01be69a27c56b5ec68aa8f1d10367/1a81c84ab7dc18cc-7d/s250x400/cb296b4e546e1011811791cc8dc9806ad55454f7.gif",
            "https://66.media.tumblr.com/df01ac77966af691ba09e419a3fd6d64/3390969e7f44fb8c-48/s540x810/b0b1866ffdc30d518394f9266bada8282426144a.gif",
            "https://static.tumblr.com/c413c2a56293eece2fb7512dc14fdb42/s7oz85c/8YQow78v8/tumblr_static_tumblr_static__focused_v3.gif",
            "https://64.media.tumblr.com/93e69acf8af716ce8a5ed39e69a9420d/tumblr_p2g357Uqso1r3hdhfo1_r1_400.gif",
            "https://64.media.tumblr.com/9396c745c7ec77a4a4cb3764d9c6ddb5/tumblr_omim6tVhEA1r3hdhfo1_540.gif",
            "https://64.media.tumblr.com/507d71a00e1bed314653968c06e92f90/tumblr_pjskmaFnHx1uttdkc_400.gif",
            "https://64.media.tumblr.com/bc67632a1bec2e6c95de4eb2e277a41f/tumblr_pjskm5U1ER1uttdkc_400.gif",
            "https://64.media.tumblr.com/e34b4d0a09d8023304eafbdccd546ce0/3b9bd9c072f20d81-f4/s540x810/88174d37360f9a09ba3764da28f99ca6a243ba03.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/812081207998677002/0a1099a4-d70a-44bc-8ec0-510458b61b9b.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/812081318706806825/0ac8074f-b0f2-446f-8831-a6ecd37d58fb.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/812082428582559744/1bc303fd-8866-4fd8-8343-e3b5d086f231.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/812082515925925919/1d3b71de-38b8-4565-b87b-764444e5a81b.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/812082532010557490/1d45881d-0f99-442d-89da-0013664ff9e8.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/812082624251822090/1e8b3568-a771-4dd5-b8c2-2c78a8c415cf.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/812082844330491954/2aa497ad-0e52-42db-947e-a8ee1a6a229e.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/812083146794598430/2ef8ebe0-0efc-4569-9ccf-f67b519c4181.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/812084091599323206/4c80aa10-47b0-433a-b77b-8a29557cfccd.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/812084551815528518/5a1082cb-959d-4791-a96a-3d0b71f3c09e.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/812084851544293376/5c17034e-9f96-4c0d-9d4c-b108d146abff.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/812085044763951164/5ea7a890-99a2-48cc-a76d-d1539be9be81.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/812085186996731954/6b32bf6f-52fa-465d-af59-32ecb7ccf283.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/812085825985577001/7c793086-658e-4980-a1dc-87712ca177bd.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/812085871381184572/7d9b9479-9a87-4ba9-aec2-9e4ea8ae2d39.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/815305990127747072/Tumblr_l_692363365570517.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/815305991137656842/Tumblr_l_692361882756195.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/815305991734296596/Tumblr_l_692359924210050.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/818295076592812052/9cccb7ae-d8c0-45e4-8dc3-aaae904ab4b4.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/818295571525271562/9e62957b-8e4c-493c-8864-4a15c4aff206.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/818296240482680832/13f08388-c626-4851-9098-d4e42caf51b3.gif",
            "https://cdn.discordapp.com/attachments/804188554896867410/818296406020194345/18a34afb-0cc2-4de4-a5af-776bb5ae84d9.gif"]

        self.bot.exo_do_gif = ["https://tenor.com/view/head-lucky-one-kyungsoo-funny-gif-12694480",
            "https://tenor.com/view/soo-ksoo-kyungsoo-k-pop-singer-gif-5691853",
            "https://tenor.com/view/laughing-happy-do-kyungsoo-gif-13184812",
            "https://tenor.com/view/kyungsoo-exo-do-kpop-%E9%83%BD%E6%9A%BB%E7%A7%80-gif-9003340",
            "https://tenor.com/view/exo-kyungsoo-exo-kyungsoo-head-leaning-in-gif-20030715",
            "https://tenor.com/view/kyungsoo-do-heart-exo-kpop-gif-7576476",
            "https://tenor.com/view/exo-do-kyungsoo-finger-heart-silly-flirt-gif-12852657",
            "https://tenor.com/view/angry-mad-angry-pinguin-angry-do-do-kyungsoo-gif-18379964",
            "https://tenor.com/view/exo-do-gif-8101618",
            "https://tenor.com/view/exo-do-do-kyungsoo-kpop-handsome-gif-15918786",
            "https://tenor.com/view/do-kyungsoo-laughing-exo-lmao-lol-gif-9470952",
            "https://tenor.com/view/love-heart-cute-exo-do-kyungsoo-gif-13990606",
            "https://tenor.com/view/kyungsoo-exo-smile-smiling-laugh-gif-5716417",
            "https://64.media.tumblr.com/4bd281fce91cbf23b0d745197156d9c2/d5701b10c6682bc5-bd/s250x400/6b116675852cafd99441d8eb484944469d51ad83.gif",
            "https://64.media.tumblr.com/8276d92f20987806257dfa3124bc9b0e/1aecaa4a65ebec20-d5/s400x600/7cfdabf7d16832ef0ac2f2b40841c93523e97102.gif",
            "https://64.media.tumblr.com/1c853d16df44b371f4e3fb5fb9d591f3/f50823d7b834bd93-6a/s540x810/536fc43614315d7ef0616f892c010416b0964158.gif",
            "https://64.media.tumblr.com/6b3d5e16dad948c8b8f1ce6ce90ab2af/f50823d7b834bd93-76/s400x600/0ad0ac9e20899256f6778200fec217de66cc4d60.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/812081364101890048/0acd4be5-f4bc-4f45-b796-a9d753655133.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/812081677999669297/0c2cfc6a-dcf0-4bed-a6bb-9e0fbe6991e7.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/812082930071240714/2c9dce95-92b0-40ba-a5ab-c508ffe5c845.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/812083007028199454/2d72cec1-bbad-4e82-8548-77ac8f83b924.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/812083174091522108/2f19977f-216a-4331-a8e1-c532fed1059a.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/812083915132502016/4b7bb451-93e4-4247-a298-cfec0f8b9611.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/812084589731512340/5ac33a4d-74bf-4a8c-900b-fb6ed2b5a9dc.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/812084644832477235/5c12d55f-7975-451d-8b16-49e719058893.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/812085305216729118/6c583b36-3793-44e8-89b0-fe1ed6f21a2e.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/812085793493090344/7b41313b-b4b9-43c2-900a-6adc89f6ed5a.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/812085800933392414/7c43179a-9463-4837-86ef-df7481a770f8.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/812869056888963132/Tumblr_l_381409887702782.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/812869057220968448/Tumblr_l_381408553833720.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/812869058256568350/Tumblr_l_381407153644814.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/812869058780332052/Tumblr_l_381405579296690.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/818293601943289856/9a1b1357-51cf-4f46-b165-12cbe9c81f96.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/818295465291808810/9de4caf0-2eb7-4101-b4b8-e945beb6fcf6.gif",
            "https://cdn.discordapp.com/attachments/804188814989197322/818296075516641340/13ad2fa2-12fc-438e-a180-7928f66d19dd.gif"]

        self.bot.exo_baekhyun_gif = ["https://tenor.com/view/hoodie-byunny-baekhyun-hyun-baek-gif-19020958",
            "https://tenor.com/view/baekhyun-byun-exo-baek-laugh-gif-12920068",
            "https://tenor.com/view/tipton2109-exo-baekhyun-wave-bye-gif-13173812",
            "https://tenor.com/view/baekhyun-exo-kpop-gif-6019701",
            "https://tenor.com/view/dorama-baekhyun-kpop-exo-cute-gif-14915007",
            "https://tenor.com/view/baekhyun-mood-sass-cute-gif-15124384",
            "https://tenor.com/view/baekhyun-kpop-exo-chin-on-palm-gif-14454742",
            "https://tenor.com/view/south-korea-kpop-exo-baekhyun-gif-13913354",
            "https://tenor.com/view/exo-baekhyun-brush-up-hair-gif-15563752",
            "https://tenor.com/view/baekhyun-byun-exo-baek-glasses-gif-12920065",
            "https://tenor.com/view/exo-baekhyun-byun-laughing-gif-13045718",
            "https://tenor.com/view/baekhyun-exo-hello-gif-13993129",
            "https://tenor.com/view/tipton2109-exo-baekhyun-pout-gif-13173790",
            "https://tenor.com/view/k-pop-korean-exo-baekhyun-wink-gif-5288904",
            "https://tenor.com/view/baekhyun-exo-kpop-silly-mouth-gif-7198684",
            "https://tenor.com/view/baekyun-cute-love-heart-kpop-gif-6132186",
            "https://tenor.com/view/baekhyun-byun-exo-baek-bunny-gif-12920067",
            "https://tenor.com/view/exo-baekhyun-breathing-gif-13710749",
            "https://tenor.com/view/exo-baekhyun-camie-smile-gif-14301071",
            "https://tenor.com/view/exo-baek-hyun-k-pop-gif-11761578",
            "https://cdn.discordapp.com/attachments/804188853916270622/812081106202787850/00b4fede-a678-42cb-bf82-e668d97deefb.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812081129141829702/00d9b76d-9ad2-4a2a-bb20-ee693e8e4705.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812081176066916422/0a39af09-d925-4900-9633-e8ccce2d63d9.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812081471049039902/0b5378fb-2e2a-4590-a53c-0ecaa8b9ff86.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812081762888843294/0d1fb111-c4fa-45c7-b257-7215a5988ec0.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812081977598672936/0e9a2599-3c4c-446a-927a-9b6119a3e11b.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812082090958913556/01b44fb8-d315-4486-ae59-2769a6403980.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812082218218160178/1a55a762-e808-41ff-a521-9df6f3a172d5.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812082266389348412/1aa3fa70-4530-434a-b30c-efb532ad2547.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812082410694508614/1b8487b3-9511-4af7-ae97-899f1f337402.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812082454806528060/1c048f3f-255a-4848-8ec2-93a167b3108b.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812082709819818074/1fb8fddc-b1ff-4189-afc5-efaf3ca1b283.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812082816157745162/2a0183e8-dde7-4f1b-9ec5-ca7b19610491.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812082953697099776/2c23b3c8-d4ec-4b9b-8b6b-a6602bd5bbd1.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812083037554343966/2dea3592-3fe3-4d53-9f3d-34835bb2a826.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812083043342483476/2e33d383-b30b-44d3-b872-78c94e490cb3.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812083167347212328/2f5fbaf1-d592-484c-9454-81722384361d.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812083203296722985/03a73440-aaa9-4f8a-9955-94e708427eac.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812083337468051506/3b2b32ee-9bab-4935-ad20-5a416ecc05fc.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812083362452996116/3b2c151a-13d4-48af-8e5c-d9fc998e05d5.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812083444745109544/3c3be655-ef8e-4813-befc-0214f4fa68ca.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812083479499636737/3d4d4aaa-47ba-4e7f-91f9-ecf4bd578e46.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812083483895660554/3d17e7b9-7031-4a93-8f76-0ab428a41c88.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812083548525559841/3dc22842-d828-4633-a323-e08c179472f7.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812083855724249098/4a3c53a0-e584-455d-9d07-6fd588ece309.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812083966495424563/4bd1c471-78c8-4023-a461-86658870eeb1.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812083971835822131/4be2b0db-eb0f-491d-a44f-2e3167babc13.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812083981084262410/4bb56880-c7ef-43a0-b58a-d5b2f1a867e0.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812084055629758485/4c7bea1d-8272-48c3-8ea9-96a92fed19f4.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812084170234527796/4d90a3c6-7a6d-45ce-bd0f-7d2483f268a2.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812084212236550236/4dfa3db2-7930-4c35-b900-f2198bad2d5e.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812084423091552336/4ffdcb58-095d-4fac-8330-abe3cd8b88f0.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812084424564146226/05c510f8-dab3-4a2c-8293-9f0fda314733.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812084884612579378/5cc0c873-794f-4420-b632-df1ebd84f657.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812085083334901760/06a83574-d733-4b6e-8da9-0222dd7b2e33.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812085096827715634/06d7a022-c7e9-44fa-8c2b-a2f3b5a1f534.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812085122828337203/6a0f2cfb-179c-46f1-8723-5b522fdeee48.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812085177177473094/6b5b8b78-a353-49a4-9e41-b791e398ae1f.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812085305501810748/6d25e44e-8870-4018-82d9-17568ef1bba3.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812085340789538866/6da6b895-71e0-4563-9c4e-e2382ac8861e.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812085345590968360/6dae736c-2c09-495c-a818-815ffb23131b.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812085382337396746/6e3ad96f-b75f-4d68-a8ec-a224bac9b511.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812085390986051584/6e8fa1c4-c435-4774-92ae-5e33af52efa3.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812085484003131412/6ebb7a52-15dc-48ea-a609-1bdc6db5f27d.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812085502424776714/6ee9d67d-4549-4627-9827-133f26de7eca.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812085606326599740/6fbe063e-81c3-415f-8050-ec925de3c707.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812085646851833926/7a30d02d-1080-45d3-a94a-04e95bb6ddf2.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812085705568288808/7aff0140-ed65-45b8-b976-71e4823d5830.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812085896065187890/7da6a99a-a48c-40e9-94f1-d046dd760af3.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812086056257323044/7Wf2ngH.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812086160209739786/8aab3d6f-f058-4dc0-84d9-59f67e661080.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812086180597727242/8b3cfc02-d8e6-4f5a-a005-020c43d9044c.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812086183713833020/8abae963-8cb1-4521-9bb2-99dbfd59fb9b.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/812086187925569587/8b626f3c-58d0-463a-ab65-403cc4ce1b14.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/818292627518652476/8ddd5583-6194-4901-8fde-63298eedc044.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/818293015265017896/8f033e40-aee8-472d-ae5f-04395bfb35dd.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/818293123100442634/8f560701-5b5f-4c46-8c44-db869ed5e93f.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/818295185007050822/9d4d048f-df28-4455-8cda-7ee46e8665ca.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/818295639061823498/9ebf7aae-a2f7-4782-ad01-fa6d9a6de7e2.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/818295704543821844/9fb12efb-18a3-4f2d-8a91-055e5f53998a.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/818295748461330472/9fc8a17e-581e-4792-abb1-55c3ab79ec12.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/818295882692034570/12a736d3-23e5-4a5b-8f1b-6313abb1742d.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/818296101605212170/13dbaef8-d87b-4feb-a952-fc1de04b21c0.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/818296499347521576/19cbd480-b5d4-4d6a-b8c2-c02542bb7b54.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/818296831556976650/023a8962-cdd0-41bf-a309-c17d9a50e12f.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/818296880815276042/23dd8158-b679-4fc7-9888-26dcb1a93f2d.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/818521646037598289/Tumblr_l_1093682006427114.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/818521646573813760/Tumblr_l_1093680967810291.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/818521647526445096/Tumblr_l_1093675650178731.gif",
            "https://cdn.discordapp.com/attachments/804188853916270622/818521648323493898/Tumblr_l_1093674172835346.gif",
            "https://64.media.tumblr.com/973a45d98b608fc8f9a5bde9142e345a/be182a3ce688bed3-6f/s400x600/238e75da07e0280390d23a3168fea9535f30323d.gif",
            "https://64.media.tumblr.com/63db20fbf37d5d54256aee718792955a/be182a3ce688bed3-e3/s400x600/5a8a3227a10ec0eb80d4cba66b8a1d24eba95b35.gif",
            "https://64.media.tumblr.com/aa1833b561959450a4765c2a5cf5a6a5/be182a3ce688bed3-57/s400x600/ffcec9120b95a6b925d2ee89a7b6618dfa46b0c8.gif",
            "https://64.media.tumblr.com/2acfaab83e8637a9fd44824d50968d75/be182a3ce688bed3-2e/s400x600/3a18e5269bc460301b83708d1df7ef763b9a2e7f.gif",
            "https://64.media.tumblr.com/a7f11de76309a0aed237dfad98121c6c/be182a3ce688bed3-8a/s400x600/7cc54866defe21c18913d26c75352b235d9aef86.gif",
            "https://64.media.tumblr.com/27a7347d1e1cf3fe88988ee2b39f6a21/be182a3ce688bed3-bf/s400x600/0021d4c774587f233ab5c0b75ebe1b3429e2cfe5.gif",
            "https://64.media.tumblr.com/9a0c93ab6665847bf03b9f7ba2755bd8/be182a3ce688bed3-4b/s400x600/8c9f6d97ae78d748afc988c3642681968d14506d.gif",
            "https://64.media.tumblr.com/0f104e2e7c7ad307320c2343f1793571/be182a3ce688bed3-95/s400x600/b9cdf110e7807a96ff56051ec1923600bab0d85b.gif",
            "https://64.media.tumblr.com/c990f0068206f216a2d6ce0519d21ed5/534cd3b35b85d537-dc/s540x810/cfe65fff55c03b2d6b684954e81ef7d94cc26fdc.gif",
            "https://64.media.tumblr.com/dc051214a688bcedbd35cadcd82a5c5d/534cd3b35b85d537-22/s540x810/6f59d7cbdd218407f86f9648838ea8a76a6e60dc.gif",
            "https://64.media.tumblr.com/1d11d634440c1ef34f4255c9652cbe38/534cd3b35b85d537-41/s540x810/15e7e19e5a1992bd72f2f0e861a163584f400eda.gif",
            "https://64.media.tumblr.com/1648b40066a3263b32364edaa3cda8cc/534cd3b35b85d537-15/s540x810/3b78975fff11207e57f579bb6506c9d8dab3a9c0.gif",
            "https://64.media.tumblr.com/338bfb7dcd7aa4318e294495bd2ed4f1/534cd3b35b85d537-e7/s540x810/34f346b51d06de28927a96a83d8fe0f1a93ec052.gif",
            "https://64.media.tumblr.com/3d57e6eee0cd1246df0f7220c41a9814/534cd3b35b85d537-94/s540x810/c4204afce7c0aa077913ab181e4a7ad783d4a8ec.gif"]

        self.bot.exo_chaenyeol_gif = ["https://tenor.com/view/chanyeol-kiss-kpop-exo-gif-15449030",
            "https://tenor.com/view/chanyeol-exo-gif-15408144",
            "https://tenor.com/view/chanyeol-%E6%9C%B4%E7%81%BF%E7%83%88-gif-8087170",
            "https://tenor.com/view/chanyeol-thumbs-up-gif-9717745",
            "https://tenor.com/view/chanyeol-pcy-channie-kpop-oppa-gif-5219053",
            "https://tenor.com/view/chanyeol-exo-k-pop-sunglasses-gif-11966103",
            "https://tenor.com/view/exo-chanyeol-kpop-korean-gashina-gif-10103192",
            "https://tenor.com/view/chanyeol-pcy-channie-gif-5379301",
            "https://tenor.com/view/chanyeol-gif-9405253",
            "https://tenor.com/view/exo-chanyeol-serious-kpop-gif-12252921",
            "https://tenor.com/view/exo-chanyeol-park-chan-yeol-piao-can-lie-main-rapper-gif-17292808",
            "https://tenor.com/view/chanyeol-exo-heart-gif-15231195",
            "https://tenor.com/view/exo-chanyeol-pcy-channie-smile-gif-5307508",
            "https://tenor.com/view/chanyeol-blow-kiss-gif-5206392",
            "https://tenor.com/view/kpop-exo-chanyeol-wave-gif-8856446",
            "https://tenor.com/view/exo-chanyeol-dab-silly-dance-gif-7198679",
            "https://tenor.com/view/chanyeol-fish-exo-gif-18120027",
            "https://tenor.com/view/chanyeol-park-exo-kpop-gif-10713610",
            "https://tenor.com/view/sexy-chanyeol-chanyeol-dance-kpop-gif-13726788",
            "https://tenor.com/view/chanyeol-gif-9269407",
            "https://tenor.com/view/rapping-chan-yeol-chanyeol-exo-gif-13093858",
            "https://tenor.com/view/chanyeol-thinking-wondering-silent-gif-13657746",
            "https://tenor.com/view/chanyeol-singing-kpop-gif-13726784",
            "https://cdn.discordapp.com/attachments/804188917775466496/812082754631237633/02aeac60-1ee4-40a3-8513-786b1ca8d088.gif",
            "https://cdn.discordapp.com/attachments/804188917775466496/812083265581482024/3a77d3fe-ba55-40d3-b975-2eeb526ee796.gif",
            "https://cdn.discordapp.com/attachments/804188917775466496/812085201059446854/6b57ab69-0d20-4a78-b5b1-d33a9ba558b0.gif",
            "https://cdn.discordapp.com/attachments/804188917775466496/812446208316276766/Tumblr_l_315556848229622.gif",
            "https://cdn.discordapp.com/attachments/804188917775466496/812446209120665600/Tumblr_l_315559925054569.gif",
            "https://cdn.discordapp.com/attachments/804188917775466496/818293813218377728/9a9f95a8-1020-4404-8fde-4b18116b0466.gif"]

        self.bot.exo_sehun_gif = ["https://cdn.discordapp.com/attachments/804188518985367563/812081997051985960/0ef445a5-37e5-4211-a186-d44b97e2edbc.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/812082323704381510/1b07fb73-34c8-472b-b667-1d30298d684e.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/812082645977923594/1e760955-98bb-4c1c-add9-201dc95bc546.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/812083549268213800/3dbd8431-c5d6-4aec-983b-05cb392896b8.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/812083841133051964/4a0dee09-8a36-4c46-955d-b3585cbdee96.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/812084617892724767/5b2442fb-b198-400c-a91a-54eded940b19.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/812084920481873961/5d8305a1-961a-4a05-b2e9-0ea7b1fb98ee.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/812084921950535730/5d17289f-5d24-47dd-a8c6-d670b5a0229a.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/812084988731588618/5df3dacf-cbb5-4d2a-8853-1146a9f8a746.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/812085106192941116/06fb7076-abfd-440e-a6f8-e95e5c250949.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/812085158428541008/6ad374ba-c270-4635-aa62-e64bf95fcccb.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/812085369780174868/6dfde2d6-94a0-468b-b0b5-0bb24cd6a0df.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/818293171947175966/8f645928-5b9e-45fd-b6ba-60cce7f799ea.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/818295532669501470/9e918b47-d0cf-4a25-a126-4e5b9e45f259.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/818295659609718794/9ed43779-03cd-4edb-b790-7080cca3d74a.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/818296726946578432/23a93a98-c57f-4636-b1c0-17ed0be44ba1.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/818296953238192148/24b1f449-2da5-421f-9357-b11de942a131.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/818296955788460042/23ea801e-1b8d-4ef8-89d5-cc6d3cc72c96.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/818521670913884180/Tumblr_l_1093134586563156.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/818521671626784858/Tumblr_l_1093136219713311.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/818521672381497385/Tumblr_l_1093132497569042.gif",
            "https://cdn.discordapp.com/attachments/804188518985367563/818521672918892544/Tumblr_l_1093131221403053.gif"]

        self.bot.exo_chen_gif = ["https://cdn.discordapp.com/attachments/804189007500148786/812081819025408000/0d88a762-e789-4083-9a9f-20c43cdd8528.gif",
            "https://cdn.discordapp.com/attachments/804189007500148786/812083862334603285/4a377461-050f-434b-8ac1-74d54831c901.gif",
            "https://cdn.discordapp.com/attachments/804189007500148786/812084080011247616/4c74f854-ef83-400f-91d6-e79a907b6062.gif",
            "https://cdn.discordapp.com/attachments/804189007500148786/812084128128303114/4cc8a7af-9d10-48ab-9963-90eb9aba8803.gif",
            "https://cdn.discordapp.com/attachments/804189007500148786/812085027797860362/5e08f246-c680-4dd0-8c87-22e6a6b3263a.gif",
            "https://cdn.discordapp.com/attachments/804189007500148786/812085839550349402/7d0c865b-ce9e-4012-ab66-4a026f76290e.gif",
            "https://cdn.discordapp.com/attachments/804189007500148786/812086020333764618/7f391d0b-da8d-4390-9471-ca13b4fca84e.gif",
            "https://cdn.discordapp.com/attachments/804189007500148786/812086115871490078/08e23a25-f1f1-4d4d-9dc3-c2c0a496260e.gif",
            "https://cdn.discordapp.com/attachments/804189007500148786/815305845247442974/Tumblr_l_692324587523709.gif",
            "https://cdn.discordapp.com/attachments/804189007500148786/815305845817606214/Tumblr_l_692326182023240.gif"]

        self.bot.exo_suho_gif = ["https://tenor.com/view/exo-suho-heart-love-finger-heart-gif-15782676",
            "https://tenor.com/view/exo-sehun-suho-hunho-sejun-gif-11610480",
            "https://cdn.discordapp.com/attachments/804188541231431700/812081511108968489/0b201361-b292-4264-8bdc-54ce9d3bf865.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812081522433064960/0b638645-3ff9-4c16-8691-2bfefcecb5e5.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812081777907859516/0d06c095-9e6e-4f1d-bddb-5123081ea461.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812081950662590554/0e1ae379-b25b-4997-9d7c-721e381e1837.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812081958996803594/0e4beba4-b7d3-427e-ae15-1f122fca7185.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812082013804167208/0f007652-d0bd-4a7a-b0fc-1c7d5167a7c3.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812082237838721034/1a310eb4-cdc1-42aa-814c-acd63ea90913.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812082364750626816/1b4926f9-036e-48cf-87be-206e99beed08.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812082479355527209/1c89c457-5678-4cf8-abb7-57537ada4e52.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812082791683850280/02bf4801-af3f-4f8d-8cdd-ba8f4d06ab9e.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812082922991124480/2c2f1f62-9a0f-42b5-b8f9-20d75bb3f104.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812082982243270656/2c482473-2d2f-42c6-8720-2a68ab281a42.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812083055610298408/2e4dee75-3e66-4879-a985-0d265a7a0cfa.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812083383517315092/3b09abf2-cb3c-4922-b31f-051fa6b272e0.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812083405985546250/3bd07b00-33e9-449b-ab65-3b00d54ae69b.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812083466920263720/3cf53d8b-854c-4159-9eca-1149f53d2765.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812083564900253696/3e0ac614-fc8b-45bd-9389-64f6c378949b.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812083927048126498/4b63f192-83ee-45a0-a739-2a21b006fe8e.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812084155016937502/4d2df191-02c0-4877-8c13-89a05f88819f.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812084324778115102/4e469d67-21fd-464e-a452-625b362df8ed.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812084344012537856/4f5e3cfe-a672-4e61-8bb0-38d2defc725d.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812084360500084736/4f60de65-4d9a-4f3a-87ea-6cd3e93cf3cc.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812084367735390208/4f294ee0-3a87-4e7e-a3cf-a95f80cb8f50.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812084509498540072/5a4c4b27-1424-42e3-affd-91a6b6faa2ea.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812084523671486504/5a18a52a-72c9-4f11-bebb-43e25a01a655.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812084526784053258/5a50ff0f-a6e2-437b-ad9b-cae0621f3990.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812084604457713704/5af29cbf-55dd-43b0-b073-12644eeab277.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812084897744289862/5cdbd999-5b6f-4219-84d9-5c983a6395f9.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812084957685481502/5d653980-03de-49a2-8546-79007219b9ab.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812085011586482186/5e5a99d5-cd4a-4455-81dc-ef35302d90bd.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812085145808535552/6a9204dc-973b-4e77-a7ee-92bcc95a502d.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812085269423456326/6c2ce3b7-b6d9-4497-96be-327ba8688f82.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812085275387101185/6cb8cb67-9b1b-4fd7-a4a5-a912d643f6f9.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812085631621529630/7a0ad10c-4476-4055-8b52-8934f29164ba.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812085682617057321/7aa22199-32af-4eaf-9477-3c56e64ace43.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812085711615688774/7b01a057-788b-4a66-b1cf-0bc86663f638.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812085856880820266/7d8aca83-83aa-4b27-83d3-84b9a1f61b7e.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812085960413937694/7eff81cb-ff77-4642-9b7f-b423cc2a89e7.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812086047861112832/7fb84426-ffbc-4772-9015-5b3813aaedfe.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812086073479659550/008ced41-6c5a-4620-81ab-94287bfeb5bf.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812086117821841428/08eac52f-68ca-4a89-a329-9e234db8ae5c.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812086208112623666/8bb518b4-a84b-47d2-875e-cfb891bb577c.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812086216899821578/8cb774f7-bab1-400d-bc4d-aeae266df514.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812086244246683668/8d0e7f8b-886b-4df1-86e0-51764e263d04.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/812086246754615316/8d00f64a-f1c0-4ced-bd94-527284c8c450.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/818293639465533510/9a8d4238-92f2-4c3c-844c-c3cc941f6412.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/818295404160221194/9d881348-1e15-4f25-99dc-457bb2f2b0fa.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/818295839948406794/11b603df-a4a5-4fd1-8c4e-e1717ee9a32a.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/818296282425720863/15dfb2f0-ff4f-4683-a534-9ec54f8fbb0b.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/818296578405564476/20bb54de-4dac-419f-977d-91e401bb1c2e.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/818296592624123944/21b762a3-fcda-4df5-9d31-5118628c5324.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/818296660152549376/21e286be-6b2c-4e82-9ea0-1dd3f73d4bc4.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/818296677277499442/22dd7c72-3a6c-4729-9840-a4494153404a.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/818296927199166534/23f3a650-aff4-45d8-bc25-0f70322c7207.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/818296986251034654/25a93b04-4388-4a3d-bcee-c1af8a862d65.gif",
            "https://cdn.discordapp.com/attachments/804188541231431700/818297006262583347/25afe9dc-972d-4414-be3b-a9a24391ea16.gif"]

        self.bot.exo_lay_gif = ["https://64.media.tumblr.com/7da14c8ed43d8b8e9d2e4fe4f7e94c66/94fe4f5961e578a1-36/s540x810/3613bde3b0d000e112a0ad2037aed2d677f890f9.gif",
            "https://64.media.tumblr.com/6dfb3a8af79e0b73b81ca6b225fc48bf/94fe4f5961e578a1-12/s540x810/9802cd57df8d5d4b651e6605eda7f952cffc54c8.gif",
            "https://64.media.tumblr.com/9534730e7a91cd5e60990c9763f3d6c0/94fe4f5961e578a1-cf/s540x810/8ee5273c4b92c784b47d662d3155e429e4d486db.gif",
            "https://64.media.tumblr.com/341641282f92baa3afc723636424d615/94fe4f5961e578a1-ee/s540x810/0da5e283bde10cae86c7ba85960122d4f7707159.gif",
            "https://64.media.tumblr.com/e3769784dfa48f2256627a3d752afe21/ef092c986b395c96-ee/s400x600/764c7fa21f6a6efcaf0852bd94a7a93ae9407791.gif",
            "https://i.pinimg.com/originals/db/8f/fa/db8ffa49c4b0f74da41b6a1a1007d831.gif",
            "https://64.media.tumblr.com/99bec5c6f94081a1caea55fed061792b/dccf2ef37764af38-7c/s540x810/9fe0e8803cee9a8d470ac7a6e26bd107526ac4dc.gif",
            "https://data.whicdn.com/images/270974134/original.gif",
            "https://media1.tenor.com/images/5f755e9729321a992d715b74032a448d/tenor.gif?itemid=8267767",
            "https://i.pinimg.com/originals/ce/27/4d/ce274d01caf36a80ef54934b7d1748f4.gif",
            "http://31.media.tumblr.com/145c9a5c4160d29431791848fd9eb6e5/tumblr_nanoqagr9b1sgyexeo1_500.gif",
            "https://64.media.tumblr.com/aa1f1c741ee18ba558ed7941a7907cbf/tumblr_p5r262uVtC1t2376io1_500.gif",
            "https://64.media.tumblr.com/b571e9291954e7113c196ddb6933e054/tumblr_pt37v4cVri1rtsp19o2_r1_500.gif",
            "https://64.media.tumblr.com/671b6e895c68209e4bf42dba1dab97f1/tumblr_pt40bg0Dbo1y8h8uco1_r2_500.gif",
            "https://data.whicdn.com/images/275140585/original.gif",
            "https://data.whicdn.com/images/331545182/original.gif",
            "https://64.media.tumblr.com/1fc6f432ea59916ce49b5fdfcbc0cbc4/tumblr_prppt3Pny41xvcr1xo3_400.gif",
            "https://data.whicdn.com/images/277118144/original.gif",
            "https://66.media.tumblr.com/22c4f93aa92a43714a61bbb5061c8ec3/tumblr_p6x27fKPej1xoaddbo2_500.gif",
            "https://i.pinimg.com/originals/da/b3/bd/dab3bd7678f159eb4bd6ecdec15be113.gif",
            "https://cdn.discordapp.com/attachments/804189050193051669/812081164298616843/00bfef14-b88b-4c4c-87d0-ef7a28cb4048.gif",
            "https://cdn.discordapp.com/attachments/804189050193051669/812081293164413018/0ac40de2-0b80-4e1d-876b-e4c26ac00d02.gif",
            "https://cdn.discordapp.com/attachments/804189050193051669/812082180967628890/01ff5723-ecc6-47fd-8f0d-c83f07bf9685.gif",
            "https://cdn.discordapp.com/attachments/804189050193051669/812082546338037790/1d949669-ab58-4612-a214-6f6d57fad805.gif",
            "https://cdn.discordapp.com/attachments/804189050193051669/812082731999428618/1fdb2c9f-f97c-4648-8220-788cc02369fc.gif",
            "https://cdn.discordapp.com/attachments/804189050193051669/812082893954351164/2bac971b-2451-442c-af0c-8e8483a4c5c0.gif",
            "https://cdn.discordapp.com/attachments/804189050193051669/812083217141465118/03fa052b-ef76-434b-b107-f78459485126.gif",
            "https://cdn.discordapp.com/attachments/804189050193051669/812083279905816606/3a2076ed-299f-4b76-a8e8-3dff3e6d9047.gif",
            "https://cdn.discordapp.com/attachments/804189050193051669/812083289724026910/3abcf214-16d1-4d59-8e8c-bf7f6ec8c24c.gif",
            "https://cdn.discordapp.com/attachments/804189050193051669/812084640516669447/5b8356ed-eb31-4d30-9421-c26795770aee.gif",
            "https://cdn.discordapp.com/attachments/804189050193051669/812084999791706192/5e0bca69-b734-4b69-be4e-96356527c1c2.gif",
            "https://cdn.discordapp.com/attachments/804189050193051669/812085251076784169/6bd565fd-ad51-4a31-abb7-18c8a0f816a9.gif",
            "https://giphy.com/gifs/lay-e7WenYeCcmYlG",
            "https://giphy.com/gifs/musicvideo-lay-layzhang-wJlhPRXRQy947E00MO",
            "https://giphy.com/gifs/sheep-lay-layzhang-orwArQiwsVu5GDXMoI",
            "https://giphy.com/gifs/interview-layzhang-buzzfeedceleb-TuhHuVWrUQv2wWKOJh",
            "https://giphy.com/gifs/judge-lay-zhang-CSzDNTS1XUpgsy4teD",
            "https://cdn.discordapp.com/attachments/804189050193051669/818294875458895923/9bb046d4-10f4-4dcf-b5da-8b57079e7772.gif",
            "https://cdn.discordapp.com/attachments/804189050193051669/818295008947077140/9ca8cf02-140d-44a2-b3b7-75c833a35b45.gif",
            "https://cdn.discordapp.com/attachments/804189050193051669/818296381029744670/17d201bd-809c-4de0-9806-3a03b17692f3.gif"]

        self.bot.exo_xiumin_gif = ["https://cdn.discordapp.com/attachments/804189116748398633/812081403722334248/0b0f7062-b94d-4009-b283-eb7a4e472034.gif",
            "https://cdn.discordapp.com/attachments/804189116748398633/812082498845540372/1c522771-cba9-478f-a442-5d1099cb8037.gif",
            "https://cdn.discordapp.com/attachments/804189116748398633/812083239401160714/3a1b9a55-686b-4b6a-8309-19ff8f5f95c6.gif",
            "https://cdn.discordapp.com/attachments/804189116748398633/812084475474870272/05eb5300-1b2b-4266-84e6-3e5b7522a1b7.gif",
            "https://cdn.discordapp.com/attachments/804189116748398633/812084698272235530/5c756d00-df9f-47a3-a9af-ecc563bd8453.gif",
            "https://cdn.discordapp.com/attachments/804189116748398633/812085055698239488/5ed9f39f-1b24-48b6-9aa2-e953a47134f2.gif",
            "https://cdn.discordapp.com/attachments/804189116748398633/812085576814821396/6fa39c57-a469-4552-b15e-3394d05ca193.gif",
            "https://cdn.discordapp.com/attachments/804189116748398633/818296253749788702/14b98671-7a9f-49bd-95df-e9a69f63f396.gif",
            "https://cdn.discordapp.com/attachments/804189116748398633/818296868709990400/23d135ed-1d6a-4ff4-b26d-dcdd1eeb64bd.gif"]
    #. Golden Child
        self.bot.golcha_bomin_gif = ["https://gfycat.com/FastTartBirdofparadise",
            "https://gfycat.com/ComposedBiodegradableCuttlefish",
            "https://gfycat.com/ElectricCarelessEmperorshrimp",
            "https://gfycat.com/MealyEnlightenedKarakul",
            "https://gfycat.com/EminentRedHaddock",
            "https://gfycat.com/FortunatePlaintiveAmericanlobster",
            "https://gfycat.com/PleasantHideousArmyant",
            "https://gfycat.com/VigorousImpressionableFowl",
            "https://gfycat.com/SlimyJealousElephant",
            "https://gfycat.com/EvenIllinformedGuineafowl",
            "https://gfycat.com/IllegalDetailedKakapo",
            "https://gfycat.com/AngryAthleticCanary",
            "https://gfycat.com/ThankfulYellowishAllosaurus",
            "https://gfycat.com/RepulsiveDarlingGossamerwingedbutterfly",
            "https://gfycat.com/TenderHonestBushbaby",
            "https://gfycat.com/SilentScrawnyChinesecrocodilelizard",
            "https://gfycat.com/SnoopyVelvetyAtlanticsharpnosepuffer",
            "https://gfycat.com/EllipticalImaginativeHypsilophodon",
            "https://gfycat.com/EachOrganicDoctorfish",
            "https://gfycat.com/FormalLittleArkshell",
            "https://gfycat.com/MenacingHorribleIchidna",
            "https://gfycat.com/DefenselessCompetentFrigatebird",
            "https://gfycat.com/CraftySameDuckbillcat",
            "https://gfycat.com/MiserlyGlisteningAdamsstaghornedbeetle",
            "https://gfycat.com/FoolhardyClassicAbyssiniangroundhornbill",
            "https://gfycat.com/ElegantCloudyCollardlizard",
            "https://gfycat.com/ScornfulSimplisticAsiandamselfly",
            "https://gfycat.com/VictoriousImpracticalGarpike",
            "https://gfycat.com/FrightenedEvilAtlanticspadefish",
            "https://gfycat.com/MellowEsteemedGeese",
            "https://gfycat.com/TastyScentedDogwoodclubgall",
            "https://gfycat.com/WelltodoShamelessLcont",
            "https://gfycat.com/WaryScarceGoral",
            "https://gfycat.com/UnawarePlaintiveCopperhead",
            "https://gfycat.com/AgileVibrantBufeo",
            "https://gfycat.com/ShabbyWebbedAlbino",
            "https://gfycat.com/OrnateMessyBooby",
            "https://gfycat.com/BrilliantUniformArmyant",
            "https://gfycat.com/BothFirmDonkey",
            "https://gfycat.com/LeanAridArawana",
            "https://gfycat.com/GenuinePoliticalCaiman",
            "https://gfycat.com/SlightIdioticAntbear",
            "https://gfycat.com/ExcellentPerfumedDiplodocus",
            "https://gfycat.com/IllfatedExcitableHedgehog",
            "https://gfycat.com/KindlyAlertAnkole",
            "https://gfycat.com/AdolescentPalatableGreatwhiteshark",
            "https://gfycat.com/ClassicScarceEsok",
            "https://gfycat.com/IdealisticMiserlyGrouse",
            "https://gfycat.com/RevolvingIllegalFlicker",
            "https://gfycat.com/PerfectImperturbableAmmonite",
            "https://gfycat.com/ShallowReflectingFlyinglemur",
            "https://gfycat.com/DazzlingWhisperedCony",
            "https://gfycat.com/ClosedCluelessJackrabbit",
            "https://gfycat.com/GiantOldfashionedEasternglasslizard",
            "https://gfycat.com/OffensiveZealousBrahmancow",
            "https://gfycat.com/FlawlessRareCuttlefish",
            "https://gfycat.com/HeavenlyFantasticHawaiianmonkseal",
            "https://gfycat.com/SilkyPerfectAntbear",
            "https://gfycat.com/GreedyGloomyAlligatorsnappingturtle",
            "https://gfycat.com/SimilarZanyFlyinglemur",
            "https://gfycat.com/ColdHonestFunnelweaverspider",
            "https://gfycat.com/HarmfulNaughtyGibbon",
            "https://gfycat.com/DapperSelfishBlacknorwegianelkhound",
            "https://gfycat.com/OblongWeeklyHog",
            "https://gfycat.com/OffensiveFakeBurro",
            "https://gfycat.com/SerpentineGroundedAxisdeer",
            "https://gfycat.com/ImaginativeIdolizedIchthyosaurs",
            "https://gfycat.com/BossyImpassionedFinch",
            "https://gfycat.com/HospitableWebbedGiraffe",
            "https://gfycat.com/SecondaryGenuineBuck",
            "https://gfycat.com/AptAridCrocodileskink",
            "https://gfycat.com/SpotlessNiceDragon",
            "https://gfycat.com/GlisteningInsignificantAfricanparadiseflycatcher",
            "https://gfycat.com/DeliriousCanineCuckoo",
            "https://gfycat.com/JoyousArtisticFrillneckedlizard",
            "https://tenor.com/bqc82.gif",
            "https://tenor.com/bqc85.gif",
            "https://tenor.com/bqc68.gif",
            "https://tenor.com/bhvNP.gif",
            "https://tenor.com/bvHzx.gif",
            "https://gfycat.com/GrippingImpeccableCutworm",
            "https://gfycat.com/ExhaustedExcellentBlueshark",
            "https://gfycat.com/SentimentalGrandBlesbok",
            "https://gfycat.com/PlainHighKilldeer",
            "https://gfycat.com/AdvancedIncredibleBunting",
            "https://gfycat.com/WillingHealthyCub",
            "https://gfycat.com/CrazyBasicGilamonster",
            "https://gfycat.com/CornyClumsyBeauceron",
            "https://gfycat.com/HealthyPerfectGrunion",
            "https://gfycat.com/OrdinaryDistantDugong",
            "https://gfycat.com/WhisperedNeglectedBadger",
            "https://gfycat.com/BigCreepyDotterel",
            "https://gfycat.com/LinedShabbyEasternglasslizard",
            "https://gfycat.com/onlylateargentinehornedfrog",
            "https://gfycat.com/disfiguredscrawnyfugu",
            "https://gfycat.com/identicalhiddendarklingbeetle",
            "https://gfycat.com/immaterialuniquecapybara",
            "https://gfycat.com/longwillingcapybara",
            "https://gfycat.com/harmfuldifferentincatern",
            "https://gfycat.com/firstcharmingatlanticblackgoby"]

        self.bot.golcha_daeyeol_gif = ["https://gfycat.com/WhoppingUnpleasantBoilweevil",
            "https://gfycat.com/SkinnyTastyCoypu",
            "https://gfycat.com/HandyMeaslyItalianbrownbear",
            "https://gfycat.com/HotRightGoral",
            "https://gfycat.com/RawDeepIrishwaterspaniel",
            "https://tenor.com/bzrsg.gif",
            "https://tenor.com/bv9tu.gif",
            "https://tenor.com/bv9tA.gif",
            "https://tenor.com/bv9tx.gif",
            "https://tenor.com/bw8ka.gif",
            "https://gfycat.com/BlaringAmazingBagworm",
            "https://gfycat.com/DisfiguredEverlastingAdouri",
            "https://gfycat.com/SpanishSnivelingCreature",
            "https://gfycat.com/AgedWholeDrongo",
            "https://gfycat.com/ComposedShortKillerwhale",
            "https://gfycat.com/SimplisticPresentAdder",
            "https://gfycat.com/TangibleSandyIslandcanary",
            "https://gfycat.com/ForsakenLiveAfricanaugurbuzzard",
            "https://gfycat.com/ScornfulGiganticDowitcher",
            "https://gfycat.com/FeistyShorttermHarborporpoise",
            "https://gfycat.com/ColdEnragedGardensnake",
            "https://gfycat.com/ElegantImpracticalJuliabutterfly",
            "https://gfycat.com/QuarrelsomeGrippingFurseal",
            "https://gfycat.com/PettySlimIndianjackal",
            "https://gfycat.com/SharpSoulfulCuttlefish",
            "https://gfycat.com/AstonishingWarpedDeviltasmanian",
            "https://gfycat.com/UnnaturalDefiantGourami",
            "https://gfycat.com/AnotherUnfitApisdorsatalaboriosa",
            "https://gfycat.com/DescriptiveDimwittedAmbushbug",
            "https://gfycat.com/UnhappyThankfulChevrotain",
            "https://gfycat.com/IlliterateAchingHummingbird",
            "https://gfycat.com/AjarZigzagIberiannase",
            "https://gfycat.com/UnevenDarlingIndiancow",
            "https://gfycat.com/ViciousMilkyGrayfox",
            "https://gfycat.com/NearDeterminedAtlanticbluetang",
            "https://gfycat.com/BigheartedJaggedBrownbear",
            "https://gfycat.com/AggravatingConsiderateHog",
            "https://gfycat.com/OldTintedFlatfish",
            "https://gfycat.com/GleamingMilkyLamb",
            "https://gfycat.com/IdealisticBitesizedGrasshopper",
            "https://gfycat.com/VibrantAccurateHarvestmen",
            "https://gfycat.com/SnappyHastyDuckbillplatypus",
            "https://gfycat.com/DearestAlertHoneybee",
            "https://gfycat.com/UnnaturalGargantuanEnglishpointer",
            "https://gfycat.com/ChiefSafeBlobfish",
            "https://gfycat.com/GrayUnawareEasteuropeanshepherd",
            "https://gfycat.com/ElectricVillainousAbalone",
            "https://gfycat.com/MellowFearfulAntarcticfurseal",
            "https://gfycat.com/CarefulSpeedyGrizzlybear",
            "https://gfycat.com/AlienatedFreshFulmar",
            "https://gfycat.com/QueasyFaroffAmericantoad",
            "https://gfycat.com/BraveKindheartedCentipede",
            "https://gfycat.com/AllHardtofindDwarfmongoose",
            "https://gfycat.com/DeliriousIckyEnglishsetter",
            "https://gfycat.com/FreshReliableElver",
            "https://gfycat.com/ArcticKindCamel",
            "https://gfycat.com/NervousLeadingBlackwidowspider",
            "https://gfycat.com/WickedWindyBarb",
            "https://gfycat.com/LavishPointlessGuernseycow",
            "https://gfycat.com/MajesticSlowArmyant",
            "https://gfycat.com/UnpleasantBackAsianporcupine",
            "https://gfycat.com/NiftyObeseAnkolewatusi",
            "https://gfycat.com/EnormousRewardingHermitcrab",
            "https://gfycat.com/SickIncredibleBuffalo",
            "https://gfycat.com/GraciousGlisteningChupacabra",
            "https://gfycat.com/LankyRecentBobcat",
            "https://gfycat.com/WarmBlaringGilamonster",
            "https://gfycat.com/DefiantThirstyAbyssiniangroundhornbill",
            "https://gfycat.com/IndolentGrossGoldeneye",
            "https://gfycat.com/ElderlySlushyAdder",
            "https://gfycat.com/LawfulAbsoluteDotterel",
            "https://gfycat.com/AdeptParallelAmericanquarterhorse",
            "https://gfycat.com/CraftyMiserableGhostshrimp",
            "https://gfycat.com/SnivelingThornyHellbender",
            "https://gfycat.com/GranularSpeedyHarborporpoise",
            "https://gfycat.com/ZealousLightheartedArabianoryx",
            "https://gfycat.com/ImpartialKeyLeech",
            "https://gfycat.com/BetterAlertIchidna",
            "https://gfycat.com/JointAstonishingEider",
            "https://gfycat.com/LeafyEllipticalAiredaleterrier",
            "https://gfycat.com/RapidBountifulAsiaticmouflon",
            "https://gfycat.com/LightAngelicCottonmouth",
            "https://gfycat.com/PoshHarshGrouse",
            "https://gfycat.com/DefensiveHeavenlyBlesbok",
            "https://gfycat.com/ParallelThriftyCusimanse",
            "https://gfycat.com/HeartfeltInsidiousBlackpanther",
            "https://gfycat.com/spanishsnivelingcreature",
            "https://gfycat.com/IncompleteSourGoral",
            "https://gfycat.com/CompetentNippyKoi",
            "https://gfycat.com/BiodegradableGraveEyelashpitviper",
            "https://gfycat.com/MildCraftyCrab",
            "https://gfycat.com/ArcticWebbedGnat",
            "https://gfycat.com/ShoddyVigilantAlligatorgar",
            "https://gfycat.com/DishonestDishonestGalapagosalbatross",
            "https://gfycat.com/NearReliableGreendarnerdragonfly",
            "https://gfycat.com/AridNearAustralianshelduck",
            "https://gfycat.com/UnfortunateAdorableIbadanmalimbe",
            "https://gfycat.com/EuphoricSoftEstuarinecrocodile",
            "https://gfycat.com/DefiniteSecretIberianbarbel",
            "https://gfycat.com/WebbedDazzlingHairstreakbutterfly",
            "https://gfycat.com/academicgrouchyhorseshoebat",
            "https://gfycat.com/ashamedseveralbumblebee",
            "https://gfycat.com/sophisticatedornatearabianoryx",
            "https://gfycat.com/generalcommonarchaeocete",
            "https://gfycat.com/peacefulexemplarybangeltiger"]

        self.bot.golcha_donghyun_gif = ["https://gfycat.com/IdolizedTameBangeltiger",
            "https://gfycat.com/DifficultDeadEyra",
            "https://gfycat.com/SlimWhoppingHarpseal",
            "https://gfycat.com/JitteryExemplaryGharial",
            "https://gfycat.com/VapidAppropriateAmericanalligator",
            "https://gfycat.com/PitifulShadyBats",
            "https://gfycat.com/ExcitableDarlingIvorybackedwoodswallow",
            "https://gfycat.com/FastFelineEnglishsetter",
            "https://gfycat.com/LonePleasantCaecilian",
            "https://gfycat.com/BowedEveryAfricanparadiseflycatcher",
            "https://gfycat.com/IllustriousFamousAlbertosaurus",
            "https://gfycat.com/SecondaryGargantuanJunebug",
            "https://gfycat.com/BriskCorruptIrishdraughthorse",
            "https://gfycat.com/GlamorousAstonishingBonobo",
            "https://gfycat.com/UnnaturalBeautifulAllensbigearedbat",
            "https://gfycat.com/AggressivePersonalBanteng",
            "https://gfycat.com/EqualEnragedCardinal",
            "https://gfycat.com/TestyNimbleHound",
            "https://gfycat.com/ClosedWideGraysquirrel",
            "https://gfycat.com/DarlingGleamingArcherfish",
            "https://gfycat.com/MadeupShamelessAnaconda",
            "https://gfycat.com/ZanyWeeCougar",
            "https://gfycat.com/PresentSinfulBronco",
            "https://gfycat.com/UnsightlySeveralCorydorascatfish",
            "https://gfycat.com/JealousSatisfiedCoypu",
            "https://gfycat.com/SparklingDistantJabiru",
            "https://gfycat.com/NearKlutzyBobolink",
            "https://gfycat.com/SpicyDizzyBlackwidowspider",
            "https://gfycat.com/FancyNaiveAngwantibo",
            "https://gfycat.com/LazyValuableGavial",
            "https://gfycat.com/DismalTintedAzurevasesponge",
            "https://gfycat.com/NaughtySecondhandJumpingbean",
            "https://gfycat.com/FatalNeighboringAnchovy",
            "https://gfycat.com/WildUnitedCamel",
            "https://gfycat.com/FloweryDecisiveLeafcutterant",
            "https://gfycat.com/EvenPoorKite",
            "https://gfycat.com/ColossalFormalItaliangreyhound",
            "https://gfycat.com/WarlikeIncompatibleAzurevase",
            "https://gfycat.com/OptimalPastelElephant",
            "https://gfycat.com/FelineVariableGoldeneye",
            "https://gfycat.com/LightSpecificDeer",
            "https://gfycat.com/WeepyPerfectCaimanlizard",
            "https://gfycat.com/GlisteningSillyHorsefly",
            "https://gfycat.com/WillingBabyishBallpython",
            "https://gfycat.com/HollowCourteousBluemorphobutterfly",
            "https://gfycat.com/MammothAliveHarlequinbug",
            "https://gfycat.com/ImmaterialDampKronosaurus",
            "https://gfycat.com/AstonishingFatherlyDikkops",
            "https://gfycat.com/TiredShockingIlladopsis",
            "https://gfycat.com/NervousConstantCub",
            "https://gfycat.com/AntiqueSelfreliantEidolonhelvum",
            "https://gfycat.com/SpanishCarefreeBarbet",
            "https://gfycat.com/MistyLightAsianlion",
            "https://gfycat.com/SnoopyReasonableGalapagosalbatross",
            "https://gfycat.com/PlayfulAcclaimedAdmiralbutterfly",
            "https://gfycat.com/OrderlyPossibleGermanshepherd",
            "https://gfycat.com/SadWavyBandicoot",
            "https://gfycat.com/ThunderousJubilantAddax",
            "https://gfycat.com/UnfortunateLeafyHarvestmen",
            "https://gfycat.com/RevolvingGoodnaturedFrillneckedlizard",
            "https://gfycat.com/UnrealisticNegativeDuiker",
            "https://gfycat.com/FlatAmbitiousIriomotecat",
            "https://gfycat.com/TartFixedBarbet",
            "https://gfycat.com/PlumpHatefulJaeger",
            "https://gfycat.com/MajesticPotableKitty",
            "https://gfycat.com/AdmirableIcyHydra",
            "https://gfycat.com/ShowyRapidLiger",
            "https://gfycat.com/WelcomeDefiantCowrie",
            "https://gfycat.com/SmoggyBigGodwit",
            "https://gfycat.com/VerifiableDependableCamel",
            "https://gfycat.com/FastImpartialKronosaurus",
            "https://gfycat.com/FailingEmbarrassedAstrangiacoral",
            "https://gfycat.com/HappyDeliriousIberianemeraldlizard",
            "https://gfycat.com/AgedUnfoldedArcticfox",
            "https://gfycat.com/UnfoldedSlushyJackal",
            "https://gfycat.com/AfraidFamousFowl",
            "https://gfycat.com/OffensiveSpryIndianabat",
            "https://gfycat.com/ChiefDisfiguredConure",
            "https://gfycat.com/FlippantMeatyAustralianshelduck",
            "https://gfycat.com/AlarmedAliveBoaconstrictor",
            "https://gfycat.com/PoliteFrighteningFantail",
            "https://gfycat.com/ConsiderateDecimalFrog",
            "https://gfycat.com/ParchedPleasedAddax",
            "https://gfycat.com/TheseVillainousAmericantoad",
            "https://gfycat.com/PowerlessEnormousJabiru",
            "https://gfycat.com/HopefulBareAmericanlobster",
            "https://gfycat.com/ForcefulOddballApisdorsatalaboriosa",
            "https://gfycat.com/SorrowfulGrayBonobo",
            "https://gfycat.com/FinishedAmazingAlligatorgar",
            "https://gfycat.com/ScaredTintedCusimanse",
            "https://gfycat.com/SophisticatedThinAstrangiacoral",
            "https://gfycat.com/ResponsibleMessyAmericanrobin",
            "https://gfycat.com/IncompatibleGivingHoneyeater",
            "https://gfycat.com/SilverBestGrouse",
            "https://gfycat.com/FeistyRingedGallinule",
            "https://gfycat.com/MadeupPoliteEskimodog",
            "https://gfycat.com/SaneHandmadeAsianpiedstarling",
            "https://gfycat.com/celebratedwindingantelopegroundsquirrel",
            "https://gfycat.com/infinitedisguisedkakarikis",
            "https://gfycat.com/qualifiedmeekcoyote"]

        self.bot.golcha_jaehyun_gif = ["https://gfycat.com/BlackUncomfortableGreyhounddog",
            "https://gfycat.com/ThreadbareOpulentCusimanse",
            "https://gfycat.com/MedicalHandsomeIrishwaterspaniel",
            "https://gfycat.com/DaringSlightIceblueredtopzebra",
            "https://gfycat.com/PastSillyBlackfootedferret",
            "https://gfycat.com/LikableMintyChafer",
            "https://gfycat.com/CorruptSmallBeauceron",
            "https://gfycat.com/ActualForkedClam",
            "https://gfycat.com/HelplessGiantAmericanbulldog",
            "https://gfycat.com/HatefulBonyIndianabat",
            "https://gfycat.com/DeterminedRespectfulArmedcrab",
            "https://gfycat.com/EnlightenedCommonBelugawhale",
            "https://gfycat.com/ImpressionableColorfulImperialeagle",
            "https://gfycat.com/CornyBlindBarb",
            "https://gfycat.com/HollowIgnorantDeinonychus",
            "https://gfycat.com/TastyFastKoodoo",
            "https://gfycat.com/LivelyJovialAlbertosaurus",
            "https://gfycat.com/RecklessRewardingEidolonhelvum",
            "https://gfycat.com/ImmediateRingedHarborporpoise",
            "https://gfycat.com/OrdinarySneakyAustraliankelpie",
            "https://gfycat.com/MinorRealEastrussiancoursinghounds",
            "https://gfycat.com/CostlyMerryHyracotherium",
            "https://gfycat.com/DimParchedAfricanelephant",
            "https://gfycat.com/AdoredPaleCowrie",
            "https://gfycat.com/MeanKindKodiakbear",
            "https://gfycat.com/LonelyTartBorzoi",
            "https://gfycat.com/FewJadedDouglasfirbarkbeetle",
            "https://gfycat.com/LegalGenerousFattaileddunnart",
            "https://gfycat.com/SpotlessFrenchDaddylonglegs",
            "https://gfycat.com/SmallKindheartedHammerheadshark",
            "https://gfycat.com/CostlySecondHalicore",
            "https://gfycat.com/CharmingGivingGreatwhiteshark",
            "https://gfycat.com/HollowSnivelingAntipodesgreenparakeet",
            "https://gfycat.com/NastyDarkEsok",
            "https://tenor.com/bdsbP.gif",
            "https://tenor.com/buDym.gif",
            "https://tenor.com/boH1F.gif",
            "https://tenor.com/bzm6O.gif",
            "https://tenor.com/bzzSY.gif",
            "https://gfycat.com/AstonishingForcefulGentoopenguin",
            "https://gfycat.com/OfficialBigheartedIrishredandwhitesetter",
            "https://gfycat.com/PastUnrealisticGermanspaniel",
            "https://gfycat.com/FluidFirstBaboon",
            "https://gfycat.com/DistortedCheerfulIrishwolfhound",
            "https://gfycat.com/BelatedDazzlingArcherfish",
            "https://gfycat.com/AptHopefulGrayfox",
            "https://gfycat.com/DelightfulUncomfortableHalcyon",
            "https://gfycat.com/ImperturbableSolidAzurewingedmagpie",
            "https://gfycat.com/ScaryDeficientGlobefish",
            "https://gfycat.com/WarlikeUnfortunateAffenpinscher",
            "https://gfycat.com/HeavenlyAcrobaticAztecant",
            "https://gfycat.com/CheapLivelyBigmouthbass",
            "https://gfycat.com/FewMasculineIndianskimmer",
            "https://gfycat.com/InsistentSecretHornet",
            "https://gfycat.com/WanHeftyAegeancat",
            "https://gfycat.com/RectangularSnarlingBittern",
            "https://gfycat.com/FlusteredRichEyas",
            "https://gfycat.com/WavyCanineBirdofparadise",
            "https://gfycat.com/ObeseHeavyFlee",
            "https://gfycat.com/HappygoluckyArcticBarb",
            "https://gfycat.com/TatteredLoathsomeAtlanticbluetang",
            "https://gfycat.com/LawfulBonyAmericancrow",
            "https://gfycat.com/SilentCavernousDolphin",
            "https://gfycat.com/SimpleUnsightlyAustrianpinscher",
            "https://gfycat.com/VengefulNegligibleChafer",
            "https://gfycat.com/IllustriousPhonyEland",
            "https://gfycat.com/UnevenElegantCaterpillar",
            "https://gfycat.com/IgnorantMagnificentKusimanse",
            "https://gfycat.com/DecentIdleEstuarinecrocodile",
            "https://gfycat.com/GleefulDependentDinosaur",
            "https://gfycat.com/ConstantWarlikeGermanwirehairedpointer",
            "https://gfycat.com/AmpleHealthyArcticseal",
            "https://gfycat.com/WhichNewHagfish",
            "https://gfycat.com/AgreeableExcitableArmyant",
            "https://gfycat.com/ViciousRevolvingDegus",
            "https://gfycat.com/CheeryBoilingCottontail",
            "https://gfycat.com/BabyishThoseAmericanbittern",
            "https://gfycat.com/InfantileLoathsomeJaguar",
            "https://gfycat.com/FemaleEvenDassierat",
            "https://gfycat.com/MajorCorruptGroundhog",
            "https://gfycat.com/DescriptiveMetallicAppaloosa",
            "https://gfycat.com/WateryCriminalBubblefish",
            "https://gfycat.com/SpryTameCavy",
            "https://gfycat.com/SeparateJampackedAtlanticspadefish",
            "https://gfycat.com/HighFixedArmednylonshrimp",
            "https://gfycat.com/SecretSpottedAustraliansilkyterrier",
            "https://gfycat.com/DapperMediocreBluetonguelizard",
            "https://gfycat.com/AlienatedChillyGalapagossealion",
            "https://gfycat.com/BrilliantLivelyGermanshorthairedpointer",
            "https://gfycat.com/parallelhighemperorpenguin",
            "https://gfycat.com/FirsthandSandyHammerkop",
            "https://gfycat.com/HastyEmptyImpala",
            "https://gfycat.com/FavorableBruisedGaur",
            "https://gfycat.com/AthleticPitifulIridescentshark",
            "https://gfycat.com/HealthyAnyAlaskanhusky",
            "https://gfycat.com/baggywindinggraywolf",
            "https://gfycat.com/sophisticatedvictoriousatlanticspadefish",
            "https://gfycat.com/illinformedassuredfiddlercrab",
            "https://gfycat.com/easyjointindianpalmsquirrel"]

        self.bot.golcha_jangjun_gif = ["https://gfycat.com/UnhappyHospitableAmericanalligator",
            "https://gfycat.com/SoreRewardingBangeltiger",
            "https://gfycat.com/UnfortunateAggressiveFlyingsquirrel",
            "https://gfycat.com/ThinTotalEagle",
            "https://gfycat.com/GlitteringOldfashionedCapeghostfrog",
            "https://tenor.com/bqphM.gif",
            "https://tenor.com/bxpHr.gif",
            "https://tenor.com/bytvG.gif",
            "https://tenor.com/bzCXX.gif",
            "https://tenor.com/bzt3g.gif",
            "https://gfycat.com/RevolvingRespectfulHarrierhawk",
            "https://gfycat.com/SeveralReflectingJapanesebeetle",
            "https://gfycat.com/GreedyDistinctHoneyeater",
            "https://gfycat.com/UncomfortableInformalFox",
            "https://gfycat.com/MelodicDiligentAnemonecrab",
            "https://gfycat.com/GleefulCapitalKingsnake",
            "https://gfycat.com/ImpressionableNaughtyHumpbackwhale",
            "https://gfycat.com/WelcomeUltimateKite",
            "https://gfycat.com/GleefulJointBarnswallow",
            "https://gfycat.com/MilkyGargantuanHare",
            "https://gfycat.com/ExemplaryDeadBee",
            "https://gfycat.com/DesertedHauntingEquestrian",
            "https://gfycat.com/MistyBadGuanaco",
            "https://gfycat.com/FarawayBlissfulAustraliansilkyterrier",
            "https://gfycat.com/SnarlingUnkemptFurseal",
            "https://gfycat.com/CrazyRipeCoati",
            "https://gfycat.com/SplendidOldfashionedBorer",
            "https://gfycat.com/ImpassionedSecretChickadee",
            "https://gfycat.com/WellwornKaleidoscopicHartebeest",
            "https://gfycat.com/FlickeringLinedIggypops",
            "https://gfycat.com/AccurateFreshGrison",
            "https://gfycat.com/PeriodicFearlessBergerpicard",
            "https://gfycat.com/GroundedSandyBlackpanther",
            "https://gfycat.com/PresentAmpleBluebottlejellyfish",
            "https://gfycat.com/CandidIdioticAlpinegoat",
            "https://gfycat.com/BronzeWiltedAmericancrow",
            "https://gfycat.com/SorrowfulIllegalGoldenretriever",
            "https://gfycat.com/ShrillSizzlingLamb",
            "https://gfycat.com/DisloyalAchingAstrangiacoral",
            "https://gfycat.com/CookedAnyHorsechestnutleafminer",
            "https://gfycat.com/LividMessyFulmar",
            "https://gfycat.com/SmoggyWateryAstarte",
            "https://gfycat.com/LoathsomeFoolishAfricangoldencat",
            "https://gfycat.com/UnrealisticWeirdGypsymoth",
            "https://gfycat.com/CanineLastingHammerheadbird",
            "https://gfycat.com/SleepyAgreeableAntarcticfurseal",
            "https://gfycat.com/AridGargantuanEarthworm",
            "https://gfycat.com/SelfishAlertDarwinsfox",
            "https://gfycat.com/SkeletalBriskGermanwirehairedpointer",
            "https://gfycat.com/FirstGlisteningAtlanticblackgoby",
            "https://gfycat.com/EnergeticSmugHorse",
            "https://gfycat.com/DefiniteBriefHerring",
            "https://gfycat.com/SelfishHorribleCaimanlizard",
            "https://gfycat.com/BriefTepidAlligatorgar",
            "https://gfycat.com/PessimisticRelievedGlobefish",
            "https://gfycat.com/PracticalDiligentDaddylonglegs",
            "https://gfycat.com/DependentAppropriateJohndory",
            "https://gfycat.com/GleamingMedicalBarracuda",
            "https://gfycat.com/BronzeDarlingAmethystinepython",
            "https://gfycat.com/LividHauntingDeermouse",
            "https://gfycat.com/PettyImmenseIsopod",
            "https://gfycat.com/AmbitiousShimmeringAzurevase",
            "https://gfycat.com/WhirlwindAmpleBoubou",
            "https://gfycat.com/CarefulWebbedGuineafowl",
            "https://gfycat.com/ObeseUnluckyHornshark",
            "https://gfycat.com/YawningBoldAlaskanhusky",
            "https://gfycat.com/EsteemedImpoliteHornet",
            "https://gfycat.com/ImperfectGlumFallowdeer",
            "https://gfycat.com/LinedSoftBoar",
            "https://gfycat.com/UnfoldedUnhappyBullmastiff",
            "https://gfycat.com/FeistyVagueAmurratsnake",
            "https://gfycat.com/CarelessUnluckyBeardedcollie",
            "https://gfycat.com/WelltodoNeglectedGraywolf",
            "https://gfycat.com/GiganticHelplessArchaeopteryx",
            "https://gfycat.com/AnchoredEllipticalFly",
            "https://gfycat.com/AlarmingUnhappyBittern",
            "https://gfycat.com/OblongCrispAdmiralbutterfly",
            "https://gfycat.com/SereneLegitimateBobwhite",
            "https://gfycat.com/VengefulGentleGyrfalcon",
            "https://gfycat.com/UnevenPointlessGenet",
            "https://gfycat.com/InfiniteUntimelyAntlion",
            "https://gfycat.com/AdmiredGreatGardensnake",
            "https://gfycat.com/GlumHandyHarpseal",
            "https://gfycat.com/ComplicatedScentedGrub",
            "https://gfycat.com/BeneficialAltruisticBee",
            "https://gfycat.com/LegalBewitchedIbizanhound",
            "https://gfycat.com/AlertApprehensiveLark",
            "https://gfycat.com/EsteemedTiredHorsemouse",
            "https://gfycat.com/OblongMassiveBrownbutterfly",
            "https://gfycat.com/EdibleHandyBantamrooster",
            "https://gfycat.com/AssuredUnrulyFlies",
            "https://gfycat.com/CreamyInfatuatedHoneyeater",
            "https://gfycat.com/SmoggyOnlyIrrawaddydolphin",
            "https://gfycat.com/SelfreliantAromaticGuernseycow",
            "https://gfycat.com/OddIlliterateAntarcticgiantpetrel",
            "https://gfycat.com/TautBonyBettong",
            "https://gfycat.com/AccomplishedCharmingBluemorphobutterfly",
            "https://gfycat.com/EducatedBelovedAztecant",
            "https://gfycat.com/EntireIdealGopher",
            "https://gfycat.com/AdvancedFatalGerenuk"]

        self.bot.golcha_jibeom_gif = ["https://gfycat.com/AmpleThriftyInchworm",
            "https://gfycat.com/HiddenRemorsefulBobolink",
            "https://gfycat.com/GloriousFlickeringArcticduck",
            "https://gfycat.com/UnsungRespectfulGull",
            "https://gfycat.com/QuerulousDifficultAlleycat",
            "https://gfycat.com/SpicyCooperativeAsp",
            "https://gfycat.com/NimbleNegativeGull",
            "https://gfycat.com/HelpfulGlisteningLamb",
            "https://gfycat.com/PleasingBiodegradableChanticleer",
            "https://gfycat.com/ClearUnfortunateKoalabear",
            "https://gfycat.com/ExcitableLimpJellyfish",
            "https://gfycat.com/MaleInsignificantEeve",
            "https://gfycat.com/ConcernedTintedCrownofthornsstarfish",
            "https://gfycat.com/VictoriousSmartHadrosaurus",
            "https://gfycat.com/InfamousImportantCrustacean",
            "https://gfycat.com/GloriousLawfulAfricanporcupine",
            "https://gfycat.com/UncommonPessimisticCurlew",
            "https://gfycat.com/DesertedHighAegeancat",
            "https://gfycat.com/PerkyCompleteGreatdane",
            "https://gfycat.com/QuarrelsomeKindlyDorado",
            "https://gfycat.com/EmbarrassedHollowAntarcticfurseal",
            "https://gfycat.com/LegalElasticAztecant",
            "https://gfycat.com/HastyCavernousFeline",
            "https://gfycat.com/WildFoolhardyIvorygull",
            "https://gfycat.com/PracticalSilentJunco",
            "https://gfycat.com/WateryMellowBlackpanther",
            "https://gfycat.com/KeenHonorableJohndory",
            "https://gfycat.com/UnawareEnergeticBarasinga",
            "https://gfycat.com/InsidiousDeliriousCowbird",
            "https://gfycat.com/ActiveDisloyalBeauceron",
            "https://gfycat.com/SmallHastyGavial",
            "https://gfycat.com/UnhappyBadBeetle",
            "https://gfycat.com/UnnaturalOilyLice",
            "https://gfycat.com/WelllitBeneficialKestrel",
            "https://gfycat.com/CorruptOldBass",
            "https://gfycat.com/FrighteningWillingBernesemountaindog",
            "https://gfycat.com/TimelyBonyAtlasmoth",
            "https://gfycat.com/GreenFamiliarDog",
            "https://gfycat.com/FreeEntireLhasaapso",
            "https://gfycat.com/DefinitiveOffbeatBlacklab",
            "https://gfycat.com/WigglyAffectionateBeardeddragon",
            "https://gfycat.com/FixedJadedBlueandgoldmackaw",
            "https://gfycat.com/ScornfulCleverFrog",
            "https://gfycat.com/IndelibleAgreeableGalapagostortoise",
            "https://gfycat.com/IdolizedContentBlackbuck",
            "https://gfycat.com/GenerousAjarBinturong ",
            "https://gfycat.com/BoldConventionalAustraliansilkyterrier",
            "https://gfycat.com/BossySecondaryAtlanticridleyturtle",
            "https://gfycat.com/SleepyNextCutworm",
            "https://gfycat.com/CalculatingHarmoniousGander",
            "https://gfycat.com/WellinformedIndelibleAmethystsunbird ",
            "https://gfycat.com/TimelyThoughtfulArcticwolf",
            "https://gfycat.com/SadBarrenEgg",
            "https://gfycat.com/SmartFatherlyCalf",
            "https://gfycat.com/ForthrightUnknownIridescentshark",
            "https://gfycat.com/FoolishOldfashionedGull",
            "https://gfycat.com/PhysicalGranularHyrax",
            "https://gfycat.com/MiserlyPiercingBoa",
            "https://gfycat.com/HeftyWebbedKomododragon",
            "https://gfycat.com/IllinformedAnotherFulmar",
            "https://gfycat.com/WideJointElectriceel",
            "https://gfycat.com/FairMassiveIggypops ",
            "https://gfycat.com/GreatMiniatureLeveret ",
            "https://gfycat.com/WideeyedWellmadeIggypops ",
            "https://gfycat.com/OfficialImpracticalHeron",
            "https://gfycat.com/LiquidSinfulAmurminnow",
            "https://gfycat.com/MeagerUnkemptCattle",
            "https://gfycat.com/AnyOrganicCatbird",
            "https://gfycat.com/ExcitableReflectingDuckling",
            "https://gfycat.com/CrispHotCaecilian",
            "https://gfycat.com/LightheartedMildDuiker",
            "https://gfycat.com/PitifulPolishedLcont",
            "https://gfycat.com/MetallicHideousGiantschnauzer",
            "https://gfycat.com/WeeDismalEyas",
            "https://gfycat.com/WindingHealthyGoral",
            "https://gfycat.com/EducatedFailingGemsbok ",
            "https://gfycat.com/RevolvingLeafyCow",
            "https://gfycat.com/ClearcutFemaleAmethystsunbird",
            "https://gfycat.com/LoneTameCaracal ",
            "https://gfycat.com/CompleteShrillAtlanticspadefish",
            "https://gfycat.com/ShadowyPaltryCopperbutterfly",
            "https://gfycat.com/UniformWelllitAmericanquarterhorse ",
            "https://gfycat.com/BlindScientificArizonaalligatorlizard ",
            "https://gfycat.com/MemorableSmoggyKillifish",
            "https://gfycat.com/SharpTastyFinnishspitz",
            "https://gfycat.com/InfantileBewitchedGrouper",
            "https://gfycat.com/SneakyBrokenHapuku",
            "https://gfycat.com/NeedyImmaterialCats",
            "https://gfycat.com/JauntyMagnificentBassethound",
            "https://gfycat.com/ForcefulFreshFluke",
            "https://gfycat.com/FrequentFamiliarGreatwhiteshark",
            "https://gfycat.com/GenuineEcstaticKawala",
            "https://gfycat.com/ThreadbareThoughtfulAsianlion",
            "https://gfycat.com/CoolAptCivet",
            "https://gfycat.com/MindlessSophisticatedCats",
            "https://gfycat.com/shadowyinfinitejapanesebeetle",
            "https://gfycat.com/hoarsecavernouscuscus",
            "https://gfycat.com/antiquesoftjaguarundi",
            "https://gfycat.com/granddefenselesskawala",
            "https://gfycat.com/firstcandidleafhopper",
            "https://gfycat.com/idolizedangelicleafcutterant",
            "https://gfycat.com/hardtofindposhavocet",
            "https://gfycat.com/vigilantqueasyleopard",
            "https://gfycat.com/mediumdimcygnet",
            "https://gfycat.com/linedgraybarebirdbat"]

        self.bot.golcha_joochan_gif = ["https://64.media.tumblr.com/2c33c38af5dce11489851532da286526/49083d489dab8ac6-50/s250x400/c32c3ed0a16e1f756fdf31e5cb11f25437be8f0b.gif",
            "https://64.media.tumblr.com/b8ae7388fffd66c19999686ac7a1aac6/ff9b924952edb88f-6c/s250x400/466b4f08403a990a70b57ebef74f7cd9b04bb5e7.gif",
            "https://64.media.tumblr.com/3e9f4cc9ea2a8e01d994c1f17959eb3d/b3c20c3fafcec14c-7b/s250x400/5459ec19455098b92df21d844b59221871d9a6f0.gif",
            "https://64.media.tumblr.com/78ec9c4d4489c673b18e35a2461237a6/7b42ab1871c2458c-ca/s400x600/5389237c135dbe1b5af9db8c2ee82c8214d9eeb8.gif",
            "https://64.media.tumblr.com/68a1f0013c421095fb7dafe0aee25e97/7b42ab1871c2458c-c8/s400x600/d0c717c3bf288fd057f40ec08b36d32743659b7b.gif",
            "https://gfycat.com/dirtysmartkarakul",
            "https://gfycat.com/silveraccurateenglishpointer",
            "https://gfycat.com/BlandVagueBarnowl",
            "https://gfycat.com/favoriteevilgoosefish",
            "https://gfycat.com/narrowmagnificentflatcoatretriever",
            "https://64.media.tumblr.com/d8bba3877e658a14d4d1746044e1120f/19d9412bb00b32b4-76/s250x400/211d5350c54191058804a62052b08ee9e6264f74.gif",
            "https://64.media.tumblr.com/d0746d407e5be37b431b10888e41a049/ca198a95ae7ad60b-dc/s250x400/512e5a86097d38f896af0aa08900030d42cdc7d5.gif",
            "https://64.media.tumblr.com/12e9b9c65fee8d71481d5997815a56f2/cb73fa872427ce4a-11/s250x400/8b3602fe48ed5d212203cd7f66df54aaa1ff341c.gif",
            "https://64.media.tumblr.com/0a96987d8ebbed6acda59083bc601681/259ac045404f5916-1e/s400x600/d18f7baf16cc7759a4aa730caa987199a3805f66.gif",
            "https://64.media.tumblr.com/e7232590d8be8a21946b71034141988a/020f7b17338f6291-52/s250x400/b18d1062804c5cc28ab26bc04c0f42d428ad0503.gif",
            "https://tenor.com/bscu4.gif",
            "https://tenor.com/bscu0.gif",
            "https://tenor.com/bscvf.gif",
            "https://tenor.com/bscyw.gif",
            "https://tenor.com/bjzBa.gif",
            "https://tenor.com/bd7ke.gif",
            "https://tenor.com/bd7j1.gif",
            "https://tenor.com/bf7sP.gif",
            "https://tenor.com/bgNOj.gif",
            "https://tenor.com/bgNOJ.gif",
            "https://gfycat.com/KlutzyDisastrousBluetickcoonhound",
            "https://gfycat.com/UnrealisticFrenchBeagle",
            "https://gfycat.com/GreedyBrownKillerwhale",
            "https://gfycat.com/WeightyWhirlwindDolphin",
            "https://gfycat.com/UnrulyWellinformedChafer",
            "https://gfycat.com/SecretInsidiousGoa",
            "https://gfycat.com/UnpleasantDishonestAzurevasesponge",
            "https://gfycat.com/LeftPessimisticHare",
            "https://gfycat.com/SomeTheseHedgehog",
            "https://gfycat.com/RepulsiveBlackandwhiteIcelandichorse",
            "https://gfycat.com/SnoopyTimelyHogget",
            "https://gfycat.com/GiftedLoathsomeAlpinegoat",
            "https://gfycat.com/PrestigiousTidyEuropeanfiresalamander",
            "https://gfycat.com/SpiritedClosedBilby",
            "https://gfycat.com/PlasticWelldocumentedEland",
            "https://gfycat.com/MisguidedUnfoldedInganue",
            "https://gfycat.com/DeadlyRepulsiveJuliabutterfly",
            "https://gfycat.com/NastyDishonestAfricanjacana",
            "https://gfycat.com/IllustriousNegativeHoverfly",
            "https://gfycat.com/AstonishingEuphoricCornsnake",
            "https://gfycat.com/ImaginativeAdvancedHoopoe",
            "https://gfycat.com/DesertedFilthyAmericancrayfish",
            "https://gfycat.com/TartAltruisticFritillarybutterfly",
            "https://gfycat.com/HandsomeGreedyLice",
            "https://gfycat.com/SimplisticBlindAmericanbadger",
            "https://gfycat.com/FailingAthleticElver",
            "https://gfycat.com/ChubbyEachBluewhale",
            "https://gfycat.com/WillingVigorousBichonfrise",
            "https://gfycat.com/SleepyGranularAllensbigearedbat",
            "https://gfycat.com/IncomparableHugeKoodoo",
            "https://gfycat.com/CookedUncomfortableAnteater",
            "https://gfycat.com/AnchoredBeautifulAfricanharrierhawk",
            "https://gfycat.com/IdenticalAbleGnatcatcher",
            "https://gfycat.com/JaggedCreepyDeer",
            "https://gfycat.com/HandyBewitchedGonolek",
            "https://gfycat.com/DeadlySparseJunebug",
            "https://gfycat.com/BaggyLawfulCarpenterant",
            "https://gfycat.com/AnguishedCarefulAntarcticfurseal",
            "https://gfycat.com/JampackedGleamingAmericanbulldog",
            "https://gfycat.com/CostlyBarrenImperatorangel",
            "https://gfycat.com/OrderlyDismalDeinonychus",
            "https://gfycat.com/WideLimpingBlackandtancoonhound",
            "https://gfycat.com/ThirdDemandingCat",
            "https://gfycat.com/PiercingQualifiedCrossbill",
            "https://gfycat.com/FriendlyMiserlyLeopardseal",
            "https://gfycat.com/RegalBelatedIceblueredtopzebra",
            "https://gfycat.com/LiveCelebratedDove",
            "https://gfycat.com/PinkAdeptFrog",
            "https://gfycat.com/RealHighlevelAvians",
            "https://gfycat.com/TimelySadHomalocephale",
            "https://gfycat.com/SinfulSparklingGarpike",
            "https://gfycat.com/TemptingMemorableKiwi",
            "https://gfycat.com/RemarkableSpottedFugu", 
            "https://gfycat.com/GrippingAngelicHen",
            "https://gfycat.com/DownrightGlossyHellbender",
            "https://gfycat.com/ShortFarawayCow",
            "https://gfycat.com/MedicalUnsungChicken ",
            "https://gfycat.com/windylankyakitainu ",
            "https://gfycat.com/ComfortableScaryBorzoi",
            "https://gfycat.com/WickedHospitableBlackmamba",
            "https://gfycat.com/CrispAllCuscus ",
            "https://gfycat.com/AltruisticBabyishBrownbutterfly",
            "https://gfycat.com/WhitePoliteIslandwhistler",
            "https://gfycat.com/SaneRequiredEider",
            "https://gfycat.com/FatherlyGeneralJavalina",
            "https://gfycat.com/LeafyInexperiencedEthiopianwolf",
            "https://gfycat.com/FormalAcceptableAtlanticbluetang",
            "https://gfycat.com/DistortedInconsequentialAsianlion",
            "https://gfycat.com/ClassicMintyAssassinbug",
            "https://gfycat.com/DistantZigzagLhasaapso",
            "https://gfycat.com/RipeConsciousDugong",
            "https://gfycat.com/ComposedEmptyAfricanharrierhawk",
            "https://gfycat.com/WholeDarkAoudad",
            "https://gfycat.com/GaseousCloseBlackfootedferret",
            "https://gfycat.com/LazyResponsibleLadybird",
            "https://gfycat.com/shylimitedkronosaurus",
            "https://gfycat.com/tiredindolenthornshark",
            "https://gfycat.com/alarmingannualeasternnewt",
            "https://gfycat.com/wellmadedeepbluetonguelizard",
            "https://gfycat.com/selfreliantgrayanteater",
            "https://gfycat.com/MiserableGregariousAmbushbug",
            "https://gfycat.com/JadedScaryArrowworm",
            "https://gfycat.com/BasicQualifiedBlowfish",
            "https://gfycat.com/DefiniteWeeArgentinehornedfrog",
            "https://gfycat.com/severalsolideuropeanpolecat",
            "https://gfycat.com/unsteadypoliteitaliangreyhound",
            "https://gfycat.com/enormousshadyflatcoatretriever",
            "https://gfycat.com/ellipticalallgoldenmantledgroundsquirrel",
            "https://gfycat.com/clumsyhandsomeblacklab",
            "https://gfycat.com/whirlwindpitifulcaterpillar"]

        self.bot.golcha_seungmin_gif = ["https://gfycat.com/MiserlyZealousCockatiel",
            "https://gfycat.com/SmoggyHelpfulCoral",
            "https://gfycat.com/PossibleBeneficialHippopotamus",
            "https://gfycat.com/UnnaturalRectangularIndianhare",
            "https://gfycat.com/OpulentWiltedCoypu",
            "https://gfycat.com/WillingCarefreeGrebe",
            "https://gfycat.com/CompassionateFrigidEider",
            "https://gfycat.com/WearySaneHusky",
            "https://gfycat.com/TightReadyGalapagostortoise",
            "https://gfycat.com/AdmirablePaleAffenpinscher",
            "https://gfycat.com/LeftInexperiencedKawala",
            "https://gfycat.com/ClassicBlissfulAtlanticsharpnosepuffer",
            "https://gfycat.com/ApprehensiveCookedEgg",
            "https://gfycat.com/QueasyFittingBeaver",
            "https://gfycat.com/MelodicHarmfulErne",
            "https://gfycat.com/GrotesqueSoggyCollie",
            "https://gfycat.com/AffectionateBoringGecko",
            "https://gfycat.com/FragrantTerrificAruanas",
            "https://gfycat.com/VeneratedObeseInsect",
            "https://gfycat.com/UnevenClutteredCentipede",
            "https://gfycat.com/IdealNarrowBird",
            "https://gfycat.com/UnnaturalQuestionableGallowaycow",
            "https://gfycat.com/NiftyThornyGoat",
            "https://gfycat.com/UnripeBitterDiscus",
            "https://gfycat.com/ParallelTenderAlabamamapturtle",
            "https://gfycat.com/HarmoniousShrillKiskadee",
            "https://gfycat.com/DigitalValidJellyfish",
            "https://gfycat.com/JovialDimpledAmethystsunbird",
            "https://gfycat.com/EvilWindingCricket",
            "https://gfycat.com/PlasticWhoppingAtlanticblackgoby",
            "https://gfycat.com/EquatorialThisFoxterrier",
            "https://gfycat.com/BreakableFewFritillarybutterfly",
            "https://gfycat.com/OffbeatFondGonolek",
            "https://gfycat.com/CleverGlumHart",
            "https://gfycat.com/HastyRadiantHamadryas",
            "https://gfycat.com/FailingLegalHectorsdolphin",
            "https://gfycat.com/PolishedPitifulBlackbird",
            "https://gfycat.com/DimpledFantasticBordercollie",
            "https://gfycat.com/OblongMasculineBengaltiger",
            "https://gfycat.com/CommonEasygoingHog",
            "https://gfycat.com/FrenchRapidCaribou",
            "https://gfycat.com/NeighboringGoldenIridescentshark",
            "https://gfycat.com/SpectacularColorfulAmericancrayfish",
            "https://gfycat.com/AggressiveTightFlee",
            "https://gfycat.com/SpiffyUniqueChinesecrocodilelizard",
            "https://gfycat.com/CreepyJealousBrownbutterfly",
            "https://gfycat.com/EthicalSharpIchthyosaurs",
            "https://gfycat.com/BowedVagueBurro",
            "https://gfycat.com/CharmingAggravatingCavy",
            "https://gfycat.com/UncommonHeartyGermanshorthairedpointer",
            "https://gfycat.com/FlippantWelldocumentedAmberpenshell",
            "https://gfycat.com/InsignificantEnergeticDogfish",
            "https://gfycat.com/ReflectingGlossyClumber",
            "https://gfycat.com/FancyFantasticElectriceel",
            "https://gfycat.com/ScholarlyFlamboyantAmericanlobster",
            "https://gfycat.com/WarmUnfitBuckeyebutterfly",
            "https://gfycat.com/PinkHarmlessBurro",
            "https://gfycat.com/PoshWholeGrouse",
            "https://gfycat.com/HomelyEarlyKillerwhale",
            "https://gfycat.com/HatefulLinearAbalone",
            "https://gfycat.com/TenderDisloyalAmericanalligator",
            "https://gfycat.com/AggravatingKlutzyDolphin",
            "https://gfycat.com/UnequaledAngryFalcon",
            "https://gfycat.com/FarJubilantCockroach",
            "https://gfycat.com/TartMatureBoutu",
            "https://gfycat.com/LavishAllIndochinahogdeer",
            "https://gfycat.com/FailingShortFairybluebird",
            "https://gfycat.com/ActivePoliteBrant",
            "https://gfycat.com/ComfortableFavorableGoldfinch",
            "https://gfycat.com/PettyFocusedBaleenwhale",
            "https://gfycat.com/WeepyLiveArawana",
            "https://gfycat.com/PotableUglyArawana",
            "https://gfycat.com/DeterminedVariableBarbet",
            "https://gfycat.com/LazyAdeptDolphin",
            "https://gfycat.com/HeavenlyGlumAnkole",
            "https://gfycat.com/HomelyHeartyEasternnewt",
            "https://gfycat.com/WeeklyScentedIndigowingedparrot",
            "https://gfycat.com/QuerulousBriefChupacabra",
            "https://gfycat.com/BigheartedBareCapeghostfrog",
            "https://gfycat.com/TameMedicalFinch",
            "https://gfycat.com/LiveBelovedArabianhorse",
            "https://gfycat.com/WarpedPoshKitten",
            "https://gfycat.com/FrayedFirmIndianringneckparakeet",
            "https://gfycat.com/RegularSneakyElectriceel",
            "https://gfycat.com/ImaginativeBrokenCutworm",
            "https://gfycat.com/FoolhardyDifferentAmethystsunbird",
            "https://gfycat.com/CompetentAccurateBengaltiger",
            "https://gfycat.com/MeekLameHippopotamus",
            "https://gfycat.com/RemorsefulNecessaryGyrfalcon",
            "https://gfycat.com/UnluckyComposedHoneybee",
            "https://gfycat.com/UntimelyUnripeBlacklemur",
            "https://gfycat.com/OldEvilAnura",
            "https://gfycat.com/scentedgrouchyape",
            "https://gfycat.com/SpectacularSlipperyCrocodileskink",
            "https://gfycat.com/AdventurousPowerlessBushsqueaker",
            "https://gfycat.com/giganticthirstyblackmamba",
            "https://gfycat.com/lonealertabyssiniangroundhornbill",
            "https://gfycat.com/amusedclosedblackfish",
            "https://gfycat.com/shabbyscarceamoeba",
            "https://gfycat.com/indolentthinblobfish"]

        self.bot.golcha_tag_gif = ["https://gfycat.com/PinkHospitableFinwhale",
            "https://gfycat.com/SoreCrispBlackfish",
            "https://gfycat.com/UnderstatedOrangeKoala",
            "https://gfycat.com/LazyLavishDogfish",
            "https://gfycat.com/AdvancedNeighboringAkitainu",
            "https://tenor.com/8Zad.gif",
            "https://tenor.com/bygVf.gif",
            "https://tenor.com/5r3M.gif",
            "https://tenor.com/buDyn.gif",
            "https://tenor.com/bwxhA.gif",
            "https://gfycat.com/SoftSimplisticAmericansaddlebred",
            "https://gfycat.com/ObedientTameIbizanhound",
            "https://gfycat.com/ShimmeringMiserableArcticseal",
            "https://gfycat.com/SimplePowerfulIndianpalmsquirrel",
            "https://gfycat.com/PossibleVainDouglasfirbarkbeetle",
            "https://gfycat.com/SecondhandQuaintGhostshrimp",
            "https://gfycat.com/SardonicImmaculateHog",
            "https://gfycat.com/UnfoldedWarmheartedDartfrog",
            "https://gfycat.com/UntriedIncomparableIvorybilledwoodpecker",
            "https://gfycat.com/YellowSeveralGalapagosdove",
            "https://gfycat.com/AbsoluteThoseAsianconstablebutterfly",
            "https://gfycat.com/FocusedExemplaryFirebelliedtoad",
            "https://gfycat.com/EnormousAgreeableCobra",
            "https://gfycat.com/KlutzyDaringCottontail",
            "https://gfycat.com/ThankfulFewCoyote",
            "https://gfycat.com/TestySmoothBengaltiger",
            "https://gfycat.com/BareMindlessCamel",
            "https://gfycat.com/DemandingKeenApatosaur",
            "https://gfycat.com/ExaltedIncompleteJabiru",
            "https://gfycat.com/OrangeUnrulyChupacabra",
            "https://gfycat.com/DelightfulIcyCurassow",
            "https://gfycat.com/GlamorousUnhappyBlackbear",
            "https://gfycat.com/ExaltedAlertFossa",
            "https://gfycat.com/SevereInferiorHusky",
            "https://gfycat.com/TornObeseBushsqueaker",
            "https://gfycat.com/HeftyRaggedErmine",
            "https://gfycat.com/EverlastingBaggyEft",
            "https://gfycat.com/FatherlyUnsightlyFox",
            "https://gfycat.com/RareVapidGosling",
            "https://gfycat.com/SingleDirectEastsiberianlaika",
            "https://gfycat.com/DefensiveMasculineGalapagostortoise",
            "https://gfycat.com/ImpartialMasculineCranefly",
            "https://gfycat.com/DisloyalQueasyKitten",
            "https://gfycat.com/LividUnrealisticAmurratsnake",
            "https://gfycat.com/DeliciousConfusedFrenchbulldog",
            "https://gfycat.com/SilentClassicGull",
            "https://gfycat.com/FamousGoldenGander",
            "https://gfycat.com/FrankJovialGiantschnauzer",
            "https://gfycat.com/SorrowfulHalfIchneumonfly",
            "https://gfycat.com/OrangeInnocentGazelle",
            "https://gfycat.com/GleefulMealyCrocodile",
            "https://gfycat.com/ThoroughGrandioseAcornweevil",
            "https://gfycat.com/ReflectingLikableGraysquirrel",
            "https://gfycat.com/ZigzagMetallicGraywolf",
            "https://gfycat.com/UglyFavorableHammerkop",
            "https://gfycat.com/ShimmeringEsteemedEelelephant",
            "https://gfycat.com/ImpoliteFatherlyHornedviper",
            "https://gfycat.com/GlumAridIbisbill",
            "https://gfycat.com/BriskShadyLemming",
            "https://gfycat.com/ShadyUntimelyCapeghostfrog",
            "https://gfycat.com/QualifiedWatchfulBigmouthbass",
            "https://gfycat.com/SecondhandLividBantamrooster",
            "https://gfycat.com/CoolWhimsicalHornbill",
            "https://gfycat.com/EmbellishedSparseArgali",
            "https://gfycat.com/WindyKindheartedDodo",
            "https://gfycat.com/BlandRichIriomotecat",
            "https://gfycat.com/HeartySardonicHydatidtapeworm",
            "https://gfycat.com/RealQuestionableCrocodileskink",
            "https://gfycat.com/MisguidedOnlyLeveret",
            "https://gfycat.com/PoisedZealousGroundhog",
            "https://gfycat.com/AromaticSingleCrocodile",
            "https://gfycat.com/DeadlyHideousAnemone",
            "https://gfycat.com/SimpleDetailedEwe",
            "https://gfycat.com/CooperativeScaredIvorygull",
            "https://gfycat.com/SerpentineLimpIcelandgull",
            "https://gfycat.com/ConstantPlumpCowrie",
            "https://gfycat.com/AblePolishedGrayling",
            "https://gfycat.com/OrnateNegligibleAmericancurl",
            "https://gfycat.com/ZanyAlarmedAustraliankelpie",
            "https://gfycat.com/PreciousGlamorousGnu",
            "https://gfycat.com/DecimalAngelicGreathornedowl",
            "https://gfycat.com/FamousHopefulHorsefly",
            "https://gfycat.com/WebbedUltimateCowbird",
            "https://gfycat.com/ImpartialTediousCommabutterfly",
            "https://gfycat.com/ActualDecisiveEasternnewt",
            "https://gfycat.com/BelatedDistantCollardlizard",
            "https://gfycat.com/HilariousSeparateFlickertailsquirrel",
            "https://gfycat.com/GrandioseVerifiableDingo",
            "https://gfycat.com/DeepBeautifulIcefish",
            "https://gfycat.com/CluelessSparseAnglerfish",
            "https://gfycat.com/NimbleFewAlabamamapturtle",
            "https://gfycat.com/AngryUnluckyFossa",
            "https://gfycat.com/IdioticImaginativeDartfrog",
            "https://gfycat.com/JollyHighlevelAnaconda",
            "https://gfycat.com/NervousFittingConch",
            "https://gfycat.com/cookedajardogwoodclubgall",
            "https://gfycat.com/leanspectacularkiskadee",
            "https://gfycat.com/angryopenkilldeer",
            "https://gfycat.com/satisfiedcalculatinghoneybadger",
            "https://gfycat.com/responsiblegraveboubou"]

        self.bot.golcha_y_gif = ["https://64.media.tumblr.com/55e48640d01cecdcc5023d2747fefd09/020f7b17338f6291-31/s250x400/6ce3f7faa33d5fd05105c26f30b92edaebd1324a.gif",
            "https://64.media.tumblr.com/18ee933ba44cd38c78266d09ba5e775a/28c3096dd7c4a6ca-ae/s250x400/8d1eb15ab4d52d1f8108712b3f350f928ef31263.gif",
            "https://64.media.tumblr.com/106f3731492a46879ae77b192c262857/28c3096dd7c4a6ca-69/s250x400/91ae13796478d7ae3a78e123928058f1818af070.gif",
            "https://64.media.tumblr.com/33cbe957d13ce460dbb7486ec19fd1c9/49083d489dab8ac6-75/s250x400/d91de7cd0bd2115ccb53309897dbbb9354ab0fbe.gif",
            "https://64.media.tumblr.com/e3db72e153db96d71cc9f874baf76acd/da6d02ac512c0c52-52/s250x400/f0701e828b2a9c8f08fe6101c94e67ab7b3f3912.gif",
            "https://gfycat.com/SaltyCavernousCornsnake",
            "https://gfycat.com/ThatIndelibleIrukandjijellyfish",
            "https://gfycat.com/DenseParallelKawala",
            "https://gfycat.com/JitteryAggressiveEelelephant",
            "https://gfycat.com/HairyFluidGrizzlybear",
            "https://gfycat.com/ZanyBraveJaguarundi",
            "https://gfycat.com/OddballPotableHogget",
            "https://gfycat.com/ColorlessImpressionableEwe",
            "https://gfycat.com/HomelyRectangularBarbet",
            "https://gfycat.com/DecisivePastHagfish",
            "https://gfycat.com/FittingInferiorBoilweevil",
            "https://gfycat.com/CourageousViciousGalapagossealion",
            "https://gfycat.com/WholeIdealisticBlackbuck",
            "https://gfycat.com/DishonestNervousBaiji",
            "https://gfycat.com/DefensiveHeavyAntbear",
            "https://gfycat.com/OpulentAnyLeopard",
            "https://gfycat.com/EnormousCrispAmethystinepython",
            "https://gfycat.com/WhiteJollyAmericanbobtail",
            "https://gfycat.com/HeavenlyScentedAyeaye",
            "https://gfycat.com/BleakDefenselessGhostshrimp",
            "https://gfycat.com/FreshSpiffyEchidna",
            "https://gfycat.com/IndelibleCreepyIberianlynx",
            "https://gfycat.com/ElementaryGlisteningCutworm",
            "https://gfycat.com/IdenticalMeagerDeer",
            "https://gfycat.com/UnhappyJitteryLeafcutterant",
            "https://gfycat.com/WellinformedAdeptArctichare",
            "https://gfycat.com/PleasingWastefulIlsamochadegu",
            "https://gfycat.com/DecimalChubbyGalapagosmockingbird",
            "https://gfycat.com/DefensiveValuableInexpectatumpleco",
            "https://gfycat.com/LikableSeveralBlackbear",
            "https://gfycat.com/ShowyRepentantFeline",
            "https://gfycat.com/VigilantPeriodicBorderterrier",
            "https://gfycat.com/CourteousSmallBarasinga",
            "https://gfycat.com/KeyJovialAmericansaddlebred",
            "https://gfycat.com/ThisBeautifulArmyworm",
            "https://gfycat.com/WelcomeBrightKilldeer",
            "https://gfycat.com/BaggyRichAppaloosa",
            "https://gfycat.com/SardonicMasculineAsianpiedstarling ",
            "https://gfycat.com/SharpCheeryGourami ",
            "https://gfycat.com/SoupySilkyBighornedsheep",
            "https://gfycat.com/CornyIncompleteGrizzlybear",
            "https://gfycat.com/ReliableWarmheartedInchworm ",
            "https://gfycat.com/ScholarlyPoisedCirriped",
            "https://gfycat.com/GreatCharmingIvorybackedwoodswallow ",
            "https://gfycat.com/CreepyScalyCattle",
            "https://gfycat.com/OddTanChinchilla",
            "https://gfycat.com/WebbedDeterminedGossamerwingedbutterfly",
            "https://gfycat.com/FeminineHarmfulBushbaby",
            "https://gfycat.com/NarrowPlayfulCavy",
            "https://gfycat.com/MilkyDescriptiveArabianwildcat",
            "https://gfycat.com/RewardingAltruisticGelding",
            "https://gfycat.com/MessyBareKangaroo",
            "https://gfycat.com/SoggyInsidiousCrossbill ",
            "https://gfycat.com/NeatExhaustedBinturong",
            "https://gfycat.com/GentleEasyDutchsmoushond",
            "https://gfycat.com/ExhaustedVengefulAlaskankleekai",
            "https://gfycat.com/SecretOpenLadybug",
            "https://gfycat.com/WildExcellentBass",
            "https://gfycat.com/DrearyImpoliteAmbushbug ",
            "https://gfycat.com/WellgroomedAdventurousKronosaurus",
            "https://gfycat.com/AlienatedInformalAmericankestrel",
            "https://gfycat.com/BlissfulWildHorseshoecrab",
            "https://gfycat.com/VagueElasticGiantschnauzer",
            "https://gfycat.com/AggravatingAlienatedGrouse",
            "https://gfycat.com/UnhappyPerfectChafer",
            "https://gfycat.com/AdvancedCloseBeauceron ",
            "https://gfycat.com/AffectionateUnhappyIndianspinyloach",
            "https://gfycat.com/VacantIdealFirefly",
            "https://gfycat.com/ShabbyAcidicArcticfox",
            "https://gfycat.com/WarlikeGlassAmericanbadger",
            "https://gfycat.com/LonelyTastyItalianbrownbear",
            "https://gfycat.com/BigheartedGrimCapeghostfrog",
            "https://gfycat.com/GleefulAridBluetonguelizard",
            "https://gfycat.com/UnselfishIllinformedFlatfish",
            "https://gfycat.com/GlamorousFearfulBaboon",
            "https://gfycat.com/ShinyNeedyAfricanharrierhawk",
            "https://gfycat.com/DiscreteQueasyAmethystsunbird",
            "https://gfycat.com/ImportantYawningEider",
            "https://gfycat.com/PerfumedThornyHornedviper",
            "https://gfycat.com/UnripeFlippantCowrie",
            "https://gfycat.com/OffensiveRapidIchidna",
            "https://gfycat.com/ThoseWildFlycatcher",
            "https://gfycat.com/AbandonedFatAsiantrumpetfish",
            "https://gfycat.com/ThreadbareParallelGoldenretriever",
            "https://gfycat.com/SlightClutteredBoilweevil",
            "https://gfycat.com/TeemingDefinitiveGalapagoshawk",
            "https://gfycat.com/BeneficialThriftyDarwinsfox",
            "https://gfycat.com/VapidDearestJabiru",
            "https://gfycat.com/ForsakenRequiredGourami",
            "https://gfycat.com/ThatRashIndigobunting",
            "https://gfycat.com/necessaryenchantinggrayreefshark",
            "https://gfycat.com/tautesteemedindianabat",
            "https://gfycat.com/smoggycourageouscaimanlizard",
            "https://gfycat.com/poorafraidantelope",
            "https://gfycat.com/victoriousbonybaleenwhale",
            "https://gfycat.com/perfectidleindianpangolin",
            "https://gfycat.com/whimsicalfoolishindianrhinoceros",
            "https://gfycat.com/rawhideousaustraliankestrel",
            "https://gfycat.com/carefreeincomparableimpala",
            "https://gfycat.com/bigdarlinghyrax"]
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
            "https://64.media.tumblr.com/fecf7ab54b06c8007e225826d4fc503f/tumblr_pmmmgdUDLa1wvslp2o3_250.gif",
            "https://tenor.com/view/kevin-moon-the-boyz-the-boyz-kevin-canadian-singer-handsome-gif-17250561"]

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
            "https://tenor.com/view/sangyeon-tbz-sangyeon-the-boyz-the-boyz-sangyeon-kpop-gif-17450017",
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
            "https://tenor.com/view/younghoon-chanhee-the-boyz-tbz-tbz-younghoon-gif-18984986",
            "https://tenor.com/view/younghoon-chanhee-the-boyz-tbz-tbz-younghoon-gif-18984986",
            "https://tenor.com/view/the-boyz-younghoon-kim-younghoon-kpop-handsome-gif-15713938",
            "https://tenor.com/view/%EB%8D%94%EB%B3%B4%EC%9D%B4%EC%A6%88-the-boyz-younghoon-kim-younghoon-kpop-gif-17717615",
            "https://tenor.com/view/younghoon-the-boyz-kim-younghoon-kpop-cute-gif-17490371",
            "https://tenor.com/view/younghoon-the-boyz-tbz-gif-19303453",
            "https://cdn.discordapp.com/attachments/815387335419494431/816923992043683840/image0.gif",
            "https://64.media.tumblr.com/a200291aa466e4532833e9e9b2299137/ee10f750df78267f-6b/s540x810/7e7af3a03fcb0dffda22fd2b8fb76bfa6898cb6e.gif",
            "https://64.media.tumblr.com/b9a5ae4e16c39489e685db1dcad60b93/ee10f750df78267f-bf/s540x810/898bf5b727984311b68670cfa4860c8dcae9effb.gif",
            "https://64.media.tumblr.com/e457d0abe2e00f6744695080cc20a71b/15b224548b6f596d-7f/s400x600/666653f6f90eff9370ff3b2ca13309b4f349933d.gif",
            "https://64.media.tumblr.com/d512d355fd7517c2211c797cb035b4ad/3e3c8c440d69ef1d-30/s540x810/f236107ca3cc2188a48e04d4d68c121e2652d79c.gif",
            "https://64.media.tumblr.com/3c4d0ee5bc3e9a7f8b08fab45c2b06e2/3e3c8c440d69ef1d-3c/s540x810/38e08b07d50bb4654b4a04dd53e6b521ec5e3fb2.gif",
            "https://64.media.tumblr.com/02d89c18492db7d521276ee2b9a9511b/3e3c8c440d69ef1d-cc/s540x810/618a0ac26f99773f8664f6010617149286998a4a.gif",
            "https://64.media.tumblr.com/6be26e6b290c42e952c8981df3206409/3e3c8c440d69ef1d-30/s540x810/a9244ce15f784d2883c59a3453270a683c18dd0f.gif",
            "https://64.media.tumblr.com/f7c9e155b850aaef95cf87d9d08bd176/56efc61063453b3f-ae/s640x960/32afce67bcb58af8af279cf4f070889d2efeb5d4.gif",
            "https://64.media.tumblr.com/89bd9c334d04c5206ef0eb2e0973bf4e/dc12d9ade3530ddd-c9/s400x600/192d130ee99e40bc3396ef465eb23b13290f1362.gif",
            "https://64.media.tumblr.com/3602816f137cc585380d944dc3390efe/tumblr_p0k3kpftan1wvslp2o4_500.gif",
            "https://data.whicdn.com/images/322832844/original.gif",
            "https://66.media.tumblr.com/9f95aff2ab925c453d50c8feaf0f7cf7/4449f6155ef6b7cb-1e/s400x600/883343d45cbd819a390250fa520aa073dc819501.gif",
            "https://64.media.tumblr.com/945bc7478026da7c86eb0f371ea983ff/8da340711f62c008-dd/s400x600/38172ba3fc0d130b5cf3a6e46e796f701d9ff563.gif",
            "https://data.whicdn.com/images/320880041/original.gif",
            "https://data.whicdn.com/images/322769161/original.gif",
            "http://pa1.narvii.com/7002/42cee87ae642a079fdecfeafbda2fded361d62f9r1-268-334_00.gif",
            "https://data.whicdn.com/images/323183931/original.gif",
            "https://cdn.kstarlive.com/image/1580375532856-0.gif",
            "https://64.media.tumblr.com/a594a9370e31cb598eac3d7dfa35a34a/tumblr_p0u24rbBvm1wvzntio3_400.gif",
            "https://cdn140.picsart.com/329166859007201.gif?to=min&r=640"]

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
            "https://tenor.com/view/%EB%8D%94%EB%B3%B4%EC%9D%B4%EC%A6%88-the-boyz-hyunjae-lee-jaehyun-kpop-gif-16153899",
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
            "https://64.media.tumblr.com/27cda92df9e2733e9141c9b07e688ad8/3bc76cabf7f13e6f-99/s250x400/f1e88a311f3343532e09ae936b031ce6136d3477.gif",
            "https://tenor.com/view/handsome-the-boyz-juyeon-tbz-kpop-gif-17904898"]

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
            "https://tenor.com/view/choi-chanhee-new-the-boyz-the-boyz-gif-18810560",
            "https://tenor.com/view/choi-chanhee-new-the-boyz-the-boyz-gif-18810545",
            "https://tenor.com/view/chanhee-new-the-boyz-the-boyz-gif-18009021",
            "https://tenor.com/view/chanhee-choi-new-the-boyz-the-boyz-gif-18810536",
            "https://tenor.com/view/choi-chanhee-new-the-boyz-the-boyz-gif-18810560",
            "https://tenor.com/view/choi-chanhee-new-the-boyz-the-boyz-gif-18810551",
            "https://64.media.tumblr.com/51cd41167c5a80d1a4d56de90810a84c/tumblr_p93qg00PK91xsj5gko5_r6_250.gif",
            "https://tenor.com/view/chanhee-the-boyz-new-the-boyz-gif-18009008",
            "https://tenor.com/view/kiss-the-boyz-chanhee-new-nyu-gif-16642851",
            "https://tenor.com/view/the-boyz-new-choi-chanhee-main-vocalist-kpop-gif-16028891"]

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
            "https://64.media.tumblr.com/88422061b3c901b056d8c11a53bc4f31/2af42dbe1d769b2e-60/s250x400/270ed86bfb6a516954abee78b0dc56b163421b35.gif",
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
            "https://tenor.com/view/sunwoo-gif-19843755",
            "https://tenor.com/view/sunwoo-imitating-kevin-sunwoo-tbz-the-boyz-gif-20224449",
            "https://tenor.com/view/tbz-the-boyz-sunwoo-kim-sunwoo-amazed-gif-17863040",
            "https://tenor.com/view/sunwoo-kim-sunwoo-tbzhour-tbz-the-boyz-gif-18439976",
            "https://tenor.com/view/sunwoo-the-boyz-kim-sunwoo-dance-gif-20085120",
            "https://tenor.com/view/sunwoo-kim-sunwoo-the-boyz-tbz-kpop-gif-17323830",
            "https://tenor.com/view/sunwoo-the-boyz-kim-sunwoo-gif-18352599",
            "https://tenor.com/view/sunwoo-the-boyz-tbz-sunwoo-sunwooeating-sunu-gif-18876590",
            "https://64.media.tumblr.com/77efa11b27effcd431d5c4be4e468702/498cad7066bde806-00/s250x400/7db3d004cb9613538f359fa4f271f092577f0dd6.gif",
            "https://64.media.tumblr.com/7a9675cc77811ce55d82d543fd3d866f/498cad7066bde806-0b/s250x400/c65722cb9b531bfad0579eea5f32cdb2764f35bb.gif",
            "https://64.media.tumblr.com/8cd7f2253b32e9cc36f05795705b4919/498cad7066bde806-a2/s250x400/8a25460c159522dd3c8f92fb32c895edb4306e94.gif",
            "https://64.media.tumblr.com/7fc74ed8e4b1f009dec49d3f2d115e19/1da6e28388181611-48/s250x400/3a69eeab0227e03d877c3c07c95c2ff029a75298.gif",
            "https://64.media.tumblr.com/bf53391ac9949818d0ab41d43e6f58b9/1da6e28388181611-4e/s250x400/61352b08fea3ad73ba312df34e8307839ffc0541.gif",
            "https://64.media.tumblr.com/0e80a2295f2605fd8ca6d2c253113f0f/498cad7066bde806-d4/s250x400/046826d10ec9634fc01a5191d611bacaeeb0b75a.gif",
            "https://64.media.tumblr.com/d0c49d486518d6b289c905db98950d1f/498cad7066bde806-02/s250x400/a44a2725b1269434c6827d0d8b93130d8db5da6b.gif"]

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

        self.bot.theboyz_hwall_gif = ["https://64.media.tumblr.com/a95c260a8d7e2d69e2f9f17325553854/tumblr_oxzsetn9nC1wrrz1eo1_400.gif",
            "https://64.media.tumblr.com/735dd97c8f7ba1ce6bef398579019789/tumblr_p556z9StHn1wvslp2o5_r1_250.gif",
            "https://64.media.tumblr.com/c71a1e7e99ebf90a79436bf82d776934/tumblr_p556z9StHn1wvslp2o7_r2_250.gif",
            "https://64.media.tumblr.com/8f3d24c31b5a726e4138bd44f1d54144/tumblr_p556z9StHn1wvslp2o6_r1_250.gif",
            "https://64.media.tumblr.com/a8182f25ccacf80fb0374cf886dd5459/tumblr_p3xv88WcGS1wl2fq0o1_400.gif",
            "https://64.media.tumblr.com/8b848139508618daec6d7db517b32b43/tumblr_pkc35iNQbB1xi376ko1_250.gif",
            "https://64.media.tumblr.com/1e4214f6b5cc236db1c799c1e49e769b/tumblr_pkc35iNQbB1xi376ko4_250.gif",
            "https://64.media.tumblr.com/ea8b324c6325c4e05c9dd21c15e0de1d/tumblr_pmftreM5Aa1wvslp2o3_r1_250.gif",
            "https://64.media.tumblr.com/12144c75b98a04b9882429b90421a9e7/tumblr_p9izg6d3iY1wl2fq0o1_250.gif",
            "https://64.media.tumblr.com/15b90d0657037dce08b487fd076d152f/tumblr_p9izg6d3iY1wl2fq0o7_250.gif"]
    
        self.bot.theboyz_group_gif = ["https://tenor.com/view/theboyz-giftheboyz-theboyzhd-tbz-gif-18694836",
            "https://tenor.com/view/the-boyz-kpop-boyz-the-greeting-cute-gif-12285048",
            "https://64.media.tumblr.com/c4ef728387c5a91e77b7af30cdd5d6a1/tumblr_inline_pmsbgxr5hW1w0xass_500.gif",
            "https://64.media.tumblr.com/521c8e16e78cdcea9ae10c2fa70f7cbd/7db70edc0587b5f4-c8/s250x400/da2a36365113bcdbfcc222ee9dcc1901eb8b2bf7.gif",
            "https://64.media.tumblr.com/8f7c652b6d790577d80b40b2af8eaaa8/tumblr_pbvq5f0dCO1swg2mjo8_r1_400.gif",
            "https://64.media.tumblr.com/6945754e41f2cb892dd381aec3c07974/fa1b10438eef1e02-f8/s400x600/cf2a8fc5762b02b1b179d3161bfe69336bfd1a4a.gif",
            "https://64.media.tumblr.com/a673f6c01b474dc19b9ee2f578c66e2e/tumblr_pbvq5f0dCO1swg2mjo9_r1_400.gif",
            "https://static.tumblr.com/65bfd79d6c50c879910e19c58488c024/kizoio0/6Gpp3n960/tumblr_static_tumblr_static_2rh9vzehnw8w04kwgsg0wk0g0_focused_v3.gif"]
    #. P1Harmony
        self.bot.p1harmony_intak_gif = ["https://cdn.discordapp.com/attachments/800206337073479690/800261657557074000/image0.gif",
            "https://cdn.discordapp.com/attachments/800206337073479690/800261657880166400/image1.gif",
            "https://cdn.discordapp.com/attachments/800206337073479690/800261658508394516/image2.gif",
            "https://cdn.discordapp.com/attachments/800206337073479690/800261658890731550/image3.gif",
            "https://cdn.discordapp.com/attachments/800206337073479690/800261758714380358/image0.gif",
            "https://cdn.discordapp.com/attachments/800206337073479690/800261759302500392/image1.gif",
            "https://tenor.com/view/p1harmony-maniac-p1harmony-intak-intak-gif-19859801"]

        self.bot.p1harmony_jiung_gif = ["https://cdn.discordapp.com/attachments/800206376210661406/800262168904859668/image0.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262169299910686/image1.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262170029195304/image2.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262170419396628/image3.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262170691764244/image4.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262170952466452/image5.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262218733322270/image0.gif",
            "https://tenor.com/view/jiung-choi-jiung-p1h-p1harmony-gif-20392814",
            "https://tenor.com/view/jiung-p1h-p1harmony-choi-jiung-gif-20392787",
            "https://tenor.com/view/jiung-choi-jiung-p1h-p1harmony-gif-20392855",
            "https://tenor.com/view/p1harmony-siren-p1harmony-siren-jiung-choi-jiung-gif-19887400"]

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
            "https://tenor.com/view/keeho-mini-heart-%E0%B8%A1%E0%B8%B4%E0%B8%99%E0%B8%B4%E0%B8%AE%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B8%97-%E0%B8%81%E0%B8%B5%E0%B9%82%E0%B8%AE-p1h-gif-19524452",
            "https://tenor.com/view/p1harmony-siren-p1harmony-siren-yoon-keeho-keeho-gif-19887399"]

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
            "https://cdn.discordapp.com/attachments/800206797604519936/800264279206264842/image0.gif",
            "https://tenor.com/view/theo-p1harmony-theo-sheep-choi-taeyang-taeyang-gif-20166435"]
    
        self.bot.p1harmony_group_gif = ["https://tenor.com/view/thoe-p1harmony-theo-keeho-p1h-gif-19371047",
            "https://tenor.com/view/p1harmony-gif-19761328",
            "https://tenor.com/view/p1h-p1harmony-gif-19927014",
            "https://tenor.com/view/p1harmony-kpop-siren-siren-p1harmony-p1harmony-siren-gif-19887489",
            "https://tenor.com/view/p1harmony-siren-p1harmony-p1harmony-siren-siren-kpop-gif-19887478",
            "https://tenor.com/view/p1harmony-siren-siren-p1harmony-p1harmony-siren-kpop-gif-19887473",
            "https://tenor.com/view/p1harmony-siren-p1harmony-siren-jongseob-kim-jongseob-gif-19887398"]
    #. Seventeen
        self.bot.seventeen_scoups_gif = ["https://tenor.com/view/s-coups-seventeen-handsome-gif-13332018",
            "https://tenor.com/view/scoups-seventeen-svt-jicheol-okay-gif-11883208",
            "https://tenor.com/view/seungcheol-kpop-homerun-scoups-seventeen-gif-18815323",
            "https://tenor.com/view/s-coups-choi-seungcheol-kpop-cute-serious-face-gif-15763940",
            "https://tenor.com/view/choi-seungcheol-time-scoups-seventeen-svt-gif-16207048",
            "https://tenor.com/view/scoups-seventeen-seungcheol-smile-cute-gif-15501046",
            "https://tenor.com/view/seungcheol-choi-scoups-gif-18064505",
            "https://tenor.com/view/scoups-gif-18097690",
            "https://tenor.com/view/seungcheol-scoups-seventeen-scoups-cheol-dancing-gif-17675232",
            "https://tenor.com/view/scoups-seungcheol-seventeen-hearts-love-gif-15673610",
            "https://tenor.com/view/seungcheol-scoups-svt-gif-18064497",
            "https://gfycat.com/disastrousoldbats",
            "https://tenor.com/view/seungcheol-svt-seventeen-funny-firework-gif-8747127",
            "https://tenor.com/view/svt-seventeen-kpop-ccg-ccg1-gif-19005762",
            "https://tenor.com/view/seventeen-svt-ccg-kpop-scoups-gif-15519817",
            "https://tenor.com/view/scoups-seventeen-left-and-right-seventeen-choi-seungcheol-seventeen-scoups-seventeen-gif-19125334",
            "https://tenor.com/view/seventeenscoups-seungcheol-choiseungcheol-seventeenseungcheol-leftnrightseventeen-gif-18121123"]

        self.bot.seventeen_wonwoo_gif = ["https://tenor.com/view/jeon-wonwoo-wonwoo-wonu-jeon-wonu-seventeen-gif-13528172",
            "https://tenor.com/view/wonwoo-jeon-wonwoo-seventeen-seventeen-wonwoo-gif-18117134",
            "https://tenor.com/view/seventeen-wonwoo-jeon-won-woo-lead-rapper-sub-vocalist-gif-17355993",
            "https://tenor.com/view/wonwoo-seventeen-seventeen-falling-flower-seventeen-wonwoo-jeon-wonwoo-gif-19117555",
            "https://tenor.com/view/seventeen-wonwoo-jeon-won-woo-lead-rapper-sub-vocalist-gif-17580514",
            "https://tenor.com/view/wonwoo-seventeen-cute-gif-15490179",
            "https://tenor.com/view/kpop-seventeen-wonwoo-jeon-wonwoo-handsome-gif-17677215",
            "https://tenor.com/view/kpop-seventeen-wonwoo-jeon-wonwoo-handsome-gif-15563909",
            "https://tenor.com/view/wonwoo-seventeen-cute-handsome-kpop-gif-16124120",
            "https://tenor.com/view/wonwoo-seventeen-smile-gif-15468801",
            "https://tenor.com/view/seventeen-wonwoo-gif-17976335",
            "https://tenor.com/view/wonwoo-jeon-wonwoo-seventeen-seventeen-wonwoo-gif-18117161",
            "https://tenor.com/view/wonwoo-jeon-wonwoo-wonu-seventeen-svt-gif-18115775",
            "https://tenor.com/view/seventeen-wow-wonwoo-wow-hoshi-wow-wonwoo-seventeen-hoshi-seventeen-gif-20037407",
            "https://tenor.com/view/svtszone-wonwoo-wonwoo-crying-svt-wonwoo-wonwoo-seventee-gif-17694336",
            "https://tenor.com/view/wonwoo-seventeen-24h-seventeen-wonwoo-seventeen-jeon-wonwoo-gif-19434628",
            "https://tenor.com/view/wonwoo-seventeen-heart-love-kpop-gif-9089134",
            "https://tenor.com/view/wonwoo-handsome-cute-cool-cutie-gif-16661313",
            "https://tenor.com/view/sleepy-wonwoo-svt-seventeen-yawn-gif-15464698",
            "https://tenor.com/view/wonwoo-mingyu-seventeen-gif-8982788",
            "https://tenor.com/view/wonwoo-seventeen-my-my-seventeen-wonwoo-seventeen-my-my-gif-19125780",
            "https://tenor.com/view/seventeen-wonwoo-jeon-won-woo-lead-rapper-sub-vocalist-gif-17581708"]

        self.bot.seventeen_mingyu_gif = ["https://tenor.com/view/seventeen-svt-kpop-ccg-kim-mingyu-gif-14815665",
            "https://tenor.com/view/min7yu-mingyu-seventeen-svt-gif-18317581",
            "https://tenor.com/view/seventeen-kim-mingyu-hot-gif-12464691",
            "https://tenor.com/view/mingyu-seventeen-pose-pot-cute-gif-15519436",
            "https://tenor.com/view/kim-mingyu-gyu-mingyu-seventeen-hot-gif-12535346",
            "https://tenor.com/view/seventeen-mingyu-kim-mingyu-handsome-gif-16071110",
            "https://tenor.com/view/mingyu-gyu-gyu-kim-smile-svt-seventeen-cute-gif-13510257",
            "https://tenor.com/view/seventeen-mingyu-kim-mingyu-gif-15422130",
            "https://tenor.com/view/kpop-seventeen-svt-kim-mingyu-mingyu-gif-15502818",
            "https://tenor.com/view/seventeen-mingyu-kim-mingyu-gif-16009204",
            "https://tenor.com/view/wonwoo-mingyu-seventeen-gif-8982788",
            "https://tenor.com/view/mingyu-korean-thumbs-up-approve-gif-10004095",
            "https://tenor.com/view/seventeen-mingyu-kim-mingyu-kpop-handsome-gif-15460246",
            "https://tenor.com/view/mingyu-seventeen-my-my-seventeen-mingyu-seventeen-kim-mingyu-gif-19125837",
            "https://64.media.tumblr.com/a2a6c2fc395b83b1e9c54fd32c1bd4cd/12416bda98f57482-65/s540x810/7b685e4b2785ba3c179e9b6f7ef0cf95c214613e.gif"]

        self.bot.seventeen_vernon_gif = ["https://tenor.com/view/vernon-seventeen-kpop-wink-gif-5144884",
            "https://tenor.com/view/seventeen-vernon-vernon-pose-gif-12266891",
            "https://tenor.com/view/vernon-hansol-vernon-chwe-seventeen-kpop-cute-gif-16190243",
            "https://tenor.com/view/seventeen-kpop-17-hansol-vernon-gif-8043534",
            "https://tenor.com/view/vernon-hansol-kpop-seventeen-mingyu-gif-7622748",
            "https://tenor.com/view/seventeen-vernon-hansol-vernon-chwe-kpop-cute-gif-16650650",
            "https://tenor.com/view/svt-seventeen-vernon-gif-18312901",
            "https://tenor.com/view/vernon-seventeen-seventeen-vernon-hansol-hansol-chwe-gif-18117310",
            "https://tenor.com/view/seventeen-vernon-vernon-chwe-hansol-hansol-chwe-gif-18117314",
            "https://tenor.com/view/henggarae-seventeen-vernon-svt-%EC%84%B8%EB%B8%90%ED%8B%B4-gif-17712664",
            "https://tenor.com/view/vernon-seventeen-kpop-gif-5080446",
            "https://gfycat.com/concernedfeistybunting",
            "https://gfycat.com/warlikehelplesskoi",
            "https://c.tenor.com/F65o_FQ_m-wAAAAM/seventeen-vernon.gif",
            "https://c.tenor.com/XTERrBCsJSUAAAAM/vernon-seventeen.gif",
            "https://c.tenor.com/8xmCegFFLhQAAAAM/vernon-seventeen.gif",
            "https://c.tenor.com/ldoUdTYKIp4AAAAM/vernon-seventeen.gif",
            "https://c.tenor.com/9Ioc6K-xqpQAAAAM/vernon-seventeen.gif",
            "https://c.tenor.com/nwBeqfh2vrkAAAAM/vernon-seventeen.gif",
            "https://giphy.com/gifs/vernon-hansol-chwe-LNHifSMammT2U",
            "https://giphy.com/gifs/vernon-hansol-chwe-NVIob9GyE1lHa",
            "https://64.media.tumblr.com/7548bf869991809ccba8f6c960ac62b2/544aa913eaa695f8-94/s540x810/1d0e65ac8514523723370bb9670d1e416a1173c1.gif",
            "https://64.media.tumblr.com/d73a9a4f7df6edd53b8d030ac3018324/544aa913eaa695f8-a1/s540x810/9c853e95e00e52ea9b14a708d5a1d777495d69f4.gif",
            "https://64.media.tumblr.com/1d884a4eea0520b89a8cff4e2445b04e/tumblr_pjj9quz8ZT1qbst9go3_400.gif"]

        self.bot.seventeen_woozi_gif = ["https://tenor.com/view/woozi-musician-artist-music-sing-gif-5680981",
            "https://tenor.com/view/seventeen-woozi-smile-cute-gif-15490074",
            "https://tenor.com/view/woozi-dance-kpop-gif-14972216",
            "https://tenor.com/view/woozi-svt-gif-18020196",
            "https://tenor.com/view/woozi-seventeen-ji-hoon-lee-jihoon-woozi-seventeen-gif-19434481",
            "https://tenor.com/view/woozi-musician-artist-music-sing-gif-5680979",
            "https://tenor.com/view/seventeen-woozi-kpop-gif-9061880",
            "https://tenor.com/view/jicheol-hi-seventeen-woozi-cute-gif-11758352",
            "https://tenor.com/view/kpop-seventeen-woozi-lee-jihoon-handsome-gif-15536382",
            "https://tenor.com/view/woozi-gif-9896801",
            "https://tenor.com/view/jicheol-sad-seventeen-woozi-cute-gif-11758353",
            "https://tenor.com/view/seventeen-woozi-playing-gif-10314518",
            "https://tenor.com/view/woozi-dance-kpop-gif-14972216",
            "https://tenor.com/view/kpop-seventeen-woozi-lee-jihoon-handsome-gif-15536389",
            "https://cdn.discordapp.com/attachments/812175781341560853/812194110537596928/woozi.gif",
            "https://giphy.com/gifs/kpop-svt-woozi-eGOqv0O6QKRUMibuvJ"]

        self.bot.seventeen_jeonghan_gif = ["https://tenor.com/view/jeonghan-seventeen-cute-smile-peekaboo-gif-16321993",
            "https://tenor.com/view/seventeen-jeonghan-gif-19104339",
            "https://tenor.com/view/svtszone-jeonghan-jeonghan-svt-seventeen-jeonghan-confused-gif-17684082",
            "https://tenor.com/view/jeonghan-yoon-long-hair-seventeen-peace-flower-gif-17299312",
            "https://tenor.com/view/seventeen-jeonghan-yoon-jeonghan-sexy-hot-gif-15291690",
            "https://tenor.com/view/seventeen-yoon-jeonghan-jeonghan-hot-kpop-gif-15291691",
            "https://tenor.com/view/muzzzies-jeonghan-seventeen-svt-jeonghan-hitting-camera-gif-18968596",
            "https://tenor.com/view/seventeen-jeonghan-gif-19104339",
            "https://tenor.com/view/jeonghan-gif-18595241",
            "https://tenor.com/view/jeonghan-choking-seungkwan-choking-jeonghan-svt-jeonghan-seventeen-jeonghan-gif-17675262",
            "https://tenor.com/view/yoon-jeonghan-jeonghan-seventeen-kpop-blonde-gif-19089551",
            "https://tenor.com/view/seventeen-seventeen-jeonghan-yoon-jeonghan-jeonghan-kpop-gif-15498170",
            "https://gfycat.com/antiqueunpleasantinganue-seventeen-jeonghan",
            "https://gfycat.com/blankevilindianrhinoceros",
            "https://gfycat.com/whiterevolvingasiantrumpetfish",
            "https://tenor.com/view/jeong-han-seventeen-my-my-seventeen-jeonghan-seventeen-my-my-gif-19125647",
            "https://64.media.tumblr.com/5883ad93f4f695da55c67d663a642df5/d5909d563ff3f1ec-77/s540x810/8be58212ceb6e6255c950cc691015d88908d9c26.gif",
            "https://64.media.tumblr.com/6f778c09e885cad20a653938b376858e/d5909d563ff3f1ec-a9/s540x810/422f37691b6ca1a67d5c672a50a62bafd96836a3.gif",
            "https://64.media.tumblr.com/64f2f1a09fd6ebad6bb2b5afc41cb470/d5909d563ff3f1ec-b9/s540x810/3aaed04f37ef35beafe1f11b09f9a5f92a03b9e1.gif",
            "https://64.media.tumblr.com/014ae9e474a0d5de9287e46645b13609/12416bda98f57482-30/s540x810/0177847632b300051ebf0edb711f3fd5e146bad1.gif"]

        self.bot.seventeen_joshua_gif = ["https://tenor.com/view/seventeen-joshua-joshua-hong-hong-ji-soo-lead-vocalist-gif-17103306",
            "https://tenor.com/view/joshua-joshua-seventeen-seventeen-joshua-joshua-hong-seventeen-gif-19512745",
            "https://tenor.com/view/seventeen-joshua-seventeen-joshua-svt-svt-joshua-gif-19508629",
            "https://tenor.com/view/josh-joshua-joshua-hong-josh-hong-seventeen-gif-15121872",
            "https://tenor.com/view/joshua-hong-seventeen-svt-jisoo-laugh-gif-10308342",
            "https://tenor.com/view/joshua-joshua-seventeen-seventeen-svt-joshua-confused-gif-17675614",
            "https://tenor.com/view/joshua-hong-svt-seventeen-kpop-korean-gif-10998286",
            "https://tenor.com/view/joshua-seventeen-love-gif-15877342",
            "https://tenor.com/view/seventeen-joshua-joshua-hong-hong-ji-soo-lead-vocalist-gif-17704358",
            "https://tenor.com/view/joshua-hong-svt-seventeen-gif-10998281",
            "https://tenor.com/view/choco-seventeen-joshua-kpop-chocolate-gif-11662308",
            "https://tenor.com/view/ji-soo-joshua-seventeen-left-and-right-seventeen-left-and-right-seventeen-gif-19114951",
            "https://64.media.tumblr.com/772171e67ee98707a0338e208862013b/0647cdf4181ab186-a6/s400x600/a31d9539bf30dab343014332a86fb409f1f3ea8f.gif",
            "https://64.media.tumblr.com/e947b4c37c0b557b19e1d095db822f2e/760bff8848442216-63/s400x600/29e23bc63c3919aa27f7b6e6a9bce15b0cb1bef3.gif"]

        self.bot.seventeen_dk_gif = ["https://tenor.com/view/seventeen-dk-dokyeom-lee-seok-min-vocalist-gif-17218035",
            "https://tenor.com/view/seventeen-dk-dokyeom-laugh-gif-15556452",
            "https://tenor.com/view/dk-dokyeom-seventeen-cute-gif-15454895",
            "https://tenor.com/view/seventeen-dk-dokyeom-smile-cute-gif-15498964",
            "https://tenor.com/view/seventeen-dk-dokyeom-kpop-gif-15556457",
            "https://tenor.com/view/seventeen-dk-dokyeom-lee-seokmin-left-and-right-gif-17758259",
            "https://tenor.com/view/dk-smile-cute-kpop-gif-15454900",
            "https://tenor.com/view/dk-seventeen-svt-dab-dance-gif-15464702",
            "https://tenor.com/view/dk-dokyeom-seventeen-kpop-smile-gif-15455037",
            "https://tenor.com/view/seventeen-dk-dokyeom-lee-seok-min-vocalist-gif-17225558",
            "https://tenor.com/view/seventeen-dokyeom-dk-fix-hair-gif-15498955",
            "https://tenor.com/view/seventeen-dk-seventeen-dk-lee-seokmin-pledis-entertainment-gif-17279788",
            "https://tenor.com/view/seventeen-dk-dokyeom-lee-seok-min-vocalist-gif-17741933",
            "https://64.media.tumblr.com/d6983f5db91ad038d4fac0f64645e78f/0fa48e4845010ee6-25/s500x750/05adfb566fde2f438ae9cdb107a0ba5cb7eb0edc.gif",
            "https://giphy.com/gifs/kpop-k-pop-seventeen-l0ErUhF5QGceuqSwo",
            "https://64.media.tumblr.com/51e9e220e7e97fd5584fd3c2edc29cef/4ef9177dcd70d655-ad/s500x750/acfadc8f8cdff555b2a8df17e1bcab140b2ce7c1.gif",
            "https://64.media.tumblr.com/e02610c18faa6b49da03a9cbb25b8e7f/4ef9177dcd70d655-6f/s500x750/f7a5e7c596b1e942481343b84ce1ce047e51d987.gif",
            "https://64.media.tumblr.com/4f0116f3dde03669912a5ee1df8d4855/4ef9177dcd70d655-25/s500x750/891a5fbc7b3fd13ae501383bf325ee1a0f0adf54.gif",
            "https://64.media.tumblr.com/4f0116f3dde03669912a5ee1df8d4855/4ef9177dcd70d655-25/s500x750/891a5fbc7b3fd13ae501383bf325ee1a0f0adf54.gif",
            "https://64.media.tumblr.com/dcdb3f046b02f18467b55ad08a820e4f/b702552a6cb5b989-72/s400x600/6306b9113aad4b0a4fba416edc8b43a8048f5db5.gif",
            "https://64.media.tumblr.com/4eb7c4f2ef646c22b603f86e33f7633d/b702552a6cb5b989-7a/s400x600/0a89dfb5d9eed00e14e0a52273b7861ba1c0d286.gif",
            "https://64.media.tumblr.com/9d276b9714aa818f27bc93ce3148f25a/b702552a6cb5b989-93/s400x600/8bf7545794ee2cc331953329fb78313a1d11c8a3.gif",
            "https://64.media.tumblr.com/921f6e46df461f2068989e029e688e8e/9f91cba612e2a294-d3/s400x600/f6630543699e1e320584d9b4d7c26ec49d4b96d3.gif",
            "https://64.media.tumblr.com/424a80a66c701a002bf3f8739afa10ab/1c79149f70d7f8f6-fe/s250x400/b4e22647dce75c24957bd76e2529545ab809d322.gif",
            "https://64.media.tumblr.com/775a7fbc4cf4b7ee8b78e61f0e5eb6b7/1c79149f70d7f8f6-aa/s250x400/c652679602d809b71cc77fa58b05c98a5b89d17d.gif",
            "https://64.media.tumblr.com/8b3527e1f26ec0fe3e1f9db0e981e69d/1c79149f70d7f8f6-f0/s250x400/bff76d14ca46c5f2d0f4bcf1dbd46e061eb421c5.gif",
            "https://64.media.tumblr.com/eec14f07f966f0ba29b84c639848554e/be29939023e06360-c8/s400x600/01634b21bc93ea7bf959f438b8dd3c59c7107d01.gif",
            "https://64.media.tumblr.com/ac9b440b49fd1f7ec333b1e4d1d9e313/d008bf0111427939-4d/s250x400/5bfb4046f1a4403e239e9db1baabe90e49b9a392.gif",
            "https://64.media.tumblr.com/b3248adc3aa6ea262e55419703ccc06a/d008bf0111427939-c3/s250x400/a7d70e355fd5642012811a71e348194f73f9d23d.gif",
            "https://64.media.tumblr.com/2f9c10be0a067a69cac1de57b53cb157/d008bf0111427939-20/s250x400/e665425de5dda6eac33db366ba10bcb9af465b4d.gif",
            "https://64.media.tumblr.com/437629c402fa6e7e53da59e3a497d877/c69cb9e310746a97-f5/s400x600/05c216c51bbb57f85e76cc2300ff40e808957546.gif",
            "https://64.media.tumblr.com/0b03c436e1d82d41e09c8165f6f94cba/1f4d50e1f1b62b2c-ab/s400x600/826fcc0473c486cd4249aa82365bfc9453c19340.gif"]

        self.bot.seventeen_seungkwan_gif = ["https://tenor.com/view/%EC%8A%B9%EA%B4%80-seungkwan-%EC%84%B8%EB%B8%90%ED%8B%B4-seventeen-%EB%B6%80%EC%8A%B9%EA%B4%80-gif-18205335",
            "https://tenor.com/view/performance-stage-music-dance-dance-performance-gif-15895493",
            "https://tenor.com/view/seungkwan-side-eye-caratiz-boo-seungkwan-kpop-gif-19587947",
            "https://tenor.com/view/kpop-boo-seungkwan-boo-seungkwan-seventeen-gif-12059496",
            "https://tenor.com/view/boo-seungkwan-cute-seventeen-kpop-gif-15461084",
            "https://tenor.com/view/svt-seventeen-kpop-ccg-ccg1-gif-19005803",
            "https://tenor.com/view/booricano-seungkwan-shocked-seungkwan-shock-seungkwan-stare-seungkwan-staring-gif-18996227",
            "https://tenor.com/view/booricano-seungkwan-punch-seungkwan-punching-screen-seungkwan-gif-18996177",
            "https://tenor.com/view/seungkwan-seventeen-seventeen-seungkwan-boo-seungkwan-seventeen-boo-seungkwan-gif-19982867",
            "https://tenor.com/view/%EC%8A%B9%EA%B4%80-seungkwan-%EC%84%B8%EB%B8%90%ED%8B%B4-seventeen-%EB%B6%80%EC%8A%B9%EA%B4%80-gif-18205383",
            "https://tenor.com/view/performance-stage-music-dance-dance-performance-gif-15895495",
            "https://tenor.com/view/bskfiles-seungkwan-seventeen-boo-seungkwan-seventeen-seungkwan-gif-20206149",
            "https://tenor.com/view/%EC%8A%B9%EA%B4%80-seungkwan-%EC%84%B8%EB%B8%90%ED%8B%B4-seventeen-%EB%B6%80%EC%8A%B9%EA%B4%80-gif-18205399",
            "https://tenor.com/view/boo-seungkwan-seungkwan-seventeen-oh-my-gawd-suprised-gif-13403075"]

        self.bot.seventeen_hoshi_gif = ["https://tenor.com/view/hoshi-seventeen-cat-paw-cute-gif-15513589",
            "https://tenor.com/view/hoshi-seventeen-kwon-soonyoung-smile-kpop-gif-16362661",
            "https://tenor.com/view/hoshi-soonyoung-kwon-soonyoung-seventeen-gif-15135297",
            "https://tenor.com/view/kwon-soonyoung-hoshi-seventeen-kpop-cute-gif-15763948",
            "https://tenor.com/view/seventeen-kpop-hoshi-gif-9426790",
            "https://tenor.com/view/seventeen-wow-wonwoo-wow-hoshi-wow-wonwoo-seventeen-hoshi-seventeen-gif-20037407",
            "https://tenor.com/view/hoshi-kpop-seventeen-seventeen-hoshi-soonyoung-gif-14750860",
            "https://tenor.com/view/hoshi-seventeenhoshi-kwonsoonyoung-horanghae-hoshihoranghae-gif-18120878",
            "https://tenor.com/view/kpop-hoshi-seventeen-kwon-soonyoung-handsome-gif-17675637",
            "https://tenor.com/view/thumbs-up-soonyoung-kwon-hoshi-seventeen-gif-9298464",
            "https://tenor.com/view/hoshi-seventeen-seventeen-hoshi-soonyoung-kwon-soonyoung-gif-18117255",
            "https://tenor.com/view/hoshi-seventeen-kpop-gif-15556451",
            "https://tenor.com/view/hoshi-wink-seventeen-hoshi-seventeen-hoshi-wink-kwon-soonyoung-soonyoung-gif-18098031",
            "https://tenor.com/view/hoshi-seventeen-going-seventeen-hoshi-going-seventeen-seventeen-hoshi-gif-20167573",
            "https://tenor.com/view/seventeen-going-seventeen-gose-hoshi-soonyoung-gif-17008409",
            "https://tenor.com/view/seventeen-hoshi-kwon-soon-young-leader-main-dancer-gif-17311478",
            "https://tenor.com/view/seventeen-hoshi-abs-gif-17-gif-19933095",
            "https://gfycat.com/sarcasticappropriategaur",
            "https://64.media.tumblr.com/70f8bd6be632741225c955439f3ba947/43ff1411b29809a1-3c/s540x810/cc69b87026e3c26a949e108a251e55f050eddd07.gif",
            "https://64.media.tumblr.com/7075359d55ce86215714749d8fd59aba/43ff1411b29809a1-ae/s540x810/dea547eaaa238f9318e50776f731d9a748a89698.gif",
            "https://64.media.tumblr.com/7beac75bb388c22b1cb6bead9227f9a7/43ff1411b29809a1-4c/s540x810/b1ce333cd42a53b6c40d2079bc4c86e53fe35cf5.gif",
            "https://64.media.tumblr.com/243e87481947e87787ba98dde178d8bd/43ff1411b29809a1-7e/s540x810/559440eb9332ca977328abaf1fc764aa002f544e.gif",
            "https://64.media.tumblr.com/fdb720766c0d21d83da617910fcadc2c/43ff1411b29809a1-7b/s540x810/b0d39493c895b5e7e081bc675ba0c2513ea8c59f.gif"]

        self.bot.seventeen_jun_gif = ["https://tenor.com/view/junhui-jun-seventeen-svt-seventeen-jun-gif-17166952",
            "https://tenor.com/view/seventeen-jun-wen-junhui-kpop-cute-gif-16830644",
            "https://tenor.com/view/seventeen-jun-junhui-wen-junhui-kpop-gif-15498186",
            "https://tenor.com/view/wen-junhui-junhui-jun-seventeen-smile-gif-17005986",
            "https://tenor.com/view/svt-seventeen-kpop-ccg-ccg1-gif-19005846",
            "https://tenor.com/view/junhui-seventeen-svt-kpop-gif-10751052",
            "https://tenor.com/view/nicesnupi-jun-svt-jun-jun-svt-seventeen-jun-gif-19159473",
            "https://tenor.com/view/seventeen-jun-seventeen-jun-and-joshua-jun-junhui-junhui2x-speed-gif-19689672",
            "https://tenor.com/view/jun-seventeen-jun-seventeen-moon-junhwi-gif-19434376",
            "https://tenor.com/view/seventeen-jun-junhui-gif-15481250",
            "https://tenor.com/view/jun-seventeen-jun-svt-svt-jun-svt-china-line-jun-hui-wen-gif-13410894",
            "https://tenor.com/view/nicesnupi-seventeen-svt-going-seventeen-gose-gif-20000257",
            "https://tenor.com/view/jun-junhui-seventeen-kpop-heart-gif-13407252",
            "https://gfycat.com/afraidfrenchiberiannase-wen-junhui-seventeen",
            "https://gfycat.com/bewitchedfalseblackbuck-wen-junhui-seventeen",
            "https://gfycat.com/animatedredangelfish-seventeen-wen-junhui",
            "https://gfycat.com/charmingsizzlingbullmastiff-seventeen-wen-junhui",
            "https://gfycat.com/uniformuglybluet-seventeen-wen-junhui",
            "https://tenor.com/view/jun-wen-junhui-seventeen-oh-my-sing-gif-14128437",
            "https://64.media.tumblr.com/04334f9e1c6196f739a7e2fd82349ffa/e3ecbfb6e01493f2-2e/s400x600/3e6159241fd4b4128c5226e6985a4e632e9a07c7.gif",
            "https://64.media.tumblr.com/1b2557a34ebb7c283555bbeda9726f0d/374d82f7f6e0c436-8c/s400x600/34c4edcd2a926974aae24a434f43be3e24f8a395.gif",
            "https://64.media.tumblr.com/b38bdd2aa8349c9b8b24aef1c9938a77/374d82f7f6e0c436-65/s400x600/d219cb2a489801a0d51783a40c0aef121481107f.gif",
            "https://64.media.tumblr.com/2b3f07c1547d8101befaef9314d61cc8/374d82f7f6e0c436-bc/s400x600/83f65ec2853290228a351378724a16101f68d34f.gif",
            "https://64.media.tumblr.com/e037caa857a260ac7efeff6d4205f267/26c8029e44aebe40-c6/s250x400/ac3a522d9358e238387a31eb91f001ed31aa02df.gif",
            "https://64.media.tumblr.com/8810f2886dd00e8ee6491761e7ac686d/26c8029e44aebe40-f5/s250x400/b6a569319b6905476669298def50f37ad5499615.gif",
            "https://64.media.tumblr.com/79b4d71106af23349dd7a199257c36f9/92e816405be096b2-27/s250x400/57ba247c7eaf89c4ae345906d99f3620edd02b4a.gif",
            "https://64.media.tumblr.com/863718fbd22649be0763808519c7843d/92e816405be096b2-ad/s250x400/e6ec2190110dfef0325efa5006cb5eb107cab224.gif",
            "https://64.media.tumblr.com/9825052c6c34cce3cde13956b24a5368/92e816405be096b2-2a/s250x400/c396d30a1be84016490e6efa30e656326183cd23.gif",
            "https://64.media.tumblr.com/0a012bc8430c6efd184d58fae144ccb1/92e816405be096b2-65/s250x400/625271bf08c8a805b0f9b52d0cb7d1ba575bb4b7.gif",
            "https://64.media.tumblr.com/c8b6c98418f52c7200e8abb90e6c3e26/243afcafa21d0717-7c/s400x600/2b3500248f7dd258fe3a6b18ccdcc76e8d6ddfc5.gif",
            "https://64.media.tumblr.com/a3abbf372406215775b4674aba9533d1/243afcafa21d0717-69/s400x600/fa0bbeee07a23670196dc5ddc89c0d3da8da203c.gif",
            "https://64.media.tumblr.com/8fbac147e7e8991723a61fa89cf4575f/a3a97a6656520278-4c/s400x600/3e8e66251d28d9593671673bd9b59582e99b40b8.gif",
            "https://64.media.tumblr.com/452c10310cf7931c28145ccce3ecf9fa/a3a97a6656520278-4f/s400x600/3ac82a098eaefe6b538c2ba23cac2dd588b07ddb.gif",
            "https://64.media.tumblr.com/f2e81ca998c5169791db71056ac1bede/0b5a8266b6f38d16-3b/s400x600/52c6315670f309382526c512f8b512a6f355831d.gif",
            "https://64.media.tumblr.com/d65dcfb9aa77d3b09e9a0d5448c543e5/23d82e58bcd64a01-63/s400x600/2f430fac42784c3f21bb0051aa31756e0f426518.gif",
            "https://64.media.tumblr.com/05c43d373a233c07ca83260379616f44/23d82e58bcd64a01-02/s400x600/5253e01f67b88b23dc2974944eda92e7bbb857bf.gif",
            "https://64.media.tumblr.com/fc4c3cfbaac3c2ec44d2cf421a299a44/23d82e58bcd64a01-91/s400x600/27f74dc92158fac3094914f3cecd36e2a76ff8f2.gif",
            "https://64.media.tumblr.com/d34096e38548c73abf8a6025457c0ee3/fa0df3da4c75faf5-d3/s250x400/f9a3ec699cb696a770a6a2a533097c54f2077625.gif",
            "https://64.media.tumblr.com/eba1b60835808dd229c1b7a00401ab04/fa0df3da4c75faf5-72/s250x400/851f4fe48c5d2bed8d489826b82cb05162cf1dc9.gif",
            "https://64.media.tumblr.com/daac9ed2d8cd74ee7e7b7483c461eecf/ba8dbbe285699cf0-e7/s400x600/1953d3431bd3abd37d6249ef08e2aa7c518f0a48.gif",
            "https://64.media.tumblr.com/43ba6a343b46137c252ac93ad5a015c4/b80192dd49386c42-74/s250x400/0aea0cd0a272d41d0d3cb699e5a06b122171c6dd.gif",
            "https://64.media.tumblr.com/49f84c3e5ebcf0ce2a2a8c4c902e4a20/159cba653ca05de2-19/s400x600/b62ada2dec5385b34b40df6eb0db8e568b44421a.gif",
            "https://64.media.tumblr.com/1143c04aa224b9a6936076d76a80c3fd/cef2fafff3e1e049-cf/s250x400/eb74e9e1db9710a26b9949310508a554c055e6be.gif",
            "https://64.media.tumblr.com/94e8aa4429ee6c1b87facc532982c56c/cef2fafff3e1e049-3b/s250x400/9e3129d9d5fd87f4a227e936683e3a7c03850726.gif",
            "https://64.media.tumblr.com/c04262ccc6b4608e8edd84a2d8ccc0d4/120dbd0642a8f262-75/s400x600/b47e4156c950bc3bcf70bbd74a5e64af6aecaf4a.gif",
            "https://64.media.tumblr.com/e0e451f0aec612038dc700619a909091/6512d23b287b2e51-41/s400x600/216af084da927e6f87f72489255a5b16ca87c5b6.gif",
            "https://64.media.tumblr.com/dca75c8eb2d688be13bbf5c5eb5f599d/6512d23b287b2e51-3a/s400x600/d18a29d1374de6bfff9d6289653bbe9336bdc774.gif",
            "https://64.media.tumblr.com/ab95a1e62d658a21d293c46a38f65f35/6496313074ee7df7-3a/s250x400/7c73395eefa283474ade52e9bd769c45569bec97.gif",
            "https://64.media.tumblr.com/e8e693d70907de3b3aec5ec20884b3a0/6496313074ee7df7-64/s250x400/fe82b918e4f17b6b7707bda4009e20d298893a52.gif",
            "https://64.media.tumblr.com/ad3d99bd253d29719325a0c9237852dd/9bf10f307743baac-7e/s400x600/7b62a104de186e817644f64c5d418bdbe20dc960.gif"]

        self.bot.seventeen_the8_gif = ["https://tenor.com/view/kpop-minghao-seventeen-xu-minghao-handsome-gif-15563182",
            "https://tenor.com/view/8zones-minghao-the8-gif-18639338",
            "https://tenor.com/view/the8-xu-minghao-seventeen-bite-finger-gif-14128433",
            "https://tenor.com/view/minghao-svt-the8-seventeen-xu-minghao-gif-18929071",
            "https://tenor.com/view/minghao-pink-billboard-gift-wink-gif-19837558",
            "https://tenor.com/view/8zones-minghao-the8-gif-18638552",
            "https://tenor.com/view/the8-seventeen-xu-minghao-wave-smile-gif-16728125",
            "https://tenor.com/view/minghao-svt-the8-seventeen-kpop-gif-15464730",
            "https://tenor.com/view/kpop-minghao-seventeen-xu-minghao-handsome-gif-15824823",
            "https://tenor.com/view/the8-seventeen-handsome-cute-cool-gif-16728127",
            "https://tenor.com/view/minghao-xu-minghao-the8-seventeen-svt-gif-17346025",
            "https://tenor.com/view/minghao-the8-seventeen-the8-seventeen-svt-gif-20088190",
            "https://64.media.tumblr.com/b337ddf297f729d314fa493d7f7598d2/03c8e7411d027c2b-84/s400x600/c3b8bcf3ef2239f5f1bed89e47cdea3561777228.gif"]

        self.bot.seventeen_dino_gif = ["https://tenor.com/view/seventeen-dino-lee-chan-main-dancer-vocalist-gif-17591014",
            "https://tenor.com/view/dino-seventeen-seventeen-smile-dino-smile-seventeen-gif-20041133",
            "https://tenor.com/view/dino-seventeen-seventeen-dino-lee-chan-seventeen-snapshoot-seventeen-gif-19116959",
            "https://tenor.com/view/seventeen-dino-lee-chan-main-dancer-vocalist-gif-17704447",
            "https://tenor.com/view/dino-seventeen-dino-lee-chan-chan-dino-seventeen-chan-gif-19987833",
            "https://tenor.com/view/lee-chan-dino-seventeen-smile-cute-gif-15673658",
            "https://tenor.com/view/gifs-seven-gif-20400681",
            "https://tenor.com/view/dinoloops-dino-dino-svt-seventeen-dino-svt-gif-gif-19131074",
            "https://tenor.com/view/dino-seventeen-bangs-gif-13388669",
            "https://tenor.com/view/kpop-svt-seventeen-ccg-dino-gif-15524297",
            "https://tenor.com/view/lol-seventeen-dino-seventeen-going-seventeen-seventeen-lol-gif-20204692",
            "https://tenor.com/view/lee-chan-dino-seventeen-gif-15471840",
            "https://64.media.tumblr.com/a73658c0b300a9edc8da1e017792fe5d/9d049a3ab45f07f4-73/s400x600/097f3448463994ccf630eb951812d264ce5a07d1.gif",
            "https://64.media.tumblr.com/755893a92e50d94993708c3fc98a45de/24bbea4d6fd61d33-db/s400x600/9411934009319ae3edf9031620d028380cd4af9a.gif",
            "https://64.media.tumblr.com/7a668f27892e61feb74a2bddd4f2e2c8/24bbea4d6fd61d33-d7/s400x600/99443d4243003a0dc2f5ec7dcbeb45e96c1f0984.gif",
            "https://64.media.tumblr.com/fe14464b8abc1457de2682e877283270/24bbea4d6fd61d33-5a/s400x600/739a42c333fcc82ef4d980f93bbce0a7cd01801f.gif",
            "https://64.media.tumblr.com/aebdd74c443b1be8a3242bbfb732f15b/24bbea4d6fd61d33-d5/s400x600/5ea5879905e7f72dabe174926968be847ce2dbda.gif",
            "https://64.media.tumblr.com/b1acf3d64dc124d69b4a186e1942692e/1c5850b3002ee5c5-01/s400x600/ee7b6e04db78687734bdf757b0f2f6d88919ab67.gif",
            "https://64.media.tumblr.com/6c6c6228f5582b3a9e34162381a56055/1c5850b3002ee5c5-3b/s400x600/1135e8dfd11c47ef3ccfb011f53c23141ca9c9d7.gif"]
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
            "https://cdn.discordapp.com/attachments/805178530279325697/805180236706742342/image3.gif",
            "https://64.media.tumblr.com/35a27df70216785d3b73a21006fa275f/9236732440054ab7-87/s400x600/e94e6b3a8f3763742638aa85215660c41992f420.gif",
            "https://64.media.tumblr.com/3529ac539e5034274a9bcc2b95b336cf/tumblr_pmuz5kUPN11x8i9gko6_400.gif",
            "https://64.media.tumblr.com/35a27df70216785d3b73a21006fa275f/9236732440054ab7-87/s400x600/e94e6b3a8f3763742638aa85215660c41992f420.gif",
            "https://64.media.tumblr.com/3529ac539e5034274a9bcc2b95b336cf/tumblr_pmuz5kUPN11x8i9gko6_400.gif",
            "https://64.media.tumblr.com/f92b2a111a72953ca6cfbe0d88a32c52/tumblr_pn47mbig6E1x8i9gko8_r1_400.gif"]

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
            "https://cdn.discordapp.com/attachments/805178727222083635/805181235621920798/image1.gif",
            "https://64.media.tumblr.com/9acaa9a75572791aef0aa97d8963a2da/tumblr_pe0vqjUELp1we7cjco2_250.gif",
            "https://64.media.tumblr.com/81b7511869cbc44deae88eb2dba45609/tumblr_puqjqzvJtn1wmcyxto3_250.gif",
            "https://64.media.tumblr.com/301f130bb9bbca94227b4b5d36fd8268/tumblr_p4i8ft1nsS1we7cjco2_400.gif",
            "https://64.media.tumblr.com/d91520800e483b9a94309226716c4196/tumblr_puqjqzvJtn1wmcyxto1_250.gif",
            "https://64.media.tumblr.com/3c59f4da9bb50651773183bbf6091625/tumblr_p5aovyIXzJ1we7cjco2_400.gif",
            "https://64.media.tumblr.com/4a75da4b3b04755aff008392bca3e3f2/b594d9dbbb1f231d-ca/s250x400/282da0f1dfafc241b388105c19dde4c417a9fac7.gif",
            "https://64.media.tumblr.com/2baa554ec19d3bb4e72e995c42b2c1b3/b594d9dbbb1f231d-9d/s250x400/3c94649f0ba61242ac7ca902ad019781f5fb8f58.gif",
            "https://64.media.tumblr.com/1cb3f9121bbd731e265b1fa389d365f3/tumblr_pf9dkx1qJX1two6hzo2_400.gif",
            "https://64.media.tumblr.com/1edc5a9930578e88d1e74855054747cb/tumblr_pexvf9oVHg1x8i9gko4_250.gif",
            "https://64.media.tumblr.com/3ce5467634fb7f2d89734864013f29b5/tumblr_pdi751iWAq1we7cjco1_250.gif",
            "https://64.media.tumblr.com/46c57b191f3021e9804d6bf98a076fd9/tumblr_poqfnbLV0b1x8i9gko3_400.gif",
            "https://64.media.tumblr.com/e799940e95377e7810ce6ea43de205e0/tumblr_peydepk5lR1x1yp8ko3_250.gif",
            "https://64.media.tumblr.com/71651211f3e80ae3711ac093a2e62e25/tumblr_p69kwkKsEg1t7qu3mo2_250.gif",
            "https://64.media.tumblr.com/58b241f49f51d6638cf023633a9acc4b/tumblr_p7q23mFP9M1we7cjco4_250.gif"]

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
            "https://cdn.discordapp.com/attachments/805178992180199434/805182663136116796/image1.gif",
            "https://64.media.tumblr.com/1efe1be20dc3c9fbce84335e243f158c/21343b79ffc2efb5-cc/s400x600/b3ea32987e1366178058520544353860745be1f9.gif",
            "https://64.media.tumblr.com/dbde0cc7466ac1287760ddb4c010044d/c7779f120387f22e-c9/s250x400/3bb31f9fa081afe913a3dfe911ca3e465cfc71cb.gif",
            "https://64.media.tumblr.com/82ac1ce3a46b8eaffabde13eec7c1681/tumblr_pu358x4wyZ1y7lqmco1_250.gif",
            "https://64.media.tumblr.com/2dad052fcc53f002d62c8b33ff61e037/1bfcf2b4b41bcf38-a0/s400x600/54b4e7004b602df53f94b046fb6e83affe7c62ea.gif",
            "https://64.media.tumblr.com/843851d29558beb6cd5f5bba058cd611/tumblr_pd8l0b1oVG1x1yp8ko3_250.gif",
            "https://64.media.tumblr.com/87963ad482d35228034425fd23b97ed7/tumblr_pd8l0b1oVG1x1yp8ko1_250.gif",
            "https://64.media.tumblr.com/c1dbe277316b69b434193afa18a29ebb/tumblr_pz9mvw8CmF1w7yd36o2_400.gif",
            "https://64.media.tumblr.com/6a1a981706f33d0c0000751eb310b5e0/tumblr_py3stqZ7bd1y7lqmco2_250.gif",
            "https://64.media.tumblr.com/9315aaa8f16ce51a257c824037705851/3586c58cc04a19d1-a5/s400x600/135af7c85588ce67ee60e4862eb68ad718f67e98.gif",
            "https://64.media.tumblr.com/fcb1de7b9de44edfea3d1ef1a48cc315/3586c58cc04a19d1-06/s400x600/f765fd03dbfebfb24966b3dfb13a49d65e694e2f.gif",
            "https://64.media.tumblr.com/ee821898a3367b823bca1ed40f2190c8/tumblr_poa1qrZWac1va7u78o3_r1_400.gif",
            "https://cdn.discordapp.com/attachments/805178992180199434/813197485077692456/image0.gif"]

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
    
        self.bot.sf9_ot9_gif = ["https://tenor.com/view/sf9-sensation-feeling9-kpop-handsome-cute-gif-16808646",
            "https://gfycat.com/ornatewellwornballoonfish",
            "https://giphy.com/gifs/kpop-k-pop-k-pop-l1KsDYA3KfqJpdE7C",
            "https://giphy.com/gifs/3ohuAo3wxzDaUkQoco",
            "https://giphy.com/gifs/kpop-k-pop-k-pop-l1KsRfB5WOIG72IxO",
            "https://cdn.discordapp.com/attachments/813193512744517683/813196760180064256/image0.gif",
            "https://cdn.discordapp.com/attachments/813193512744517683/813196916661288960/image0.gif",
            "https://cdn.discordapp.com/attachments/813193512744517683/813197275723333662/image0.gif"]
    #. Shinee
        self.bot.shinee_jonghyun_gif = ["https://tenor.com/view/kim-jonghyun-jonghyun-shinee-kpop-cute-gif-15967764",
            "https://tenor.com/view/jonghyun-kim-shinee-fighting-gif-17986917",
            "https://tenor.com/view/jonghyun-kpop-shinee-heart-love-gif-9591694",
            "https://tenor.com/view/shinee-kpop-jonghyun-heart-signs-gif-11162355",
            "https://tenor.com/view/jonghyun-kim-jonghyun-shinee-kpop-handsome-gif-17083298",
            "https://tenor.com/view/shinee-jonghyun-gif-7258912",
            "https://tenor.com/view/shinee-jonghyun-smile-gif-7740406",
            "https://tenor.com/view/shinee-jonghyun-wave-hello-hey-gif-7837893",
            "https://tenor.com/view/shinee-jonghyun-kpop-topless-hot-gif-17584569",
            "https://tenor.com/view/kim-jonghyun-jonghyun-smiles-gif-14292890",
            "https://tenor.com/view/jonghyun-shinee-gif-7258937",
            "https://tenor.com/view/shinee-jonghyun-gif-7258902",
            "https://tenor.com/view/shinee-jonghyun-gif-7258901",
            "https://tenor.com/view/shinee-jonghyun-kpop-wink-winking-gif-11162160",
            "https://tenor.com/view/shinee-jonghyun-jonghyun-clapping-jonghyun-cute-faeteez-gif-19943769",
            "https://tenor.com/view/hug-big-for-you-jonghyun-gif-13110586",
            "https://tenor.com/view/shinee-jonghyun-pout-cute-nod-gif-7748510",
            "https://tenor.com/view/love-jonghyun-kim-jonghyun-precious-cute-gif-14965254",
            "https://tenor.com/view/shinee-jonghyun-jonghyun-cute-faeteez-gif-19943770",
            "https://tenor.com/view/sweet-dreams-gif-14381727",
            "https://tenor.com/view/kim-jonghyun-jonghyun-singing-gif-14221565",
            "https://tenor.com/view/shinee-jonghyun-contented-gif-7213693",
            "https://tenor.com/view/jonghyun-smiling-kim-jonghyun-gif-14965255",
            "https://tenor.com/view/jonghyun-shinee-kpop-cute-eyesmile-gif-5587614",
            "https://tenor.com/view/shinee-dino-smile-selfie-cute-gif-14476967",
            "https://tenor.com/view/jonghyun-gif-19626260",
            "https://tenor.com/view/shinee-jonghyun-gif-7258920",
            "https://tenor.com/view/gleektate-irene-jonghyun-laughing-gif-20229602",
            "https://tenor.com/view/jonghyun-reaction-screaming-gif-10344112",
            "https://tenor.com/view/jonghyun-shinee-gif-7258947",
            "https://tenor.com/view/kim-jonghyun-jonghyun-hello-gif-14221545",
            "https://tenor.com/view/jonghyun-jonghyun-shinee-jonghyun-kpop-jonghyun-shinee-kpop-crazy-guilty-pleasure-gif-15364593",
            "https://tenor.com/view/kim-jonghyun-jonghyun-view-lookup-gif-14221552",
            "https://tenor.com/view/kim-jonghyun-jonghyun-laugh-gif-14221544",
            "https://tenor.com/view/jonghyun-jonghyun-shinee-jonghyun-kpop-jonghyun-shinee-kpop-crazy-guilty-pleasure-gif-15364600",
            "https://tenor.com/view/shinee-jonghyun-smile-gif-7748521",
            "https://tenor.com/view/127baek-jonghyun-shinee-oprah-gif-19889869",
            "https://tenor.com/view/jonghyun-shinee-gif-7258930",
            "https://tenor.com/view/jonghyun-kpop-korean-hallyu-korean-music-gif-10935037",
            "https://tenor.com/view/jonghyun-kpop-korean-hallyu-korean-music-gif-10935037",
            "https://tenor.com/view/jong-hyun-shinee-k-pop-gif-11581439",
            "https://tenor.com/view/jonghyun-shinee-jonghyun-sexy-jonghyun-oppa-gif-11373129",
            "https://tenor.com/view/handsome-beautiful-jonghyun-shinee-jonghyun-kim-jonghyun-gif-14860254",
            "https://tenor.com/view/bleh-jonghyun-shinee-jonghyun-kim-jonghyun-gif-14860249",
            "https://tenor.com/view/jjong-jonghyun-shinee-shinee-jonghyun-kim-jonghyun-gif-19598522",
            "https://tenor.com/view/swag-jonghyun-shinee-jonghyun-kim-jonghyun-gif-14860248",
            "https://tenor.com/view/smile-jonghyun-shinee-jonghyun-kim-jonghyun-gif-14860247",
            "https://tenor.com/view/jonghyun-shinee-jonghyun-kim-jonghyun-smile-gif-14860252",
            "https://tenor.com/view/jonghyun-shinee-dance-pelvic-thrust-perform-gif-4964054",
            "https://tenor.com/view/kim-jonghyun-jonghyun-smile-gif-14221546",
            "https://tenor.com/view/onew-shinee-jonghyun-gif-10717312",
            "https://tenor.com/view/ripjonghyun-kpop-korean-gif-10547066",
            "https://tenor.com/view/jonghyun-dancing-127baek-shinee-jonghyun-jonghyun-gif-20032175",
            "https://tenor.com/view/shinee-excuse-me-miss-j-onghyun-taemin-dance-gif-17047724",
            "https://tenor.com/view/kpop-shinee-ot5-lee-taemin-choi-jongho-gif-17312262",
            "https://cdn.discordapp.com/attachments/813235619064971323/822445252668948530/Tumblr_l_239399224563101.gif",
            "https://cdn.discordapp.com/attachments/813235619064971323/822445253637570611/Tumblr_l_239397973464039.gif",
            "https://cdn.discordapp.com/attachments/813235619064971323/822445255206502467/Tumblr_l_239400507954663.gif",
            "https://cdn.discordapp.com/attachments/813235619064971323/822445255865532416/Tumblr_l_239394564087738.gif"]

        self.bot.shinee_key_gif = ["https://tenor.com/view/hi-key-shinee-gif-7394564",
            "https://tenor.com/view/shinee-key-kibum-wink-kpop-handsome-cute-gif-17047484",
            "https://tenor.com/view/shinee-kpop-key-kibum-cute-gif-11162138",
            "https://tenor.com/view/shinee-key-kibum-kpop-handsome-cute-gif-17047485",
            "https://tenor.com/view/key-onew-kibum-kfc-mcdonalds-gif-10144594",
            "https://tenor.com/view/shinee-key-kibum-laugh-kpop-gif-8836694",
            "https://tenor.com/view/key-shinee-kim-ki-bum-ki-bum-shawol-gif-19757690",
            "https://tenor.com/view/kibum-key-kim-kibum-hair-swipe-wink-gif-17083300",
            "https://cdn.discordapp.com/attachments/813235635456180264/818521865722658847/Tumblr_l_1093753469659430.gif",
            "https://cdn.discordapp.com/attachments/813235635456180264/818522020672831528/Tumblr_l_1093778223299733.gif",
            "https://cdn.discordapp.com/attachments/813235635456180264/818522140760211456/Tumblr_l_1093823891117320.gif",
            "https://cdn.discordapp.com/attachments/813235635456180264/818522501780865034/Tumblr_l_1093903089315154.gif",
            "https://cdn.discordapp.com/attachments/813235635456180264/818522502924861440/Tumblr_l_1093901825891926.gif",
            "https://cdn.discordapp.com/attachments/813235635456180264/818522504481472582/Tumblr_l_1093900612961405.gif",
            "https://cdn.discordapp.com/attachments/813235635456180264/818522505387048970/Tumblr_l_1093899873615051.gif",
            "https://cdn.discordapp.com/attachments/813235635456180264/818522613420261376/Tumblr_l_1093933063861653.gif",
            "https://cdn.discordapp.com/attachments/813235635456180264/818522614153871400/Tumblr_l_1093931151890560.gif",
            "https://cdn.discordapp.com/attachments/813235635456180264/818523085556285440/Tumblr_l_1094042337450362.gif",
            "https://cdn.discordapp.com/attachments/813235635456180264/818523086798061608/Tumblr_l_1094040747084373.gif",
            "https://cdn.discordapp.com/attachments/813235635456180264/818523147191451738/Tumblr_l_1094056187179054.gif",
            "https://cdn.discordapp.com/attachments/813235635456180264/818523311268692038/Tumblr_l_1094094368269613.gif",
            "https://cdn.discordapp.com/attachments/813235635456180264/818523311909634079/Tumblr_l_1094092720400394.gif",
            "https://cdn.discordapp.com/attachments/813235635456180264/818523313609113620/Tumblr_l_1094091764464978.gif"]

        #^ taemin is a soloist rn, under taemin_gif

        self.bot.shinee_onew_gif = ["https://tenor.com/view/onew-shinee-jonghyun-gif-10717312",
            "https://cdn.discordapp.com/attachments/813235506393251840/815306142754144317/Tumblr_l_692393651383630.gif",
            "https://cdn.discordapp.com/attachments/813235506393251840/815306143340822538/Tumblr_l_692392334254673.gif",
            "https://cdn.discordapp.com/attachments/813235506393251840/815306144050315285/Tumblr_l_692389950153528.gif",
            "https://cdn.discordapp.com/attachments/813235506393251840/815306145329053756/Tumblr_l_692388125691081.gif",
            "https://cdn.discordapp.com/attachments/813235506393251840/818522164767752233/Tumblr_l_1093819773775394.gif",
            "https://cdn.discordapp.com/attachments/813235506393251840/818522232736317490/Tumblr_l_1093817018279458.gif",
            "https://cdn.discordapp.com/attachments/813235506393251840/818522233567445012/Tumblr_l_1093815401908886.gif",
            "https://cdn.discordapp.com/attachments/813235506393251840/818522901275869214/Tumblr_l_1093978031450178.gif",
            "https://cdn.discordapp.com/attachments/813235506393251840/818523179449319464/Tumblr_l_1094062293494104.gif",
            "https://cdn.discordapp.com/attachments/813235506393251840/822445267944996925/Tumblr_l_239418077804396.gif",
            "https://cdn.discordapp.com/attachments/813235506393251840/822445268498120705/Tumblr_l_239416339838146.gif",
            "https://cdn.discordapp.com/attachments/813235506393251840/822445269018476584/Tumblr_l_239414946167522.gif",
            "https://cdn.discordapp.com/attachments/813235506393251840/822445269596504104/Tumblr_l_239414450535543.gif",
            "https://cdn.discordapp.com/attachments/813235506393251840/822445305169575976/Tumblr_l_239391294710708.gif",
            "https://cdn.discordapp.com/attachments/813235506393251840/822445305957449758/Tumblr_l_239389382270188.gif",
            "https://cdn.discordapp.com/attachments/813235506393251840/822445306539933726/Tumblr_l_239388140540188.gif",
            "https://cdn.discordapp.com/attachments/813235506393251840/822445307283243018/Tumblr_l_239387157872428.gif"]

        self.bot.shinee_minho_gif = ["https://tenor.com/view/shinee-minho-kpop-heart-gif-9591712",
            "https://tenor.com/view/minho-kiss-shinee-kissing-gif-10672502",
            "https://tenor.com/view/minho-choi-shinee-shineeworld-gif-13334159",
            "https://tenor.com/view/shinee-minho-cute-smile-pose-gif-12562760",
            "https://tenor.com/view/choi-minho-shinee-minho-performance-gif-14254206",
            "https://tenor.com/view/kpop-shinee-ot5-lee-taemin-choi-jongho-gif-17312262",
            "https://cdn.discordapp.com/attachments/813235536469688320/818522920153907200/Tumblr_l_1093983344508301.gif",
            "https://cdn.discordapp.com/attachments/813235536469688320/818523191777558528/Tumblr_l_1094059577962907.gif"]

        self.bot.shinee_group_gif = ["https://tenor.com/view/shinee-clap-dance-kpop-handsome-cute-gif-17047490",
            "https://tenor.com/view/shi-nee-kpop-korean-boy-group-korean-group-gif-10723465",
            "https://tenor.com/view/shinee-onew-jong-hyun-shinee-key-shinee-minho-gif-14108384",
            "https://tenor.com/view/shinee-sing-cute-kpop-boy-group-gif-17047772",
            "https://tenor.com/view/shinee-dxdxd-pose-kpop-cute-gif-17301140",
            "https://tenor.com/view/gaze-look-shinee-kpop-korean-gif-3519620",
            "https://tenor.com/view/shinee-onew-key-minho-taemin-gif-17506668",
            "https://tenor.com/view/jonghyun-shinee-shineeminho-taemin-onew-gif-14411220",
            "https://tenor.com/view/shinee-onew-jonghyun-taemin-shinee-key-gif-14131901",
            "https://tenor.com/view/shinee-onew-lee-jinki-key-kim-kibum-gif-17345444",
            "https://tenor.com/view/shinee-gif-18448144",
            "https://tenor.com/view/shinew-onew-jong-hyun-shinee-key-shinee-minho-gif-14108379",
            "https://tenor.com/view/kpop-korean-shinee-group-concert-gif-3521477",
            "https://tenor.com/view/shinee-laugh-kpop-group-pic-gif-12082547",
            "https://tenor.com/view/shinee-onew-lee-jinki-key-kim-kibum-gif-17083221",
            "https://cdn.discordapp.com/attachments/813287404311412786/817075275203477524/Tumblr_l_909494561560188.gif",
            "https://cdn.discordapp.com/attachments/813287404311412786/818522362231914506/Tumblr_l_1093874306738030.gif",
            "https://cdn.discordapp.com/attachments/813287404311412786/818522363137622026/Tumblr_l_1093873282275530.gif",
            "https://cdn.discordapp.com/attachments/813287404311412786/818522951942144042/Tumblr_l_1093987285390330.gif"]
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
            "https://tenor.com/view/vav-jacob-jang-peng-rapper-vocalist-gif-17750525",
            "https://cdn.discordapp.com/attachments/796980439843602472/818292834741649408/8e4c9975-c69c-46be-888c-7542d2f54edf.gif"]

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

    @commands.command()
    async def astro(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Astro {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "eunwoo":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Eunwoo :heart:')
            await ctx.send(random.choice(self.bot.astro_eunwoo_gif))
            await ctx.message.delete()
        elif arg == "mj":
            await ctx.send(f'<@!{ctx.author.id}> is talking about MJ :heart:')
            await ctx.send(random.choice(self.bot.astro_mj_gif))
            await ctx.message.delete()

    @commands.command()
    async def cravity(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Cravity {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "serim":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Serim :heart:')
            await ctx.send(random.choice(self.bot.cravity_serim_gif))
            await ctx.message.delete()
        elif arg == "allen":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Allen :heart:')
            await ctx.send(random.choice(self.bot.cravity_allen_gif))
            await ctx.message.delete()
        elif arg == "jungmo":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jungmo :heart:')
            await ctx.send(random.choice(self.bot.cravity_jungmo_gif))
            await ctx.message.delete()
        elif arg == "woobin":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Woobin :heart:')
            await ctx.send(random.choice(self.bot.cravity_woobin_gif))
            await ctx.message.delete()
        elif arg == "wonjin":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Wonjin :heart:')
            await ctx.send(random.choice(self.bot.cravity_wonjin_gif))
            await ctx.message.delete()
        elif arg == "minhee":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Minhee :heart:')
            await ctx.send(random.choice(self.bot.cravity_minhee_gif))
            await ctx.message.delete()
        elif arg == "hyeongjun":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Hyeongjun :heart:')
            await ctx.send(random.choice(self.bot.cravity_hyeongjun_gif))
            await ctx.message.delete()
        elif arg == "taeyoung":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Taeyoung :heart:')
            await ctx.send(random.choice(self.bot.cravity_taeyoung_gif))
            await ctx.message.delete()
        elif arg == "seongmin":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Seongmin :heart:')
            await ctx.send(random.choice(self.bot.cravity_seongmin_gif))
            await ctx.message.delete()

    @commands.command()
    async def exo(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [EXO {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "kai":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Kai :heart:')
            await ctx.send(random.choice(self.bot.exo_kai_gif))
            await ctx.message.delete()
        elif arg == "do" or arg == "d.o.":
            await ctx.send(f'<@!{ctx.author.id}> is talking about D.O. :heart:')
            await ctx.send(random.choice(self.bot.exo_do_gif))
            await ctx.message.delete()
        elif arg == "baekhyun":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Baekhyun :heart:')
            await ctx.send(random.choice(self.bot.exo_baekhyun_gif))
            await ctx.message.delete()
        elif arg == "chanyeol":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Chanyeol :heart:')
            await ctx.send(random.choice(self.bot.exo_chaenyeol_gif))
            await ctx.message.delete()
        elif arg == "sehun":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Sehun :heart:')
            await ctx.send(random.choice(self.bot.exo_sehun_gif))
            await ctx.message.delete()
        elif arg == "chen":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Chen :heart:')
            await ctx.send(random.choice(self.bot.exo_chen_gif))
            await ctx.message.delete()
        elif arg == "suho":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Suho :heart:')
            await ctx.send(random.choice(self.bot.exo_suho_gif))
            await ctx.message.delete()
        elif arg == "lay":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Lay :heart:')
            await ctx.send(random.choice(self.bot.exo_lay_gif))
            await ctx.message.delete()
        elif arg == "xiumin":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Xiumin :heart:')
            await ctx.send(random.choice(self.bot.exo_xiumin_gif))
            await ctx.message.delete()

    @commands.command()
    async def golden(self, ctx, child, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Golden Child {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
            await ctx.message.delete()
        else:
            if child == "child":
                if arg == "bomin":
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Bomin :heart:')
                    await ctx.send(random.choice(self.bot.golcha_bomin_gif))
                    await ctx.message.delete()
                elif arg == "daeyeol":
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Daeyeol :heart:')
                    await ctx.send(random.choice(self.bot.golcha_daeyeol_gif))
                    await ctx.message.delete()
                elif arg == "donghyun":
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Donghyun :heart:')
                    await ctx.send(random.choice(self.bot.golcha_donghyun_gif))
                    await ctx.message.delete()
                elif arg == "jaehyun":
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Jaehyun :heart:')
                    await ctx.send(random.choice(self.bot.golcha_jaehyun_gif))
                    await ctx.message.delete()
                elif arg == "jangjun":
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Jangjun :heart:')
                    await ctx.send(random.choice(self.bot.golcha_jangjun_gif))
                    await ctx.message.delete()
                elif arg == "jibeom":
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Jibeom :heart:')
                    await ctx.send(random.choice(self.bot.golcha_jibeom_gif))
                    await ctx.message.delete()
                elif arg == "joochan":
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Joochan :heart:')
                    await ctx.send(random.choice(self.bot.golcha_joochan_gif))
                    await ctx.message.delete()
                elif arg == "seungmin":
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Seungmin :heart:')
                    await ctx.send(random.choice(self.bot.golcha_seungmin_gif))
                    await ctx.message.delete()
                elif arg == "tag":
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Tag :heart:')
                    await ctx.send(random.choice(self.bot.golcha_tag_gif))
                    await ctx.message.delete()
                elif arg == "y":
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Y :heart:')
                    await ctx.send(random.choice(self.bot.golcha_y_gif))
                    await ctx.message.delete()

    @commands.command()
    async def the(self, ctx, boyz="boyz", *, arg = "group"):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [The Boyz {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
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
        elif arg == "group":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about The Boyz :heart:')
                await ctx.send(random.choice(self.bot.theboyz_group_gif))
                await ctx.message.delete()
    
    @commands.command(aliases = ['p1h'])
    async def p1harmony(self, ctx, arg = "group"):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [P1Harmony {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
            await ctx.message.delete()
        else:
            if arg == "intak":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Intak :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_intak_gif))
                await ctx.message.delete()
            elif arg == "jiung":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jiung :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_jiung_gif))
                await ctx.message.delete()
            elif arg == "jongseob":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jongseob :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_jongseob_gif))
                await ctx.message.delete()
            elif arg == "keeho":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Keeho :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_keeho_gif))
                await ctx.message.delete()
            elif arg == "soul":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Soul :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_soul_gif))
                await ctx.message.delete()
            elif arg == "theo":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Theo :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_theo_gif))
                await ctx.message.delete()
            elif arg == "group":
                await ctx.send(f'<@!{ctx.author.id}> is talking about P1Harmony :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_group_gif))
                await ctx.message.delete()
    
    @commands.command(aliases = ['svt'])
    async def seventeen(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Seventeen {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
            await ctx.message.delete()
        else:
            if arg == "scoups" or arg == "s.coups":
                await ctx.send(f'<@!{ctx.author.id}> is talking about S.coups :gem:')
                await ctx.send(random.choice(self.bot.seventeen_scoups_gif))
                await ctx.message.delete()
            elif arg == "wonwoo":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Wonwoo :gem:')
                await ctx.send(random.choice(self.bot.seventeen_wonwoo_gif))
                await ctx.message.delete()
            elif arg == "mingyu":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Mingyu :gem:')
                await ctx.send(random.choice(self.bot.seventeen_mingyu_gif))
                await ctx.message.delete()
            elif arg == "vernon":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Vernon :gem:')
                await ctx.send(random.choice(self.bot.seventeen_vernon_gif))
                await ctx.message.delete()
            elif arg == "woozi":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Woozi :gem:')
                await ctx.send(random.choice(self.bot.seventeen_woozi_gif))
                await ctx.message.delete()
            elif arg == "jeonghan":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jeonghan :gem:')
                await ctx.send(random.choice(self.bot.seventeen_jeonghan_gif))
                await ctx.message.delete()
            elif arg == "joshua":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Joshua :gem:')
                await ctx.send(random.choice(self.bot.seventeen_joshua_gif))
                await ctx.message.delete()
            elif arg == "dk":
                await ctx.send(f'<@!{ctx.author.id}> is talking about DK :gem:')
                await ctx.send(random.choice(self.bot.seventeen_dk_gif))
                await ctx.message.delete()
            elif arg == "seungkwan":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Seungkwan :gem:')
                await ctx.send(random.choice(self.bot.seventeen_seungkwan_gif))
                await ctx.message.delete()
            elif arg == "hoshi":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Hoshi :gem:')
                await ctx.send(random.choice(self.bot.seventeen_hoshi_gif))
                await ctx.message.delete()
            elif arg == "jun":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jun :gem:')
                await ctx.send(random.choice(self.bot.seventeen_jun_gif))
                await ctx.message.delete()
            elif arg == "the8":
                await ctx.send(f'<@!{ctx.author.id}> is talking about The8 :gem:')
                await ctx.send(random.choice(self.bot.seventeen_the8_gif))
                await ctx.message.delete()
            elif arg == "dino":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Dino :gem:')
                await ctx.send(random.choice(self.bot.seventeen_dino_gif))
                await ctx.message.delete()

    @commands.command()
    async def shinee(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Shinee {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
            await ctx.message.delete()
        else:
            if arg == "jonghyun":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jonghyun :heart::angel:')
                await ctx.send(random.choice(self.bot.shinee_jonghyun_gif))
                await ctx.message.delete()
            elif arg == "key":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Key :heart:')
                await ctx.send(random.choice(self.bot.shinee_key_gif))
                await ctx.message.delete()
            elif arg == "taemin":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Taemin :heart:')
                await ctx.send(random.choice(self.bot.taemin_gif))
                await ctx.message.delete()
            elif arg == "onew":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Onew :heart:')
                await ctx.send(random.choice(self.bot.shinee_onew_gif))
                await ctx.message.delete()
            elif arg == "minho":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Minho :heart:')
                await ctx.send(random.choice(self.bot.shinee_minho_gif))
                await ctx.message.delete()
            elif arg == "group":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Shinee :heart:')
                await ctx.send(random.choice(self.bot.shinee_group_gif))
                await ctx.message.delete()

    @commands.command()
    async def sf9(self, ctx, *, arg = "ot9"):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [SF9 {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
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
        elif arg == "ot9":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about SF9 :heart:')
                await ctx.send(random.choice(self.bot.sf9_ot9_gif))
                await ctx.message.delete()

    @commands.command()
    async def vav(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [VAV {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
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

    # @bot.command()
    # async def sendGif(self, ctx, idol:str, gifSet:List[str], emoji:str):
    #     if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
    #         await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
    #         await ctx.message.delete()
    #     else:
    #         await ctx.send(f'<@!{ctx.author.id}> is talking about {idol} :{emoji}:')
    #         await ctx.send(random.choice(gifSet))
    #         await ctx.message.delete()
    


def setup(client):
    client.add_cog(BGS(client))