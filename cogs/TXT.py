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
            "https://64.media.tumblr.com/ec923667af58d540adcea3cc4b6124ee/6f5e0fa2421a8291-35/s250x400/6e170a3d75af6f55e1feb99b115210f7e2f885b9.gif"]

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
            "https://cdn.discordapp.com/attachments/807006158665285673/807007674033635348/Tumblr_l_213971776728731.gif"]

        #7
        self.bot.txt_beomgyu_gif = ["https://tenor.com/view/txt-tomorrow-x-together-tomorrow-by-together-big-hit-entertainment-beomgyu-gif-17683775",
            "https://tenor.com/view/beomgyu-txt-tomorrow-x-together-kpop-choi-beomgyu-gif-19211104",
            "https://tenor.com/view/performance-stage-dance-dance-performance-%EB%B2%94%EA%B7%9C-gif-15902416",
            "https://tenor.com/view/choi-beomgyu-txt-tomorrow-by-together-tomorrow-x-together-todo-gif-16310981",
            "https://tenor.com/view/beomgyu-beomgyu-model-beomgyu-runway-txt-beomgyu-beomgyu-txt-gif-18950063",
            "https://tenor.com/view/choi-beomgyu-txt-tomorrow-by-together-tomorrow-x-together-todo-gif-16310980",
            "https://tenor.com/view/beomgyu-choi-beomgyu-txt-tomorrow-x-together-kpop-gif-19211432"]

        #7
        self.bot.txt_taehyun_gif = ["https://tenor.com/view/txt-taehyun-kang-taehyun-kang-taehyun-txt-taehyun-txt-gif-18959632",
            "https://tenor.com/view/taehyun-kang-taehyun-txt-tomorrow-x-together-taehyunie-gif-19009636",
            "https://tenor.com/view/txt-taehyun-taehyun-kang-taehyun-taehyun-heart-gif-19290757",
            "https://tenor.com/view/kang-taehyun-txt-tomorrowbytogether-tomorrowxtogether-gif-16277417",
            "https://tenor.com/view/txt-taehyun-taehyun-txt-taehyun-aegyo-kangtaehyun-taehyun-cute-gif-19361155",
            "https://tenor.com/view/kang-taehyun-txt-tomorrow-by-together-tomorrow-x-together-todo-gif-16310954",
            "https://tenor.com/view/txt-taehyun-txt-txt-taehyun-kangtaehyun-txt-drama-gif-19384362"]

        #7
        self.bot.txt_hueningkai_gif = ["https://tenor.com/view/txt-huening-kai-hyuka-txt-hueningkai-huening-kai-blue-hour-gif-19341353",
            "https://tenor.com/view/love-huening-kai-wink-confetti-performance-gif-16420492",
            "https://tenor.com/view/performance-stage-music-dance-dance-performance-gif-15902429",
            "https://tenor.com/view/huening-kai-im-dead-ghost-cute-handsome-gif-16798350",
            "https://tenor.com/view/hueningkai-huening-kai-kpop-txt-gif-19211443",
            "https://tenor.com/view/txt-puma-puma-huening-kai-hyuka-kai-gif-18009318",
            "https://tenor.com/view/txt-huening-kai-cant-you-see-me-gif-18717975"]

    @commands.command()
    async def txt(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [TXT {arg} | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
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


def setup(client):
    client.add_cog(txtPings(client))