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
k8 = 573974040679809044
mae = 492769416610840586
rith = 346724857725059075

class aespaPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.giselle_gif = ["https://cdn.discordapp.com/attachments/771238115255255060/781338667973214208/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338668513886208/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338669524975616/image2.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338670694531072/image3.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338671202304087/image4.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338671714271282/image5.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338672481173514/image6.gif",
            "https://gfycat.com/badtepidhyracotherium",
            "https://gfycat.com/adeptwellgroomedhorse",
            "https://gfycat.com/thankfulmammothamericanindianhorse",
            "https://gfycat.com/craftythinibex",
            "https://gfycat.com/knobbyimpressionablefennecfox",
            "https://gfycat.com/imaginaryoldfashionedbrahmancow",
            "https://gfycat.com/aridenchantingegret",
            "https://gfycat.com/imperfectthoroughladybug",
            "https://gfycat.com/periodicillegaleasternglasslizard",
            "https://gfycat.com/unlawfulshamefulbabirusa",
            "https://gfycat.com/likelyreadykinkajou",
            "https://gfycat.com/livelybigheartedamericantoad",
            "https://gfycat.com/specificinfatuateddikkops",
            "https://gfycat.com/wickedgrizzledchrysomelid",
            "https://gfycat.com/thatnecessarycolt",
            "https://gfycat.com/defenselesseverlastingguppy",
            "https://gfycat.com/gentledecimalgalapagosdove",
            "https://gfycat.com/untriedblankdoe",
            "https://gfycat.com/lankyfatherlyamericanredsquirrel",
            "https://gfycat.com/enragedlazycowrie",
            "https://gfycat.com/disguisedcreamykiwi",
            "https://gfycat.com/scornfulequalharlequinbug",
            "https://gfycat.com/nervouseasygoingandeancondor",
            "https://gfycat.com/weehideousaddax",
            "https://gfycat.com/warmheartedrequiredcirriped",
            "https://gfycat.com/fancytalkativefairyfly",
            "https://gfycat.com/unripegraciousivorygull-giselle-aespa",
            "https://gfycat.com/badtepidhyracotherium-giselle-aespa",
            "https://gfycat.com/blissfulcleankoi-giselle-aespa",
            "https://gfycat.com/forsakensophisticatedacornwoodpecker-aespa-giselle-black-mamba-girl-group-kpop-aeri",
            "https://gfycat.com/violetpointlesscolt-giselle-aespa",
            "https://gfycat.com/samesoggyaddax-giselle-aespa",
            "https://gfycat.com/yearlyfemininelemming-giselle-aespa",
            "https://gfycat.com/bewitchedmediocreindianelephant",
            "https://gfycat.com/thisshabbyhumpbackwhale",
            "https://gfycat.com/immediateyellowindianrockpython",
            "https://gfycat.com/likelyscarydormouse",
            "https://gfycat.com/goodnaturedimmensecentipede",
            "https://64.media.tumblr.com/9d55f22b43358c3b207b66db4b4ccaa9/2a21d750b4ec58ee-91/s400x600/315191bfd8a58d571268d08a66e100c2313c0787.gif",
            "https://64.media.tumblr.com/3d599adaf041a835d8391570c3abd95f/2a21d750b4ec58ee-0a/s400x600/a97ed2e0ca6fdb95436aa87a3ddeecf8917e9d6d.gif",
            "https://64.media.tumblr.com/f43a3f62bda5490a73efdaa77044ff7e/2a21d750b4ec58ee-8a/s400x600/45d281390322ecb2d487822629307c3fa4422aae.gif",
            "https://64.media.tumblr.com/f0c0fb971922df358bf46f56b4e05e4b/2a21d750b4ec58ee-83/s400x600/716f5134ad5cf740722f736c1592991b5d5e387b.gif",
            "https://64.media.tumblr.com/2233c086bdf1c9e95b936b9ca2e94d6a/2a21d750b4ec58ee-15/s400x600/8c987a7464cd9ffff290e8335b5d802a428ed9cc.gif",
            "https://64.media.tumblr.com/271dd99ed59a69ca583289fd81a9f08c/e030f2f6276cf773-cf/s540x810/d234e920a305bfd73b0e2b0ee11f2200c96e373c.gif",
            "https://64.media.tumblr.com/73ff6e8b3b8274ffc35545b495559931/e030f2f6276cf773-52/s540x810/1908d5b36ca0023708d8cbc2531adeedd460d802.gif",
            "https://64.media.tumblr.com/abaf58508fdaf28302fe8ab8397e4e03/e030f2f6276cf773-f6/s540x810/dbbcdc8cc7edf7ab576577f672872020de0d012e.gif",
            "https://64.media.tumblr.com/41285458c13addd210da8adf144154ad/c707d4895d84d26d-14/s540x810/c19ab44b14dacffae0a1128f6e16895f530376f3.gif",
            "https://64.media.tumblr.com/f293432529c04998961284194cc2a5f7/c707d4895d84d26d-bb/s540x810/8c0d391235a9a8a7dfaefcc5dd9bb39919210830.gif",
            "https://64.media.tumblr.com/7d06f7a0440cb10f99d1ff90bd142916/f38a3938477b5163-13/s400x600/7f6d874ef9789a4a78f383706c1618565d2cce4b.gif",
            "https://64.media.tumblr.com/3b3fc196da00138d610ed1d257ddc857/f38a3938477b5163-0f/s400x600/987f5a0b37799d76b7b297fd99bd8094dca80867.gif",
            "https://64.media.tumblr.com/20a2fe93d04090df0eeabf5a15ba5df5/f38a3938477b5163-ee/s400x600/d9af62bf35fc69bc69b944df17aa81e6911e177e.gif",
            "https://64.media.tumblr.com/f2bf798dfbca999fe6cc1a30e76b22c7/de1767081c0b7b1d-90/s400x600/97be2f7e1a84fab0e4e34d389d39bb5e32bef667.gif",
            "https://64.media.tumblr.com/3ca0bc12cd8d9b2f4249d79f04351c17/de1767081c0b7b1d-90/s400x600/49c4d31da8f9161611049817e2610864d502f9f1.gif",
            "https://gfycat.com/contentdopeyalligator"]

        self.bot.winter_gif = ["https://tenor.com/view/aespa-archive_aespa-winter-aespa-winter-winter-aespa-gif-19207739",
            "https://tenor.com/view/aespa-winter-aespa-winter-aespa-kim-minjeong-kim-minjeong-gif-19029912",
            "https://tenor.com/view/aespa-%EC%97%90%EC%8A%A4%ED%8C%8C-%EC%9C%88%ED%84%B0-winter-gif-19207490",
            "https://tenor.com/view/archive_aespa-aespa-winter-aespa-winter-minjeong-gif-19138516",
            "https://tenor.com/view/winter-aespa-aespa-gif-19226090",
            "https://tenor.com/view/winter-aespa-aespa-gif-19323697",
            "https://cdn.discordapp.com/attachments/771238115255255060/781388912189898752/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781388912873832473/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781388914480513064/image2.gif",
            "https://gfycat.com/gloriousenergetickoala",
            "https://gfycat.com/achinglargecicada",
            "https://gfycat.com/blondunkemptchipmunk",
            "https://gfycat.com/blindanimatedborderterrier",
            "https://gfycat.com/bigcheerfuliberiannase",
            "https://gfycat.com/fancyshydrongo",
            "https://gfycat.com/phonydeficientcomet",
            "https://gfycat.com/scrawnyfarflungkilldeer",
            "https://gfycat.com/testyjovialchicken",
            "https://gfycat.com/acclaimedclearhatchetfish",
            "https://gfycat.com/healthyimaginativekillerwhale",
            "https://gfycat.com/clutteredtenseamericanblackvulture",
            "https://gfycat.com/definitiverapidbuckeyebutterfly",
            "https://gfycat.com/snarlingpastglobefish",
            "https://gfycat.com/directpettygermanshepherd",
            "https://gfycat.com/maleindelibleaxolotl",
            "https://gfycat.com/hastysparsedeermouse",
            "https://gfycat.com/heartfeltquarrelsomeekaltadeta",
            "https://gfycat.com/bleakdistanthare",
            "https://gfycat.com/cluelessbowedbarnowl",
            "https://64.media.tumblr.com/31d931739678ed3e36fc48e0a3f17e99/a131eb50b79882f9-50/s540x810/5ab8448ddd26bc61ba7c5703d5091b7f99bd2583.gif",
            "https://64.media.tumblr.com/586719a51532e50898342d0bfcaabd01/a131eb50b79882f9-51/s540x810/db0e7a6b2ccd6ee601116f874babc336764c865f.gif",
            "https://64.media.tumblr.com/95308d80745fa096c3d90617e42452f1/a131eb50b79882f9-4a/s540x810/dbad43401d18708a7acb56ca3d9a88b02f1da99d.gif",
            "https://64.media.tumblr.com/54fbd6676ec089e865a9259f2bbd7316/a131eb50b79882f9-02/s540x810/97ff2ab3b7ebe66d9592065f5d0418157234ac29.gif",
            "https://64.media.tumblr.com/44206357ecab57c31273bc68be10b686/bcda8463ac9d31eb-b0/s400x600/c9337942d8686d0cfce172e03feda421aa2d4287.gif",
            "https://64.media.tumblr.com/062a5ca9f28bb5934e0cf3a146f3df24/bcda8463ac9d31eb-a7/s400x600/9c13f4f2d1222c3d03bf750e13779dfb345b4da4.gif",
            "https://64.media.tumblr.com/cfaee9aac750512e5abc585b5c1029b4/dbb9ccc02f218f22-53/s400x600/dc1d62a6d101f1ff82bb3a4245b8943ea3d421f9.gif",
            "https://64.media.tumblr.com/9973e06190e9463b0031d395bac70b42/dbb9ccc02f218f22-27/s400x600/9c1a77eae2c6afeaf1a6fb1a2c81b6e922e1e452.gif",
            "https://64.media.tumblr.com/4feeb6cf9e40061bb25f0a1d17cd456d/dbb9ccc02f218f22-d5/s400x600/148e91059dad325233b2a7fd5270671d52e1aa4c.gif",
            "https://64.media.tumblr.com/bee05713165f6d2a933cf199f88f47bf/4ed085c3ac808702-36/s400x600/07f0ad878670c6fe7ef1ba6e2c50a132de430834.gif",
            "https://64.media.tumblr.com/8648d9dd3114f3de17b427b980b9b865/7193b89f1258bb29-21/s400x600/51195bc9240e8868b77362c02eae86d2c3b0ef7f.gif",
            "https://64.media.tumblr.com/813d5443d8ec2f24daba02e9069a9b0a/7193b89f1258bb29-04/s400x600/381d4e530d52cb3ed160f87aed4c313c8390edca.gif",
            "https://64.media.tumblr.com/fef3d32339c253257f1bebdb2235656a/7193b89f1258bb29-3a/s400x600/d9219a83e6774b125deb4323a5755db83a3381ba.gif",
            "https://64.media.tumblr.com/c6cabaaaca6a12b826915d45d30802b6/7193b89f1258bb29-52/s400x600/11c5d5c6092a23fee478465fe57ba7b9a9e51fa9.gif",
            "https://64.media.tumblr.com/7e868d7ecca59f33c00a1fd1ca3b0486/8e937dcbc110e592-d5/s540x810/ccf6e530117c2f9e928a79b515ae4b48fedbfacd.gif",
            "https://64.media.tumblr.com/8648d9dd3114f3de17b427b980b9b865/7193b89f1258bb29-21/s400x600/51195bc9240e8868b77362c02eae86d2c3b0ef7f.gif",
            "https://64.media.tumblr.com/813d5443d8ec2f24daba02e9069a9b0a/7193b89f1258bb29-04/s400x600/381d4e530d52cb3ed160f87aed4c313c8390edca.gif",
            "https://64.media.tumblr.com/fef3d32339c253257f1bebdb2235656a/7193b89f1258bb29-3a/s400x600/d9219a83e6774b125deb4323a5755db83a3381ba.gif",
            "https://64.media.tumblr.com/c6cabaaaca6a12b826915d45d30802b6/7193b89f1258bb29-52/s400x600/11c5d5c6092a23fee478465fe57ba7b9a9e51fa9.gif",
            "https://64.media.tumblr.com/7e868d7ecca59f33c00a1fd1ca3b0486/8e937dcbc110e592-d5/s540x810/ccf6e530117c2f9e928a79b515ae4b48fedbfacd.gif",
            "https://64.media.tumblr.com/aec81c36af7213298e87306b87c49b7d/1d8ce061135939d5-b4/s400x600/41671a98d8c9407cc326df492371f791f7fbc16b.gif",
            "https://64.media.tumblr.com/ebba71d1b76727b9948ef47f62d44d95/1d8ce061135939d5-c8/s400x600/d807e8b9bb8afbb9d2a8b34349deab339975e83c.gif",
            "https://64.media.tumblr.com/2c0d6eec616e8e4d2f03966d4e697d68/1d8ce061135939d5-c4/s400x600/56726b97ffdb245a77fa6925ed38d50b7d7a805e.gif",
            "https://64.media.tumblr.com/f77d06a4fca31f4732c5cb98c64b127b/9f12c101faf5aad2-bb/s540x810/a274b6f7e97e6a0cb69f441766ad574a0a4a4486.gif",
            "https://64.media.tumblr.com/c08231f25bbf9db8d8d059b6ebdf0c93/9f12c101faf5aad2-82/s540x810/88d80b65bab4d1cfdfefad913facce02e64bf6c9.gif"]

        self.bot.ningning_gif = ["https://cdn.discordapp.com/attachments/747275528993636424/781391569986125824/7226125c-1e30-4c1d-b3a9-f6a71db55fad.gif",
            "https://cdn.discordapp.com/attachments/747275528993636424/781391570829836308/3ee3defb-5472-48b9-b5ef-743984c6996d.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782482430879596544/giphy_1.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782482991351463966/tenor_1.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782482998293430302/tenor.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782483030086385714/MediumFlickeringFrogmouth-max-1mb.gif",
            "https://tenor.com/view/ningning-aespa-crying-shaking-fist-gif-19355492",
            "https://tenor.com/view/aespa-giselle-karina-ningning-winter-gif-19293865",
            "https://gfycat.com/opulentamusinggalago",
            "https://gfycat.com/pointedoldafghanhound",
            "https://gfycat.com/slipperyblackandwhiteacornweevil",
            "https://gfycat.com/inexperiencedimperturbablebluejay",
            "https://gfycat.com/fragrantenlightenedgerenuk",
            "https://gfycat.com/glumhighlevelindianabat",
            "https://gfycat.com/understatedacceptableargentinehornedfrog",
            "https://gfycat.com/flippantpresentivorygull",
            "https://gfycat.com/easygoingfixedafghanhound",
            "https://gfycat.com/educateddearestcob",
            "https://gfycat.com/peacefulredargentineruddyduck",
            "https://gfycat.com/consciousnextamericanbulldog",
            "https://gfycat.com/brownimpossibleasianconstablebutterfly",
            "https://gfycat.com/unlawfulgreatlark",
            "https://gfycat.com/practicalfancyantarcticfurseal",
            "https://gfycat.com/specificvastbear",
            "https://tenor.com/view/black-mamba-aespa-ningning-aespa-ningning-kpop-gif-19881136",
            "https://tenor.com/view/aespa-ningning-aespa-ningning-archive_aespa-archive-aespa-gif-19196653",
            "https://tenor.com/view/ning-ning-yizhuo-ningning-yizhuo-aespa-gif-19000866",
            "https://64.media.tumblr.com/f920153e8a6f32433ddd31de59364fa2/6f34313929a96185-74/s400x600/1b7d65c1677a23cd44084bbfdbb51a2c68c932b2.gif",
            "https://64.media.tumblr.com/1f85b9667be4b710207a9b0a43cc63e3/6f34313929a96185-a9/s400x600/e9e545b27b8bcb7415c9aaa7a65306a0d46b2ac6.gif",
            "https://64.media.tumblr.com/3fbb3f7facfdd2aed390c8de56a72e1d/6f34313929a96185-55/s400x600/af2bc5ccd13a001831647110272249e2963295f6.gif",
            "https://64.media.tumblr.com/5c65bc4e2cc21b463abcf312188df6ea/6f34313929a96185-1c/s400x600/16f57d6bc137a8f636aebe6a37e1ecd09921cdd6.gif",
            "https://64.media.tumblr.com/1381129340737c9e8759cd7913ff3b8b/0f7f2797330b5cca-d9/s400x600/35d4363b87d41c72cf99654a3aa48d07d521dbc1.gif",
            "https://64.media.tumblr.com/e30ea303c688122fac974040202dc0d9/0f7f2797330b5cca-eb/s400x600/d0c6a575023324a3a349daba8c8b5d6e5c958787.gif",
            "https://64.media.tumblr.com/2d2a7c7dcec85e457958c0148d5739f9/0f7f2797330b5cca-9c/s400x600/f52ea66f5fb4582381bddd0e93efaecb244970dc.gif",
            "https://64.media.tumblr.com/c48aacf9e957bc6aa7eadd904f70916b/0f7f2797330b5cca-ec/s400x600/54825a50734449abe2e899cd7ad68322b9104ac5.gif",
            "https://64.media.tumblr.com/ebe4d520f5e423c8e5a89a3e3b65215c/a85596cb07de2c30-69/s400x600/bc847c378a77f4b7d5bf26e995d311f8d9de4f4f.gif",
            "https://64.media.tumblr.com/d3f4f7d44fc3acd92253ed911133f606/a85596cb07de2c30-2d/s400x600/3116adb7cfdd8978b539eaa8672162f65004fd35.gif",
            "https://64.media.tumblr.com/fa63b34500a19498611c7ea24bb5a1df/4326fdc224fda6a9-b3/s400x600/6ee660697eb4251ace8e27bfe7cb86423a5fe91b.gif",
            "https://64.media.tumblr.com/c6e45ca709f5dcfc7576e8d4ade0ec41/4326fdc224fda6a9-96/s400x600/54b03021d96a37e85db4760ef44d6be08b703c81.gif",
            "https://64.media.tumblr.com/89a9ab97d8f3c2ff3fbf80ed76b54a8b/4326fdc224fda6a9-cd/s400x600/5f3e52b66042d86c897e4fba24642a4df210eea0.gif",
            "https://64.media.tumblr.com/dc9b6a888f7fad32926869f5ff24d26e/4326fdc224fda6a9-8d/s400x600/8365224f76bcf37942ac7a0c960f9a6ca6fc75f5.gif",
            "https://64.media.tumblr.com/05d8492a4819978205ff1b85c8cf9622/884f3ffb9948a614-23/s540x810/80c234f88ddf2550787184a1bd2c224d7bb57ac5.gif",
            "https://64.media.tumblr.com/00834c0998204658a55c85a223f29e39/884f3ffb9948a614-18/s540x810/f7e91fbdb534e0c225c5e0e03286f21e6669af99.gif",
            "https://64.media.tumblr.com/a6ccbfbc89f1bdafeb2fae8d486b0f6a/9fb3f55561f1ac8b-aa/s400x600/a1f911b305ffeae8552ff2b3ba9a972cbaa05c9e.gif",
            "https://64.media.tumblr.com/c02491425ff0e8dd2f37bedbfb8ebce9/9fb3f55561f1ac8b-18/s400x600/726f287588ed620c810fb2c763484214427a8fe0.gif",
            "https://64.media.tumblr.com/c6aaabf59ed10ff2a2ca658df0b2b998/84ee19f9ad038ab1-d6/s540x810/841be9f9fc2fbfebd730f7eddc58cd112965988d.gif",
            "https://gfycat.com/gentleamusedalaskajingle",
            "https://gfycat.com/diligentembarrassedargentineruddyduck",
            "https://gfycat.com/forsakenbelovedfalcon"]

        self.bot.karina_gif = ["https://cdn.discordapp.com/attachments/772980032086999090/782482078616125470/giphy.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782482080427671552/20201028144417-7ae7.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782482084324966430/giphy1.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782482084869832724/tumblr_0cac220cdb85f9cf71d97263a7935097_de5c9738_540.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782482091320803328/original.gif",
            "https://cdn.discordapp.com/attachments/772980032086999090/782482091656871956/HardRemorsefulFlicker-size_restricted.gif",
            "https://gfycat.com/tightharmfularizonaalligatorlizard",
            "https://gfycat.com/antiquesarcasticeyas",
            "https://gfycat.com/mildweehake",
            "https://gfycat.com/jovialcrazycoral",
            "https://gfycat.com/shabbysarcasticharborseal",
            "https://gfycat.com/fancyunfitgalago",
            "https://gfycat.com/distinctneatcutworm",
            "https://gfycat.com/gracefulperfectbasilisk",
            "https://gfycat.com/disguisedcomposedbunny",
            "https://gfycat.com/bronzehighlevelharrierhawk",
            "https://gfycat.com/ultimateweirdhapuku",
            "https://gfycat.com/shinyfewazurevasesponge",
            "https://gfycat.com/eagerscrawnykob",
            "https://gfycat.com/gaseoussprycentipede",
            "https://gfycat.com/slushyinsignificantboto",
            "https://gfycat.com/heartfeltwickedarchaeocete",
            "https://gfycat.com/tenseadorablegreendarnerdragonfly",
            "https://gfycat.com/portlyblandanophelesmosquito",
            "https://gfycat.com/blackdisfiguredgourami",
            "https://gfycat.com/alienatednaughtycapybara",
            "https://gfycat.com/thosetandamselfly",
            "https://64.media.tumblr.com/b4b27b5ea6e3511cdd488cf531e1e0d4/a89eaf172248a501-b2/s400x600/83af4790e04e67950208c57879ddc36719ed4239.gif",
            "https://64.media.tumblr.com/1f2022addf3f86e033234719a593e73d/a89eaf172248a501-cd/s400x600/c7df531d4ee4a92f74bdb9464b45eb746d850f7d.gif",
            "https://64.media.tumblr.com/9fc9bf5662a193e3e5fe958d8a116280/a89eaf172248a501-9a/s400x600/00a8ed22b9ab7e2a1c38d619d6e1736565a54418.gif",
            "https://64.media.tumblr.com/a29bec19d3547864a4c4e6493bdd8941/a89eaf172248a501-5a/s400x600/c08f2506f3e1a52db51348d8616afb421453ef18.gif",
            "https://64.media.tumblr.com/ba52ff8e2ab375951e747be74d780cc8/1289e6747b2ca0f2-06/s400x600/c3243fed3dc53096eb9a972429bda64bc8b7b274.gif",
            "https://64.media.tumblr.com/da906502d7289c089eb2cdfea471789d/5a5b30a8df2a1281-68/s400x600/63f08c76bf29f2a65fe4a36680a335d77e86bfc9.gif",
            "https://64.media.tumblr.com/597fd64fa021462407971a7cd0f5bfb3/5a5b30a8df2a1281-25/s400x600/d9a5500d5ef1322e8e488c5a4b5a3c3f0b15a0f1.gif",
            "https://64.media.tumblr.com/7ed0eb61ed37d5e43e64820bccb55d86/9644094b95d89431-58/s540x810/b8add28b55a37088f005ee25615ede741c0bafb7.gif",
            "https://64.media.tumblr.com/7228012ee4690f88ced08ee8c7405f8d/9644094b95d89431-02/s540x810/069209d21cb7f12a8ee96db255f6dc7834b88940.gif",
            "https://64.media.tumblr.com/96b73d7f56f81cd3a837b0412805b79b/9644094b95d89431-06/s540x810/79c256b6b37130dc8bb9e82725ca1defdca4032c.gif",
            "https://64.media.tumblr.com/9d89604bd1ca4f97e28313d5c5921dba/6fa84bbd6af7f56e-f3/s400x600/ac3017946fe247cfb791a6d29ca8053d43f97f52.gif",
            "https://64.media.tumblr.com/418c009e7b4d2bb309a1dc71a4ace365/6fa84bbd6af7f56e-7b/s400x600/ea11da2111fb36ba83efecd349b6f63b65b8d424.gif",
            "https://64.media.tumblr.com/da87f17469e82f2baf24031451e22284/6fa84bbd6af7f56e-71/s400x600/bda869e5baa7bb2e7c554930497bf3fd4ed72aa7.gif",
            "https://64.media.tumblr.com/05d8492a4819978205ff1b85c8cf9622/884f3ffb9948a614-23/s540x810/80c234f88ddf2550787184a1bd2c224d7bb57ac5.gif",
            "https://64.media.tumblr.com/00834c0998204658a55c85a223f29e39/884f3ffb9948a614-18/s540x810/f7e91fbdb534e0c225c5e0e03286f21e6669af99.gif",
            "https://64.media.tumblr.com/52cc91cd2805e6cb017e3f3cd058fce7/eddeacda76a18b9e-87/s400x600/7dc434664cbee7dd5f0239cfa1825172f16a3900.gif",
            "https://64.media.tumblr.com/1dcb5a1469ac8939b06f9b47955a63dc/eddeacda76a18b9e-51/s400x600/99cea52b8e189d7deca5991a6de36ec173aaff6a.gif",
            "https://64.media.tumblr.com/cbc37ac09589d70380518cc794cf0027/eddeacda76a18b9e-c3/s400x600/dff2f98d2e70fb8aeae75b0be024c4af2bbb744e.gif",
            "https://64.media.tumblr.com/b7073960a723c463c91a6777baf47792/eddeacda76a18b9e-45/s400x600/882c8aebf34d3a52efcf15f44776e7be4eac0fc7.gif",
            "https://64.media.tumblr.com/1e020263c3510e011b3c802a158b2528/f11f5080d76be8bf-bc/s400x600/e8ae788d4cce09ca1191893d25997c7c7d25eddd.gif",
            "https://64.media.tumblr.com/90ac590a6e39fff53c01eb41d39df20d/f11f5080d76be8bf-00/s400x600/c2ab807c23ad11215609f089c20dfa9a32a896e7.gif",
            "https://64.media.tumblr.com/724dc54fe19557b3ab412473150d5d27/5761b4593766d8f3-2d/s400x600/a9cb10b57f3d75be472a95c5f9d3e1c4534229ee.gif",
            "https://64.media.tumblr.com/31e6d4c78134ef9afdc00e31827de94b/f90c14dee7fa100c-61/s400x600/b20fdd8e020a48a6d4112fd991f28fedc4cfb1af.gif",
            "https://64.media.tumblr.com/6e4c3af4426fa37f441fb5ad3f36357e/6eba718d36e55085-31/s540x810/b906ed3aa6ebf69f95ee98d94fc471e904546f1d.gif",
            "https://gfycat.com/contentdopeyalligator"]

    @commands.command()
    async def aespa(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [aespa {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "giselle":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{k8}>, <@{rith}> <@!{ctx.author.id}> is talking about Giselle :crescent_moon: ')
                    await ctx.send(random.choice(self.bot.giselle_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Giselle :crescent_moon:')
                await ctx.send(random.choice(self.bot.giselle_gif))
                await ctx.message.delete()
        elif arg == "winter":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{k8}>, <@{mae}>, <@{rith}> <@!{ctx.author.id}> is talking about Winter :star: ')
                    await ctx.send(random.choice(self.bot.winter_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Winter :star:')
                await ctx.send(random.choice(self.bot.winter_gif))
                await ctx.message.delete()
        elif arg == "ningning" or arg == "ning ning":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{k8}>, <@{mae}>, <@{rith}> <@!{ctx.author.id}> is talking about Ningning :star: ')
                    await ctx.send(random.choice(self.bot.ningning_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Ningning :star:')
                await ctx.send(random.choice(self.bot.ningning_gif))
                await ctx.message.delete()
        elif arg == "karina":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Karnia :star: ')
                    await ctx.send(random.choice(self.bot.karina_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Karina :star:')
                await ctx.send(random.choice(self.bot.karina_gif))
                await ctx.message.delete()


def setup(client):
    client.add_cog(aespaPings(client))
