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
jon = 109914198544240640

class RedVelvetPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.irene_gif = ["https://tenor.com/view/irene-irene-bae-bae-joohyun-%ec%95%84%ec%9d%b4%eb%a6%b0-red-velvet-gif-14130526",
            "https://tenor.com/view/irene-pretty-rv-red-velvet-annoyed-gif-14019706",
            "https://tenor.com/view/irene-dance-red-velvet-kpop-irene-red-velvet-gif-13290460",
            "https://tenor.com/view/red-velvet-irene-smile-gif-11069117",
            "https://tenor.com/view/irene-bae-juhyun-irene-bae-%EC%95%84%EC%9D%B4%EB%A6%B0-red-velvet-gif-14480962",
            "https://tenor.com/view/%c4%b1rene-gif-18020419",
            "https://tenor.com/view/irene-red-velvet-ew-eww-scared-gif-12882453",
            "https://tenor.com/view/irene-peace-two-cute-gif-7841178",
            "https://tenor.com/view/irene-gif-14829402",
            "https://i.pinimg.com/originals/a9/b6/dd/a9b6dd7a16af12151c9716b5fb16e015.gif",
            "https://i.pinimg.com/originals/84/39/03/84390331c3efab7da0346eb3cf1a787f.gif",
            "https://data.whicdn.com/images/323301155/original.gif",
            "https://pa1.narvii.com/6676/0249f4be84945c6186df3f5af7dfa86e5aa44a39_hq.gif",
            "http://pa1.narvii.com/6806/495bdfb556909b92603b2f75a1a85e7bb4d70643_00.gif",
            "https://i.pinimg.com/originals/ae/11/85/ae11856b8b002f6017547ceec1b312da.gif",
            "https://data.whicdn.com/images/328703247/original.gif",
            "https://data.whicdn.com/images/325057302/original.gif",
            "http://images6.fanpop.com/image/photos/41700000/-Red-Velvet-Really-Bad-Boy-MV-red-velvet-41709843-540-226.gif",
            "https://i.pinimg.com/originals/73/1a/54/731a5448c70b6c9f79058886706bed75.gif",
            "https://pa1.narvii.com/6727/bb73c30ac45dd744883fbb76b0419424141cb731_hq.gif",
            "http://cdn.lowgif.com/full/ed9eb6576b4733c9-.gif",
            "https://66.media.tumblr.com/43eaa5f23c63c7c968057424616f8f35/tumblr_p3svh4SuUn1tiq650o1_400.gif",
            "https://66.media.tumblr.com/79fe8fa91656bde27ac381d39b8f3c3a/tumblr_pkieyp5FME1x1uv52o4_r2_250.gif",
            "https://thumbs.gfycat.com/WelldocumentedUnimportantBeetle-max-1mb.gif",
            "https://thumbs.gfycat.com/BestSinfulKilldeer-small.gif",
            "https://pa1.narvii.com/7074/ad0e5dd6f1c61b028eaa394d0a29c4c8d653f649r1-720-537_hq.gif",
            "https://i.pinimg.com/originals/8f/ee/1a/8fee1ab7ae34673d4bd5b94495fc3af1.gif",
            "https://pa1.narvii.com/7274/2fbd3985915fd64786b5ecd00494c070bb5dfffar1-250-374_00.gif",
            "https://i.pinimg.com/originals/6a/91/61/6a9161ec3e34b6503bb74ebf86fa5918.gif",
            "https://data.whicdn.com/images/309612308/original.gif",
            "https://i.pinimg.com/originals/e5/22/d9/e522d9d93b71d320b652383614f9e12b.gif",
            "https://64.media.tumblr.com/0ba95968349cc7bfe57e94ee8e893cfa/29fe0a561958fc89-87/s400x600/8267fe6f16738e9ab8044d84a517b59345768dca.gif",
            "https://data.whicdn.com/images/325057357/original.gif",
            "https://media1.tenor.com/images/72e80a57847cc3e536645cbd391f8682/tenor.gif?itemid=12505529",
            "https://p.favim.com/orig/2018/08/17/gif-bae-joohyun-red-velvet-Favim.com-6175630.gif",
            "https://i.pinimg.com/originals/30/2b/ad/302bad3abcf4106ed8431777c46a36e0.gif",
            "https://i.pinimg.com/originals/5a/82/2c/5a822c18888278daac347a416f561e77.gif",
            "https://data.whicdn.com/images/338662359/original.gif",
            "https://i.pinimg.com/originals/c0/a1/83/c0a18397f73752020d39809dcae75297.gif",
            "https://i.pinimg.com/originals/68/9e/04/689e04e26f4aac9eb55a4edbf627ad1d.gif",
            "https://data.whicdn.com/images/334296316/original.gif",
            "https://i.pinimg.com/originals/21/a8/9f/21a89f8dbe0fbccbb91726b0fe534978.gif",
            "http://file3.instiz.net/data/file3/2019/08/26/6/8/1/68165b1cfdca7918e59728a2ec96dce3.gif",
            "https://i.pinimg.com/originals/d6/b8/b2/d6b8b27e2d40f7352163bb99cc7ee7c8.gif",
            "https://p.favim.com/orig/2018/12/27/joy-fashion-seulgi-Favim.com-6707064.gif",
            "http://images6.fanpop.com/image/photos/42700000/Irene-red-velvet-42729049-559-525.gif",
            "https://data.whicdn.com/images/302693362/original.gif",
            "https://i.pinimg.com/originals/d8/6e/9b/d86e9b28de06998df3b77cdda8c9f168.gif",
            "https://i.pinimg.com/originals/95/1c/ae/951cae75b19e8c91616cfc990042340b.gif",
            "https://i.pinimg.com/originals/bf/28/32/bf2832e56a136d4ed3cbdf65ca67dc9e.gif",
            "https://data.whicdn.com/images/323427955/original.gif",
            "https://i.gifer.com/MNd0.gif",
            "https://64.media.tumblr.com/07d820072fe2b05f9476158409b5e333/cc0e8c05fbc18dc2-5a/s1280x1920/5a9c12286695c767dc40a30ae5e0386c474a9247.gif",
            "https://data.whicdn.com/images/302453974/original.gif",
            "https://p.favim.com/orig/2018/11/24/bae-joohyun-irene-red-velvet-Favim.com-6621517.gif",
            "https://i.pinimg.com/originals/1e/e5/15/1ee515f6a0bc882c2c6863d6a6640aff.gif",
            "https://data.whicdn.com/images/266413336/original.gif"]

        self.bot.seulgi_gif = ["https://tenor.com/view/red-velvet-%eb%a0%88%eb%93%9c%eb%b2%a8%eb%b2%b3-kpop-seulgi-kang-seulgi-gif-17827226",
            "https://tenor.com/view/seulgi-kang-seulgi-%ec%8a%ac%ea%b8%b0-red-velvet-%eb%a0%88%eb%93%9c%eb%b2%a8%eb%b2%b3-gif-14354377",
            "https://tenor.com/view/seulgi-red-velvet-%ec%8a%ac%ea%b8%b0-%eb%a0%88%eb%93%9c%eb%b2%a8%eb%b2%b3-kpop-gif-16068955",
            "https://tenor.com/view/dancing-twice-red-velvet-kpop-badboy-gif-11824341",
            "https://tenor.com/view/seulgi-gif-18548350",
            "https://tenor.com/view/red-velvet-kpop-seulgi-bored-gif-14040756",
            "https://tenor.com/view/seulgi-ears-flapping-pikachu-hat-red-velvet-gif-12865105",
            "https://tenor.com/view/red-velvet-seulgi-kang-seulgi-smile-kpop-gif-17202871",
            "https://tenor.com/view/seulgi-money-gun-seulgimoneygun-gif-19038811"]

        self.bot.wendy_gif = ["https://tenor.com/view/ryoo-seungwan-wendy-red-velvet-kpop-redhair-gif-5230074",
            "https://tenor.com/view/red-velvet-dance-dumb-dumb-joy-irene-gif-14365084",
            "https://tenor.com/view/wendy-red-velvet-psycho-gif-15872100",
            "https://tenor.com/view/wendy-seungwan-redvelvet-rv-smtown-gif-5110994",
            "https://tenor.com/view/yuuuko-gif-11448258",
            "https://tenor.com/view/red-velvet-wendy-cute-kpop-gif-15124930",
            "https://tenor.com/view/ryoo-seungwan-wendy-red-velvet-kpop-redhair-gif-5229992",
            "https://tenor.com/view/redvelvet-wendy-gif-13398469",
            "https://tenor.com/view/wendy-red-velvet-wendy-wendy-shon-son-seungwan-%EC%9B%AC%EB%94%94-gif-13910394"]

        self.bot.yeri_gif = ["https://tenor.com/view/kim-yerim-yeri-pointing-lipstick-on-gif-12579366",
            "https://tenor.com/view/yeri-dance-cute-gif-13149660",
            "https://tenor.com/view/yeri-kim-yerim-red-velvet-%EB%A0%88%EB%93%9C%EB%B2%A8%EB%B2%B3-%EC%98%88%EB%A6%AC-gif-14233858",
            "https://tenor.com/view/umpahumpah-kimyeri-yerim-yeri-redvelvet-gif-14820164",
            "https://tenor.com/view/kimyerim-yeri-dance-gif-12536748",
            "https://tenor.com/view/yeri-gif-18540987",
            "https://tenor.com/view/red-velvet-yeri-sm-entertainment-kpop-beautiful-gif-17036585",
            "https://tenor.com/view/yeri-redvelvet-gif-18663409",
            "https://tenor.com/view/yeri-kim-yerim-%EC%98%88%EB%A6%AC-red-velvet-%EB%A0%88%EB%93%9C%EB%B2%A8%EB%B2%B3-gif-15501276",
            "https://tenor.com/view/kim-yerim-yeri-sad-gif-12536905",
            "https://tenor.com/view/kim-yerim-yeri-mua-kisses-gif-12579362",
            "https://tenor.com/view/yeri-wink-cute-gif-13149664",
            "https://tenor.com/view/yeri-kim-yerim-i-dont-care-red-velvet-%EC%98%88%EB%A6%AC-gif-13639966",
            "https://gfycat.com/briskpessimisticanhinga-umpah-umpah-girl-group-music-bank",
            "https://gfycat.com/unfitpleasedcoyote-umpah-umpah-girl-group-music-core",
            "https://gfycat.com/ablesimpleafricanaugurbuzzard-red-velvet-yeri",
            "https://gfycat.com/acrobaticoffbeatjerboa-red-velvet-laughing-kpop-yeri",
            "https://gfycat.com/agitatedunluckyleafbird-beauty",
            "https://gfycat.com/alarmedunconsciousdanishswedishfarmdog-red-velvet",
            "https://gfycat.com/ashamedsamegoldfish",
            "https://gfycat.com/absolutedeliriouslcont-red-velvet-yeri",
            "https://gfycat.com/alllimitedcaimanlizard",
            "https://gfycat.com/allwarmheartedbluewhale-umpah-umpah-red-velvet-kim-yerim-comeback",
            "https://gfycat.com/ajaremptydragon-red-velvet-zimzalabim-kim-yerim-beauty",
            "https://gfycat.com/plainexaltedelephant-2nd-concert-red-velvet-kim-yerim-bluray",
            "https://gfycat.com/wanreflectinggeese-red-velvet",
            "https://gfycat.com/arcticgroundedbrant-red-velvet-dumb-dumb-kpopfap-panites",
            "https://gfycat.com/baggyminiaturecusimanse-red-velvet",
            "https://gfycat.com/ablekeyhuemul-umpah-umpah-red-velvet-kim-yerim-comeback",
            "https://gfycat.com/admirableembarrassediberianbarbel-red-velvet-yeri",
            "https://gfycat.com/aptimperturbablehellbender",
            "https://gfycat.com/angrywickedazurevase",
            "https://gfycat.com/aggressivemeatygerenuk",
            "https://gfycat.com/bigheartedspiffybunny-girl-group-red-velvet-yerimiese-200302",
            "https://gfycat.com/flatspottedlice",
            "https://gfycat.com/briskdefinitivecrocodile-red-velvet-yeri",
            "https://gfycat.com/bossyrepulsiveguillemot",
            "https://gfycat.com/focusedbadarabianoryx-beauty",
            "https://gfycat.com/animatedkeygosling",
            "https://gfycat.com/athleticoffensivegopher",
            "https://gfycat.com/adolescentdefiniteibadanmalimbe-beauty",
            "https://gfycat.com/embellishedillalpineroadguidetigerbeetle",
            "https://gfycat.com/bonythesejackal-minitmute-official-red-velvet-yeri",
            "https://gfycat.com/calmsilverdodobird",
            "https://gfycat.com/breakablecavernousjoey",
            "https://gfycat.com/cautiousillfatedcoqui",
            "https://gfycat.com/candidcraftygermanspaniel",
            "https://gfycat.com/colorlesselasticflyingfish-icn-airport-girl-group-red-velvet",
            "https://gfycat.com/commonvictoriousaffenpinscher",
            "https://gfycat.com/cleverfavoritecrustacean",
            "https://gfycat.com/fakeidlegartersnake",
            "https://gfycat.com/flimsyflusteredalpinegoat",
            "https://i.pinimg.com/originals/85/1e/02/851e02616f72a2a148e1ebc307ade2c2.gif",
            "https://i.pinimg.com/originals/2f/2f/e5/2f2fe585a0255e68bc58a2fb6ee6f20c.gif",
            "https://pa1.narvii.com/6912/aec98160c588ddf9c326a7e5b023e03d0a37f0d1r1-540-230_hq.gif",
            "https://64.media.tumblr.com/037158d4d333be0d8deb2553e0ad4d6c/94ad1cdf9635cd11-56/s540x810/1e81a8e6a1d4beb15b2c39426c79d6402e7d72ff.gif",
            "https://64.media.tumblr.com/df0af9f15fc9991b9848f900e417cadc/94ad1cdf9635cd11-dd/s540x810/f368cee966244e82c0aa6dcc58e602c769b2309a.gif",
            "https://64.media.tumblr.com/3accc85e9568ea1d0b9c621eb1c2201f/b5ba9e1eac8f4a93-5a/s400x600/76dcabb4410ee546c303f948c88f7884cb9a1c78.gif",
            "https://i.pinimg.com/originals/f0/3c/32/f03c324809177d611513ccd531f4666b.gif",
            "https://i.pinimg.com/originals/94/45/5c/94455c4c162c5e4701a1689c09184209.gif",
            "https://i.pinimg.com/originals/d5/14/78/d51478194d75c110ec032778bdcc18a0.gif",
            "https://64.media.tumblr.com/062c0f8b3f800a89c3ddd086b4386096/d9b3053be317c95e-b0/s400x600/8b4156a7efcc91cfb041357c31727cf24ae6ba12.gif",
            "https://cdn130.picsart.com/320204154255201.gif",
            "https://64.media.tumblr.com/c372fe7949325bd20942d2fc892dc829/94ad1cdf9635cd11-e3/s540x810/8de264203bad198951ba83b143824b5549783518.gif",
            "https://data.whicdn.com/images/338659516/original.gif",
            "https://64.media.tumblr.com/18e331cf5aaa07f5f4d3fc2043c76c9f/tumblr_pwhu29ypir1wmumuzo2_540.gif",
            "https://data.whicdn.com/images/334270992/original.gif",
            "https://64.media.tumblr.com/df2d48454df0e59ec760e1920e76857e/tumblr_pwhu29ypir1wmumuzo4_540.gif",
            "https://i.pinimg.com/originals/81/60/c5/8160c53fe7df52a029432fbd1ea99edd.gif",
            "https://64.media.tumblr.com/9af557a512ebc866fea8e56b6a5b1dc9/tumblr_pxw56owkVF1r3hdhfo2_400.gif",
            "https://64.media.tumblr.com/0326e874c987eb6db8d787e2027f2d8e/tumblr_pxtkrrnL3Y1x1uv52o1_400.gif",
            "https://thumbs.gfycat.com/MintyBelovedAmericanshorthair-size_restricted.gif",
            "https://66.media.tumblr.com/8d8af41b9dd757e407cb7035d9402fd9/tumblr_pwssq6ROjl1wn53pgo2_400.gif",
            "https://thumbs.gfycat.com/AngelicUnitedGourami-size_restricted.gif",
            "https://i.pinimg.com/originals/ff/51/dd/ff51dd70e3e23439c95513cc0608d273.gif",
            "https://i.pinimg.com/originals/36/fc/63/36fc63551f2709641e05eca14ec1e22b.gif",
            "https://64.media.tumblr.com/e69c3ee48b4e8c8e385b8fa7ec74d0c5/tumblr_pwlu2mselp1y5g35io5_400.gif",
            "https://thumbs.gfycat.com/AntiqueClearcutAlbertosaurus-size_restricted.gif",
            "https://thumbs.gfycat.com/AbleKeyHuemul-size_restricted.gif",
            "https://thumbs.gfycat.com/AllWarmheartedBluewhale-size_restricted.gif",
            "https://thumbs.gfycat.com/WiltedCommonFlicker-size_restricted.gif",
            "https://thumbs.gfycat.com/ActualDeliriousIberiannase-size_restricted.gif",
            "https://thumbs.gfycat.com/LeadingVeneratedIggypops-size_restricted.gif",
            "https://thumbs.gfycat.com/HugeHalfHarrierhawk-size_restricted.gif",
            "https://thumbs.gfycat.com/EarnestUnnaturalBedlingtonterrier-size_restricted.gif",
            "https://thumbs.gfycat.com/AdolescentDefiniteIbadanmalimbe-max-1mb.gif",
            "https://thumbs.gfycat.com/AppropriateNaughtyAcornweevil-size_restricted.gif",
            "https://thumbs.gfycat.com/ImportantImpeccableKestrel-size_restricted.gif",
            "https://64.media.tumblr.com/1e0cfa54fda69d76b9a7e34a788f0329/tumblr_pwslnfmqRr1x1uv52o1_250.gif",
            "https://i.pinimg.com/originals/97/73/ba/9773baeedbc5f1e9f0d88c4e06e6c918.gif",
            "https://i.pinimg.com/originals/c7/7b/c9/c77bc98d25820969d0a9ebe4733e09b5.gif",
            "http://68.media.tumblr.com/9a12625e39b4350a37f6368332e26b86/tumblr_ot1ncrAxDt1ti7fhko2_400.gif",
            "https://thumbs.gfycat.com/LastForthrightBooby-size_restricted.gif",
            "https://thumbs.gfycat.com/InbornMeagerDuiker-size_restricted.gif",
            "https://i.pinimg.com/originals/3a/45/68/3a45688fcafecb4f7bdd482a2a45368c.gif",
            "https://64.media.tumblr.com/4843750ea3690e579e514c46350a3f9c/tumblr_ptg5u3dk3g1whmsz5o3_250.gif",
            "https://66.media.tumblr.com/fdee8ad7302ac4a8fff268219732c08c/tumblr_plpo4pZMIs1tizu4so2_400.gif",
            "https://data.whicdn.com/images/349999061/original.gif",
            "https://i.pinimg.com/originals/5d/cb/45/5dcb45360dbdf43c7285637e4427e3fc.gif",
            "https://pa1.narvii.com/6220/c1d53b1ad8ff3d497247298583873b596f08cde1_hq.gif",
            "https://i.pinimg.com/originals/3d/5d/1a/3d5d1a207b1d2751079b46299a70cdb0.gif",
            "https://i.pinimg.com/originals/33/2f/d1/332fd10111b0ed8afded398ebd70c4b1.gif",
            "https://media1.tenor.com/images/fccce4bbd53a6286abf95c11232bbc92/tenor.gif?itemid=15855601",
            "https://i.pinimg.com/originals/33/12/0b/33120bf555dd7f74030c4c0a847937fb.gif",
            "https://2.bp.blogspot.com/-Fp2KYxG4jXc/XHaVb62wcaI/AAAAAAAAPd4/59xGTmtlqywKfxiZmjpVjnRhIl2jhKGaACLcBGAs/s1600/20671027b60626e6896e946d4c39e44d.gif",
            "https://data.whicdn.com/images/291710638/original.gif",
            "https://64.media.tumblr.com/c29392c27d2c9ec3c279dcb2aefaf516/tumblr_o7a9nkO1yE1v0e4aao1_400.gif",
            "https://data.whicdn.com/images/250632443/original.gif",
            "https://i.pinimg.com/originals/af/86/16/af8616d14ade0b9284655d5bb5ffc162.gif",
            "https://78.media.tumblr.com/f57e491705b65c0c70b78bfa5755b33e/tumblr_ptiduexnaf1wmumuzo1_400.gif",
            "https://data.whicdn.com/images/335962312/original.gif",
            "https://data.whicdn.com/images/335962283/original.gif",
            "https://data.whicdn.com/images/306650477/original.gif",
            "https://data.whicdn.com/images/306601116/original.gif",
            "http://images6.fanpop.com/image/photos/41100000/Yeri-red-velvet-41157594-268-370.gif",
            "https://i.pinimg.com/originals/a4/47/a3/a447a3362762b0431bf31fe95736ed35.gif",
            "https://i.pinimg.com/originals/01/6d/76/016d76c83090b7730f25bfbecca361c4.gif",
            "https://78.media.tumblr.com/e81cae37212d2f007deedec1412065ca/tumblr_oznp64trvh1wza31uo1_400.gif",
            "https://data.whicdn.com/images/301700072/original.gif",
            "https://media.tenor.com/images/c73774836b33ab29eec56c5673d0e52c/tenor.gif",
            "https://thumbs.gfycat.com/MealyPlasticGreendarnerdragonfly-size_restricted.gif",
            "https://thumbs.gfycat.com/CourteousTastyChimneyswift-size_restricted.gif",
            "https://thumbs.gfycat.com/WindingReadyJavalina-size_restricted.gif",
            "https://thumbs.gfycat.com/IllfatedEnviousDartfrog-size_restricted.gif",
            "https://i.pinimg.com/originals/40/0d/65/400d6563fa67bbf6a1e8267fc843aa95.gif",
            "https://64.media.tumblr.com/b86c8f238b7e6e5dd76cd9d6090c86a5/2a71e2850baee111-0a/s640x960/34626579c6bada6fe265900fcdb4c6c7d476719b.gif",
            "https://data.whicdn.com/images/302239646/original.gif",
            "https://data.whicdn.com/images/323252230/original.gif",
            "https://data.whicdn.com/images/334980038/original.gif",
            "https://data.whicdn.com/images/306777830/original.gif",
            "https://64.media.tumblr.com/cba14a0a6b769cba82cef4e349f3ca5a/tumblr_ptcctbjKOc1wmumuzo4_250.gif",
            "https://64.media.tumblr.com/78e48e08a3f83884ffe221f43f36d732/1b55f3f19149f9a6-cb/s400x600/2738a3fe44f0c51b35e021d8b92e4f3fc7877cab.gif",
            "https://imgur.com/N59ZW6U",
            "https://i.pinimg.com/originals/d6/dd/31/d6dd31ed3b13d2fdd0f5dc4b09f81bd6.gif",
            "https://i.pinimg.com/originals/81/7c/16/817c16c34abe4bb8a06a16ef28a339a8.gif",
            "https://data.whicdn.com/images/194389941/original.gif",
            "https://data.whicdn.com/images/323124560/original.gif",
            "https://media1.tenor.com/images/da9996829be28d26e4948d1454002fc2/tenor.gif?itemid=12579432",
            "https://i.pinimg.com/originals/b5/e7/42/b5e7425d51f1c81bc9f2fa027a3c49da.gif",
            "https://data.whicdn.com/images/243040663/original.gif",
            "https://64.media.tumblr.com/064f1eff33b548b84d300341ede510c6/tumblr_pudv2sT7KB1ti7fhko2_400.gif",
            "https://64.media.tumblr.com/90b2c30e19752c8612c855ceae768558/50f44c7772b9630c-c4/s500x750/ce8ff458b59dbea69514dbe9629adfce1835b3fa.gif",
            "https://data.whicdn.com/images/327851772/original.gif",
            "https://i.makeagif.com/media/3-17-2019/XdDqKp.gif",
            "https://i.makeagif.com/media/3-17-2019/RFYYu5.gif",
            "https://66.media.tumblr.com/dd40f1ab9217b7524c80159d088b60be/tumblr_poconkyF1S1x1uv52o2_540.gif",
            "https://data.whicdn.com/images/327983847/original.gif",
            "https://i.makeagif.com/media/3-17-2019/ttrrVC.gif",
            "https://i.makeagif.com/media/3-17-2019/txtBdr.gif",
            "https://i.pinimg.com/originals/b1/d6/d7/b1d6d786633ebaec2f36b7fbc42e53c5.gif",
            "https://i.pinimg.com/originals/86/45/56/864556a7cff6bcac5c1524967b008608.gif",
            "https://imgur.com/fLLI76K",
            "https://64.media.tumblr.com/894fd64265ebd262b8c329d642d03fba/tumblr_pd8ow7gSMd1x1uv52o1_400.gif",
            "https://data.whicdn.com/images/318244140/original.gif",
            "https://data.whicdn.com/images/317279483/original.gif",
            "https://data.whicdn.com/images/319707034/original.gif",
            "https://64.media.tumblr.com/4c6699e9a9dddf2b6d732b035f353c75/tumblr_pecvf4FZXw1swg2mjo4_400.gif",
            "https://64.media.tumblr.com/8f66c866b0cdb40cf0dc28db666fc7a8/5da27baa990fe7b9-ac/s640x960/7fd24eee9f4b580b48d98e26e1ecdd29951212da.gif",
            "https://64.media.tumblr.com/618f0763263e6016b2a88932653c7cf0/3ca417207bc67d2b-c4/s250x400/8a43cdef6612cfaf7aa1396b5b71c4d83113dc30.gif",
            "https://64.media.tumblr.com/c64bc06bc686a8ff1bf71f088bb676ae/tumblr_pkm11tp3261x1uv52o3_400.gif",
            "https://64.media.tumblr.com/aafc04006627152661e25c26e55b0e45/tumblr_pkm11tp3261x1uv52o1_400.gif",
            "https://data.whicdn.com/images/323108938/original.gif",
            "https://pa1.narvii.com/7030/6d405340ba5dfa8c02abfb93105db859b9ad4287r1-268-375_hq.gif",
            "https://i.pinimg.com/originals/06/da/05/06da05ce9aae93a6ad0fc67b004f3198.gif",
            "https://64.media.tumblr.com/7b860da9671d478d73aa6281be15d937/tumblr_pfhfquuhMJ1xu6x27o1_250.gif",
            "https://64.media.tumblr.com/a5ba6f2613cbeea5f46bfd1e38b7e09d/tumblr_pd18da9Bm01x1uv52o1_r2_540.gif",
            "https://68.media.tumblr.com/804600e7d556e956206d6e66cf9343e1/tumblr_ost4qchaUN1s5kxalo3_250.gif",
            "https://i.pinimg.com/originals/40/dc/d0/40dcd0c895bc8df1ec8c053522ad6c28.gif",
            "https://78.media.tumblr.com/403f9431f1ea5c5cf00df031ae342d19/tumblr_othirlHw191ti7fhko2_400.gif",
            "https://64.media.tumblr.com/a85599a27d8aa3d56c6731a160717eb6/tumblr_o4e9zdTtsp1tg6rvso2_r4_400.gif",
            "https://68.media.tumblr.com/308e53a7a51bdd008086016347087055/tumblr_oa5nibLV591ti7fhko5_250.gif",
            "https://68.media.tumblr.com/2d22dd5bb7d5cd117c084b9de446e992/tumblr_oa5nibLV591ti7fhko6_250.gif",
            "https://68.media.tumblr.com/44050ddf7f29423e549e1be1e4cec798/tumblr_o4js4bSElL1tg6rvso2_400.gif",
            "https://68.media.tumblr.com/601a42a90a538810c64ee3870935fae7/tumblr_o4js4bSElL1tg6rvso1_400.gif",
            "https://68.media.tumblr.com/6bb704aa45eb162b0962cdc25470f79b/tumblr_o4js4bSElL1tg6rvso4_r1_400.gif",
            "https://45.media.tumblr.com/4d6f14824ca82834cb80bc8f9075db96/tumblr_o3k272yhtj1s5q5l6o8_400.gif",
            "https://49.media.tumblr.com/2d02c8d773f13586382311cd91d44372/tumblr_o3k272yhtj1s5q5l6o1_400.gif",
            "https://49.media.tumblr.com/78c5f9bcebd3336812f455bc71e4f6d0/tumblr_o3k272yhtj1s5q5l6o6_400.gif",
            "https://38.media.tumblr.com/30040e4e8163c10a715d672d54a60141/tumblr_nvp41jiMCT1uqb8gto3_500.gif",
            "https://49.media.tumblr.com/aa9c057a40b213bb143d129fa0ec0c1e/tumblr_o3tubxLACa1thovwno2_r3_400.gif",
            "https://49.media.tumblr.com/f7deb89c1d007d126b71cf8a3f22d53e/tumblr_o13wrq2Tut1thcsgto1_400.gif",
            "https://49.media.tumblr.com/7767412799398b28cfaf6d76f0c8a458/tumblr_o13wrq2Tut1thcsgto2_400.gif",
            "https://49.media.tumblr.com/acd899dea9a555f0a82e5548ff830ea3/tumblr_o13wrq2Tut1thcsgto4_400.gif",
            "https://49.media.tumblr.com/2fec750b7491a994d4ffd598adbd43a1/tumblr_o13wrq2Tut1thcsgto3_400.gif",
            "https://45.media.tumblr.com/83e8f5ae32f5a3f572ea21e0d42a3d9a/tumblr_o13wrq2Tut1thcsgto5_400.gif",
            "https://45.media.tumblr.com/4f2f04b12e5f083030a1ea8388758eab/tumblr_o13wrq2Tut1thcsgto7_400.gif",
            "https://45.media.tumblr.com/0a92ee1a5427a6cb303a27dfd451d2a8/tumblr_o451ykvAb31ti7d08o4_400.gif",
            "https://45.media.tumblr.com/8a9871bde0bdc1ffd93d8b76cb2d9018/tumblr_o45j2tea4f1ugf371o2_400.gif",
            "https://49.media.tumblr.com/c351c6fb4b2651e63d6333ca73af8474/tumblr_o45b0enAf61v0e4aao2_500.gif",
            "https://68.media.tumblr.com/3dca14c0ea9560177c319425e53d5982/tumblr_oly14k2mHI1vz7a02o7_250.gif",
            "https://s-media-cache-ak0.pinimg.com/originals/c7/69/29/c76929bb1e211c7c1101d436019872ff.jpg",
            "https://66.media.tumblr.com/ae0c20ed0a2708c59c19aff080fe3366/tumblr_nvqimb7wLT1u2a5o6o1_500.gif",
            "https://68.media.tumblr.com/d7ebf4986b5d534b1f8e7b45f2d206e6/tumblr_oq81vtTvWh1uhjfaxo2_540.gif",
            "https://68.media.tumblr.com/b6f02628f6f74c7f6072d23351355c01/tumblr_oq81vtTvWh1uhjfaxo1_540.gif",
            "https://68.media.tumblr.com/09db668be9dafa43765c71c08e6e4033/tumblr_nnbrndFaX41u2ih1oo2_400.gif",
            "https://66.media.tumblr.com/099fe8d545b55b172b80282d1bd75f06/tumblr_od9bv1Rvkp1uq060ko9_400.gif",
            "https://68.media.tumblr.com/71bc95880dc08de67fd8e211e4d8a5fc/tumblr_nudft2ev4g1rov828o1_500.gif",
            "https://64.media.tumblr.com/a8fcc00df3063223aab095ab5e9f83ed/tumblr_on9ew9QpRW1tizu4so2_540.gif",
            "https://64.media.tumblr.com/e1ae29e083b4f8742ee3cae445dda35b/tumblr_on9ew9QpRW1tizu4so1_540.gif",
            "https://64.media.tumblr.com/4320a2420bc898309240ad1ee3c794a9/tumblr_oplmcpjzwJ1ti7fhko1_400.gif",
            "https://64.media.tumblr.com/a93a94eb541de5f901809085089ddf2d/tumblr_oplmcpjzwJ1ti7fhko4_400.gif",
            "https://68.media.tumblr.com/592e521f7cd5ac39cb8163b4ed487562/tumblr_oqakrwKWZP1rm8evlo2_540.gif"]

        self.bot.joy_gif = ["https://tenor.com/view/joy-joy-red-velvet-red-velvet-joy-red-velvet-%EC%A1%B0%EC%9D%B4-gif-19140467",
            "https://tenor.com/view/joy-joy-red-velvet-red-velvet-joy-red-velvet-%EB%B0%95%EC%88%98%EC%98%81-gif-19140470",
            "https://tenor.com/view/joy-red-velvet-red-velvet-joy-joy-red-velvet-gif-19142799",
            "https://tenor.com/view/joy-red-velvet-red-velvet-joy-joy-red-velvet-gif-19142802",
            "https://tenor.com/view/joy-red-velvet-red-velvet-joy-joy-red-velvet-gif-19142804",
            "https://tenor.com/view/red-velvet-joy-red-velvet-joy-joy-red-velvet-park-soo-young-gif-19142825",
            "https://tenor.com/view/joy-hi-redvelvet-hello-waving-gif-11110834",
            "https://tenor.com/view/red-velvet-joy-red-velvet-joy-joy-red-velvet-park-soo-young-gif-19142833",
            "https://tenor.com/view/joy-red-velvet-red-velvet-joy-joy-red-velvet-park-soo-young-gif-19142846",
            "https://tenor.com/view/joy-red-velvet-gif-11882538",
            "https://tenor.com/view/joy-joy-red-velvet-red-velvet-korea-gif-18169146",
            "https://tenor.com/view/joy-red-velvet-park-sooyoung-gif-12536684",
            "https://tenor.com/view/joy-red-velvet-joy-red-velvet-gif-11882544",
            "https://tenor.com/view/joy-red-velvet-gif-11882537",
            "https://tenor.com/view/kpop-gif-10448235",
            "https://tenor.com/view/park-sooyoung-joy-red-velvet-wave-hi-gif-12536019",
            "https://tenor.com/view/joy-red-velvet-joy-park-joy-park-sooyoung-%EC%A1%B0%EC%9D%B4-gif-13910368",
            "https://tenor.com/view/joy-red-velvet-kpop-cute-pretty-gif-17059487",
            "https://tenor.com/view/joy-red-velvet-gif-11882529",
            "https://cdn.discordapp.com/attachments/776007496321990666/776011215993438208/park.gif",
            "https://cdn.discordapp.com/attachments/776007496321990666/776011680593084466/heart.gif",
            "https://i.pinimg.com/originals/d8/1a/03/d81a03b3aeb12a985fec7fb4e1135973.gif",
            "https://i.pinimg.com/originals/ad/23/bc/ad23bc99f511ffc236502c6a7c31e87b.gif",
            "https://64.media.tumblr.com/eef515b87bef807ce26add8a5bd261a0/tumblr_pd19aw91gf1x4vf4mo1_540.gif",
            "https://data.whicdn.com/images/323252826/original.gif",
            "https://pa1.narvii.com/6947/0db4eb2bbda975024684ce3eb2ee50e63b0889b8r1-420-185_hq.gif",
            "https://i.pinimg.com/originals/db/a8/00/dba8003945f735ec0534c2fe61507483.gif",
            "https://data.whicdn.com/images/302027092/original.gif",
            "https://i.pinimg.com/originals/15/8c/63/158c63c8a89cd86d8586726b9056e024.gif",
            "https://i.pinimg.com/originals/de/48/50/de4850b868e8884180992997f657b0b5.gif",
            "https://i.pinimg.com/originals/a5/f9/3e/a5f93e8cedbf989f0e6210d76e845bae.gif",
            "https://pa1.narvii.com/6575/cd9c6032a1293f7b4d37b13088f6cb5d5e39dff2_hq.gif",
            "https://data.whicdn.com/images/332797125/original.gif",
            "https://data.whicdn.com/images/306285895/original.gif",
            "https://media1.tenor.com/images/4819071110ca0841c6404f8c11663112/tenor.gif?itemid=8620197",
            "https://data.whicdn.com/images/325056734/original.gif",
            "https://64.media.tumblr.com/03e8679e55b492a597d33871ef671b61/tumblr_pkv6da2pXE1vzhooro1_540.gif",
            "https://thumbs.gfycat.com/BowedRespectfulBettong-max-1mb.gif",
            "https://i.pinimg.com/originals/41/33/7c/41337c469b9da9df2bd067ef982d6ea4.gif",
            "https://thumbs.gfycat.com/BewitchedUnawareFreshwatereel-size_restricted.gif",
            "https://thumbs.gfycat.com/CheerfulTimelyGar-max-14mb.gif",
            "https://data.whicdn.com/images/237846376/original.gif",
            "https://media1.tenor.com/images/9c36c78d57f5f5185303a224f50c96b6/tenor.gif?itemid=12576883",
            "https://i.pinimg.com/originals/db/a8/00/dba8003945f735ec0534c2fe61507483.gif"]

        self.bot.redvelvet_group_gif = ["https://i.pinimg.com/originals/69/88/a3/6988a3beb07459e565763eb59c99e938.gif",
            "https://i.pinimg.com/originals/0b/6b/41/0b6b41f6b5b7a2f14ef136c671e939cf.gif",
            "https://i.gifer.com/C4GX.gif",
            "https://i.gifer.com/JRuP.gif",
            "https://i.pinimg.com/originals/58/ed/45/58ed456ab9d31d215cb60fd7243140c5.gif",
            "https://pa1.narvii.com/6213/37d190c7def1e7355d939639478cc46685f534fc_hq.gif",
            "https://i.gifer.com/Hhbl.gif",
            "https://64.media.tumblr.com/8c88e17cfd9fb04e73b7ed609953c21a/tumblr_ob7q7ii2RV1vurgqao1_500.gif",
            "https://33.media.tumblr.com/fbf6d7bbd358842bb95d17014939ea17/tumblr_nud3e0Xm7y1tiedrso2_540.gif",
            "http://38.media.tumblr.com/23e5e64bb2a82631e0ba0a834a4851bb/tumblr_nud4gg1d2j1r315cio3_540.gif",
            "https://pa1.narvii.com/6111/f06e42305d7578842f29920259cb2cf33ac8cd64_hq.gif",
            "https://pa1.narvii.com/6246/88c5e1416fafe0cb587162ddb0c9d92905067d84_hq.gif",
            "https://64.media.tumblr.com/b34116979fdc9a6e5aa4b3457fc3acba/9a77db56d2e80a60-5d/s540x810/093a6c02b67066c3112f2346ed1ee8d77ec21125.gif",
            "https://data.whicdn.com/images/300338202/original.gif",
            "https://i.pinimg.com/originals/f0/1b/f7/f01bf755bef7c36a4d83d4a5bc4f0e5a.gif",
            "https://66.media.tumblr.com/17c89f8520d390bc8821df4cb94981bf/tumblr_pbvgidEOgd1whjw8go3_500.gif",
            "https://data.whicdn.com/images/304852689/original.gif",
            "https://data.whicdn.com/images/277300422/original.gif",
            "https://media1.tenor.com/images/e9fe9c69e0802ec3bc835e4f54c049a7/tenor.gif?itemid=17083585",
            "https://i.pinimg.com/originals/d8/9c/5b/d89c5b5cf4a0fd22ad9129d5d0007ed9.gif",
            "https://i.gifer.com/AOS9.gif",
            "https://data.whicdn.com/images/314362965/original.gif",
            "https://data.whicdn.com/images/314383732/original.gif",
            "https://pa1.narvii.com/6866/07a795e6869f42c3e06a52d293b204548f42da40r1-540-230_hq.gif",
            "https://data.whicdn.com/images/313716083/original.gif",
            "https://64.media.tumblr.com/700477914dc43e27539277191a9ebcb4/c52377a6bcb2b08e-01/s540x810/548ce6fbb3004ea3ad94a18da1e56d760771a042.gif",
            "https://data.whicdn.com/images/315086075/original.gif?t=1530661540"]

    @commands.command()
    async def red(self, ctx, vel="velvet", *, arg = "ot5"):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Red Velvet {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if vel == "velvet":
            if arg == "irene":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@{jon}>, <@!{ctx.author.id}> is talking about Irene :watermelon:')
                        await ctx.send(random.choice(self.bot.irene_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Irene :watermelon:')
                    await ctx.send(random.choice(self.bot.irene_gif))
                    await ctx.message.delete()
            elif arg == "seulgi":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Seulgi :pineapple:')
                    await ctx.send(random.choice(self.bot.seulgi_gif))
                    await ctx.message.delete()
            elif arg == "wendy":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Wendy :blue_heart:')
                    await ctx.send(random.choice(self.bot.wendy_gif))
                    await ctx.message.delete()
            elif arg == "yeri":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Yeri :grapes:')
                    await ctx.send(random.choice(self.bot.yeri_gif))
                    await ctx.message.delete()
            elif arg == "joy":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Joy :kiwi:')
                    await ctx.send(random.choice(self.bot.joy_gif))
                    await ctx.message.delete()
            elif arg == "ot5":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Red Velvet :heart:')
                    await ctx.send(random.choice(self.bot.redvelvet_group_gif))
                    await ctx.message.delete()

def setup(client):
    client.add_cog(RedVelvetPings(client))