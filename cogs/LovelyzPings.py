import discord, random
from discord.ext import commands
from discord.utils import get

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

class gamerPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.yein_gif = ["https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-yein-%EC%98%88%EC%9D%B8-gif-18419239",
            "https://tenor.com/view/lovelyz-yein-%EC%98%88%EC%9D%B8-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kpop-gif-16459793",
            "https://tenor.com/view/lovelyz-kpop-yein-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EC%98%88%EC%9D%B8-gif-18588376",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-yein-%EC%98%88%EC%9D%B8-gif-18213767",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-yein-%EC%98%88%EC%9D%B8-gif-18213757",
            "https://tenor.com/view/lovelyz-kpop-yein-eat-it-gif-16074106",
            "https://tenor.com/view/lovelyz-kpop-kei-mijoo-yein-gif-18565694",
            "https://tenor.com/view/yein-blow-a-bubble-bubble-gum-gum-lovelyz-gif-11607390",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-yein-kpop-%EC%98%88%EC%9D%B8-gif-16459879",
            "https://tenor.com/view/lovelyz-lvlz-jung-yein-yein-gorani-gif-16341215",
            "https://tenor.com/view/yein-lovelyz-kpop-girlgroup-fight-gif-18292941",
            "https://media.discordapp.net/attachments/170383062633283584/755514607308636260/ecd790977d987c6bc0db74a80ca893fb.gif",
            "https://gfycat.com/quarterlymerrydingo",
            "https://gfycat.com/oldfashionedspiritedbluefish",
            "https://gfycat.com/uncomfortablesafebarbet",
            "https://tenor.com/view/yein-lovelyz-oblivate-gif-18541914",
            "https://tenor.com/view/yein-lovelyz-oblivate-gif-18541915",
            "https://gfycat.com/sparserawdiplodocus",
            "https://gfycat.com/lavishteemingalligatorgar",
            "https://tenor.com/view/%EC%A0%95%EC%98%88%EC%9D%B8-gif-18273271"]

        self.bot.kei_gif = ["https://tenor.com/view/lovelyz-kpop-kei-heart-%eb%9f%ac%eb%b8%94%eb%a6%ac%ec%a6%88-gif-18565559",
            "https://tenor.com/view/obliviate-lovelyz-lovelyzkei-kimjiyeon-kei-gif-18226419",
            "https://media.discordapp.net/attachments/448355257383387138/738587515237302312/254A623658B808590C.gif",
            "https://media.discordapp.net/attachments/448355257383387138/738587871904137266/99998A3F5C5A9C4553.gif",
            "https://tenor.com/view/lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kei-%EC%BC%80%EC%9D%B4-gif-16303444",
            "https://tenor.com/view/lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kei-%EC%BC%80%EC%9D%B4-gif-16303756",
            "https://tenor.com/view/kei-kpop-i-go-lovelyz-over-and-over-gif-15309714",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kpop-lovelyz-%EC%BC%80%EC%9D%B4-kei-gif-18182587",
            "https://tenor.com/view/kpop-lovelyz-kei-i-go-lovelinus-gif-15336273",
            "https://tenor.com/view/kpop-korean-lovelyz-kei-gif-10760158",
            "https://tenor.com/view/lovelyz-kei-delicous-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-16496984",
            "https://tenor.com/view/lovelyz-kei-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EC%BC%80%EC%9D%B4-kpop-gif-16516714",
            "https://tenor.com/view/lovelyz-kei-kim-jiyeon-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-16626147",
            "https://tenor.com/view/kpop-lovelyz-kei-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EC%BC%80%EC%9D%B4-gif-18225963",
            "https://tenor.com/view/lovelyz-kei-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EC%BC%80%EC%9D%B4-gif-18588396",
            "https://tenor.com/view/kei-lovelyz-adorable-braid-gif-18525447",
            "https://tenor.com/view/kpop-korean-lovelyz-kei-gif-10760160",
            "https://tenor.com/view/lovelyz-kei-mijoo-kiss-kpop-gif-16318978",
            "https://tenor.com/view/lovelyz-lovelyz-kei-kei-kim-kei-kim-jiyeon-gif-16341360",
            "https://tenor.com/view/lovelyz-kei-will-kpop-gif-14248063",
            "https://tenor.com/view/lovelyz-kei-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EC%BC%80%EC%9D%B4-gif-19103729"]

        self.bot.lovelyzjisoo_gif = ["https://tenor.com/view/lovelyz-jisoo-oblivate-gif-18570444",
            "https://tenor.com/view/lovelyz-jisoo-oblivate-gif-18570439",
            "https://tenor.com/view/lovelyz-jisoo-smile-kpop-laugh-gif-16210760",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-jisoo-cute-gif-18419265",
            "https://tenor.com/view/lovelyz-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kpop-%EC%A7%80%EC%88%98-jisoo-gif-18243268",
            "https://tenor.com/view/lovelyz-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kpop-%EC%A7%80%EC%88%98-jisoo-gif-18243275",
            "https://tenor.com/view/jisoo-lovelyz-kpop-taking-picture-smile-gif-16278240",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-jisoo-wink-gif-18419268",
            "https://tenor.com/view/lovelyz-oblivate-jisoo-gif-18570448",
            "https://tenor.com/view/lovelyz-oblivate-jisoo-gif-18570440",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-jisoo-%EC%A7%80%EC%88%98-gif-18588384",
            "https://gfycat.com/familiarfluidcrossbill/",
            "https://gfycat.com/leftaffectionateibadanmalimbe/",
            "https://gfycat.com/loathsomehonoredchinesecrocodilelizard/",
            "https://gfycat.com/poshsilentleonberger/",
            "https://gfycat.com/poshsilentleonberger/",
            "https://gfycat.com/dimsimplisticewe",
            "https://gfycat.com/clutteredcandidhectorsdolphin",
            "https://gfycat.com/separateforkedbirdofparadise",
            "https://gfycat.com/jampackedsimplistickillifish",
            "https://gfycat.com/shortshortadder",
            "https://gfycat.com/diligentcandidhairstreak",
            "https://gfycat.com/foolishuncommonhuia",
            "https://gfycat.com/ickymaleamericanratsnake",
            "https://gfycat.com/entirevalidblueandgoldmackaw",
            "https://gfycat.com/soulfulwillingjaguarundi",
            "https://gfycat.com/warmangryjerboa",
            "https://gfycat.com/unhappycompetentbasilisk",
            "https://gfycat.com/untimelywarmheartedbug",
            "https://gfycat.com/completeinfantilealaskankleekai",
            "https://gfycat.com/grotesquemisguidedauk"]

        self.bot.babysoul_gif = ["https://tenor.com/view/lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EB%B2%A0%EC%9D%B4%EB%B9%84%EC%86%8C%EC%9A%B8-babysoul-gif-18331417",
            "https://tenor.com/view/kpop-lovelyz-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EB%B2%A0%EC%9D%B4%EB%B9%84%EC%86%8C%EC%9A%B8-babysoul-gif-18062427",
            "https://tenor.com/view/lovelyz-kpop-babysoul-mijoo-kiss-gif-16319206",
            "https://tenor.com/view/lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-babysoul-%EB%B2%A0%EC%9D%B4%EB%B9%84%EC%86%8C%EC%9A%B8-gif-16303603",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EB%B2%A0%EC%9D%B4%EB%B9%84%EC%86%8C%EC%9A%B8-babysoul-lovelyz-kpop-gif-18230362",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-babysoul-hi-gif-18419259",
            "https://tenor.com/view/lovelyz-babysoul-wow-kpop-gif-16074100",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EB%B2%A0%EC%9D%B4%EB%B9%84%EC%86%8C%EC%9A%B8-babysoul-lovelyz-kpop-gif-18230373",
            "https://tenor.com/view/lovelyz-jisoo-baby-soul-kpop-like-gif-16412292",
            "https://imgur.com/Cgao0Gu"]

        self.bot.mijoo_gif = ["https://tenor.com/view/mijoo-wink-finger-heart-hearts-flying-gif-13440816",
            "https://tenor.com/view/mijoo-dancing-spin-gif-13440825",
            "https://tenor.com/view/lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-mijoo-%EB%AF%B8%EC%A3%BC-gif-16303580",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-kpop-lovelyz-%EB%AF%B8%EC%A3%BC-mijoo-gif-18182571",
            "https://tenor.com/view/mijoo-kpop-lovelyz-%EB%AF%B8%EC%A3%BC-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-18213669",
            "https://tenor.com/view/lovelyz-mijoo-gif-18622921",
            "https://tenor.com/view/lovelyz-mijoo-gif-18622925",
            "https://tenor.com/view/lovelyz-mijoo-kpop-kei-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-19038372",
            "https://tenor.com/view/lovelyz-mijoo-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-focus-gif-19103728",
            "https://tenor.com/view/mijoo-lovelyz-kpop-asian-cute-gif-9068562",
            "https://tenor.com/view/mijoo-mijoo-wdzwm-lovelyz-walk-walking-gif-19219992",
            "https://tenor.com/view/lovelyz-mijoo-gif-18622927",
            "https://tenor.com/view/lovelyz-lee-mijoo-beautiful-beauty-gif-14322042",
            "https://tenor.com/view/mijoo-pose-gif-13440814",
            "https://tenor.com/view/lovelyz-lee-mijoo-mijoo-kpop-pretty-gif-16341282"]

        self.bot.jiae_gif = ["https://tenor.com/view/lovelyz-jiae-kpop-wait-cute-gif-16204526",
            "https://tenor.com/view/lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-jiae-%EC%A7%80%EC%95%A0-gif-16303788",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-jiae-kpop-%EC%A7%80%EC%95%A0-gif-16459876",
            "https://tenor.com/view/lovelyz-jiae-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EC%A7%80%EC%95%A0-gif-17339573",
            "https://tenor.com/view/kpop-%EC%A7%80%EC%95%A0-jiae-lovelyz-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-18243238",
            "https://tenor.com/view/kpop-%EC%A7%80%EC%95%A0-jiae-lovelyz-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-18243242",
            "https://tenor.com/view/kpop-%EC%A7%80%EC%95%A0-jiae-lovelyz-gif-18243246",
            "https://tenor.com/view/jiae-lovelyz-gif-19181488",
            "https://tenor.com/view/jiae-lovelyz-kpop-twinkle-yoo-jiae-gif-15899150",
            "https://tenor.com/view/lovelyz-jiae-yoo-jiae-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-17339578",
            "https://tenor.com/view/lovelyz-yoo-jiae-jiae-lovelyz-jiae-kpop-gif-16673424",
            "https://tenor.com/view/lovelyz-yoo-jiae-jiae-lovelyz-jiae-kpop-gif-16673446"]

        self.bot.ljin_gif = ["https://tenor.com/view/lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-jin-%EB%AA%85%EC%9D%80-gif-16303377",
            "https://tenor.com/view/sugarman3-%EC%8A%88%EA%B0%80%EB%A7%A83-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-%EB%B0%95%EB%AA%85%EC%9D%80-gif-15800266",
            "https://tenor.com/view/lovelyz-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-jin-kpop-%EB%AA%85%EC%9D%80-gif-18588391",
            "https://tenor.com/view/kpop-jin-lovelyz-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EB%AA%85%EC%9D%80-gif-18240324",
            "https://tenor.com/view/kpop-jin-lovelyz-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EB%AA%85%EC%9D%80-gif-18240328",
            "https://tenor.com/view/lovelyz-jin-kpop-cute-pretty-gif-15958211",
            "https://tenor.com/view/lovelyz-jin-kpop-ooh-gif-15998320",
            "https://tenor.com/view/kpop-lovelyz-jin-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-%EB%AA%85%EC%9D%80-gif-18230835",
            "https://tenor.com/view/lovelyz-jin-baby-talking-cute-should-be-like-gif-16057160",
            "https://tenor.com/view/lovelyz-jin-heart-pretty-cute-gif-16057166"]

        self.bot.sujeong_gif = ["https://tenor.com/view/sujeong-lovelyz-ryu-sujeong-gif-13815496",
            "https://tenor.com/view/%EB%A5%98%EC%88%98%EC%A0%95-lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-sujeong-gif-18225977",
            "https://tenor.com/view/sujeon-sujeong-lovelyz-mijoo-babysoul-gif-18201454",
            "https://tenor.com/view/%EB%A5%98%EC%88%98%EC%A0%95-lovelyz-kpop-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-sujeong-gif-18225979",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-kpop-sujeong-%EB%A5%98%EC%88%98%EC%A0%95-gif-18419231",
            "https://tenor.com/view/lovelyz-sujeong-gif-18601629",
            "https://tenor.com/view/sujeong-ryusujeong-lovelyz-lovelyzgif-sujeonggif-gif-19038286",
            "https://tenor.com/view/lovelyz-lovelyzsujeong-ryusujeong-obliviate-unforgettable-gif-18226595",
            "https://tenor.com/view/lovelyz-sujeong-gif-18601631",
            "https://tenor.com/view/lovelyz-mijoo-kpop-sujeong-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-19038398",
            "https://tenor.com/view/sujeong-lovelyz-ryu-sujeong-gif-13815502",
            "https://tenor.com/view/lvlz-lovelyz-ryu-sujeong-sujeong-kpop-gif-16341229",
            "https://tenor.com/view/%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-lovelyz-sujeong-kpop-%EB%A5%98%EC%88%98%EC%A0%95-gif-17312055",
            "https://tenor.com/view/lovelyz-sujeong-kpop-%EB%A5%98%EC%88%98%EC%A0%95-%EB%9F%AC%EB%B8%94%EB%A6%AC%EC%A6%88-gif-17312104",
            "https://tenor.com/view/sujeong-lovelyz-ryu-sujeong-gif-13815500"]

    @commands.command()
    async def yein(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@{mae}>, <@{kiwi}>, <@!{ctx.author.id}> is talking about Yein :white_heart:')
                await ctx.send(random.choice(self.bot.yein_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yein :white_heart:')
            await ctx.send(random.choice(self.bot.yein_gif))
            await ctx.message.delete()

    @commands.command()
    async def kei(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{muffin}>, <@!{ctx.author.id}> is talking about Kei <:keiheart:785792014657912842>')
                await ctx.send(random.choice(self.bot.kei_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Kei <:keiheart:785792014657912842>')
            await ctx.send(random.choice(self.bot.kei_gif))
            await ctx.message.delete()

    @commands.command()
    async def ljisoo(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{mae}>, <@{kiwi}>, <@!{ctx.author.id}> is talking about Jisoo :white_heart:')
                await ctx.send(random.choice(self.bot.lovelyzjisoo_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jisoo :white_heart:')
            await ctx.send(random.choice(self.bot.lovelyzjisoo_gif))
            await ctx.message.delete()

    @commands.command(aliases = ['baby', 'soul'])
    async def babysoul(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Baby Soul :purple_heart:')
                await ctx.send(random.choice(self.bot.babysoul_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Baby Soul :purple_heart:')
            await ctx.send(random.choice(self.bot.babysoul_gif))
            await ctx.message.delete()

    @commands.command()
    async def mijoo(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Mijoo :heart:')
                await ctx.send(random.choice(self.bot.mijoo_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Mijoo :heart:')
            await ctx.send(random.choice(self.bot.mijoo_gif))
            await ctx.message.delete()

    @commands.command()
    async def jiae(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jiae :white_heart:')
                await ctx.send(random.choice(self.bot.jiae_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jiae :white_heart:')
            await ctx.send(random.choice(self.bot.jiae_gif))
            await ctx.message.delete()

    @commands.command()
    async def ljin(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jin :white_heart::black_heart:')
                await ctx.send(random.choice(self.bot.jin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jin :white_heart::black_heart:')
            await ctx.send(random.choice(self.bot.jin_gif))
            await ctx.message.delete()

    @commands.command()
    async def sujeong(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Sujeong <:keiheart:785792014657912842>')
                await ctx.send(random.choice(self.bot.sujeong_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Sujeong <:keiheart:785792014657912842>')
            await ctx.send(random.choice(self.bot.sujeong_gif))
            await ctx.message.delete()

def setup(client):
    client.add_cog(gamerPings(client))