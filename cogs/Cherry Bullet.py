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

class CherryBullet(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.cherrybullet_bora_gif = ["https://tenor.com/view/bora-chabul-gif-19633080",
            "https://tenor.com/view/bora-chebul-gif-19633077",
            "https://tenor.com/view/bora-chebul-gif-19633078",
            "https://tenor.com/view/bora-chebul-gif-19633079",
            "https://tenor.com/view/kcon2019japan-kcon-%EC%BC%80%EC%9D%B4%EC%BD%98-m-countdown-mnet-gif-14557828",
            "https://tenor.com/view/bora-chebul-gif-19633079",
            "https://tenor.com/view/kcon2019japan-kcon-%EC%BC%80%EC%9D%B4%EC%BD%98-m-countdown-mnet-gif-14557828",
            "https://cdn.discordapp.com/attachments/805983594925391902/805987008735477800/image0.gif",
            "https://cdn.discordapp.com/attachments/805983594925391902/805987009100775434/image1.gif",
            "https://cdn.discordapp.com/attachments/805983594925391902/805987009490583613/image2.gif",
            "https://cdn.discordapp.com/attachments/805983594925391902/805987009863745557/image3.gif",
            "https://cdn.discordapp.com/attachments/805983594925391902/805987010539683920/image4.gif",
            "https://cdn.discordapp.com/attachments/805983594925391902/805987038288543764/image0.gif",
            "https://cdn.discordapp.com/attachments/805983594925391902/805987038859886592/image1.gif",
            "https://cdn.discordapp.com/attachments/805983594925391902/805987039312609290/image2.gif",
            "https://gfycat.com/wickedrevolvinggoldenretriever",
            "https://gfycat.com/naivedarlinghamadryad",
            "https://gfycat.com/crispimpressionableislandcanary",
            "https://gfycat.com/welloffsmartaxolotl",
            "https://gfycat.com/imperfectvapidicelandgull",
            "https://gfycat.com/orneryadmiredgoat",
            "https://gfycat.com/fearfulscratchyamericanalligator",
            "https://gfycat.com/dampleanekaltadeta",
            "https://gfycat.com/jollysomeaplomadofalcon",
            "https://gfycat.com/difficultgrouchyhog",
            "https://gfycat.com/frequenthelplessindigowingedparrot",
            "https://gfycat.com/jollyknobbydoctorfish",
            "https://gfycat.com/hideousunawareagouti"]

        self.bot.cherrybullet_chaerin_gif = ["https://cdn.discordapp.com/attachments/805983341849477140/805987297425358848/image0.gif",
            "https://cdn.discordapp.com/attachments/805983341849477140/805987297770209291/image1.gif",
            "https://cdn.discordapp.com/attachments/805983341849477140/805987298323071056/image2.gif",
            "https://cdn.discordapp.com/attachments/805983341849477140/805987423254478918/image0.gif",
            "https://cdn.discordapp.com/attachments/805983341849477140/805987423754125332/image1.gif",
            "https://cdn.discordapp.com/attachments/805983341849477140/805987424470564884/image2.gif",
            "https://cdn.discordapp.com/attachments/805983341849477140/805987491135356952/image0.gif",
            "https://cdn.discordapp.com/attachments/805983341849477140/805987491898458142/image1.gif",
            "https://cdn.discordapp.com/attachments/805983341849477140/805987492330864709/image2.gif",
            "https://cdn.discordapp.com/attachments/805983341849477140/805987555874308136/image0.gif",
            "https://cdn.discordapp.com/attachments/805983341849477140/805987556373299220/image1.gif",
            "https://gfycat.com/selfreliantneariraniangroundjay",
            "https://gfycat.com/embellishedzanyacornbarnacle",
            "https://gfycat.com/miserableilliteratedachshund",
            "https://gfycat.com/secretdecentleech",
            "https://gfycat.com/capitalvaluablekilldeer",
            "https://gfycat.com/sizzlingimpressivealabamamapturtle",
            "https://gfycat.com/brightposhbackswimmer",
            "https://gfycat.com/homelyoddballhuia",
            "https://gfycat.com/repulsivefluidarcticwolf",
            "https://gfycat.com/impressionabledentalcommongonolek",
            "https://gfycat.com/revolvingeverychupacabra",
            "https://gfycat.com/jollyserpentinealtiplanochinchillamouse",
            "https://gfycat.com/formalunlinedfalcon",
            "https://gfycat.com/terrificliveamericanrobin"]

        self.bot.cherrybullet_haeyoon_gif = ["https://tenor.com/view/haeyoon-gif-19633020",
            "https://tenor.com/view/haeyoon-gif-19633021",
            "https://tenor.com/view/haeyoon-gif-19633019",
            "https://tenor.com/view/haeyoon-gif-19633018",
            "https://tenor.com/view/haeyoon-gif-19633017",
            "https://tenor.com/view/open-mouth-ahh-jawdrop-blank-cherrybullet-gif-14606312",
            "https://cdn.discordapp.com/attachments/805984245511749652/805987967528730654/image0.gif",
            "https://cdn.discordapp.com/attachments/805984245511749652/805987967985778688/image1.gif",
            "https://cdn.discordapp.com/attachments/805984245511749652/805987968421855262/image2.gif",
            "https://cdn.discordapp.com/attachments/805984245511749652/805987968955318313/image3.gif",
            "https://cdn.discordapp.com/attachments/805984245511749652/805988113264148490/image0.gif",
            "https://cdn.discordapp.com/attachments/805984245511749652/805988127477858353/image0.gif",
            "https://cdn.discordapp.com/attachments/805984245511749652/805988135292764160/image0.gif",
            "https://64.media.tumblr.com/2cd7b4899d83f13527d1cb0e3f9a2f87/tumblr_pm15e3yO6M1x15lmpo1_400.gif",
            "https://64.media.tumblr.com/1d11acb01006ed23c21caba6cd26aa79/tumblr_pm15e3yO6M1x15lmpo2_400.gif",
            "https://64.media.tumblr.com/5418f0e6230a16fb3a86b4ce490a0875/tumblr_pm15e3yO6M1x15lmpo3_400.gif",
            "https://64.media.tumblr.com/902ded09cb78a0aeafb20f40a9df32ff/tumblr_pm15e3yO6M1x15lmpo5_400.gif"]

        self.bot.cherrybullet_jiwon_gif = ["https://tenor.com/view/jiwon-cherrybullet-gif-19267608",
            "https://tenor.com/view/jiwon-cherrybullet-gif-19267631",
            "https://tenor.com/view/jiwon-cherrybullet-gif-19267645",
            "https://tenor.com/view/jiwon-cherrybullet-gif-19267642",
            "https://tenor.com/view/jiwon-cherrybullet-gif-19267587",
            "https://tenor.com/view/jiwon-cherry-bullet-pose-kpop-pretty-gif-16634902",
            "https://tenor.com/view/jiwon-cherrybullet-gif-19267648",
            "https://tenor.com/view/cherry-bullet-jiwon-may-kpop-cute-gif-16641928",
            "https://gfycat.com/neglectedgrandioseimperatorangel",
            "https://gfycat.com/immaculateidealisticarabianhorse",
            "https://gfycat.com/untidybravefattaileddunnart",
            "https://gfycat.com/madzealouscaecilian",
            "https://cdn.discordapp.com/attachments/805983699287015424/805988500277166090/image2.gif",
            "https://cdn.discordapp.com/attachments/805983699287015424/805988499253100584/image0.gif",
            "https://cdn.discordapp.com/attachments/805983699287015424/805988499617742878/image1.gif",
            "https://cdn.discordapp.com/attachments/805983699287015424/805988555381276713/image1.gif",
            "https://cdn.discordapp.com/attachments/805983699287015424/805988556157878293/image3.gif"]

        self.bot.cherrybullet_kokoro_gif = ["https://cdn.discordapp.com/attachments/805983739339210782/805984205057163266/image0.gif",
            "https://cdn.discordapp.com/attachments/805983739339210782/805984205343293470/image1.gif",
            "https://cdn.discordapp.com/attachments/805983739339210782/805984206068383774/image2.gif",
            "https://cdn.discordapp.com/attachments/805983739339210782/805984206824013864/image3.gif",
            "https://cdn.discordapp.com/attachments/805983739339210782/805984207305310218/image4.gif",
            "https://cdn.discordapp.com/attachments/805983739339210782/805988783862448138/image0.gif",
            "https://cdn.discordapp.com/attachments/805983739339210782/805988784629743656/image1.gif",
            "https://cdn.discordapp.com/attachments/805983739339210782/805988785476337674/image2.gif",
            "https://cdn.discordapp.com/attachments/805983739339210782/805988785766662184/image3.gif",
            "https://cdn.discordapp.com/attachments/805983739339210782/805988882327011338/image0.gif",
            "https://cdn.discordapp.com/attachments/805983739339210782/805988882730582026/image1.gif",
            "https://cdn.discordapp.com/attachments/805983739339210782/805988955882782800/image0.gif",
            "https://cdn.discordapp.com/attachments/805983739339210782/805988956122251264/image1.gif"]

        self.bot.cherrybullet_linlin_gif = ["https://cdn.discordapp.com/attachments/805984073507799070/805989153388101652/image0.gif",
            "https://cdn.discordapp.com/attachments/805984073507799070/805989153699266590/image1.gif",
            "https://cdn.discordapp.com/attachments/805984073507799070/805989154084093972/image2.gif",
            "https://cdn.discordapp.com/attachments/805984073507799070/805989154521088050/image3.gif",
            "https://cdn.discordapp.com/attachments/805984073507799070/805989287115751424/image0.gif",
            "https://cdn.discordapp.com/attachments/805984073507799070/805989287388119050/image1.gif",
            "https://cdn.discordapp.com/attachments/805984073507799070/805989287735722014/image2.gif",
            "https://cdn.discordapp.com/attachments/805984073507799070/805989288449015898/image3.gif",
            "https://cdn.discordapp.com/attachments/805984073507799070/805989343817760768/image0.gif",
            "https://cdn.discordapp.com/attachments/805984073507799070/805989344371671070/image1.gif",
            "https://cdn.discordapp.com/attachments/805984073507799070/805989442711060500/image0.gif"]

        self.bot.cherrybullet_may_gif = ["https://cdn.discordapp.com/attachments/805884231049936966/805989574668058634/image1.gif",
            "https://cdn.discordapp.com/attachments/805884231049936966/805989575193264189/image2.gif",
            "https://cdn.discordapp.com/attachments/805884231049936966/805989688715378718/image0.gif",
            "https://cdn.discordapp.com/attachments/805884231049936966/805989689453445131/image1.gif",
            "https://cdn.discordapp.com/attachments/805884231049936966/805989689865142362/image2.gif",
            "https://cdn.discordapp.com/attachments/805884231049936966/805989690237911132/image3.gif",
            "https://tenor.com/view/hirokawa-mao-mao-may-cherrybullet-cherrybullet-may-gif-20000895",
            "https://tenor.com/view/hirokawa-mao-may-cherrybullet-cherrybullet-may-may-cherrybullet-gif-20000300",
            "https://tenor.com/view/hirokawa-mao-may-cherrybullet-cherrybullet-may-may-cherrybullet-gif-20000847",
            "https://tenor.com/view/hirokawa-mao-may-cherrybullet-cherrybullet-may-may-cherrybullet-gif-20000845",
            "https://gfycat.com/powerfulremorsefulhawaiianmonkseal",
            "https://gfycat.com/idioticcalmlamb",
            "https://gfycat.com/pastelignorantkid",
            "https://gfycat.com/elateduncommonconey",
            "https://gfycat.com/directgreedykittiwake",
            "https://gfycat.com/widebelovedfrenchbulldog",
            "https://gfycat.com/theseabsolutecowrie",
            "https://gfycat.com/bluehonestborderterrier",
            "https://gfycat.com/imaginativecelebratedherring",
            "https://gfycat.com/medicaluntriedbagworm",
            "https://gfycat.com/earnestmalegroundbeetle",
            "https://gfycat.com/blandenragedjaguar",
            "https://gfycat.com/dismalpolisheddove",
             "https://gfycat.com/improbablehappygalapagosalbatross",
             "https://gfycat.com/hideousremarkablecomet"]

        self.bot.cherrybullet_mirae_gif = ["https://cdn.discordapp.com/attachments/805984147708575794/805989858379563018/image0.gif",
            "https://cdn.discordapp.com/attachments/805984147708575794/805989859067166740/image1.gif",
            "https://cdn.discordapp.com/attachments/805984147708575794/805989859545055312/image2.gif",
            "https://cdn.discordapp.com/attachments/805984147708575794/805989899794251776/image0.gif",
            "https://cdn.discordapp.com/attachments/805984147708575794/805989975933845534/image0.gif",
            "https://cdn.discordapp.com/attachments/805984147708575794/805989976490901514/image2.gif",
            "https://cdn.discordapp.com/attachments/805984147708575794/805990071467638795/image0.gif",
            "https://cdn.discordapp.com/attachments/805984147708575794/805990071806590996/image1.gif",
            "https://cdn.discordapp.com/attachments/805984147708575794/805990072318165012/image2.gif",
            "https://cdn.discordapp.com/attachments/805984147708575794/805990144314048512/image0.gif",
            "https://cdn.discordapp.com/attachments/805984147708575794/805990144795738122/image1.gif"]

        self.bot.cherrybullet_remi_gif = ["https://cdn.discordapp.com/attachments/805884130276409345/805990267018149958/image0.gif",
            "https://cdn.discordapp.com/attachments/805884130276409345/805990267412152320/image1.gif",
            "https://cdn.discordapp.com/attachments/805884130276409345/805990267865530398/image2.gif",
            "https://cdn.discordapp.com/attachments/805884130276409345/805990315282268171/image0.gif",
            "https://cdn.discordapp.com/attachments/805884130276409345/805990317245333504/image2.gif",
            "https://cdn.discordapp.com/attachments/805884130276409345/805990317878804490/image3.gif",
            "https://cdn.discordapp.com/attachments/805884130276409345/805990341576622121/image0.gif",
            "https://cdn.discordapp.com/attachments/805884130276409345/805990341915312158/image1.gif",
            "https://gfycat.com/boldwhimsicalalpinegoat",
            "https://gfycat.com/legitimatefluidantlion",
            "https://gfycat.com/annualscornfulamericanbittern",
            "https://gfycat.com/commonrealblueshark",
            "https://gfycat.com/bruisedableewe",
            "https://gfycat.com/plainaridbuzzard",
            "https://gfycat.com/officialqualifiedbudgie",
            "https://gfycat.com/sarcasticuntimelydrake",
            "https://gfycat.com/hilariouscoarseamericanblackvulture",
            "https://gfycat.com/silverrevolvingankole",
            "https://gfycat.com/backimaginaryirishwaterspaniel",
            "https://gfycat.com/loathsomeoptimisticaffenpinscher",
            "https://gfycat.com/jubilantshamefulamericancrayfish",
            "https://gfycat.com/knobbycirculardrever",
            "https://gfycat.com/constantoptimisticassassinbug",
            "https://gfycat.com/querulousneglectedamericanbittern",
            "https://gfycat.com/courteousanguisheddonkey",
            "https://gfycat.com/vastnewfowl",
            "https://gfycat.com/dizzywhoppinghammerkop",
            "https://gfycat.com/bonythirstyafricanrockpython",
            "https://gfycat.com/bleakanyfowl",
            "https://64.media.tumblr.com/e2be09d36751bb79ffae02cd543771ff/ce24503b95d8581b-29/s400x600/8e3b3de5b83db02b3c7abc2f7ec72e8d62538328.gif",
            "https://64.media.tumblr.com/145e9337b9f6bf8ac99bd32b5f586f18/ce24503b95d8581b-1f/s400x600/3e07693590291a5d65d58900da11cac7ad1cacff.gif",
            "https://64.media.tumblr.com/8d6ff2948cca8d3a0846e326ec0ba983/ce24503b95d8581b-20/s400x600/65eb1136c678de3c9304a118f78954db083959fc.gif",
            "https://64.media.tumblr.com/11e62111137ea34ddcac564863f91273/ce24503b95d8581b-90/s400x600/e77d3c895f9fdab3c2747e394cd35518b3ccfcef.gif"]

        self.bot.cherrybullet_yuju_gif = ["https://tenor.com/view/yuju-cherry-bullet-kpop-huh-suprised-gif-17717737",
            "https://tenor.com/view/yuju-cherry-bullet-kpop-huh-suprised-gif-17717737",
            "https://tenor.com/view/cherry-bullet-yuju-pretty-girl-smiling-gif-16634873",
            "https://tenor.com/view/cherry-bullet-yuju-cherry-bullet-smile-kpop-cute-gif-17717767",
            "https://tenor.com/view/cherry-bullet-yuju-kpop-dancing-cute-gif-17717719",
            "https://tenor.com/view/yuju-cherry-bullet-kpop-cute-smile-gif-16634882",
            "https://tenor.com/view/yuju-cherry-bullet-kpop-cute-pretty-gif-17717763",
            "https://tenor.com/view/yuju-cherry-bullet-yuju-smile-heart-cute-gif-17717728",
            "https://tenor.com/view/cherry-bullet-yuju-yuju-cherry-bullet-gif-15959991",
            "https://tenor.com/view/cherry-bullet-yuju-cute-gif-15054827",
            "https://cdn.discordapp.com/attachments/805984467596345364/805990586841694268/image0.gif",
            "https://cdn.discordapp.com/attachments/805984467596345364/805990587903115294/image1.gif",
            "https://cdn.discordapp.com/attachments/805984467596345364/805990677476671518/image0.gif",
            "https://cdn.discordapp.com/attachments/805984467596345364/805990678357999691/image2.gif",
            "https://cdn.discordapp.com/attachments/805984467596345364/805990724868112384/image0.gif",
            "https://cdn.discordapp.com/attachments/805984467596345364/805990725380210719/image1.gif",
            "https://64.media.tumblr.com/ff5db8934d65967499f6a9b1e2eeac8b/3e8ae42d188a3377-05/s400x600/edc0f76e75a22d72a72a9042497d76174da1f8a3.gif",
            "https://64.media.tumblr.com/bb65b51e93dba1d0543e57faaa4d1c0c/3e8ae42d188a3377-fd/s400x600/3b6cb895fb5fc66b74f994d8f04a04ab0184d129.gif",
            "https://64.media.tumblr.com/95c8b28dca72ac6e4397980b03a3a1b0/dd68639adb58af99-c3/s400x600/3b42ab7a99da508c2891a26d306d4dc18c591869.gif",
            "https://64.media.tumblr.com/cc0bb951397a9b48552cc3bed712eb34/dd68639adb58af99-5c/s400x600/b0f45122dc54eaf186648f68cc30b79873ec7b9c.gif",
            "https://64.media.tumblr.com/8c45061c90bc9cd8e79ce827db9e5954/tumblr_pmq4uos8Sk1ui9xsvo2_400.gif",
            "https://64.media.tumblr.com/04a48210a3e41f0c191a71304d5bbb2a/tumblr_piyfwbwdbc1qg5nyao1_400.gif",
            "https://64.media.tumblr.com/1bf428c8ecb55b88d3b9dc5da6a3f71f/tumblr_plu79mIcRK1s2vcg0o3_400.gif",
            "https://64.media.tumblr.com/50b5779e3a986e1491e445561b1f45e9/tumblr_plu79mIcRK1s2vcg0o4_400.gif"]

    @commands.command(aliases = ['chebul'])
    async def cherry(self, ctx, *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Cherry Bullet {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "bora" or arg == "bullet bora":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Bora :heart:')
                await ctx.send(random.choice(self.bot.cherrybullet_bora_gif))
                await ctx.message.delete()
        elif arg == "chaerin" or arg == "bullet chaerin":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chaerin :heart:')
                await ctx.send(random.choice(self.bot.cherrybullet_chaerin_gif))
                await ctx.message.delete()
        elif arg == "haeyoon" or arg == "bullet haeyoon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Haeyoon :heart:')
                await ctx.send(random.choice(self.bot.cherrybullet_haeyoon_gif))
                await ctx.message.delete()
        elif arg == "jiwon" or arg == "bullet jiwon":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jiwon :heart:')
                await ctx.send(random.choice(self.bot.cherrybullet_jiwon_gif))
                await ctx.message.delete()
        elif arg == "kokoro" or arg == "bullet kokoro":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about kokoro :heart:')
                await ctx.send(random.choice(self.bot.cherrybullet_kokoro_gif))
                await ctx.message.delete()
        elif arg == "linlin" or arg == "bullet linlin":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Linlin :heart:')
                await ctx.send(random.choice(self.bot.cherrybullet_linlin_gif))
                await ctx.message.delete()
        elif arg == "may" or arg == "bullet may":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about May :heart:')
                await ctx.send(random.choice(self.bot.cherrybullet_may_gif))
                await ctx.message.delete()
        elif arg == "mirae" or arg == "bullet mirae":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Mirae :heart:')
                await ctx.send(random.choice(self.bot.cherrybullet_mirae_gif))
                await ctx.message.delete()
        elif arg == "remi" or arg == "bullet remi":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Remi :heart:')
                await ctx.send(random.choice(self.bot.cherrybullet_remi_gif))
                await ctx.message.delete()
        elif arg == "yuju" or arg == "bullet yuju":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Yuju :heart:')
                    await ctx.send(random.choice(self.bot.cherrybullet_yuju_gif))
                    await ctx.message.delete()

def setup(client):
    client.add_cog(CherryBullet(client))