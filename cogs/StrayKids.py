import discord, random
from discord.ext import commands

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

class StrayPings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.felix_gif = ["https://tenor.com/view/felix-lee-yongbok-dog-puppy-gif-16974825",
            "https://tenor.com/view/stray-kids-felix-lee-lee-felix-cute-gif-13005382",
            "https://tenor.com/view/cute-felix-gif-16008442",
            "https://tenor.com/view/felix-stray-kids-kpop-stare-cute-gif-17660812",
            "https://tenor.com/view/stray-kids-lee-felix-fly-kiss-gif-14222407",
            "https://cdn.discordapp.com/attachments/802983833204162670/802986872878923786/image0.gif",
            "https://cdn.discordapp.com/attachments/802983833204162670/802986873449742356/image1.gif",
            "https://cdn.discordapp.com/attachments/802983833204162670/802987069186113616/image0.gif",
            "https://cdn.discordapp.com/attachments/802983833204162670/802987069726785556/image1.gif",
            "https://tenor.com/view/felix-lee-cute-stray-kids-gif-18617656",
            "https://tenor.com/view/stray-kids-felix-lee-felix-lee-yongbok-lead-dancer-gif-17580819",
            "https://tenor.com/view/felix-stray-kids-smile-gif-10510975"]

        self.bot.shyunjin_gif = ["https://tenor.com/view/funny-jyp-cute-hyunjincute-hyunjin-gif-13417088",
            "https://tenor.com/view/hyunjin-hyunjin-skz-anyways-skz-stray-kids-gif-18096876",
            "https://tenor.com/view/hyunjin-hwang-gif-18553566",
            "https://tenor.com/view/straykids-hyunjin-rapper-hair-f-ix-head-shake-gif-17468856",
            "https://tenor.com/view/hwang-hyunjin-kpop-gif-14009678",
            "https://cdn.discordapp.com/attachments/802983894273359942/802987219883130880/image0.gif",
            "https://tenor.com/view/stray-kids-stray-kids-hyunjin-gif-18127666"]
    
        self.bot.bangchan_gif = ["https://tenor.com/view/bang-chan-stray-kids-skz-wave-gif-15490742",
            "https://tenor.com/view/bang-chan-stray-kids-kpop-hanger-funny-gif-15229014",
            "https://tenor.com/view/stray-kids-dingo-bang-chan-hey-kpop-gif-14230381",
            "https://tenor.com/view/bang-chan-gif-18200044",
            "https://tenor.com/view/bang-chan-gif-18199694"]

        self.bot.leeknow_gif = ["https://tenor.com/view/lee-know-straykids-lee-minho-leeknow-straykids-leeminho-straykids-gif-14398192",
            "https://tenor.com/view/stray-kids-lee-know-minho-lee-lee-minho-gif-13005374",
            "https://tenor.com/view/lee-know-lee-minho-stray-kids-shocked-kpop-gif-14968607",
            "https://tenor.com/view/stray-kids-lee-know-lee-know-stray-kids-stray-kids-lee-know-minho-gif-18109448",
            "https://tenor.com/view/hanniefelix-stray-kids-lee-know-minho-gif-18122290",
            "https://tenor.com/view/lee-know-lino-minho-lee-minho-stray-kids-gif-18658916"]

        self.bot.changbin_gif = ["https://tenor.com/view/seo-changbin-changbin-stray-kids-cute-kpop-gif-16229714",
            "https://tenor.com/view/stray-kids-skx-changbin-seo-changbin-lip-bite-gif-16669575",
            "https://tenor.com/view/stray-kids-skz-changbin-seo-changbin-handsome-gif-16669535",
            "https://tenor.com/view/stray-kids-changbin-seo-kpop-smile-handsome-gif-16275076",
            "https://tenor.com/view/stray-kids-skz-changbin-seo-changbin-gif-16669559"]

        self.bot.han_gif = ["https://tenor.com/view/skz-stray-kidz-stray-kids-han-jisung-kpop-gif-16958093",
            "https://tenor.com/view/nct-jisung-park-jisung-kpop-handsome-gif-15640966",
            "https://tenor.com/view/stray-kids-han-jisung-kpop-cute-shocked-gif-16276398",
            "https://tenor.com/view/han-jisung-han-gif-17974604",
            "https://tenor.com/view/han-flip-hair-gif-13165511",
            "https://tenor.com/view/han-jisung-stray-kids-gif-14185103"]

        self.bot.jeongin_gif = ["https://tenor.com/view/clapping-stray-kids-in-yang-jeongin-vocalist-gif-17816584",
            "https://tenor.com/view/in-yang-jeongin-shocked-stray-kids-kpop-gif-14357751",
            "https://tenor.com/view/stray-kids-cute-smile-kpop-gif-12423054",
            "https://tenor.com/view/straykids-skz-wave-jeongin-gif-18444736",
            "https://tenor.com/view/stray-kids-in-yang-jeongin-vocalist-maknae-gif-17946216",
            "https://cdn.discordapp.com/attachments/802983955733282816/802987402914299914/image0.gif"]

        self.bot.seungmin_gif = ["https://tenor.com/view/stray-kids-kim-seungmin-seungmin-cute-kpop-gif-16435548",
            "https://tenor.com/view/kim-seungmin-stray-kids-seungmin-thumbs-up-approve-gif-16363315",
            "https://tenor.com/view/seung-min-kim-straykids-chomp-heart-smile-gif-13471299",
            "https://tenor.com/view/stray-kids-seungmin-kim-seungmin-seungmin-stray-kids-laugh-gif-14375802",
            "https://tenor.com/view/kim-seungmin-stray-kids-seungmin-cute-kpop-gif-16363329"]

    @commands.command()
    async def felix(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Felix :heart:')
                await ctx.send(random.choice(self.bot.felix_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Felix :heart:')
            await ctx.send(random.choice(self.bot.felix_gif))
            await ctx.message.delete()

    @commands.command()
    async def shyunjin(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Hyunjin :heart:')
                await ctx.send(random.choice(self.bot.shyunjin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Hyunjin :heart:')
            await ctx.send(random.choice(self.bot.shyunjin_gif))
            await ctx.message.delete()

    @commands.command(alias=['bang chan'])
    async def bang(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Bang Chan :heart:')
                await ctx.send(random.choice(self.bot.bangchan_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Bang Chan :heart:')
            await ctx.send(random.choice(self.bot.bangchan_gif))
            await ctx.message.delete()

    @commands.command(aliases=['leeknow', 'leeminho', 'lee'])
    async def lino(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Lee Know :heart:')
                await ctx.send(random.choice(self.bot.leeknow_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Lee Know :heart:')
            await ctx.send(random.choice(self.bot.leeknow_gif))
            await ctx.message.delete()

    @commands.command()
    async def changbin(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Changbin :heart:')
                await ctx.send(random.choice(self.bot.changbin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Changbin :heart:')
            await ctx.send(random.choice(self.bot.changbin_gif))
            await ctx.message.delete()

    @commands.command()
    async def han(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Han :heart:')
                await ctx.send(random.choice(self.bot.han_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Han :heart:')
            await ctx.send(random.choice(self.bot.han_gif))
            await ctx.message.delete()

    @commands.command()
    async def jeongin(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jeongin :heart:')
                await ctx.send(random.choice(self.bot.jeongin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jeongin :heart:')
            await ctx.send(random.choice(self.bot.jeongin_gif))
            await ctx.message.delete()

    @commands.command()
    async def seungmin(self,ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Seungmin :heart:')
                await ctx.send(random.choice(self.bot.seungmin_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Seungmin :heart:')
            await ctx.send(random.choice(self.bot.seungmin_gif))
            await ctx.message.delete()

    @commands.command()
    async def stray(self, ctx, kids, *, arg="yessir"):
        if kids == "kids":
            if arg == "felix":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@!{ctx.author.id}> is talking about Felix :heart:')
                        await ctx.send(random.choice(self.bot.felix_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Felix :heart:')
                    await ctx.send(random.choice(self.bot.felix_gif))
                    await ctx.message.delete()
            elif arg == "bang chan":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@!{ctx.author.id}> is talking about Bang Chan :heart:')
                        await ctx.send(random.choice(self.bot.bangchan_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Bang Chan :heart:')
                    await ctx.send(random.choice(self.bot.bangchan_gif))
                    await ctx.message.delete()
            elif arg == "lee know" or arg == "minho":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@!{ctx.author.id}> is talking about Lee Know :heart:')
                        await ctx.send(random.choice(self.bot.leeknow_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Lee Know :heart:')
                    await ctx.send(random.choice(self.bot.leeknow_gif))
                    await ctx.message.delete()
            elif arg == "changbin":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@!{ctx.author.id}> is talking about Changbin :heart:')
                        await ctx.send(random.choice(self.bot.changbin_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Changbin :heart:')
                    await ctx.send(random.choice(self.bot.changbin_gif))
                    await ctx.message.delete()
            elif arg == "han":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@!{ctx.author.id}> is talking about Han :heart:')
                        await ctx.send(random.choice(self.bot.han_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Han :heart:')
                    await ctx.send(random.choice(self.bot.han_gif))
                    await ctx.message.delete()
            elif arg == "jeongin" or arg == "in" or arg == "i.n":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@!{ctx.author.id}> is talking about I.N :heart:')
                        await ctx.send(random.choice(self.bot.jeongin_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about I.N :heart:')
                    await ctx.send(random.choice(self.bot.jeongin_gif))
                    await ctx.message.delete()
            elif arg == "seungmin":
                if ctx.guild.id == luminary:
                    if ctx.channel.id == kbotcom:
                        await ctx.send(f'<@!{ctx.author.id}> is talking about Seungmin :heart:')
                        await ctx.send(random.choice(self.bot.seungmin_gif))
                        await ctx.message.delete()
                    else:
                        await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                        await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Seungmin :heart:')
                    await ctx.send(random.choice(self.bot.seungmin_gif))
                    await ctx.message.delete()
            elif arg == "hyunjin":
                if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                    await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                    await ctx.message.delete()
                else:
                    await ctx.send(f'<@!{ctx.author.id}> is talking about Hyunjin :heart:')
                    await ctx.send(random.choice(self.bot.shyunjin_gif))
                    await ctx.message.delete()



def setup(client):
    client.add_cog(StrayPings(client))