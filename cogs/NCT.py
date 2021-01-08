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
            "https://tenor.com/view/lucas-nct-gif-18844446"]

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
            "https://tenor.com/view/mark-lee-serious-fierce-pose-nct-gif-13469194"]

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
            "https://tenor.com/view/nct-wayv-dong-sicheng-winwin-chinese-rapper-gif-15797792"]

        self.bot.nct_jaemin_gif = ["https://cdn.discordapp.com/attachments/772975408912007180/790097070399815690/image0.jpg",
            "https://cdn.discordapp.com/attachments/772975408912007180/790097322155180043/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790097352589180968/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790097423921315840/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790097683116326912/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790097724523282432/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790097737801793537/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790097988662984734/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790098038285664306/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790098124474548234/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790101053294510090/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790101053399629834/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790101176627625984/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790101177252839454/image1.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790103352352178196/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790103993077596170/image1.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790104121116983346/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790104121600376842/image1.gif"]

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
            "https://cdn.discordapp.com/attachments/772975408912007180/790117484866174996/image1.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790117616676634645/image0.gif",
            "https://cdn.discordapp.com/attachments/772975408912007180/790117617339072512/image1.gif"]

        self.bot.nct_kun_gif = ["https://tenor.com/view/kun-wayv-nct-gif-19030306",
            "https://tenor.com/view/kun-kun-from-home-nct-from-home-mv-from-home-gif-18886755",
            "https://tenor.com/view/way-v-qian-kun-cute-nct-gif-14621591",
            "https://tenor.com/view/way-v-qian-kun-nct-kun-handsome-gif-15937670",
            "https://tenor.com/view/qian-kun-kun-qian-wayv-gif-18761255",
            "https://tenor.com/view/neo-culture-technology-nct-nctzen-kun-qian-kun-gif-12100534",
            "https://tenor.com/view/way-v-qian-kun-nct-kun-handsome-gif-15937667",
            "https://tenor.com/view/kun-wayv-nct-gif-19030350",
            "https://tenor.com/view/way-v-qian-kun-nct-kun-handsome-gif-15937652",
            "https://tenor.com/view/way-v-qian-kun-nct-kun-handsome-gif-15937660"]

        self.bot.nct_ten_gif = ["https://tenor.com/view/ten-nct-singing-nct-kpop-gif-14732794",
            "https://tenor.com/view/ten-nct-ten-nct-mark-lee-wayv-gif-14997188",
            "https://tenor.com/view/ten-chittaphon-leechaiyapornkul-nct-gif-18900846",
            "https://tenor.com/view/nct-chittaphon-ten-k-pop-gif-11577935",
            "https://tenor.com/view/tenalice-wayv-nct-ten-gif-19016713",
            "https://tenor.com/view/ten-dancing-nct-nctu-nct2018-gif-11536073",
            "https://tenor.com/view/ten-nct-way-v-finger-heart-cute-gif-14733893",
            "https://tenor.com/view/ten-nct-superm-wayv-wayv-ten-gif-19468090",
            "https://tenor.com/view/nct-kpop-ccg-chittaphon-leechaiyapornkul-ten-gif-14839951"]

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
            "https://tenor.com/view/xiaojun-assdaya-wayv-embarrassed-gif-19225097"]

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
            "https://tenor.com/view/hendery-wayv-nct-heart-gif-14723398"]

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
            "https://tenor.com/view/wayv-nct-liu-yangyang-yangyang-handsome-gif-16282250"]

        self.bot.nct_taeyong_gif = ["https://tenor.com/view/nct-taeyong-cute-gif-15119070",
            "https://tenor.com/view/nct-vocalist-visual-sm-entertainment-nct-subunit-gif-17505770",
            "https://tenor.com/view/nct-taeyong-sunscreen-nature-republic-gif-16980421",
            "https://tenor.com/view/nctu-nct-nct127-nctdream-taeyong-gif-9647830",
            "https://tenor.com/view/nct127-nct-kpop-ccg-shock-gif-16007114",
            "https://tenor.com/view/taeyong-nct-smiling-cute-gif-14544492",
            "https://tenor.com/view/taeyong-nct-nct127-nct-u-regular-gif-13569029"]

    @commands.command()
    async def nct(self, ctx, *, arg):
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


    @commands.command()
    async def lucas(self, ctx):
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
    
    @commands.command()
    async def mark(self, ctx):
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

    @commands.command()
    async def winwin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Winwin :heart: ')
                await ctx.send(random.choice(self.bot.nct_winwin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Winwin :heart:')
            await ctx.send(random.choice(self.bot.nct_winwin_gif))
            await ctx.message.delete()

    @commands.command()
    async def jaemin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jaemin :heart: ')
                await ctx.send(random.choice(self.bot.nct_jaemin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jaemin :heart:')
            await ctx.send(random.choice(self.bot.nct_jaemin_gif))
            await ctx.message.delete()

    @commands.command()
    async def jaehyun(self, ctx):
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