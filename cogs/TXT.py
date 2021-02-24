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


class txtPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.txt_soobin_gif = ["https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-soobin-gif-17906793",
            "https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-soobin-gif-17599191",
            "https://tenor.com/view/soobin-txt-choisoobin-tomorrowbytogether-tomorrowxtogether-gif-16277376",
            "https://tenor.com/view/choi-soobin-txt-tomorrow-by-together-tomorrow-x-together-todo-gif-16311084",
            "https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-soobin-gif-16642602",
            "https://tenor.com/view/soobin-txt-tomorrow-x-together-kpop-choi-soobin-gif-19186061",
            "https://tenor.com/view/choi-soobin-txt-tomorrow-by-together-tomorrow-x-together-todo-gif-16311086",
            "https://64.media.tumblr.com/507bccfa336be80ffba3d75815232176/d1054e684c2730d2-2e/s400x600/6792f4d3ad265b315839490315fe7354c2d6c6cd.gif",
            "https://64.media.tumblr.com/34baecc7ba027c2ad567b0e3e1c04212/50d0abd235da0690-bf/s540x810/faad23131b0c223e0d12596a50f8e34957486a04.gif",
            "https://64.media.tumblr.com/929afea96ff0db12b0bc226d1390f588/15ee179e7c2e6f5a-9e/s250x400/f4fbd5b2f4f6e3c91a6694e5d121fb7bd77485c8.gif",
            "https://64.media.tumblr.com/ea4a157012d88b56f8d728b7030ee4e7/6a9a02a7b5e67065-23/s250x400/5fcf8b8aa0ca48b1418e5d39c1e6e48df4eb4fff.gif",
            "https://64.media.tumblr.com/a112f5bbb7597c3d0aabe090c33a7ab3/f259972bf7bc441f-45/s250x400/6f89ad6867c691bb7e1cf34ace7ccdefbd23c6d6.gif",
            "https://64.media.tumblr.com/6e9fcb191d7e73486d24e02f772ec436/1d216d8d0f4d66ea-2e/s400x600/7f727b4ea05c9a25c7efd6c1255fce0c1eddaad5.gif",
            "https://64.media.tumblr.com/cf4d4bf4e7cec2a3978ef1f9c21381f0/2e740671808518a4-b0/s400x600/20078f1cb3785bc00f89682bfb046a9c3ce906f2.gif",
            "https://64.media.tumblr.com/e7915f36fecd62d602234052960b8c30/45cca56035c208bd-cd/s400x600/8da58e10a1cfd53e4771b2a28fb5360d65b646fb.gif",
            "https://64.media.tumblr.com/1127690ffd719d1c4c87fd4ae78fb142/566118b151c6ae4a-4f/s250x400/465e531989b1133292ecb180e17634b5d53035a0.gif",
            "https://64.media.tumblr.com/a4d5dcee47a46c66b4317b0d70242003/6504a210d47a014f-35/s400x600/400bba1e69352ae91f6f63d789e45e762f6425ed.gif",
            "https://64.media.tumblr.com/52373d794e0f784cd575386adcbee323/ea16d8c6291dadc7-bd/s400x600/549fe2d29624fcb62063475bd45b01fcd1f606e9.gif",
            "https://64.media.tumblr.com/6033736a33eb8e2f02be9d0a9a6ed681/61f149f82685eb86-d9/s400x600/65d0602deb633b84f0c3c225c9210d4ac3c02e6d.gif",
            "https://64.media.tumblr.com/e5d0da0a0b73719bf2450aba2304bdfb/88fcaf885095be25-65/s400x600/640b1f38a1d67ff517718a521f30d6f173c995e6.gif",
            "https://64.media.tumblr.com/5db88f1e5792dad7096088093e6673c1/45e24c8b5c499b99-95/s400x600/d50cb9c9d76174ca0fb6cea79461d31c772b8957.gif",
            "https://64.media.tumblr.com/c6f6ef8605daedddc4208acdefd9ff7c/45e24c8b5c499b99-3e/s400x600/47514ca4039b19b94ed85d615b82e7ad5df6f736.gif",
            "https://64.media.tumblr.com/2109955a173f130656ce2f6a58da878a/db94427586de7f3a-86/s250x400/84359c93416b58abfb942149c492672672db5a45.gif",
            "https://64.media.tumblr.com/7d83adf86056a8df2b1a9898eff99383/ffba49c0cd30fc4d-76/s250x400/528b7e24f9e0bdef09b6a953e6ad8601801dba06.gif",
            "https://64.media.tumblr.com/0c3e7733ff1d6542b33a3cd8e51d1820/6b1ebfc23ea993cd-31/s250x400/d3514ef3e5bd5993dd037d9eb001bc15dac39e8e.gif",
            "https://64.media.tumblr.com/42d1e9de722bc692e676d5726849c05f/6b1ebfc23ea993cd-a6/s250x400/46d6b8e92294ee81afb306d433b397bb094bf2c0.gif",
            "https://64.media.tumblr.com/9d5187c63f7bf13f436695e94bdd70bf/e90fbe6c6758cbd2-9e/s400x600/e13b9faa13786ac71a6f1af605bad220759dac2a.gif",
            "https://64.media.tumblr.com/c940a12094ee9165b9ce498cd37dc2f9/e90fbe6c6758cbd2-a5/s400x600/dc6455bcf1cc46b90ec4622e722bc65bdaed80b3.gif",
            "https://64.media.tumblr.com/0cd1949cb22f7423f7bc9ca31b4a24d5/a4cb02ac28a4e573-14/s250x400/79207d746049b18c99a7c5339506f684d12e05c7.gif",
            "https://64.media.tumblr.com/d662715713804f189355e557e2f8bed6/e427ebf770517461-ba/s400x600/10cd5bc12d4fca444cc373e2b3ae58e51e02b7ae.gif",
            "https://64.media.tumblr.com/49a480d5f9a7686d3c3487dafc1ad61a/95c84ac6e98b5800-07/s250x400/a011d8a439f3867bce5dcf4d76b75ebfcbcde6d9.gif",
            "https://64.media.tumblr.com/32a269c1da3f81833cb9778be7b7ebf1/5b68e107f90da0a2-78/s400x600/1df7ea7d91dbb1eb43727f092c59a0822aa5f60a.gif",
            "https://64.media.tumblr.com/ac7e546489bf9320b85d237bb7e1e7a9/4090158e966b8d87-af/s400x600/3c7a19838e978ff2fd82e40ff68c4450f719c71b.gif",
            "https://64.media.tumblr.com/0f64302d896912aa11699552d661fcb8/4090158e966b8d87-1c/s400x600/c1b68c6e18a1c1365bed3f73865c3c355d2f7b47.gif",
            "https://64.media.tumblr.com/c071bf4402538e20ad8a04e9b8c83999/2c4750bc356ac2e2-98/s400x600/8b78eb9d5fb1fac8001a6ec408bf7f7a4d0cc4c5.gif",
            "https://64.media.tumblr.com/3fcc3f5d6d77c02561dccb46bc47ff18/4019a788917ca943-e7/s400x600/f729dac1f8298ff02bb537b3a5e50f05b5b641e1.gif",
            "https://64.media.tumblr.com/99edd63f0b1717db481fa1a92536e5a6/586f3be617856415-45/s400x600/848a4b496261bbd76f1990954f81ae3d4c44f528.gif",
            "https://64.media.tumblr.com/ef98ec095800fc9c2e9c16ccd7823738/ee5554a2727a4f28-9c/s400x600/029146341bfb5bcb1335c0d217f4fb9613f97c99.gif",
            "https://64.media.tumblr.com/9f28df595f67cbc6a5d75d30a89898b9/91e4470d8f2ac9d1-74/s250x400/319ddc2ff8410afc0b4cda5f85a22971f133c30f.gif",
            "https://64.media.tumblr.com/66b72d96713fb0c0852ce2dde5703fe4/6b2ef7d9d62f22da-c9/s400x600/40290e48fcc2e067fbc11c2bdcc7e05808fedac0.gif",
            "https://64.media.tumblr.com/ec923667af58d540adcea3cc4b6124ee/6f5e0fa2421a8291-35/s250x400/6e170a3d75af6f55e1feb99b115210f7e2f885b9.gif",
            "https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-soobin-gif-16784698",
            "https://gfycat.com/amazingpopularanophelesmosquito",
            "https://gfycat.com/likelygeneroushuia",
            "https://gfycat.com/euphoricnauticalgoldfish",
            "https://gfycat.com/wholerelievedharrier",
            "https://gfycat.com/charmingdarkhoiho"]

        self.bot.txt_yeonjun_gif = ["https://tenor.com/view/tomorrow-by-together-big-hit-entertainmen-txt-yeonjun-handsome-gif-17716681",
            "https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-yeonjun-gif-17647828",
            "https://tenor.com/view/yeonjun-txt-tomorrow-by-together-blue-hour-moa-gif-18951417",
            "https://tenor.com/view/yeonjun-txt-tomorrow-x-together-kpop-yeonjun-noona-gif-19211100",
            "https://tenor.com/view/yeonjun-txt-tomorrow-x-together-kpop-yeonjun-noona-gif-19211095",
            "https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-yeonjun-gif-17647836",
            "https://tenor.com/view/choi-yeonjun-txt-tomorrowbytogether-tomorrowxtogether-gif-16277571",
            "https://cdn.discordapp.com/attachments/807006158665285673/807006777908133909/Tumblr_l_211673872934920.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807006778868236368/Tumblr_l_211734956508022.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807006781368565861/Tumblr_l_211753081701713.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807006782345445426/Tumblr_l_211780453128838.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807006782919802880/Tumblr_l_211787843879044.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007035090141184/Tumblr_l_211855654035737.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007035492270120/Tumblr_l_211876113648802.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007035958886420/Tumblr_l_211882417654633.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007036767993917/Tumblr_l_211886198497652.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007037585358868/Tumblr_l_211926113807949.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007038198120508/Tumblr_l_211929646072896.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007038902239232/Tumblr_l_212168482875773.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007039262818365/Tumblr_l_212173662393167.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007668350091334/Tumblr_l_212295783828017.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007669285683200/Tumblr_l_213925366730520.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007669654257684/Tumblr_l_213935720058328.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007670451437618/Tumblr_l_213953962443217.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007671009804308/Tumblr_l_213953365225509.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007671692689458/Tumblr_l_213959735187955.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007672465358888/Tumblr_l_213964612717849.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007673530581055/Tumblr_l_213968417346962.gif",
            "https://cdn.discordapp.com/attachments/807006158665285673/807007674033635348/Tumblr_l_213971776728731.gif",
            "https://tenor.com/view/yeonjun-eating-yeonjun-sanapinkhair-gif-18606067",
            "https://gfycat.com/shoddydetailedkiskadee",
            "https://gfycat.com/bogusvaliddrongo",
            "https://gfycat.com/slipperyleanaustraliancurlew",
            "https://tenor.com/view/txt-yeonjun-eating-bleuiz-gif-19716063",
            "https://tenor.com/view/seulgicfm-yeonjun-eating-gif-19467105"
            "https://tenor.com/view/txt-pissahousu-tomorrow-x-together-yeonjun-yeonjun-txt-gif-20061231",
            "https://tenor.com/view/txt-pissahousu-tomorrow-x-together-yeonjun-yeonjun-txt-gif-20061223"]

        self.bot.txt_beomgyu_gif = ["https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-beomgyu-gif-17683775",
            "https://tenor.com/view/beomgyu-txt-tomorrow-x-together-kpop-choi-beomgyu-gif-19211104",
            "https://tenor.com/view/performance-stage-dance-dance-performance-%EB%B2%94%EA%B7%9C-gif-15902416",
            "https://tenor.com/view/choi-beomgyu-txt-tomorrow-by-together-tomorrow-x-together-todo-gif-16310981",
            "https://tenor.com/view/beomgyu-beomgyu-model-beomgyu-runway-txt-beomgyu-beomgyu-txt-gif-18950063",
            "https://tenor.com/view/choi-beomgyu-txt-tomorrow-by-together-tomorrow-x-together-todo-gif-16310980",
            "https://tenor.com/view/beomgyu-choi-beomgyu-txt-tomorrow-x-together-kpop-gif-19211432",
            "https://64.media.tumblr.com/fc0990a955333d9585668b28e7429df7/50d0abd235da0690-25/s540x810/8ab940d5ae3278fa6c35f5034346a6646c7de985.gif",
            "https://64.media.tumblr.com/ca14a68fa43c81ec6964be55be4fc0c0/006a8455cb49cac7-f3/s400x600/bcc440965254e0199cbe85da04769d6335f0d4fd.gif",
            "https://64.media.tumblr.com/fbecc1310bcc2a234f02a1229121ccd3/33b69961da04d201-27/s540x810/206714e55ab5a87e14b577f4cf758c35362b73ea.gif",
            "https://64.media.tumblr.com/72b9744c2baaa522f3f4c513d7dbdf07/505ddab9b72c3890-fe/s400x600/fafd60c754236ab60bfca9cb02be2dbc1d357ff1.gif",
            "https://64.media.tumblr.com/d02d276b4c3ff6d71cb542516823344b/505ddab9b72c3890-72/s400x600/be23c07a79fddb95a47484a07e8860934c694a19.gif",
            "https://64.media.tumblr.com/5afcc196a3233a9a8d0611c4e2c0297e/88fcaf885095be25-4c/s540x810/70a56e9833305a97cbe9cc2cfd48b680274b3d42.gif",
            "https://64.media.tumblr.com/156e8c6bf2a6a215097083ffea9075b3/79b4dd27c37c449a-b6/s400x600/77d87b6aeb5eee5893696a8194c0389e9cded629.gif",
            "https://64.media.tumblr.com/d7f4b896a8bcc2dfbfba63f15edc7d4c/7597adbdfa359384-c8/s400x600/b4d0dc3d2aa9ecb9145b26172aa2a4a4aef36a15.gif",
            "https://64.media.tumblr.com/94afa093be8d703ba7a67c3181655b6a/7597adbdfa359384-25/s400x600/e61b4f71f020e6661fadc7d45cc83aec0103d5f2.gif",
            "https://64.media.tumblr.com/967fa3d818531fd003011d14f0a1e7bc/0ba3842e18023e38-6e/s540x810/7b899a62e13fcdb0db1b706550ddee69f5544e1f.gif",
            "https://64.media.tumblr.com/2b176cefd35037757f765005a0bc8516/764627cc1bdae6ab-c8/s540x810/014bab6b00844c5007758f579e2e94aced9086f4.gif",
            "https://64.media.tumblr.com/01b83e4ce482cad69b3188cffedfe4fd/764627cc1bdae6ab-92/s540x810/4889a761e8613856ca7888366ea4aa5d08d57c9d.gif",
            "https://64.media.tumblr.com/7d0ea4ffe958ead2ddc107174f35681e/764627cc1bdae6ab-31/s540x810/7bfb2f9c69db69802554c634dbb5f4cdb10859c7.gif",
            "https://64.media.tumblr.com/8f54adf9c3c0b68852de33c9a319b307/6fe51525e67da24e-1e/s400x600/bffa87459721cb8b7bc401425d39981c5a9e0563.gif",
            "https://64.media.tumblr.com/66bc26328c9a18f1ab0685b8cbb9b976/6fe51525e67da24e-0d/s400x600/05db0a387c4c7ff8fc8a29208218628ad6fab23a.gif",
            "https://64.media.tumblr.com/0fbba2de87e3267ac3351f52799a1736/c091cdf2484de6dc-a8/s400x600/ced774b156a15920a1ab4ac2c494b30f622727a3.gif",
            "https://64.media.tumblr.com/e8367b35fdc9d43be86bbd8ed161c81b/48b49720094c29a8-1d/s400x600/1bf630e50fe25fadc881d108351cc2b496f15cfa.gif",
            "https://64.media.tumblr.com/0591651e3a0d86e1ea03996aeb89074a/7eb96c6031c4d5f2-15/s400x600/c046df59a97e4b9c541133d17cc40781caaddc05.gif",
            "https://64.media.tumblr.com/0284c3493ab2e47a0227b928a31bea23/d1304f7d2e180fe8-4d/s400x600/a7f51c04c220d51dbb2a7ce50da8d7d106fbac46.gif",
            "https://64.media.tumblr.com/9d6a89557230bd857132e89166a99f5f/486b67f57768da26-c6/s400x600/e82b85ce85da9f579e1e48e3857b4c13758cda0b.gif",
            "https://64.media.tumblr.com/dc8b5b75cbd62b41c57b1131d44a925c/0137d4afb0358b80-ff/s400x600/e2c17ca55fac00b1fc2ade5a29154e77c44a46c6.gif",
            "https://64.media.tumblr.com/23dc1d94fece36e53aa9042bf495112a/6b2ef7d9d62f22da-16/s400x600/4c16d29606a7b13b55756c733dea3bb5160ffbae.gif",
            "https://64.media.tumblr.com/700a344f255a6a1c7e44742543d0e852/58283d468c69ac9f-cf/s400x600/d44a7c30fd580e130553470becc05e7b81de68f3.gif",
            "https://64.media.tumblr.com/b92885fe7e91dd53ea279bdb94dd294f/c4342612dd38b354-57/s400x600/0742f56e900a02cd98fa0fe062c8216cd1982e95.gif",
            "https://64.media.tumblr.com/42b8cf0da0934ef925a9f21f6e6953c0/8f4b614ba02521fd-93/s400x600/c69747fa8526ef0c37b7e33811294ba948096031.gif",
            "https://64.media.tumblr.com/9dcd6b856f1171382141b2d240c6d9e1/1a2c7a40a1884605-94/s250x400/45d74bfb04f3beb87c3ce22495a2c5a110fd288a.gif",
            "https://64.media.tumblr.com/b92885fe7e91dd53ea279bdb94dd294f/c4342612dd38b354-57/s400x600/0742f56e900a02cd98fa0fe062c8216cd1982e95.gif",
            "https://64.media.tumblr.com/42b8cf0da0934ef925a9f21f6e6953c0/8f4b614ba02521fd-93/s400x600/c69747fa8526ef0c37b7e33811294ba948096031.gif",
            "https://64.media.tumblr.com/9dcd6b856f1171382141b2d240c6d9e1/1a2c7a40a1884605-94/s250x400/45d74bfb04f3beb87c3ce22495a2c5a110fd288a.gif",
            "https://64.media.tumblr.com/ee8e28fbe248191f32f8993c4878d7ae/33b46d68fd51e50e-45/s400x600/5bca06522490bddf3f23af5d952e95abb37f7182.gif",
            "https://64.media.tumblr.com/55855e5df28d1ed61359f4a75e0f48d7/e062177d311f93ca-3a/s250x400/c9e681c756b06ee7917b47965fb058e89276ef38.gif",
            "https://64.media.tumblr.com/41ba2035c992f131a0e655d186a6ed4e/e062177d311f93ca-9a/s250x400/14cdef420df2f52ed703a50f50b382f050a03476.gif",
            "https://64.media.tumblr.com/08198cbc57e53d76176d6100eec44096/a7a7610158ee18c0-ce/s400x600/5a80587acc7a41a66c95d24fc2d93db221437744.gif",
            "https://64.media.tumblr.com/911ae07c047c16b4b61b9b71ecd29a61/7290f64bf1c77ddd-dc/s250x400/903498bd7d758c0308db075034b7f432b5ba8366.gif",
            "https://64.media.tumblr.com/81c6a572ba6f49481b1ec7ad8d1cc9f4/7290f64bf1c77ddd-2d/s250x400/25fe40f7704f40d63a4f0ddd1c7d0a4f42608344.gif",
            "https://64.media.tumblr.com/f3e23308ae8bace94d062fa2e6fbfe5f/e8fc55e383b48e3e-5e/s250x400/0be467a874a949b45cdc41f16b8b317837b23d47.gif",
            "https://64.media.tumblr.com/da85079c85534683aa53fb763d4d1dd8/ef93c3a58a0351ce-d2/s400x600/611e588493e25b6884c0435f3027164cfea71475.gif",
            "https://64.media.tumblr.com/fe8e5d7b744ede9af48b789bf0233c32/ef93c3a58a0351ce-e2/s400x600/210e6ca20c9d4808efcba3f7078e24b19a1435f2.gif",
            "https://64.media.tumblr.com/34ecb0ab29fcdef5162db88b17dbbf60/35a40c21915888bc-18/s400x600/38a96163f25f186bc9461afd2d6be28c49b95295.gif",
            "https://64.media.tumblr.com/7ad843a4be7c2aaf0fa84cbf915b24a1/861154d116409519-86/s540x810/cb0f421cf7bf7e061996631a3f99c3fd999bb5f7.gif",
            "https://64.media.tumblr.com/632ead720a3c5929d99bfac2853c6373/1e5f1137aa77b023-77/s250x400/e1b104152f5dc287e0181bc09ffcddc302339cba.gif",
            "https://64.media.tumblr.com/58aac89283e92150e9135a7c07948efc/f4d925f44e07bc74-fe/s400x600/0d68b0aca7ebce4842245dd522008f41ee1a67b9.gif",
            "https://64.media.tumblr.com/b352306f520c92dd55a192a594845ca2/26428aed59af714b-5b/s250x400/e33339120cea48064a994cc5eefa2a2381496740.gif",
            "https://64.media.tumblr.com/4e557f6362ee900813c2ed32277ce35d/59cc50ef9fdb03e7-79/s250x400/44e7d7fa078fdfc40e261a3816c9fe2e9f7a4a68.gif",
            "https://64.media.tumblr.com/96cdac8b333060c207adeaa180563fed/2e22d4fa400d7650-42/s250x400/73ce3e962bba0fa5977a5ac7ebf8c5acbfc0cf35.gif",
            "https://64.media.tumblr.com/894da9834cc6c98edbbb2c7d147dabfe/2b2ea54ceedd91a4-0c/s400x600/08953cbe0b90a39f5867f843f400607abf63bbc7.gif",
            "https://64.media.tumblr.com/6cef17f7b063bee7dbae32abffaf4052/75c331dd786b5d51-58/s250x400/690183b088129a29575c53eb78c880f2c63d0e31.gif",
            "https://64.media.tumblr.com/609a53fd16838750ed8a418deff213e9/f70ad9f69fcbe327-b4/s400x600/8f3cf70b980e25c3ec6d40e9b54b4a036589bed7.gif",
            "https://64.media.tumblr.com/d8cf2caedf3d647517851b24ca79f227/0d16c72a083ed72e-fd/s400x600/151d8032b64cd0de8665683590bf030d824d5934.gif",
            "https://64.media.tumblr.com/821e7a4d3de4f547d16ad0f3323bf3ab/1a34a3eb03cf0bc1-cc/s250x400/923d95274b9cdc965a125101c961826efb1b4cee.gif",
            "https://64.media.tumblr.com/af8b2af14f2430c3791a937284820c72/tumblr_pzh4u8xU401y51zjto2_400.gif",
            "https://64.media.tumblr.com/0123422b078190a0f3f2936a6daadcd4/ea4e37e1feff3d9b-2d/s250x400/6d7dbd706c1211eeff4c57c4b1b6030b112d6f94.gif",
            "https://64.media.tumblr.com/238c4853d4fc01a1562af1594cf1d6cb/d0f07b9d683f94a6-2c/s400x600/4b505562a4b5a93c4b7813074fc7499e704acc29.gif",
            "https://64.media.tumblr.com/26195c752ead6f20c38191f1fbe8c29f/9cb1c0cb6ff1dcd4-92/s250x400/36634e195d411ccc5f93137e5560aadd6306cc84.gif",
            "https://64.media.tumblr.com/e7098e2f708c07b5cafce6a83e67bf56/9cb1c0cb6ff1dcd4-36/s250x400/71ed86c087e50fb3e68350a20ad6811a5af92221.gif",
            "https://64.media.tumblr.com/8a72f66db1b04798d1c06f6f725f5f76/4b499fe77ee6ce52-60/s250x400/22e49dbb8d837fe375b8923fd23729d26b9253ac.gif",
            "https://64.media.tumblr.com/ce7ddb8de658779f62e529c6c072b3b4/fecf39e82c1e66af-da/s250x400/c11262b7d4ced3da7b728b13dfcb690f797ec3e3.gif",
            "https://64.media.tumblr.com/23816533e9989c0efae388d0fa201f5e/3555f9f2910a38ca-a7/s400x600/d0163fc8075695b87564676d6b960c1096f08768.gif",
            "https://64.media.tumblr.com/2c489910af03d86217a11d4766682d41/7cccc6538fb782ed-70/s400x600/d8d7d3ae140f15148cf90b8cbb85fe1a6ac2f733.gif",
            "https://64.media.tumblr.com/685d584fd2ea5a3778e175a65c5c5422/2663ae6e6c340401-21/s250x400/f605ade6239fe176c348ba50c2eb896403bae55c.gif",
            "https://64.media.tumblr.com/edd75405029482fb48b7fcfacb195fd0/2489d8250347ff95-80/s250x400/b4cb9e0593f872d2bad72429389e0e8bea91dda1.gif",
            "https://64.media.tumblr.com/878da0f75cbb24fa50e727f922213e6b/e8f112586e863629-a7/s400x600/7ff06ecd49b93c999c894fe72cbefdd5595109a8.gif",
            "https://64.media.tumblr.com/961e3b0d29c099a8feaeb78c5be88ded/3b228c48de341975-8d/s400x600/e9802590972c5b3d7c6069a28dde2d35f28bcf4a.gif",
            "https://64.media.tumblr.com/d75224b9d25715802d84bb987e2a964c/87b222c1d55fd157-2b/s400x600/032f4412aed188dd5da111fd4d79eb760e588142.gif",
            "https://64.media.tumblr.com/b45d9fe66a75475d65bc46367c8611ea/87b222c1d55fd157-cc/s400x600/0e33a047616aa2aa5050ae7b469a719fb10d112c.gif",
            "https://64.media.tumblr.com/72cebe4287b3c2741407857165acf3a9/87b222c1d55fd157-e9/s400x600/e04ca8658282dd54b5e79f010475e03c6d169031.gif",
            "https://64.media.tumblr.com/3241fdf4e4b6e82b8a1fee21eac91ffa/tumblr_pnu5dnIQh71u1fc83o7_r2_400.gif",
            "https://cdn.discordapp.com/attachments/807314037712748544/809242450987843614/Tumblr_l_454468591757129.gif",
            "https://cdn.discordapp.com/attachments/807314037712748544/809242451591430144/Tumblr_l_454474837691933.gif",
            "https://cdn.discordapp.com/attachments/807314037712748544/809242452438941706/Tumblr_l_454153343662201.gif",
            "https://64.media.tumblr.com/3c56eeb2c258f1ec29be8285b26474b1/79b4dd27c37c449a-ff/s400x600/04b7569fb434fa21b7efdb6793c8333a2b4cece6.gif",
            "https://64.media.tumblr.com/0d1387b3a7d7ce8ffac6ce3864d85aea/33ae048e3ca441ff-2d/s400x600/f74981e1df50d1607a55605101b2b695ead61321.gif",
            "https://64.media.tumblr.com/48a87ac162fa4fd23117f07f3f53ad92/33ae048e3ca441ff-25/s250x400/93c16ae044cac4844a5f4d90e9f7cb6c87f4404b.gif",
            "https://64.media.tumblr.com/b2df770aedef04d1235b4b3a22c081a8/48326eda540b84be-d2/s250x400/0e68173651b40408e3510d4fa31ccce4641016b0.gif",
            "https://64.media.tumblr.com/d970423f78ce2792f832288d7adaa1e3/b8331573a4293d9b-52/s250x400/ee8a320e854d0f1f905e727740ec1d46e27cab5b.gif",
            "https://64.media.tumblr.com/ae639e11830e714328bc06368d9c17da/6909eeda92011eb7-f7/s400x600/daac4567abe609cc70895c9f408d96e92c68cbfb.gif",
            "https://64.media.tumblr.com/328fa41135ea0ff55bcfca915d3a1a01/1a50101a837f31a4-5a/s400x600/0b618e051dd856cfcb048c4baa9e01ce4b3416ff.gif",
            "https://64.media.tumblr.com/e029c9c04df1da6c095faa1d1267ca39/1a50101a837f31a4-dc/s400x600/4806eb7d3397882d403f2831c2f11d3f45f50377.gif",
            "https://64.media.tumblr.com/54ac7490a51fc080a1821fb51750c306/4f4a5e55820fb49c-84/s250x400/4d75fc164b10c8ebc40a48b4ad8ea384d1b16a72.gif",
            "https://64.media.tumblr.com/35c622e02f65455dff09bbda9c05400f/4f4a5e55820fb49c-56/s250x400/09b3f34689a1eb2c92b6197fb23b84018d8b9805.gif",
            "https://64.media.tumblr.com/2c90a4527d13f2e543504f0ef2796da1/0119df94e819fd70-13/s250x400/69d4f91e1171f2a2c3094b99461a871f75c036be.gif",
            "https://64.media.tumblr.com/de196c71c58e09c8ba75d9fc4d9fe88e/df7b7eed65d0b271-f4/s250x400/ed89e1a20dd981c8a5dedbc6c0bb397afc16efab.gif",
            "https://64.media.tumblr.com/cc0897c1b500af66859ddfd6e6c92135/df7b7eed65d0b271-97/s250x400/522c1a2d6b8327456083633976ccf66f46db484b.gif",
            "https://64.media.tumblr.com/d0f2fc016b9f3a5d95dcc3106eea62f0/f4d925f44e07bc74-97/s400x600/bbeab9b7f751213a6efdcdc56d536e7b5f8a08c8.gif",
            "https://64.media.tumblr.com/58fda757dfe7cfbeeab4b955234bd9d8/9acc7760c92a2349-dd/s400x600/0714c59543dd61844945536e46dd9ada599c43b1.gif",
            "https://64.media.tumblr.com/37c55aeb87a52eb1c1fc6f849ab9adb0/9acc7760c92a2349-e7/s400x600/d6833784368e78ce195689cf2c51aa8c342c8fa5.gif",
            "https://64.media.tumblr.com/7f90ee785c89d5c33969fb905f634408/113bbae9f9286a4c-60/s250x400/996f6b2a6c8a951ff31be7795768a701f99e384d.gif",
            "https://64.media.tumblr.com/392dde620e2fad9c1283874329e08c62/c106f5b90d750764-d5/s250x400/6fbb603e61bf91b5a8b8fd451a3a05b6ec8f706d.gif",
            "https://64.media.tumblr.com/1a3f3228607db6ab8e8830870677e406/84c26e27d0150f38-3a/s250x400/14f72aaa0e991762bbcf4ed5055a2c1eba18bb3b.gif",
            "https://64.media.tumblr.com/46df9084f07d75d133be1bb5ab8c1bb8/295d56b2120fd51e-aa/s250x400/7c18566ab14fadd840cb2d18e9bb98bdd39724c6.gif",
            "https://tenor.com/view/beomgyu-txt-gif-18631877",
            "https://tenor.com/view/beomgyu-beomgyu-pout-beomgyu-txt-tomorrow-x-together-new-rules-beomgyu-gif-15383636",
            "https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-beomgyu-gif-17660347",
            "https://tenor.com/view/choi-beomgyu-txt-tomorrowbytogether-tomorrowxtogether-gif-16277593",
            "https://tenor.com/view/txt-moa-beomgyu-gif-19581614",
            "https://tenor.com/view/%EC%B5%9C%EB%B2%94%EA%B7%9C-%EB%B2%94%EA%B7%9C-beomgyu-txt-gif-18600830",
            "https://tenor.com/view/txt-beomgyu-eating-sweet-cute-gif-14481352",
            "https://gfycat.com/disgustingnauticalkusimanse",
            "https://gfycat.com/testyfinebarasingha",
            "https://gfycat.com/remarkablealtruistichairstreakbutterfly",
            "https://gfycat.com/sinfulshrillamericanpainthorse",
            "https://gfycat.com/whoppingscalyguernseycow",
            "https://gfycat.com/smoothamusingflea",
            "https://gfycat.com/ordinarypitifulilladopsis",
            "https://tenor.com/view/cat-and-dog-txt-tomorrow-x-together-tomorrow-by-together-txt-cat-and-dog-gif-16375703"]

        self.bot.txt_taehyun_gif = ["https://tenor.com/view/txt-taehyun-kang-taehyun-kang-taehyun-txt-taehyun-txt-gif-18959632",
            "https://tenor.com/view/taehyun-kang-taehyun-txt-tomorrow-x-together-taehyunie-gif-19009636",
            "https://tenor.com/view/txt-taehyun-taehyun-kang-taehyun-taehyun-heart-gif-19290757",
            "https://tenor.com/view/kang-taehyun-txt-tomorrowbytogether-tomorrowxtogether-gif-16277417",
            "https://tenor.com/view/txt-taehyun-taehyun-txt-taehyun-aegyo-kangtaehyun-taehyun-cute-gif-19361155",
            "https://tenor.com/view/kang-taehyun-txt-tomorrow-by-together-tomorrow-x-together-todo-gif-16310954",
            "https://tenor.com/view/txt-taehyun-txt-txt-taehyun-kangtaehyun-txt-drama-gif-19384362",
            "https://64.media.tumblr.com/506757257562f200f99a7439cedfd1e2/006a8455cb49cac7-e9/s400x600/9800099716f90b006b5c93415a07f876caeab789.gif",
            "https://64.media.tumblr.com/9b416a2c47d685b47ed060d5d8e366cc/9c3d909260c8cd9e-1f/s400x600/57e1a80f82565baafdc4d799207c186277e390cf.gif",
            "https://64.media.tumblr.com/0122c73225cbfe13029994d84dd74c62/25ddb8f6c30f1092-66/s400x600/76bdeb4d5f723220357fa9f862be35840bbb96dc.gif",
            "https://64.media.tumblr.com/1d866233932ec708793037cdeffbfb2d/25ddb8f6c30f1092-da/s400x600/e8997c6c57fa6a8f91fa35e15b4b696859e5d45d.gif",
            "https://64.media.tumblr.com/b5e32c467b1d6df3a5507ba31952874b/1dd8fd33efe647c1-b1/s400x600/04907fdce08e0f9452c78bf933986bc94ed6d4b6.gif",
            "https://64.media.tumblr.com/8cbe6af05232df8cc8fc661b86db4865/b600daa336b4aa16-38/s400x600/1ed66ab938409ed9d68e6f217d43425c1388d3d7.gif",
            "https://64.media.tumblr.com/8b733de869e609827bcc0d52908d3af8/33b69961da04d201-2f/s540x810/5135c4d318332d6b39e4e00462994e3813b78c80.gif",
            "https://64.media.tumblr.com/e90001bcda002add01cc23a5e304af93/59b4026a1821c95a-e9/s250x400/dc3d1a0ae39bb1a5f6f497eea76dd57cbdcfdf99.gif",
            "https://64.media.tumblr.com/9f77a0f2d53c5cc8f6629af22ee2573f/59b4026a1821c95a-d3/s250x400/d87225fa0e9a96fdec69d66a379765312b6ffb98.gif",
            "https://64.media.tumblr.com/374265d82ebfd61e109adb4de7fa7730/d4ee177f95387426-bc/s250x400/223936a792e97f2a759b601d3240328b3c9cec48.gif",
            "https://64.media.tumblr.com/6f3ac83d4cf6d5f89d7b97856c1c8f98/423edd95dfef67fb-80/s250x400/6e7ec1433e14e1ab7183e7a9a8d7ddf7452a52cf.gif",
            "https://64.media.tumblr.com/80b6cfcc330d4b2ef9f1eb8603f3c84e/6f8b6b6e721c3e40-08/s400x600/ee98f38a60605f00a4319925ca1640c6a383b0d1.gif",
            "https://64.media.tumblr.com/6ccfda0569f770c342f6e2f9b2dcadda/94ea04ef76949660-25/s250x400/5591329449dfc0afa154788d5913b3ceb3c6ed8e.gif",
            "https://64.media.tumblr.com/69159f10b9b2e5f57c1008f11836e606/94ea04ef76949660-1a/s250x400/4abf19b84d36f6c63a284f2c97e04d4ed5cca1a2.gif",
            "https://64.media.tumblr.com/fca070236e43834afbb2a153f8f1c066/59daaa1549e16c5d-97/s250x400/54ba36b0681064572d571a00c41109bfe3f410a9.gif",
            "https://64.media.tumblr.com/ca47d2c301bec91ab20790c428e15e41/f307ebd27b126432-74/s400x600/6e9bc9dbb2ebf96f682b47de259140d2b7421ff7.gif",
            "https://64.media.tumblr.com/2b1e065e70d489e5c8aaf0bc3da3c420/efbe7a4cda536152-28/s400x600/87964840a162c0d8f02acc4c8d145b8cafc6912b.gif",
            "https://64.media.tumblr.com/d0ed49b3bea4d7067731a5fbd9fbba81/81acacd2fcb70d9f-d9/s400x600/4e2558e670a7db9aa9e365c515f7309c9607db02.gif",
            "https://64.media.tumblr.com/953f394fc554a4affc97889c2b243265/d91f17fce63545c1-e0/s400x600/7f45d03a7432e2cbdf2698bef325da081e0c9d19.gif",
            "https://64.media.tumblr.com/781442352195056f039d2cc992671421/d91f17fce63545c1-95/s400x600/185b9f0c6697afd9d324082d7ad02e205c98f75b.gif",
            "https://64.media.tumblr.com/d66cbba044a739d85a0a55cb4c7c59ab/481e4fc4beeb0fe7-b8/s400x600/6c732520ac20a70f451754676dd7667bc4e74305.gif",
            "https://64.media.tumblr.com/7e2d05a464b4d571c49a2e8cb283d77c/481e4fc4beeb0fe7-67/s400x600/7b91862694e0c13bb3b2871a842257eea33c962a.gif",
            "https://64.media.tumblr.com/e4f1d16dac0490fd0a439eda2bba542c/481e4fc4beeb0fe7-76/s400x600/adf3601da1a9bd8eb0618d4ba01dcf26f45089a4.gif",
            "https://64.media.tumblr.com/0c99e0047956bfd5a6a11b54d300671e/1ad497ed88fe1a82-0e/s250x400/12e92d2a60b778e16902c7408fea26603a9450a9.gif",
            "https://64.media.tumblr.com/5ce02fb953f47da26bebd27798d33e46/b157fb90c357433c-d9/s250x400/112494407ea25214b183f04de3507beb8ede329e.gif",
            "https://64.media.tumblr.com/a3c769b5378a4b56243a5c743712b87e/6b2ef7d9d62f22da-fc/s400x600/b8a69036427bf2d552fffd46f78185b11f2dcfea.gif",
            "https://64.media.tumblr.com/62279cb0b8e2192bec52439ae6244905/574f3be874229f0b-b7/s250x400/39b36aeeae7cf15cad38091dcbf1fa6a6d330005.gif",
            "https://64.media.tumblr.com/29abda341ecec8c60b71de6370df10b9/02c985443d4a9ff2-2e/s250x400/5c671aa2ba3735b9654d54131d858daa51cc4386.gif",
            "https://64.media.tumblr.com/5da0155e63c796dadf88d17b5c870e93/b2696e81b9da65b2-1d/s250x400/afdababd58adcec0bf5e7cd766e564348dbb733d.gif",
            "https://64.media.tumblr.com/21c5e7ecddd7d0d245d374ea9fc433b9/0b6f825c365820df-81/s400x600/3f24227f25234258f22f22ac7504b9ee73c9da34.gif",
            "https://64.media.tumblr.com/18c1608bb510c121b83a45610537001a/26f3e204676f6e31-1d/s400x600/7375503a621c6712b53a136da3d4d82465cfe5d0.gif",
            "https://64.media.tumblr.com/5754e969157aecbc1079fdb15d2f132e/1ec35c5234526683-4d/s250x400/bdb90caaf3e4088fd6a0cadd93f08ab2f9d526ce.gif",
            "https://64.media.tumblr.com/04b155956f5d3f0b4d6f1251bc5886f8/c655a2403fe63946-12/s250x400/7f76563230de93fe9b157f83f575f87dc36c4159.gif",
            "https://64.media.tumblr.com/86d8bfc55c0111d51f37f1f872b90aef/c655a2403fe63946-a2/s250x400/7ded650486fc8bb1211e6b3433a9f26a634cfc10.gif",
            "https://64.media.tumblr.com/535b5fff1a41d0ef645afc7a4ca7d03b/c655a2403fe63946-87/s250x400/1e9139aa92dbd33ae2e83b6930171d293df94ca3.gif",
            "https://64.media.tumblr.com/d8cf540a6c265cfec93742e887c7ee77/c655a2403fe63946-21/s250x400/8b2f53e682caae92de7de6f20d1202da4de2c55e.gif",
            "https://64.media.tumblr.com/441186f41d16e64b3eee7bb4d19e488c/84acf6e243adbb48-a0/s400x600/941f419d017abb11a99ace022a6228c2fe698756.gif",
            "https://64.media.tumblr.com/f61c35f6ab75c48f59fa0d623f00187c/7d56f23aa5a39ecb-4d/s250x400/892c947636e069f31e11acb5d0a8b63c28194666.gif",
            "https://tenor.com/view/txt-taehyun-taehyun-kangtaehyun-taehyun-cute-taehyun-txt-gif-19361137",
            "https://gfycat.com/creepyglamorouseyas",
            "https://gfycat.com/determinedunselfishamberpenshell"]

        self.bot.txt_hueningkai_gif = ["https://tenor.com/view/txt-huening-kai-hyuka-txt-hueningkai-huening-kai-blue-hour-gif-19341353",
            "https://tenor.com/view/love-huening-kai-wink-confetti-performance-gif-16420492",
            "https://tenor.com/view/performance-stage-music-dance-dance-performance-gif-15902429",
            "https://tenor.com/view/huening-kai-im-dead-ghost-cute-handsome-gif-16798350",
            "https://tenor.com/view/hueningkai-huening-kai-kpop-txt-gif-19211443",
            "https://tenor.com/view/txt-puma-puma-huening-kai-hyuka-kai-gif-18009318",
            "https://tenor.com/view/txt-huening-kai-cant-you-see-me-gif-18717975",
            "https://64.media.tumblr.com/2c046435dc00aeb9f0af34e3d75a5ed3/50d0abd235da0690-78/s400x600/72c4cadf406161638f2fe462a6caf83c92e5bc4d.gif",
            "https://64.media.tumblr.com/a33c6f9c285e87b6c9449c11bb7be87f/923906fa12c68ec4-70/s400x600/968c5b8552dd768e659bd9f9190f2680498d37ea.gif",
            "https://64.media.tumblr.com/6ba15b5de4c5a84d8b6e84ce4c696b5c/006a8455cb49cac7-b9/s400x600/f66520089b1a4c813f7e67627eb8f502112b5b7e.gif",
            "https://64.media.tumblr.com/f982d4a7d8210343c1ac314e8560b1ca/88fcaf885095be25-df/s400x600/c3d077938f4c13927c96a99981dbaa603b2c6262.gif",
            "https://64.media.tumblr.com/57693e787a8a5f2b15530af20e22f54f/ecd310db29097256-d9/s400x600/f1e3d5271ebd48ed9efd1680d460b8cf66c68c57.gif",
            "https://64.media.tumblr.com/5e8c81429ce2f1fece45fe7306c0cce7/ecd310db29097256-b4/s400x600/4b3eb5fa1acbe3a62f61921929aad0d1a706de22.gif",
            "https://64.media.tumblr.com/28bc97bc7906e5085e0aa7fb71400ee4/41fb363d52a0ca85-8a/s400x600/a9118aedd8e85110c85d23fe03f50e464ebe2cb9.gif",
            "https://64.media.tumblr.com/a39e7dac69d4d67d945bc5fce6a2617a/41fb363d52a0ca85-56/s400x600/eb2175724738f3e7b9cff5d9f7850f4d81574ebb.gif",
            "https://64.media.tumblr.com/ae231b0138a37279f07820a4b17e5d44/d73b75a307d4e44c-01/s400x600/f67a2c88d97ffcd599073e3826fab85279269980.gif",
            "https://64.media.tumblr.com/37a1a67f7404f7bc91340c58861a02dc/tumblr_pnzt9u1Qiq1y4hs0wo1_250.gif",
            "https://64.media.tumblr.com/849fa882a7e484f5ef7edafbe06cff9c/tumblr_po9f2vBHrU1y4hs0wo1_250.gif",
            "https://64.media.tumblr.com/a7ae41587995b2806e0c78393279fa85/tumblr_ptqp79LT7Q1ynxih9o4_250.gif",
            "https://64.media.tumblr.com/a6840054e0f7a852a78f8245830c787a/7e0f5c0b1508e63a-f9/s400x600/07a9263c5e859dce734c3900020f6b62be71245c.gif",
            "https://64.media.tumblr.com/f937d826177385b4303077df2b36f19e/7e0f5c0b1508e63a-e3/s400x600/a13a664431639703d74e46a6a7e3bb8dbda2505c.gif",
            "https://64.media.tumblr.com/396a2ac4fb84d79bb940aa24f16c9ba2/7e0f5c0b1508e63a-ab/s400x600/bdf7a4deca04573bc670b91aada878f3b3abf92c.gif",
            "https://64.media.tumblr.com/58406b53ed84b0df33bf07c28fd7b543/tumblr_pqgv6xn8RW1y4hs0wo5_400.gif",
            "https://64.media.tumblr.com/af24a4884f0eded0ddff992488a017cc/tumblr_inline_pohmjzZETz1w2lw8w_400.gif",
            "https://64.media.tumblr.com/7dd2c75bc252d0eb5ce31fd071c8d056/04fc32b0b11cf902-b1/s250x400/72f063668d8722078a134aadd0c718d3e655f703.gif",
            "https://64.media.tumblr.com/a74aa6e24ae20231a78b46fbb1a306ab/04fc32b0b11cf902-54/s250x400/35eaf6dfcee71b545364adca25a8bde338da7e06.gif",
            "https://64.media.tumblr.com/e0a75c6bb3faa1c20f2665ad4b389af6/tumblr_plsjnyhRGt1us7sgvo1_400.gif",
            "https://64.media.tumblr.com/8381bdd8ccd75363d65571ce0fcc0149/tumblr_plsjnyhRGt1us7sgvo2_400.gif",
            "https://64.media.tumblr.com/9c376e8162eb5c3807f95d9eaeb99151/dc30df792ff4f184-b9/s400x600/764b47fc46a4892cff840e91bd4950a5642e9515.gif",
            "https://64.media.tumblr.com/efde7b36ac992bc6c24309a44a6dba7b/dc30df792ff4f184-18/s400x600/5bc7a46a9ac5de8524ed296e90d1dbabb3eb416f.gif",
            "https://64.media.tumblr.com/ef9525874b1b1976320e2114aa0d3391/tumblr_prwnldM2At1y4iumjo2_250.gif",
            "https://64.media.tumblr.com/08d4c4dc85dcc3ad0eb054ebf71c88c4/tumblr_pldp3uddd01y4f16vo3_400.gif",
            "https://64.media.tumblr.com/5e6b09892854b14ad996f6b03d62ff1c/390edc5e35873f89-a1/s400x600/ee11b8ece1ebea614644c16ba3cff408ae69b147.gif",
            "https://64.media.tumblr.com/1f3fc49b74866351224e04c77824f87e/1250dfd06a6ed377-a0/s250x400/249ffd9f431d352d703011e68703fb06a86d9144.gif",
            "https://64.media.tumblr.com/b72314a7a14ed3aa91f2a8162d2fb193/7e0a55a84f6adf9c-02/s400x600/06f3f2445f288f7cf8bd23caa873881f6b2659db.gif",
            "https://64.media.tumblr.com/99fe259414ce3b8ab19560edbaeb6aff/b9ac5b79f239a23b-ef/s400x600/0e67f874deeb2c5cc78f52437d255598fcabec49.gif",
            "https://64.media.tumblr.com/79ef6af4fda0839abe65b027b846a495/tumblr_pnjh8yEkLn1y4f16vo2_400.gif",
            "https://64.media.tumblr.com/bc0777b016138d7077010b9d6b752d64/ceac2dffda5e4ffe-22/s250x400/69105ca55da91a92fc26db0508100590771a0666.gif",
            "https://tenor.com/view/sookai-soobin-hueningkai-kai-hyuka-gif-18364963",
            "https://gfycat.com/finishedindolentdunnart"]

        self.bot.txt_ot5_gif = ["https://tenor.com/view/txt-tomorrow-x-together-teen-vogue-puma-yeonjun-gif-17788891",
            "https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-txt-group-gif-19340189",
            "https://tenor.com/view/yeonjun-txt-cpr-yeonjun-cpr-moa-gif-17201920",
            "https://tenor.com/view/txt-cat-dog-tomorrow-x-together-big-hit-gif-14005559",
            "https://tenor.com/view/ot7-kaisercrew-ot5-txt-jejuisland-gif-18632016",
            "https://tenor.com/view/txt-tomorrowxtogether-tomorrow_x_together-ot5-soobin-gif-18388545",
            "https://tenor.com/view/bye-bye-everyone-byebye-see-yah-see-you-gif-14624568"]

    @commands.command()
    async def txt(self, ctx, *, arg = "ot5"):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [TXT {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        if arg == "soobin":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Soobin :rabbit:')
                await ctx.send(random.choice(self.bot.txt_soobin_gif))
                await ctx.message.delete()
        elif arg == "yeonjun":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yeonjun :fox:')
                await ctx.send(random.choice(self.bot.txt_yeonjun_gif))
                await ctx.message.delete()
        elif arg == "beomgyu":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Beomgyu :bear:')
                await ctx.send(random.choice(self.bot.txt_beomgyu_gif))
                await ctx.message.delete()
        elif arg == "taehyun":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Taehyun :chipmunk:')
                await ctx.send(random.choice(self.bot.txt_taehyun_gif))
                await ctx.message.delete()
        elif arg == "huening kai":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Huening Kai :penguin:')
                await ctx.send(random.choice(self.bot.txt_hueningkai_gif))
                await ctx.message.delete()
        elif arg == "ot5":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about TXT :penguin:')
                await ctx.send(random.choice(self.bot.txt_ot5_gif))
                await ctx.message.delete()

def setup(client):
    client.add_cog(txtPings(client))