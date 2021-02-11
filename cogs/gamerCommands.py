import discord, random, os
from discord.ext import commands
from datetime import datetime

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.logs
logs = 786515662214397973
#.luminary bot-commands
kbotcom = 764610881513324574

#//people
muffin = 488423352206229505
gareth = 389897179701182465
mae = 492769416610840586
aster = 495714786823241728

class gamerPings(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.dream_gif = ["https://tenor.com/view/dream-george-not-found-sapnap-speedrunning-manhunt-gif-18187566",
            "https://tenor.com/view/minecraft-dream-gif-18394858",
            "https://tenor.com/view/popipo-dream-scrundy-pundy-technoblade-sapnap-gif-18226411",
            "https://tenor.com/view/dream-dreamwastaken-minecraft-desert-dance-gif-18987175",
            "https://tenor.com/view/dream-dreamwastaken-minecraft-gif-18176440",
            "https://tenor.com/view/dream-team-minecraft-love-dream-sapnap-gif-18710509"]

        self.food_gif = ["https://gfycat.com/uncomfortablesafebarbet",
            "https://tenor.com/view/jenniekim-gif-18818029",
            "https://tenor.com/view/tipton2109-nct-nct-mark-mark-lee-regular-gif-13173755",
            "https://tenor.com/view/sakura-miyawaki-sakura-izone-%E3%81%95%E3%81%8F%E3%82%89-%E5%AE%AE%E8%84%87%E5%92%B2%E8%89%AF-gif-14974458",
            "https://tenor.com/view/jisoo-food-blackpink-kpop-eating-gif-9473818",
            "https://tenor.com/view/hwasa-lollipop-kpop-be-calm-beautiful-day-gif-18873828",
            "https://tenor.com/view/lalisa-manoban-lisa-blackpink-lollipop-kpop-gif-17772815",
            "https://tenor.com/view/seulgi-kang-seulgi-red-velvet-cute-bear-gif-16728717",
            "https://tenor.com/view/wheein-mamamoo-eating-eggs-eating-egg-idol-gif-18928054",
            "https://tenor.com/view/mamamoo-hwasa-ahn-hye-jin-vocalist-rapper-gif-17583679",
            "https://tenor.com/view/hwasa-eat-eating-ramen-hot-gif-12261725",
            "https://tenor.com/view/mamamoo-solar-eating-pole-bibimbap-gif-16227163",
            "https://tenor.com/view/izone-hyewon-eating-gif-13780770",
            "https://tenor.com/view/chou-tzuyu-kpop-gif-11360919",
            "https://tenor.com/view/toosie-slide-cute-eat-jennie-jennie-kim-gif-16780128",
            "https://media.giphy.com/media/disxZ6CKe4b9wbFhhT/giphy.gif",
            "https://tenor.com/view/mamamoo-wheein-strawberry-yum-gif-7596438",
            "https://tenor.com/view/jo-yuri-yuri-iz-one-cute-eating-gif-14800422",
            "https://gfycat.com/miserableslipperygartersnake",
            "https://gfycat.com/aridpitifulchipmunk",
            "https://gfycat.com/zealousunsightlyhumpbackwhale",
            "https://gfycat.com/vaguefreshflickertailsquirrel",
            "https://tenor.com/view/mark-mark-lee-nct-cold-eating-gif-14683790",
            "https://gfycat.com/unconsciousweirdfishingcat",
            "https://tenor.com/view/yeeun-jang-clc-not-yummy-gif-13252749",
            "https://tenor.com/view/yum-delicious-cheng-xiao-yummy-gif-12031986",
            "https://gfycat.com/flamboyantunlinedisabellinewheatear",
            "https://gfycat.com/limpingunrulygrasshopper",
            "https://gfycat.com/sentimentalmadeupgrayfox",
            "https://cdn.discordapp.com/attachments/781312260118806529/781378241817608192/image3.gif",
            "https://tenor.com/view/soyeon-senorita-g-idle-cute-kpop-kpop-girl-group-gif-15338342",
            "https://tenor.com/view/shuhua-yeh-shuhua-shuhua-gidle-shuhua-idle-gidle-gif-19200395",
            "https://tenor.com/view/moonbyul-lunch-tang-hulu-cutie-mamamoo-gif-17053045",
            "https://tenor.com/view/hotel-del-luna-iu-eating-chew-bite-gif-17750091",
            "https://tenor.com/view/delicious-cant-stop-unstoppable-eating-again-gif-17375580",
            "https://tenor.com/view/solar-solarsido-mamamoo-eating-gif-14246383",
            "https://tenor.com/view/hitomi-honda-hitomi-%ED%9E%88%ED%86%A0%EB%AF%B8-%ED%98%BC%EB%8B%A4%ED%9E%88%ED%86%A0%EB%AF%B8-wow-gif-14017107",
            "https://tenor.com/view/nct-nct127-jaehyun-coffee-work-gif-12640382",
            "https://tenor.com/view/mamamoo-moonbyul-solar-moonsun-veggies-gif-7724635",
            "https://tenor.com/view/moonbyul-gif-7446949",
            "https://gfycat.com/longadmiredindianspinyloach",
            "https://tenor.com/view/hyojung-gif-19800693",
            "https://tenor.com/view/hyojung-gif-19857822",
            "https://tenor.com/view/oh-my-girl-omg-kpop-cute-pretty-gif-17578691",
            "https://gfycat.com/harmlesssecondappaloosa",
            "https://gfycat.com/evendismalamphibian",
            "https://tenor.com/view/chuu-loona-kim-jiwoo-loonatheworld-kpop-gif-gif-19449093",
            "https://tenor.com/view/wayv-nct-xiao-xiaojun-xiao-de-jun-gif-17708611",
            "https://tenor.com/view/jungkook-eating-jungkook-cute-jungkook-hot-jungkook-bts-jungkookie-gif-19814145",
            "https://cdn.discordapp.com/attachments/800224391258439721/800565546701160458/f1fc5f292c3132ff952b3b50e952698b.gif",
            "https://gfycat.com/soggyaccomplishedcolt-heejin-loona",
            "https://gfycat.com/agilefamiliariberianmidwifetoad",
            "https://gfycat.com/closefreshbantamrooster-yeojin-loona",
            "https://gfycat.com/admiredharshgrebe-yeojin-loona",
            "https://gfycat.com/blackshockingazurevasesponge-yeojin-loona",
            "https://gfycat.com/honoredcluelessleveret-yeojin-loona",
            "https://gfycat.com/faintcookedgreatwhiteshark-yeojin-loona",
            "https://gfycat.com/breakableequatorialcod-loona-yves-chuu",
            "https://gfycat.com/flusteredremarkablegnat-kim-lip",
            "https://gfycat.com/insecurepastanhinga-jinsoul-loona",
            "https://gfycat.com/helpfulwholedoctorfish-jinsoul-loona-chuu",
            "https://gfycat.com/handmadedisastrousdipper-loona-yves",
            "https://gfycat.com/flimsypiercingdugong",
            "https://gfycat.com/cavernousforcefulcicada-loona-gowon",
            "https://gfycat.com/delectableminiaturefurseal-gowon-loona",
            "https://gfycat.com/clutteredrewardingbackswimmer",
            "https://gfycat.com/breakabletotalkingbird-olivia-hye-choerry-jinsoul-loona",
            "https://gfycat.com/accomplisheduniformleafbird-loona-chuu",
            "https://gfycat.com/angelicsandybobolink-loona-chuu",
            "https://gfycat.com/backwhiteafricanparadiseflycatcher",
            "https://gfycat.com/fearlesspeskybrownbear",
            "https://gfycat.com/failingmammothatlasmoth-loona-chuu",
            "https://gfycat.com/impracticalpotablebunting-loona-chuu",
            "https://gfycat.com/colorlessgargantuandinosaur",
            "https://gfycat.com/harmfulperfumedhake-loona-chuu",
            "https://gfycat.com/ignorantsilverbumblebee-dating-class-loona-chuu",
            "https://cdn.discordapp.com/attachments/802261212846882826/802263665729863700/image0.gif",
            "https://cdn.discordapp.com/attachments/798320383539412992/806345491176620072/image0.gif",
            "https://gfycat.com/quarterlyinexperiencedanura",
            "https://64.media.tumblr.com/3629e5aed89ff2a1aa94a51a9ac0396d/ba269b895e46fb77-2d/s400x600/766afd4caedc073d6001eb909116fe2c0fea4c4d.gif",
            "https://gfycat.com/tartpastellangur"]

        self.monke = ["https://www.youtube.com/watch?v=PipzizkF-SY",
            "https://www.youtube.com/watch?v=-JUhUI_KvUI",
            "https://www.youtube.com/watch?v=05sJVEwZuZ4",
            "https://www.youtube.com/watch?v=2EKKMof_Ywg",
            "https://www.youtube.com/watch?time_continue=5&v=-a57_IOKpjM&feature=emb_logo"]

        self.tuna_wrong = ["Tina",
            "Yuna",
            "Putuna"]

    @commands.command()
    async def dreammc(self, ctx):
        if ctx.guild.id == jst:
            await ctx.send(f'<@150742733743587328>, <@!{ctx.author.id}> is talking about Dream :cactus:')
            await ctx.send(random.choice(self.dream_gif))
            await ctx.message.delete()

    @commands.command()
    async def food(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [food] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
            await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to #bot-commands', delete_after=2)
        else:
            # await ctx.send(f'Aster is the best :smiling_face_with_3_hearts:')
            await ctx.send(random.choice(self.food_gif))

    @commands.command()
    async def screm(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [screm] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send('https://tenor.com/view/loona-loona-hyunjin-hyunjin-kim-hyunjin-loona-aeong-gif-18902504')
        await ctx.message.delete()

    @commands.command()
    async def rahul(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [rahul] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'<@579636764889841665> monke ' + random.choice(self.monke))
        await ctx.message.delete()

    @commands.command()
    async def weakado(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [weakado] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'<@259409277482041344> fiesta good \nhttps://www.youtube.com/watch?v=eDEFolvLn0A')
        await ctx.message.delete()

    @commands.command()
    async def veery(self,ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [veery] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'https://cdn.discordapp.com/attachments/735713250989309984/779101391871934484/veery_good.mp3')
        await ctx.message.delete()

    @commands.command()
    async def sex(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [sex] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if ctx.guild.id == jst:
            await ctx. send(f'https://www.youtube.com/watch?v=VfCYZ3pks48&list=FLFkJiNcjfwfDWZMEHJ1C_Ew&index=522')
            await ctx.message.delete()

    @commands.command()
    async def ren(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [ren] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'I love you <@749085760354910280>')

    @commands.command()
    async def muffin(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [muffin] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'<@!{ctx.author.id}> :heart: you <@488423352206229505>')

    @commands.command()
    async def aster(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Aster] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'<@{ctx.author.id}> :heart: you <@{aster}>!')

    @commands.command()
    async def god(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [G O D] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'<@!{ctx.author.id}> says stop being sus <@573974040679809044>')

    @commands.command()
    async def tuna(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Tuna] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'*{random.choice(self.tuna_wrong)}')

    @commands.command()
    async def llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if ctx.author.id == muffin or ctx.author.id == gareth or ctx.author.id == mae:            
            embed=discord.Embed(
                    title = 'llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch',
                    description = '🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿🏴󠁧󠁢󠁷󠁬󠁳󠁿',
                    colour = discord.Color.from_rgb(0,173,54))
            embed.set_footer(text="What happened on the fishing trip?")
            embed.add_field(name='Llanymawddwy:', value=f'```\nFfion\nFfion\nFfion\nFfion\nFfion\nFfion```', inline=True)
            embed.add_field(name='Llanrhychwyn:', value=f'```\nFfion\nFfion\nFfion\nFfion\nFfion\nFfion```', inline=True)
            embed.add_field(name='Llanbrynmair:', value=f'```\nFfion\nFfion\nFfion\nFfion\nFfion\nFfion```', inline=True)
            embed.add_field(name='Pontrhydfendigaid:', value=f'```\nFfion\nFfion\nFfion\nFfion\nFfion\nFfion```', inline=True)
            embed.add_field(name='Pontnewynydd:', value=f'```\nFfion\nFfion\nFfion\nFfion\nFfion\nFfion```', inline=True)
            embed.add_field(name='Pontrhydygroes:', value=f'```\nFfion\nFfion\nFfion\nFfion\nFfion\nFfion```', inline=True)
            await ctx.send(embed=embed)
            await ctx.message.delete()

    @commands.command()
    async def caillou(self, ctx):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Caillou] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        await ctx.send(f'Hey, {ctx.author.name} are you a short little bald white boy on a television kids show?\nBecause youre Caillou-te')
        await ctx.message.delete()

    @commands.command()
    async def pickupline(self, ctx, *, name=f'Bae Suzy Is the Best'):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Pickupline] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if name == "Bae Suzy Is the Best":
            person = ctx.author.name
        else:
            person = name
        number = random.randint(1,5)
        if number == 1:
            await ctx.send(f'Hey, {person} are you a short little bald white boy on a television kids show?\nBecause youre Caillou-te')
        elif number == 2:
            await ctx.send(f'If you are the us police can I be systematic racism?\nBecause I think we\'d be naturally together')
        elif number == 3:
            await ctx.send(f'Hey, {person}, are you Bae Suzy?\nBecause you could literally punch me and I\'d be thankful')
        elif number == 4:
            await ctx.send(f'Hey, {person},  are you hawaiin bread rolls?\nBecause I love your buns')
        elif number == 5:
            await ctx.send(f'Hey, {person}, are you Jo Yuri?\nBecause, Jo, Yuri-lly pretty')
        else:
            await ctx.send(f'{person}, please report this to @muffin521#9280, or in the support server: https://discord.gg/Ntk9Jp26yx')

        
def setup(client):
    client.add_cog(gamerPings(client))