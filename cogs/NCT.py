import discord, random
from discord.ext import commands
from datetime import datetime

#//servers
luminary = 758468592957521972

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

class NCT(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
        self.bot.nct_lucas_gif = ["https://tenor.com/view/lucas-wayv-heart-gif-14723401",
            "https://tenor.com/view/smile-handsome-cute-lucas-nct-gif-15246419",
            "https://tenor.com/view/nct-lucas-nct-lucas-cute-smile-gif-12612522",
            "https://tenor.com/view/nct-lucas-being-extra-hi-gif-14904496",
            "https://tenor.com/view/pout-kiss-handsome-cute-lucas-gif-15246420",
            "https://tenor.com/view/lucas-nct-way-v-gif-13770508",
            "https://tenor.com/view/wong-yukhei-lucas-nct-cute-kpop-gif-16350448",
            "https://tenor.com/view/lucas-nct-wayv-gif-19030351",
            "https://tenor.com/view/lucas-nct-smile-gif-19015832",
            "https://tenor.com/view/lucas-smile-cute-poke-cheek-gif-12719055",
            "https://tenor.com/view/lucas-nct-wong-yukhei-wayv-gif-14579895",
            "https://tenor.com/view/lucas-lucasspecial-hunk-daddy-lucasabs-gif-19057230",
            "https://tenor.com/view/lucas-nct-gif-18844446",
            "https://tenor.com/view/bad-alive-music-video-wayv-nct-lucas-gif-17944712",
            "https://tenor.com/view/nct-yearbook-photoshoot-pose-gif-13626687",
            "https://gfycat.com/defenselesssnoopydove",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-u5hVwoY3GtPt935jrz",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-Nyc1N8AwIHt4X7Ihi2",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-i499c3xkvwFtiofT6g",
            "https://64.media.tumblr.com/8726998367d408b9becf22cf21980f83/3da403ca6112e1ca-83/s400x600/87a5f70f92477def1479cb2323b4d915fbe3efc3.gif",
            "https://64.media.tumblr.com/0251d83bd2bdad6b0562af6ee0933a1c/140e02c93672e4df-31/s400x600/1540482fed8d224d116f5e45823c5c1448c590b3.gif"]

        self.bot.nct_mark_gif = ["https://tenor.com/view/mark-lee-nct-school-rapper-gif-9575546",
            "https://tenor.com/view/nct-mark-lee-swimming-gif-14378569",
            "https://tenor.com/view/nct-mark-oh-yeah-gif-13990858",
            "https://tenor.com/view/nct-nct127-nct2019-wakey-wakey-wakey-gif-13764197",
            "https://tenor.com/view/chill-relax-stuffed-animals-lay-down-mark-gif-16109322",
            "https://tenor.com/view/cute-mark-lee-kpop-handsome-nct-gif-16625675",
            "https://tenor.com/view/mark-lee-aestethic-mark-lee-boyfriend-mark-bad-boy-mark-superm-mark-gif-18373893",
            "https://tenor.com/view/nct-nct127-mark-mark-lee-lee-min-hyung-gif-17366636",
            "https://tenor.com/view/mark-smiling-nct-kpop-gif-9061895",
            "https://tenor.com/view/tipton2109-nct-nct-mark-mark-lee-regular-gif-13173755",
            "https://tenor.com/view/mark-mark-lee-superm-mark-superm-nct-mark-gif-18379738",
            "https://tenor.com/view/mark-heart-nct-k-pop-gif-9674546",
            "https://tenor.com/view/tipton2109-nct-mark-smile-gif-13172322",
            "https://tenor.com/view/mark-mark-lee-nct-cold-eating-gif-14683790",
            "https://tenor.com/view/super-m-mark-lee-nct-dream-%EB%A7%88%ED%81%AC-127-gif-17019572",
            "https://tenor.com/view/wink-nct-mark-cute-smile-gif-12423198",
            "https://tenor.com/view/mark-mark-lee-nct-kpop-cute-gif-16094611",
            "https://tenor.com/view/tipton2109-nct-mark-lee-eating-gif-13173807",
            "https://tenor.com/view/mark-lee-serious-fierce-pose-nct-gif-13469194",
            "https://tenor.com/view/nct-nct127-mark-lee-kpop-choc-chipg-gukies-gif-14393243",
            "https://tenor.com/view/mark-lee-nct-nct127-kpop-gif-19380061",
            "https://tenor.com/view/mark-lee-aestethic-mark-lee-boyfriend-mark-bad-boy-mark-superm-mark-gif-18373893",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435531685953566/image0.gif",
            "https://giphy.com/gifs/nctsmtown-nct-127-highway-to-heaven-YQBpUUFF2g226dXEBc",
            "https://giphy.com/gifs/nctsmtown-nct-127-highway-to-heaven-JUFm2EXF4IrKqZ6BF9",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-QYjt6B9r26p4odudpH",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-Kb5VEV4AIqPmb0hmaH",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-172-bRtW9WyXyRFwvMli8A",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-172-sVNY9PkKBEGlnsN1JW",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-VS8myHwaL43gIiz2vs",
            "https://gfycat.com/JubilantSelfassuredIndianabat",
            "https://gfycat.com/HardSingleBittern",
            "https://gfycat.com/IncomparableVengefulAurochs",
            "https://gfycat.com/EsteemedEnlightenedBats",
            "https://gfycat.com/ScratchyRemoteDingo",
            "https://gfycat.com/GreedyComplexBovine",
            "https://gfycat.com/ForthrightQuarrelsomeHorsefly",
            "https://gfycat.com/JubilantWhiteBagworm",
            "https://gfycat.com/FaithfulGleefulAmmonite",
            "https://gfycat.com/GiftedMisguidedFireant"]

        self.bot.nct_winwin_gif = ["https://tenor.com/view/winwin-nct-127-way-v-gif-13776784",
            "https://tenor.com/view/dong-siicheng-winwin-nct-wayv-cute-gif-14464703",
            "https://tenor.com/view/dong-sicheng-sicheng-dong-winwin-wayv-gif-14997192",
            "https://tenor.com/view/nct-127-winwin-gif-14168699",
            "https://tenor.com/view/nct-wayv-winwin-nct-wayv-teaser-gif-13760142",
            "https://tenor.com/view/winwin-dancing-winwin-flossing-winwin-hani3-gif-19452678",
            "https://tenor.com/view/winwin-wayv-sicheng-dongsicheng-gif-14098151",
            "https://tenor.com/view/winwin-nct-nct127-dong-si-cheng-dong-sa-sung-gif-17360118",
            "https://tenor.com/view/winwin-winwin-happy-wayv-nct-equifinality-gif-14896880",
            "https://tenor.com/view/nct-nct127-kpop-ccg-bunny-gif-14846461",
            "https://tenor.com/view/nct-wayv-dong-sicheng-winwin-chinese-rapper-gif-15797790",
            "https://tenor.com/view/nct-wayv-dong-sicheng-winwin-chinese-rapper-gif-15797792",
            "https://tenor.com/view/nct-yuta-winwin-love-yuwin-gif-11839935",
            "https://gfycat.com/definitivecreativebagworm-let-me-love-u-weishenv-yangyang-hendery",
            "https://gfycat.com/lavishdeterminedalpineroadguidetigerbeetle",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-172-cXGwNxRJHkbiZTWH3R",
            "https://gfycat.com/ShallowOrangeIvorygull",
            "https://gfycat.com/SoupySmoggyChanticleer",
            "https://gfycat.com/FrigidElderlyEasternglasslizard",
            "https://gfycat.com/ElderlyPleasingChuckwalla",
            "https://gfycat.com/FickleRipeArmadillo",
            "https://cdn.discordapp.com/attachments/790419146030317578/819224178854854736/Tumblr_l_1157633029848552.gif",
            "https://cdn.discordapp.com/attachments/790419146030317578/819224179164708864/Tumblr_l_1157631458539125.gif",
            "https://cdn.discordapp.com/attachments/790419146030317578/819224179588988988/Tumblr_l_1157628709559022.gif",
            "https://cdn.discordapp.com/attachments/790419146030317578/819224195267166228/Tumblr_l_1157627041408814.gif",
            "https://cdn.discordapp.com/attachments/790419146030317578/819224195505717302/Tumblr_l_1157625458890325.gif",
            "https://cdn.discordapp.com/attachments/790419146030317578/819224195888054282/Tumblr_l_1157623061757826.gif",
            "https://cdn.discordapp.com/attachments/790419146030317578/819224208164913212/Tumblr_l_1157622001686733.gif",
            "https://cdn.discordapp.com/attachments/790419146030317578/819224208491806761/Tumblr_l_1157620093707567.gif",
            "https://cdn.discordapp.com/attachments/790419146030317578/819224208793272320/Tumblr_l_1157619186094755.gif",
            "https://64.media.tumblr.com/c3cadccebf30913d91d5bba5b50a1906/9be6f63619859bd9-d3/s540x810/b82dba64a4a76afc1bd0b210b2968ead9c127bf0.gif",
            "https://64.media.tumblr.com/591b99ef8c3a46477a21e130509cd60d/d127c60627a34218-fb/s540x810/cfc9262662a8e271af508722cddf67918cb0d92e.gif",
            "https://64.media.tumblr.com/c6f7631c7f5c978b474937455beca55e/d127c60627a34218-c6/s540x810/5ec85880e5b1daadfc79876c47e3c15130e0ffa8.gif",
            "https://64.media.tumblr.com/dd192138e30a3a84bd3d913fe9c30ce0/140e02c93672e4df-92/s400x600/a01eb9af02ca6f3e7dbc86983cd36425d39ab726.gif",
            "https://64.media.tumblr.com/0f7b1950d46e76ec5c4d74e363430b36/ea0352b5ba837d08-d0/s400x600/a0e49471478f26bcda2215680c8600414f67e360.gif"]

        self.bot.nct_jaemin_gif = ["https://cdn.discordapp.com/attachments/772975408912007180/790097423921315840/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790097683116326912/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790097724523282432/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790097737801793537/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790101053294510090/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790101053399629834/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790101176627625984/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790101177252839454/image1.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790103352352178196/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790103993077596170/image1.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790104121116983346/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790104121600376842/image1.gif",
            "https://tenor.com/view/jaemin-nct-dream-kpop-cute-smile-gif-16969202",
            "https://tenor.com/view/love-heart-shape-smile-cute-sm-entertainment-gif-15115182",
            "https://tenor.com/view/jaemin-na-jaemin-ice-cream-kpop-cute-gif-16621837",
            "https://tenor.com/view/jaemin-nct-dream-nct-smile-kpop-gif-16452165",
            "https://tenor.com/view/smile-cute-sm-entertainment-nct-dream-jaemin-gif-15115166",
            "https://tenor.com/view/hand-kiss-hand-kiss-jaemin-na-gif-18900580",
            "https://tenor.com/view/chenle-jaemin-nct-dream-zhong-chenle-na-jaemin-gif-16857724",
            "https://tenor.com/view/kiss-jaemin-nct-na-jaemin-kpop-gif-16392459",
            "https://tenor.com/view/jaemin-nana-na-jaemin-nct-smile-gif-17013043",
            "https://tenor.com/view/kpop-boy-boring-nct-dream-jaemin-gif-15115161",
            "https://tenor.com/view/jaemin-nct-dream-serious-cute-handsome-gif-17041026",
            "https://tenor.com/view/na-jae-min-jaemin-nct-dream-wink-gif-14754677",
            "https://cdn.discordapp.com/attachments/794052570574225478/804433282631729232/image0.gif",
            "https://gfycat.com/differentdarkcolt-sm-entertainment-haechan-chenle-jaemin",
            "https://giphy.com/gifs/nctsmtown-nct-127-u-xLsubrckeG2eUD2J19",
            "https://giphy.com/gifs/nctsmtown-nct-127-u-KTY1NKqWu3uNjb2niu",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-tUBSmzCGLGfAYynRTu",
            "https://64.media.tumblr.com/39d9536c2228b944dfd596ccbbd8e16f/1b91aaec34336370-03/s400x600/0c301160b8475b80adcd085b7966c1bbc8695216.gif"]

        self.bot.nct_jaehyun_gif = ["https://tenor.com/view/jaehyun-kiss-nct-127-kpop-gif-15454039",
            "https://tenor.com/view/nct127-nct-kick-it-jeong-jaehyun-nct-jaehyun-gif-18047865",
            "https://tenor.com/view/gifmiah-gif-19600506",
            "https://tenor.com/view/handsome-jaehyun-nct-nct127-nct-u-gif-16653893",
            "https://tenor.com/view/chill-relax-whatever-smile-kpop-gif-15545125",
            "https://tenor.com/view/cute-smile-nct-jaehyun-kpop-gif-16350460",
            "https://tenor.com/view/nct-jaehyun-tipton2109-jaehyun-nct-coatoff-gif-13173729",
            "https://tenor.com/view/nct-kpop-ccg-pinch-cheek-gif-14838121",
            "https://tenor.com/view/jaehyun-nct127-blow-kiss-kpop-cute-gif-15315336",
            "https://tenor.com/view/kpop-nct-jaehyun-heart-gif-14324479",
            "https://tenor.com/view/nct-jaehyun-jung-jungjaehyun-yoonoh-gif-12928593",
            "https://tenor.com/view/jaehyun-nct-kpop-peace-cute-gif-14544427",
            "https://tenor.com/view/jaehyun-miahsgifs-gif-19370411",
            "https://tenor.com/view/jaehyun-nct-brush-up-kpop-gif-14081724",
            "https://tenor.com/view/jaehyun-cute-bunny-ears-gif-13909975",
            "https://tenor.com/view/jung-jaehyun-nct-nct127-nct-u-jaehyun-nct-gif-18351037",
            "https://tenor.com/view/jaehyun-nct-dimples-cute-kiss-gif-19337661",
            "https://tenor.com/view/jaehyun-nct-nct127-its-always-sunny-jaehyun-charlie-gif-18830480",
            "https://tenor.com/view/jaehyun-nct-kpop-nod-gif-9008248",
            "https://tenor.com/view/nct-sm-entertainment-sm-jaehyun-nct-jaehyun-gif-9009058",
            "https://tenor.com/view/jaehyun-jung-jaehyun-nct-nct127-nct2018-gif-14375589",
            "https://tenor.com/view/nct127-jaehyun-crying-sad-gif-14692588",
            "https://tenor.com/view/nct-jaehyun-go-jaehyun-dance-kpop-gif-18739096",
            "https://tenor.com/view/nct-nct127-jaehyun-jung-yoon-oh-lead-vocalist-gif-17661505",
            "https://tenor.com/view/kpop-ccg-nct-nct127-jaehyun-gif-14887755",
            "https://tenor.com/view/jaehyun-nct-kpop-smile-laugh-gif-16504962",
            "https://tenor.com/view/jaehyun-bff-sexy-jeong-yuno-jeong-jae-hyun-gif-15275566",
            "https://tenor.com/view/sexy-park-jinyoung-abs-gif-15318396",
            "https://tenor.com/view/nct-jaehyun-cute-smile-k-pop-gif-11533337",
            "https://tenor.com/view/jaehyun-nctjaehyun-jeongjaehyun-jeongyoonoh-nct-gif-19065427",
            "https://tenor.com/view/jaehyunn-gif-18383986",
            "https://tenor.com/view/kpop-nct-jaehyun-heart-gif-14324479",
            "https://tenor.com/view/jaehyun-jung-jaehyun-gif-18837045",
            "https://tenor.com/view/jeong-yuno-jaehyun-nct-kpop-cute-gif-17383014",
            "https://tenor.com/view/jaehyun-jung-jaehyun-nct-nct127-nct2018-gif-14375590",
            "https://tenor.com/view/jaehyun-jung-jaehyun-gif-18837043",
            "https://tenor.com/view/jaehyun-nct-jungjaehyun-gif-11568836",
            "https://tenor.com/view/jungjaehyun-clapping-nctu-nct127-nct-gif-11853050",
            "https://tenor.com/view/jaehyun-bff-sexy-jeong-yuno-jeong-jae-hyun-gif-15275553",
            "https://tenor.com/view/jaehyun-nct-dance-kpop-gif-14544431",
            "https://tenor.com/view/jaehyun-jung-nct127-cute-dance-nct-jaehyun-gif-14733874",
            "https://tenor.com/view/nct-nct127-jaehyun-coffee-work-gif-12640382",
            "https://cdn.discordapp.com/attachments/772975408912007180/790116651960893440/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790116930018607114/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790116930568585256/image1.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790116946061688852/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790117215944704010/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790117416230322206/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790117616676634645/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790117617339072512/image1.gif",
            "https://cdn.discordapp.com/attachments/199465139026657280/805690845407739944/210131_6.gif",
            "https://data.whicdn.com/images/248620976/original.gif",
            "https://cdn.discordapp.com/attachments/199465139026657280/805690803719634964/210131_5.gif",
            "https://cdn.discordapp.com/attachments/199465139026657280/805690768907698186/210131_4.gif",
            "https://cdn.discordapp.com/attachments/199465139026657280/805690703363178496/210131_2.gif",
            "https://cdn.discordapp.com/attachments/199465139026657280/805690665945661470/210131.gif",
            "https://cdn.discordapp.com/attachments/199465139026657280/810887657353117716/jaehyun_h.gif",
            "https://tenor.com/view/jaehyun-brown-hair-nct127-nct-smile-gif-17312204",
            "https://tenor.com/view/jaehyun-jae-nct-jung-jaehyun-jaehyun-nct-gif-19681222",
            "https://tenor.com/view/jaehyun-nct-gif-18953406",
            "https://tenor.com/view/nct-nct127-kpop-ccg-jaehyun-gif-16032827",
            "https://tenor.com/view/nct-jaehyun-jeong-yoonoh-abs-show-abs-gif-16359184",
            "https://tenor.com/view/jaehyun-hula-hoop-nct-k-pop-dancing-gif-8970838",
            "https://tenor.com/view/jaehyun-jung-gif-18924213",
            "https://tenor.com/view/awkward-cute-smile-jaehyun-gif-14232505",
            "https://tenor.com/view/jaehyun-nct-hunk-abs-shirt-off-gif-14549666",
            "https://tenor.com/view/jaehyun-nct-jung-127-cute-gif-14997183",
            "https://tenor.com/view/nct-nct127-nct2019-superhuman-james-corden-gif-14137623",
            "https://tenor.com/view/jaehyuk-gif-20064155",
            "https://tenor.com/view/jaehyuk-gif-20065364",
            "https://tenor.com/view/jaehyun-spooky-jaehyun-jung-jaehyun-jeong-jaehyun-jaehyun-sena-gif-19366085",
            "https://tenor.com/view/jaehyun-jaehyun-nct-nct-jaehyun-johnny-johnny-nct-gif-18770253",
            "https://tenor.com/view/jaehyun-nct-nct127-hot-sexy-gif-10244887",
            "https://tenor.com/view/wakey-wakey-nct-jaehyun-hot-mv-gif-15159878",
            "https://tenor.com/view/sexy-jaehyun-nct-kpop-handsome-gif-15159824",
            "https://tenor.com/view/jaehyun-sexy-hot-nct-dance-gif-14397472",
            "https://tenor.com/view/eyeroll-jaehyun-nct-kpop-gif-12221341",
            "https://tenor.com/view/jaehyun-nct-nct127-kpop-sleepy-gif-13931352",
            "https://tenor.com/view/poetic-jaehyun-smile-gif-19763125",
            "https://tenor.com/view/tipton2109-nct-jaehyun-smile-happy-gif-13173808",
            "https://tenor.com/view/smile-handsome-cute-gif-17210508",
            "https://tenor.com/view/jaehyun-soyboy-jaehyuncringe-smile-jaehyunsmile-gif-18830591",
            "https://tenor.com/view/jaehyun-nct-kpop-smile-gif-9008243",
            "https://tenor.com/view/jaehyun-jung-jaehyun-nct-nct127-nct2018-gif-14375588",
            "https://tenor.com/view/jaehyun-jung-jaehyun-ngambek-nct-gif-19681276",
            "https://tenor.com/view/jaehyun-nct-nct-jaehyun-jung-jaehyun-gif-18356305",
            "https://tenor.com/view/jaehyun-nct-vibing-vibe-music-gif-19478467",
            "https://tenor.com/view/jaehyun-jung-jaehyun-gif-18837049",
            "https://tenor.com/view/jaehyun-nct-sunglass-model-jung-yoon-oh-gif-12751889",
            "https://cdn.discordapp.com/attachments/199465139026657280/794393984423690290/img1.daumcdn.gif",
            "https://cdn.discordapp.com/attachments/199465139026657280/794393353714008085/411fc42f04690a4ab412bef8fd2b6d6e.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812433295128002630/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812433306113015878/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812433314592849970/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812433321136226334/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812433324248530954/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812433338248724530/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812433342863114270/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812433349091786824/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812433354287743069/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435306560487424/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435385338691614/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435394821881906/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435402648453140/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435412425375824/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435418997850153/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435432629469184/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435437682688000/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435482674987055/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435531685953566/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435534516584488/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435546638385182/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435551402721291/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435561234956308/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435569883480095/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435598714732565/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435607694606386/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812435631975170068/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812436514730541126/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812436586456809539/image0.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812436587359109150/image1.gif",
            "https://cdn.discordapp.com/attachments/794052637024059443/812436590336540672/image2.gif",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-Bku1doI6JyAXJJDLLc",
            "https://tenor.com/view/jaehyun-kiss-nct-127-kpop-gif-15454039",
            "https://tenor.com/view/nct127-neo-culture-technology127-kpop-kick-it-jaehyun-gif-16603649",
            "https://tenor.com/view/jaehyun-brown-hair-nct127-nct-smile-gif-17312204",
            "https://giphy.com/gifs/nctsmtown-nct-127-highway-to-heaven-fvTyUB7qBzHZIqG9xo",
            "https://giphy.com/gifs/nctsmtown-nct-127-highway-to-heaven-h4kpeInzW26mnl7q9K",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-QZ2WEYReF4GQ32ak2u",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-ZdrNfc8OxKmjojoBDq",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-dM7e06nO13X0PW9vS3"]

        self.bot.nct_kun_gif = ["https://tenor.com/view/kun-wayv-nct-gif-19030306",
            "https://tenor.com/view/kun-kun-from-home-nct-from-home-mv-from-home-gif-18886755",
            "https://tenor.com/view/way-v-qian-kun-cute-nct-gif-14621591",
            "https://tenor.com/view/way-v-qian-kun-nct-kun-handsome-gif-15937670",
            "https://tenor.com/view/qian-kun-kun-qian-wayv-gif-18761255",
            "https://tenor.com/view/neo-culture-technology-nct-nctzen-kun-qian-kun-gif-12100534",
            "https://tenor.com/view/way-v-qian-kun-nct-kun-handsome-gif-15937667",
            "https://tenor.com/view/kun-wayv-nct-gif-19030350",
            "https://tenor.com/view/way-v-qian-kun-nct-kun-handsome-gif-15937652",
            "https://tenor.com/view/way-v-qian-kun-nct-kun-handsome-gif-15937660",
            "https://gfycat.com/grandioseopenbillygoat-wayv-kun-nct",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-p8KfgL5e1bkwnaSHx1",
            "https://tenor.com/view/kun-wayv-turn-back-time-gif-18999711",
            "https://cdn.discordapp.com/attachments/790418977092010064/819224430801846302/Tumblr_l_1157680677587908.gif",
            "https://cdn.discordapp.com/attachments/790418977092010064/819224431585918996/Tumblr_l_1157677887789732.gif",
            "https://cdn.discordapp.com/attachments/790418977092010064/819224432391749703/Tumblr_l_1157676551526243.gif",
            "https://cdn.discordapp.com/attachments/790418977092010064/819224433125359616/Tumblr_l_1157673630093015.gif",
            "https://cdn.discordapp.com/attachments/790418977092010064/819224433909956608/Tumblr_l_1157674652117702.gif",
            "https://gfycat.com/whirlwinddangerousbird-wayv-ehind-weishenv-takeoff-music-wu-yi-er-fei",
            "https://64.media.tumblr.com/3d9e3e214707fe9461aeeefabd0b805c/ea0352b5ba837d08-47/s400x600/af1dda2cb9bca4c512fb59e9416ec8841e705610.gif"]

        self.bot.nct_ten_gif = ["https://tenor.com/view/ten-nct-singing-nct-kpop-gif-14732794",
            "https://tenor.com/view/ten-nct-ten-nct-mark-lee-wayv-gif-14997188",
            "https://tenor.com/view/ten-chittaphon-leechaiyapornkul-nct-gif-18900846",
            "https://tenor.com/view/nct-chittaphon-ten-k-pop-gif-11577935",
            "https://tenor.com/view/tenalice-wayv-nct-ten-gif-19016713",
            "https://tenor.com/view/ten-dancing-nct-nctu-nct2018-gif-11536073",
            "https://tenor.com/view/ten-nct-way-v-finger-heart-cute-gif-14733893",
            "https://tenor.com/view/ten-nct-superm-wayv-wayv-ten-gif-19468090",
            "https://tenor.com/view/nct-kpop-ccg-chittaphon-leechaiyapornkul-ten-gif-14839951",
            "https://giphy.com/gifs/nctsmtown-nct-127-u-w9xPevVQxzss7NKL39",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-172-qwrqKiFGiBC5BNQVDx",
            "https://64.media.tumblr.com/eae55d7be9406b63883af46c5e64e562/470f67f1f79dfda4-0f/s540x810/00ad532f7dadfe6422fc38cc04fbbe021712de4a.gif",
            "https://64.media.tumblr.com/5535d1f92a9fda943dd4ff13fa0cfc40/470f67f1f79dfda4-cb/s540x810/74e44acdd21306c8425f1aea06f2620e58c874df.gif",
            "https://64.media.tumblr.com/6c3b6b6db4335c0f736c3e3439bff827/44d1074433fee229-e8/s400x600/95bd5e8634d7e7237502ed039bb2d97fe3d7b40e.gif",
            "https://64.media.tumblr.com/feb99ca3c67e3654af62d5a722673ef9/0fb517e6ec8ed2f3-59/s400x600/7120559946c9c254b14ffe46faf95b36e7801662.gif",
            "https://64.media.tumblr.com/f482994e461bca228cfb7d976ac20f7c/140e02c93672e4df-eb/s400x600/67a09d71a00c7e6e014334b7faf5b48f03011ead.gif",
            "https://64.media.tumblr.com/28134a5e49c9ed8488f23a64ee37b3a7/ea0352b5ba837d08-9a/s400x600/ab59c768039912cdf7338895e93921e0942872a6.gif"]

        self.bot.nct_xiaojun_gif = ["https://tenor.com/view/wayv-nct-xiaojun-xiao-de-jun-handsome-gif-15963229",
            "https://tenor.com/view/nct-wayv-xiaojun-nct-wayv-regular-gif-13760124",
            "https://tenor.com/view/wayv-nct-xiaojun-xiao-de-jun-handsome-gif-15963240",
            "https://tenor.com/view/nct-gif-18778907",
            "https://tenor.com/view/wayv-nct-xiao-xiaojun-xiao-de-jun-gif-17708608",
            "https://tenor.com/view/wayv-nct-xiao-xiaojun-xiao-de-jun-gif-17708295",
            "https://tenor.com/view/wayv-xiaojun-wayv-xiaojun-wayv-princess-nct-gif-19170087",
            "https://tenor.com/view/xiaojun-dejun-wayv-gif-19479598",
            "https://tenor.com/view/wayv-nct-xiaojun-xiao-de-jun-handsome-gif-15963228",
            "https://tenor.com/view/wayv-nct-xiaojun-xiao-de-jun-handsome-gif-15963227",
            "https://tenor.com/view/xiaojun-assdaya-wayv-embarrassed-gif-19225097",
            "https://cdn.discordapp.com/attachments/772975408912007180/790097352589180968/image0.gif",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-UcDvbvOQcoVAShlctP",
            "https://64.media.tumblr.com/b3128ca4300e3fba281515e37708b209/3c19e60818abaec5-53/s500x750/6f4625e52f3cfe70ebc8599b7f9f81d3c704961d.gif",
            "https://64.media.tumblr.com/03f668b12f1dbd0879870a4949b59add/3c19e60818abaec5-ea/s500x750/fe40fbdb125d0b80b39a0ccc86becd1bc0f1044a.gif",
            "https://64.media.tumblr.com/e46892bacd2dbed257300cbd3f307dfe/3c19e60818abaec5-00/s500x750/75d4f360ba89138d97147c2b7d73f6bed7ee2ee5.gif",
            "https://64.media.tumblr.com/ea288a013030a3edc3162dee14b10e0d/560e73b1ac211a25-4e/s400x600/59f11be21fdf5c8acc92680a010ff95a55b32687.gif",
            "https://64.media.tumblr.com/3d1f21df190bf1f7fa05143c5b36028c/ea0352b5ba837d08-aa/s400x600/96b02a46236989c3d47cbb6c090c4e7bcef6a86c.gif",
            "https://64.media.tumblr.com/79708d31c326042d94ebdacdb7ab1489/140e02c93672e4df-21/s400x600/983bc2cfab5b7b8f88de0fd6f16b9eb030f2c58b.gif"]

        self.bot.nct_hendery_gif = ["https://tenor.com/view/hendery-wayv-heart-gif-14544395",
            "https://tenor.com/view/wayv-nct-hendery-wong-kunhang-handsome-gif-16028474",
            "https://tenor.com/view/hendery-wayv-gif-14682187",
            "https://tenor.com/view/wayv-nct-hendery-weishenv-kpop-gif-18979010",
            "https://tenor.com/view/rjwdz-hendery-gif-19116582",
            "https://tenor.com/view/hendery-wayv-heart-kpop-gif-14544389",
            "https://tenor.com/view/wayv-wayv-princess-nct-hendery-henpunzel-gif-19170091",
            "https://tenor.com/view/hendery-gif-19183671",
            "https://tenor.com/view/hendery-wayv-kpop-smile-gif-14544403",
            "https://tenor.com/view/hendery-wayv-nct-cute-smile-gif-14733904",
            "https://tenor.com/view/hendery-way-v-nct-cute-selfie-gif-14698268",
            "https://tenor.com/view/seulgicfm-hendery-gif-19467114",
            "https://tenor.com/view/hendery-wayv-nct-heart-gif-14723398",
            "https://tenor.com/view/hendery-wayv-nct-gif-19296592",
            "https://tenor.com/view/nct-hendery-turn-back-time-mv-way-v-hendery-nct-hendery-nct-hendery-turn-back-time-mv-gif-19674019",
            "https://tenor.com/view/nct-hendery-nct-hendery-turn-back-time-mv-way-v-hendery-gif-19674013",
            "https://tenor.com/view/hendery-wayv-hendery-crying-hendery-waaa-waaa-gif-19336487",
            "https://tenor.com/view/wayv-nct-hendery-wong-kunhang-handsome-gif-16028470",
            "https://giphy.com/gifs/nctsmtown-nct-nct127-127-3ddsPMDOgK7PY6p0qS",
            "https://c.tenor.com/kBpvrb_2gvYAAAAM/wayv-nct.gif",
            "https://64.media.tumblr.com/9ecc24975a49baa39321de0dfe669c59/tumblr_pqkafdNpyC1v3d1zko1_r1_400.gif",
            "https://64.media.tumblr.com/ee953e1357807675051fbf64c7665191/b405d2720e8396a2-35/s540x810/d15e0b5c754cfa4d58c6fc434988dbbe48132489.gif",
            "https://64.media.tumblr.com/8641ac782d2c128e16ccec5ff06d8493/b405d2720e8396a2-e8/s540x810/9b4cac0c4f1c9f91a52f70f4ea3c20142cff9c57.gif",
            "https://64.media.tumblr.com/dc92521c1608c864a10da4c63885cfbf/20600febbde8c4c1-cb/s400x600/05025af59351a839b9c1ea58245f994be5244e42.gif",
            "https://64.media.tumblr.com/f514d084249bdc6c85d09a2c8a2967fb/20600febbde8c4c1-e9/s400x600/e727aa812de9cb68386f3fd9aa68bad530d15963.gif",
            "https://64.media.tumblr.com/c4a7eae812107ea834cd0cd1305c9055/20600febbde8c4c1-01/s400x600/5ac708bdf231b9ca4400a41ac3d8d8f708156a24.gif",
            "https://64.media.tumblr.com/9025e4795447286e48eff37e64b94008/20600febbde8c4c1-22/s400x600/fb1a51bd5f340354463469afb14193b593b9b433.gif",
            "https://64.media.tumblr.com/22d319975ec89e6fbfc6db1715c6e40d/3ad11140a1b68acf-87/s250x400/48ff3b9c33255e74337e80767bf2191a3ac06743.gif",
            "https://64.media.tumblr.com/9e1cbb182693c3c72efbfdf030bf39b1/3299fb3e00f24532-26/s250x400/674cc41d68e6b39a622d3d0ae9c4e16c3bfbcc96.gif",
            "https://64.media.tumblr.com/6598861f04d48ba2f4cba24fb3a0465f/3299fb3e00f24532-8e/s250x400/48f31991264ea9343cf3a906a71f9a65d736bb56.gif",
            "https://64.media.tumblr.com/ddd1e0845b8a672bb91266eee689cfc3/3299fb3e00f24532-d8/s250x400/76f14eff9e01fb230010bea65431902ce68846b0.gif",
            "https://64.media.tumblr.com/58f3dfd7dca59d9bc1d3f1e9f5952110/3299fb3e00f24532-d9/s250x400/0514641f74c3cb67b60eadab2671ff8f3ee4a800.gif",
            "https://64.media.tumblr.com/cc372d4f6baf0fc4d3dcfea4302e34be/3832f232f2b705b6-a0/s400x600/f6122822278877cef50839a3cba8445414bbf3cf.gif",
            "https://64.media.tumblr.com/4e5f879fe73217d3400725e6d38eb92e/a580af8e2c2029f2-0a/s400x600/98399eb650b6c94e4fe8b5a7e73f227bcacf0795.gif",
            "https://64.media.tumblr.com/fe879e36a7c6bc8fad1efdfa0bfcb99f/a5da3aee62cc7738-51/s250x400/af354b6480b4d5e1f617683b76ec77ea8cc7af39.gif",
            "https://64.media.tumblr.com/1d010dbd9756fbf62431e906bda05f58/ea0352b5ba837d08-7b/s400x600/9239e3739e9393bf2dfda3f3d49482ca990fee00.gif",
            "https://64.media.tumblr.com/8e61124f3a79d62e46272a7788ccc9c7/c7e5a1669a0843f4-9d/s400x600/66e5ec797e2c538d9bb34c6695173f79ae08e26f.gif",
            "https://64.media.tumblr.com/a6fd2d89b472606812dc4cef638c3f04/c7e5a1669a0843f4-4b/s400x600/86f4507578d6a5bfddafe9307c2a76540fc48baf.gif",
            "https://64.media.tumblr.com/31bdf501a9a18c14122992e9e4c5714a/c7e5a1669a0843f4-94/s400x600/378c963e9bce7bfaca5871cb8c2a284431ce8a07.gif",
            "https://64.media.tumblr.com/0b40937beb987bbf55633d7820b82db2/ecf9918c08f1f15c-bd/s250x400/2af2d1e68d4308557aba5dbd41e362eec530e74f.gif",
            "https://64.media.tumblr.com/debe019340b3da7ec0275a7ddfbca691/ecf9918c08f1f15c-e1/s250x400/067977076eca4a16fa6b35817030df61f2dc7347.gif",
            "https://64.media.tumblr.com/42289de9a3ff62edbb84ec8fb1c7215a/140e02c93672e4df-15/s400x600/948381186791bded03ffa54a2fc3adc4050b6989.gif",
            "https://64.media.tumblr.com/33065a0d7c73d3c2c852f7bd05e62de1/415189a35178aa60-c0/s400x600/36d62fb86a68a8124df5db27021f022d425d6127.gif",
            "https://64.media.tumblr.com/6c56b218bc280923e4ecad8886969b84/415189a35178aa60-cd/s400x600/c21ce64c2bfe65ccb8b2ea6eb011fcce64f8163d.gif",
            "https://64.media.tumblr.com/d1a51e80e5cede2352ba15243ae529a4/4105f6a24c700139-f4/s250x400/2696a6265005991e2e33ab6ff5dffb7fd27d3d56.gif",
            "https://64.media.tumblr.com/8bcf71cb6c5e7af9e439ef1d55340f5c/4105f6a24c700139-dd/s250x400/3a74f5ba6ea992d0313c174983e9bcb94b102b7e.gif",
            "https://64.media.tumblr.com/161012067a9ca25797468c5b6d17e6d6/35d9a9c927b23e52-d1/s250x400/f1465f9bb7be7bf86ac01f653087c5c868bf5ef7.gif",
            "https://64.media.tumblr.com/319e5da85737c4cb04618f1b9d7520b2/61d0fca0e3f50e07-1f/s400x600/5c9d26b7b691ccaf253daf1fa8dbb3ca9ccd2625.gif",
            "https://64.media.tumblr.com/cb0328e76a9f5a3b9c76b93a6a676ab1/61d0fca0e3f50e07-2b/s400x600/59742af84d53a394cc04b850cedb3fc1f0353b50.gif",
            "https://64.media.tumblr.com/ee1a779f41e405c1e2d7259dc569a915/61d0fca0e3f50e07-8b/s400x600/ec6040916ea87dcd976b889378dc0a0718231c62.gif"]

        self.bot.nct_yangyang_gif = ["https://tenor.com/view/yangyang-wayv-ariel-liu-yangyang-gif-18990980",
            "https://tenor.com/view/wayv-nct-liu-yangyang-yangyang-handsome-gif-16282245",
            "https://tenor.com/view/yangyang-wayv-nct-baby-yangyang-dancing-yangyang-gif-19030426",
            "https://tenor.com/view/nct-yangyang-yangyang-nct-nct90s-love-90s-love-gif-19660010",
            "https://tenor.com/view/yangyang-wayv-nct-baby-yangyang-dancing-yangyang-gif-19030435",
            "https://tenor.com/view/yangyang-kpop-look-stare-gif-15250491",
            "https://tenor.com/view/wayv-nct-liu-yangyang-yangyang-handsome-gif-15963232",
            "https://tenor.com/view/wayv-yangyang-yangers-wayv-princess-nct-gif-19170089",
            "https://tenor.com/view/way-v-yangyang-yangyang-nct-yangyang-way-v-nct-gif-19660042",
            "https://tenor.com/view/neojno-yangyang-gif-19720511",
            "https://tenor.com/view/wayv-yangyang-kpop-boyfriend-gif-14757910",
            "https://tenor.com/view/yangyang-gif-18194871",
            "https://tenor.com/view/wayv-nct-liu-yangyang-yangyang-handsome-gif-16282250",
            "https://giphy.com/gifs/nctsmtown-nct-nct127-127-GjowzkCLLZxhkuvF6F",
            "https://giphy.com/gifs/nctsmtown-nct-nct127-127-i1HeG0kGBCRCGFPVfq",
            "https://64.media.tumblr.com/a1e0e6a39ed3ce8be3f1fb154f836b5a/46c7c760d7530937-28/s540x810/723843e665d3ca285fccbefe27469c50b675ce14.gif",
            "https://64.media.tumblr.com/28f5019ea40187e8dca6304d93c8afa1/46c7c760d7530937-1d/s540x810/1cde7a05ab978f2206c015d833cc356405295427.gif",
            "https://64.media.tumblr.com/235f5d2a11f491e26dcd777aebbfe641/edea37bc56b39b21-89/s400x600/245b4d02427108d12f8793598d3de18820386de8.gif",
            "https://64.media.tumblr.com/96f5d812a94f49566a36af42fcb90e92/edea37bc56b39b21-71/s400x600/25a6cedc3031f2495ba288ee1c3f2fa9baebe84d.gif",
            "https://64.media.tumblr.com/a7518189f48350fe32290c868e0a744f/140e02c93672e4df-ad/s400x600/4a4008176468be1d949590920e5dd6f18dcc3fd4.gif",
            "https://64.media.tumblr.com/1490d517b01173c226cb25bf7d5ed95d/ea0352b5ba837d08-21/s400x600/880aebf1881afbc13d00957f2869a371854d7c0a.gif"]

        self.bot.nct_taeyong_gif = ["https://tenor.com/view/nct-taeyong-cute-gif-15119070",
            "https://tenor.com/view/nct-vocalist-visual-sm-entertainment-nct-subunit-gif-17505770",
            "https://tenor.com/view/nct-taeyong-sunscreen-nature-republic-gif-16980421",
            "https://tenor.com/view/nctu-nct-nct127-nctdream-taeyong-gif-9647830",
            "https://tenor.com/view/nct127-nct-kpop-ccg-shock-gif-16007114",
            "https://tenor.com/view/taeyong-nct-smiling-cute-gif-14544492",
            "https://tenor.com/view/taeyong-nct-nct127-nct-u-regular-gif-13569029",
            "https://cdn.discordapp.com/attachments/793028403463716875/804433955771645962/image0.gif",
            "https://cdn.discordapp.com/attachments/793028403463716875/804433956224106587/image1.gif",
            "https://cdn.discordapp.com/attachments/793028403463716875/804434007336026112/image0.gif",
            "https://gfycat.com/actualaccurateayeaye",
            "https://gfycat.com/likelydifficultgallinule",
            "https://gfycat.com/equatorialadmirablegalapagospenguin-nct-2018-jaehyun-jungwoo-taeyong-chenle",
            "https://gfycat.com/misguidedimaginaryangelfish",
            "https://gfycat.com/dismalpastdinosaur",
            "https://gfycat.com/honestpleasantglobefish",
            "https://gfycat.com/joyfulorangekiskadee-beauty",
            "https://gfycat.com/pleasantchiefguineafowl",
            "https://gfycat.com/spiffypeacefulalleycat",
            "https://gfycat.com/mixedhollowjaeger",
            "https://gfycat.com/altruisticpitifulcanary",
            "https://gfycat.com/demandingidleaustralianshelduck",
            "https://gfycat.com/zealoussanecaimanlizard-taeyong-kpop-nct",
            "https://gfycat.com/immateriallargekitty-lee-taeyong-sm-rookies-sr15b",
            "https://gfycat.com/softconfusedafricanjacana-lee-taeyong-sm-rookies-sr15b",
            "https://gfycat.com/basicfragrantanglerfish-longflight-smstation-nct-127-taeyong",
            "https://gfycat.com/flippantimpartialbrontosaurus",
            "https://gfycat.com/ornategentlegalapagosmockingbird",
            "https://gfycat.com/tarthatefulhatchetfish",
            "https://gfycat.com/legalimmaterialaddax-nct-taeyong-long-flight-sm-station",
            "https://gfycat.com/relieveddensecomet",
            "https://gfycat.com/impressivewideeyedcopperbutterfly-highwaytoheavenenglish-wearesuperhuman-taeyong",
            "https://i.pinimg.com/originals/7b/c2/4b/7bc24bc7ff88fcec939303cf529ce06a.gif",
            "https://v-phinf.pstatic.net/20201106_234/16046706748106uLnj_GIF/be1603d6daff167df8805df8f95d3f7e.gif?type=w1000",
            "https://i.pinimg.com/originals/b3/1c/7b/b31c7bda897bf5725e8736c57d05cb00.gif",
            "https://data.whicdn.com/images/307974399/original.gif",
            "https://i.pinimg.com/originals/fe/83/36/fe8336d5818f5fcdfe2d72e8b6f4691f.gif",
            "https://i.pinimg.com/originals/0d/13/48/0d1348d480ba10564048375efcaa3112.gif",
            "https://64.media.tumblr.com/16e09ae681e7ef77c54fd8a6b8cd9473/tumblr_oxwhsdraHf1wwki56o1_400.gif",
            "https://i.pinimg.com/originals/fe/14/36/fe14369aca437ea087221f3954f6d52b.gif",
            "https://media4.giphy.com/media/Wn0zbBAfNFkpxOa0OI/giphy.gif",
            "https://i.pinimg.com/originals/0f/2a/db/0f2adb19835bb7eabedf4ad81629105e.gif",
            "https://i.pinimg.com/originals/b2/87/0f/b2870f55d9c353f26969c41a2315a731.gif",
            "https://tenor.com/view/taeyong-lee-tae-yong-kpop-nct127-super-m-gif-17380108",
            "https://tenor.com/view/lee-taeyong-nct-127-stare-gif-14733836",
            "https://tenor.com/view/taeyong-nct-nct127-taeyong-malfunctioning-taeyong-meme-gif-14896845",
            "https://tenor.com/view/nct127-nct-taeyong-cute-jungwoo-gif-13770501",
            "https://tenor.com/view/lee-taeyong-kpop-nct-127-gif-19252838",
            "https://giphy.com/gifs/nctsmtown-nct-127-highway-to-heaven-h4m53w0m76xr02JLTc",
            "https://giphy.com/gifs/nctsmtown-nct-127-highway-to-heaven-gK55PS79z1wZHsi2If",
            "https://giphy.com/gifs/nctsmtown-nct-127-highway-to-heaven-l31GcDieIb32DCRUmH",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-IevcMUEq3knMKUKGjC",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-f9qKqtCFuJCSjJ9B42",
            "https://giphy.com/gifs/nctsmtown-nct-nct127-127-pKKlTxmKO9QKPzD3zw",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-hpSZlN0nFzILgPbp61",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-ATmBrSXPpXbBaN9ngv"]

        self.bot.nct_jungwoo_gif = ["https://tenor.com/view/nct-nct127-jungwoo-kim-jungwoo-jin-ting-you-gif-16941098",
            "https://tenor.com/view/neo-culture-technology-nct-nctzen-jungwoo-park-jungwoo-gif-12100520",
            "https://tenor.com/view/nct-nct127-ccg-kpop-jungwoo-gif-14886529",
            "https://tenor.com/view/jungwoo-nct-heart-kim-jungwoo-gif-12623235",
            "https://tenor.com/view/kimkiyomi-jung-woo-nct-kim-uw-u-kpop-cute-gif-16580967",
            "https://tenor.com/view/nct-nct127-dowoo-doyoung-kim-dong-young-gif-17674638",
            "https://tenor.com/view/jungwoo-nct-pose-gif-14378541",
            "https://tenor.com/view/jungwoo-nct-nct127-heart-kpop-gif-16653764",
            "https://tenor.com/view/nct-nct127-dowoo-doyoung-kim-dong-young-gif-17674610",
            "https://tenor.com/view/jungwoo-kim-jungwoo-jungwoo-nct-kim-jungwoo-nct-jungwoo-nct127-gif-19560238",
            "https://tenor.com/view/jungwoo-kim-jungwoo-jungwoo-nct-kim-jungwoo-nct-jungwoo-nct127-gif-19560255",
            "https://tenor.com/view/jungwoo-kim-jungwoo-jungwoo-nct-kim-jungwoo-nct-jungwoo-nct127-gif-19560263",
            "https://tenor.com/view/kim-jungwoo-nct-nct127-cute-adorable-gif-14675058",
            "https://tenor.com/view/jungwoo-kim-jungwoo-jeongwoo-nct-nct-u-gif-14244195",
            "https://tenor.com/view/jungwoo-kim-gif-18917951",
            "https://tenor.com/view/jungwoo-kim-gif-18917950",
            "https://tenor.com/view/nct-nct127-dowoo-doyoung-kim-dong-young-gif-17674592",
            "https://tenor.com/view/jungwoo-nct-heart-kim-jungwoo-gif-12623235",
            "https://tenor.com/view/jungwoo-nct-nct127-kim-jungwoo-jungwoo-nct-gif-19560127",
            "https://tenor.com/view/jungwoo-kim-jungwoo-jungwoo-nct-kim-jungwoo-nct-jungwoo-nct127-gif-19560268",
            "https://tenor.com/view/jungwoo-nct-gif-18755383",
            "https://giphy.com/gifs/nctsmtown-nct-127-u-f38r3qkFFzG9cXNSml",
            "https://giphy.com/gifs/nctsmtown-nct-127-u-f38r3qkFFzG9cXNSml",
            "https://tenor.com/view/nct127-nct-taeyong-cute-jungwoo-gif-13770501",
            "https://giphy.com/gifs/nctsmtown-nct-127-highway-to-heaven-UoYD0qxOlzCX94gBb9",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-KfqKwHSEP5ZmokrmYp",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-jn1TRkYIshuxOd4hcn",
            "https://giphy.com/gifs/nctsmtown-nct-127-u-kEp104oGLhMB7rawA3",
            "https://giphy.com/gifs/nctsmtown-nct-127-u-hz5fsO2337Z6SwBEcD"]

        self.bot.nct_yuta_gif = ["https://tenor.com/view/yuta-nakamoto-smile-cute-japanese-singer-gif-15773495",
            "https://tenor.com/view/nct-gif-18066481",
            "https://tenor.com/view/nct-yuta-k-pop-dance-gif-9451979",
            "https://tenor.com/view/nct-yuta-winwin-love-yuwin-gif-11839935",
            "https://tenor.com/view/nct-yuta-yuta-nakamoto-smile-kpop-gif-14019680",
            "https://tenor.com/view/cute-smile-yuta-taeil-nct-gif-13475851",
            "https://tenor.com/view/yuta-nakamotonct-nct127-cute-smile-gif-14733835",
            "https://tenor.com/view/nct-nct127-yuta-nakamoto-yuta-sub-vocals-gif-17637557",
            "https://tenor.com/view/nct-nct127-yuta-nakamoto-yuta-sub-vocals-gif-17661500",
            "https://tenor.com/view/yuta-nct-nakamoto-nct127-gif-18999821",
            "https://tenor.com/view/yuta-nakamotonct-nct127-cute-kiss-wink-gif-14733839",
            "https://tenor.com/view/yuta-nct-nct127-yuta-nakamoto-kpop-gif-17155668",
            "https://tenor.com/view/nakamotoyuta-nct-yuta-yutagif-nct127-gif-19160084",
            "https://tenor.com/view/really-yuta-nakamoto-nct-gif-12788521",
            "https://tenor.com/view/yuta-yuta-nct-yuta-sexy-yuta-nakamoto-nct-sexy-yuta-nct-gif-20324650",
            "https://giphy.com/gifs/nctsmtown-nct-127-u-MGu1EmjOquub9cgwuU",
            "https://giphy.com/gifs/nctsmtown-nct-127-u-PWiQLOzatuyj70H3gu",
            "https://tenor.com/view/nct-nct127-yuta-nakamoto-yuta-sub-vocals-gif-17251770",
            "https://tenor.com/view/yuta-nakamotonct-nct127-cute-kiss-wink-gif-14733839",
            "https://tenor.com/view/nct-nct127-yuta-nakamoto-yuta-sub-vocals-gif-17637557",
            "https://giphy.com/gifs/nctsmtown-nct-127-highway-to-heaven-RlI2wIV2Yo6vW54rci",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-cIEXH1rEagHtQ9LWsT",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-lSgkIQH7fnueclfEwQ",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-vE9s1D7gnQ6h2K4vfW"]

        self.bot.nct_jeno_gif = ["https://tenor.com/view/jeno-nct-dream-sexy-dance-gif-12526719",
            "https://tenor.com/view/jeno-jeno-seolie-nct-jeno-nct-dream-gif-12958231",
            "https://tenor.com/view/nct-dream-jeno-surprised-cute-kpop-gif-16310898",
            "https://tenor.com/view/nctdream-nct-jeno-lee-nctjeno-hi-gif-14687660",
            "https://tenor.com/view/nct-dream-we-young-renjun-jeno-hearts-gif-15871557",
            "https://tenor.com/view/nctjeno-nct-mark-lee-jeno-gif-12958199",
            "https://tenor.com/view/jeno-nct-jeno-nct-dream-gif-12958228",
            "https://tenor.com/view/jeno-lee-jeno-jeno-abs-nct-abs-nct-jeno-abs-gif-19209629",
            "https://tenor.com/view/jeno-nct-dream-jeno-nct-jeno-nct-looks-around-gif-18121824",
            "https://tenor.com/view/jeno-nct-jeno-idea-thought-thinking-gif-18121777",
            "https://tenor.com/view/jeno-nct-nct-dream-jeno-seolie-jeno-nct-gif-12958239",
            "https://tenor.com/view/jeno-lee-jeno-nct-nct-dream-hot-gif-16643500",
            "https://tenor.com/view/nct-dream-jeno-nct-jeno-gif-19863273",
            "https://tenor.com/view/jeno-lee-nct-dream-winking-gif-19521202",
            "https://tenor.com/view/please-use-your-mind-jeno-nct-lee-jeno-use-your-brain-gif-16359219",
            "https://tenor.com/view/nct-dream-lee-jeno-kpop-gif-19250920",
            "https://gfycat.com/soggywaterydrafthorse",
            "https://gfycat.com/possibleashamedbug",
            "https://gfycat.com/fatalfondcarpenterant-beauty",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-kllnNQHdVLxKt79Dfa",
            "https://giphy.com/gifs/nctsmtown-nct-nct127-127-pvwjLhnPLkJq5KKn2J",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-60jwOwLAcSMSimfMGF",
            "https://giphy.com/gifs/kpop-k-pop-k-pop-3ohuPaXsHAHYykmWKA",
            "https://giphy.com/gifs/nct-hsmszp0kOVnhgCyqFU",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-172-AwY4PUEguW8iNVO3CX"]

        self.bot.nct_jisung_gif = ["https://tenor.com/view/nct-jisung-park-jisung-kpop-handsome-gif-15640963",
            "https://tenor.com/view/nct-jisung-park-jisung-kpop-handsome-gif-15641120",
            "https://tenor.com/view/jisung-nct-dream-park-jisung-kpop-cute-gif-17373930",
            "https://tenor.com/view/sm-entertainment-nct-subunit-kpop-handsome-cute-gif-17503874",
            "https://tenor.com/view/nct-kpop-ccg-park-jisung-nct-dream-gif-14800373",
            "https://tenor.com/view/nct-jisung-nct-jisung-jisung-nct-liyonqi-gif-19532744",
            "https://tenor.com/view/nct-kpop-jisung-park-jisung-heart-gif-14675163",
            "https://tenor.com/view/park-jisung-jisung-nct-ccg-nct-dream-gif-14769375",
            "https://tenor.com/view/finger-heart-gif-18034442",
            "https://tenor.com/view/jisung-119zs-nct-dream-kpop-nct-gif-18891097",
            "https://tenor.com/view/nct-dream-jisung-kpop-korean-gif-9994549",
            "https://tenor.com/view/park-ji-sung-nct-nctdream-nctjisung-adorable-gif-16921855",
            "https://tenor.com/view/jisung-nct-go-park-jisung-cute-af-gif-13149929",
            "https://tenor.com/view/kpop-nct-jisung-gif-11399818",
            "https://tenor.com/view/jisung-park-jisung-dream-nct-dream-cutie-gif-16426945",
            "https://tenor.com/view/nct-kpop-ccg-cute-nct-dream-gif-14846159",
            "https://tenor.com/view/nct-nct-dream-jisung-park-ji-sung-main-dancer-gif-16812214",
            "https://tenor.com/view/nct-dream-jisung-stop-wait-pause-gif-15216558",
            "https://tenor.com/view/nct-nctdream-parkjisung-jisung-gif-19646404",
            "https://giphy.com/gifs/nctsmtown-nct-127-u-NiElXN3pnQxUip98B8",
            "https://giphy.com/gifs/nctsmtown-nct-127-u-zm8Rb23qSxfbIEfu8E",
            "https://giphy.com/gifs/nctsmtown-nct-127-u-Cobs8ZH3yAGTwVHS0h"]

        self.bot.nct_renjun_gif = ["https://tenor.com/view/finger-bite-cute-kpop-renjun-nct-dream-gif-16895396",
            "https://tenor.com/view/renjun-renjun-cute-renjun-nom-nom-renjun-bungeoppang-gif-19626068",
            "https://tenor.com/view/renjun-nct-dream-nct-renjun-laughs-laughs-gif-19662361",
            "https://tenor.com/view/%EB%9F%B0%EC%A5%94-renjun-huang-renjun-ruddygif-renjun-pretty-gif-19648935",
            "https://tenor.com/view/renjun-cat-renjun-kity-what-gif-19127612",
            "https://tenor.com/view/nct-renjun-gif-17980630",
            "https://tenor.com/view/renjun-renjun-cry-renjun-actor-renjunkr-gif-19573528",
            "https://tenor.com/view/renjun-nct-rensung-renjun-eyes-renjun-funny-gif-19637468",
            "https://tenor.com/view/nct-dream-renjun-huang-ren-jun-kpop-cute-gif-16529193",
            "https://tenor.com/view/renjun-nct-dream-nct-renjun-fake-crying-renjun-fake-cry-gif-19734101",
            "https://tenor.com/view/renjundancer-renjun-nctdream-renjunzer-gif-19664456",
            "https://tenor.com/view/nct-dream-renjun-pissed-done-gif-15674115",
            "https://tenor.com/view/tipton2109-nct-nct-dream-nct-renjun-renjun-gif-13172220",
            "https://tenor.com/view/renjun-renjun-heart-renjun-oyf-cute-love-gif-16458926",
            "https://tenor.com/view/renjun-huang-nctrenjun-renjunnct-nctdream-gif-14733838",
            "https://tenor.com/view/renjun-nct-dream-confused-what-huang-renjun-gif-16915794",
            "https://tenor.com/view/kpop-nct-nct-dream-hwang-injun-huang-renjun-gif-14541458",
            "https://tenor.com/view/nct-nct-dream-renjun-huang-ren-jun-hwang-in-joon-gif-17167756",
            "https://cdn.discordapp.com/attachments/772975408912007180/790097322155180043/image0.gif",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-1Ty9e67rQp8aB1l9oJ",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-7y8gFfTLNbBjtxkHgg",
            "https://64.media.tumblr.com/f4e1f9413df13112e193bc467baedd02/1b91aaec34336370-e9/s400x600/7f9c7777505523ed210be2365175b98288ed8a33.gif"]

        self.bot.nct_doyoung_gif = ["https://i.pinimg.com/originals/c3/3c/af/c33caff35228f8c25b79756bf3858490.gif",
            "https://data.whicdn.com/images/320339609/original.gif",
            "https://78.media.tumblr.com/35f8f28866bd985922db13eec3d3d2ab/tumblr_p8mek1s3a21sajt0bo1_400.gif",
            "https://data.whicdn.com/images/312017515/original.gif",
            "https://data.whicdn.com/images/321897209/original.gif",
            "https://78.media.tumblr.com/b6606fbac3059d16860b14baab69d204/tumblr_p566iwH9Tv1x7lc5jo3_400.gif",
            "https://pa1.narvii.com/6690/eb89dc13d6ffbdc52c2766001ff304496a1060e4_hq.gif",
            "https://media1.tenor.com/images/2d40483ad03f8648a591e3d4d716216b/tenor.gif?itemid=15749825",
            "https://64.media.tumblr.com/9b46169d562186c48dfa192edce186d4/7372b4a5ed630294-65/s540x810/62262631f234313d8c8ca221de00a5214db13b07.gif",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-h7jxJ4TtjzeIWXjjVF",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-sETpe4fZXpRL62foAm",
            "https://giphy.com/gifs/nctsmtown-nct-127-highway-to-heaven-gfIQsfME5I0LrEF93O",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-S5zUE2zUAkycLqP4Nh",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-dxCXXifRkjIM1ur925",
            "https://c.tenor.com/qYLYCx2IT3gAAAAM/nct-nct127.gif"]

        self.bot.nct_haechan_gif = ["https://data.whicdn.com/images/312017472/original.gif",
            "https://64.media.tumblr.com/20aa6e1fc21ad09a3c46a1bda021f92b/2e7c33e88cfa45b6-1a/s250x400/03e8c3e5dc265549348372c81e2326c91c0b56e7.gif",
            "https://64.media.tumblr.com/75ef7a734537d58e74904c48c9cb7017/tumblr_inline_pow2abTWdm1waucm1_500.gif",
            "https://p.favim.com/orig/2018/09/27/nct-127-nct-dream-regular-Favim.com-6379197.gif",
            "https://media1.tenor.com/images/b561fa662544b25f8627f3aa83738172/tenor.gif?itemid=17383374",
            "https://i.pinimg.com/originals/95/23/fe/9523fe8c6242656d6749518de57a1119.gif",
            "https://i.pinimg.com/originals/32/52/9c/32529ca296c7d6114a34e44dd4e8ef48.gif",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-bDuuUV0V4MeIxXBWQN",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-Gi655hgtqzknoCyN1k",
            "https://giphy.com/gifs/nctsmtown-nct-127-highway-to-heaven-Ln3YaITQqWZ2wVMn3Q",
            "https://giphy.com/gifs/nctsmtown-nct-127-highway-to-heaven-PmMWl4SOGZxqb19bac",
            "https://giphy.com/gifs/nctsmtown-nct-127-highway-to-heaven-ZYFDcJUqHxX4y4DOeU",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-MWqpmelIZT4xtmdagg",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-URpZM8FqlSxCLXn8oq",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-1Q09RkLGBlV4FKGbgx",
            "https://giphy.com/gifs/Fanfickk-nct-dream-haechan-Kd5q0RMlTj2nNfvvIt",
            "https://64.media.tumblr.com/ef5af9ada1b71a098a09889db3be535e/1b91aaec34336370-c1/s400x600/2856a1cd420106784fab301d24935a44d16a2189.gif"]

        self.bot.nct_shotaro_gif = ["https://data.whicdn.com/images/351628694/original.gif",
            "https://64.media.tumblr.com/6edafc4e3260369fc2985fba82b15445/28949b3c12da530c-06/s540x810/052ac6091eb548bd42872edc47493087d9effd66.gif",
            "https://i.pinimg.com/originals/98/15/81/9815815163d0c1e0e2684b8dbf0b350a.gif",
            "https://64.media.tumblr.com/ed525c8f42475f3a1cabc6d2415a20e1/16d2020971cda3d1-e0/s400x600/177a2c6c491972336440d4adc7c7e0e56bb7fb6b.gif",
            "https://i.pinimg.com/originals/ff/70/ec/ff70ec397a9742db8f3a3bb899c3b862.gif",
            "https://data.whicdn.com/images/351456132/original.gif",
            "https://lh3.googleusercontent.com/-oPCo2mOsMNA/X2odftlLkWI/AAAAAAABIHU/WGyRoYVSc4YaMtYEp06likNYkmlvjatxwCLcBGAsYHQ/s16000/download%2B%25281%2529.gif",
            "https://64.media.tumblr.com/479ed0fb7b0e877859761b7b4abb316e/e518acab0afea2ee-01/s250x400/1699ca4024158bdfc711a9d915558ece1c103393.gif",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-LIBd1nfU9PJJnEOdBT",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-C0LpuEm9SldsMhfrOp",
            "https://tenor.com/view/nct-shotaro-nct-shotaro-heart-cute-gif-18928804",
            "https://tenor.com/view/nct-nct-u-shotaro-nct-shotaro-cute-gif-18810709",
            "https://tenor.com/view/nct-nct-u-shotaro-kpop-gif-18893113",
            "https://tenor.com/view/shotaro-gif-20031841",
            "https://64.media.tumblr.com/b4f8d69d97cd627730ea00cffbfbb2ee/b39b7fda6a13a80d-5b/s400x600/208ef71030552742bb3fe965bddf6980ca671343.gif",
            "https://64.media.tumblr.com/c152905fe42336c15e226e048a64c93a/272620fd2499e588-fb/s250x400/3b4df1c38c99d112a92b94d35005d7372beac432.gif",
            "https://64.media.tumblr.com/c4fb2d344d11927f7e18dcdbf443a7b9/0dfd0b26813b092c-4a/s250x400/fc319de0b72d8a696b9f16db5ac7354e61584197.gif",
            "https://64.media.tumblr.com/6e35153d8efd4302fbd8c26c27ef8dab/0dfd0b26813b092c-7c/s250x400/49ba789ba9ac4834f7239ec8272594b6e513cf3b.gif",
            "https://64.media.tumblr.com/640b6232c0fff0436d1e1d52e2bb8320/0dfd0b26813b092c-c0/s250x400/daa68b713242fdc40a5c1c99978f1f26dc7d8954.gif",
            "https://64.media.tumblr.com/fefab935edf53f7df022e7d91fb11dcc/0dfd0b26813b092c-f8/s250x400/49c7c6b746fac9d05a8013dec649fca4a698b2cd.gif",
            "https://64.media.tumblr.com/a3b0f1e8334f91ee8f64f547dfa58e96/a33acb101f3f3903-55/s250x400/0d93fc1f967c68f4b80fab6b5e44637f7d63ff3f.gif",
            "https://64.media.tumblr.com/01a23c83de4e4907366978558aa89df1/a33acb101f3f3903-c6/s250x400/93239ac74a39bb19de3f57fb659d3ac7bdea90f5.gif",
            "https://64.media.tumblr.com/949d0c188a6adddbd148ee27cc626c9c/8055c2722388e012-2b/s250x400/f12a69a536de3e74003325d66fddf43d85fe87c0.gif",
            "https://64.media.tumblr.com/1e650fe4bd88af09a64e3328e70db3c4/b25daaa3617f4d9c-d7/s400x600/8264ae91ac0d875d48883a0e499e64ee97ae0f3d.gif",
            "https://64.media.tumblr.com/68026a69466284a8e095752360412536/17030700b5829f3f-84/s250x400/6403afed330a7d062cca7b020466539314827c77.gif",
            "https://64.media.tumblr.com/bd3a7cecddd9e9fe7e2a3b4cd2183e5c/653824dcc05ecc7f-10/s400x600/f8ea4c13bb05bcdb0e5108569b74062ed30d379d.gif",
            "https://64.media.tumblr.com/1620e38a78309fdd3eff2e2860ded802/653824dcc05ecc7f-4c/s400x600/33e4eafb7b72f4142fb1af63cebadbb1c96c6d55.gif",
            "https://64.media.tumblr.com/a25a8638b81b326c3ab9f9b356c8378c/653824dcc05ecc7f-f9/s400x600/35363b0bad60ae38087090de2458a99383d9faf3.gif",
            "https://64.media.tumblr.com/702318a5a5007f1feaa03cd710531fdb/653824dcc05ecc7f-df/s400x600/c2d03da2c162bc6ac7f1ffa5febef025ee8d0c40.gif",
            "https://64.media.tumblr.com/af1d769de97bd917ecc5e25a86a738fd/d99c01d9b708b5fc-88/s400x600/f0417ed1cd990b99a90bde84bc58c4b711dacdf8.gif",
            "https://64.media.tumblr.com/2e84810e5af05233c97c10c54d91c569/3bb6944b2b8123c2-4f/s250x400/f22c315e658fc0a9313475ad8bb0a124840eb113.gif"]

        self.bot.nct_taeil_gif = ["https://tenor.com/view/nct-1994-moon-tae-il-taeil-finger-heart-gif-14375657",
            "https://tenor.com/view/nct-1994-moon-tae-il-taeil-heart-gif-14375647",
            "https://tenor.com/view/taeil-moon-gif-18057151",
            "https://tenor.com/view/dazed-look-distracted-concentrate-stare-gif-16109314",
            "https://tenor.com/view/moon-taeil-nct127-cute-gif-14352845",
            "https://tenor.com/view/moon-taeil-nct127-hot-kpop-side-view-gif-14733906",
            "https://tenor.com/view/nct-nct127-kpop-seventeen-happy-gif-15879465",
            "https://tenor.com/view/nct-1994-moon-tae-il-taeil-gif-14375660",
            "https://i.pinimg.com/originals/a5/a6/4d/a5a64d5c3459e443c347509b39e4851a.gif",
            "https://i.pinimg.com/originals/28/43/b1/2843b10af9f42c153877c5cd1878b210.gif",
            "https://media1.tenor.com/images/e0c64433f133d81fa9e1422bd7d87c3a/tenor.gif?itemid=14266544",
            "https://64.media.tumblr.com/a2f303114f52e194c367f7b439cbf9fa/tumblr_p378oh3Jaz1x2ayioo1_500.gif",
            "https://media1.tenor.com/images/acdc3c5360386cba413bf3400f000b91/tenor.gif?itemid=14352845",
            "https://data.whicdn.com/images/321043162/original.gif",
            "https://tenor.com/view/polite-cat-polite-cat-taeil-taeil-nct-nct-taeil-gif-19929210",
            "https://tenor.com/view/taeil-moon-tae-taeil-nct-nct-taeil-cute-gif-14266551",
            "https://tenor.com/view/taeil-moon-gif-14186038",
            "https://tenor.com/view/nct-kpop-nct127-ccg-taeil-gif-15853148",
            "https://tenor.com/view/nct-kpop-ccg-taeil-moon-taeil-gif-14839368",
            "https://tenor.com/view/nct-nct-u-nct127-nct2018-nct-dream-gif-12061716",
            "https://tenor.com/view/nct-1994-moon-tae-il-taeil-pose-gif-14375653",
            "https://giphy.com/gifs/nctsmtown-nct-127-highway-to-heaven-eJuLKhM5Oi1PCOwQRo",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-SVkXSzL6INpop2mNWx",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-H7f1WyUAYUEkB32rqr",
            "https://tenor.com/view/nct-taeil-belle-gif-14901073",
            "https://64.media.tumblr.com/a4c8fdf6d2887689f20dd5995853b3a5/a8c97127a1ff7be1-c8/s400x600/dcf176dc23c23bebb57285ee2b59aa0e55b3171c.gif",
            "https://64.media.tumblr.com/00b501b79a136a6016ee85756a1f116e/a8c97127a1ff7be1-9d/s400x600/12e3d08b523d8402c4dee48061f6bff40af63562.gif",
            "https://64.media.tumblr.com/9a6ed88655079733c14616dbc036077c/a8c97127a1ff7be1-cf/s400x600/d71936b323b0872af2b0e95c4e20ef931f531ec4.gif",
            "https://64.media.tumblr.com/c29d3fc0057554b8166a3d2bdb794228/0b9bd379401e3ffc-69/s400x600/4cf53f3bbc6001ed2e268e1f21d753cc6f4629cd.gif",
            "https://64.media.tumblr.com/31642c735d1c769a554e7ff23444e79b/0b9bd379401e3ffc-5f/s400x600/97fb0a6793acc4ec6e6fe6ac564c5a3c883e6396.gif",
            "https://64.media.tumblr.com/4940b6afa760d74fab8ff44eee2cfdeb/0b9bd379401e3ffc-41/s400x600/5c7b521716ab163ded9f7461b6810d8494dadf94.gif",
            "https://64.media.tumblr.com/ff996283c01344b6238db8e8ed9bbea7/0b9bd379401e3ffc-08/s400x600/c22dca04b0f15f7c54634d01d07b4bede083203c.gif",
            "https://64.media.tumblr.com/73a8ceae18dced8da1144d3ec4fd573c/66e1a7cd001ddecf-77/s250x400/185e4dad1683e82c27280a005e185f812298cb47.gif",
            "https://64.media.tumblr.com/f50f424bbd9ab15937fd11e8ff1a7d73/66e1a7cd001ddecf-1b/s250x400/8f906be3a90872e3f316226dbe6dbe0be8b03ffa.gif",
            "https://64.media.tumblr.com/21136d5f1ab30a7ca6ab93189cd876b6/286ea5d7c7157ee5-5a/s400x600/48a35b5b13f865204e08546fd3d2a1776dafd0b8.gif",
            "https://64.media.tumblr.com/bee0165d85bc1d6c0f68524233def2fc/286ea5d7c7157ee5-cb/s400x600/629cf93785a64cdf39e7689b8bc4cb47925d0b6a.gif",
            "https://64.media.tumblr.com/6af91ead9c7ea58489c1378ff4c04cd9/286ea5d7c7157ee5-ec/s400x600/5db79ff49eac5a396ac635f8328c627b42c85c70.gif",
            "https://64.media.tumblr.com/bee0114a5bc38a2ae5f702376d51cec5/286ea5d7c7157ee5-81/s400x600/9bf8bc4479ae6f509acfb51204856aa4d6dc2624.gif",
            "https://64.media.tumblr.com/03aa31324e902a46a158377bea9037a2/9279b702df64c486-5d/s400x600/406d55d9dc1f28797a4ebe16f47709885792f865.gif",
            "https://64.media.tumblr.com/6a2dbbd8a708f38ee9c0662895d449cd/92a4d133c06ecc38-de/s250x400/7f1a40ee81b7cee4a2ea74e4a3437f7601a6ad31.gif",
            "https://64.media.tumblr.com/e3a77761d2e63a0149723774e04e726a/92a4d133c06ecc38-44/s250x400/82cd363785a0efd5f4547ff924d6bb1374928195.gif",
            "https://64.media.tumblr.com/421936022e5b239cff87529062c504fb/2d696f968dae6aa4-ce/s250x400/3396ee82ee30b717b003b11d231bad0bc100c6b2.gif",
            "https://64.media.tumblr.com/60292da6fe804fa0e01a566e51eaa900/2d696f968dae6aa4-e6/s250x400/e5a6a46555e5c80268e3e9066ec2bd21e8102580.gif",
            "https://64.media.tumblr.com/9162bdeae57f6772da2b80d6846fafde/2d696f968dae6aa4-05/s250x400/52169381de27eacba3e5698501bf6681ad3de11b.gif",
            "https://64.media.tumblr.com/29005f3d7f1ae15c55905d9e5028907c/2d696f968dae6aa4-ff/s250x400/eb05253ca6318ea94072a189e6ad9be06a28e8cc.gif",
            "https://64.media.tumblr.com/26c40c5a18080d6fa98b8462c8acb28f/aac4ce26c58aa892-53/s400x600/66ec48b22de04050c005bb6baa650f1a498906e9.gif",
            "https://64.media.tumblr.com/477e0b04eb6e99b0fe24e0df4f287e59/aac4ce26c58aa892-84/s400x600/1a166bad269e522cc37cf1ee493c782ea22a3504.gif",
            "https://64.media.tumblr.com/2f35eb3e5a7e3e917177e30b02bade8b/aac4ce26c58aa892-04/s400x600/68af10fd6b69cebca68a32b1a023ffb0687b6af9.gif",
            "https://64.media.tumblr.com/ec4d2124a9ffe84ec3b8ab177b07b90e/eb65fdddfbf1801f-51/s400x600/2782d2be68cedb0af431cfd253b6111a6adfec03.gif",
            "https://64.media.tumblr.com/f4922c4f0d9d028a8ab5cacdbc0186fe/eb65fdddfbf1801f-05/s400x600/751e363c18ccec0f4382d86fb83696a2ac292520.gif",
            "https://64.media.tumblr.com/2051d180f3b8bda6b70d5dbc45a70560/3890681902d6cfaf-4d/s400x600/6b15e2c703c003517052fbc4da09d33ddd0fd39d.gif",
            "https://64.media.tumblr.com/60e56a30d4b72d76eeaf1944e20c8869/3890681902d6cfaf-dd/s400x600/e66e3dcebb02c5a4f98fb19e6e0eb495b717bf72.gif",
            "https://64.media.tumblr.com/2dc8d85743f0f38977e69d7a8ebffb2b/999fcd18b9604f7c-57/s400x600/d1736cd2522762601120383036458f18878e30e2.gif",
            "https://64.media.tumblr.com/1aaa89c4d02f04c37765e94adf0ae13f/f8716ca9e730c971-0d/s400x600/d217c836f544b027a6edea99e3ee3e74bb2e5253.gif",
            "https://64.media.tumblr.com/af27f9e8c2097f0a5305de9d335384cd/dca8b785757a4251-c9/s400x600/d7b202c8f0810e6ebd77a00c136be16022026298.gif"]

        self.bot.nct_johnny_gif = ["https://tenor.com/view/nct-nct127-johnny-seo-young-ho-john-suh-gif-17600646",
            "https://tenor.com/view/nct-kpop-ccg-nct127-johnny-suh-gif-14838201",
            "https://tenor.com/view/johnny-suh-nct-nctu-nct127-gif-19397616",
            "https://tenor.com/view/sip-tea-sips-tea-sipping-tea-tea-not-my-problem-gif-17953668",
            "https://tenor.com/view/johnnysuh-johnny-nct-127-johnnyseo-gif-14185990",
            "https://tenor.com/view/johnny-suh-johnny-johnny-nct-jyani-youngho-gif-19646436",
            "https://tenor.com/view/nct-kpop-ccg-idk-i-dont-know-gif-14838261",
            "https://tenor.com/view/nct-nct127-johnny-seo-young-ho-john-suh-gif-17056834",
            "https://i.pinimg.com/originals/24/a3/01/24a301425ef0e90dc3a8e931cd03e3d2.gif",
            "https://data.whicdn.com/images/322395528/original.gif",
            "https://64.media.tumblr.com/5c0689090b84b707ba20c4f85f284b32/tumblr_ph3o825jBP1rd83cko1_400.gif",
            "https://pa1.narvii.com/6937/6ea104d5dd53d6a4c71813c7bfa1825245e3c08dr1-600-338_hq.gif",
            "https://64.media.tumblr.com/6eee8c2756fedd75ce6d68592d2b05b7/c8f61988c4ad0f55-da/s400x600/0921a5511cc10017712be76e79d66ebb00670894.gif",
            "https://64.media.tumblr.com/0ab4a42f47acf64423b50eb86ee66a91/tumblr_op2tt55N8w1vtzx3lo1_500.gif",
            "https://static.tumblr.com/de7420edecd565e32132d0fa012d472d/sfqrjnj/8cpop35eg/tumblr_static_tumblr_static_2aa3z9eusisk0wo84s8gosgs4_focused_v3.gif",
            "https://64.media.tumblr.com/4a31dc164ae626c8c6ddb59d6f2829da/7bcbfe36332b251a-bd/s400x600/89a256dd13ca49430ffbb26e4fd1730b3d648c18.gif",
            "https://i.pinimg.com/originals/42/b7/5f/42b75f1ed6c341e99191ce5679e73274.gif",
            "https://i1.daumcdn.net/thumb/R600x0/?fname=https://blog.kakaocdn.net/dn/bfHPCi/btqEh7GyMO0/6Z8uS2sFQMfVBNkYHgkQk0/img.gif",
            "https://data.whicdn.com/images/347268939/original.gif",
            "https://i.pinimg.com/originals/1f/d9/f8/1fd9f8b2df93d123b71163f378d1283f.gif",
            "https://i.pinimg.com/originals/83/53/c8/8353c8c9c8aba0ee8f99b4691d04e889.gif",
            "https://gfycat.com/bigexhaustedfishingcat-doyoung-haechan-jaehyun-jungwoo-taeyong",
            "https://tenor.com/view/winwincel-nct-johnny-gif-19370943",
            "https://tenor.com/view/nct-nct127-johnny-seo-young-ho-john-suh-gif-17745163",
            "https://tenor.com/view/nct127-johnny-johnny-suh-kick-it-kpop-gif-17169184",
            "https://tenor.com/view/johnny-nct-pose-kpop-gif-14603420",
            "https://tenor.com/view/johnny-nct127-johnny-seo-johnny-suh-smile-gif-14397094",
            "https://tenor.com/view/nct127-johnny-suh-johnny-nct-kick-it-sexy-gif-16500096",
            "https://tenor.com/view/nct127-nct-johnnynct-nctjohnny-nctcon-gif-13199412",
            "https://tenor.com/view/johnny-nct-handsome-pose-hair-flip-gif-14331091",
            "https://tenor.com/view/johnny-oh-daddy-nct-nctdaddy-nctjohnny-gif-11704443",
            "https://tenor.com/view/nct-johnny-thicc-ohdaddy-nct127-gif-13935515",
            "https://tenor.com/view/nct127-johnny-suh-johnny-kick-it-kpop-gif-17169139",
            "https://tenor.com/view/nct-nct127-johnny-john-suh-car-gif-14629908",
            "https://tenor.com/view/johnnysuh-johnny-nct-127-johnnyseo-gif-14185990",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-LT5lH8xtjzdfxLf5Kt",
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-JR6UTFm1zVc5Fu0RtC",
            "https://giphy.com/gifs/nctsmtown-nct-127-u-1kLYKJnUnI21Bn3uNe"]

        self.bot.nct_chenle_gif = ["https://tenor.com/view/alechris-gif-19117093",
            "https://tenor.com/view/nct-chenle-nct-dream-chenle-nct-nct-dream-ridin-mv-gif-19715375",
            "https://tenor.com/view/chenle-zhong-chenle-nct-dream-shades-on-kpop-gif-16095981",
            "https://tenor.com/view/zhong-chenle-nct-yearbook-photoshoot-bored-gif-13626674",
            "https://tenor.com/view/nct-chenle-nct-dream-chenle-nct-dream-chenle-nct-dream-chenle-nct-gif-19715373",
            "https://tenor.com/view/nct-nct-dream-kpop-zhong-chenle-chenle-gif-14900503",
            "https://gfycat.com/advanceddeafeningbobcat",
            "https://64.media.tumblr.com/fb1b4cc9acefa5261a15384710bdd471/5708ec1f20b34f8b-22/s400x600/2677c1703d24dbb7c1ab4664229fbb8f6282bf29.gif",
            "https://64.media.tumblr.com/2c47f819058dd28eb31a06e620080687/tumblr_oztkw5NXuj1ubch87o1_400.gif",
            "https://zhongchenlenctdream.carrd.co/assets/images/image01.gif?v57784692551551",
            "https://i.pinimg.com/originals/4f/16/41/4f1641bcbd46cfdd77600bbeec94c89c.gif",
            "https://data.whicdn.com/images/309088415/original.gif",
            "https://64.media.tumblr.com/22ffd7b241c8e6b385f08c67c3cd4ed7/tumblr_ozr19c6QFX1um8zcso1_500.gif",
            "https://imgur.com/U5CnCWL",
            "http://pa1.narvii.com/6823/fb669e25a2315f05262a4277bf8fa51035be3b51_00.gif",
            "https://tenor.com/view/nct-nct-dream-kpop-what-wow-gif-14900509",
            "https://tenor.com/view/zeusnnie-snoopyzenz-gif-19291054",
            "https://tenor.com/view/nct-dream-nct-chenle-nct-chenle-nct-chenle-nct-dream-gif-19715366",
            "https://tenor.com/view/chenle-nct-cute-nctdream-laugh-gif-12562611",
            "https://tenor.com/view/nct-christmas-merry-christmas-kpop-cute-gif-15880091",
            "https://tenor.com/view/chenle-nct-dream-zhong-chenle-locker-room-kpop-gif-17201970",
            "https://tenor.com/view/nct-dream-chenle-ridin-mv-ridin-mv-nct-chenle-chenle-nct-dream-gif-19715376",
            "https://tenor.com/view/nct-chenle-ridin-mv-nct-dream-chenle-gif-19715377",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-p5FXsQOzRoVgU2SmkA",
            "https://64.media.tumblr.com/7570a5f70af01223ccca18a8a56b5043/1b91aaec34336370-6e/s400x600/89e86517efeef3cb251e3eda3d315bccded691c1.gif"]

        self.bot.nct_sungchan_gif = ["https://tenor.com/view/sungchan-sungchansmile-nct-nct2020-nctsungchan-gif-19820916",
            "https://tenor.com/view/nct-sungchan-nct-u-sungchan-nct2020sungchan-gif-20286601",
            "https://tenor.com/view/sungchan-jung-nct-nctu-pointing-gif-19594749",
            "https://tenor.com/view/nct-u90s-love-sungchan-nct-u-sungchan-nct-sungchan-gif-19887803",
            "https://tenor.com/view/nct-sungchan-nct2020sungchan-gif-20286636",
            "https://64.media.tumblr.com/68a0632113213e4ee388f3ecb6214321/21316b4d2e005c47-f0/s400x600/60ff2adc4b04fa5993ff4d417dd8358d3a17c749.gif",
            "https://64.media.tumblr.com/d7c8b5a150c15c77de8926203d248884/f9206b42435c4649-12/s400x600/3714b23c7e212d9a4b2e6501def9b7549fb4763d.gif",
            "https://i.pinimg.com/originals/7e/38/e9/7e38e908c8d9349c0744348881b92230.gif",
            "https://data.whicdn.com/images/348941908/original.gif",
            "https://i.pinimg.com/originals/d1/8d/42/d18d42b93aaf9529ee394d4714e8577b.gif",
            "https://media1.tenor.com/images/07ef96d11ff046f955c193cfdf75e35c/tenor.gif?itemid=19371869",
            "https://64.media.tumblr.com/eb5a6109f128f973e1f31f3f7416b766/d3c767270b070037-30/s400x600/c677d636d7025dc10f58266aaaa72ae053a1aa1d.gif",
            "https://64.media.tumblr.com/38efdee1d25f2698c56b524746873acd/c7085a0b7ee464e9-b2/s500x750/a91bc4d45d00f52477c5a8f727eabb30b8d99bb7.gif",
            "https://64.media.tumblr.com/4d604f7852e24b36438dd6467d56c9f9/d3c767270b070037-ee/s400x600/0c25a3e3d12504edb22af26526d342e547c3c19a.gif",
            "https://i.pinimg.com/originals/c1/95/b6/c195b676c01a27d23bd9bdc6b52ae16d.gif",
            "https://media1.tenor.com/images/6c7b5b9051b7c78e62e993b3b882a184/tenor.gif?itemid=20286601",
            "https://64.media.tumblr.com/cfbfaac0dc29bdbc5ab36f4a6a5fd4b7/c9c961a5d1076ab6-fb/s400x600/0c0daca12beac5a237082b33392a37955724449d.gif",
            "https://tenor.com/view/sungchan-gif-19303434",
            "https://tenor.com/view/sungchan-nct-nct-sungchan-pout-aegyo-gif-18929266",
            "https://tenor.com/view/sungchan-gif-19899739",
            "https://tenor.com/view/nct-sungchan-gif-19975659",
            "https://tenor.com/view/nct-sungchan-nct-u-sungchan-nct2020sungchan-gif-20286540",
            "https://tenor.com/view/nct-sungchan-kitty-cat-kitten-gif-19481210",
            "https://tenor.com/view/jung-sungchan-sungchan-nct-nct-u-kiss-gif-19819628",
            "https://tenor.com/view/nct-u-sungchan-nct-u90s-love-sungchan-nct-sungchan-nct2020-gif-19887790",
            "https://tenor.com/view/love-sungchan-nct-jlgif-heart-gif-19798986",
            "https://tenor.com/view/sungchan-nct-sungchan-sungchan-smile-gif-19371721",
            "https://tenor.com/view/sungchan-nct-nct-sungchan-pout-aegyo-gif-18929266",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-172-HRUXMoxwcIGKQp2etr",
            "https://64.media.tumblr.com/532c09c7414263ff881effefc625527e/515e1132e5db1174-91/s640x960/55cb5196bd96dbff14a5d25403abfe564416b165.gif"]

        self.bot.nct_dream_ot7_gif = ["https://gfycat.com/alarminghopefulalabamamapturtle-haechan-chenle-jaemin-jisung-renjun",
            "https://cdn.discordapp.com/attachments/813178959352037436/813201653427732510/dreamot71.gif",
            "https://tenor.com/view/seasonsbloom-wegoup-7dream-nctdream-nct-gif-19351968",
            "https://tenor.com/view/7dream-wegoup-we-go-up-gif-19351970",
            "https://media.giphy.com/media/0ApiD4eUldGbbOTe7j/giphy.gif",
            "https://tenor.com/view/nct-dream-nct-dream-dreamies-ot7-gif-19649096",
            "https://tenor.com/view/nct-dream-gif-18192845",
            "https://tenor.com/view/seasonsbloom-nctdream-nct-dream-gif-19351943",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-WBOgIZFabt7llNu9Iw",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-IOZrC17vafHEuVIu2C",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-ruMxuqmAJu3O1UUFj0",
            "https://cdn.discordapp.com/attachments/813178959352037436/813786950417776640/nctdreamot73.gif",
            "https://giphy.com/gifs/Ehd4rd16bnR3fiHh50",
            "https://data.whicdn.com/images/318273495/original.gif",
            "https://64.media.tumblr.com/cc4485bc329dd1a0b4a19675619ea38a/8735679a8aa62d3a-86/s400x600/714011d92603db9c0350d015063ad42d58fc609e.gif",
            "https://64.media.tumblr.com/6bdaf1e4dfcf302e9e464a2acaf0e0f4/8735679a8aa62d3a-82/s400x600/a71cd66692707b16af772daabb94e52f0975cb99.gif",
            "https://64.media.tumblr.com/d7d1ddded8b802f0735d39b394e63678/tumblr_pjarqzPBtF1wz1z6io4_r1_400.gif",
            "https://64.media.tumblr.com/1e99dc43b3807e74dff898601b05a505/tumblr_pjarqzPBtF1wz1z6io6_r1_400.gif",
            "https://64.media.tumblr.com/62a36e6460bed575dcc902dceb122c8e/tumblr_pjarqzPBtF1wz1z6io5_r1_400.gif",
            "https://64.media.tumblr.com/5f0a9cf5ca9dd5a8425f1226ada8672a/12e2dad76db22ec9-d0/s540x810/ed74d35dcce5d98818bc3851d07829554fac2e65.gif",
            "https://64.media.tumblr.com/96d8698720e5a3e1f0a5a17c4612b060/8735679a8aa62d3a-91/s400x600/1603eb7f67f8659eef6e61edad03f123467bdad5.gif",
            "https://64.media.tumblr.com/73b9307ed2fb647234ba6f6c2d8091f4/f5ea5e1bb26d7bde-28/s400x600/3ea81119916cdc07f7098b41c13d06d69704c460.gif",
            "https://64.media.tumblr.com/8c982973484dba6cd5908766859b3b82/57c87f954860a97f-93/s400x600/e88e3b334a3687f30a3b499609a4b07c1269fcd3.gif",
            "https://64.media.tumblr.com/423a75f2c4e40e62d87755bf7e756bbd/tumblr_pkytboBkk41qhfbpw_400.gif",
            "https://64.media.tumblr.com/a290a70db6d01eb3c0a42551c27ad2e1/f3008b1f7da8f713-ff/s400x600/ce59d92b049d95cef778629524e7c4e97dcbf8b3.gif",
            "https://64.media.tumblr.com/281cd5304b5eaeb0a902c6655942b761/f3008b1f7da8f713-d7/s400x600/c2226014ec3acf27926a16b5194b886629206a51.gif",
            "https://64.media.tumblr.com/48ca511cad37538df3ac79863aa9b582/1e51d1d56caae7a2-7a/s400x600/92fa82bda6cdc4f21406fd37bcbd8c6a9c3ef155.gif",
            "https://64.media.tumblr.com/b864084bba6b88972a6fd3a897ea4f6d/0043511a90fe19f3-ee/s540x810/f9301bdb716a14ef9f85eba52ece930acc3628b4.gif",
            "https://64.media.tumblr.com/3c65cfcce26a4a3c6d28e417178ece0f/0043511a90fe19f3-52/s540x810/fd8df67d0d3d2b4ce194d59193956201af56b75e.gif",
            "https://64.media.tumblr.com/40a68df9fbed353443205ed4313017f2/0043511a90fe19f3-e7/s540x810/cbdcee960ae154de1f37203dcaa98f8e6b34de36.gif",
            "https://64.media.tumblr.com/cec453333b277d85cc3404adcf73adb8/0043511a90fe19f3-d0/s540x810/8e5cac4759758432b1db7d3dd48e98413707a389.gif"]

        self.bot.nct_127_ot9_gif = ["https://tenor.com/view/nct-127-gif-14185973",
            "https://tenor.com/view/singing-%EC%97%94%EC%94%A8%ED%8B%B0127-nct127-touch-dancing-gif-16429761",
            "https://tenor.com/view/nct-boy-group-kpop-sm-entertainment-pose-gif-17917866",
            "https://tenor.com/view/nct-kpop-nct127-gif-18010518",
            "https://tenor.com/view/taking-a-photo-%EC%97%94%EC%94%A8%ED%8B%B0127-nct127-touch-photograph-gif-16429790",
            "https://tenor.com/view/group-pose-posing-badass-boy-group-kpop-group-gif-14622352",
            "https://tenor.com/view/nct-127-simon-says-simon-says-gif-13753815",
            "https://tenor.com/view/nct-nct127-gif-19934254",
            "https://tenor.com/view/nct127-kick-it-haechan-marklee-johnny-gif-16533501",
            "https://tenor.com/view/nct-nct127-nct-meme-creepy-creeping-gif-14265891",
            "https://tenor.com/view/nct127-nct-dance-gif-14378498",
            "https://tenor.com/view/nct127-nct-dance-gif-14378470",
            "https://tenor.com/view/neostelle-polaryong-polaryong-lee-neostelle-debut-gif-19361670",
            "https://tenor.com/view/nct127-johnny-jaehyun-nct-gif-19036872"]

        self.bot.nct_wayv_gif = ["https://tenor.com/view/nct-wayv-kun-ten-winwin-gif-13569066",
            "https://gfycat.com/plasticacademicerne-wayv-nct",
            "https://gfycat.com/coarseunnaturalfiddlercrab",
            "https://gfycat.com/directhastybarb",
            "https://gfycat.com/shabbyhelplessgilamonster-people-blogs-weishenv-yangyang-hendery",
            "https://gfycat.com/blandpoorguernseycow",
            "https://tenor.com/view/wayv-gif-19764878",
            "https://tenor.com/view/wayv-turn-back-time-music-video-kpop-dance-gif-17480425",
            "https://tenor.com/view/wayv-kpop-boy-group-cute-handsome-gif-17691644",
            "https://64.media.tumblr.com/b48c485d4be7bbd667f34ad411789bc6/a70d023a1a0b6024-80/s540x810/a4f95851482014bc12fa5922b23ecbce14e8a662.gif",
            "https://64.media.tumblr.com/a494a83748b8dcea4e72254a6a263a76/tumblr_plunt5P5pY1rg9u0to2_540.gif",
            "https://64.media.tumblr.com/bce6a95fc759e5d108f0646693372a39/d8223b9d43a16523-45/s540x810/fea62b03c1cba0efaa0a012d179528c9d7c592a3.gif",
            "https://64.media.tumblr.com/82d8b1debd11d6e9ad4b7582f2838121/bf7ccc59c863df21-d6/s540x810/f410cbb5a4a260fd04d43ac238b6ff4fba1491f7.gif",
            "https://64.media.tumblr.com/894795b12d2baa31da9468f7307498c4/583e9ed81d92da88-38/s400x600/d3205fec0a09c3d818f6a222f52357ba1609752a.gif",
            "https://64.media.tumblr.com/dc24dfdef2658ca99d5f8e679b22036a/583e9ed81d92da88-78/s400x600/f8742b2cebe8912aa13c69c9bbfc9f7c835c4b4a.gif",
            "https://64.media.tumblr.com/a98235bf3154e1e8fa74459749bdb843/bcce55925b8a9da6-20/s400x600/c83861f954d66c3c3f821f4c0a899c071cd46073.gif",
            "https://64.media.tumblr.com/ff69445b9745c2d82bf889f66b1621fa/bcce55925b8a9da6-59/s400x600/503c659e3106dd70c10742cc06340d50955db590.gif",
            "https://64.media.tumblr.com/c35481b6dcb1d3e16ee52ef5fbe2e489/bcce55925b8a9da6-29/s400x600/6d71bae68a59e9036b3a34a441d0af2731ea112e.gif",
            "https://64.media.tumblr.com/15787dd03132064c420d62558271ccab/bcce55925b8a9da6-ea/s400x600/0c67606c4221dcb4622e1d4889e4f7c4b430dff3.gif",
            "https://64.media.tumblr.com/36f0bff886d67425bbde4b3d5f38a9ac/bcce55925b8a9da6-78/s400x600/47e03c6969c72adc2a7623bd74d7293cd21e492e.gif"]

    @commands.command()
    async def nct(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [NCT {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "mark":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Mark :heart:')
                await ctx.send(random.choice(self.bot.nct_mark_gif))
                await ctx.message.delete()
        elif arg == "lucas":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Lucas :heart:')
                await ctx.send(random.choice(self.bot.nct_lucas_gif))
                await ctx.message.delete()
        elif arg == "winwin":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Winwin :heart:')
                await ctx.send(random.choice(self.bot.nct_winwin_gif))
                await ctx.message.delete()
        elif arg == "jaemin":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jaemin :heart: ')
                await ctx.send(random.choice(self.bot.nct_jaemin_gif))
                await ctx.message.delete()
        elif arg == "jaehyun":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jaehyun :heart: ')
                await ctx.send(random.choice(self.bot.nct_jaehyun_gif))
                await ctx.message.delete()
        elif arg == "kun":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Kun :heart: ')
                await ctx.send(random.choice(self.bot.nct_kun_gif))
                await ctx.message.delete()
        elif arg == "ten":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Ten :heart: ')
                await ctx.send(random.choice(self.bot.nct_ten_gif))
                await ctx.message.delete()
        elif arg == "xiaojun":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Xiaojun :heart: ')
                await ctx.send(random.choice(self.bot.nct_xiaojun_gif))
                await ctx.message.delete()
        elif arg == "hendery":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Hendery :heart: ')
                await ctx.send(random.choice(self.bot.nct_hendery_gif))
                await ctx.message.delete()
        elif arg == "yangyang":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yangyang :heart: ')
                await ctx.send(random.choice(self.bot.nct_yangyang_gif))
                await ctx.message.delete()
        elif arg == "taeyong":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Taeyong :heart: ')
                await ctx.send(random.choice(self.bot.nct_taeyong_gif))
                await ctx.message.delete()
        elif arg == "jungwoo":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jungwoo :heart: ')
                await ctx.send(random.choice(self.bot.nct_jungwoo_gif))
                await ctx.message.delete()
        elif arg == "yuta":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yuta :heart: ')
                await ctx.send(random.choice(self.bot.nct_yuta_gif))
                await ctx.message.delete()
        elif arg == "jeno":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jeno :heart: ')
                await ctx.send(random.choice(self.bot.nct_jeno_gif))
                await ctx.message.delete()
        elif arg == "jisung":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jisung :heart: ')
                await ctx.send(random.choice(self.bot.nct_jisung_gif))
                await ctx.message.delete()
        elif arg == "renjun":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Renjun :heart: ')
                await ctx.send(random.choice(self.bot.nct_renjun_gif))
                await ctx.message.delete()
        elif arg == "doyoung":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Doyoung :heart: ')
                await ctx.send(random.choice(self.bot.nct_doyoung_gif))
                await ctx.message.delete()
        elif arg == "haechan":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Haechan :heart: ')
                await ctx.send(random.choice(self.bot.nct_haechan_gif))
                await ctx.message.delete()
        elif arg == "shotaro":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Shotaro :heart: ')
                await ctx.send(random.choice(self.bot.nct_shotaro_gif))
                await ctx.message.delete()
        elif arg == "taeil":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Taeil :heart: ')
                await ctx.send(random.choice(self.bot.nct_taeil_gif))
                await ctx.message.delete()
        elif arg == "johnny":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Johnny :heart: ')
                await ctx.send(random.choice(self.bot.nct_johnny_gif))
                await ctx.message.delete()
        elif arg == "chenle":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chenle :heart: ')
                await ctx.send(random.choice(self.bot.nct_chenle_gif))
                await ctx.message.delete()
        elif arg == "sungchan":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Sungchan :heart:')
                await ctx.send(random.choice(self.bot.nct_sungchan_gif))
                await ctx.message.delete()
        elif arg == "dream":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about NCT Dream :heart:')
                await ctx.send(random.choice(self.bot.nct_dream_ot7_gif))
                await ctx.message.delete()
        elif arg == "127":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about NCT 127 :heart:')
                await ctx.send(random.choice(self.bot.nct_127_ot9_gif))
                await ctx.message.delete()

    @commands.command()
    async def wayv(self, ctx,):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [WayV] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about WayV :heart:')
            await ctx.send(random.choice(self.bot.nct_wayv_gif))
            await ctx.message.delete()
    
    @commands.command()
    async def jaehyun(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Jaehyun] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jaehyun :heart: ')
                await ctx.send(random.choice(self.bot.nct_jaehyun_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jaehyun :heart:')
            await ctx.send(random.choice(self.bot.nct_jaehyun_gif))
            await ctx.message.delete()


def setup(client):
    client.add_cog(NCT(client))

    # @commands.command()
    # async def lucas(self, ctx):
    #     if ctx.guild.id == luminary:
    #         if ctx.channel.id == kbotcom:
    #             await ctx.send(f'<@{kate}>, <@!{ctx.author.id}> is talking about Lucas :heart: ')
    #             await ctx.send(random.choice(self.bot.nct_lucas_gif))
    #             await ctx.message.delete()
    #         else:
    #             await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
    #             await ctx.message.delete()
    #     else:
    #         await ctx.send(f'<@!{ctx.author.id}> is talking about Lucas :heart:')
    #         await ctx.send(random.choice(self.bot.nct_lucas_gif))
    #         await ctx.message.delete()
    
    # @commands.command()
    # async def mark(self, ctx):
    #     if ctx.guild.id == luminary:
    #         if ctx.channel.id == kbotcom:
    #             await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Mark :heart: ')
    #             await ctx.send(random.choice(self.bot.nct_mark_gif))
    #             await ctx.message.delete()
    #         else:
    #             await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
    #             await ctx.message.delete()
    #     else:
    #         await ctx.send(f'<@!{ctx.author.id}> is talking about Mark :heart:')
    #         await ctx.send(random.choice(self.bot.nct_mark_gif))
    #         await ctx.message.delete()

    # @commands.command()
    # async def winwin(self, ctx):
    #     if ctx.guild.id == luminary:
    #         if ctx.channel.id == kbotcom:
    #             await ctx.send(f'<@!{ctx.author.id}> is talking about Winwin :heart: ')
    #             await ctx.send(random.choice(self.bot.nct_winwin_gif))
    #             await ctx.message.delete()
    #         else:
    #             await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
    #             await ctx.message.delete()
    #     else:
    #         await ctx.send(f'<@!{ctx.author.id}> is talking about Winwin :heart:')
    #         await ctx.send(random.choice(self.bot.nct_winwin_gif))
    #         await ctx.message.delete()

    # @commands.command()
    # async def jaemin(self, ctx):
    #     if ctx.guild.id == luminary:
    #         if ctx.channel.id == kbotcom:
    #             await ctx.send(f'<@!{ctx.author.id}> is talking about Jaemin :heart: ')
    #             await ctx.send(random.choice(self.bot.nct_jaemin_gif))
    #             await ctx.message.delete()
    #         else:
    #             await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
    #             await ctx.message.delete()
    #     else:
    #         await ctx.send(f'<@!{ctx.author.id}> is talking about Jaemin :heart:')
    #         await ctx.send(random.choice(self.bot.nct_jaemin_gif))
    #         await ctx.message.delete()
