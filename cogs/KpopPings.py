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
k8 = 573974040679809044
mae = 492769416610840586
kiwi = 390317665463566336
kate = 382715972722753536

class KpopPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
        self.bot.lucas_gif = ["https://tenor.com/view/lucas-wayv-heart-gif-14723401",
            "https://tenor.com/view/smile-handsome-cute-lucas-nct-gif-15246419",
            "https://tenor.com/view/nct-lucas-nct-lucas-cute-smile-gif-12612522",
            "https://tenor.com/view/nct-lucas-being-extra-hi-gif-14904496",
            "https://tenor.com/view/pout-kiss-handsome-cute-lucas-gif-15246420",
            "https://tenor.com/view/lucas-nct-way-v-gif-13770508",
            "https://tenor.com/view/wong-yukhei-lucas-nct-cute-kpop-gif-16350448",
            "https://tenor.com/view/lucas-nct-wayv-gif-19030351",
            "https://tenor.com/view/lucas-nct-smile-gif-19015832",
            "https://tenor.com/view/lucas-smile-cute-poke-cheek-gif-12719055",
            "https://tenor.com/view/lucas-nct-wong-yukhei-wayv-gif-14579895"]

        self.bot.nctmark_gif = ["https://tenor.com/view/mark-lee-nct-school-rapper-gif-9575546",
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
            "https://tenor.com/view/kpop-nct-mark-mark-lee-nct-gif-18031005",
            "https://tenor.com/view/mark-lee-serious-fierce-pose-nct-gif-13469194"]

        self.bot.nctwinwin_gif = ["https://tenor.com/view/winwin-nct-127-way-v-gif-13776784",
            "https://tenor.com/view/dong-siicheng-winwin-nct-wayv-cute-gif-14464703",
            "https://tenor.com/view/dong-sicheng-sicheng-dong-winwin-wayv-gif-14997192",
            "https://tenor.com/view/nct-127-winwin-gif-14168699",
            "https://tenor.com/view/nct-wayv-winwin-nct-wayv-teaser-gif-13760142",
            "https://tenor.com/view/winwin-dancing-winwin-flossing-winwin-hani3-gif-19452678",
            "https://tenor.com/view/winwin-wayv-sicheng-dongsicheng-gif-14098151",
            "https://tenor.com/view/winwin-nct-nct127-dong-si-cheng-dong-sa-sung-gif-17360118"]

        self.bot.nctjaemin_gif = ["https://cdn.discordapp.com/attachments/772975408912007180/790097070399815690/image0.jpg",
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

        self.bot.nctjaehyun_gif = ["https://tenor.com/view/jaehyun-kiss-nct-127-kpop-gif-15454039",
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

        self.bot.ses_mv = ["https://www.youtube.com/watch?v=WpmTLDtr4qY", #im your girl
            "https://www.youtube.com/watch?v=ZpJJIK1gK6I", #oh my love
            "https://www.youtube.com/watch?v=q_yyXw83rt8", #dreams come true 
            "https://www.youtube.com/watch?v=Z3UBcSRxjo0", #i love you
            "https://www.youtube.com/watch?v=1Cjt_2BsnCs", #shy boy
            "https://www.youtube.com/watch?v=T-KJZjHJYjo", #love
            "https://www.youtube.com/watch?v=A_x9_iK1nGA", #twilight zone
            "https://www.youtube.com/watch?v=T7imPmAQhfc", #show me your love
            "https://www.youtube.com/watch?v=geWN7mHXzv4", #be natural
            "https://www.youtube.com/watch?v=Izyclmg2Jp8", #just in love
            "https://www.youtube.com/watch?v=z1Px4wF9dMo", #U
            "https://www.youtube.com/watch?v=8XrnhhmTN9E", #just a feeling
            "https://www.youtube.com/watch?v=-gUU29UCQwQ", #S.II.S (Soul to Soul)
            "https://www.youtube.com/watch?v=M14nT1ZELfM", #love story
            "https://www.youtube.com/watch?v=Rr0kii_IYqU", #remember
            "https://www.youtube.com/watch?v=vAO_OcRz6xQ" #paradise
            ]

        self.bot.cl_gif = ["https://media.discordapp.net/attachments/771238115255255060/785288565273788426/image2.gif",
            "https://media.discordapp.net/attachments/771238115255255060/785288564912160819/image1.gif",
            "https://media.discordapp.net/attachments/771238115255255060/785288541785161758/image0.gif",
            "https://tenor.com/view/cl-hello-bitches-group-show-gif-14566826",
            "https://tenor.com/view/2ne1-cl-chaelin-chaerin-chaelin-lee-gif-7177115",
            "https://tenor.com/view/cl-kpop-performance-singer-gif-14566821",
            "https://tenor.com/view/cl-2ne1-rapper-korean-k-pop-gif-9210983",
            "https://tenor.com/view/2ne1-hello-kpop-hi-gif-14032003",
            "https://tenor.com/view/2ne1-chaelin-cl-chaelin-lee-mocking-gif-7177330"]

    
    #^lucas nct (wayv)
    @commands.command()
    async def lucas(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{kate}>, <@!{ctx.author.id}> is talking about Lucas :heart: ')
                await ctx.send(random.choice(self.bot.lucas_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Lucas :heart:')
            await ctx.send(random.choice(self.bot.lucas_gif))
            await ctx.message.delete()
    
    #^mark nct
    @commands.command()
    async def mark(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Mark :heart: ')
                await ctx.send(random.choice(self.bot.nctmark_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Mark :heart:')
            await ctx.send(random.choice(self.bot.nctmark_gif))
            await ctx.message.delete()

    #^winwin nct
    @commands.command()
    async def winwin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Winwin :heart: ')
                await ctx.send(random.choice(self.bot.nctwinwin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Winwin :heart:')
            await ctx.send(random.choice(self.bot.nctwinwin_gif))
            await ctx.message.delete()

    #^jaemin nct
    @commands.command()
    async def jaemin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Lucas :heart: ')
                await ctx.send(random.choice(self.bot.nctjaemin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jaemin :heart:')
            await ctx.send(random.choice(self.bot.nctjaemin_gif))
            await ctx.message.delete()

    #^jaehyun nct
    @commands.command()
    async def jaehyun(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jaehyun :heart: ')
                await ctx.send(random.choice(self.bot.nctjaehyun_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jaehyun :heart:')
            await ctx.send(random.choice(self.bot.nctjaehyun_gif))
            await ctx.message.delete()

    @commands.command(aliases = ['s.e.s'])
    async def ses(self, ctx):
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
            await ctx.message.delete()
        else:
            await ctx.send(f'''S.E.S was a three member group under SM Ent. that debuted in 1996 with the album I\'m Your Girl, and lead single with the same title, making them part of the first generation. They had a fairy concept, and won mulitple bonsangs due to their unique concept. S.E.S disbanded in 2002, only 5 years after debut. In 2016-2017, they briefly reunited for their 20th anniversary, releasing a song on SM Station (Love [Story]), which is a remake of their debut song "I'm Your Girl" and lead single from their third album, "Love", and their 7th Studio album, Remember - S.E.S 20th Anniversary Special.\n{random.choice(self.bot.ses_mv)}''')

    @commands.command()
    async def cl(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{k8}>, <@!{ctx.author.id}> is talking about CL :cherries: ')
                await ctx.send(random.choice(self.bot.cl_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about CL :cherries:')
            await ctx.send(random.choice(self.bot.cl_gif))
            await ctx.message.delete()

    

def setup(client):
    client.add_cog(KpopPings(client))