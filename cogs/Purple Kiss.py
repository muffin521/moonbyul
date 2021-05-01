import discord, random
from discord.ext import commands
from datetime import datetime

#//servers
luminary = 758468592957521972

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

class PurpleKiss(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.yuki_gif = ["https://gfycat.com/slipperydecisiveindianspinyloach-purple-kiss-purple-kss-kpop-yuki",
            "https://gfycat.com/waterloggedwatchfulasianconstablebutterfly",
            "https://gfycat.com/tamegloomyamphibian",
            "https://gfycat.com/snivelingfatalgangesdolphin",
            "https://gfycat.com/definitivedeterminedantlion",
            "https://gfycat.com/glaringglitteringdore",
            "https://tenor.com/view/yuki-purple-kiss-gif-19356715",
            "https://tenor.com/view/yuki-hamster-laughing-cute-purple-kiss-gif-19603707",
            "https://cdn.discordapp.com/attachments/547946757594677268/806562700624396298/image0.gif",
            "https://cdn.discordapp.com/attachments/547946757594677268/806562701023248404/image1.gif",
            "https://cdn.discordapp.com/attachments/547946757594677268/806572183647813662/image0.gif",
            "https://cdn.discordapp.com/attachments/547946757594677268/806572210495553588/image0.gif",
            "https://cdn.discordapp.com/attachments/547946757594677268/806682389069037638/image0.gif",
            "https://tenor.com/view/mori-koyuki-yuki-purple-kiss-mworikoyuki-gif-20125374",
            "https://64.media.tumblr.com/759d808e1a951dde70988d19356f13ac/861ad649bc3e52ed-87/s540x810/bac80389d1fec357c0dad818b72dc3bd61e23039.gif",
            "https://64.media.tumblr.com/7e4dbd7351af21db0129461efabcf1fa/42ba22191a1579cf-a1/s500x750/acfddf929d8fb161b3b199acdefa6c0261f55fd6.gif",
            "https://64.media.tumblr.com/f5f94055def82564d748dfa56ce43938/9b513bde8b638a0a-d0/s540x810/659717bc9acf760a6c0eff5f40378f6e3ef7bf5a.gif",
            "https://64.media.tumblr.com/86b27e9834b01f6c46164382fa549415/a5ff213f0cfcdec9-ea/s540x810/3852535fb79b39e803a165f3b14461fd205b44d5.gif",
            "https://64.media.tumblr.com/24ef9a7fa27d1a4ec51fe85d011a0a04/d1342c671794fa4b-c4/s640x960/590404d5ed516c23f400d34c7922bd0da4823b56.gif",
            "https://64.media.tumblr.com/9c60f9ec76d0890f909485562392e5e3/8e840b1cca716356-b7/s400x600/36791bf17c0090e440e7fec4eb7552cbfb1a14cd.gif",
            "https://64.media.tumblr.com/e55ac7c751812967ebbce5a2fa6447e9/8e840b1cca716356-21/s400x600/3647beecf685ece037e85304d2c0f8774cd0ab2a.gif",
            "https://64.media.tumblr.com/9feb8656030ed12a0b1bbef855421bfa/bdae5c3d32cb7e43-25/s400x600/7212ea369484e99d4bfabdbb1ee06b533d5a2992.gif",
            "https://64.media.tumblr.com/1c9d5a3d7d3549c813ef0da645dea91e/bdae5c3d32cb7e43-46/s400x600/8199a0468b40366fea0dfc0ba23b62e5ec48bc46.gif",
            "https://64.media.tumblr.com/80c0315ff36f09035860b959b850f5bb/bdae5c3d32cb7e43-96/s400x600/005424217168d4f4a609d02e9ffc20d5bb59afa7.gif",
            "https://64.media.tumblr.com/eed04e588d3e3d2948795d48cc8d19ef/bdae5c3d32cb7e43-fc/s400x600/432817b0712c62fdb05304db8044620c2d3bfdff.gif",
            "https://tenor.com/view/yuki-mori-koyuki-mworikoyuki-purple-kiss-gif-20203328",
            "https://64.media.tumblr.com/b99be16c18fce3163245d61edaf287e8/5e9b78ac791b918f-b4/s400x600/61135077039d329004e90682224d4c930f13c837.gif",
            "https://64.media.tumblr.com/a79ced3fed503111776ff7242f67507b/5e9b78ac791b918f-57/s400x600/9fc25517c17f2afbf36897987e74e5e6c2c46010.gif",
            "https://64.media.tumblr.com/71f755890e5548944fd13610bd245d05/5e9b78ac791b918f-99/s400x600/5d2b32ea54a04df0bd653130b9ad8925cba96958.gif",
            "https://64.media.tumblr.com/d3770ab5a483c4bfc75f4114c79c977d/5e9b78ac791b918f-b5/s400x600/5c4f3f02209ce366e721a695f91886d440517fc3.gif",
            "https://64.media.tumblr.com/01d0c7a60ebb4715b2e4a5202618a384/4bd38d19211e6d97-c0/s540x810/3039090f0498c89cac2503343ee487b41bd60b05.gif",
            "https://64.media.tumblr.com/81eeac579fb89fdf6f82bb130eebc2d2/4bd38d19211e6d97-f4/s540x810/ac2f270b75f8fa96f380504ed985ff04938da9f8.gif",
            "https://64.media.tumblr.com/94f500dfa511df1753df6940d3eb0029/4bd38d19211e6d97-df/s540x810/6dc7ca9a043e5d6707bb9cccd878ca26aea1a0ca.gif",
            "https://64.media.tumblr.com/4db56f8e3e94abe845eaa69d31b04553/4bd38d19211e6d97-1c/s540x810/51f9e032eb1e6e40d9c2b5ec5fad217a881f8538.gif",
            "https://64.media.tumblr.com/e0ff6bb0ed5f2d06b7ff860e022007b0/4bd38d19211e6d97-7e/s540x810/ab174e5603316ebf355f4d6a952b0e5eff8ae2f7.gif",
            "https://64.media.tumblr.com/b8602ad9c4879c973eefa7f88f8ed054/f4e9f8db5e141eae-d4/s250x400/234a591bb27d8a7997c5df8a435a16c96844114f.gif",
            "https://64.media.tumblr.com/be45ea5df567c1ea0f8ff5c5541c0e38/f4e9f8db5e141eae-7b/s250x400/ec82b04e62add4f85a997bf2b5482bd913d7b9ee.gif",
            "https://64.media.tumblr.com/5686a5c204955d41b02058863674f70b/f4e9f8db5e141eae-1d/s250x400/7d2de299c9f55425c1bedc9e376b1569ba357267.gif",
            "https://64.media.tumblr.com/4d94c115c740eabaa7dc492feffeccac/f4e9f8db5e141eae-dd/s250x400/e9a33d69591c829479d154b16b81bf7bdd138d41.gif",
            "https://64.media.tumblr.com/5a56cd2f24246a58f368a6fdae0b0406/f4e9f8db5e141eae-82/s250x400/7ca3a4b2d055ebc5da75702b68ccd5591caddc10.gif",
            "https://64.media.tumblr.com/31d677e096353312ba3d28235a0302d3/3901bd35306afb4f-1f/s250x400/6eb64237b8cfbad5188e90322031c411bf44101f.gif",
            "https://64.media.tumblr.com/0613e3453df056c61b69f8efd3a3eb1f/f1d5344b7415e2dd-5b/s400x600/50a04152f412cc89c8257698350ae2766444d5d4.gif",
            "https://64.media.tumblr.com/10338dad5ad24bd4a3929ae65ac97623/8d6d7e1a2219a1f1-68/s1280x1920/ceeb2dd6ad45c2d7fab77008c0bbeed2abf7d915.gif",
            "https://gfycat.com/weirdblackandwhitegalapagosdove",
            "https://64.media.tumblr.com/89922f223734f499d6ae57b755a42ccb/e6430bce2995b80c-aa/s250x400/f18f2c22c29d84d844fac658af37aa304913126d.gif"]

        self.bot.nagoeun_gif = ["https://gfycat.com/BiodegradableBackClam",
            "https://gfycat.com/FrightenedQuarrelsomeHare",
            "https://gfycat.com/PortlySillyAnemone",
            "https://gfycat.com/HonorableSorrowfulHypacrosaurus",
            "https://gfycat.com/AdmiredWeightyGlowworm",
            "https://gfycat.com/LavishSneakyIcelandicsheepdog",
            "https://media.discordapp.net/attachments/762508629680586775/783175861875638302/goeun_heart_gif.gif",
            "https://gfycat.com/whitegoldenbirdofparadise",
            "https://gfycat.com/heartfelthelpfulgrayfox",
            "https://gfycat.com/glisteninguncommonilladopsis",
            "https://gfycat.com/smugraregreendarnerdragonfly",
            "https://gfycat.com/evenperkyfiddlercrab",
            "https://gfycat.com/enragedsoftenglishpointer",
            "https://media.discordapp.net/attachments/547900536565924104/740000852214808772/20200803_201852.gif",
            "https://media.discordapp.net/attachments/547900536565924104/739996247850483863/20200803_200002.gif",
            "https://media.discordapp.net/attachments/547946725592137728/740189250909372516/20200804_082123.gif",
            "https://media.discordapp.net/attachments/547946725592137728/739990286976942100/20200803_193527.gif",
            "https://tenor.com/view/purple-kiss-na-goeun-goeun-purplekiss-goeun-dancing-gif-17914994",
            "https://tenor.com/view/go-eun-chaein-purple-kiss-gif-19356750",
            "https://tenor.com/view/goeun-purplekiss-purple_kiss-nagoeun-gif-19540241",
            "https://tenor.com/view/goeun-nagoeun-purple-kiss-purple_kiss-gif-19673140",
            "https://tenor.com/view/eunnie-line-eunseo-dosie-goeun-eunseong-gif-19614430",
            "https://tenor.com/view/goeun-nagoeun-purplekiss-purple_kiss-gif-19614340",
            "https://tenor.com/view/goeun-nagoeun-purplekiss-purple_kiss-gif-19614407",
            "https://cdn.discordapp.com/attachments/547946725592137728/806563805344956486/image0.gif",
            "https://cdn.discordapp.com/attachments/547946725592137728/806563851112939548/image0.gif",
            "https://cdn.discordapp.com/attachments/547946725592137728/806563909406163005/image0.gif",
            "https://cdn.discordapp.com/attachments/547946725592137728/806566140317925476/image0.gif",
            "https://cdn.discordapp.com/attachments/547946725592137728/806570760381530122/image0.gif",
            "https://cdn.discordapp.com/attachments/547946725592137728/806597242801750046/PURPLE_KISS_Can_We_Talk_Again_MV.gif",
            "https://cdn.discordapp.com/attachments/547946725592137728/806603169541914644/PURPLE_KISS_Can_We_Talk_Again_MV_1.gif",
            "https://cdn.discordapp.com/attachments/547946725592137728/806682296023121950/image0.gif",
            "https://64.media.tumblr.com/5be3436815ec5f9b15b0028cac5b4a0d/9b513bde8b638a0a-22/s540x810/6f0d02248ca117f1e3442b68754604e5f60b0d03.gif",
            "https://64.media.tumblr.com/e1791a07cb333133a39e639b74d9fa57/a5ff213f0cfcdec9-ee/s540x810/837b6d5bd7c350b46c5a78f653d3feebd3de3122.gif",
            "https://64.media.tumblr.com/9212a09bd1c8ed2e06a0066826742f43/b894ca2379e2f5dd-f6/s540x810/775ff17edd69c1704f7070cecf5b779c1a1e0c74.gif",
            "https://64.media.tumblr.com/07ed2cb01df30d9418db1baffd563ca9/42ba22191a1579cf-14/s500x750/a5824cb1b0519db9d72fd8ce857955ad8e9d9200.gif",
            "https://64.media.tumblr.com/63acf3314fd9c4efaea82c807a050ca5/d1342c671794fa4b-5f/s640x960/06838d7265ec8118135d6eb0b5ec52da50273856.gif",
            "https://64.media.tumblr.com/79ef22b05c9d285f7c4ffec3195a21b5/22ad1bda2b08364a-8b/s540x810/43cae34a43ec4afa6cbbbe987afd43e6123523cd.gif",
            "https://64.media.tumblr.com/80c70b3cff73029f99961fce2e7719cb/943fe9d6af3ae758-7f/s400x600/5cf2d7ee496cd775aa632c2f9536dd540edf7fc5.gif",
            "https://64.media.tumblr.com/2ecb0e56a67eb7c19b0b24930e7eeb20/943fe9d6af3ae758-97/s400x600/404b53d262bdb2bd06224d266ae5f8e6dc7b912d.gif",
            "https://64.media.tumblr.com/c75658e9610059fc1030d7b0b26fdd61/943fe9d6af3ae758-ac/s400x600/e5d8e99251e7f50dfc43518c1723cd29f18e76a4.gif",
            "https://64.media.tumblr.com/dea5b5f5337288b473d47fbf5762abe0/9151c0e46796d62c-2a/s400x600/20614d16b13c362af2b5fd1963d114e93e2d1991.gif",
            "https://64.media.tumblr.com/2bfc1e1c8caf86019cc72e5809d88ade/9151c0e46796d62c-36/s400x600/1529a189b94a32e7685a79ad0a08ca32026a44a0.gif",
            "https://64.media.tumblr.com/a42bb4fba2fdd56ac8dd834ea72f7c83/9151c0e46796d62c-72/s400x600/a5eb0f12552cd1fcb17fcc925dc558abcea6adfc.gif",
            "https://64.media.tumblr.com/21eec68d27913e5f5a77c92d064ba6ca/9151c0e46796d62c-7a/s400x600/d6f158d0eb4789cd530ced1138e1db33679a003e.gif",
            "https://64.media.tumblr.com/ac9b0ada22c1b391db28743bc168b7a2/cca3b8c88050eaed-5d/s400x600/b5a25b157cb11c58175d29d49cd440db16c8db0d.gif",
            "https://64.media.tumblr.com/fd25c6a715be29d8cbf5f0ce9dde8464/af7b14fd731e3a5e-ca/s400x600/0f14e32ee60820e669fc1fb9619a89f9ac56ec23.gif",
            "https://64.media.tumblr.com/2c96b737a7c56095f02dd236c3ad4646/af7b14fd731e3a5e-c5/s400x600/cbe7497d0b5250418b2f026e16c2706ed264ca7d.gif",
            "https://64.media.tumblr.com/b31dd46e5c842e08f257d9cf1e7ae5a3/af7b14fd731e3a5e-79/s400x600/5db903dc9ea9c88af1f24748efbe7960eaa95bd7.gif",
            "https://64.media.tumblr.com/7e8ed147bb5d3761c6696c0f586a5869/af7b14fd731e3a5e-1d/s400x600/2cfe95e0a817b6797bd7cea9aea676b16d724fd1.gif",
            "https://64.media.tumblr.com/4b7a1ace055c4cc46e5ac8425970bea8/c37fc16f987632a0-9f/s400x600/3d9cc5bb3ac36a134054b6ffed049d143b883b5b.gif",
            "https://64.media.tumblr.com/ecd971a756b08765cb06dfcb29dbb1ed/c37fc16f987632a0-4d/s400x600/0c6cfdfa62a9c564bde43444757dff9defc6c0d6.gif",
            "https://64.media.tumblr.com/6b5800ccd7d4d1fa0164b5653d830e44/135ae960e62cdd22-d3/s400x600/73d5506215c3e3b945fb9effaa9d2f8fa5f2c962.gif",
            "https://64.media.tumblr.com/5cf74295d553c525dc57e5caad4d7563/135ae960e62cdd22-42/s400x600/b1ccb6842dff64d255ce1b64248e797e385df6a0.gif",
            "https://64.media.tumblr.com/615cddce1cca83976c10c7aa6c3e0038/135ae960e62cdd22-ae/s400x600/cf706cf259902a0a80b004f535c5098dcaf8f791.gif",
            "https://64.media.tumblr.com/dd0058e9b9cd94cc74dab7de1c8240cb/135ae960e62cdd22-f9/s400x600/0bc7b2e125b880c5b29408f769a6111947977f03.gif",
            "https://64.media.tumblr.com/b691057cca34e63a5bfd051f7d3b5f0c/88cd0a5e65ef170f-64/s400x600/03dbbb58c4dbc608c666d6c578e7c090742ad5cf.gif",
            "https://64.media.tumblr.com/8930f8c73cc00eca5e07bd15a577a08e/88cd0a5e65ef170f-2f/s400x600/fddbddbd8a5265d4583ffb2253ba9f19afb349ee.gif",
            "https://64.media.tumblr.com/28326b00e4902bdc1c7ca361014f6a37/88cd0a5e65ef170f-30/s400x600/e612d312cc67c5ecfe010e28c384673cf1295578.gif",
            "https://64.media.tumblr.com/c9e44dbe20de612896d405976debcab5/88cd0a5e65ef170f-f4/s400x600/7900e23ebbc2cf467ea8cdc3060ab8b0ddaf333d.gif",
            "https://64.media.tumblr.com/25dc5afea49ae24bdf35ee6e75eb4a59/d1eb1f0d4bb924ec-8a/s400x600/fda51dbe1fc006de3e677efab3d93baf2802139b.gif",
            "https://64.media.tumblr.com/b53c1d800e33a9d9a17bd6fbcba0b3be/d1eb1f0d4bb924ec-60/s400x600/751d77d3f4949e4b644471309d657218e47e5a91.gif",
            "https://64.media.tumblr.com/a48668ab06fbf7e0c6664c68dce53079/a404227845f826db-9b/s400x600/5c9a96eceda11135459b99363546c736dbff33e2.gif",
            "https://64.media.tumblr.com/8cb37f62ba9eeb471f72d5379afc57f4/a404227845f826db-6d/s400x600/30404cb8f5b411458d923cf02ce7c0035f3b4062.gif",
            "https://64.media.tumblr.com/76bbb5843297db75f5c3b44a2b2c0c31/113a5bd8f41787bc-cb/s400x600/b5c06a2563f67f55af30a6c9b9e7b92add71cc7c.gif",
            "https://64.media.tumblr.com/c38505dcf38fa7e4cf64cf9df92b25da/113a5bd8f41787bc-a3/s400x600/72bcb58b9c93838ce9a81b24cd125e42f0971408.gif",
            "https://64.media.tumblr.com/9e4ddf76abdba8cbac4593efd86ef39e/113a5bd8f41787bc-9f/s400x600/fef9b1a23a8b95a4101a5a2204883ebe41235391.gif",
            "https://64.media.tumblr.com/7a3c3a025ae1187cc87b19fba2b5242b/613b63f1e8747cca-ba/s400x600/052280bda24aa60390101e06ff9f3ae50444567e.gif",
            "https://64.media.tumblr.com/2874c77c11078e42f92c883d44d8ceff/613b63f1e8747cca-e5/s400x600/d6b8b95fcddf4ac54b6f464effbd993136cb8a34.gif",
            "https://64.media.tumblr.com/651b0fc0d72fe2665116e6c6915350f2/474712829b43e7eb-28/s400x600/544082ed7f365110d6a54a885f9d6adf5e26aefd.gif",
            "https://64.media.tumblr.com/00570f4d6c54c51bd1e1d4b4a68aa568/474712829b43e7eb-6e/s400x600/c7e7c5ef72e33a3bf59166f00979dc5f5ed9de03.gif",
            "https://64.media.tumblr.com/2279feadf0d9054fa02411eed9cd7cd0/3901bd35306afb4f-6a/s540x810/154c7b51de3215acdeb3a165600b7c066aaef523.gif",
            "https://64.media.tumblr.com/09fcdcabb6176a3ef140ebef22d8d35b/f1d5344b7415e2dd-89/s400x600/4d60238988238c6c5a2e3043ed9f82bf22a86c34.gif",
            "https://64.media.tumblr.com/e472ff5b45920505a1a4c55df7db0894/2992966a43406f03-69/s540x810/017479aaa3d5bc8c0e1828798861ef3ab4badde0.gif",
            "https://64.media.tumblr.com/c5b94d66eee41a9b5dba1f1b3fa78981/e9e86fbe5ba6e3ae-5c/s400x600/e2ede183312c931737aa52f5111a3ea1ae438e6a.gif",
            "https://64.media.tumblr.com/eaa1dac53262b9dcb60de7535324ea23/e9e86fbe5ba6e3ae-b1/s400x600/48290e2c8a902c89d1786f64d5b4c82f66d13eb1.gif",
            "https://64.media.tumblr.com/04da25d75ae5893fe0e52d8053b39b5c/e9e86fbe5ba6e3ae-d8/s400x600/b32bb6ee846c739376dc7dd71a1723879b63c248.gif",
            "https://64.media.tumblr.com/6b6a1b609ac9af14c48a9186b5569801/348dcdc7a00dbf61-0d/s400x600/6fd6a6b8a76ed87947d0aafec7b044def770ac28.gif",
            "https://64.media.tumblr.com/d34514ae314f0e810c3953ac7093fc68/61d29bdb5b82b7de-ae/s400x600/588665fb495b74fe6755970c2c9caca0f563b792.gif",
            "https://64.media.tumblr.com/e04bcbf7d186252e7f579daf43372d53/61d29bdb5b82b7de-7c/s400x600/0dcdabc69e38ad0594def7db6c1da7df19514779.gif",
            "https://64.media.tumblr.com/c776d4a0fd1ffa7f7bf757232f15cd49/61d29bdb5b82b7de-4e/s400x600/4d64b9a4d45766ed47e57dcf50164bfb76f2891b.gif",
            "https://64.media.tumblr.com/14ddea3a11dfccf655de5b4033f9465e/56ca34bce1e71b6a-e6/s400x600/cd55b16de17292fa19a2491612ea6ba22e696076.gif",
            "https://gfycat.com/simplisticsplendidasianelephant",
            "https://64.media.tumblr.com/3f1a5afe2ac887828cae87d673df5ad6/e6430bce2995b80c-5d/s250x400/00a5f33b54eca4ce38a788023d8eeb9140f59575.gif",
            "https://64.media.tumblr.com/d13dad22c720fcff331dc8e72344cf59/e6430bce2995b80c-ae/s250x400/e3364a063773a2ea5fd6e7b8ef4f31e0ab579240.gif",
            "https://64.media.tumblr.com/1a2b8afbe7fcd8fa9f54f88670eaaa14/c06ca3690cfe4471-92/s250x400/22d4a1ac6fb930160ec56f6e33595962185ccd04.gif",
            "https://64.media.tumblr.com/9b448337a6f7ed6ca84cf8b57c24293d/c06ca3690cfe4471-26/s500x750/62cee7674b29a72df603d6eecd9790495e22dfee.gif"]

        self.bot.jieun_gif = ["https://gfycat.com/ComposedPlayfulAmethystgemclam",
            "https://gfycat.com/VastDistantAnophelesmosquito",
            "https://gfycat.com/PitifulPleasedCassowary",
            "https://gfycat.com/BabyishFrankAttwatersprairiechicken",
            "https://gfycat.com/RarePleasedJunebug",
            "https://cdn.discordapp.com/attachments/547946709758509076/740189208232198184/20200804_081400.gif",
            "https://gfycat.com/contentorderlygibbon",
            "https://gfycat.com/elasticblankaustralianshelduck",
            "https://gfycat.com/exemplarybiodegradablelemur",
            "https://tenor.com/view/purple-kiss-park-jieun-gif-19609803",
            "https://gfycat.com/aridfoolishbarnswallow",
            "https://cdn.discordapp.com/attachments/547946709758509076/806564005195284541/image0.gif",
            "https://cdn.discordapp.com/attachments/547946709758509076/806564005799133184/image1.gif",
            "https://cdn.discordapp.com/attachments/547946709758509076/806567003711602708/image0.gif",
            "https://cdn.discordapp.com/attachments/547946709758509076/806682264355733504/image0.gif",
            "https://64.media.tumblr.com/0fb868e514da08ed8a2e060383b9b5f6/ead734e0a9b83979-2a/s540x810/f15a57171641c4cf006659d2e087553843766a12.gif",
            "https://64.media.tumblr.com/5f06382664265e94023f776f5e96859c/6705470e01024198-88/s540x810/f3f4e195a847d4a1f5e0d5ab09796e096f5f76c6.gif",
            "https://64.media.tumblr.com/43cdd2d4010898779933b53f89590784/6705470e01024198-3e/s540x810/29ecff5acfea1e3ebe497689c3dbcfdf02daf53e.gif",
            "https://64.media.tumblr.com/1ee44e9302a6695b91df57eb951901d3/42ba22191a1579cf-8a/s500x750/154e0b111d6997ca554854e8c5e04b7ae31cb2e3.gif",
            "https://64.media.tumblr.com/17eb07db980440614ed4f67fd52a2bc4/44c2bd0cab0993a8-89/s400x600/d1efbd915869d2ada8748b7774ed9a38637e8218.gif",
            "https://64.media.tumblr.com/ad5fde9f21701504cf0591ae267648b1/44c2bd0cab0993a8-07/s400x600/4d049a012a2c47595ee4876bb9a3c4f0bb2c6b7c.gif",
            "https://64.media.tumblr.com/b88f9305f60063d4058abb813d1fda58/44c2bd0cab0993a8-b4/s400x600/858264e2630fa1c5eb4ec7724e16786b942dfaa1.gif",
            "https://gfycat.com/adventuroushandyequine",
            "https://64.media.tumblr.com/4b8372f56319b7c63a1928dc6f39342e/8519990dd2148025-66/s400x600/238d335446c95437f39e1843559c632bfe9c268a.gif",
            "https://64.media.tumblr.com/4805f3789ed12db76d94a24cf3680f8b/8519990dd2148025-a5/s400x600/c015d4e5a901b3beedc2ff97c82f2bd2ab6aabbf.gif",
            "https://64.media.tumblr.com/2ddf89543d1a9284865ba299139730c7/8519990dd2148025-6a/s400x600/5628129de0c64a59826ab66238fce5e7f1ce2730.gif",
            "https://64.media.tumblr.com/4b8372f56319b7c63a1928dc6f39342e/8519990dd2148025-66/s400x600/238d335446c95437f39e1843559c632bfe9c268a.gif",
            "https://64.media.tumblr.com/8afe487c19e0dbc7053e77b3016435fd/c73b2b1ff2330843-75/s540x810/40998d4cab1c2dc0656d8847d92277eb30509a20.gif",
            "https://64.media.tumblr.com/37179e5fe1744bf55db36a00bd50cafb/c73b2b1ff2330843-4b/s540x810/bd2330ce8099512141a1722db8b07374158306d1.gif",
            "https://64.media.tumblr.com/6c7aba02970be26b8b56f5d9e732d69c/c73b2b1ff2330843-2d/s540x810/2677bf48e6e90e37c2ecf284906f45f1ce53db80.gif",
            "https://64.media.tumblr.com/f3def78e8261dc8cf3e7a8753c37fca3/c73b2b1ff2330843-20/s540x810/45e66fc4cd7ed6d122b6d4024a258cf69090b51e.gif",
            "https://64.media.tumblr.com/1d7255d3f8527da500db680d628c520c/3901bd35306afb4f-bb/s250x400/17373daf7dea02297a5b890c5aa0b4442afe751e.gif",
            "https://64.media.tumblr.com/40bbe39af49df8c00cd3077e6fb63651/64d82ee1b256986c-e3/s400x600/69ea3823c0a9f9eba1d7ef7fa04e9b283961478a.gif",
            "https://64.media.tumblr.com/86bdfe2648c1fa6a36e467cec90742d7/64d82ee1b256986c-85/s400x600/eeb89d877f339e77a80b66ec7f8e4bd28713ba75.gif",
            "https://64.media.tumblr.com/564149a681c454b8a26e3fcfb1589234/8d6d7e1a2219a1f1-48/s540x810/fc8675548eca3b92206ad2d7d2adb7ab5a3af1b2.gif",
            "https://64.media.tumblr.com/9d5bf0124949659f81fdb73d096bd5f6/c1d0c90e26c2536d-e0/s540x810/4b7ecd94d54e787735b640e19ea04cda2ebc1eef.gif",
            "https://64.media.tumblr.com/bd9eece2d116391a82e9e489b0ae0bbf/c1d0c90e26c2536d-ec/s540x810/dfca3545832606194a23a76eb1f993250e2ea2ef.gif",
            "https://64.media.tumblr.com/181d6646b999bb521fded377a728a599/5af5403152cf68a0-ca/s640x960/b7d1b2d170f99e676941a49dd7850f24ac42c87d.gif",
            "https://gfycat.com/alienatedfantasticcopperhead",
            "https://64.media.tumblr.com/485da634f346ea8796c8c68f8b8e804c/e6430bce2995b80c-90/s250x400/a8539e387ac76216b5993a858f159e222e9e1151.gif"]

        self.bot.dosie_gif = ["https://gfycat.com/ShorttermAgonizingIriomotecat",
            "https://gfycat.com/ReflectingPessimisticGalapagosalbatross",
            "https://gfycat.com/QuestionableImpracticalClingfish",
            "https://gfycat.com/ImpartialHonoredBangeltiger",
            "https://gfycat.com/ImprobableWatchfulKillifish",
            "https://cdn.discordapp.com/attachments/547946748811935755/740189265610408026/20200804_082421.gif",
            "https://tenor.com/view/eunnie-line-eunseo-dosie-goeun-eunseong-gif-19614430",
            "https://cdn.discordapp.com/attachments/547946748811935755/806563373672169492/image0.gif",
            "https://cdn.discordapp.com/attachments/547946748811935755/806563374472626177/image1.gif",
            "https://cdn.discordapp.com/attachments/547946748811935755/806563422388486144/image0.gif",
            "https://cdn.discordapp.com/attachments/547946748811935755/806572101648646174/image0.gif",
            "https://cdn.discordapp.com/attachments/547946748811935755/806682321117380658/image0.gif",
            "https://64.media.tumblr.com/4f55242430cdbec9ae2820a1304fe245/9b513bde8b638a0a-30/s540x810/7dff50d9cf3d8cb6e4cbd8d044efe7bc0671c9f4.gif",
            "https://64.media.tumblr.com/868769fa1e0c4d4cdae0dcb2197e9134/ead734e0a9b83979-82/s540x810/e38a70c58fba0b5493c870a433c2da05a40a102a.gif",
            "https://64.media.tumblr.com/1225e564f5a05d01be481cda8c6a023b/5d682c62ede36be6-63/s540x810/912bf647aad895112bd9efa25afb558c19968b70.gif",
            "https://64.media.tumblr.com/4ff2dee569bf36497aeafca7c4761590/8819fc8c82e54d9b-84/s540x810/fa947d752e3fe623c6301083b5ae22662b4f30c1.gif",
            "https://64.media.tumblr.com/f61d155571dd2b391abbd7d9bb7d24c9/42ba22191a1579cf-20/s500x750/9fffa58c3f31558b28c3fda156a8a8758e38e0df.gif",
            "https://64.media.tumblr.com/dadeba836ceed1a449f6e83a41ea2151/2a8a03211be7a7a7-91/s400x600/33cdab4bcc9da0bfdaa11a3334a35c4a4ef815ca.gif",
            "https://64.media.tumblr.com/bb597074ffacb3f54f0bb894ac22b2cf/2a8a03211be7a7a7-75/s400x600/9096245f49cc7436d860b96b928d94ef5ac09a36.gif",
            "https://64.media.tumblr.com/30a87b7b376bd7c5d318211f48d135f1/2a8a03211be7a7a7-b2/s400x600/aab8f5e9587be4e0bb32f0abd853c02e6a5bb100.gif",
            "https://64.media.tumblr.com/f3024a917a40aa23b8c6ab59f793895a/2a8a03211be7a7a7-90/s400x600/3edaaa5fc998b6fdd75b9df141a48996de7df3cb.gif",
            "https://64.media.tumblr.com/c436815dc54fd810a988f954e4dda208/1eef39c3277c2746-99/s400x600/09af66000c833e046f5e29a7f1fa89723d2cd501.gif",
            "https://64.media.tumblr.com/691f75540849c00cc46b47e231e90c62/1eef39c3277c2746-4e/s400x600/b084995fa48dbb828ea1bb8b47ed21a34eac261a.gif",
            "https://64.media.tumblr.com/ead90f2a192fd24aa340839f368bc594/b2305c9cbdfcead8-d7/s400x600/c9107401b88feb348506a84705d4dfdb34c515ca.gif",
            "https://64.media.tumblr.com/b26274f7ca3cc2be0f57455d37f6fc3d/b2305c9cbdfcead8-9e/s400x600/7d4fca0185d8638e31b3291b842a76b574097e24.gif",
            "https://64.media.tumblr.com/3e9a40761ee2b88ac975ed067ff4a2cd/4c525f1ea3ee316c-2a/s400x600/b8dd861535112cba4a0571847fe360daf7a91840.gif",
            "https://64.media.tumblr.com/013ec64f6f2675e3fe1e05bad9cc50e6/385017dfcbf06c78-44/s400x600/e078886ac9ffd6c61a3e018797b5161dd31dfa5b.gif",
            "https://64.media.tumblr.com/a6325150add35929589900471871d74d/3e85c9e2cf4e143b-ee/s400x600/cad0561cd9a7b0d8328fdef9145cfc0f62f829c7.gif",
            "https://64.media.tumblr.com/4a615475d4c1f4d25f844d5cf8178736/3e85c9e2cf4e143b-38/s400x600/526f3121aed60e3388a234c38bacdbda2a9886ea.gif",
            "https://64.media.tumblr.com/013ec64f6f2675e3fe1e05bad9cc50e6/385017dfcbf06c78-44/s400x600/e078886ac9ffd6c61a3e018797b5161dd31dfa5b.gif",
            "https://64.media.tumblr.com/a6325150add35929589900471871d74d/3e85c9e2cf4e143b-ee/s400x600/cad0561cd9a7b0d8328fdef9145cfc0f62f829c7.gif",
            "https://64.media.tumblr.com/4a615475d4c1f4d25f844d5cf8178736/3e85c9e2cf4e143b-38/s400x600/526f3121aed60e3388a234c38bacdbda2a9886ea.gif",
            "https://64.media.tumblr.com/27411337ecc1befc711c37901ac0ec82/4827281e384f731a-4f/s400x600/c0439f690808fe6d66d45fc8fad5add257c89eb7.gif",
            "https://64.media.tumblr.com/e8d4a8329d6455f5e4c1bc8728d7734b/4827281e384f731a-d6/s400x600/d09ebebec93a59312fa8ea7cbc78c5e88df5edde.gif",
            "https://64.media.tumblr.com/171a9de413152726c831d114e734f7e0/4827281e384f731a-1a/s400x600/f74145be7a010e5d73797f3b233f2128574f0b2d.gif",
            "https://64.media.tumblr.com/e9eb891db1bfa96a61c5a6c9e33f7838/4827281e384f731a-4a/s400x600/864bf2ca8bf218df2f008645c246dd4cc4010bd8.gif",
            "https://64.media.tumblr.com/48ad6eaa70ffdef286d6d6c02200bdaf/3901bd35306afb4f-20/s250x400/7293826bd444fe7227d35b00548d45746017fe36.gif",
            "https://64.media.tumblr.com/847e4be28a5b80af26f3c35c51c1901c/c1acc287e8c47ad4-30/s540x810/74d233498810c2d540a7852fdc7374b53f596381.gif",
            "https://64.media.tumblr.com/e10f3b9b293be704b5b2db9c840e4ebb/6044dbb45026d18c-b0/s400x600/b62599520b27b0ebb234355d0280ad3294376bcc.gif",
            "https://64.media.tumblr.com/76722c55de472cd43404b30b5c40cfdc/6044dbb45026d18c-af/s400x600/cf5aa0818a924fa90d9de7f7f78fab77fd001374.gif",
            "https://64.media.tumblr.com/7573d7678d748b9e3fe0620d82d62c6b/6044dbb45026d18c-9d/s400x600/b3c15f50479d935d9480ba8723b7f63c5d174692.gif",
            "https://64.media.tumblr.com/a9ee96dde364750f8c334379bdd29c93/6044dbb45026d18c-1a/s400x600/7d79c630c59b2bc410d2f8219f8340167096797b.gif",
            "https://64.media.tumblr.com/9b448337a6f7ed6ca84cf8b57c24293d/c06ca3690cfe4471-26/s500x750/62cee7674b29a72df603d6eecd9790495e22dfee.gif",
            "https://64.media.tumblr.com/b081e5ced9d2290fbd11877151dbaff2/c06ca3690cfe4471-e2/s500x750/8f61159c9e460d599971831200432d4d5128af59.gif",
            "https://64.media.tumblr.com/770804a5879c59766e0c7b7bc6fe1021/c06ca3690cfe4471-88/s250x400/307bad9d9745967992e733b1fe328948982bc9a3.gif",
            "https://gfycat.com/flawedsadgonolek"]

        self.bot.ireh_gif = ["https://gfycat.com/OpenEnchantedArcherfish",
            "https://gfycat.com/MediumScentedGeese",
            "https://gfycat.com/RelievedThirdBoaconstrictor",
            "https://gfycat.com/ShinyWhimsicalBlackbird",
            "https://gfycat.com/TheseAbsoluteFossa",
            "https://cdn.discordapp.com/attachments/680370499297345549/740189290876633168/20200804_080935.gif",
            "https://tenor.com/view/purple-kiss-gif-19356837",
            "https://tenor.com/view/ireh-purple-kiss-seoyoung-gif-19356698",
            "https://tenor.com/view/ireh-purple-kiss-gif-19356772",
            "https://tenor.com/view/purple-kiss-ireh-chaein-dosie-gif-19356828",
            "https://tenor.com/view/ireh-purple-kiss-gif-19356800",
            "https://tenor.com/view/done-ireh-purple-kiss-rbw-gif-19603737",
            "https://cdn.discordapp.com/attachments/680370499297345549/806562940525346816/image0.gif",
            "https://cdn.discordapp.com/attachments/680370499297345549/806562941431447602/image1.gif",
            "https://cdn.discordapp.com/attachments/680370499297345549/806682353052811264/image0.gif",
            "https://64.media.tumblr.com/59eb05d8882dc377b5362ef2a6c3af3c/9b513bde8b638a0a-df/s540x810/6e0fb67e8051ebfc80e1abd3c3adf15724c936af.gif",
            "https://64.media.tumblr.com/d87075a8752d6cb20a3db9038a37c957/ead734e0a9b83979-ee/s540x810/aac105d74806cff802898c80a4f96da2727e6747.gif",
            "https://64.media.tumblr.com/2e9a1cc47d8906080eb740b11638764a/812bdbc740efda23-48/s540x810/f773923883f4b5e6aa71f2408023048e5b455ce6.gif",
            "https://64.media.tumblr.com/3eba48d4a2a53baa78424b6af84d3e54/42ba22191a1579cf-bf/s500x750/ceb672b8ad5830ea0905ef5bc0a14236332f4514.gif",
            "https://64.media.tumblr.com/98f2ba155dcd8acadcc69d3d48bdb073/d1342c671794fa4b-8c/s640x960/7e9c2b074cfe36184ecf9233c969b4793f6ab53b.gif",
            "https://64.media.tumblr.com/d98a15f7d57487d7bbebee299ff259a3/3901bd35306afb4f-12/s250x400/e30da818f19fa145fce8c3d5e6528689998903bd.gif",
            "https://64.media.tumblr.com/ba079cfb2d45496dbfc26d48b5d5e9dc/f1d5344b7415e2dd-f0/s400x600/efe1f9ef36b68bdb7dd1fdf53d059d41b14328bd.gif",
            "https://64.media.tumblr.com/6ce7f6f7449fcfb0c160d4a1edaa2cdf/8b3898502acb86ec-7e/s400x600/92ee857e91e2dbd6c4857716da0db649fc58d724.gif",
            "https://64.media.tumblr.com/f88cce4d5dc4527575ea9eb0d31f7d77/8b3898502acb86ec-c4/s400x600/1c7fe68650119e996c815ef05dad71252bbc43eb.gif",
            "https://64.media.tumblr.com/a3f6fa36b84dced82ab1a74a63b8b360/8b3898502acb86ec-d3/s400x600/c526d7c5fc7a101769883540558cedce617f18af.gif"]

        self.bot.chaein_gif = ["https://gfycat.com/filthyforkedfirecrest",
            "https://gfycat.com/miserablejealousbengaltiger",
            "https://gfycat.com/wateryecstaticamazonparrot",
            "https://gfycat.com/easymistyflea",
            "https://gfycat.com/shrillglisteninggalapagospenguin",
            "https://gfycat.com/slightampledaddylonglegs",
            "https://gfycat.com/negligibleglumeagle",
            "https://gfycat.com/deadverifiableabyssiniancat",
            "https://gfycat.com/excitablekaleidoscopicgadwall",
            "https://gfycat.com/cloudyraggedarchaeocete",
            "https://gfycat.com/accomplishedtastyarmednylonshrimp",
            "https://gfycat.com/lamegrouchyharborseal",
            "https://tenor.com/view/chaein-purple-kiss-chaeyoung-gif-19298314",
            "https://tenor.com/view/chaein-purple-kiss-my-heart-skip-a-beat-gif-19356315",
            "https://tenor.com/view/chaein-purple-kiss-gif-19356429",
            "https://tenor.com/view/chaein-purple-kiss-lee-chaeyoung-gif-19356652",
            "https://tenor.com/view/purple-kiss-gif-19356669",
            "https://tenor.com/view/go-eun-chaein-purple-kiss-gif-19356750",
            "https://tenor.com/view/chaein-purple-kiss-gif-19356764",
            "https://gfycat.com/indolentrecentaphid",
            "https://cdn.discordapp.com/attachments/663392215929716737/806562479089647696/image0.gif",
            "https://cdn.discordapp.com/attachments/663392215929716737/806562494847123496/image0.gif",
            "https://cdn.discordapp.com/attachments/663392215929716737/806572368968810536/image0.gif",
            "https://cdn.discordapp.com/attachments/663392215929716737/806682412150947870/image0.gif",
            "https://64.media.tumblr.com/1309a2faae1d1cdb79f05509ff62fd94/9b513bde8b638a0a-8a/s540x810/4d5f3b687c673ebdbaae4a2a961441060a6a8ac0.gif",
            "https://64.media.tumblr.com/62c1d068235910a9ffa5dc209fdc618c/42ba22191a1579cf-64/s500x750/7a02f34697bf936bfe52be7cfe1d35c8ce7a723d.gif",
            "https://64.media.tumblr.com/c5d733b872007d6cf2444a08e3a2f488/d1342c671794fa4b-f6/s640x960/34434a09ea4ea52ad212fcf870a7764165425333.gif",
            "https://64.media.tumblr.com/c3694bf83ed6a18a151e4ea89ad29bbe/e73d6fee7b1fa578-14/s400x600/9e1c6205230f442e49f7e1102c7cef20dea075db.gif",
            "https://64.media.tumblr.com/dda3e7fc9262c5f0e1d7bfced2c3e567/e73d6fee7b1fa578-b0/s400x600/73a156ccaf6c2183c532612a5caaf99ea88bf542.gif",
            "https://64.media.tumblr.com/132f10731ce002981cb926e3d6a6dcb5/951828803b11f948-d5/s400x600/09d2815a1d7d4b65d23c95a2bca9efdd870a58f4.gif",
            "https://64.media.tumblr.com/f10c5f9fc074a304ce5b642a3e16120f/951828803b11f948-a1/s400x600/39f6faa396a0e37597aafc89ddc70b071b55c7f4.gif",
            "https://64.media.tumblr.com/d4a3739611aea045852721c3e299f9fe/951828803b11f948-42/s400x600/8d11de7b0d1091bbd68c92374a9b415e8fa53cdf.gif",
            "https://64.media.tumblr.com/b0a8892af0160a4555a3b08d9c987215/23e05be611939d87-2a/s1280x1920/6fb1149c5ecd7cd3e93168f02b325a9994a8f6bd.gif",
            "https://64.media.tumblr.com/b5c8fe6f5a97feeb45efd104e00c2ec2/23e05be611939d87-9b/s1280x1920/06fd16844f1f41aaf77a765b280a71025a372fc6.gif",
            "https://gfycat.com/nervoussecondhummingbird",
            "https://64.media.tumblr.com/1fc6dc07d18384952d1665208436f2f5/945c1633a2a19db2-7c/s400x600/08a7c00f563d8c55cf45d482ceab7ce8b58c03b4.gif",
            "https://64.media.tumblr.com/8c466d5f353c7bc33b8f2d7386e2b632/945c1633a2a19db2-ab/s400x600/7a690b9a0b9196c4617e387cc2a7bf43402dbc22.gif",
            "https://64.media.tumblr.com/3b7cc5cd697f4cf2458ec328487c0bd6/945c1633a2a19db2-ed/s400x600/4643f37ef9976e39920ac29748776ad9420fecb8.gif",
            "https://64.media.tumblr.com/ad294cf4deded23a4a038f8a958d5dc9/945c1633a2a19db2-f4/s400x600/a9fae2b34ed163513f938f53e85f1a14e9cc3863.gif",
            "https://64.media.tumblr.com/95e6d7f63701d519f3c1eb12fd263835/3901bd35306afb4f-a2/s250x400/701aac909677968b4bdf6431d4a7bc38ca8414df.gif",
            "https://64.media.tumblr.com/e067006510f0fea9ad60709144a9a226/fc79438548c1b2db-ba/s1280x1920/bde6b3a4f65311742db60a3a90e3b32b3b2a153e.gif",
            "https://64.media.tumblr.com/ce304b78a0baed3281603649b1285075/857ff8d0edb76bdf-03/s640x960/5fa8dcd208844216c2c1c6ec747a82716473c915.gif",
            "https://64.media.tumblr.com/aaa4c1be55627e6afcea7009c52feaa8/61fe6758996a5d80-f2/s640x960/bb0def51e97aa4d407352ae34a357fae7edac744.gif",
            "https://64.media.tumblr.com/d2b6e4c2508fb2e33d27f3fea507ae62/969c9c7a6df6d51e-27/s640x960/54dc123ab6bbd72589f770020ba57e7b1d2b964c.gif"]

        self.bot.swan_gif = ["https://gfycat.com/favoritewhoppingblueshark",
            "https://gfycat.com/babyishbelatedanaconda",
            "https://gfycat.com/adoredscrawnyleveret",
            "https://gfycat.com/forsakendishonestgrayreefshark",
            "https://gfycat.com/failingimpressionableirishdraughthorse",
            "https://cdn.discordapp.com/attachments/547946771968557076/740189347369844766/20200804_081816.gif",
            "https://cdn.discordapp.com/attachments/547900536565924104/791258374724386836/SwanPurple.gif",
            "https://cdn.discordapp.com/attachments/547946771968557076/806562262226960404/image0.gif",
            "https://cdn.discordapp.com/attachments/547946771968557076/806562330199851038/image0.gif",
            "https://cdn.discordapp.com/attachments/547946771968557076/806562308004380743/image0.gif",
            "https://cdn.discordapp.com/attachments/547946771968557076/806562366539563088/image0.gif",
            "https://cdn.discordapp.com/attachments/547946771968557076/806566967233871872/image0.gif",
            "https://cdn.discordapp.com/attachments/547946771968557076/806682442730700850/image0.gif",
            "https://64.media.tumblr.com/077a45559d5110427ee1caa62dfe3815/9b513bde8b638a0a-1f/s540x810/05209dca591cd1e0594b11665b89e87cd25b03d6.gif",
            "https://64.media.tumblr.com/aaf04687d76df105639ed7a960a830e5/a5ff213f0cfcdec9-3b/s540x810/79f0dfc276c6427a63cc5adabae1901a976491a7.gif",
            "https://64.media.tumblr.com/361da332ecd0c170235e8aed36d69342/42ba22191a1579cf-b0/s500x750/85af39305b8d9547fcb7f493d553c26e2e838adc.gif",
            "https://64.media.tumblr.com/51fdc57d6f06ffadca71f9980ae31662/d1342c671794fa4b-56/s640x960/0de98d16fe62f6ae6571bb0576470a4f62c3b69a.gif",
            "https://64.media.tumblr.com/c77a8eb6dc545e207dfbce27bd479d60/dcc849556f45958b-20/s400x600/67d6a69ad3203458e95c906e81c1a1e431859c59.gif",
            "https://64.media.tumblr.com/fa1cdde3a4cfa62249c0d18e6a1dac28/dcc849556f45958b-69/s400x600/b8f5757f6f142281890a271dc637952403d150d3.gif",
            "https://64.media.tumblr.com/645c34d9650d6fd6cafba4c04a059320/0c6b9dca8b3140ff-0f/s400x600/91fceb8ff63e9933b47b21914c065df9328ed75f.gif",
            "https://64.media.tumblr.com/0130fe2f25c6f62c69cf90348ace8149/0c6b9dca8b3140ff-62/s400x600/e23e8a70cd579c4a14331b7c853ef5e4b65edf85.gif",
            "https://64.media.tumblr.com/90a38b273b53d3ff4023ab4ccf56548b/e09a5b0da7fe1dae-4c/s400x600/0e09d4fa2f13a88879390a517cb85ba7ca7210aa.gif",
            "https://64.media.tumblr.com/fafc8437cda0a13f17cf7f3aab7be761/e09a5b0da7fe1dae-81/s400x600/dde08c026c7b03af6221436ed9ccde59c189ad51.gif",
            "https://64.media.tumblr.com/cd08e7ed02c4d7e147bb09104f4c9776/3901bd35306afb4f-ba/s250x400/369e519a8316d128dc8d93236e179d9331845766.gif",
            "https://64.media.tumblr.com/b25a2e2d6813b53e70fb8227bc9966e8/f1d5344b7415e2dd-82/s400x600/42c09e2e2ddf8a2375059a2291f3964ea37a2f8d.gif",
            "https://64.media.tumblr.com/a008fb2ef9f6e4bb61f8f6645ca27dd4/8d6d7e1a2219a1f1-df/s540x810/8e8b30cc7dd925f3c11dc7774cee1e71766a56ce.gif"]

        self.bot.purplekiss_gif = ["https://cdn.discordapp.com/attachments/547946619845345280/806564359551582208/image0.gif",
            "https://cdn.discordapp.com/attachments/547946619845345280/806571926235250728/image0.gif",
            "https://cdn.discordapp.com/attachments/547946619845345280/806572758691217448/image0.gif"]

        self.bot.pk_teasers = ["https://www.youtube.com/watch?v=k15XyaoIP0E", #.yuki
            "https://www.youtube.com/watch?v=Dye6lE4Nxqg&ab_channel=PURPLEKISS", #.goeun
            "https://www.youtube.com/watch?v=McH3WeahWzA&ab_channel=PURPLEKISS", #.chaein
            "https://www.youtube.com/watch?v=I_tiX8HlasI&ab_channel=PURPLEKISS", #.swan
            "https://www.youtube.com/watch?v=yR4gq-2wJnk&ab_channel=PURPLEKISS", #.dosie
            "https://www.youtube.com/watch?v=eWAh5yzikBQ&ab_channel=PURPLEKISS", #.ireh
            "https://www.youtube.com/watch?v=PHOaqnOFR28&ab_channel=PURPLEKISS", #.jieun
            "https://www.youtube.com/watch?v=0qKI9JhAGAk&ab_channel=PURPLEKISS"] #.group

    @commands.command()
    async def purple(self, ctx, kiss, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Purple Kiss {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if kiss == "kiss" or kiss == "k!ss":
            if arg == "yuki":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yuki :heart:')
                await ctx.send(random.choice(self.bot.yuki_gif))
                await ctx.message.delete()
            elif arg == "na goeun" or arg == "goeun" or arg == "nagoeun":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Na Goeun :heart:')
                await ctx.send(random.choice(self.bot.nagoeun_gif))
                await ctx.message.delete()
            elif arg == "jieun" or arg == "park jieun":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jieun :heart:')
                await ctx.send(random.choice(self.bot.jieun_gif))
                await ctx.message.delete()
            elif arg == "dosie":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Dosie :heart:')
                await ctx.send(random.choice(self.bot.dosie_gif))
                await ctx.message.delete()
            elif arg == "ireh":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Ireh :heart:')
                await ctx.send(random.choice(self.bot.ireh_gif))
                await ctx.message.delete()
            elif arg == "chaein":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chaein :heart:')
                await ctx.send(random.choice(self.bot.chaein_gif))
                await ctx.message.delete()
            elif arg == "swan":
                await ctx.send(f'<@!{ctx.author.id}> is talking about Swan :heart:')
                await ctx.send(random.choice(self.bot.swan_gif))
                await ctx.message.delete()
            elif arg == "teaser" or arg == "teasers":
                await ctx.send(f'<@{ctx.author.id}> is watching a Purple K!ss member trailer :purple_heart:') 
                await ctx.send(random.choice(self.bot.pk_teasers))
                await ctx.message.delete()


def setup(client):
    client.add_cog(PurpleKiss(client))