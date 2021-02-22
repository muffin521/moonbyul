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
            "https://cdn.discordapp.com/attachments/804188554896867410/812085871381184572/7d9b9479-9a87-4ba9-aec2-9e4ea8ae2d39.gif"]

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
            "https://cdn.discordapp.com/attachments/804188814989197322/812869058780332052/Tumblr_l_381405579296690.gif"]

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
            "https://cdn.discordapp.com/attachments/804188853916270622/812081129141829702/00d9b76d-9ad2-4a2a-bb20-ee693e8e4705.gif"]

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
            "https://cdn.discordapp.com/attachments/804188917775466496/812446209120665600/Tumblr_l_315559925054569.gif"]

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
            "https://cdn.discordapp.com/attachments/804188518985367563/812085369780174868/6dfde2d6-94a0-468b-b0b5-0bb24cd6a0df.gif"]

        self.bot.exo_chen_gif = ["https://cdn.discordapp.com/attachments/804189007500148786/812081819025408000/0d88a762-e789-4083-9a9f-20c43cdd8528.gif",
            "https://cdn.discordapp.com/attachments/804189007500148786/812083862334603285/4a377461-050f-434b-8ac1-74d54831c901.gif",
            "https://cdn.discordapp.com/attachments/804189007500148786/812084080011247616/4c74f854-ef83-400f-91d6-e79a907b6062.gif",
            "https://cdn.discordapp.com/attachments/804189007500148786/812084128128303114/4cc8a7af-9d10-48ab-9963-90eb9aba8803.gif",
            "https://cdn.discordapp.com/attachments/804189007500148786/812085027797860362/5e08f246-c680-4dd0-8c87-22e6a6b3263a.gif",
            "https://cdn.discordapp.com/attachments/804189007500148786/812085839550349402/7d0c865b-ce9e-4012-ab66-4a026f76290e.gif",
            "https://cdn.discordapp.com/attachments/804189007500148786/812086020333764618/7f391d0b-da8d-4390-9471-ca13b4fca84e.gif",
            "https://cdn.discordapp.com/attachments/804189007500148786/812086115871490078/08e23a25-f1f1-4d4d-9dc3-c2c0a496260e.gif"]

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
            "https://cdn.discordapp.com/attachments/804188541231431700/812086246754615316/8d00f64a-f1c0-4ced-bd94-527284c8c450.gif"]

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
            "https://giphy.com/gifs/judge-lay-zhang-CSzDNTS1XUpgsy4teD"]

        self.bot.exo_xiumin = ["https://cdn.discordapp.com/attachments/804189116748398633/812081403722334248/0b0f7062-b94d-4009-b283-eb7a4e472034.gif",
            "https://cdn.discordapp.com/attachments/804189116748398633/812082498845540372/1c522771-cba9-478f-a442-5d1099cb8037.gif",
            "https://cdn.discordapp.com/attachments/804189116748398633/812083239401160714/3a1b9a55-686b-4b6a-8309-19ff8f5f95c6.gif",
            "https://cdn.discordapp.com/attachments/804189116748398633/812084475474870272/05eb5300-1b2b-4266-84e6-3e5b7522a1b7.gif",
            "https://cdn.discordapp.com/attachments/804189116748398633/812084698272235530/5c756d00-df9f-47a3-a9af-ecc563bd8453.gif",
            "https://cdn.discordapp.com/attachments/804189116748398633/812085055698239488/5ed9f39f-1b24-48b6-9aa2-e953a47134f2.gif",
            "https://cdn.discordapp.com/attachments/804189116748398633/812085576814821396/6fa39c57-a469-4552-b15e-3394d05ca193.gif"]
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