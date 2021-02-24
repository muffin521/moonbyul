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
muffin = 488423352206229505
weakado = 259409277482041344
mae = 492769416610840586
kate = 382715972722753536

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
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-i499c3xkvwFtiofT6g"]

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
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-VS8myHwaL43gIiz2vs"]

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
            "https://giphy.com/gifs/nctsmtown-kpop-nct-172-cXGwNxRJHkbiZTWH3R"]

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
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-tUBSmzCGLGfAYynRTu"]

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
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-p8KfgL5e1bkwnaSHx1"]

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
            "https://giphy.com/gifs/nctsmtown-kpop-nct-172-qwrqKiFGiBC5BNQVDx"]

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
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-UcDvbvOQcoVAShlctP"]

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
            "https://giphy.com/gifs/nctsmtown-nct-nct127-127-3ddsPMDOgK7PY6p0qS"]

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
            "https://giphy.com/gifs/nctsmtown-nct-nct127-127-i1HeG0kGBCRCGFPVfq"]

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
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-7y8gFfTLNbBjtxkHgg"]

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
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-dxCXXifRkjIM1ur925"]

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
            "https://giphy.com/gifs/Fanfickk-nct-dream-haechan-Kd5q0RMlTj2nNfvvIt"]

        self.bot.nct_shotaro_gif = ["https://data.whicdn.com/images/351628694/original.gif",
            "https://64.media.tumblr.com/6edafc4e3260369fc2985fba82b15445/28949b3c12da530c-06/s540x810/052ac6091eb548bd42872edc47493087d9effd66.gif",
            "https://i.pinimg.com/originals/98/15/81/9815815163d0c1e0e2684b8dbf0b350a.gif",
            "https://64.media.tumblr.com/ed525c8f42475f3a1cabc6d2415a20e1/16d2020971cda3d1-e0/s400x600/177a2c6c491972336440d4adc7c7e0e56bb7fb6b.gif",
            "https://i.pinimg.com/originals/ff/70/ec/ff70ec397a9742db8f3a3bb899c3b862.gif",
            "https://data.whicdn.com/images/351456132/original.gif",
            "https://lh3.googleusercontent.com/-oPCo2mOsMNA/X2odftlLkWI/AAAAAAABIHU/WGyRoYVSc4YaMtYEp06likNYkmlvjatxwCLcBGAsYHQ/s16000/download%2B%25281%2529.gif",
            "https://64.media.tumblr.com/479ed0fb7b0e877859761b7b4abb316e/e518acab0afea2ee-01/s250x400/1699ca4024158bdfc711a9d915558ece1c103393.gif",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-LIBd1nfU9PJJnEOdBT",
            "https://giphy.com/gifs/nctsmtown-kpop-nct-nct127-C0LpuEm9SldsMhfrOp"]

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
            "https://giphy.com/gifs/nctsmtown-nct-127-nct127-H7f1WyUAYUEkB32rqr"]

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
            "https://giphy.com/gifs/nctsmtown-kpop-nct-resonance-p5FXsQOzRoVgU2SmkA"]

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
            "https://giphy.com/gifs/nctsmtown-kpop-nct-172-HRUXMoxwcIGKQp2etr"]

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
            "https://giphy.com/gifs/Ehd4rd16bnR3fiHh50"]

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
            "https://tenor.com/view/wayv-kpop-boy-group-cute-handsome-gif-17691644"]

    @commands.command()
    async def nct(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [NCT {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "mark":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Mark :heart: ')
                    await ctx.send(random.choice(self.bot.nct_mark_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Mark :heart:')
                await ctx.send(random.choice(self.bot.nct_mark_gif))
                await ctx.message.delete()
        elif arg == "lucas":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{kate}>, <@!{ctx.author.id}> is talking about Lucas :heart: ')
                    await ctx.send(random.choice(self.bot.nct_lucas_gif))
                    await ctx.message.delete()
                else:
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
        await channel.send(f"`{current_time} | USED COMMAND [WAYV] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about WAYV :heart:')
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
