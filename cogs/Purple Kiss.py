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
            "https://tenor.com/view/yuki-mori-koyuki-mworikoyuki-purple-kiss-gif-20203328"]

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
            "https://64.media.tumblr.com/7e8ed147bb5d3761c6696c0f586a5869/af7b14fd731e3a5e-1d/s400x600/2cfe95e0a817b6797bd7cea9aea676b16d724fd1.gif"]

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
            "https://64.media.tumblr.com/4b8372f56319b7c63a1928dc6f39342e/8519990dd2148025-66/s400x600/238d335446c95437f39e1843559c632bfe9c268a.gif"]

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
            "https://64.media.tumblr.com/f3024a917a40aa23b8c6ab59f793895a/2a8a03211be7a7a7-90/s400x600/3edaaa5fc998b6fdd75b9df141a48996de7df3cb.gif"]

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
            "https://64.media.tumblr.com/98f2ba155dcd8acadcc69d3d48bdb073/d1342c671794fa4b-8c/s640x960/7e9c2b074cfe36184ecf9233c969b4793f6ab53b.gif"]

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
            "https://gfycat.com/nervoussecondhummingbird"]

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
            "https://64.media.tumblr.com/0130fe2f25c6f62c69cf90348ace8149/0c6b9dca8b3140ff-62/s400x600/e23e8a70cd579c4a14331b7c853ef5e4b65edf85.gif"]

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
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Yuki :heart:')
                    await ctx.send(random.choice(self.bot.yuki_gif))
                    await ctx.message.delete()
            elif arg == "na goeun" or arg == "goeun" or arg == "nagoeun":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Na Goeun :heart:')
                    await ctx.send(random.choice(self.bot.nagoeun_gif))
                    await ctx.message.delete()
            elif arg == "jieun" or arg == "park jieun":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Jieun :heart:')
                    await ctx.send(random.choice(self.bot.jieun_gif))
                    await ctx.message.delete()
            elif arg == "dosie":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Dosie :heart:')
                    await ctx.send(random.choice(self.bot.dosie_gif))
                    await ctx.message.delete()
            elif arg == "ireh":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Ireh :heart:')
                    await ctx.send(random.choice(self.bot.ireh_gif))
                    await ctx.message.delete()
            elif arg == "chaein":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Chaein :heart:')
                    await ctx.send(random.choice(self.bot.chaein_gif))
                    await ctx.message.delete()
            elif arg == "swan":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Swan :heart:')
                    await ctx.send(random.choice(self.bot.swan_gif))
                    await ctx.message.delete()
            elif arg == "teaser" or arg == "teasers":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@{ctx.author.id}> is watching a Purple K!ss member trailer :purple_heart:') 
                    await ctx.send(random.choice(self.bot.pk_teasers))
                    await ctx.message.delete()


def setup(client):
    client.add_cog(PurpleKiss(client))