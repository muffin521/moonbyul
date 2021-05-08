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
            "https://gfycat.com/GiftedMisguidedFireant",
            "https://64.media.tumblr.com/4c8ccb5971f27489d6612f009f14085f/302e44f76695bfda-07/s540x810/888e5bc69d9e083c6abde2229d9b998f5b3a1db9.gif"]

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
            "https://64.media.tumblr.com/39d9536c2228b944dfd596ccbbd8e16f/1b91aaec34336370-03/s400x600/0c301160b8475b80adcd085b7966c1bbc8695216.gif",
            "https://tenor.com/view/jaemin-nct-najaemin-gif-20812989",
            "https://tenor.com/view/jaemin-nct-najaemin-gif-20812988"]

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
            "https://64.media.tumblr.com/28134a5e49c9ed8488f23a64ee37b3a7/ea0352b5ba837d08-9a/s400x600/ab59c768039912cdf7338895e93921e0942872a6.gif",
            "https://tenor.com/view/ten-chittaphon-leechaiyapornkul-nct-gif-21128048",
            "https://tenor.com/view/ten-chittaphon-leechaiyapornkul-nct-gif-21128051",
            "https://tenor.com/view/ten-chittaphon-leechaiyapornkul-nct-gif-21128049",
            "https://tenor.com/view/ten-chittaphon-leechaiyapornkul-nct-gif-21128047",
            "https://64.media.tumblr.com/2e66592d007e0b2457d37b4c926958db/76bb309d8238c9e4-55/s540x810/65e2b7cb3c01d3dd7ded5b025ef0d682dcbbd123.gif",
            "https://64.media.tumblr.com/606e9874e6d6396ebee3f3a260cf529a/76bb309d8238c9e4-8b/s400x600/d314e292b7f0b7d35c26a142bca76121f664ddb7.gif",
            "https://64.media.tumblr.com/2361436220408fcb3b86e1bc8fcf4f53/76bb309d8238c9e4-5d/s400x600/0bfebb591ea3fc8deb6255f489a0470c4c96946e.gif",
            "https://64.media.tumblr.com/cfb5317afb92f9bbd1e005d93c560e51/76bb309d8238c9e4-ca/s400x600/03a46ac06594f0740a560901443b5a664c8c8dad.gif",
            "https://64.media.tumblr.com/d49b77ed98fa9f410ca948812c90b718/76bb309d8238c9e4-ba/s400x600/4e226eb1b7b6c11b67bec3f73a2b3f0d26b27541.gif",
            "https://64.media.tumblr.com/c624b5bd00de3ff3a02345cdff4eacf1/76bb309d8238c9e4-60/s400x600/d8d0f144047dde8ded765c00e890718a60109dac.gif",
            "https://64.media.tumblr.com/0a9df2e0f91d15aca92d5d61dea8e36d/64462799c5d24d24-1b/s250x400/3afb16e14229ee574f131f844a1da1222caa9bec.gif",
            "https://64.media.tumblr.com/86c821fe666aca23dd0da84965968ae3/64462799c5d24d24-92/s250x400/da33c350a2740c14dc90cca880a5e45011168a41.gif",
            "https://64.media.tumblr.com/b619de4df5f6535f7bbabbfbe13caff1/64462799c5d24d24-cf/s250x400/c86972f2851fa0025dba738506de07caea90f98e.gif",
            "https://64.media.tumblr.com/d4c7b8b118b98a8438c0e9db0a11b71a/64462799c5d24d24-af/s250x400/9c2c530e18ca864f0fc9d6871a885a352ba748f7.gif",
            "https://64.media.tumblr.com/7cefd266fc15ff37507c0ac6527a89d7/64462799c5d24d24-c4/s250x400/ef8414d696b9a74398be18f9c01018ab6c952ac4.gif",
            "https://64.media.tumblr.com/d7fa9d4840a87ec36cecbfceed1cafa1/64462799c5d24d24-97/s250x400/3692bb543ddf8bc55948d2908b3aedc8ce11f3e6.gif",
            "https://64.media.tumblr.com/50cebe13b7dcee0c2b0b0074735e5e0c/64462799c5d24d24-2f/s250x400/2e825570947479abe98c4076e928a1422327d468.gif",
            "https://64.media.tumblr.com/cf959c5f2b2bb00c7f54b2569bee2956/64462799c5d24d24-82/s250x400/6ff638377149f911846f825d4cfa49c388e0ad9e.gif"]

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
            "https://64.media.tumblr.com/79708d31c326042d94ebdacdb7ab1489/140e02c93672e4df-21/s400x600/983bc2cfab5b7b8f88de0fd6f16b9eb030f2c58b.gif",
            "https://64.media.tumblr.com/b9cb0efa4b0069694a93c3690e186430/41651d8fc7482a95-b6/s400x600/7f646c3fdfda203c1dcc0455ce399b3ace29cc61.gif",
            "https://64.media.tumblr.com/05ad0378cda239663fbadf44c8a711b7/0685dff5957f4c61-8e/s400x600/46a34a6cedf765209cde72aa1ee83459257296f9.gif",
            "https://64.media.tumblr.com/f2e3773bd6a81dc3846a2278875e9082/b5ffb3b5713dd149-2d/s400x600/d9405588eb865bd319f09d73fae725e47723912d.gif",
            "https://64.media.tumblr.com/b15788eee8f48be4cfd9e8b318cb279e/40c32b0c077ac3e9-c8/s250x400/57da37a26fad4dc61ba6be6f28394c2d1aead80e.gif",
            "https://64.media.tumblr.com/ff72cff90d37f7093cc5bc453981bcf0/a580af8e2c2029f2-48/s400x600/6ec385e89d5cc30696b19b85ab3e30572242ba3a.gif",
            "https://64.media.tumblr.com/c7b558e5b05ae6229dd6d98117e2d191/c0808ecc543292fb-88/s400x600/d515c11e24e25d94c1b6a0ea20966432fb6be2ce.gif",
            "https://64.media.tumblr.com/f34ed7074322f9dfb0a80f7268030d07/52faa2430392084f-b6/s250x400/1d77d74b2167f78d494dfa68b5e389e279410887.gif",
            "https://64.media.tumblr.com/f4bc74919a69032478f6ed297237cedc/0a8e63c36f42914c-fc/s400x600/8d6377b04a8df126795fbe720a25797e0bc0c67e.gif"]

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
            "https://64.media.tumblr.com/1490d517b01173c226cb25bf7d5ed95d/ea0352b5ba837d08-21/s400x600/880aebf1881afbc13d00957f2869a371854d7c0a.gif",
            "https://64.media.tumblr.com/75c5fce386359292e83ca1e1dfdfe19b/0685dff5957f4c61-c6/s400x600/560dedc568719879847044392b9cf9260c578123.gif",
            "https://64.media.tumblr.com/efa5c7d76b23a021ef370c6a39fc18cf/1e8ffaea38db60c3-e4/s400x600/ae97d32fca6f2c006939f59130dd79a7677691bf.gif",
            "https://64.media.tumblr.com/91f855672aa0fb48344953bdfc223425/1e8ffaea38db60c3-6d/s400x600/65d80dae94a0d399332f7ba3475ceb97fdd46a7e.gif",
            "https://64.media.tumblr.com/62a7af885bbf15f2946d6ddc6efa730b/1e8ffaea38db60c3-67/s400x600/0cd5f42866f5667465c3efb91148db0e14c11cc3.gif",
            "https://64.media.tumblr.com/6af4c0fb4144ea818a566a7dd0f703ff/1e8ffaea38db60c3-09/s400x600/cfd99d426273dfce10a60d24744c5238baaef6af.gif",
            "https://64.media.tumblr.com/5a8fe24e91a268fdbeefd237c88ca345/1e8ffaea38db60c3-33/s400x600/0ff649ac6090fa0ae1b57b9c6d8eaf51f369e737.gif",
            "https://64.media.tumblr.com/4e8e9b3e01f9731cc2f8040e3a012cc3/af39b7d39426ec46-ed/s400x600/4f075f097c4cb665ee71ccc2267de4466633111d.gif",
            "https://64.media.tumblr.com/8a4b4a56254a296876f9085182c97802/a5da3aee62cc7738-08/s250x400/033665f264c8991e5a8bee8825ba01889cc44c81.gif",
            "https://64.media.tumblr.com/761a63149d6baacd6ed8f678fa96b1b3/a72985e411cca086-3a/s400x600/ef8870109496e1b97fcf3916b8a5d58e8dfc80fd.gif",
            "https://64.media.tumblr.com/95117bdfe54a14be7fde9b9f2955a783/a72985e411cca086-80/s400x600/360e13293d0a9a3afde9b2efbbff2c07a96004f8.gif",
            "https://64.media.tumblr.com/517e35200458812861b9b26413eee41c/a72985e411cca086-48/s400x600/0c8f77013ec4adb14f09edb32e35a75fe679442f.gif",
            "https://64.media.tumblr.com/9163ed9c57351368ebeb740e0e96dbab/a72985e411cca086-b5/s400x600/43d2832afc55473426db02f8f20585a809ba1473.gif",
            "https://64.media.tumblr.com/ddc9d8d72103833e6025b96c6ca9198f/a72985e411cca086-5b/s400x600/d76e89c0941109f422f97b00da7d46ced474097d.gif",
            "https://64.media.tumblr.com/9f0c959de819114bbd588a94e7760d4c/f759bd4235b1e56c-8b/s400x600/855596e92fbbb867baa7910219789622b14ea9bc.gif",
            "https://64.media.tumblr.com/356ffc9cfbe3c9a60d766a85063859c0/f759bd4235b1e56c-b0/s400x600/0d308695595d4166479c6fd89c7272c5467ec862.gif",
            "https://64.media.tumblr.com/e83b0870ed0ecb9d0d419ab13dc3efe5/f759bd4235b1e56c-52/s400x600/d671bed10f486c65a5217c73e857006eddd47b1a.gif",
            "https://64.media.tumblr.com/5c7186cc7ba80d4474b1a04a4d5972bc/f5a121467d03952b-ff/s400x600/2a8f5784edfacebb309fb3f5ff97baf2c8388af8.gif",
            "https://64.media.tumblr.com/83b03767fc2f7e2c31b8a731584ce4b0/f5a121467d03952b-b2/s400x600/72f32d4ceda280d50de4171942b8250dc682a3b1.gif",
            "https://64.media.tumblr.com/28e1ec1e8f12ac9b7dcadb5fbe080bc9/89b0e2e140d2ddaf-21/s400x600/d6af534b155fba25a60ffcac2c732fe5b7737c4b.gif",
            "https://64.media.tumblr.com/f00ec55f278df7086188469d49a3f398/89b0e2e140d2ddaf-20/s400x600/f4af1a43800867d506759af442ab497f455a9591.gif",
            "https://64.media.tumblr.com/1851ec2058a53e6fd15161797b960891/a6d3f7d457d2f56a-a4/s400x600/e043d6af527788c9079a2a035343f7266d976423.gif",
            "https://64.media.tumblr.com/a34905e17036bd610f5ec2ef7be97baa/a6d3f7d457d2f56a-2f/s400x600/f2aff9c40110a8ecfe5e238d6f240d64118bd542.gif",
            "https://64.media.tumblr.com/70c593935525b850c726ab48ce788ebb/f759bd4235b1e56c-27/s400x600/e8e830f8aa592c4ea38d1e11e02626a63e1f587a.gif",
            "https://64.media.tumblr.com/162e0ece1ad19f96f79b1fa801e1f001/a6d3f7d457d2f56a-66/s400x600/488b3cbb90f5be3fcd0a5261a96c7a62b27cd962.gif",
            "https://64.media.tumblr.com/33d57d3fde835aa6136bf9331bb48635/7f5723e904e0f637-05/s250x400/40ead5ecd9ca3ddf32e7a94b9f361cb9955c1120.gif",
            "https://64.media.tumblr.com/efbe54e869f5a98e339513ccd8c979e8/c7dcdd5404cc3291-b5/s400x600/9c746c8380b32509f93f8a8ec7d3b77e12a522ee.gif"]

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
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-ATmBrSXPpXbBaN9ngv"
            "https://tenor.com/view/taeyong-nct-leetaeyong-gif-20693082",
            "https://tenor.com/view/taeyong-nct-leetaeyong-gif-20693091",
            "https://tenor.com/view/taeyong-nct-leetaeyong-gif-20693050",
            "https://tenor.com/view/taeyong-nct-leetaeyong-gif-20693049",
            "https://tenor.com/view/nct-nct127-kpop-lee-taeyong-ccg-gif-14769111",
            "https://tenor.com/view/nct-nct127-kpop-lee-taeyong-ccg-gif-14769157"]

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
            "https://giphy.com/gifs/nctsmtown-kpop-nct-172-AwY4PUEguW8iNVO3CX",
            "https://64.media.tumblr.com/3d7362c9aac55a14244344bbb6a7626f/1ddcfbb042128c9b-3a/s400x600/164a85bc5730c062cf18b67587a2540de35e6f3d.gif",
            "https://64.media.tumblr.com/37d9c546b3eb837c88ade273eb2f0acd/1b91aaec34336370-25/s400x600/4a6eb29c6f48089fc5ca09222a61cfdd3aea702d.gif",
            "https://64.media.tumblr.com/33dfa256789e4840604f654daa725636/596f301585e9bc82-e6/s250x400/a437bb97ed26a369bd90a4809467d3ca9ee5b47a.gif",
            "https://64.media.tumblr.com/99870665af7cc81842af3005975b3f52/42728aff45482e01-d5/s400x600/8da9058764478e976a80a4bc36654f2d4fceb350.gif",
            "https://64.media.tumblr.com/4061d666745d55eac32d30aa36142963/42728aff45482e01-4f/s400x600/bcc813cbad8347adb75b55660b0aff74f7af8841.gif",
            "https://64.media.tumblr.com/6a5eadc00187bfbe502f88a511818d79/42728aff45482e01-c2/s400x600/c434c6c39b91e27daf7d15f99b3916fda336dc83.gif",
            "https://64.media.tumblr.com/1aa283418ab314980b21d148fa1cba55/b0098d704a4d43f8-1e/s400x600/4ed52cb2292a15d429f19bd47fbe76bc3f7c3f8e.gif",
            "https://64.media.tumblr.com/2cb163d780b6372e8f442aa78e3354cd/b0098d704a4d43f8-8d/s400x600/cafd9a46d636452a46de799bda27f47388152a75.gif",
            "https://64.media.tumblr.com/c38d3b15ef6b708fa662962044fa8a5d/23852bda6eb4beef-70/s540x810/4a9a89aba193c8dae297b3c2f05f034877189225.gif",
            "https://64.media.tumblr.com/5e2633db19d3cb778a58b19d3c13d4e2/23852bda6eb4beef-0c/s540x810/30eaaab63ca55451c944e58e542240c8359e9b2f.gif",
            "https://64.media.tumblr.com/3fb944bfb372676ea9003aec86512671/23852bda6eb4beef-13/s540x810/12f33ef0d94f6dbd345e88879168626bff913711.gif",
            "https://64.media.tumblr.com/2c87b106c15f1665f6e382a2f3165e3d/23852bda6eb4beef-f4/s540x810/cf7427d57e2b01472625fe15edd427657dbe2767.gif",
            "https://64.media.tumblr.com/a83ee604f0f58689ec2a5e6b13536da2/23852bda6eb4beef-66/s540x810/f0f07111136abca59e9a752843bca1fdcb89605a.gif",
            "https://64.media.tumblr.com/16c9544ba0da1fd55573996ad127122f/23852bda6eb4beef-d2/s540x810/816e0a29ea5ffd3450a4f8f1b32b64671111b77b.gif",
            "https://64.media.tumblr.com/86353e3a23c807abaed9886d9d836a1d/5e1e00a0b3dbbea9-a9/s400x600/f3006d07c4f75d174ece052ac7734f287e7801b6.gif",
            "https://64.media.tumblr.com/6acc7d4d59419ce15380fa171e953a18/936da7a6e3134f96-9c/s540x810/2544c377e50323faaf0df2a11b03286eeda030e5.gif",
            "https://64.media.tumblr.com/92f5fa9fd75989185e62261667a13cd3/936da7a6e3134f96-57/s540x810/577461f5b5752c6a78b2ce2ff648297793a8edee.gif",
            "https://64.media.tumblr.com/8eecdd3845d8a71aed8b2784d2654b93/16ce111b2d8c10d1-52/s540x810/e1898040ff7f7f0d34fa0ba6b7bf9d534c24736e.gif",
            "https://64.media.tumblr.com/c24ef37a8492e8c56b2e4dbc38b7373c/16ce111b2d8c10d1-63/s540x810/9d197dff8a4c0c825752a2f1626dab72efb497c9.gif",
            "https://64.media.tumblr.com/6a794695785af3d1bc5ed22dd2867dc6/4fd3edfef29cbd6a-cf/s540x810/cdda62af4c88bbc40ec8ab45fa8691d503b58bc9.gif",
            "https://64.media.tumblr.com/0ccc5195ef11cd4b12b0fcc04ce6806d/4fd3edfef29cbd6a-af/s540x810/b51216f0cbecbc88b446175e9a236fa8fd1061ed.gif",
            "https://64.media.tumblr.com/aaecfd614946f5560b38ef9ee7d85f60/4fd3edfef29cbd6a-54/s540x810/5a5233dc7fbbf2e0ee3ad2d6b1e2c957f1aa2418.gif",
            "https://64.media.tumblr.com/5514ca8e762d2265cfd97752aa084f9c/b2cec23210a0b8a9-ce/s400x600/a18592375b7ba339abe56b3559836dc7738ea2f9.gif",
            "https://64.media.tumblr.com/e070aff030bcc720f2db19c047021eb0/1f1e23160d4cc5b7-65/s400x600/e49fc6b35bbb30261facfbbc51f82dcc71f0ef73.gif",
            "https://64.media.tumblr.com/4f30c22af7d2b9c98ca0fed2d9ac6619/81e64212fad6050a-70/s400x600/c388f8d6c0e777c3a18b1faa7a905d06131e9518.gif",
            "https://64.media.tumblr.com/d5766fd94968f16dd669280241f1e8ef/c9754fc370ab0eb5-7a/s250x400/d15854f39dc69f935544fc515bab7255b9df3dbc.gif",
            "https://64.media.tumblr.com/3e837f1161e8fabfb256dada4877ccf0/d7356c051ca5d7b8-56/s540x810/86f1bbedaec4dd85914f5877d8b4881214bf73f9.gif",
            "https://64.media.tumblr.com/21fe2796a18d0d4db5d580ab3d23a3f7/d7356c051ca5d7b8-a0/s540x810/cb81cf2dfaf627ccdfa2d83424cdf69b16b59d92.gif",
            "https://64.media.tumblr.com/07675e455d38db94db77afb325098e59/d7356c051ca5d7b8-4d/s540x810/a2f8664a50f716620616b8dfffef566de5832c2a.gif",
            "https://64.media.tumblr.com/a309f7b49543ba6ea7955a9fe28d6fe6/d7356c051ca5d7b8-aa/s540x810/5a619e0d16ce74b4a6d978b1637b3e05d7ee854c.gif",
            "https://64.media.tumblr.com/a771012a4a11a6008bdf26c4e26f9b81/49c77350834a0dc3-d5/s540x810/20ab4aac0d2f1d23cb26a05514416d67001ecdec.gif",
            "https://64.media.tumblr.com/d162071adc16e89278592b11c5c0fdf3/048fdd0bd52606a7-41/s540x810/52698774ca41729b0d478746e230af38a380ed8d.gif",
            "https://64.media.tumblr.com/4b52b782f52458597667832b8e7a9c58/048fdd0bd52606a7-33/s540x810/58afdd32ca78d86a9a375a39829de8e55353868b.gif",
            "https://64.media.tumblr.com/58a3419b2dfb6e8e9175021764e0ffa0/56452a6714ff4416-a6/s400x600/02ba7b31cb1afe637ab6148a3c64264e728b53a9.gif",
            "https://64.media.tumblr.com/83956c8f9d8f4973bc10ae38b5509e6c/91fa44ba3f11706b-bf/s400x600/caadc9cdf0a95c85236d5c92ea4b0037bbf6dc37.gif",
            "https://64.media.tumblr.com/2e8f85b901677ad2683098ca0d466333/91fa44ba3f11706b-02/s400x600/974d4fa2364fd4d89f3ba3ef626b01358f9a262e.gif",
            "https://64.media.tumblr.com/a02b7d44f336946b003ca8a76a59d799/fa683ecddbf0b478-05/s400x600/f2a77e10aed52b708c73bf22c9d245c7c069e5fb.gif",
            "https://64.media.tumblr.com/8e9add4bd4d7709ef54917aa97d14807/fa683ecddbf0b478-e6/s400x600/c14e263383143e2a3d0492ffcf05409b68ccf67e.gif",
            "https://64.media.tumblr.com/2feff753a896cbdc43cd9e2e2988fcf8/6f8e0190de9a55aa-37/s250x400/3994f58de33f2f1413706b475b548f1e66cc4e5f.gif",
            "https://64.media.tumblr.com/81fb896604dc407bcd190b70af70238f/edef875913e82f4c-42/s540x810/82d3403e2a79569e4edd87d3dfe3d27d338657db.gif",
            "https://64.media.tumblr.com/ede574e4b20221cbb815b1eff83d681c/f3b7319d58f51abc-2b/s400x600/856c4fbaa209c77bb0c9aa6a9935589ea598a57c.gif",
            "https://64.media.tumblr.com/83643d474fc76c5e5dbd4a2b997a6099/2fd6cf7a39cdf132-ff/s400x600/850af7f41e9de70f42e23ccfedd701ccc2d9c794.gif",
            "https://64.media.tumblr.com/7f018e5d70256873232e9cd8d3433854/7d481a8cfa1b24c6-40/s400x600/76f7dc9da2233f9d614dfe6edc2cae7234bd30a4.gif",
            "https://64.media.tumblr.com/d0468c82977375726e216936279037e2/7d481a8cfa1b24c6-a6/s400x600/57850ca1625b73cf8a2dbcf5ad5aaa51de669686.gif",
            "https://64.media.tumblr.com/fcceae5e8568bdbc4ee4791b36901846/7d481a8cfa1b24c6-33/s400x600/4113a1f16b591134888da1b776b270ff69a347e2.gif",
            "https://64.media.tumblr.com/c4cb175ef87efec4ca24af24fc535d27/47bce1fa67a7aebc-f8/s400x600/48de540d7dee3835de6f3d0523dad56efd4da90f.gif",
            "https://64.media.tumblr.com/c5312a93c859ecdd8c593232117b6ab7/47bce1fa67a7aebc-2e/s400x600/9fb21e301d2f63c3d2b7dd3f8890adb452b672a8.gif",
            "https://64.media.tumblr.com/145eed97fcfda365e9420c6a82fe2b27/47bce1fa67a7aebc-50/s400x600/2a6f4397f2c66d7c5e9cb2714844c9f67a610a72.gif",
            "https://64.media.tumblr.com/f1fee2c294e5e6472299d8929a9f5fde/96d35298314acc76-63/s400x600/98c7584d1854d8f0fbe21797f7e80c1c07061a1b.gif",
            "https://64.media.tumblr.com/c41d7815312addfbcbcc2a2720540e11/96d35298314acc76-6f/s400x600/9e08db79e6d250741f6a9fb2c912d438cf264781.gif",
            "https://64.media.tumblr.com/1e95f79e8b4fb597f99b8eeb9e09e168/9c65834f25c613a4-28/s540x810/b516a2fe10a220b28f788c61b83d8c820cec6626.gif",
            "https://64.media.tumblr.com/5f82aa35dd81804a0438e4cfd97caab8/9c65834f25c613a4-6d/s540x810/c614c90c7a09615842e4827bfdb262d9d695395f.gif",
            "https://64.media.tumblr.com/56f22c79f4c7c53d28a2d45c9f2b942d/9c65834f25c613a4-6f/s540x810/d536bf6879135d23fc9f57ebb48c2532736347ef.gif",
            "https://64.media.tumblr.com/ee4fbdce158837c75d4425dc50399571/5ca6307ccbd10951-c5/s540x810/b894325f2f86cc3e385bb4ce8fa1644fa138efd2.gif",
            "https://64.media.tumblr.com/2adba04a1570d380f84ba43d0e604ce0/6257d3c279885ba5-8b/s400x600/233c0d9c07898311f09c9e26038561e1fdc76733.gif",
            "https://64.media.tumblr.com/a9c1b2afa3b204a7858c6b811e0597b6/6257d3c279885ba5-c4/s400x600/94c92ab078c24e0bcf9f416e0b05ce3a8b4b37aa.gif",
            "https://64.media.tumblr.com/dc99b3bf866721ceb3b88798b2ec6de2/d8b0702ca96856d3-6f/s250x400/fb9b219908da9c429710f54525470596ea872279.gif",
            "https://64.media.tumblr.com/2dd54809391febe6bba97d43941d583a/d8b0702ca96856d3-43/s250x400/2d2610b008152eaca9679aad198251777556dc11.gif",
            "https://64.media.tumblr.com/0c40dc62fa52bca9efd2aefa3f093e42/d6addddc51362482-e0/s400x600/93d8bde7899c81bf69243e3af5a1359191e13efe.gif",
            "https://64.media.tumblr.com/30b66cb3cb911cda0be47efc6e6c8795/d6addddc51362482-60/s400x600/157d813b63191176150fbc7c0ecdea44d2b92eb8.gif",
            "https://64.media.tumblr.com/9a74fbdde709c9c1fe4e21260a06d81a/d6addddc51362482-59/s400x600/71ebcebcdc920f29fa719b137ea2f8b0efb2828e.gif",
            "https://64.media.tumblr.com/60bb9bcafe30901942cd3a51a838ed9e/d6addddc51362482-11/s400x600/9cad062f1134845a75631abc6c1285d3e4c804ad.gif",
            "https://64.media.tumblr.com/e99229e81c0238f3d646ced49b875e6d/2e0b49ce514ce3ac-65/s400x600/44fad6532a33263a011dfb920474c695110c16d1.gif",
            "https://64.media.tumblr.com/24041c31d6fe06cf2366729e33371b5c/2e0b49ce514ce3ac-2d/s400x600/105947ce143c65ae961787061bf4f646945a419e.gif",
            "https://64.media.tumblr.com/792e48e429ec9a3ece5bc9191c2bfc07/be65805fe0312686-b0/s400x600/849d6872f5f4f92f2c3b4e5f3e3f2f494fa1519c.gif",
            "https://64.media.tumblr.com/eb3ea0d2a6808dde91b17f8102e696ad/be65805fe0312686-5f/s400x600/1a6e4c799f4dac9dc173ab8d140627a13a240b3f.gif",
            "https://64.media.tumblr.com/a36a04ec4c811aabe18b44f302fd1ee0/be65805fe0312686-71/s400x600/a691f654a849e825d00ca7cc109da3db0a63ddb7.gif",
            "https://64.media.tumblr.com/446b8cb32c702e8c00b46e33f44397f5/c1c65413b1ab7cf4-0f/s250x400/9e810b510255dcad9eaed8b88fba4daabe49585d.gif",
            "https://64.media.tumblr.com/ae685ea4fb46b36b93105ebd9812b393/8f912f73fadf2b2a-1a/s400x600/18e82dd36d34b11d2d9a27f9de4581b906bdc3ce.gif",
            "https://64.media.tumblr.com/eff197c9502c771ed34351c5e644ccd9/8f912f73fadf2b2a-28/s400x600/365438e12470a26fe3fb455d5bdfe2692ae7213e.gif",
            "https://64.media.tumblr.com/d1f2ef3edd68c70fb315875ed35c8011/8f912f73fadf2b2a-2c/s400x600/9d974e5257891b8c624125cc993ba3d76a7373e2.gif",
            "https://64.media.tumblr.com/767c3bafe1d9681d6ac546565cc5d67f/tumblr_inline_paw00prQKC1tdkl1l_540.gif",
            "https://64.media.tumblr.com/13e81cc8fa523add3489721acb0304de/5faf0610fbac2d2d-30/s400x600/55a1ef7fe2a9dde10b0fe5d03821cbc0fa244764.gif",
            "https://64.media.tumblr.com/182fb5655e9ce94389f00f2892bcb03e/5faf0610fbac2d2d-2c/s400x600/4e444e74dee023e9e61876f7abd225472ae9f9a6.gif",
            "https://64.media.tumblr.com/60048d70b7eacbb19197e6b6b7dd2578/8e3ef1c7590876f0-35/s400x600/b38ff8ddb3c7212cbe0ec652e6b426d98d4e11a2.gif",
            "https://64.media.tumblr.com/fc7efe21b80e179ba04031930441a893/dbf2907a3e52369b-92/s400x600/90b3bbe06f7b87af764c08806a7e744658a84446.gif",
            "https://64.media.tumblr.com/d445eeebec34be9812eb938a987b2d44/8e3ef1c7590876f0-76/s400x600/556b732e8faddbd7a375b014d897103b1776c1b1.gif",
            "https://64.media.tumblr.com/71c629db82fa6aa3c4622f13f46cb1db/ae0cbe4c05f4b835-47/s400x600/d095451f3c05ce8da8fa1405d01a65ee01d6f86b.gif",
            "https://64.media.tumblr.com/ab2b17374882bb0778dbceb5f5332331/ff1b2ce03354a8e9-bc/s250x400/0302ddd93dccfe8b770563b2c1cd384b3a28987a.gif",
            "https://64.media.tumblr.com/e2620481cc0659e4989471dc27de3f23/4830f3edab6ae05a-37/s400x600/46dda48ee9c9daad9050e8a4977b7a8b50819e42.gif",
            "https://64.media.tumblr.com/5174eb76945124e0845575d305eb3714/4830f3edab6ae05a-d0/s400x600/dd961ccf6615ffdd8ec964e1a16951f2bd8a9f1e.gif",
            "https://64.media.tumblr.com/eb3f5ecb8627b09a67b5756c9d288777/4830f3edab6ae05a-cf/s400x600/7baf4f8d45aae1dea5ca0856dd59c7dde3304594.gif",
            "https://64.media.tumblr.com/da7655f0229fce16f13fad0889387986/4830f3edab6ae05a-55/s400x600/a8d701e1ef8a937f06cc523270541dbc73514362.gif",
            "https://64.media.tumblr.com/e67110a6971ecc9c7457445578ae2174/be2c5dc1e5c569be-c3/s540x810/635af669560e31f9a920e14614a240d5e568c540.gif",
            "https://64.media.tumblr.com/9101ad07ad7f8b43efff056acbfe8619/be2c5dc1e5c569be-d6/s540x810/d8e2034a06a0c441dfd1a68ea05c3340e3a92b1a.gif",
            "https://64.media.tumblr.com/e1a33202169d4e18f3fefb891251f682/be2c5dc1e5c569be-34/s540x810/4d5b5b1d6a8f4d041d3d9ec805c2e6a2e0f4a1f9.gif"]

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
            "https://giphy.com/gifs/nctsmtown-nct-127-u-Cobs8ZH3yAGTwVHS0h",
            "https://64.media.tumblr.com/18d05f7da571a0b27b2a7afac22177f5/302e44f76695bfda-0c/s540x810/bc7f7a67ca9e0ed0785799e18d4a4304b22dbc51.gif",
            "https://64.media.tumblr.com/cb220315360ff0c0440d5ad6a6a8404b/302e44f76695bfda-8c/s500x750/015e2787f19361223c8e97b12b350f923767a226.gif",
            "https://64.media.tumblr.com/610cb8e0b1335b19825b9d19dfabec55/704b1d967a24ffdc-01/s540x810/702b6b88d5e0fa76e4175ddf6ae501257022c508.gif",
            "https://64.media.tumblr.com/3fb4f0eb5292f9d84164f5122accd764/3e06e7f2aa66ccb0-d4/s400x600/c84e1ef324e46d78f9011864c0e1d269dca3ab09.gif",
            "https://64.media.tumblr.com/cdff03dd7840e13517bfee83ca15fcea/3e06e7f2aa66ccb0-54/s400x600/28b76afc88d852ebea1fd22c787c18615faa6a6f.gif"]

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
            "https://64.media.tumblr.com/f4e1f9413df13112e193bc467baedd02/1b91aaec34336370-e9/s400x600/7f9c7777505523ed210be2365175b98288ed8a33.gif",
            "https://64.media.tumblr.com/62feaf9dee731d8a9c49ee7868addfe8/704b1d967a24ffdc-79/s540x810/515c2d271e4ce689b99fc7cbefa8dd2ec79b7f81.gif",
            "https://64.media.tumblr.com/fff46228b7dbc8fa7b549c785f1011a9/9bfb580552b2eb77-6a/s250x400/3d89fc486ec9cc3e03f644e8cdf7376fd77984a3.gif",
            "https://64.media.tumblr.com/39ec8a8e5025b8b8329296b240c44beb/f786477bd998a2a8-61/s540x810/14533301752c8dac8ef62a9f69a646ae54320c8c.gif",
            "https://64.media.tumblr.com/2658a999e225462db729033e7115b21c/529f30fb9c7eb309-ea/s540x810/4d11a841afb5b45f1c3b96c745b988146fdc24ba.gif"]

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
            "https://c.tenor.com/qYLYCx2IT3gAAAAM/nct-nct127.gif",
            "https://64.media.tumblr.com/3f2e07066f63d3f4f2a56dc676175ae5/20e9a4bf77c745b4-b8/s400x600/4a819e84ca48d3f1a971694f8323eb3014fbf74f.gif",
            "https://64.media.tumblr.com/bede646df8d51af5061f1fc87ef8b4d1/20e9a4bf77c745b4-e4/s400x600/ec4efd45edef10040cda8a9ea8385f51b158839a.gif",
            "https://64.media.tumblr.com/5cc75831340c940f004eb805fdee57bc/fe69f2ef9fe8b249-16/s250x400/f7ddd32e50692702830938c0256f7371f4e4aadb.gif",
            "https://64.media.tumblr.com/267a9a778a3932859ecda3909c0a6f93/fe69f2ef9fe8b249-e0/s250x400/f6a62edd4f80b80d5e2b765038413c7809308b6f.gif",
            "https://64.media.tumblr.com/69f158f24bc319dba32c969277fc2e9d/fe69f2ef9fe8b249-63/s250x400/982ce459488b971e780d99186b4a96ac58b5633e.gif",
            "https://64.media.tumblr.com/37ee62eb73e64edd99e107fda197729b/fe69f2ef9fe8b249-80/s250x400/a11eca79f830058c395654612e1a004eb975a60a.gif",
            "https://64.media.tumblr.com/d827e122a4b933d2d3bb5e1adadb27bc/3b6dceff36b2429c-6a/s250x400/aea4ad61bfcf3f9a658624891b0b88b16c3642c7.gif",
            "https://64.media.tumblr.com/25d801e59123f67dda675f8ae6e9736f/3b6dceff36b2429c-ee/s250x400/3f614300d355086d50374a3380cae356e3c86726.gif",
            "https://64.media.tumblr.com/8bc1305ae9f1b9eff2e8a3cac40a3575/3b6dceff36b2429c-7b/s250x400/c2a09bc7f8ac4f8677acd3bd58f3bcd7bd8478ec.gif",
            "https://64.media.tumblr.com/148f260f83dc0e7061741da2c99243e5/873914b9bbf08a35-5d/s400x600/032d059bb90585de9bd379c470eb9b80d9746d54.gif",
            "https://64.media.tumblr.com/7c8f03773c243c7e63acd722ed801fbf/873914b9bbf08a35-17/s400x600/820693f724356bfe587b542309be2e0d4d22c92d.gif",
            "https://64.media.tumblr.com/8c56b64184e7910d761333c563c6226d/873914b9bbf08a35-49/s400x600/1734d3908840cacf186a3d5a1aff5acef3e3a1dd.gif",
            "https://64.media.tumblr.com/f1b91f997f1e5a1bb5a4ed0ae0d5f642/f6d444d10f3ebdd6-42/s400x600/6ac2b67a1223b992eb066a295e8761752d80e0fa.gif",
            "https://64.media.tumblr.com/d4e3d149f11615be687bd89b76460399/389bf4ad8827302a-d8/s400x600/5d0b00b215cfe1ee8e839c580408aec43a4c0bdb.gif",
            "https://64.media.tumblr.com/4f7102bc82a9217343b27aa081312ca9/bdc671230d438f6b-87/s250x400/d5dc4df6e16359e55620cc0d99bbc1228161f796.gif",
            "https://64.media.tumblr.com/9ebcb86013b6eb4c39bba0422fa53911/bdc671230d438f6b-26/s250x400/fb6e72ebe2cd607448d6d06c0ebdb74257381fc2.gif",
            "https://64.media.tumblr.com/281d825b12fc578ae877da09cc775b5c/bdc671230d438f6b-40/s250x400/0de5cbb4ae1286e2f853b1d367586318d2f6c8ad.gif",
            "https://64.media.tumblr.com/2987a61f2a1ad0c7f4a21fda209f0b19/bdc671230d438f6b-53/s250x400/a70d4595a36828834fd2599a5bd011c38a742ee0.gif",
            "https://64.media.tumblr.com/6a0098f705a2d9ecb3e05917ad46ef5b/37ce77dcb5acbe7d-c7/s250x400/0a3cf7e8a65bdd7e96352482d65012a7b804c3ff.gif",
            "https://64.media.tumblr.com/64f835d46677a816a8a3b208a50e4543/37ce77dcb5acbe7d-cb/s250x400/e5638ca511d0cc1bde6a78b41308a5317ca11b89.gif",
            "https://64.media.tumblr.com/bdd03a92c64ba2d5eb841fc1936f09b4/37ce77dcb5acbe7d-3a/s250x400/39ab4b956c0bffac748f039a72f2cf6fc577361b.gif",
            "https://64.media.tumblr.com/ee0da69a4884ea663b5db2a38abef019/20e9a4bf77c745b4-aa/s400x600/374f7b4f01838f6ab272b34602495019e08799a8.gif",
            "https://64.media.tumblr.com/7a46de6a2df8d2c3b783c553bd076639/20e9a4bf77c745b4-f1/s400x600/cf9d96547c42895959d32c9bb3d249c3d65b3147.gif"]

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
            "https://64.media.tumblr.com/ef5af9ada1b71a098a09889db3be535e/1b91aaec34336370-c1/s400x600/2856a1cd420106784fab301d24935a44d16a2189.gif",
            "https://64.media.tumblr.com/9e9b7e7d1c846b4e1674b361a66a5c57/389bf4ad8827302a-e1/s400x600/765660c8d06c9330b7f3f50ce6a4fc8cd34d1b70.gif",
            "https://64.media.tumblr.com/b3cb5ccbfbb6e2667a350715801340eb/f8716ca9e730c971-7d/s400x600/8d2105169422ac720a53c147a17e0a4e8fc7d426.gif",
            "https://64.media.tumblr.com/44e34b6328bd035ef4cdebd5869207bf/b94cbb83f7124009-79/s250x400/7d007f1f804a1281eafe7db7f740cacb1c777b42.gif",
            "https://64.media.tumblr.com/a89a59ebf7200d1453b9960eccb4d80a/bf0328acf78b787c-d7/s400x600/cd2fca84e1b54ac5c33d042625e524fba044f00a.gif",
            "https://64.media.tumblr.com/bb7edbb80157357e146d279ca3d49458/a2e23c697af474db-13/s400x600/763129f262425dbef0478bee5f4438c71608a79c.gif",
            "https://64.media.tumblr.com/15e7dd090930bf1b672e10f59005ce52/a2e23c697af474db-0a/s400x600/f3b256e00f517c5c991dd818bd24d0d1fd9e72fd.gif",
            "https://64.media.tumblr.com/0e7b04be4bb895a3811c9931cd7c668e/da04a65a21f707b0-03/s400x600/6584ae0e95fd6fd3b7179105ce28a17349f473aa.gif",
            "https://64.media.tumblr.com/76a84e6abba09d01eb2487da54ba1f6a/75e59149a952d6c5-0f/s250x400/eee1a2d7c9e963c97e128b7faf98f26737ecae28.gif",
            "https://64.media.tumblr.com/caf8b74e195d04f2083d01eee82929a7/09e1951a548de4e0-7c/s400x600/e141934e7275fc09e07a9a779be739636c5ca055.gif",
            "https://64.media.tumblr.com/7fc83782305d0596cfa0d2faed31cab6/edef875913e82f4c-3b/s400x600/962c0c7c5235acb3fbd9d1f214699d1f9cbdaa29.gif",
            "https://64.media.tumblr.com/743d06ce0fec612105ceb4502f6b99e2/47c6cdcc3934ee33-1e/s250x400/e2d9aa46134cf1b983ef1804bd52a87f86e65939.gif",
            "https://64.media.tumblr.com/cc0898559d6d278f6a129f28e2278246/d379e2ab2c9bacce-57/s250x400/832aaa61b668ecfd52ebb651da82d379507761b6.gif",
            "https://64.media.tumblr.com/82b7a07593f011acf44335742b3231c6/80375a0644b5df04-05/s400x600/89cec40278d0cadece1927b1ece875905e4f2360.gif",
            "https://64.media.tumblr.com/5d505c03982a3c2bfa399393e8c80c1a/7551b24d0afbbeca-e2/s250x400/843dae26448a35b01d897cd05301f129d7c32ed6.gif",
            "https://64.media.tumblr.com/db6aa76ede6ae73bcf9e199982567956/4431382f21397755-73/s400x600/79f0541e2eafe79842aa75e5b6d3d7bbba4139c3.gif",
            "https://64.media.tumblr.com/4f66cd2767a0d2ab0f3a73210a5b398b/4431382f21397755-7e/s400x600/b86d8c501451fb5a24abd51b71f810edd294d4ae.gif",
            "https://64.media.tumblr.com/06913c74590f9edf64689e7c346fa44b/4431382f21397755-f1/s400x600/5370dd9102fb47aa877e98927b0274f4fed9b0d6.gif"]

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
            "https://64.media.tumblr.com/7570a5f70af01223ccca18a8a56b5043/1b91aaec34336370-6e/s400x600/89e86517efeef3cb251e3eda3d315bccded691c1.gif",
            "https://64.media.tumblr.com/58704975e89931b8140122c71b2bfe23/704b1d967a24ffdc-78/s540x810/f4134dd6f2c1ee2e63d2b1b5ba4a2b80d7671bee.gif"]

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
            "https://64.media.tumblr.com/cec453333b277d85cc3404adcf73adb8/0043511a90fe19f3-d0/s540x810/8e5cac4759758432b1db7d3dd48e98413707a389.gif",
            "https://64.media.tumblr.com/0cca17ff06d0c0971d5c00f8e2f88bdf/302e44f76695bfda-f2/s500x750/ab3890ac761859835f1e07b0f566bcb3d05ccd1d.gif"]

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
            "https://64.media.tumblr.com/36f0bff886d67425bbde4b3d5f38a9ac/bcce55925b8a9da6-78/s400x600/47e03c6969c72adc2a7623bd74d7293cd21e492e.gif",
            "https://64.media.tumblr.com/3c2013c79bc1d4e9fb65375712122025/b7ce461bf040a976-e8/s400x600/508944caace031701a4da86dbbd7e6fd9625f733.gif",
            "https://64.media.tumblr.com/bf24a5dfc969bd0dc54bb660be20a1f0/b7ce461bf040a976-8a/s400x600/efd22e749a6c9a7d416d142a76d91721a463339f.gif",
            "https://64.media.tumblr.com/74d90a5bebee50ee14f747845e98b5ec/06acfb93c16a93df-55/s400x600/041498938ddb3aceffc9b41008b15987ad10e1e9.gif"]

    @commands.command()
    async def nct(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [NCT {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "mark":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Mark :heart:')
            await ctx.send(random.choice(self.bot.nct_mark_gif))
            await ctx.message.delete()
        elif arg == "lucas":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Lucas :heart:')
            await ctx.send(random.choice(self.bot.nct_lucas_gif))
            await ctx.message.delete()
        elif arg == "winwin":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Winwin :heart:')
            await ctx.send(random.choice(self.bot.nct_winwin_gif))
            await ctx.message.delete()
        elif arg == "jaemin":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jaemin :heart: ')
            await ctx.send(random.choice(self.bot.nct_jaemin_gif))
            await ctx.message.delete()
        elif arg == "jaehyun":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jaehyun :heart: ')
            await ctx.send(random.choice(self.bot.nct_jaehyun_gif))
            await ctx.message.delete()
        elif arg == "kun":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Kun :heart: ')
            await ctx.send(random.choice(self.bot.nct_kun_gif))
            await ctx.message.delete()
        elif arg == "ten":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Ten :heart: ')
            await ctx.send(random.choice(self.bot.nct_ten_gif))
            await ctx.message.delete()
        elif arg == "xiaojun":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Xiaojun :heart: ')
            await ctx.send(random.choice(self.bot.nct_xiaojun_gif))
            await ctx.message.delete()
        elif arg == "hendery":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Hendery :heart: ')
            await ctx.send(random.choice(self.bot.nct_hendery_gif))
            await ctx.message.delete()
        elif arg == "yangyang":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yangyang :heart: ')
            await ctx.send(random.choice(self.bot.nct_yangyang_gif))
            await ctx.message.delete()
        elif arg == "taeyong":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Taeyong :heart: ')
            await ctx.send(random.choice(self.bot.nct_taeyong_gif))
            await ctx.message.delete()
        elif arg == "jungwoo":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jungwoo :heart: ')
            await ctx.send(random.choice(self.bot.nct_jungwoo_gif))
            await ctx.message.delete()
        elif arg == "yuta":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yuta :heart: ')
            await ctx.send(random.choice(self.bot.nct_yuta_gif))
            await ctx.message.delete()
        elif arg == "jeno":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jeno :heart: ')
            await ctx.send(random.choice(self.bot.nct_jeno_gif))
            await ctx.message.delete()
        elif arg == "jisung":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jisung :heart: ')
            await ctx.send(random.choice(self.bot.nct_jisung_gif))
            await ctx.message.delete()
        elif arg == "renjun":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Renjun :heart: ')
            await ctx.send(random.choice(self.bot.nct_renjun_gif))
            await ctx.message.delete()
        elif arg == "doyoung":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Doyoung :heart: ')
            await ctx.send(random.choice(self.bot.nct_doyoung_gif))
            await ctx.message.delete()
        elif arg == "haechan":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Haechan :heart: ')
                await ctx.send(random.choice(self.bot.nct_haechan_gif))
                await ctx.message.delete()
        elif arg == "shotaro":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Shotaro :heart: ')
            await ctx.send(random.choice(self.bot.nct_shotaro_gif))
            await ctx.message.delete()
        elif arg == "taeil":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Taeil :heart: ')
            await ctx.send(random.choice(self.bot.nct_taeil_gif))
            await ctx.message.delete()
        elif arg == "johnny":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Johnny :heart: ')
                await ctx.send(random.choice(self.bot.nct_johnny_gif))
                await ctx.message.delete()
        elif arg == "chenle":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chenle :heart: ')
                await ctx.send(random.choice(self.bot.nct_chenle_gif))
                await ctx.message.delete()
        elif arg == "sungchan":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Sungchan :heart:')
                await ctx.send(random.choice(self.bot.nct_sungchan_gif))
                await ctx.message.delete()
        elif arg == "dream":
                await ctx.send(f'<@!{ctx.author.id}> is talking about NCT Dream :heart:')
                await ctx.send(random.choice(self.bot.nct_dream_ot7_gif))
                await ctx.message.delete()
        elif arg == "127":
            await ctx.send(f'<@!{ctx.author.id}> is talking about NCT 127 :heart:')
            await ctx.send(random.choice(self.bot.nct_127_ot9_gif))
            await ctx.message.delete()

    @commands.command()
    async def wayv(self, ctx,):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [WayV] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
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
