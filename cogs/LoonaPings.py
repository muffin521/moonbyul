import discord, random
from discord.ext import commands

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

#//people
mae = 492769416610840586
aeong = 542342961392779264
k8 = 573974040679809044
stanley = 727312020717830264
rith = 346724857725059075
ple = 416903886968979466
masa = 725138411823956079
manman = 320520067265724416


class LoonaPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        #10
        self.bot.heejin_gif = ["https://tenor.com/view/%EC%9D%B4%EB%8B%AC%EC%9D%98%EC%86%8C%EB%85%80-%ED%9D%AC%EC%A7%84-loona-heejin-dancing-gif-15500748",
            "https://tenor.com/view/heejin-waving-hi-hello-smile-gif-16980677",
            "https://tenor.com/view/heejin-loona-gif-18855977",
            "https://tenor.com/view/heejin-loona-gif-18630598",
            "https://tenor.com/view/heejin-loona-gif-18892027",
            "https://tenor.com/view/loona-hee-jin-hello-smile-gif-14824756",
            "https://tenor.com/view/loona-heejin-cute-gif-8365491",
            "https://tenor.com/view/heejin-loona-nodding-sad-nodding-yeah-gif-16288849",
            "https://tenor.com/view/heejin-loona-gif-18855987",
            "https://tenor.com/view/heejin-loona-gif-18855973"]

        #16
        self.bot.hyunjin_gif = ["https://cdn.discordapp.com/attachments/771238115255255060/771239029291221022/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239029982101534/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239030301786132/image2.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239030984933376/image3.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239031534649344/image4.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239032360271872/image5.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771239033023496202/image6.gif",
            "https://tenor.com/view/hyunjin-hyunjin-cute-loona-hyunjin-loona-kpop-girl-gif-15567551",
            "https://cdn.discordapp.com/attachments/771238115255255060/771478311045955584/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771478314715447316/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/771478316427378748/image2.gif",
            "https://tenor.com/view/k-im-hyunjin-loona-got-you-cute-pretty-gif-16467662",
            "https://tenor.com/view/loona-loona-hyunjin-hyunjin-kim-hyunjin-loona-aeong-gif-18902504",
            "https://cdn.discordapp.com/attachments/771238115255255060/777819042685779978/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/777819043649683476/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/777819045034065920/image2.gif"]

        #11
        self.bot.haseul_gif = ["https://tenor.com/view/wiggle-kpop-haseul-ha-seul-gif-19167036",
            "https://tenor.com/view/ha-seul-highway-to-heaven-loona-cute-smile-gif-14669447",
            "https://tenor.com/view/haseul-loona-butterfly-dancing-kpop-gif-15567623",
            "https://tenor.com/view/let-me-in-haseul-loona-jo-haseul-music-video-gif-16481945",
            "https://tenor.com/view/hug-loona-kpop-love-haseul-gif-18585614",
            "https://tenor.com/view/ha-seul-laugh-loona-cute-gif-14669547",
            "https://tenor.com/view/loona-haseul-kpop-korean-you-gif-13811504",
            "https://tenor.com/view/haseul-loona-haseul-cute-haseul-kiss-blow-kiss-gif-15567594",
            "https://tenor.com/view/haseul-haseul-nope-yoghurt-loona-haseul-loona-gif-19296137",
            "https://tenor.com/view/loona-haseul-yes-nod-gif-15405788",
            "https://tenor.com/view/loona-haseul-kpop-gif-13775182"]

        #13
        self.bot.vivi_gif = ["https://tenor.com/view/vivi-loona-gif-19076955",
            "https://tenor.com/view/vivi-loona-gif-19186243",
            "https://tenor.com/view/loona-vivi-cute-wong-kaahei-kpop-gif-17900498",
            "https://tenor.com/view/loona-vivi-gif-18868377",
            "https://tenor.com/view/loona-vivi-wong-gaahei-vocalist-rapper-gif-17025562",
            "https://tenor.com/view/loona-vivi-wong-gaahei-vocalist-rapper-gif-17025571",
            "https://tenor.com/view/vivi-loona-sad-gif-15189378",
            "https://tenor.com/view/loona-vivi-wong-gaahei-vocalist-rapper-gif-17025543",
            "https://tenor.com/view/vivi-loona-so-what-kpop-fierce-gif-16237781",
            "https://tenor.com/view/vivi-loona-disgust-gif-15189377",
            "https://tenor.com/view/kpop-loona-vivi-gif-18586099",
            "https://tenor.com/view/kpop-loona-vivi-shoulder-wiggle-gif-18586104",
            "https://media.discordapp.net/attachments/743512478411128834/778910394126565376/vivi_peekaboo.gif"]

        #13
        self.bot.yeojin_gif = ["https://tenor.com/view/yeojin-loona-star-gif-19239212",
            "https://tenor.com/view/glasses-loona-yeojin-cute-gif-14375086",
            "https://tenor.com/view/yeojin-loona-im-yeojin-gun-aim-gif-16706146",
            "https://tenor.com/view/kiss-later-loona-yeojin-im-yeojin-maknae-gif-17090973",
            "https://tenor.com/view/yeojin-loona-yeojin-loona-gif-18910341",
            "https://tenor.com/view/yeojin-loona-yeojin-loona-gif-18972277",
            "https://tenor.com/view/yeojin-loona-yeojin-loona-finger-guns-gif-19210631",
            "https://tenor.com/view/yeojin-loona-gif-11903465",
            "https://tenor.com/view/loona-yeojin-im-yeojin-maknae-vocalist-gif-16635624",
            "https://tenor.com/view/yeojin-cute-loona-frog-finger-guns-gif-14374690",
            "https://tenor.com/view/yeojin-wiggle-kpop-loona-dance-gif-17207445",
            "https://tenor.com/view/loona-dancing-yeojin-kpop-gif-18890861",
            "https://tenor.com/view/yeojin-loona-cute-yes-surprised-gif-14381686",
            "https://tenor.com/view/loona-dancing-yeojin-kpop-gif-18890861"]

        #13
        self.bot.kimlip_gif = ["https://thumbs.gfycat.com/CaringAlertHellbender-max-1mb.gif",
            "https://64.media.tumblr.com/632b50fcf95204b79d978049034e2f9f/tumblr_pe89snEig71x29wuzo4_250.gif",
            "https://i.pinimg.com/originals/b8/22/88/b82288fdc234bd0a50be07ae1ec212ef.gif",
            "https://thumbs.gfycat.com/WeeSillyAngelfish-max-1mb.gif",
            "https://media1.tenor.com/images/8cdb11b9b4a58c517215531156cc1812/tenor.gif?itemid=13802828",
            "https://i2.wp.com/66.media.tumblr.com/935a3a56a302380eeb10be67640a880a/b3f428ad85343842-de/s400x600/b31d01f30df1a8ac781460c8460f697e87c2e57d.gif?w=817&ssl=1",
            "https://64.media.tumblr.com/496da05c77ed58eac63f37cdd4bc7e9b/abfaa74408006212-71/s400x600/df7abdfe16b17d71598cab49b1202362b5ca4e61.gif",
            "https://i.pinimg.com/originals/15/41/f8/1541f83313271d2e8eb76220cbf43f24.gif",
            "https://data.whicdn.com/images/290426395/original.gif",
            "https://64.media.tumblr.com/151136f17e11dd8f80fe626d7fe685e4/tumblr_pdue0gd2P81somnmfo2_400.gif",
            "https://i.pinimg.com/originals/b6/26/68/b62668ab9b50797aa7418e16074de809.gif",
            "https://64.media.tumblr.com/0072acb65c1a86773f842628f748faaa/tumblr_pul162PtSc1xpl3u9o1_r1_250.gif",
            "https://64.media.tumblr.com/40ad336b08f95aa5490afeedf10df5c6/tumblr_p92066rl3z1w5jkuno5_r1_500.gif"]

        #14
        self.bot.jinsoul_gif = ["https://tenor.com/view/jinsoul-loona-whynot-gif-18990936",
            "https://tenor.com/view/loona-whynot-jinsoul-gif-19093071",
            "https://tenor.com/view/jinsoul-loona-gif-11882928",
            "https://tenor.com/view/jinsoul-loona-gif-11882987",
            "https://tenor.com/view/jinsoul-loona-sad-gif-11882910",
            "https://tenor.com/view/loona-jinsoul-hello-waving-gif-14339470",
            "https://tenor.com/view/loona-jinsoul-kpop-peace-sign-cute-gif-15163631",
            "https://tenor.com/view/jinsoul-kpop-korean-cute-loona-gif-16438129",
            "https://tenor.com/view/jinsoul-loonatic-jinsoul-loona-gif-18816324",
            "https://tenor.com/view/jinsoul-loona-loona-jinsoul-singing-in-the-rain-singing-gif-11527427",
            "https://tenor.com/view/jin-soul-loona-cute-kpop-smile-gif-15164534",
            "https://tenor.com/view/jinsoul-gif-18689085",
            "https://tenor.com/view/jinsoulloona-gif-18870191",
            "https://tenor.com/view/jinsoul-gif-18689119"]

        #7
        self.bot.choerry_gif = ["https://tenor.com/view/choerry-loona-gif-18740424",
            "https://tenor.com/view/loona-choerry-kpop-cute-wave-gif-16635613",
            "https://tenor.com/view/choi-yerim-choerry-kpop-paper-loona-gif-17213985",
            "https://cdn.discordapp.com/attachments/747275528993636424/775111507486310450/4ab7d195-ce65-423a-a177-cb1f6a6a7648.gif",
            "https://media.discordapp.net/attachments/704248706269970488/775111463579942952/image0.gif",
            "https://cdn.discordapp.com/attachments/747275528993636424/775112055244980264/2010061.gif",
            "https://cdn.discordapp.com/attachments/747275528993636424/775112225965867048/2002192.gif"]
        
        #12
        self.bot.yves_gif = ["https://tenor.com/view/yves-loona-fainting-jail-kpop-gif-18490526",
            "https://tenor.com/view/loona-whynot-yves-gif-18911743",
            "https://tenor.com/view/loona-yves-gif-19104615",
            "https://tenor.com/view/yves-loona-gif-19166650",
            "https://tenor.com/view/yves-loona-gif-19166651",
            "https://tenor.com/view/yves-loona-satellite-shy-yves-shy-gif-18451495",
            "https://tenor.com/view/yves-swan-so-what-gif-19050405",
            "https://tenor.com/view/yves-loona-finger-heart-love-gif-15189376",
            "https://tenor.com/view/yves-loona-nods-gif-11903464",
            "https://tenor.com/view/whynot-loona-yves-gif-19007216",
            "https://tenor.com/view/loona-yves-love-gif-14534865",
            "https://tenor.com/view/yves-loona-come-here-come-with-me-gif-16467667"]

        #17
        self.bot.chuu_gif = ["https://tenor.com/view/chuu-loona-jiwoo-loona-chuu-heart-attack-gif-19200978",
            "https://tenor.com/view/fome-eat-hungry-snow-girl-gif-17723791",
            "https://tenor.com/view/chuu-heart-attack-arrow-gif-15516607",
            "https://tenor.com/view/chuu-chuu-heart-loona-loona-heart-kpop-girl-gif-15567590",
            "https://tenor.com/view/chuu-gif-18868429",
            "https://tenor.com/view/ooh-loona-fancy-chuu-kpop-gif-17090975",
            "https://tenor.com/view/chuu-chuu-loona-chuu-woah-woah-loona-gif-19236767",
            "https://tenor.com/view/kpop-loona-chuu-hi-happy-gif-18586089",
            "https://tenor.com/view/chuu-gif-18979392",
            "https://tenor.com/view/chuu-fire-chuu-fire-chaos-kpop-gif-17946860",
            "https://tenor.com/view/loona-kpop-korean-chuu-loona-chu-gif-12852146",
            "https://tenor.com/view/loona-chuu-happy-smile-aegyo-gif-16082308",
            "https://tenor.com/view/chuu-loonachuu-loona-stan-thumbs-up-gif-12784143",
            "https://tenor.com/view/chuu-loona-gif-18055139",
            "https://tenor.com/view/chuu-loona-hamburguer-heart-heart-untitled127-gif-13827374",
            "https://tenor.com/view/loona-chuu-yes-happy-smile-gif-14322751",
            "https://tenor.com/view/chuu-loona-ne-yes-cute-gif-14954652",
            "https://tenor.com/view/chuu-gif-18979395"]

        #13
        self.bot.gowon_gif = ["https://tenor.com/view/gowon-park-gowon-park-chaewon-loona-loona-gowon-gif-13191168",
            "https://tenor.com/view/loona-go-won-kpop-gif-14252120",
            "https://tenor.com/view/gowon-loona-gif-11903470",
            "https://tenor.com/view/loona-gowon-gif-18868391",
            "https://tenor.com/view/gowon-park-gowon-park-chaewon-loona-loona-gowon-gif-13184441",
            "https://tenor.com/view/gowon-flying-kiss-muah-red-lips-gif-13731778",
            "https://tenor.com/view/loona-gowon-kpop-gif-18738916",
            "https://tenor.com/view/loona-kpop-gowon-spoon-gif-18585817",
            "https://tenor.com/view/loona-kpop-gowon-cheek-squish-gif-18585812",
            "https://tenor.com/view/loona-gowon-dance-gif-12433093",
            "https://tenor.com/view/loona-gowon-gowon-loona-kpop-gif-18739724",
            "https://tenor.com/view/gowon-loona-gif-19126206",
            "https://tenor.com/view/loona-gowon-yawning-kpop-gif-18890935"]

        #13
        self.bot.oliviahye_gif = ["https://tenor.com/view/loona-olivia-hye-hyejoo-cute-beautiful-gif-16689725",
            "https://tenor.com/view/loona-olivia-hye-son-hyejoo-bunny-ears-bunny-gif-16778977",
            "https://tenor.com/view/olivia-hye-hyejoo-olivia-hey-loona-loona-olivia-hye-gif-16808778",
            "https://tenor.com/view/loona-olivia-hye-son-hyejoo-dancer-vocalist-gif-17147871",
            "https://tenor.com/view/kim-hyejoo-attempt-cute-olivia-fail-gif-17193603",
            "https://tenor.com/view/olivia-hye-hyejoo-loona-rae-butterfly-gif-18963804",
            "https://tenor.com/view/loona-olivia-hye-son-hyejoo-dancer-vocalist-gif-17696702",
            "https://tenor.com/view/olivia-hye-hyejoo-smile-pretty-cute-gif-15567631",
            "https://tenor.com/view/olivia-hye-son-hyejoo-loona-yyxy-puff-cheeks-gif-15633712",
            "https://tenor.com/view/olivia-hye-hyejoo-full-moon-loona-dancing-gif-15567587",
            "https://tenor.com/view/oliviahye-loona-olivia-loona-olivia-hyejoo-hyejoo-gif-16474426",
            "https://tenor.com/view/aliphobe-olivia-hye-loona-yyxy-hyejoo-gif-17860838",
            "https://tenor.com/view/oliviahye-gif-18868773"]

        #idk man
        self.bot.chuuheart_gif = ["https://static.apester.com/user-images/cb/cb60802a9e5ff8aa501df36ddfa56cce.gif",
            "https://tenor.com/view/mamamoo-wheein-heart-kpop-dance-gif-16331749",
            "https://tenor.com/view/kpop-loona-chuu-heart-love-gif-18586088",
            "https://tenor.com/view/chuu-loona-hamburguer-heart-heart-untitled127-gif-13827374",
            "https://tenor.com/view/chuu-loona-chuu-loona-cute-kpop-gif-16242378",
            "https://media.discordapp.net/attachments/758500230386679848/775129870559870976/ezgif-7-864231320452.gif",
            "https://tenor.com/view/seulgi-kang-seulgi-red-velvet-cute-pretty-gif-16937522",
            "https://tenor.com/view/wendy-shon-son-seungwan-red-velvet-%ec%9b%ac%eb%94%94-%eb%a0%88%eb%93%9c%eb%b2%a8%eb%b2%b3-gif-16069063",
            "https://tenor.com/view/yoona-im-yoona-%ec%9c%a4%ec%95%84-snsd-girls-generation-gif-14170845",
            "https://tenor.com/view/heart-love-apple-heart-chuu-heart-da-vinki-gif-18549840",
            "https://tenor.com/view/sakura-izone-sakura-miyawaki-sakura-saku-chan-chaekura-kkura-gif-13532539",
            "https://cdn.discordapp.com/attachments/704248706269970488/776652835617898516/image0.gif",
            "https://tenor.com/view/yeeun-jang-yeeun-cute-clc-kpop-gif-17883335",
            "https://tenor.com/view/g-idle-yuqi-song-yuqi-kpop-cute-gif-17667093",
            "https://tenor.com/view/chuu-gif-18979395"]

    @commands.command()
    async def loona(self, ctx, *, arg):
        if arg == "heejin":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{mae}>, <@{aeong}>, <@!{ctx.author.id}> is talking about Heejin :rabbit:')
                    await ctx.send(random.choice(self.bot.heejin_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Heejin :rabbit:')
                await ctx.send(random.choice(self.bot.heejin_gif))
                await ctx.message.delete()
        elif arg == "hyunjin":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{k8}>, <@{aeong}>, <@!{ctx.author.id}> is talking about Hyunjin :cat::bread:')
                    await ctx.send(random.choice(self.bot.hyunjin_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Hyunjin :cat::bread:')
                await ctx.send(random.choice(self.bot.hyunjin_gif))
                await ctx.message.delete()
        elif arg == "haseul":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Haseul :dove::green_heart:')
                    await ctx.send(random.choice(self.bot.haseul_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Haseul :dove::green_heart:')
                await ctx.send(random.choice(self.bot.haseul_gif))
                await ctx.message.delete()
        elif arg == "vivi":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{manman}>, <@{ctx.author.id}> is talking about ViVi :deer:')
                    await ctx.send(random.choice(self.bot.vivi_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about ViVi :deer:')
                await ctx.send(random.choice(self.bot.vivi_gif))
                await ctx.message.delete()
        elif arg == "yeojin":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Yeojin :frog::orange_heart:')
                    await ctx.send(random.choice(self.bot.yeojin_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Yeojin :frog::orange_heart:')
                await ctx.send(random.choice(self.bot.yeojin_gif))
                await ctx.message.delete()
        elif arg == "kim lip":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{stanley}>, <@!{ctx.author.id}> is talking about Kim Lip :owl:')
                    await ctx.send(random.choice(self.bot.kimlip_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=6)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Kim Lip :owl:')
                await ctx.send(random.choice(self.bot.kimlip_gif))
                await ctx.message.delete()
        elif arg == "jinsoul":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{ctx.author.id}> is talking about Jinsoul :fish:')
                    await ctx.send(random.choice(self.bot.jinsoul_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
            else:
                await ctx.send(f'<@{ctx.author.id}> is talking about Jinsoul :fish:')
                await ctx.send(random.choice(self.bot.jinsoul_gif))
                await ctx.message.delete()
        elif arg == "choerry":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{rith}>, <@{ple}>, <@!{ctx.author.id}> is talking about Choerry :bat:')
                    await ctx.send(random.choice(self.bot.choerry_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()            
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Choerry :bat:')
                await ctx.send(random.choice(self.bot.choerry_gif))
                await ctx.message.delete()
        elif arg == "yves":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Yves :swan::apple:')
                    await ctx.send(random.choice(self.bot.yves_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()            
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yves :swan::apple:')
                await ctx.send(random.choice(self.bot.yves_gif))
                await ctx.message.delete()
        elif arg == "chuu":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Chuu :penguin::strawberry:')
                    await ctx.send(random.choice(self.bot.chuu_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()            
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chuu :penguin::strawberry:')
                await ctx.send(random.choice(self.bot.chuu_gif))
                await ctx.message.delete()
        elif arg == "go won" or arg == "gowon":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@{rith}>, <@{masa}>, <@!{ctx.author.id}> is talking about Go Won :butterfly::pineapple:')
                    await ctx.send(random.choice(self.bot.gowon_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()            
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Go Won :butterfly::pineapple:')
                await ctx.send(random.choice(self.bot.gowon_gif))
                await ctx.message.delete()
        elif arg == "oliva hye":
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Olivia Hye :wolf:')
                    await ctx.send(random.choice(self.bot.oliviahye_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()            
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Olivia Hye :wolf:')
                await ctx.send(random.choice(self.bot.oliviahye_gif))
                await ctx.message.delete()



#.1/3
    @commands.command()
    async def heejin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{mae}>, <@{aeong}>, <@!{ctx.author.id}> is talking about Heejin :rabbit:')
                await ctx.send(random.choice(self.bot.heejin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Heejin :rabbit:')
            await ctx.send(random.choice(self.bot.heejin_gif))
            await ctx.message.delete()

    @commands.command()
    async def hyunjin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{k8}>, <@{aeong}>, <@!{ctx.author.id}> is talking about Hyunjin :cat::bread:')
                await ctx.send(random.choice(self.bot.hyunjin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Hyunjin :cat::bread:')
            await ctx.send(random.choice(self.bot.hyunjin_gif))
            await ctx.message.delete()

    @commands.command()
    async def haseul(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{ctx.author.id}> is talking about Haseul :dove::green_heart:')
                await ctx.send(random.choice(self.bot.haseul_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@{ctx.author.id}> is talking about Haseul :dove::green_heart:')
            await ctx.send(random.choice(self.bot.haseul_gif))
            await ctx.message.delete()

    @commands.command()
    async def vivi(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{manman}>, <@{ctx.author.id}> is talking about ViVi :deer:')
                await ctx.send(random.choice(self.bot.vivi_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@{ctx.author.id}> is talking about ViVi :deer:')
            await ctx.send(random.choice(self.bot.vivi_gif))
            await ctx.message.delete()

    @commands.command()
    async def yeojin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{ctx.author.id}> is talking about Yeojin :frog::orange_heart:')
                await ctx.send(random.choice(self.bot.yeojin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@{ctx.author.id}> is talking about Yeojin :frog::orange_heart:')
            await ctx.send(random.choice(self.bot.yeojin_gif))
            await ctx.message.delete()


#.oec
    @commands.command(aliases=['kim', 'lip', 'lippington', 'kimlip'])
    async def lippie(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{stanley}>, <@!{ctx.author.id}> is talking about Kim Lip :owl:')
                await ctx.send(random.choice(self.bot.kimlip_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=6)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Kim Lip :owl:')
            await ctx.send(random.choice(self.bot.kimlip_gif))
            await ctx.message.delete()

    @commands.command()
    async def jinsoul(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{ctx.author.id}> is talking about Jinsoul :fish:')
                await ctx.send(random.choice(self.bot.jinsoul_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@{ctx.author.id}> is talking about Jinsoul :fish:')
            await ctx.send(random.choice(self.bot.jinsoul_gif))
            await ctx.message.delete()

    @commands.command()
    async def choerry(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{rith}>, <@{ple}>, <@!{ctx.author.id}> is talking about Choerry :bat:')
                await ctx.send(random.choice(self.bot.choerry_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()            
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Choerry :bat:')
            await ctx.send(random.choice(self.bot.choerry_gif))
            await ctx.message.delete()


#.yyxy
    @commands.command()
    async def yves(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yves :swan::apple:')
                await ctx.send(random.choice(self.bot.yves_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()            
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yves :swan::apple:')
            await ctx.send(random.choice(self.bot.yves_gif))
            await ctx.message.delete()

    @commands.command()
    async def chuu(self, ctx, heart="no"):
        if heart == "heart":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to #bot-commands', delete_after=2)
            else:
                await ctx.send(f'nyam')
                await ctx.send(random.choice(self.bot.chuuheart_gif))
        else:
            if ctx.guild.id == luminary:
                if ctx.channel.id == kbotcom:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Chuu :penguin::strawberry:')
                    await ctx.send(random.choice(self.bot.chuu_gif))
                    await ctx.message.delete()
                else:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()            
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chuu :penguin::strawberry:')
                await ctx.send(random.choice(self.bot.chuu_gif))
                await ctx.message.delete()

    @commands.command()
    async def gowon(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{rith}>, <@{masa}>, <@!{ctx.author.id}> is talking about Go Won :butterfly::pineapple:')
                await ctx.send(random.choice(self.bot.gowon_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()            
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Go Won :butterfly::pineapple:')
            await ctx.send(random.choice(self.bot.gowon_gif))
            await ctx.message.delete()

    @commands.command(aliases = ['hyejoo', 'hye', 'olivia'])
    async def oliviahye(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Olivia Hye :wolf:')
                await ctx.send(random.choice(self.bot.oliviahye_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()            
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Olivia Hye :wolf:')
            await ctx.send(random.choice(self.bot.oliviahye_gif))
            await ctx.message.delete()
    
#
def setup(client):
    client.add_cog(LoonaPings(client))