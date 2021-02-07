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


class exid(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

        self.bot.hani_gif = ["https://tenor.com/view/exid-hani-rose-pretty-woman-exidolove-gif-13667122",
            "https://tenor.com/view/exid-hani-wink-gif-12894391",
            "https://tenor.com/view/exid-hani-ddd-softhani-kpop-gif-10565394",
            "https://gfycat.com/wandefensivekitfox",
            "https://tenor.com/view/hani-exid-gif-5407220",
            "https://tenor.com/view/hani-exid-pretty-rose-wink-gif-13667120",
            "https://cdn.discordapp.com/attachments/786739586633039872/789648437976891392/original_10.gif",
            "https://cdn.discordapp.com/attachments/786739586633039872/789648438382952468/original_12.gif",
            "https://cdn.discordapp.com/attachments/786739586633039872/789648439356686336/4810c7b1bcb4a71ba4878f7cf4621c72.gif",
            "https://cdn.discordapp.com/attachments/786739586633039872/789648440014405662/original_9.gif",
            "https://cdn.discordapp.com/attachments/786739586633039872/789648440669241355/AncientCircularHyracotherium-max-1mb.gif",
            "https://cdn.discordapp.com/attachments/786739586633039872/789648440941609030/giphy_7.gif",
            "https://cdn.discordapp.com/attachments/786739586633039872/789648442279985242/original_8.gif",
            "https://cdn.discordapp.com/attachments/786739586633039872/789648442942947338/tenor_13.gif"] 
        
        self.bot.jeonghwa_gif = ["https://gfycat.com/energeticboringchafer",
            "https://tenor.com/beIfZ.gif",
            "https://gfycat.com/remarkablehollowelk",
            "https://gfycat.com/gravegrouchycaimanlizard",
            "https://gfycat.com/bluewealthycatfish"]

        self.bot.le_gif = ["https://gfycat.com/bronzeamazingcob",
            "https://gfycat.com/impoliteremoteanaconda",
            "https://gfycat.com/wastefulweeklyinsect",
            "https://tenor.com/83yR.gif"]
        
        self.bot.solji_gif = ["https://gfycat.com/astonishinghairybobwhite",
            "https://gfycat.com/alllastcanine",
            "https://gfycat.com/thinimperturbableargentinehornedfrog",
            "https://tenor.com/beIgg.gif",
            "https://tenor.com/beIfG.gif"]

        self.bot.hyelin_gif = ["https://gfycat.com/illiterateglitteringcreature",
            "https://gfycat.com/uniquealiveblackfootedferret",
            "https://tenor.com/beIf3.gif",
            "https://tenor.com/7AzI.gif",
            "https://media.giphy.com/media/3ofSB8sjdj8OAOVdeg/giphy.gif"]

    @commands.command()
    async def exid(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.bot.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [Exid {arg}] | USER: {ctx.author.name} [{(ctx.author.id)} | GUILD: {ctx.guild.name} [{ctx.guild.id}]]`" )
        if arg == "hani":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Hani :heart: ')
                await ctx.send(random.choice(self.bot.hani_gif))
                await ctx.message.delete()
        elif arg == "jeonghwa":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jeonghwa :heart: ')
                await ctx.send(random.choice(self.bot.jeonghwa_gif))
                await ctx.message.delete()
        elif arg == "le":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about LE :heart: ')
                await ctx.send(random.choice(self.bot.le_gif))
                await ctx.message.delete()
        elif arg == "solji":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Solji :heart: ')
                await ctx.send(random.choice(self.bot.solji_gif))
                await ctx.message.delete()
        elif arg == "hyelin" or arg == "hyerin":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
            else: 
                await ctx.send(f'<@!{ctx.author.id}> is talking about Hyelin :heart: ')
                await ctx.send(random.choice(self.bot.hyelin_gif))
                await ctx.message.delete()

def setup(client):
    client.add_cog(exid(client))