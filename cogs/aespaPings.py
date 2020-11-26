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
k8 = 573974040679809044

class aespaPings(commands.Cog):

    def __init__(self, client):
        self.client = client

        #7
        self.giselle_gif = ["https://cdn.discordapp.com/attachments/771238115255255060/781338667973214208/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338668513886208/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338669524975616/image2.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338670694531072/image3.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338671202304087/image4.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338671714271282/image5.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781338672481173514/image6.gif"]

        #
        self.winter_gif = []

    #giselle command for k8
    @commands.command()
    async def giselle(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{k8}>, <@!{ctx.author.id}> is talking about Giselle :crescent_moon: ')
                await ctx.send(random.choice(self.giselle_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Giselle :crescent_moon:')
            await ctx.send(random.choice(self.giselle_gif))
            await ctx.message.delete()
    
    #winter command for k8
    @commands.command()
    async def winter(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{k8}>, <@!{ctx.author.id}> is talking about Winter :star: ')
                await ctx.send(random.choice(self.winter_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Winter :star:')
            await ctx.send(random.choice(self.winter_gif))
            await ctx.message.delete()






def setup(client):
    client.add_cog(aespaPings(client))