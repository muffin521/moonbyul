import discord, random, os
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
gareth = 389897179701182465

class gamerPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.mina_gif = ["https://tenor.com/NUon.gif",
            "https://tenor.com/4vrC.gif",
            "https://tenor.com/HydV.gif",
            "https://tenor.com/brQ1g.gif",
            "https://media.giphy.com/media/qzuGfHYC152dG/giphy.gif",
            "https://64.media.tumblr.com/6180c42fe314efaa840ab99c1f461550/c8dd9ab35553aa4d-7e/s540x810/e377c67b5af8309e2c9120f2ce95bfd1c44c4452.gif",
            "https://64.media.tumblr.com/567ebdddcad6bd8cd8bc1936b6e965ee/2617704d59173453-4d/s400x600/8039fbc724642a74527ffabd09d4df4b5edb7ae6.gif",
            "https://64.media.tumblr.com/ba76b980d2cd735420cf0827881fc091/b8fef663de1f7a99-1d/s400x600/9fd70725b5d8d1326247604dcfdecd420151df1c.gif",
            "https://64.media.tumblr.com/b9baab82f79bf54ae9d55dfeeae404f7/c2c0d737ddf77bee-31/s400x600/21a1e7283aef69779b6e964e07522ed17fe686b1.gif",
            "https://64.media.tumblr.com/7f447af2c8af7859490e4ad1be7fd08c/7378d62a6b5e080d-7b/s400x600/3c087510487f48bd494604058246679ec819841d.gif",
            "https://64.media.tumblr.com/e247fe8c9fe7e8c56731e5fe1131a7c5/d6d42f274ab81eb9-ed/s540x810/9d022e647bfc39663d2884d252594e522271345f.gif",
            "https://64.media.tumblr.com/9f60506b39f318fbd864ba46c5d04cf6/ea259c1353ae60d4-20/s400x600/1e8426d4f812ca6f890086991969290af5828cfd.gif",
            "https://64.media.tumblr.com/692e8b5944bf0c03651a4bfb9475fe9c/fbddd6465e73e5be-88/s540x810/cccb18e6439e1d483e1a2c030ce6c35491a1b488.gif",
            "https://64.media.tumblr.com/1962f8fb8b35e6202ce1968408b790d4/ac86dbbe396b04a5-0e/s540x810/71f05ff7c39623e7f31ae3a22b5aed063758c690.gif",
            "https://64.media.tumblr.com/26e9c4978b68f728f098f1dd7abcc666/e330829990f571a5-66/s540x810/e26e99166689f2c7373af3de241ce397954f2a39.gif",
            "https://64.media.tumblr.com/6dd8a524c52d9b56a10e7feb12301589/928dd6e3d0ee7a5a-5c/s540x810/d79eb5c8a29713e1181e888fad2efd1c927bc7de.gif",
            "https://64.media.tumblr.com/79ca43dcddbaef5afdbb82995926ce41/ccab6d71ba02df9b-91/s400x600/42a73d54093d796237cff9b42dee10aefa1cad27.gif",
            "https://64.media.tumblr.com/54bd81a8abe22d7c9b7785dde77fdf3b/2cc21bec233193aa-a9/s400x600/6b7a549b558548b7f92ea3d273b8457b88cc1a68.gif",
            "https://64.media.tumblr.com/28474864d922eef6bbeeeb71d7fbde92/7e7e6dc3eceb02ab-a3/s400x600/7b53db3b6cb0a391c28c69468861ec70805f5aec.gif",
            "https://64.media.tumblr.com/06f2790f48516cee780817da28afb7f3/26be919e22fb6fcd-52/s540x810/ad419450ee94866247d66717305065273d79c11c.gif",
            "https://64.media.tumblr.com/c3a71d0061e4647ebcc082374708b700/35a57a49f126c5fe-53/s400x600/52dd4cd2f9fffce9e8320d5298cd995920d544d7.gif",
            "https://64.media.tumblr.com/3629e5aed89ff2a1aa94a51a9ac0396d/ba269b895e46fb77-2d/s400x600/766afd4caedc073d6001eb909116fe2c0fea4c4d.gif",
            "https://64.media.tumblr.com/bd6ea2f34657fe54fcd9c301af147f3e/35c4ee5e1bee21b0-ba/s400x600/7afe24c361153f19344dc45a7c4bdb36724279d0.gif",
            "https://64.media.tumblr.com/143de6013efe79c8827fa2a08d5a6ed1/68d13c07c1735b1e-f2/s540x810/f3180f3bc9fd9405c567594ddde716b403320fb9.gif",
            "https://64.media.tumblr.com/e98884d5a77fd0c585230441b97ba15f/603cdb5ab920c1df-ad/s400x600/7c2900a8441076d1bc0651d51361da4b04812aaf.gif",
            "https://64.media.tumblr.com/18df16ccae26f9adc3a6a9dedb05e97a/74bc82b9e06f35e0-0e/s400x600/1531b95fa5f28f04c50a246eb4b9021614187ec2.gif",
            "https://64.media.tumblr.com/d752fc4aae4b78cf40a03d493a2bf396/7732225bb8893b18-5f/s400x600/1c1c17145470b9bbf7e7aa57e26c76ca59509483.gif",
            "https://data.whicdn.com/images/289498109/original.gif",
            "https://64.media.tumblr.com/86545621ad6214b8aff2f5e1a6a4fcfc/186cb8bbcfab3654-60/s400x600/e700ef010b40ecd240cd486b069bd85adfefac96.gif",
            "https://64.media.tumblr.com/6755b1038a238e0e3493f88272c4f5ee/2089d1a9445d705c-38/s400x600/5aac1b865a3ffd271e427ceaa37ba897fdcc3c81.gif",
            "https://64.media.tumblr.com/5b6753dff1d79eb4695ac7e1fdee4521/3306e196c47c89f3-c8/s400x600/64f8a5acfa378951ad6f6a2d6031d330069186fc.gif",
            "https://64.media.tumblr.com/b4ad4f3a9ee5d520abb0f023ab98fcf0/043e143bf9aca2c2-99/s540x810/4449fd38ebd0b6d77daa47b37b76f99a28913685.gif",
            "https://64.media.tumblr.com/f8d1608c175164332e7135573855155d/tumblr_p7gvk50xIt1wi7204o1_540.gif",
            "https://64.media.tumblr.com/569bc66343344560422e7d3446b9b704/tumblr_pir6g7HSqA1wj9n4bo1_400.gif",
            "https://64.media.tumblr.com/54b47b0162ad83cfda6e2b158416dbc5/46daa3353e78681b-34/s540x810/5a706736355154b290cec474d6d5265a6e90d9e9.gif",
            "https://64.media.tumblr.com/1c61bec91ad3a8bc617ba65afea6e2d5/46daa3353e78681b-c2/s540x810/948d07e92aed7b5d03dd130d8f9002f918dfdae7.gif",
            "https://64.media.tumblr.com/058f2c58a8b5faee4b63b8ee5aa3b20c/a74ec8775c4e199d-c1/s400x600/b6a3f545f11bf6052ad4ef7d3995572ec48e606c.gif",
            "https://64.media.tumblr.com/828531bb96a302009c3bcfb1adfd9cc3/df9785efa4b7ac82-54/s400x600/91b19825d1d091a589d29db0d5c8dccd57859b85.gif",
            "https://64.media.tumblr.com/162a741e154557e2c3c5c5703a8a1689/tumblr_inline_o8xq6duwiN1rifr4k_540.gif",
            "https://data.whicdn.com/images/324201333/original.gif"]

        self.bot.sana_gif = ["https://tenor.com/view/sana-twice-kitty-dance-kpop-gif-17314571",
            "https://media.giphy.com/media/xUySTXXuWvIVDggisg/giphy.gif",
            "https://tenor.com/view/sana-sana-twice-twice-sana-minatozaki-sana-gif-18564320",
            "https://tenor.com/view/sana-twice-heart-minatozaki-jpop-gif-10758695",
            "https://tenor.com/view/twice-shyshyshy-sana-dance-cute-gif-9784878",
            "https://tenor.com/view/sanapinkhair-sana-twice-sana-gif-18677676",
            "https://tenor.com/view/samichae-sana-twice-serious-gif-15019560",
            "https://tenor.com/view/fancy-twice-sana-gif-14010342",
            "https://tenor.com/view/twice-minatozaki-sana-fix-hair-gif-12344636",
            "https://tenor.com/view/fancy-twice-you-sana-gif-14137521",
            "https://tenor.com/view/sana-minatozaki-sana-twice-jyp-jyp-entertainment-gif-18654791",
            "https://tenor.com/view/performance-stage-music-dance-dance-performance-gif-15855577",
            "https://tenor.com/view/twice-sana-fancy-dance-gif-14035182",
            "https://tenor.com/view/performance-stage-music-dance-dance-performance-gif-15855648",
            "https://tenor.com/view/sana-fancy-dance-cute-fancy-gif-15434915",
            "https://tenor.com/view/sana-minatozaki-sana-twice-fancy-jyp-gif-18654790",
            "https://tenor.com/view/fancy-twice-cutie-sana-sexy-gif-13983688",
            "https://tenor.com/view/sana-ohyo-ohyo-ohyo-sana-fancy-fancy-sana-twice-gif-13983779",
            "https://tenor.com/view/twice-sana-fancy-stare-gif-14017602",
            "https://tenor.com/view/sana-twice-sana-more-more-sana-cute-sana-clumsy-gif-18766260",
            "https://tenor.com/view/sana-twice-wondering-thinking-bored-gif-6184780",
            "https://tenor.com/view/welcome-twice-sana-minatozaki-sana-vocalist-gif-17907768",
            "https://tenor.com/view/sana-twice-heart-point-gif-18331546",
            "https://tenor.com/view/sana-cute-face-gif-10623438",
            "https://tenor.com/view/twice-cheerup-sana-shyshyshy-gif-6325860",
            "https://tenor.com/view/sana-twice-kpop-gif-5328449",
            "https://tenor.com/view/kpop-twice-sana-gif-5677495",
            "https://tenor.com/view/sana-sad-crying-twice-twice-sana-gif-16875037",
            "https://tenor.com/view/twice-feel-special-twice-feel-special-kpop-gif-19924880",
            "https://tenor.com/view/twice-kiss-sana-cute-flying-kiss-gif-14041423",
            "https://tenor.com/view/sana-sana-twice-minatozaki-sana-twice-sana-twice-gif-14011183",
            "https://tenor.com/view/twice-sana-cheese-kimbap-gimbap-bros-gif-11163723",
            "https://tenor.com/view/sana-momo-sana-twice-momo-twice-twice-gif-13983819",
            "https://tenor.com/view/sana-sana-twice-minatozaki-sana-gif-18815585",
            "https://tenor.com/view/sana-sana-twice-twice-sana-twice-minatozaki-sana-gif-13495040",
            "https://64.media.tumblr.com/c45f65595b9843ea92dde971eb32b00c/ab666d001db0126c-57/s540x810/ce7be132787345b2639177b16960e72ba3127126.gif",
            "https://64.media.tumblr.com/9677e14efb1733e32c5f662fd9d57ff3/tumblr_pyynpfUc7G1vp9gyko1_540.gif",
            "https://64.media.tumblr.com/40de841f0442df520520265fabe8fa16/4a119414513c0464-79/s540x810/2ae18f0131c07088b53e4ea528f8860f804f6738.gif",
            "https://64.media.tumblr.com/d4dd3b4391f7af7fa512a6d21e9f5388/da8528a756c146b5-88/s540x810/99e38a3529ba48c702b46c51518d5a0cda9e3744.gif",
            "https://64.media.tumblr.com/2f063543ee74fb543c3a8387c1771f41/tumblr_pb79uxjM4C1vp9gyko1_540.gif",
            "https://64.media.tumblr.com/c16874d4fd41225344a087939dad90e1/tumblr_pqu0p3Cydf1s2vcg0o1_540.gif",
            "https://64.media.tumblr.com/259be50125fceab70de6a7011c5dc167/e4fbc57b43f7f1f8-08/s540x810/576364e58af4d04f63c7e19ff33f3f8532879db9.gif",
            "https://64.media.tumblr.com/01dc22661fc58f007523e3953bdb0bb6/19228f63c0e446b2-ac/s500x750/a3f18386c896f64058edc82f7ccf05ee25d14981.gif",
            "https://thumbs.gfycat.com/ScaredEverlastingIsopod-size_restricted.gif",
            "https://64.media.tumblr.com/8282eefa0ac1156454ab0ebb7671f1a5/727d20610e6da52e-40/s400x600/28cb94ef9088aa53c415aa7355ad83d421c4d269.gif",
            "https://64.media.tumblr.com/b9089c0f6c80d802dc993ad5cf1d5c94/b04f9a79884a5888-5c/s400x600/4d5390583ca4a85d8bf7d8f7e5250f5acb570652.gif",
            "https://64.media.tumblr.com/550a0ec1a7c587107f5a2bcb15927e03/5c0155eada2c6e88-db/s400x600/dc4c0e5ae0d5ef6a73f0641953a59df5e67dcc19.gif",
            "https://64.media.tumblr.com/cb3e543f525664c36d9f4968ff5f55f8/5c0155eada2c6e88-d7/s400x600/3ea66742cb46963807a60f84922c0c5e083d377b.gif",
            "https://64.media.tumblr.com/b7ce2f0c26800a56af44eeb7b9140a46/69b8e81674a00f96-db/s400x600/0d4b116db5c0e8d1f6100240029acc139d934ffd.gif",
            "https://64.media.tumblr.com/e2a28a05af29b58870f4f3067d3c11c5/833b115b2a373c64-87/s400x600/b82885ff1f0fdf2c6e1e1ca96de30bc4e5723972.gif",
            "https://64.media.tumblr.com/6925bb9c6a5976f1a8d1d9802d471202/660a7cd1c9d2d87c-b4/s400x600/0ceabe2b16cb988efa2af7ac3e5f892bac5493ec.gif",
            "https://64.media.tumblr.com/69ab6d67febb76dd0946fcc37cc32d56/ebf99922fb0abf34-ee/s400x600/02d9a9c7932726bfd4667dea02a9119e12d44f9e.gif",
            "https://64.media.tumblr.com/be4dc2af1c652cc588bf4a55f49a7762/2ad012ec6b43bd2e-7e/s540x810/a2272105620bf9ecfd353a98800dcdfa90a74109.gif",
            "https://64.media.tumblr.com/c3a44226c2e64848be8132b21be1b4b5/956f95ff1cbd7cf3-89/s400x600/5d0cda85e491514b7d7ab128c80c4ea698e8f28e.gif",
            "https://64.media.tumblr.com/b67ee8ae69c4dcf68254ef7534e33e5d/7a1cd8fb843a292e-3c/s400x600/5423c6023ce96e9019dc6143088f4b50171d49a8.gif",
            "https://64.media.tumblr.com/09005ece334ab78b3a809462f6d4a23b/7a1cd8fb843a292e-ca/s400x600/582291cfa02959a4234e58a034ba664ef3f6edf7.gif",
            "https://64.media.tumblr.com/85a0efb6af08c62f7d7a27e1582103fb/7a1cd8fb843a292e-d5/s400x600/c12b5a5b168f1770c127d35b59e835703c42c352.gif",
            "https://64.media.tumblr.com/d30055bc75b2d11f8f92118d1b0ca3ac/0f1cee4ae0bed0e8-79/s540x810/1f7a318b63d7c22d884a8cb8465f9052d98eba52.gif",
            "https://64.media.tumblr.com/e2b70dd32d0723c0877498e2322828cd/0f1cee4ae0bed0e8-be/s540x810/335c731510897034fb77e66e7e6818c3d056bafa.gif",
            "https://64.media.tumblr.com/e1099e2acd0f4727147890d4ce5b85ae/f03c20f3e1c19cf1-11/s400x600/c736bde84b48891a3b6f5a2d37d510947017348b.gif",
            "https://64.media.tumblr.com/89d31674cae0783bf20b53526f342fc4/61c22d8336ed71f1-c7/s400x600/cd6ca2731166b52e2fa80f351f3cb517c993b6dd.gif",
            "https://64.media.tumblr.com/b5487060dcd587d8410e7d3ce0335fef/d04b04cf6df40e68-6e/s540x810/e60082092a5f6a02be75f9b19a3a93b6c1cb8485.gif",
            "https://64.media.tumblr.com/a90d7753aa71656cf8399d69159deaab/0750779a379a18dd-36/s250x400/8d3f2257d1158dd1c6e5b0169a1c711c78d74249.gif",
            "https://64.media.tumblr.com/503e282c5ec6ece2387e9940b6b1ceae/e330829990f571a5-5f/s540x810/e2a1aa4f98c0a32cfd4febc64414297bbeb18d1f.gif",
            "https://64.media.tumblr.com/87d1275c8dea43c3406ed45f628b88b2/eed71e37f4e97fd2-2a/s400x600/6c324f219c05933d3f2c487c1dc65eacba1099a8.gif",
            "https://64.media.tumblr.com/020a6379509bfd3eef499057592bbda7/69cf3ec7ed1a7c95-1e/s540x810/9c6cb9c40cbb14f84bd3b1d8599d6b616f149966.gif",
            "https://64.media.tumblr.com/687811f28fcb10a67c41da55db729775/5d848e6241f1fc77-e8/s400x600/94d3770dfe438a07b4b3acb17c969c27acae0558.gif",
            "https://64.media.tumblr.com/7b716bd36d696be5e9fdf4cc04430717/5d848e6241f1fc77-7e/s400x600/a3d60e98a18318965b4753a5b1a5cc527b20c1c6.gif",
            "https://64.media.tumblr.com/b5dd3b86c87fa53294bc9965bcd1c61f/5b186261948cf8d5-d1/s400x600/73d415f076d89920ce9de0a8de225890bd39fed1.gif",
            "https://64.media.tumblr.com/ed9f48c33d11573076549452ec517678/fbb12b95165ab316-29/s540x810/28c86d2197bcd5af4fbcd310dbcdb18ea9475668.gif",
            "https://64.media.tumblr.com/80886a514f2a84d2e1258d41e9bb0cd2/a0f0e83cc309b44c-bb/s540x810/e994317748263ee831bfdf34d7b2a38da0c5987d.gif",
            "https://64.media.tumblr.com/e5ffc7f187e382ad093602f15edb42e5/e3e4bcfe91217c6f-0f/s400x600/d2f3967ec4e7a3fe1b408b011a4518aa098942d6.gif",
            "https://64.media.tumblr.com/fbdd48fbf7778bcb6cc02b8cc672c077/tumblr_p5eckzyl9q1x27aado2_250.gif",
            "https://64.media.tumblr.com/0ef93a79100a54665582069e9e8717a8/tumblr_pcqwh3ym9D1qmrscao2_250.gif",
            "https://64.media.tumblr.com/eca7c2d1677bbcda541e090e8dace4f3/tumblr_phuagdP8n71vmk10ho1_250.gif",
            "https://66.media.tumblr.com/385834fade433b2db2080392e0a6c752/tumblr_pqky3hbSrh1y7k8lwo1_400.gif",
            "https://i.pinimg.com/originals/6a/9f/6e/6a9f6e8e8adde644c2f397d0b1ff0d62.gif",
            "https://64.media.tumblr.com/1fdc8d24dfad3b9a6bd8cd24bf570297/652967e082855e67-50/s400x600/6b5fb0530cd4f30f94a960f91ec76adeefc4fa89.gif",
            "https://data.whicdn.com/images/334849515/original.gif",
            "https://data.whicdn.com/images/309941028/original.gif"]

        self.bot.momo_gif = ["https://tenor.com/UZ2D.gif",
            "https://tenor.com/boSu5.gif",
            "https://tenor.com/brfIg.gif",
            "https://media.giphy.com/media/LOQdYUQeQ1EXUP9loM/giphy.gif",
            "https://media.giphy.com/media/emLsFpAymOfaDgQ7qm/giphy.gif",
            "https://data.whicdn.com/images/330195328/original.gif",
            "https://64.media.tumblr.com/a78b3ab8ea0ffe453aa21deb2ab9bc75/115b9e9c68a3403c-af/s540x810/51d1bbda3025fb12ee24964096d0c991e28e9798.gif",
            "https://64.media.tumblr.com/40e125cfae3dcf6a8d7136699e4552a7/39a930ce41f63aa8-96/s640x960/c6298dcd831c2cebdd15c93d4211487a1177e029.gif",
            "https://64.media.tumblr.com/837f5f926fcdffd35bbb43b2f987a240/tumblr_og4o3xMRK81vd4o0go1_250.gif",
            "https://64.media.tumblr.com/524afb4c165ae33e10b70037f7629609/ce64a54314fb6f7a-2c/s540x810/1f49cc92cc5581399f9fe426ee4e0d3b5c62a95c.gif",
            "https://64.media.tumblr.com/e15673d47fc5ccae331ecadda54d3685/94de53eb038d36c6-8d/s540x810/64a1bd4704e679a5c814a222f5e0122d309c92d3.gif",
            "https://64.media.tumblr.com/0e64a144fb3828f9015a4d2c3ef579f3/tumblr_pqdpx3af9e1w03e6io1_540.gif",
            "https://64.media.tumblr.com/2195477e3e9ee2e062dc69dcc7c37dc5/b14eee683886fdc2-47/s540x810/89df0e56863cd2d2d4b324f3885a987fb2b6acb0.gif",
            "https://64.media.tumblr.com/bd3e9ed79ab4ded1220fdf6f51732f1a/tumblr_pkl2w4n58F1uh7ri8o1_540.gif",
            "https://64.media.tumblr.com/cb50dccf1d9d12face1d5bf20cfbc988/tumblr_pphfldj57w1qefpsho1_540.gif",
            "https://64.media.tumblr.com/7c13d4e833f0cb5f4805f88486ffe87f/tumblr_pr5h99s3pS1y68jmfo1_500.gif",
            "https://64.media.tumblr.com/bc96fa18cbd9a2ee716aaaacfe61a188/f355cda1a5329d5d-11/s540x810/7e7c7651692d8323298f71f0f97debb9099a720c.gif",
            "https://64.media.tumblr.com/9474bce6ddecff3ed45aa75d6963c8be/f1f4671493ff8549-2b/s400x600/eac8b35e2a9ad21acc03f714259199660b8a591d.gif",
            "https://64.media.tumblr.com/265ee345457f443ec9165ca31bbedb02/e0130da8845e3279-20/s400x600/e9cd5dd73e7eaa1b206eaa23bed938667a1955a1.gif",
            "https://64.media.tumblr.com/be7b08d577ec319d3646476f11a5a1e8/8c6f771089b013e1-90/s400x600/de1dadd002536f61a60cfe1dda2a52a724904dd9.gif",
            "https://64.media.tumblr.com/e7a3d96c68b0f958938fec98803fdbf2/29da03946373c987-e2/s540x810/6a55dfdb5bdbc5d99aa4d3573b0a7b332151d4d4.gif",
            "https://64.media.tumblr.com/0ea370d678a6704d33408fd8f668458a/344d874eae2c4409-18/s540x810/705c55ba118516147ec03c5a30f7c28e07616250.gif",
            "https://64.media.tumblr.com/844859a2b4515dcb20e949b568abe53f/9d1a61abc118f131-ae/s540x810/449d3310100ffba05d4c06ee2c1499d3ac00c9ed.gif",
            "https://64.media.tumblr.com/6422c313121ecf99f5fc536b5693ecd1/e98424289a1f242f-13/s400x600/dbf5c0993f58ccba54f81bdea6c18f7667ae2ffb.gif",
            "https://64.media.tumblr.com/a6257d0b51b25c5969631f6189da9a52/7d7adea7ddee406f-95/s400x600/60c693cdab91ce8b794fcdccf3384a31ca51c7d4.gif",
            "https://64.media.tumblr.com/cddf7e286806b84b656983b8152d2ace/0af759193e6153cf-b0/s400x600/fd2af02ad150dbeeb130bde5c1a39b16dc9fea6b.gif",
            "https://64.media.tumblr.com/5ea447b0d6952476ca85a4fea8ac3d70/0af759193e6153cf-c0/s400x600/512db50fe9c341d269c98e0be2adc459df21900e.gif",
            "https://64.media.tumblr.com/89d72e2f6aff1fb1a886fae196666018/0af759193e6153cf-d1/s400x600/f8bf602c7f2dd35c1e5ea1a4e0726bd70c44473a.gif",
            "https://64.media.tumblr.com/e8a6ad19e6cb61e6c207354e05683b1f/0af759193e6153cf-45/s400x600/d08c8baa63b2ed6cf54e5afd8e074f75878bbf50.gif",
            "https://64.media.tumblr.com/7e696bfc5e098ff3a9bf206ba5dcc952/f9dc4eced26b513d-85/s400x600/f18a5185338c8d403ae1fd0160416a378f90f8ab.gif",
            "https://i.pinimg.com/originals/c4/df/9b/c4df9b373aba6e66418dc7ed370b0c58.gif",
            "https://i.pinimg.com/originals/5c/f0/25/5cf025e803da560a95c0425397c8f670.gif",
            "https://media.tenor.com/images/0a86b8dedba13e4c109b18cac100fed3/tenor.gif",
            "https://thumbs.gfycat.com/DisloyalHatefulHuemul-size_restricted.gif",
            "https://data.whicdn.com/images/330195349/original.gif",
            "https://64.media.tumblr.com/b34483c49c78839175b3ca4550a64f8c/dc5fcd3bd7e1bf7c-fb/s400x600/6953b4b1ec96e3fa08571e9a7bc2555359a7e073.gif",
            "https://data.whicdn.com/images/338966832/original.gif",
            "https://64.media.tumblr.com/074e20853438613a23ba426a72138453/6f64d542fff2abf5-4f/s500x750/1ed691374468c78e6f8c21c5ddbb9393cd4fb8f8.gif",
            "https://thumbs.gfycat.com/FarawayCreativeAmbushbug-max-1mb.gif",
            "https://media.tenor.com/images/daf76ea527a7668dd0aa4760b8781ff0/tenor.gif",
            "https://media1.tenor.com/images/028faf70eedd9d27a2d700c5d029d24a/tenor.gif?itemid=14321501",
            "https://thumbs.gfycat.com/AngryFrighteningFlyingfish-size_restricted.gif",
            "http://pa1.narvii.com/6635/91f403c10da5f9b5721f136a33f82f45f85272b1_00.gif",
            "https://64.media.tumblr.com/c30cceb62842893e2ba9228de4ccaf75/tumblr_pz1tnw1Tae1ut8ku9o3_540.gif"]

        self.bot.jeongyeon_gif = ["https://tenor.com/bgvYS.gif",
            "https://tenor.com/bm9Bh.gif",
            "https://media.giphy.com/media/QxYGmXN0vs2W6oHAO2/giphy.gif",
            "https://media.giphy.com/media/Pm3E3SsR3TSeT0eI6p/giphy.gif",
            "https://media.giphy.com/media/jOyCT02EvfnMc7trkh/giphy.gif",
            "https://64.media.tumblr.com/9262abb6fc397402f40eb9380dd4fd12/tumblr_pq8l6wlhBq1qmrscao2_400.gif",
            "https://64.media.tumblr.com/02142604dc8f9151428452ce5a5a9f3a/676b8a0e852214ce-72/s400x600/0e61d6ac2294886876ec733aeff3a4f8ed0ce21a.gif",
            "https://64.media.tumblr.com/9aa0fdde98125212eeb7124fd04099dc/tumblr_pya3w1MiMU1wjbytmo10_540.gif",
            "https://64.media.tumblr.com/179d2ddb1aeb4da542b80e9905335947/42b1f6ccb6fd028f-87/s540x810/9767089b2438a39635e6a3d53e034e742e2b363d.gif",
            "https://64.media.tumblr.com/609ff2ed3782c1d6809cf07f9c788380/42b1f6ccb6fd028f-d4/s540x810/61756a51b6bf79f71d3fd6c762b0211893ffe1a2.gif",
            "https://64.media.tumblr.com/b2ad790f819c55149ed35454a609f529/e8751f49bf91c003-92/s540x810/301cdd989ed723d995fb02d2f6ba557177dbfa18.gif",
            "https://64.media.tumblr.com/65dde615460da540591e07b5120e0942/tumblr_pqdev9tPpy1s2vcg0o3_250.gif",
            "https://64.media.tumblr.com/52990888263be9dbc9f0576ad8a5b43d/tumblr_pqoicwZQmH1ueg2m0o3_540.gif",
            "https://64.media.tumblr.com/3e1bd918dd8e4d44c607e722391dcc76/d0e49fe9dc258d99-bd/s250x400/9f428672e7517762643c5099f2ea59dbe3631669.gif",
            "https://64.media.tumblr.com/b8574badce63fb259035d42941aad8e6/74c0ce66680e3626-9b/s250x400/fca54df057a4f6e6f7e489ed5bc623c9781b7e88.gif",
            "https://64.media.tumblr.com/ba11e6344d514f54449627fcf7391eb8/74c0ce66680e3626-8a/s250x400/f122b8fc473feab804e3243126ff7e3df49a2565.gif",
            "https://64.media.tumblr.com/7ca03986be36f9015ec28d6a8d4d218a/tumblr_psy2c2HgxL1sk2kqwo3_540.gif",
            "https://64.media.tumblr.com/b831d47a7c1f52268d6c5c046aa63aac/5eb1cd496a5cee38-9b/s540x810/9ad4e39e8be5a26472880d824b00f4ae28958e30.gif",
            "https://64.media.tumblr.com/0c6c3440dd33a99cddd32f734188ac37/913dd4a15be0e198-da/s400x600/46cdbfd88b27d9486ee549d7d6b226aed809e5e2.gif",
            "https://64.media.tumblr.com/15b737537b4412638ac44e5de931fb48/tumblr_pylg6zFKho1s2vcg0o1_400.gif",
            "https://64.media.tumblr.com/e69566f445cd0fcdedfda282ff4465a5/tumblr_pylg6zFKho1s2vcg0o4_r1_400.gif",
            "https://64.media.tumblr.com/0606f3919b5f90bb054707e9cb049faf/tumblr_pylg6zFKho1s2vcg0o3_400.gif",
            "https://64.media.tumblr.com/016aa7abeb8d10c5bfc1ae27ad297b81/tumblr_pylg6zFKho1s2vcg0o2_400.gif",
            "https://64.media.tumblr.com/f343378fa5a2afe4b1e50d967ea681f3/5ea2dbbcb07a2e21-01/s250x400/33b2ca9c6410cb34e793e6f4bee75dfa3b032158.gif",
            "https://64.media.tumblr.com/07843a377273f535788aea18aec4de39/5ea2dbbcb07a2e21-06/s250x400/ff68d5e4cc3730cd09512dd4e0dd051470012fd0.gif",
            "https://64.media.tumblr.com/ee039ae8c66740c210d35b4299e38c48/55c36f80f2c2d523-5b/s250x400/d3363d2be088af25be709533fedc55e3999a8d61.gif",
            "https://64.media.tumblr.com/74617ec87ad65c35dcb8b2e814387242/55c36f80f2c2d523-5d/s250x400/6bda9ec1faaf55bf45a8e6d982e3088aca755d50.gif",
            "https://64.media.tumblr.com/6c226fc6453a833ff4e26ffb3ca4ce02/55c36f80f2c2d523-e3/s250x400/ba25a8c01d71212ff8c6c378b0c9f456b0f32f45.gif",
            "https://64.media.tumblr.com/c8261f7d7b5fa6ca6582a5fdec1cd668/55c36f80f2c2d523-de/s250x400/70e251b5eda0a711acdf8456667d058eea279fba.gif",
            "https://64.media.tumblr.com/7bf422924ffdf42fe3446ee30a0eaba8/55c36f80f2c2d523-2f/s250x400/15ab06feb502b91cce6d5c9bd37294e465bf71df.gif",
            "https://64.media.tumblr.com/dc29a916409a5cfed722d28df0e23dd3/b67e7bde41ea540d-23/s250x400/24edbcf82686f8dec945870552858fce9c99b481.gif",
            "https://64.media.tumblr.com/653cb569efeeaf12bc045a5e956db66f/189e98bf76ed2f8d-eb/s250x400/1fc6eecf3f6599c78a589d35f46c51bd0696bc52.gif",
            "https://64.media.tumblr.com/60ece86acd84cf99c3d7020b0755f342/189e98bf76ed2f8d-cd/s250x400/2e00ab97f463ee0db3bfb0bf63c3af050196e4ff.gif",
            "https://64.media.tumblr.com/abde93db4fcbec573e5d3cd478052bd3/189e98bf76ed2f8d-9c/s250x400/c29d7f98f6702ed87724a1be0e62a60acb42b5a1.gif",
            "https://64.media.tumblr.com/ab06457360b58beada3a6366f4f75f6a/e132cc4c08bb4be1-96/s400x600/749274e87a1d22e722c451e8e1309c85c480e004.gif",
            "https://64.media.tumblr.com/257c179289a6e538f335fc14e3a8794e/e132cc4c08bb4be1-39/s400x600/1958b235a177d6dab46520a44b7b5ab6ed4eec1b.gif",
            "https://64.media.tumblr.com/30a9c5fdf7bb9c6d1baa1bc834ec2d37/7565473f5bc8701e-6e/s400x600/37e4cef60d507936858d58c089427a6109746bd5.gif",
            "https://64.media.tumblr.com/707f06fbd2b61f66c9a5c16a6ed5b340/7565473f5bc8701e-fc/s400x600/b099d9cb910ecb53e4d64ee2d18846f4db0b9d41.gif",
            "https://64.media.tumblr.com/0cb661c5330b9deebfb81f49e1623547/0c4c375bdd14e477-1f/s400x600/5f273323b5e155ae5253bded3ab7754cf14ffa35.gif",
            "https://64.media.tumblr.com/048c0f5183cd04019e92280ba68b7310/1e765d0758b6d3ce-69/s400x600/f627dfbef6ea20bfd06fc878ac0ea398b7e51e38.gif",
            "https://64.media.tumblr.com/a73c0b909258203c1eeb6060849c7f2a/1e765d0758b6d3ce-8f/s400x600/22905ca766831c52f0b186858025dfd3a9a36c48.gif",
            "https://64.media.tumblr.com/f348ec7bdf0c0f08be22c3d4fad210f5/3358a74438fbca58-02/s250x400/ae438632d543c7c17721d8f9b81fc724a1a1b813.gif",
            "https://64.media.tumblr.com/b8409fb28396a896c6d2193abee6e2ff/d59c4d22341cf303-88/s400x600/7f70bdee3df774dd6b8358faf293fe1183c3f6c6.gif",
            "https://64.media.tumblr.com/db1ab8ef84a3070b5f2d04945be69816/d59c4d22341cf303-a3/s400x600/9a112592f62773b40614fc0e23d703e2d713a73b.gif",
            "https://64.media.tumblr.com/f035d55956bdd80d3f8e0d319566d19f/d59c4d22341cf303-4f/s400x600/6b8cd5e23bf1ed9a455fa28e4e03a5f86fd1e8ee.gif",
            "https://64.media.tumblr.com/aca33a2cef4d132a5b389f207231a867/d59c4d22341cf303-9d/s400x600/67615fcd8c9b788231ea0b33613972b03196e447.gif",
            "https://64.media.tumblr.com/a0f8354ade87b481a684bc5171511283/161fb26de1cdfd71-4b/s250x400/773ae4d90b66dba4fd1dc0c53e61b7da1cf0f71a.gif",
            "https://64.media.tumblr.com/c42735f34b91084c000ac885d3e0a67d/tumblr_pvyyl7Wir91qi59tso4_250.gif",
            "https://64.media.tumblr.com/1b5d7f91e4014d81b3753d2e935c9572/tumblr_pr3bly19aO1sy8x5ho1_400.gif",
            "https://64.media.tumblr.com/85444030652663480287b8741fba57bc/tumblr_pr3bly19aO1sy8x5ho3_400.gif",
            "https://64.media.tumblr.com/157f7a8cb8a5343fdb9d7d32282c08e2/tumblr_pxkk5iqmis1wi7204o1_r1_540.gif",
            "https://64.media.tumblr.com/50ddbd3f1ade30484dad05dcca954b84/721f7a5dbd2edd8b-f2/s400x600/3748e1a957926c9dfb660a96ddae7dcc29636011.gif",
            "https://64.media.tumblr.com/383a75dd83467acad138366cae224a31/721f7a5dbd2edd8b-d1/s400x600/1a1d191461314f364391376dd3d94f96bcffd907.gif",
            "https://64.media.tumblr.com/1f72a510680f9bf6be87ad9216156ea6/8c91fcbd6f4c48fd-23/s400x600/eb2f540b5731fb6ffaa4f8f3b86573d41625a7bb.gif",
            "https://64.media.tumblr.com/57a46fb4517b19269a23dd5f8ae86a7e/8c91fcbd6f4c48fd-40/s400x600/50ebd20754deaec93c0bde4a1497113dc9bd752c.gif",
            "https://64.media.tumblr.com/0e660cb47f6673e0825ef80874b814e8/7c640728168c887f-3c/s540x810/4b2a4e3381c8d57c445f7304c1bc43bf093381e4.gif",
            "https://64.media.tumblr.com/190be39a03e3a804f6bc70b1a1639b4f/tumblr_pyfcmhlGCm1s2vcg0o3_400.gif",
            "https://64.media.tumblr.com/0d251ffa6fc70271d2be30334fe066cd/tumblr_pyfcmhlGCm1s2vcg0o2_400.gif",
            "https://64.media.tumblr.com/8945c3b106ad1d2c2985e9738ee41b8d/tumblr_pyfcmhlGCm1s2vcg0o4_400.gif",
            "https://64.media.tumblr.com/e77c525e8a5147ab606dcf1b52634503/bbc3d248090a91e8-42/s400x600/e0dd88b5d05cb970149ec8dea856866907bd3da8.gif",
            "https://64.media.tumblr.com/50c02719b98e4bd8ebf2d85805bade81/46d39a0f89707b9d-15/s400x600/d79d9c898b0d8cf826bd5fa899570d6e1f75c71a.gif",
            "https://64.media.tumblr.com/6f0763f77bf4ae803b174104662f8ee6/46d39a0f89707b9d-c0/s400x600/7cae05446b87ab86061b839fa8b181b8277109f5.gif",
            "https://64.media.tumblr.com/976dd4f5678e6056268f417a0d737965/46d39a0f89707b9d-a5/s400x600/80d8b8c0ec7329d3d589edecc68969183603176e.gif",
            "https://64.media.tumblr.com/bc8e9d8c6f2b00d2b08b14bcd44e21d3/46d39a0f89707b9d-43/s400x600/7892f4da50c36727bbae7d67fec412dc9a7c1004.gif",
            "https://64.media.tumblr.com/535c78c47b06931cab452eb3e6f97414/94d0f0984b192a84-e2/s540x810/4a2d2774e88c3a7f93abe4bf1d9b6192d96f6e38.gif",
            "https://64.media.tumblr.com/fb1f711e43a1cb876bdb95fdf00b4a13/29526036330ec695-2d/s250x400/0d6c0c5c88ff01a8127f46f5b0d6742e4e0ab0b4.gif",
            "https://64.media.tumblr.com/2c72aacdd92aa7580a17479302aa95e2/29526036330ec695-a3/s250x400/4f8406d053d7f4240aa2c4ecdbcc8815ce33de8f.gif",
            "https://64.media.tumblr.com/94c7c515cf8c13613bc08f21b0c210c8/tumblr_pqg05ir9rs1uh7ri8o3_540.gif",
            "https://64.media.tumblr.com/3d6d23d1f9a43e66c6683683272025d8/tumblr_prknfvxHS51s2vcg0o4_400.gif",
            "https://64.media.tumblr.com/6ffa77fe64bcb53f6ef3071e2452cd1e/6032da0587ea636e-04/s400x600/55154da6306cab2a421356297c3ea1b404da9cfd.gif",
            "https://64.media.tumblr.com/cdfe9213219b760ea1552090cac54a7d/tumblr_pp8wm9sq9P1uh7ri8o2_400.gif",
            "https://64.media.tumblr.com/89aa8c1e3e15626902f0284646ad9c94/tumblr_pgyeta4IuE1srtw16o1_400.gif"]
        
        self.bot.tzuyu_gif = ["https://media.giphy.com/media/sKdL5e5zah0gE/giphy.gif",
            "https://media.giphy.com/media/jmphxHznc7wBmsuaW1/giphy.gif",
            "https://tenor.com/5MSV.gif",
            "https://tenor.com/Fguv.gif",
            "https://tenor.com/bsSaJ.gif",
            "https://64.media.tumblr.com/7ed96f62f8204763f65e3a5a7e55d47a/261d1415ea1f0f6b-f4/s400x600/fbed6f163db8392d5f8c828b8a4b455a0a67fb9d.gif",
            "https://64.media.tumblr.com/9a1a380b832e998d47883efa55f61d56/tumblr_pya30eEG3U1sk2kqwo4_400.gif",
            "https://64.media.tumblr.com/d7b036cc9557473df34906c16e246980/tumblr_py9sxd6iIZ1ut8ku9o8_250.gif",
            "https://64.media.tumblr.com/9b137c3a70890e5e71767d58db99d0a8/6a369b9906230ab5-f2/s400x600/6c7823157aab08cae234fd6a6c765b2e656239d3.gif",
            "https://64.media.tumblr.com/cce3b92ee5b6e482a94e43b870b67ded/6a369b9906230ab5-69/s400x600/951fe370f9968a4d7b233a0deaffe7eb8a7032da.gif",
            "https://64.media.tumblr.com/0c673865fd02467743d2600dd344462d/6a369b9906230ab5-81/s400x600/8cc16ced9ab11e950ec08cff3d1337a5a2e2e222.gif",
            "https://64.media.tumblr.com/dcc300c8b51dd03513b9d045a6562b47/6a369b9906230ab5-d5/s400x600/29cf595ac7dcc768e19202555f8825d04b925c4e.gif",
            "https://64.media.tumblr.com/04867cfa49ddf44bbc201180c3be0650/6a369b9906230ab5-cd/s400x600/d6adbf0b8e471e351f2304b5b6e10190580a43c3.gif",
            "https://64.media.tumblr.com/13eb7123a08da63e315c879f72952e8e/e2842f8e7eb04bb3-e0/s400x600/893fe44efbf2c5749a7245cf4bfdf9e242806eb8.gif",
            "https://64.media.tumblr.com/6176902f0bcd098cfc2c5f04b3fae6e8/e2842f8e7eb04bb3-95/s400x600/b60f4b963be4b614a4b6d74a940702007d64596a.gif",
            "https://64.media.tumblr.com/8c6c27607b6f0155f03d73ccde8f706a/tumblr_pyiugyw8pQ1ut8ku9o2_400.gif",
            "https://64.media.tumblr.com/915f7dc8678e2af8713dead928350b6e/d0e49fe9dc258d99-ae/s250x400/1863e5978e937e67104a7e899585b2d8bf35cfe8.gif",
            "https://64.media.tumblr.com/c34b76324007cc16ff1e3ebfecb9cdf7/tumblr_pyglzzAnyy1r3hdhfo5_400.gif",
            "https://64.media.tumblr.com/e80dc917872cc351a3135a70a6c8e439/tumblr_pyyyk8S6Az1wi7204o5_400.gif",
            "https://64.media.tumblr.com/ad9061f3a053fda39e6adf61e8131e9a/4614759c294852aa-8e/s540x810/d8f861ec7c187a4998cfbd74647a846f32dbf220.gif",
            "https://64.media.tumblr.com/dce0e994bf069012b0bc782648c5f603/4614759c294852aa-e1/s540x810/e14da7ec77c51dff3d9a0f1be251994e3f47c061.gif",
            "https://64.media.tumblr.com/82b28ce48293af199e3967f1e4bd49eb/4614759c294852aa-35/s540x810/e70e4196d88c48af72bed30c2cfe5328f20fe02e.gif",
            "https://64.media.tumblr.com/fc51c47ff4eac16ba62310dcd9de03f8/a628ba3712f673ef-fa/s540x810/bff4dfc1df928a3395e880508dedab1eb22b1cc1.gif",
            "https://64.media.tumblr.com/b106627ad4410a7a487c861e7b42c2a0/a628ba3712f673ef-cb/s540x810/1d989bc8957912da653dc8d175f0a5b561a6af34.gif",
            "https://64.media.tumblr.com/efc9bd8bcadaf5295de879d5563b0648/a628ba3712f673ef-d0/s540x810/b449b13d56b262507571ad37716d64046186f061.gif",
            "https://64.media.tumblr.com/0f3cb2e29ab0daf9553f17b6d59b0254/d8e9bc75612ffd76-b6/s400x600/265b9181a1171d21d8867a42f619b288c2b54f46.gif",
            "https://64.media.tumblr.com/310070256ccade4877f5c4960b16b802/ae0327d52bf1e1ee-f2/s400x600/61f9ef6e6e8e0a5c7b3cb4fab6df0ad9ddde7ec7.gif",
            "https://64.media.tumblr.com/9ebd0bb59bfbc3d54cce4b5c0e220382/tumblr_pyf5whEJjO1vg2vnoo1_400.gif",
            "https://64.media.tumblr.com/0e288f24ec3a973bd73c585e5a5157df/tumblr_pzosowzZpL1x71qabo1_400.gif",
            "https://64.media.tumblr.com/76d5a66a01be3ac2862ce0e60c679376/b67e7bde41ea540d-5e/s250x400/fd7ea2c72ce82dfa311d1e3ba71d5da69da17d8c.gif",
            "https://64.media.tumblr.com/86c1e0204415b7c2f908e3778943b25e/5434c718491c1c78-df/s250x400/f0811701b9a0603220688c7233ef722b308368ac.gif",
            "https://64.media.tumblr.com/68a7e328cb9c45450d57f1eb1847d42c/5434c718491c1c78-bb/s250x400/e542f8fc147ee1068dc46f63b6fd1c9ef81cf5da.gif",
            "https://64.media.tumblr.com/a0a96c464c74aeace9961130ab6184ce/5434c718491c1c78-e1/s250x400/08c77291be41fd35035d618d801c9009e22c2e98.gif",
            "https://64.media.tumblr.com/f7cca1191c5f98ecc6543290052f6878/5434c718491c1c78-65/s250x400/1a8b4b8e88716fec59d4dfa60812c7bd6c1b5362.gif",
            "https://64.media.tumblr.com/23ecdae91368b8147f4c80b2a0ba96da/1d5cb96a31ae8e99-51/s400x600/b3b48f53f1ea7086eaf18b463179bc389ac07a57.gif",
            "https://64.media.tumblr.com/9a121f58bba626c68e49311193f05fbe/tumblr_pvkrt2p8y41s2vcg0o4_400.gif",
            "https://64.media.tumblr.com/a76c4e5142085b0c8c5dd8bec4f5bd10/15f3c9b2c9b57a0e-e0/s540x810/d0ad9abc8615358bd4eb29b79d4997a59dee9530.gif",
            "https://64.media.tumblr.com/d2acd865e90d711d318b88944442d63c/tumblr_pyqke1OmGQ1wi7204o1_400.gif",
            "https://64.media.tumblr.com/7bc2dabc13d74b69759f57884a1b7ca9/tumblr_pyqke1OmGQ1wi7204o2_400.gif",
            "https://64.media.tumblr.com/f0be6ccb7e09732fe56c6f03b0f09744/b9437f0fb7fc49a7-eb/s540x810/ac0411e6a04b7f7cac0c32b807b429d1cd1a02c4.gif",
            "https://64.media.tumblr.com/f0f3ca8a9146544f0e806b7ce348de89/a2a9a8886ed930c0-e5/s250x400/0aa40cb9d7c19d3958f034aa72bae6b56bc4edeb.gif",
            'https://64.media.tumblr.com/0adf51ee9475b9fea752686ec5f5786a/97089c3768bb424a-35/s400x600/27a88061859f6a9bf479ef9fbbf7512157517af3.gif',
            "https://64.media.tumblr.com/7debeac7e902dcad149744e81a6362d0/208f12635043a2e4-5b/s250x400/2358b4be35740c00a84747b6d349a80056659c41.gif",
            "https://64.media.tumblr.com/a52c62eae6ccaa3a2555ee8a0a5c554c/208f12635043a2e4-5a/s250x400/5f449136920a6dd70eb17c49ae7a7ca9e2c28ac2.gif",
            "https://64.media.tumblr.com/48e57c8493ac9db9407aa063b8365e0a/219ffcd33345398c-af/s400x600/5f534323f76157d2e1555575b7ef718d18cd0776.gif",
            "https://64.media.tumblr.com/5cbc17650b73ca0d1c7941c317c97ca8/219ffcd33345398c-d9/s400x600/b2db200898390e265400e0598025debd4ba1ebbf.gif",
            "https://64.media.tumblr.com/1adb60e524126a167b8e2c24d2c477f5/b09b0a6376c9e28b-aa/s250x400/4afc3880005e095db90f54d95ff129cf00c0eb17.gif",
            "https://64.media.tumblr.com/581d4504f6d19db8c70d4af50be5ae41/b09b0a6376c9e28b-98/s250x400/f53d68266268add39c44bdaf56e51ad2facb7edb.gif",
            "https://64.media.tumblr.com/efa3194aed41afba5c12a51477ff4d02/tumblr_pyfwnuIqnC1wi7204o6_r1_400.gif",
            "https://64.media.tumblr.com/fca6e2db519441404ab007bae3722a86/e6d8de4c8e08ff1a-7a/s400x600/0cc5bd8d9e4174e54cc219f6a60816d4a103fdc1.gif",
            "https://64.media.tumblr.com/7fdb74f4c90e8213c63370a44573fb2e/tumblr_pwn6s8mxPP1wi7204o3_r1_400.gif",
            "https://64.media.tumblr.com/bf1dada3c4bc31ba5ee1dbb7fb9a579e/fc7a8f19462fd8cd-79/s400x600/63b56fb726ae74542a5ea98875d42ca348bc0670.gif",
            "https://64.media.tumblr.com/53805212749d1d49cb1f71aa738dfaa6/676a9474cc2271cb-9c/s250x400/17340e54a42fb81ed3d9b62476197e3114350867.gif",
            "https://64.media.tumblr.com/aef3e7cc2382840ebdf9fc7b672139ae/tumblr_pxl0ftKnmX1qmrscao1_400.gif",
            "https://64.media.tumblr.com/470a58ff1d348afe0990bb5aa7eb1477/c81e1dbe0a67852a-73/s250x400/7bffabaabeb1bef826b860838426c0ef587a5bc4.gif",
            "https://64.media.tumblr.com/b52fbe27661279cb345b78e4333e9986/187c55d237602353-11/s540x810/d1f237604dce40a59f782776bf7b27de9165157f.gif",
            "https://64.media.tumblr.com/10918fa8fb320d1081bcf89da8a4753a/53cea5be946593a5-ef/s400x600/3ca37c3f7f2c973922368c2acf7feb186a337b5f.gif",
            "https://64.media.tumblr.com/13c67ee3a6900aa9d3b74fa054e16fd2/499ca70b35c231ac-2f/s400x600/d1912e5e1cc6aac7ad9a31197af097c20a0502f6.gif",
            "https://64.media.tumblr.com/bacae57a0f68bdcab0d8b1376aa849e4/eee7a86854317b55-95/s540x810/6f9dd5dd07fbbcaf721fade0380341a227c7e20c.gif",
            "https://64.media.tumblr.com/77a7f4519cc8d888befc448121fdbdb4/02d3e1d7d884bc08-86/s400x600/b14cdeb70d63bfaefdd65f51f0c2416616d3cecc.gif",
            "https://64.media.tumblr.com/da006c2db3b9ae2f6b2ad8097c4199ae/195ae00b747c1a1d-1a/s400x600/b947451db20ed92167d6c87bfdd6c196293a68d8.gif",
            "https://64.media.tumblr.com/f515b1304d3da3aa66b681df0a9fa70f/195ae00b747c1a1d-3f/s400x600/8836c3c31432cbc23e18104be26dc7eb3057cc70.gif",
            "https://i.pinimg.com/originals/87/6c/91/876c9177201ea51569d1e4ce057ba09a.gif",
            "https://66.media.tumblr.com/5b67a01d8f9679bb3fa777f6f3d4454e/5f17239926e48cfb-f1/s500x750/1772ee5c9914a39dfed48b6374d9e4d3aced378c.gif",
            "https://i.pinimg.com/originals/df/47/86/df478648a061ae6acbc8e6e528270c91.gif",
            "https://i.pinimg.com/originals/db/b1/af/dbb1af574f241be2d9c12abf99a6b181.gif",
            "https://64.media.tumblr.com/74cc1804075625dbf6c6aec0f334f861/tumblr_p3s6p7G1Xm1wk8cqeo1_400.gif",
            "https://64.media.tumblr.com/5659b83f05a84a1be4ae488245afcd50/tumblr_p6fgkoHBGl1qmrscao5_250.gif",
            "https://data.whicdn.com/images/282798038/original.gif",
            "https://64.media.tumblr.com/76d5a66a01be3ac2862ce0e60c679376/b67e7bde41ea540d-5e/s250x400/fd7ea2c72ce82dfa311d1e3ba71d5da69da17d8c.gif"]

        self.bot.nayeon_gif = ["https://tenor.com/9b5w.gif",
            "https://tenor.com/YChI.gif",
            "https://tenor.com/bs6Qy.gif",
            "https://media.giphy.com/media/gg3XU0ggfN7B0tlHnw/giphy.gif",
            "https://media.giphy.com/media/URvyQpZe0uoCT6jHo8/giphy.gif",
            "https://media.giphy.com/media/h7dxG65XwW00aBVkBc/giphy.gif",
            "https://tenor.com/view/mood-twice-nayeon-i-dont-know-gif-14052273",
            "https://tenor.com/view/pop-hair-twice-mouth-kpop-gif-16633600",
            "https://tenor.com/view/twice-nayeon-kpop-cute-gif-15007259"]

        self.bot.dahyun_gif = ["https://tenor.com/zEfV.gif",
            "https://tenor.com/ZKRA.gif",
            "https://tenor.com/brQ06.gif",
            "https://media.giphy.com/media/gLcbZ01uqIOZIsBWlC/giphy.gif",
            "https://tenor.com/bd1b8.gif"]

        self.bot.jihyo_gif = ["https://media.giphy.com/media/Ph6A5WjBAI3981PAsf/giphy.gif",
            "https://tenor.com/bnZ6r.gif",
            "https://tenor.com/bbKLS.gif",
            "https://tenor.com/brGhA.gif",
            "https://tenor.com/brT8L.gif"]

        self.bot.chaeyoung_gif = ["https://tenor.com/view/chaeyoung-twice-kpop-jyp-jypnation-gif-14436666",
            "https://media.giphy.com/media/xUySTt5f5AmRUBgdUI/giphy.gif",
            "https://media.giphy.com/media/lptOHczNAFD1G79Ofq/giphy.gif",
            "https://media.giphy.com/media/Qy2WthVCTLkeT1gZLS/giphy.gif",
            "https://tenor.com/XiHw.gif",
            "https://tenor.com/bn9Lf.gif"]

    @commands.command()
    async def twice(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Twice {arg} | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "mina":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Mina :heart:')
                    await ctx.send(random.choice(self.bot.mina_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Mina :heart:')
                await ctx.send(random.choice(self.bot.mina_gif))
                await ctx.message.delete()
        elif arg == "sana":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Sana :heart:')
                    await ctx.send(random.choice(self.bot.sana_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Sana :heart:')
                await ctx.send(random.choice(self.bot.sana_gif))
                await ctx.message.delete()
        elif arg == "momo":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Momo :heart:')
                    await ctx.send(random.choice(self.bot.momo_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Momo :heart:')
                await ctx.send(random.choice(self.bot.momo_gif))
                await ctx.message.delete()
        elif arg == "jeongyeon":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Jeongyeon :heart:')
                    await ctx.send(random.choice(self.bot.jeongyeon_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jeongyeon :heart:')
                await ctx.send(random.choice(self.bot.jeongyeon_gif))
                await ctx.message.delete()
        elif arg == "tzuyu":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Tzuyu :heart:')
                    await ctx.send(random.choice(self.bot.tzuyu_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Tzuyu :heart:')
                await ctx.send(random.choice(self.bot.tzuyu_gif))
                await ctx.message.delete()
        elif arg == "nayeon":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Nayeon :heart:')
                    await ctx.send(random.choice(self.bot.nayeon_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Nayeon :heart:')
                await ctx.send(random.choice(self.bot.nayeon_gif))
                await ctx.message.delete()
        elif arg == "dahyun" or arg == "dubu":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Dahyun :heart:')
                    await ctx.send(random.choice(self.bot.dahyun_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Dahyun :heart:')
                await ctx.send(random.choice(self.bot.dahyun_gif))
                await ctx.message.delete()
        elif arg == "jihyo":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Jihyo :heart:')
                    await ctx.send(random.choice(self.bot.jihyo_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jihyo :heart:')
                await ctx.send(random.choice(self.bot.jihyo_gif))
                await ctx.message.delete()
        elif arg == "chaeyoung":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{gareth}>, <@!{ctx.author.id}> is talking about Chaeyoung :heart:')
                    await ctx.send(random.choice(self.bot.chaeyoung_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chaeyoung :heart:')
                await ctx.send(random.choice(self.bot.chaeyoung_gif))
                await ctx.message.delete()


   
def setup(client):
    client.add_cog(gamerPings(client))