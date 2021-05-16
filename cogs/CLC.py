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

class CLC(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.clc_yeeun_gif = ["https://tenor.com/view/yeeun-clc-gif-19116003",
            "https://tenor.com/view/yeeun-clc-gif-19116004",
            "https://tenor.com/view/yeeun-clc-gif-19116007",
            "https://tenor.com/view/yeeun-clc-gif-19116012",
            "https://tenor.com/view/yeeun-clc-bad-girls-jang-gif-13252706",
            "https://tenor.com/view/yeeun-clc-crystal-clear-cute-girl-group-gif-15041212",
            "https://tenor.com/view/clc-yeeun-clc-yeeun-rap-kpop-gif-15340668",
            "https://tenor.com/view/clc-kpop-yeeun-gif-18657579",
            "https://tenor.com/view/yeeun-jang-clc-cute-stare-gif-13329818",
            "https://tenor.com/view/yeeun-jang-yeeun-cute-clc-kpop-gif-17883335",
            "https://tenor.com/view/yeeun-clc-crystal-clear-cute-girl-group-gif-15041189",
            "https://tenor.com/view/yeeun-clc-bad-girls-jang-gif-13252063",
            "https://tenor.com/view/yeeun-jang-clc-flip-hair-gif-13252498",
            "https://tenor.com/view/yeeun-jang-clc-gif-13328477",
            "https://tenor.com/view/jang-ye-eun-selfie-talking-cute-pretty-gif-16653425",
            "https://tenor.com/view/yeeun-jang-yeeun-clc-crystal-clear-girl-group-gif-15041366",
            "https://tenor.com/view/crystal-clear-jang-kpop-yeeun-clc-gif-14859536",
            "https://tenor.com/view/yay-wink-cute-yeeun-clc-gif-14300869",
            "https://tenor.com/view/yeeun-jang-clc-not-yummy-gif-13252749",
            "https://tenor.com/view/crystal-clear-jang-kpop-devil-yeeun-gif-14999392",
            "https://tenor.com/view/chonnasorn-sajakul-yeeun-clc-sorn-gif-13252160",
            "https://64.media.tumblr.com/6cc3923c8ca7c746a975b1a6e824b699/tumblr_pxoa50mSnk1xmrigxo3_250.gif",
            "https://64.media.tumblr.com/6231613cc2c14240698dc03c4fa8d9bd/tumblr_pxo8a5zhMZ1xmrigxo1_250.gif",
            "https://64.media.tumblr.com/a092760b41ebc5859351f68a4121b0c9/tumblr_p4lhncBYqR1vx1psgo3_250.gif",
            "https://64.media.tumblr.com/d226ef4b0d79f14ce26620b3d578f459/d94ceaf10a2cb394-54/s400x600/2606f1f60966652acdc1d008a9ac79746451c065.gif",
            "https://tenor.com/view/yeeun-clc-crystal-clear-cute-girl-group-gif-15041212",
            "https://tenor.com/view/yeeun-clc-crystal-clear-cute-kpop-gif-15041179",
            "https://tenor.com/view/yeeun-clc-crystal-clear-cute-girl-group-gif-15041199",
            "https://tenor.com/view/crystal-clear-yeeun-korean-cute-gif-16805024",
            "https://64.media.tumblr.com/ecf4e9acad7a41ca05d3e5a89cf370ed/9e1729afe5c39c45-81/s540x810/e405171f8b4baa8f38cca1af7d53fb0163351697.gif",
            "https://64.media.tumblr.com/b5be13499a9eafb485ea2822884ec44a/9e1729afe5c39c45-7a/s540x810/ce08c2a98e34d117686e738da3adeb61360391a2.gif",
            "https://64.media.tumblr.com/077c2b90f2403cd62d0ab7ebcd8a7eb9/9e1729afe5c39c45-d7/s540x810/2c9588a65980871c4cd35b46fda82498e8437628.gif",
            "https://64.media.tumblr.com/e63226d1d49e1fc9cc06b78eec8e1a91/tumblr_pzhoppr3J21szf0bzo1_400.gif",
            "https://64.media.tumblr.com/dcc3eb1ba45b5ae32bfefe9e861d039c/tumblr_pzhoppr3J21szf0bzo2_400.gif",
            "https://64.media.tumblr.com/dcc3eb1ba45b5ae32bfefe9e861d039c/tumblr_pzhoppr3J21szf0bzo2_400.gif",
            "https://64.media.tumblr.com/d7aa34482f128afbb722b139b81a9c9b/tumblr_pzhoppr3J21szf0bzo3_400.gif",
            "https://64.media.tumblr.com/7fe7eeabc668d6346d945f0f3946c2f9/tumblr_pwv698ioWK1uv2r7ko2_400.gif",
            "https://64.media.tumblr.com/781bb6def5fdaf6e51ceb10b7ecdfee2/tumblr_pwv698ioWK1uv2r7ko1_400.gif",
            "https://64.media.tumblr.com/7fe7eeabc668d6346d945f0f3946c2f9/tumblr_pwv698ioWK1uv2r7ko2_400.gif",
            "https://64.media.tumblr.com/781bb6def5fdaf6e51ceb10b7ecdfee2/tumblr_pwv698ioWK1uv2r7ko1_400.gif",
            "https://64.media.tumblr.com/c841ffdefd1f178f35698ff582502f7b/tumblr_pxo8a5zhMZ1xmrigxo2_400.gif",
            "https://64.media.tumblr.com/9029995812d21d7bd80aa1325e558bd5/tumblr_pxo8a5zhMZ1xmrigxo3_400.gif",
            "https://64.media.tumblr.com/dd2a2696c374050bb8bee7fe02de2baf/tumblr_pxo8a5zhMZ1xmrigxo4_400.gif",
            "https://64.media.tumblr.com/6231613cc2c14240698dc03c4fa8d9bd/tumblr_pxo8a5zhMZ1xmrigxo1_400.gif",
            "https://64.media.tumblr.com/adf944640f96fa4f6ae6c593a2f33eca/8d61357e3c16284b-f8/s250x400/efe4fb02aed115847431af1f99e9db602ae74a4f.gif",
            "https://64.media.tumblr.com/98f03c88e8967da1d0c9975f61b4d508/8d61357e3c16284b-de/s250x400/9e7f5673559f4b3902a684080085e85469eeff33.gif",
            "https://64.media.tumblr.com/4f88e1fcae3eea736bf190d5380711a9/8d61357e3c16284b-12/s250x400/131f4f4fbaefc853688371f12a8f2dcc8b320189.gif",
            "https://64.media.tumblr.com/49b76f62423512122d2386b37c71bc80/8d61357e3c16284b-51/s250x400/cdb3abcaa86704e9ca580c8713f4cdf53e226318.gif"]

        self.bot.clc_sorn_gif = ["https://tenor.com/bqihb.gif",
            "https://tenor.com/bunmH.gif",
            "https://tenor.com/bunmN.gif",
            "https://tenor.com/view/sorn-clc-gif-18620769",
            "https://tenor.com/view/clcsorn-sorn-clc-gif-18176207",
            "https://tenor.com/view/sorn-clc-gif-18563360",
            "https://64.media.tumblr.com/f2dd1f2bdb800b59e2971c749ae4f16f/tumblr_pm51yog1Qd1wjbytmo2_400.gif",
            "https://64.media.tumblr.com/12b85a509f7f120b172707d81ddb7519/tumblr_pxmjd9A6qD1sk2kqwo2_250.gif",
            "https://64.media.tumblr.com/b1b142aa5b528d42c755684ae616fe15/tumblr_pwe1ykW04l1yoiwkxo2_250.gif",
            "https://64.media.tumblr.com/31cf0d2e805bfaa81ec99ae07639f23c/tumblr_pxhwztNk8j1r7qnpao10_400.gif",
            "https://64.media.tumblr.com/bd15b3b9799ae1cdb647fe482f63ff42/tumblr_pmub54CoEj1vmyrtpo3_r1_400.gif",
            "https://64.media.tumblr.com/06ef8735907d2c2cabd846d88ac97c2f/tumblr_ps9edwdVXW1sk2kqwo2_400.gif",
            "https://64.media.tumblr.com/765e0eb934ff869d20dc349a0be4c474/tumblr_pam2tu9ySc1whlmf0o1_250.gif",
            "https://64.media.tumblr.com/96465f8b2a060af07b04d8f7e6b10cf8/tumblr_po19dnpNne1xp5ff0o2_250.gif",
            "https://64.media.tumblr.com/f1af90c46947fa345bb453b1329a87d2/ea894064fe54c025-b1/s250x400/fd085de6011ad14c9b1d91259c56946c60067470.gif",
            "https://64.media.tumblr.com/b2358d1fc47c9ed4a1606feb5a5899bb/tumblr_pyxb2j5KlF1yvevxlo4_250.gif",
            "https://64.media.tumblr.com/105a94d59771577fe046f492ccaa908d/tumblr_pa46r0AFJK1whlmf0o3_250.gif",
            "https://64.media.tumblr.com/68121afe56373a32f7b5bf2a483a2409/tumblr_p7rihoHKHI1vchkyho2_400.gif",
            "https://64.media.tumblr.com/2e47cc027a05e5d6738ba916d0ab7c18/tumblr_pn916lZKsk1xp5ff0o2_400.gif",
            "https://64.media.tumblr.com/1e55b8379b60496df6e5666e47450dd4/tumblr_pxsv42n0yi1vpomzuo7_250.gif",
            "https://64.media.tumblr.com/f96053e54377ab9b0f23ee5e78a2470b/ed9c43afbac98e03-2d/s250x400/bc1c07b91b13fab7b177978a383f0e71906d4190.gif",
            "https://tenor.com/view/gee-crystal-clear-chonnasorn-sajakul-sorn-mbc-gif-16423580",
            "https://tenor.com/view/clc-crystal-clear-kpop-cute-girl-group-gif-15041318",
            "https://tenor.com/view/mnet-one-step-crystal-clear-gif-15007494",
            "https://tenor.com/view/sorn-clc-chonnasornsajakul-gif-21019513",
            "https://tenor.com/view/sorn-clc-chonnasornsajakul-gif-21019506",
            "https://tenor.com/view/sorn-clc-chonnasornsajkul-gif-21019505",
            "https://tenor.com/view/sorn-clc-chonnasornsajakul-gif-21019504",
            "https://tenor.com/view/sorn-clc-chonnasornsajakul-gif-21019502",
            "https://64.media.tumblr.com/b2358d1fc47c9ed4a1606feb5a5899bb/tumblr_pyxb2j5KlF1yvevxlo4_400.gif",
            "https://64.media.tumblr.com/fe2937ac15d87072472ff392d3a03f17/tumblr_pyxb2j5KlF1yvevxlo2_400.gif",
            "https://64.media.tumblr.com/cf79f09c4cfc16c10b432ef4df1da6d7/tumblr_pxlyy2RZhX1yq4k1ko1_250.gif",
            "https://64.media.tumblr.com/ecc27b643004e2e8a5481f08b6296505/tumblr_pxmjd9A6qD1sk2kqwo3_400.gif",
            "https://64.media.tumblr.com/c8aa9b4065557055b94d54ff97765017/tumblr_pxmjd9A6qD1sk2kqwo4_400.gif",
            "https://64.media.tumblr.com/12b85a509f7f120b172707d81ddb7519/tumblr_pxmjd9A6qD1sk2kqwo2_400.gif"]

        self.bot.clc_eunbin_gif = ["https://tenor.com/RCQt.gif",
            "https://tenor.com/RCSH.gif",
            "https://tenor.com/9gg1.gif",
            "https://tenor.com/view/devil-crystal-clear-mbc-music-core-kwon-eunbin-kpop-gif-15048708",
            "https://64.media.tumblr.com/38badc52c4a790cfc3ece9d2fd974526/tumblr_p3psars9J81rmcvtso8_500.gif",
            "https://64.media.tumblr.com/e2ae729ab6bbe9b75cf35863747b75c5/tumblr_p65flbtGIh1rggxt1o1_540.gif",
            "https://64.media.tumblr.com/8f1dc3086a670f43423c72c266339989/tumblr_p3psars9J81rmcvtso5_500.gif",
            "https://64.media.tumblr.com/4989ce65929daba9a241271952684a7e/21b83549f399204e-7f/s400x600/5aa5e2bab63dc5ca1e08b7f91d730ab32833dd31.gif",
            "https://64.media.tumblr.com/c32f2a3e88a4c330dcdf2bab852c420f/b2364dcdce157e24-f1/s400x600/d53dc342b4d1c7559f84204b0e5188c16dd144b7.gif",
            "https://64.media.tumblr.com/4e3b7526c2249d9ae8d7a6ddd4e835b2/7074e2f0bb2effbe-25/s540x810/ae2f964bac67c2829a530880953dce4fcf0097b0.gif",
            "https://64.media.tumblr.com/3604d9f2331ca9848a96a10bb5ba760c/tumblr_ps6qajFaOa1xp5ff0o2_400.gif",
            "https://64.media.tumblr.com/8eed5aee1150c7a381fca29e4694dfe8/tumblr_pxw1uaEzZW1yul0bxo1_400.gif",
            "https://64.media.tumblr.com/c707989ee6536941d8f941dc9ed8a176/tumblr_pxekelIibg1u1fc83o3_r1_540.gif",
            "https://64.media.tumblr.com/17d9bd161fd1898b4c1774902d170e2e/tumblr_pmm07eWuU71vdiozeo3_400.gif",
            "https://64.media.tumblr.com/28a75291bfdbba0f98cbaeeb9012204b/tumblr_pxeltsZNhD1wjbytmo3_400.gif",
            "https://64.media.tumblr.com/46a748fbe3dc5e59f927c89ea848ca08/tumblr_p3j4ncW3NM1vx1psgo4_400.gif",
            "https://64.media.tumblr.com/193b1ba9f5f0d122c6fc7fa5cc06a9d6/tumblr_oxgzwshBjK1w8h4f6o2_250.gif",
            "https://64.media.tumblr.com/39aedea98cc4aed4b85e0d34e2c01285/tumblr_pxhwztNk8j1r7qnpao2_400.gif",
            "https://64.media.tumblr.com/8eef54c1d5f39dc84df82d5b8e9cdfb7/tumblr_ov8xnma8CR1ssnf1qo3_250.gif",
            "https://64.media.tumblr.com/63fd9572ca41d7606e5f7c54a308688d/tumblr_p5qmlmYbip1wjqhtxo3_250.gif",
            "https://64.media.tumblr.com/40229e940027d537bd3e81912dfb80de/tumblr_pmu3j1TVFO1sk2kqwo3_250.gif",
            "https://64.media.tumblr.com/e64527638845239b918213a9b8b4e434/tumblr_pm51yog1Qd1wjbytmo3_400.gif",
            "https://tenor.com/view/eunbin-kwon-clc-pout-gif-13252512",
            "https://tenor.com/view/kwon-eunbin-eunbin-clc-maknae-cube-entertainment-gif-17697064",
            "https://tenor.com/view/gramarly-clc-eunbin-clc-eunbin-cat-gif-19334577",
            "https://tenor.com/view/clc-eunbin-clc-eunbin-cute-blow-kiss-gif-15044691",
            "https://tenor.com/view/kwon-eunbin-eunbin-clc-maknae-cube-entertainment-gif-17697062",
            "https://64.media.tumblr.com/87f283234c27b1df4b3900f650943a5f/tumblr_pzogdt5lkL1yv59mao1_400.gif",
            "https://64.media.tumblr.com/503440cbba77c1fc1c7b0a3fa7951355/tumblr_pzogdt5lkL1yv59mao3_400.gif"]

        self.bot.clc_yujin_gif = ["https://tenor.com/ba9ol.gif",
            "https://tenor.com/bunmO.gif",
            "https://tenor.com/3LBO.gif",
            "https://tenor.com/view/yujin-yujinclc-yeeun-yeeunclc-clchelicopter-gif-19218780",
            "https://tenor.com/view/yujin-yujinclc-clc-yeeun-sorn-gif-19221197",
            "https://64.media.tumblr.com/eaa5d80a259de2879d31f59c0d0d3b23/tumblr_pmub54CoEj1vmyrtpo4_r1_400.gif",
            "https://64.media.tumblr.com/688a2bc4eee96788b0dd838e613aea27/tumblr_p4jpo85abS1wjbytmo2_400.gif",
            "https://64.media.tumblr.com/9625761d740c831d000478f7ef49bdbb/tumblr_pweoqpbmaf1yoiwkxo3_250.gif",
            "https://64.media.tumblr.com/ccaea787f2db05747e8eee2f840d44d0/tumblr_plud7zwtUu1xzvzwco2_r1_400.gif",
            "https://64.media.tumblr.com/b708cfdfe8875d0f9ff5017127ff6f98/tumblr_pxyingPs931yoiwkxo1_250.gif",
            "https://64.media.tumblr.com/b4b74676d0fe12e01a3a6e16c26bdfcb/tumblr_pluauuNDn21vxqfkro3_r2_250.gif",
            "https://64.media.tumblr.com/2243b5cf9916c5faacdfcdf15e58e5c0/tumblr_pczsw3pW3j1wmpssyo2_250.gif",
            "https://64.media.tumblr.com/cb46b0313a537ba2ba2e0d961a7d7b44/tumblr_p5spp8ZVry1sy8x5ho4_250.gif",
            "https://64.media.tumblr.com/665cca8dcc08cb218e0fe7b7a137a346/tumblr_py65s2O8MN1yoiwkxo3_250.gif",
            "https://64.media.tumblr.com/b77ac06976e62dff605497cd1aa285e1/tumblr_pxt1n4jjsI1x15lmpo1_250.gif",
            "https://64.media.tumblr.com/024b2b1632a6baf94b2035f8097cadba/tumblr_p5lgeoYpRZ1rdewgpo3_250.gif",
            "https://64.media.tumblr.com/b148960bb825ee4e7af41acccb08ca38/tumblr_pxsv42n0yi1vpomzuo4_250.gif",
            "https://64.media.tumblr.com/482c514c4b181d731643c66481328353/tumblr_plklc0ir041u6zsc1o2_400.gif",
            "https://64.media.tumblr.com/e78215758ef8e4fbaa91bf4511461dad/tumblr_p602drnx7Y1wlu57to2_250.gif",
            "https://64.media.tumblr.com/d1b9a1e7bd470665d75d36961d57d81f/tumblr_pnkmqrqOFj1xp5ff0o2_250.gif",
            "https://64.media.tumblr.com/0cf1321f073581504ad4015aae68a5f4/e6f25649cbbbc8bb-0c/s250x400/2585c27136e52d158e2e67f05a4ace0bdda3d49c.gif",
            "https://tenor.com/view/clc-yujin-gif-19259495",
            "https://tenor.com/view/devil-crystal-clear-kbs-music-bank-choi-yujin-kpop-gif-15048714",
            "https://tenor.com/view/happy-excited-cute-yujin-clc-gif-14302664",
            "https://tenor.com/view/cute-yujin-clc-hi-wave-gif-13944583",
            "https://64.media.tumblr.com/1158e40ce3dd8ff7056e6f00c3ee9cfb/tumblr_px8bsiXOD31x15lmpo3_400.gif",
            "https://64.media.tumblr.com/b4586a7df9b6d1eb7d100c24268abcbf/tumblr_px8bsiXOD31x15lmpo4_400.gif",
            "https://64.media.tumblr.com/72851b3b47eb586ec7b403e8edc7fe59/tumblr_px8bsiXOD31x15lmpo1_400.gif",
            "https://64.media.tumblr.com/a971d7759b9d83d8ff498c97756844bd/tumblr_px8bsiXOD31x15lmpo2_400.gif",
            "https://64.media.tumblr.com/a7e6a5ce5dd832ff5f799a84fb2faa20/tumblr_py65s2O8MN1yoiwkxo4_400.gif",
            "https://64.media.tumblr.com/665cca8dcc08cb218e0fe7b7a137a346/tumblr_py65s2O8MN1yoiwkxo3_400.gif",
            "https://64.media.tumblr.com/d06e61f7b4d5256fa14ca983e960e19a/tumblr_py65s2O8MN1yoiwkxo2_400.gif",
            "https://64.media.tumblr.com/bb41d0dce753eea8622b267780ccd8ce/tumblr_py65s2O8MN1yoiwkxo1_400.gif"]

        self.bot.clc_seunghee_gif = ["https://tenor.com/view/crystal-clear-%ec%98%a4-%ec%94%a8%ec%97%98%ec%94%a8-kpop-%ec%98%a4%ec%8a%b9%ed%9d%ac-gif-17069531",
            "https://tenor.com/view/crystal-clear-kpop-phone-devil-gif-14977696",
            "https://tenor.com/view/eyebrow-kpop-bangs-clc-oh-gif-14148382",
            "https://tenor.com/view/oh-seunghee-clc-gif-13251990",
            "https://64.media.tumblr.com/b7d9121ebdc9531df21a2891a96abd38/tumblr_okndb2vhCG1uz2i8ro1_r1_400.gif",
            "https://64.media.tumblr.com/c377460240895e38c7e09c71039afc00/tumblr_ok6urxWOMg1sq9iy3o2_250.gif",
            "https://64.media.tumblr.com/16ce20d80680b4178b760b66892f7bee/tumblr_pmub54CoEj1vmyrtpo7_r1_400.gif",
            "https://64.media.tumblr.com/b8f0b4513a2cd8415aeb2a11f8f59293/tumblr_p4jpo85abS1wjbytmo4_400.gif",
            "https://64.media.tumblr.com/e866a2021c9981ac5dddc81d58aca98d/tumblr_ps9y30HNfD1uy7qvvo1_400.gif",
            "https://64.media.tumblr.com/73d7d0aa9a48aa026c17fe8210f96e73/tumblr_p4q0ahLeJd1rdd5fxo3_250.gif",
            "https://64.media.tumblr.com/efb269b17a3789823a78eb4aef67666c/tumblr_plud7zwtUu1xzvzwco1_r1_400.gif",
            "https://64.media.tumblr.com/5104c3ef2a61134d97de847905657a9e/tumblr_pmdhdkLDmg1uk1uhco1_250.gif",
            "https://64.media.tumblr.com/f391c0f3d59d8261b7ea0c4f8f8fdee4/tumblr_pmdhdkLDmg1uk1uhco2_250.gif",
            "https://64.media.tumblr.com/289beeb5c2692e2e2e7ff5ff83a623cc/tumblr_ps9f5puaP51wjbytmo2_400.gif",
            "https://64.media.tumblr.com/9337658ec8557603c7effd7349fb6c6a/tumblr_pmr8bcF45o1shf90so1_r1_250.gif",
            "https://64.media.tumblr.com/c83adacc958440727fa958e9bd8e02a5/tumblr_pluehnyZie1rov828o5_r1_400.gif",
            "https://64.media.tumblr.com/df001812cf3c540ce9ba59d47624df89/tumblr_peyliod5au1x15lmpo1_250.gif",
            "https://64.media.tumblr.com/272b5aa323e3a26a9b797aa8f9747ada/tumblr_pxsv42n0yi1vpomzuo3_250.gif",
            "https://64.media.tumblr.com/d67ebedd45b6fa8c4cd867626cb6a74f/tumblr_pm537rDTD81vuefjyo1_400.gif",
            "https://64.media.tumblr.com/8d5a80a33ab716f5dd4cc1af1c5fa5e9/tumblr_pn571j5Psk1xp5ff0o1_250.gif",
            "https://64.media.tumblr.com/c8a66404c08bcec1ea32134165067b46/tumblr_psp82zMhcB1s2vcg0o1_250.gif",
            "https://tenor.com/view/crystal-clear-kpop-oh-clc-gif-19119529",
            "https://tenor.com/view/crystal-clear-kpop-devil-clc-oh-seunghee-gif-15048706",
            "https://tenor.com/view/crystal-clear-%EC%98%A4-%EC%94%A8%EC%97%98%EC%94%A8-kpop-%EC%98%A4%EC%8A%B9%ED%9D%AC-gif-17069530",
            "https://tenor.com/view/crystal-clear-helicopter-kpop-oh-gif-18336145"]

        self.bot.clc_seungyeon_gif = ["https://tenor.com/view/seungyeon-clc-please-begging-gif-13944535",
            "https://tenor.com/view/seungyeon-chang-clc-gif-13252414",
            "https://tenor.com/view/seungyeon-chang-clc-hobgoblin-pretty-gif-13252470",
            "https://tenor.com/view/black-dress-seungyeon-chang-clc-gif-13251952",
            "https://tenor.com/view/seungyeon-chang-clc-gif-13252136",
            "https://64.media.tumblr.com/ef3a76e0c1eecb0d1231a3be5e596690/tumblr_px48uiArt01s2vcg0o4_r1_250.gif",
            "https://64.media.tumblr.com/418be3e4026f2c4ed3eb795b0b6eca00/tumblr_px48uiArt01s2vcg0o2_r1_250.gif",
            "https://64.media.tumblr.com/f3abdd65019520a9dc4e0e169d75cee6/tumblr_pxeltsZNhD1wjbytmo6_400.gif",
            "https://64.media.tumblr.com/8540a6ddc8f3caf91a82c792cd973b5c/tumblr_pmq7m5S5RZ1vjco6so1_250.gif",
            "https://64.media.tumblr.com/ddcdfb2b02fa147f37da41a618eb9acf/tumblr_pnlyt9KBXv1uk1uhco3_250.gif",
            "https://64.media.tumblr.com/122994cc7672124e8c20d62d38ad01e7/tumblr_psqpegp2881u7licjo4_250.gif",
            "https://64.media.tumblr.com/45922e0c00f1653310d87538f48b1f8d/62f9eae17fe7a162-57/s250x400/c9dc81f97a19f78652b7d06fafde8014bfd67793.gif",
            "https://64.media.tumblr.com/25a41cab30e2b88ef498b80d2acfffeb/tumblr_pp3ls8AZH01xp5ff0o2_250.gif",
            "https://64.media.tumblr.com/4258b7712ee848e16b44337da8c9a757/7cbeb6aa13642b42-34/s250x400/1efad9186ce73e04e6bf787bd32dc76a91f2e1f3.gif",
            "https://64.media.tumblr.com/39ce390dc3702cf1025aa8be23b36731/bf198219becc4803-14/s400x600/706c7e26fdb17a917c61ac7a2ca0681459b0a6c4.gif",
            "https://64.media.tumblr.com/a030543a112b3809ed534ae87fabc3aa/tumblr_pynk1otZgU1uk0y4po3_250.gif",
            "https://64.media.tumblr.com/19a3bd9019b76922e64341f020b09a9a/tumblr_pxhwztNk8j1r7qnpao8_400.gif",
            "https://64.media.tumblr.com/6694c6da738d482bf301f322bb15ed11/66e088193f5b889d-6e/s400x600/506dbced8c6240c96761d581b8f236fd0a3519c6.gif",
            "https://64.media.tumblr.com/88813d3a17388c59540443c738d58486/tumblr_p4jpo85abS1wjbytmo1_400.gif",
            "https://64.media.tumblr.com/1ac559a282c8b480c35c4c1ca451c7f9/tumblr_pkbhq9IUzY1vpomzuo10_r1_400.gif",
            "https://64.media.tumblr.com/b58da77e1dfb1818c5658e3ac8dcbd40/tumblr_pm0zqly4gY1vpomzuo2_400.gif",
            "https://64.media.tumblr.com/cae2fd80dccdcae681066aa11177f948/9142621037b7fd37-dc/s400x600/f418b215973710566a639da762b40270d25c4dc1.gif",
            "https://tenor.com/view/jang-seungyeon-clc-%EC%94%A8%EC%97%98%EC%94%A8-cute-gif-14155127",
            "https://tenor.com/view/crystal-clear-seungyeon-kpop-chang-devil-gif-14985227",
            "https://tenor.com/view/clc-kpop-ccg-seunyeon-chang-seungyeon-gif-17814175",
            "https://64.media.tumblr.com/a030543a112b3809ed534ae87fabc3aa/tumblr_pynk1otZgU1uk0y4po3_400.gif",
            "https://64.media.tumblr.com/8eddae0838f72a70f0a698c7200801bc/tumblr_pynk1otZgU1uk0y4po4_400.gif",
            "https://64.media.tumblr.com/8f7e2d3744f523d246872942f6cae8c4/tumblr_pynk1otZgU1uk0y4po5_400.gif",
            "https://64.media.tumblr.com/1d0680c3b188f6ff8b2e078f9040ea14/tumblr_pynk1otZgU1uk0y4po2_400.gif",
            "https://64.media.tumblr.com/40ca2eb0f58cdeb1dedc577960017c21/tumblr_pynk1otZgU1uk0y4po6_400.gif"]

        self.bot.clc_elkie_gif = ["https://tenor.com/view/puppy-dog-elkie-clc-gif-13944542",
            "https://tenor.com/view/elkie-singer-clc-gif-18154058",
            "https://tenor.com/view/chong-tingyan-crystal-clear-elkie-chong-kpop-devil-gif-15036131",
            "https://tenor.com/view/chong-tingyan-elkie-clc-come-here-gif-13252022",
            "https://tenor.com/view/chong-tingyan-elkie-clc-hi-gif-13252481",
            "https://64.media.tumblr.com/7aaae3dd2e8940b419c6f5b124b5b506/tumblr_pxeltsZNhD1wjbytmo2_400.gif",
            "https://64.media.tumblr.com/ac8019058ef37c6ec4a360c88bcf8a95/tumblr_p4jpo85abS1wjbytmo3_400.gif",
            "https://64.media.tumblr.com/e2147e325f16bd5e25f4ade708265824/tumblr_ps9gddOZd71ui9s1qo7_r1_400.gif",
            "https://64.media.tumblr.com/1282d22ebc23143a67ae3b6cb465dbeb/tumblr_peqoleYFMo1w6okd3o2_250.gif",
            "https://64.media.tumblr.com/a9106d86985f6274c919d951a4e37194/tumblr_pj4y23KpqB1xt8vh9o1_250.gif",
            "https://64.media.tumblr.com/45693a69bc6b9f2c69666510786f0411/tumblr_pmahpgmkTg1u6zsc1o2_400.gif",
            "https://64.media.tumblr.com/9c89ad45063bd08a30339b4556a25e44/tumblr_pxx4qi0Dew1uk0y4po2_250.gif",
            "https://64.media.tumblr.com/790b873abb091ef6e74cf1303e11c283/tumblr_pnip7slL4h1sk2kqwo2_250.gif",
            "https://64.media.tumblr.com/cfbf31fea72b7ba0286f7a05bbc4cc4b/tumblr_pj3zye7T3I1w6okd3o1_250.gif",
            "https://64.media.tumblr.com/aa80e2527eca9301cad0e7179d094f2e/tumblr_pj6za3rEsA1vpomzuo1_400.gif",
            "https://64.media.tumblr.com/e03ac29e43b1312584271ce9d5b4f6bd/tumblr_pnip7slL4h1sk2kqwo3_250.gif",
            "https://64.media.tumblr.com/ce5f6f75f9fcbc5445fa881e6c58c56a/tumblr_p4p83mggxv1sy8x5ho2_250.gif",
            "https://64.media.tumblr.com/1048f5c7e940e4bb88c5e3189366987e/tumblr_p4o2jvKt8H1w6ly9lo1_250.gif",
            "https://64.media.tumblr.com/1ccd80dcad19d6a5f96ef84fbe442c03/tumblr_pxsv42n0yi1vpomzuo6_250.gif",
            "https://64.media.tumblr.com/547e5232236f5df6a7b4d6784ee21505/6139f1f50fe78efb-88/s250x400/b83aafa021ad46a1c952da11ec96ca47d86e8ce7.gif",
            "https://64.media.tumblr.com/d509ccedee6b9bd80c863564b9e71745/daddcdc6015afd06-0d/s400x600/b1fe8bf9d18a709b92d03c6f32d672295e1b3f01.gif",
            "https://64.media.tumblr.com/ebbb9c156381b46521c289f6a29c4348/tumblr_pin4qmE6PB1xrv0wso4_400.gif",
            "https://tenor.com/view/clc-kpop-elkie-ending-fairy-gif-18657577",
            "https://tenor.com/view/elkie-clc-gif-18563342",
            "https://tenor.com/view/chong-tingyan-elkie-clc-hobgoblin-gif-13252289",
            "https://tenor.com/view/clc-elkie-hungry-eating-gif-13944518",
            "https://tenor.com/view/chong-tingyan-elkie-clc-sad-gif-13252122",
            "https://64.media.tumblr.com/8277c1e3c69eb48e7ff9565915bd821e/6139f1f50fe78efb-e2/s400x600/19448fc29a0719e87a56819dd236e9c492bd763d.gif",
            "https://64.media.tumblr.com/a0b0f509d3dbad3ca51a7b4d8ba3c80c/6139f1f50fe78efb-07/s400x600/f64b7f230a1d8fb18030913e61533ebc98658d45.gif",
            "https://64.media.tumblr.com/3cb040f3dcee563861302f835b09ec32/6139f1f50fe78efb-16/s400x600/ffe1d6104fb3d08de9f01f9cb7ab307b067ee56c.gif",
            "https://64.media.tumblr.com/547e5232236f5df6a7b4d6784ee21505/6139f1f50fe78efb-88/s400x600/f47b24bf3c319990e2e7caf6878a134537d1546f.gif",
            "https://64.media.tumblr.com/8cf016ce25318797f331f33438f3d2dc/tumblr_pz2deoO7I11viv1xyo2_400.gif",
            "https://64.media.tumblr.com/16644aa08ac8bbacf6e4c82d0f543d16/tumblr_pz2deoO7I11viv1xyo1_400.gif",
            "https://64.media.tumblr.com/fb73d83cd75dc6d127d43cde08be56dd/tumblr_py7f7imUoF1yvbw14o3_400.gif",
            "https://64.media.tumblr.com/1853f993f222a3de02e076a78ffbc4b6/tumblr_py7f7imUoF1yvbw14o4_400.gif",
            "https://64.media.tumblr.com/80bda85ffb99aeb58f53db266c12c39c/tumblr_py7f7imUoF1yvbw14o1_400.gif",
            "https://64.media.tumblr.com/ccfb5bc0495e1c78cb8aa4cd2b61e7a6/tumblr_py7f7imUoF1yvbw14o2_400.gif",
            "https://64.media.tumblr.com/e41b13636b9c983e0bc28c0f67ad4f65/tumblr_pxl58cbluh1whhy97o1_400.gif",
            "https://64.media.tumblr.com/aed5cca405a0bd113c32402b86c52deb/tumblr_pxl58cbluh1whhy97o2_400.gif",
            "https://64.media.tumblr.com/dc3a374c36ac6a2828cf5730c2f1aad1/tumblr_pxl58cbluh1whhy97o3_400.gif",
            "https://64.media.tumblr.com/a242630a329db60d2e2f785e4dcabf82/tumblr_pxl58cbluh1whhy97o4_400.gif"]

    @commands.command()
    async def clc(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [CLC {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "yeeun":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yeeun :heart:')
            await ctx.send(random.choice(self.bot.clc_yeeun_gif))
            await ctx.message.delete()
        elif arg == "sorn":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Sorn :heart:')
            await ctx.send(random.choice(self.bot.clc_sorn_gif))
            await ctx.message.delete()
        elif arg == "eunbin":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Eunbin :heart:')
            await ctx.send(random.choice(self.bot.clc_eunbin_gif))
            await ctx.message.delete()
        elif arg == "yujin":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yujin :heart:')
            await ctx.send(random.choice(self.bot.clc_yujin_gif))
            await ctx.message.delete()
        elif arg == "seunghee":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Seunghee :heart:')
            await ctx.send(random.choice(self.bot.clc_seunghee_gif))
            await ctx.message.delete()
        elif arg == "seungyeon":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Seungyeon :heart:')
            await ctx.send(random.choice(self.bot.clc_seungyeon_gif))
            await ctx.message.delete()
        elif arg == "elkie":
            await ctx.send(f'<@!{ctx.author.id}> is talking about Elkie :heart:')
            await ctx.send(random.choice(self.bot.clc_elkie_gif))
            await ctx.message.delete()

def setup(client):
    client.add_cog(CLC(client))