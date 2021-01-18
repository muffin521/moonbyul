import discord, random, datetime
from discord.ext import commands
from datetime import datetime

        #= P1Harmony

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

class twoneone(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        self.bot.p1harmony_intak_gif = ["https://cdn.discordapp.com/attachments/800206337073479690/800261657557074000/image0.gif",
            "https://cdn.discordapp.com/attachments/800206337073479690/800261657880166400/image1.gif",
            "https://cdn.discordapp.com/attachments/800206337073479690/800261658508394516/image2.gif",
            "https://cdn.discordapp.com/attachments/800206337073479690/800261658890731550/image3.gif",
            "https://cdn.discordapp.com/attachments/800206337073479690/800261758714380358/image0.gif",
            "https://cdn.discordapp.com/attachments/800206337073479690/800261759302500392/image1.gif"]

        self.bot.p1harmony_jiung_gif = ["https://cdn.discordapp.com/attachments/800206376210661406/800262168904859668/image0.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262169299910686/image1.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262170029195304/image2.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262170419396628/image3.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262170691764244/image4.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262170952466452/image5.gif",
            "https://cdn.discordapp.com/attachments/800206376210661406/800262218733322270/image0.gif"]

        self.bot.p1harmony_jongseob_gif = ["https://cdn.discordapp.com/attachments/800206414597455872/800262445016809472/image0.gif",
            "https://cdn.discordapp.com/attachments/800206414597455872/800262445314211850/image1.gif",
            "https://cdn.discordapp.com/attachments/800206414597455872/800262554202931261/image0.gif",
            "https://cdn.discordapp.com/attachments/800206414597455872/800262587488534558/image0.gif",
            "https://cdn.discordapp.com/attachments/800206414597455872/800262610305024040/image0.gif"]

        self.bot.p1harmony_keeho_gif = ["https://cdn.discordapp.com/attachments/800206480837574666/800262794280304661/image0.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800262794531569684/image1.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800262795144724480/image2.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800262795446845460/image3.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800262908646522880/image0.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800262909077749760/image1.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800262909682253845/image2.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800262909984505856/image3.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800263019380342804/image0.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800263019929665566/image1.gif",
            "https://cdn.discordapp.com/attachments/800206480837574666/800263020420005908/image2.gif"]

        self.bot.p1harmony_soul_gif = ["https://cdn.discordapp.com/attachments/800206684193685504/800263221390213170/image0.gif",
            "https://cdn.discordapp.com/attachments/800206684193685504/800263221792473088/image1.gif",
            "https://cdn.discordapp.com/attachments/800206684193685504/800263222166814730/image2.gif",
            "https://cdn.discordapp.com/attachments/800206684193685504/800263222514810880/image3.gif",
            "https://cdn.discordapp.com/attachments/800206684193685504/800263223194550272/image4.gif",
            "https://cdn.discordapp.com/attachments/800206684193685504/800263416635588658/image0.gif",
            "https://cdn.discordapp.com/attachments/800206684193685504/800263417167609886/image1.gif",
            "https://cdn.discordapp.com/attachments/800206684193685504/800263417604079636/image2.gif",
            "https://cdn.discordapp.com/attachments/800206684193685504/800263460730437632/image0.gif"]

        self.bot.p1harmony_theo_gif = ["https://cdn.discordapp.com/attachments/800206797604519936/800263698639487016/image0.gif",
            "https://cdn.discordapp.com/attachments/800206797604519936/800263825638293504/image0.gif",
            "https://cdn.discordapp.com/attachments/800206797604519936/800263826138202113/image1.gif",
            "https://cdn.discordapp.com/attachments/800206797604519936/800263827073007616/image2.gif",
            "https://cdn.discordapp.com/attachments/800206797604519936/800263827786432512/image3.gif",
            "https://cdn.discordapp.com/attachments/800206797604519936/800264225443676210/image0.gif",
            "https://cdn.discordapp.com/attachments/800206797604519936/800264226001387540/image1.gif",
            "https://cdn.discordapp.com/attachments/800206797604519936/800264226445852693/image2.gif",
            "https://cdn.discordapp.com/attachments/800206797604519936/800264279206264842/image0.gif"]

    @commands.command(aliases = ['p1h'])
    async def p1harmony(self, ctx, arg):
        now = datetime.now()
        channel = ctx.bot.get_channel(logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [P1Harmony {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}]`" )
        if arg == "intak":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Intak :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_intak_gif))
                await ctx.message.delete()
        elif arg == "jiung":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jiung :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_jiung_gif))
                await ctx.message.delete()
        elif arg == "jongseob":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jongseob :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_jongseob_gif))
                await ctx.message.delete()
        elif arg == "keeho":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Keeho :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_intak_gif))
                await ctx.message.delete()
        elif arg == "soul":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Soul :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_soul_gif))
                await ctx.message.delete()
        elif arg == "theo":
            if ctx.guild.id == luminary and ctx.channel.id != kbotcom:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#{kbotcom}>', delete_after=2)
                await ctx.message.delete()
            else:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Theo :rotating_light:')
                await ctx.send(random.choice(self.bot.p1harmony_theo_gif))
                await ctx.message.delete()

    
def setup(client):
    client.add_cog(twoneone(client))