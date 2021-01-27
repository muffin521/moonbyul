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

#//people
jon = 109914198544240640

class RedVelvetPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        #9
        self.bot.irene_gif = ["https://tenor.com/view/irene-irene-bae-bae-joohyun-%ec%95%84%ec%9d%b4%eb%a6%b0-red-velvet-gif-14130526",
            "https://tenor.com/view/irene-pretty-rv-red-velvet-annoyed-gif-14019706",
            "https://tenor.com/view/irene-dance-red-velvet-kpop-irene-red-velvet-gif-13290460",
            "https://tenor.com/view/red-velvet-irene-smile-gif-11069117",
            "https://tenor.com/view/irene-bae-juhyun-irene-bae-%EC%95%84%EC%9D%B4%EB%A6%B0-red-velvet-gif-14480962",
            "https://tenor.com/view/%c4%b1rene-gif-18020419",
            "https://tenor.com/view/irene-red-velvet-ew-eww-scared-gif-12882453",
            "https://tenor.com/view/irene-peace-two-cute-gif-7841178",
            "https://tenor.com/view/irene-gif-14829402"]

        #9
        self.bot.seulgi_gif = ["https://tenor.com/view/red-velvet-%eb%a0%88%eb%93%9c%eb%b2%a8%eb%b2%b3-kpop-seulgi-kang-seulgi-gif-17827226",
            "https://tenor.com/view/seulgi-kang-seulgi-%ec%8a%ac%ea%b8%b0-red-velvet-%eb%a0%88%eb%93%9c%eb%b2%a8%eb%b2%b3-gif-14354377",
            "https://tenor.com/view/seulgi-red-velvet-%ec%8a%ac%ea%b8%b0-%eb%a0%88%eb%93%9c%eb%b2%a8%eb%b2%b3-kpop-gif-16068955",
            "https://tenor.com/view/dancing-twice-red-velvet-kpop-badboy-gif-11824341",
            "https://tenor.com/view/seulgi-gif-18548350",
            "https://tenor.com/view/red-velvet-kpop-seulgi-bored-gif-14040756",
            "https://tenor.com/view/seulgi-ears-flapping-pikachu-hat-red-velvet-gif-12865105",
            "https://tenor.com/view/red-velvet-seulgi-kang-seulgi-smile-kpop-gif-17202871",
            "https://tenor.com/view/seulgi-money-gun-seulgimoneygun-gif-19038811"]

        self.bot.wendy_gif = ["https://tenor.com/view/ryoo-seungwan-wendy-red-velvet-kpop-redhair-gif-5230074",
            "https://tenor.com/view/red-velvet-dance-dumb-dumb-joy-irene-gif-14365084",
            "https://tenor.com/view/wendy-red-velvet-psycho-gif-15872100",
            "https://tenor.com/view/wendy-seungwan-redvelvet-rv-smtown-gif-5110994",
            "https://tenor.com/view/yuuuko-gif-11448258",
            "https://tenor.com/view/red-velvet-wendy-cute-kpop-gif-15124930",
            "https://tenor.com/view/ryoo-seungwan-wendy-red-velvet-kpop-redhair-gif-5229992",
            "https://tenor.com/view/redvelvet-wendy-gif-13398469",
            "https://tenor.com/view/wendy-red-velvet-wendy-wendy-shon-son-seungwan-%EC%9B%AC%EB%94%94-gif-13910394"]

        #13
        self.bot.yeri_gif = ["https://tenor.com/view/kim-yerim-yeri-pointing-lipstick-on-gif-12579366",
            "https://tenor.com/view/yeri-dance-cute-gif-13149660",
            "https://tenor.com/view/yeri-kim-yerim-red-velvet-%EB%A0%88%EB%93%9C%EB%B2%A8%EB%B2%B3-%EC%98%88%EB%A6%AC-gif-14233858",
            "https://tenor.com/view/umpahumpah-kimyeri-yerim-yeri-redvelvet-gif-14820164",
            "https://tenor.com/view/kimyerim-yeri-dance-gif-12536748",
            "https://tenor.com/view/yeri-gif-18540987",
            "https://tenor.com/view/red-velvet-yeri-sm-entertainment-kpop-beautiful-gif-17036585",
            "https://tenor.com/view/yeri-redvelvet-gif-18663409",
            "https://tenor.com/view/yeri-kim-yerim-%EC%98%88%EB%A6%AC-red-velvet-%EB%A0%88%EB%93%9C%EB%B2%A8%EB%B2%B3-gif-15501276",
            "https://tenor.com/view/kim-yerim-yeri-sad-gif-12536905",
            "https://tenor.com/view/kim-yerim-yeri-mua-kisses-gif-12579362",
            "https://tenor.com/view/yeri-wink-cute-gif-13149664",
            "https://tenor.com/view/yeri-kim-yerim-i-dont-care-red-velvet-%EC%98%88%EB%A6%AC-gif-13639966"]

        self.bot.joy_gif = ["https://tenor.com/view/joy-joy-red-velvet-red-velvet-joy-red-velvet-%EC%A1%B0%EC%9D%B4-gif-19140467",
            "https://tenor.com/view/joy-joy-red-velvet-red-velvet-joy-red-velvet-%EB%B0%95%EC%88%98%EC%98%81-gif-19140470",
            "https://tenor.com/view/joy-red-velvet-red-velvet-joy-joy-red-velvet-gif-19142799",
            "https://tenor.com/view/joy-red-velvet-red-velvet-joy-joy-red-velvet-gif-19142802",
            "https://tenor.com/view/joy-red-velvet-red-velvet-joy-joy-red-velvet-gif-19142804",
            "https://tenor.com/view/red-velvet-joy-red-velvet-joy-joy-red-velvet-park-soo-young-gif-19142825",
            "https://tenor.com/view/joy-hi-redvelvet-hello-waving-gif-11110834",
            "https://tenor.com/view/red-velvet-joy-red-velvet-joy-joy-red-velvet-park-soo-young-gif-19142833",
            "https://tenor.com/view/joy-red-velvet-red-velvet-joy-joy-red-velvet-park-soo-young-gif-19142846",
            "https://tenor.com/view/joy-red-velvet-gif-11882538",
            "https://tenor.com/view/joy-joy-red-velvet-red-velvet-korea-gif-18169146",
            "https://tenor.com/view/joy-red-velvet-park-sooyoung-gif-12536684",
            "https://tenor.com/view/joy-red-velvet-joy-red-velvet-gif-11882544",
            "https://tenor.com/view/joy-red-velvet-gif-11882537",
            "https://tenor.com/view/kpop-gif-10448235",
            "https://tenor.com/view/park-sooyoung-joy-red-velvet-wave-hi-gif-12536019",
            "https://tenor.com/view/joy-red-velvet-joy-park-joy-park-sooyoung-%EC%A1%B0%EC%9D%B4-gif-13910368",
            "https://tenor.com/view/joy-red-velvet-kpop-cute-pretty-gif-17059487",
            "https://tenor.com/view/joy-red-velvet-gif-11882529",
            "https://cdn.discordapp.com/attachments/776007496321990666/776011215993438208/park.gif",
            "https://cdn.discordapp.com/attachments/776007496321990666/776011680593084466/heart.gif",
            "https://i.pinimg.com/originals/d8/1a/03/d81a03b3aeb12a985fec7fb4e1135973.gif",
            "https://i.pinimg.com/originals/ad/23/bc/ad23bc99f511ffc236502c6a7c31e87b.gif"]

    @commands.command()
    async def red(self, ctx, vel="velvet", *, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Red Velvet {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if vel == "velvet":
            if arg == "irene":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@{jon}>, <@!{ctx.author.id}> is talking about Irene :watermelon:')
                        await ctx.send(random.choice(self.bot.irene_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Irene :watermelon:')
                    await ctx.send(random.choice(self.bot.irene_gif))
                    await ctx.message.delete()
            elif arg == "seulgi":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Seulgi :pineapple:')
                    await ctx.send(random.choice(self.bot.seulgi_gif))
                    await ctx.message.delete()
            elif arg == "wendy":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Wendy :blue_heart:')
                    await ctx.send(random.choice(self.bot.wendy_gif))
                    await ctx.message.delete()
            elif arg == "yeri":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Yeri :grapes:')
                    await ctx.send(random.choice(self.bot.yeri_gif))
                    await ctx.message.delete()
            elif arg == "joy":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Joy :kiwi:')
                    await ctx.send(random.choice(self.bot.joy_gif))
                    await ctx.message.delete()

    @commands.command()
    async def irene(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{jon}>, <@!{ctx.author.id}> is talking about Irene :watermelon:')
                await ctx.send(random.choice(self.bot.irene_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Irene :watermelon:')
            await ctx.send(random.choice(self.bot.irene_gif))
            await ctx.message.delete()
    
    @commands.command()
    async def seulgi(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Seulgi :pineapple:')
                await ctx.send(random.choice(self.bot.seulgi_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Seulgi :pineapple:')
            await ctx.send(random.choice(self.bot.seulgi_gif))
            await ctx.message.delete()

    @commands.command()
    async def wendy(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Wendy :blue_heart:')
                await ctx.send(random.choice(self.bot.wendy_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Wendy :blue_heart:')
            await ctx.send(random.choice(self.bot.wendy_gif))
            await ctx.message.delete()

    @commands.command()
    async def yeri(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Yeri :grapes:')
                await ctx.send(random.choice(self.bot.yeri_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Yeri :grapes:')
            await ctx.send(random.choice(self.bot.yeri_gif))
            await ctx.message.delete()

    @commands.command()
    async def joy(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Joy :kiwi:')
                await ctx.send(random.choice(self.bot.joy_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Joy :kiwi:')
            await ctx.send(random.choice(self.bot.joy_gif))
            await ctx.message.delete()
    
    


def setup(client):
    client.add_cog(RedVelvetPings(client))