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
            "https://tenor.com/83yR.gif",
            "https://media.discordapp.net/attachments/170190224457072640/815847290337230898/431202028652593152tumblr_mh1mc8a5GH1s46ypvo8_400.gif",
            "https://media.discordapp.net/attachments/170190224457072640/816013638363775037/431195981045039105tumblr_nzlpgyfITg1uvceqto3_400.gif",
            "https://media.discordapp.net/attachments/170190224457072640/815051402459480124/4135848318853447781518676675034.gif",
            "https://media.discordapp.net/attachments/170190224457072640/815021179055374376/431202012634415108tumblr_mh1mc8a5GH1s46ypvo2_400.gif",
            "https://media.discordapp.net/attachments/170190224457072640/814198012871573524/431195951953346560tumblr_nqlgz5LnYp1u9cs5co1_500.gif",
            "http://gph.is/2rohMOY",
            "https://tenor.com/3EYx.gif",
            "https://tenor.com/Y2Zs.gif",
            "https://tenor.com/3IiL.gif",
            "https://tenor.com/4Jru.gif",
            "https://tenor.com/4JqI.gif",
            "https://tenor.com/3BFP.gif",
            "https://tenor.com/7YId.gif",
            "https://tenor.com/Y2Ze.gif",
            "https://tenor.com/bimZw.gif",
            "https://tenor.com/3BF3.gif",
            "https://tenor.com/beIjf.gif",
            "https://tenor.com/beIgj.gif",
            "https://tenor.com/bgGJj.gif",
            "https://tenor.com/3BC0.gif",
            "http://gph.is/2rTK081",
            "http://gph.is/2rohMOY",
            "http://gph.is/2rTF7fi",
            "https://tenor.com/beIgc.gif",
            "https://tenor.com/beIfH.gif",
            "https://tenor.com/beHXP.gif",
            "https://tenor.com/bimZx.gif",
            "https://media.discordapp.net/attachments/434128829821222923/811449277607837716/lewut.gif"]

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