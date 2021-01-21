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


class OhMyGirl(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.ohmygirl_arin_gif = ["https://gfycat.com/rapidregalkingsnake-oh-my-girl-arin-kpop",
            "http://gfycat.com/GorgeousThinGrayreefshark",
            "https://gfycat.com/regulartidycrow",
            "https://gfycat.com/frenchbrowngalapagosdove",
            "https://gfycat.com/wholeillustriousboar",
            "https://gfycat.com/frigidsmoothbaleenwhale",
            "https://tenor.com/view/arin-gif-19615783",
            "https://tenor.com/view/arin-omg-oh-my-girl-confused-maknae-gif-11167451",
            "https://tenor.com/view/arin-oh-nari-oh-my-girl-kpop-when-crush-is-flirting-with-other-girl-gif-18284767",
            "https://tenor.com/view/arin-dance-ohmygirl-mylove-nui-gif-19089552",
            "https://tenor.com/view/%EC%95%84%EB%A6%B0-%EC%98%A4%EB%A7%88%EC%9D%B4%EA%B1%B8-arin-maknae-ohmygirl-gif-18617575",
            "https://tenor.com/view/ohmygirl-arinohmygirl-arin-gif-19590171",
            "https://tenor.com/view/arin-ohmygirl-gif-7348565",
            "https://tenor.com/view/arin-ohmygirl-gif-7348613",
            "https://tenor.com/view/arin-arinohmygirl-ohmygirl-gif-19590570",
            "https://tenor.com/view/arin-kpop-oh-nari-ohmygirl-%EC%95%84%EB%A6%B0-gif-18284837",
            "https://tenor.com/view/arinohmygirl-arin-ohmygirl-gif-19590229",
            "https://tenor.com/view/arinohmygirl-arin-ohmygirl-gif-19590295",
            "https://tenor.com/view/arinohmygirl-arin-ohmygirl-gif-19590311",
            "https://tenor.com/view/arin-ohmygirl-arinohmygirl-gif-19590617",
            "https://tenor.com/view/arinohmygirl-arin-ohmygirl-kpop-gif-19590712",
            "https://tenor.com/view/oh-my-girl-omg-kpop-cute-pretty-gif-17578691",
            "https://tenor.com/view/arin-ohmygirl-gif-19627547",
            "https://tenor.com/view/arin-ohmygirl-gif-19627552",
            "https://tenor.com/view/arin-oh-my-girl-k-pop-cute-gif-10864594",
            "https://tenor.com/view/arin-oh-na-ri-oh-my-girl-girls-world-kpop-gif-18284697",
            "https://tenor.com/view/arin-oh-my-girl-fresh-look-%EC%95%84%EB%A6%B0-%EC%98%A4%EB%A7%88%EC%9D%B4%EA%B1%B8-gif-18617383",
            "https://tenor.com/view/arin-oh-my-girl-%EC%95%84%EB%A6%B0-%EC%98%A4%EB%A7%88%EC%9D%B4%EA%B1%B8%EC%95%84%EB%A6%B0-kpop-gif-19649272",
            "https://tenor.com/view/%EC%95%84%EB%A6%B0-%EC%B5%9C%EC%95%84%EB%A6%B0-arin-oh-my-girl-maknae-gif-19834825",
            "https://tenor.com/view/arin-dane-arin-gif-19063881",
            "https://tenor.com/view/arin-gif-19615781",
            "https://tenor.com/view/arin-choi-arin-oh-my-girl-maknae-gif-19835052",
            "https://tenor.com/view/arin-approved-oh-my-girl-oh-my-girl-arin-arin-choiarin-gif-7566702",
            "https://tenor.com/view/%EC%82%B4%EC%A7%9D%EC%84%A4%EB%A0%9C%EC%96%B4-%EC%98%A4%EB%A7%88%EC%9D%B4%EA%B1%B8-%EC%95%84%EB%A6%B0-%EC%82%B4%EC%A7%9D-%EC%84%A4%EB%A0%9C%EC%96%B4-gif-18599815",
            "https://tenor.com/view/arin-gif-18197837",
            "https://tenor.com/view/arin-gif-19615785",
            "https://tenor.com/view/arin-gif-19588473",
            "https://tenor.com/view/%EC%95%84%EB%A6%B0-%EC%98%A4%EB%A7%88%EC%9D%B4%EA%B1%B8%EC%95%84%EB%A6%B0-arin-ohmygirl-arin-kpop-gif-18295336",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19768503",
            "https://tenor.com/view/oh-my-girl-arin-gif-19488436"]

        self.bot.ohmygirl_binnie_gif = ["https://gfycat.com/sadlonegalapagosdove",
            "https://tenor.com/view/oh-my-girl-kpop-hi-wave-binnie-gif-15821110",
            "https://tenor.com/view/oh-my-girl-nods-binnie-gif-15516237",
            "https://tenor.com/view/oh-my-girl-binnie-smiliing-thumbs-up-okay-gif-6023652",
            "https://tenor.com/view/oh-my-girl-binnie-headset-cute-smile-gif-15422340",
            "https://tenor.com/view/oh-my-girl-binnie-heart-cute-pretty-gif-15486924",
            "https://tenor.com/view/oh-my-girl-binnie-cute-smile-pretty-gif-15486918",
            "https://tenor.com/view/oh-my-girl-binnie-so-cute-cute-pretty-gif-15534812",
            "https://tenor.com/view/oh-my-girl-binnie-cute-smile-kpop-gif-15586122",
            "https://tenor.com/view/oh-my-girl-binnie-smile-cute-eyeglasses-gif-15586120",
            "https://tenor.com/view/oh-my-girl-binnie-party-hat-eating-hungry-gif-15813573",
            "https://tenor.com/view/oh-my-girl-binnie-what-gif-16233447",
            "https://tenor.com/view/oh-my-girl-binnie-laugh-gif-16233448",
            "https://tenor.com/view/oh-my-girl-binnie-heart-cute-gif-16233454",
            "https://tenor.com/view/oh-my-girl-binnie-shower-sing-gif-16233451",
            "https://tenor.com/view/binnie-oh-my-girl-kpop-cute-gif-14728577",
            "https://tenor.com/view/oh-my-girl-binnie-oh-my-gif-15422337",
            "https://tenor.com/view/bae-yoobin-binnie-binnie-oh-my-girl-dance-gif-15125077",
            "https://tenor.com/view/binnie-binnie-oh-my-girl-bae-yoobin-kpop-windy-gif-15131354",
            "https://tenor.com/view/binnie-binnie-oh-my-girl-bae-yoobin-peace-sign-kpop-gif-15131355",
            "https://tenor.com/view/binnie-binnie-oh-my-girl-bae-yoobin-me-kpop-gif-15131357",
            "https://tenor.com/view/oh-my-girl-binnie-cute-short-hair-happy-gif-15586118",
            "https://tenor.com/view/oh-my-girl-binnie-laugh-happy-cute-gif-15813570",
            "https://tenor.com/view/oh-my-girl-binnie-dance-cool-moves-gif-15856553",
            "https://tenor.com/view/oh-my-girl-binnie-wave-hi-cute-gif-15856563"]

        self.bot.ohmygirl_hyojung_gif = ["https://tenor.com/view/oh-my-girl-cute-girl-smile-illusion-gif-16725606",
            "https://tenor.com/view/lol-rofl-laughing-laugh-oh-my-girl-gif-14647344",
            "https://tenor.com/view/hyojung-oh-my-girl-kpop-candy-cute-gif-15174724",
            "https://tenor.com/view/hyo-jung-ohmygirl-two-hyo-jungs-gif-11362670",
            "https://tenor.com/view/hyojung-gif-17985829",
            "https://tenor.com/view/hyojung-choihyojung-oh-my-girl-candyleader-leader-gif-19591309",
            "https://tenor.com/view/choihyojung-hyojung-ohmygirl-candyleader-gif-19591317",
            "https://tenor.com/view/hyojung-gif-19591387",
            "https://tenor.com/view/hyojung-gif-19591416",
            "https://tenor.com/view/%ED%9A%A8%EC%A0%95-hyojung-gif-19600566",
            "https://tenor.com/view/%ED%9A%A8%EC%A0%95-hyojung-gif-19600428",
            "https://tenor.com/view/hyojung-%ED%9A%A8%EC%A0%95-gif-19639358",
            "https://tenor.com/view/hyojung-%ED%9A%A8%EC%A0%95-gif-19703279",
            "https://tenor.com/view/%ED%9A%A8%EC%A0%95-hyojung-gif-19703281",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19768489",
            "https://tenor.com/view/%ED%9A%A8%EC%A0%95-hyojung-gif-19703302",
            "https://tenor.com/view/%ED%9A%A8%EC%A0%95-hyojung-gif-19790779",
            "https://tenor.com/view/%ED%9A%A8%EC%A0%95-hyojung-gif-19790850",
            "https://tenor.com/view/hyojung-gif-19800689",
            "https://tenor.com/view/hyojung-gif-19800690",
            "https://tenor.com/view/hyojung-gif-19800691",
            "https://tenor.com/view/hyojung-gif-19800693",
            "https://tenor.com/view/hyojung-gif-19800694",
            "https://tenor.com/view/hyojung-gif-19800695",
            "https://tenor.com/view/hyojung-gif-19857821",
            "https://tenor.com/view/hyojung-gif-19857822",
            "https://tenor.com/view/choi-hyojung-hyojung-gif-19591487",
            "https://tenor.com/view/hyojung-gif-19857823"]

        self.bot.ohmygirl_jiho_gif = ["https://gfycat.com/velvetywildcowbird",
            "https://tenor.com/view/jiho-omg-oh-my-girl-kim-jiho-kpop-gif-17349420",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19796935",
            "https://tenor.com/view/oh-my-girl-jiho-kim-jiho-kpop-bye-gif-16936859",
            "https://tenor.com/view/oh-my-girl-jiho-pew-pew-gif-14581615",
            "https://tenor.com/view/oh-my-girl-kpop-jiho-gif-13994116",
            "https://tenor.com/view/kpop-oh-my-girl-kim-jiho-jiho-pretty-gif-17096348",
            "https://tenor.com/view/oh-my-girl-jiho-kim-jiho-kpop-kawaii-gif-16936836",
            "https://tenor.com/view/jiho-omg-oh-my-girl-kim-jiho-kpop-gif-17349426",
            "https://tenor.com/view/jiho-omg-oh-my-girl-kim-jiho-kpop-gif-17349428",
            "https://tenor.com/view/jiho-omg-oh-my-girl-kim-jiho-kpop-gif-17349421",
            "https://tenor.com/view/kpop-oh-my-girl-kim-jiho-jiho-pretty-gif-17096350",
            "https://tenor.com/view/kim-jiho-jiho-omg-oh-my-girl-kpop-gif-17514374",
            "https://tenor.com/view/jiho-kim-jiho-oh-my-girl-dancing-dance-gif-15912862",
            "https://tenor.com/view/kim-jiho-jiho-omg-oh-my-girl-kpop-gif-17514371",
            "https://tenor.com/view/jiho-kim-jiho-oh-my-girl-k-pop-gif-11085667",
            "https://tenor.com/view/oh-my-girl-jiho-clap-applause-gif-14581662",
            "https://tenor.com/view/oh-my-girl-jiho-princess-korean-smile-gif-14581638",
            "https://tenor.com/view/kpop-oh-my-girl-jiho-singing-gif-13982656",
            "https://tenor.com/view/jiho-oh-my-girl-kpop-binnie-gif-15174709",
            "https://tenor.com/view/jiho-oh-my-girl-bye-cute-gif-14786179",
            "https://tenor.com/view/jiho-oh-my-girl-kpop-gif-11085635",
            "https://tenor.com/view/jiho-ohmygirl-gif-19507110"]

        self.bot.ohmygirl_mimi_gif = ["https://tenor.com/view/mimi-oh-my-girl-rap-forehead-mic-gif-15514487",
            "https://tenor.com/view/ohmygirl-mimi-gif-19477876",
            "https://tenor.com/view/ohmygirl-mimi-gif-19477868",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19796894",
            "https://tenor.com/view/oh-my-girl-mimi-wink-smile-gif-16233449",
            "https://tenor.com/view/mimi-mihyun-oh-my-girl-blonde-kpop-gif-15149089",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19796931",
            "https://tenor.com/view/mimi-oh-my-girl-cute-kiss-gif-15401382",
            "https://tenor.com/view/ohmygirl-mimi-gif-6083158",
            "https://tenor.com/view/mimi-ohmygirl-windyday-gif-6083154",
            "https://tenor.com/view/ohmygirl-mimi-gif-6083155",
            "https://tenor.com/view/mimi-birthday-mimi-mimi-omg-mimi-oh-my-girl-oh-my-girl-gif-19911544",
            "https://tenor.com/view/mimi-mimi-oh-my-girl-omg-oh-my-girl-mimi-kim-mihyun-gif-19911077"]

        self.bot.ohmygirl_seunghee_gif = ["https://tenor.com/view/aww-jiggle-ohmygirl-pout-korean-gif-18118579",
            "https://gfycat.com/bountifulbronzekarakul",
            "https://gfycat.com/demandingnauticalankolewatusi",
            "https://gfycat.com/specificmammothimago",
            "https://gfycat.com/memorableweticelandicsheepdog",
            "https://gfycat.com/belatedfrighteningamericancrow",
            "https://tenor.com/view/seunghee-ohmygirl-gif-7956413",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19796891",
            "https://tenor.com/view/seunghee-oh-my-girl-bungee-oh-my-girl-bungee-kpop-gif-14748328",
            "https://tenor.com/view/oh-my-girl-seunghee-cute-gif-15318622",
            "https://tenor.com/view/oh-my-girl-seunghee-binnie-what-shocked-gif-16233453",
            "https://tenor.com/view/oh-my-girl-seunghee-cute-smirk-kpop-gif-15813574",
            "https://gfycat.com/farinsignificantguanaco",
            "https://gfycat.com/allsimilardodobird"]

        self.bot.ohmygirl_yooa_gif = ["https://gfycat.com/querulousangelicarctichare-yooa",
            "https://media.discordapp.net/attachments/643623059541983242/770648857595084832/2ac60c3d-e2fd-4649-beca-88c8cc046231.gif",
            "https://media.discordapp.net/attachments/643623059541983242/765810697668919306/a86f6994-2d5b-4e53-99d4-a9e97afe702c.gif",
            "https://media.discordapp.net/attachments/643623059541983242/762172786579472424/743ee0e1-bed3-47cd-b0df-009f52f49e24.gif",
            "https://tenor.com/view/yooa-oh-my-girl-pose-gif-13089630",
            "https://tenor.com/view/yooa-oh-my-girl-swing-gif-13089628",
            "https://tenor.com/view/yooa-oh-my-girl-windy-gif-14668696",
            "https://tenor.com/view/oh-my-girl-kpop-yooa-gif-14589516",
            "https://tenor.com/view/yooa-kpop-oh-my-girl-stare-bored-gif-14719310",
            "https://tenor.com/view/yooa-oh-my-girl-no-gif-16116013",
            "https://tenor.com/view/yooa-oh-my-girl-yes-cute-gif-16116022",
            "https://tenor.com/view/love-ent-dance-moves-cute-kpop-gif-16763464",
            "https://tenor.com/view/yooa-yoo-shiah-oh-my-girl-cute-model-gif-17136236",
            "https://tenor.com/view/cupid-yooa-yoo-shiah-shasha-gif-17230832",
            "https://tenor.com/view/yooa-oh-my-girl-gif-18411900",
            "https://tenor.com/view/%EC%82%B4%EC%A7%9D%EC%84%A4%EB%A0%9C%EC%96%B4-%EC%9C%A0%EC%95%84-%EC%98%A4%EB%A7%88%EC%9D%B4%EA%B1%B8-%EC%82%B4%EC%A7%9D-%EC%84%A4%EB%A0%9C%EC%96%B4-gif-18599365",
            "https://tenor.com/view/yooa-ohmygirl-gif-18677966",
            "https://tenor.com/view/yooa-bon-voya-bon-voyage-oh-my-girl-yen-gif-19129387",
            "https://tenor.com/view/yooa-oh-my-girl-dance-gif-19129508",
            "https://tenor.com/view/yooa-ohmygirl-kick-gif-19367595",
            "https://tenor.com/view/yooa-%EC%9C%A0%EC%95%84-gif-19536364",
            "https://tenor.com/view/yooa-%EC%9C%A0%EC%95%84-gif-19585283",
            "https://tenor.com/view/yooa-gif-19800697",
            "https://tenor.com/view/yooa-gif-19800699",
            "https://tenor.com/view/yooa-gif-19800700",
            "https://tenor.com/view/yooa-gif-19845605",
            "https://tenor.com/view/2020mama-mama-moment-performance-music-kpop-gif-19846776",
            "https://tenor.com/view/yooa-gif-9766588",
            "https://tenor.com/view/yooa-gif-19864148",
            "https://tenor.com/view/yooa-oh-my-girl-yoo-shiah-kpop-cute-gif-17057394",
            "https://tenor.com/view/yooa-oh-my-girl-cute-gif-13089631",
            "https://tenor.com/view/oh-my-girl-yooa-yoo-yeonjoo-yoo-shiah-kpop-gif-16995123",
            "https://tenor.com/view/yooa-gif-9815748",
            "https://gfycat.com/pointedagitatedbeauceron",
            "https://gfycat.com/talkativefrightenedekaltadeta",
            "https://gfycat.com/passionateweirdacornweevil",
            "https://gfycat.com/frailinfantilealbertosaurus",
            "https://gfycat.com/caringfinishedcurlew",
            "https://cdn.discordapp.com/attachments/643623059541983242/760833049712656444/8301befb-9751-4549-b05b-e63db5493a08.gif",
            "https://gfycat.com/unevendistantindianspinyloach-oh-my-girl-yooa",
            "https://gfycat.com/whoppingloathsomecanary-beauty"]

    @commands.command()
    async def oh(self, ctx, my, girl, arg):
        if my == "my" and girl == "girl":
            if arg == "arin":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Arin :heart:')
                    await ctx.send(random.choice(self.bot.ohmygirl_arin_gif))
                    await ctx.message.delete()
            elif arg == "binnie":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Binnie :heart:')
                    await ctx.send(random.choice(self.bot.ohmygirl_binnie_gif))
                    await ctx.message.delete()
            elif arg == "hyojung":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Hyojung :heart:')
                    await ctx.send(random.choice(self.bot.ohmygirl_hyojung_gif))
                    await ctx.message.delete()
            elif arg == "jiho":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Jiho :heart:')
                    await ctx.send(random.choice(self.bot.ohmygirl_jiho_gif))
                    await ctx.message.delete()
            elif arg == "mimi":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Mimi :heart:')
                    await ctx.send(random.choice(self.bot.ohmygirl_mimi_gif))
                    await ctx.message.delete()
            elif arg == "seunghee":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Seunghee :heart:')
                    await ctx.send(random.choice(self.bot.ohmygirl_seunghee_gif))
                    await ctx.message.delete()
            elif arg == "yooa":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about YooA :heart:')
                    await ctx.send(random.choice(self.bot.ohmygirl_yooa_gif))
                    await ctx.message.delete()


def setup(client):
    client.add_cog(OhMyGirl(client))