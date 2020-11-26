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
mae = 492769416610840586
rith = 346724857725059075

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

        #9
        self.winter_gif = ["https://tenor.com/view/aespa-archive_aespa-winter-aespa-winter-winter-aespa-gif-19207739",
            "https://tenor.com/view/aespa-winter-aespa-winter-aespa-kim-minjeong-kim-minjeong-gif-19029912",
            "https://tenor.com/view/aespa-%EC%97%90%EC%8A%A4%ED%8C%8C-%EC%9C%88%ED%84%B0-winter-gif-19207490",
            "https://tenor.com/view/archive_aespa-aespa-winter-aespa-winter-minjeong-gif-19138516",
            "https://tenor.com/view/winter-aespa-aespa-gif-19226090",
            "https://tenor.com/view/winter-aespa-aespa-gif-19323697",
            "https://cdn.discordapp.com/attachments/771238115255255060/781388912189898752/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781388912873832473/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/781388914480513064/image2.gif"]

        #2
        self.ningning_gif = ["https://cdn.discordapp.com/attachments/747275528993636424/781391569986125824/7226125c-1e30-4c1d-b3a9-f6a71db55fad.gif",
        "https://cdn.discordapp.com/attachments/747275528993636424/781391570829836308/3ee3defb-5472-48b9-b5ef-743984c6996d.gif"]

    @commands.command()
    async def giselle(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{k8}>, <@{rith}> <@!{ctx.author.id}> is talking about Giselle :crescent_moon: ')
                await ctx.send(random.choice(self.giselle_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Giselle :crescent_moon:')
            await ctx.send(random.choice(self.giselle_gif))
            await ctx.message.delete()
    
    @commands.command()
    async def winter(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{k8}>, <@{mae}>, <@{rith}> <@!{ctx.author.id}> is talking about Winter :star: ')
                await ctx.send(random.choice(self.winter_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Winter :star:')
            await ctx.send(random.choice(self.winter_gif))
            await ctx.message.delete()

    @commands.command()
    async def ningning(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{k8}>, <@{mae}>, <@{rith}> <@!{ctx.author.id}> is talking about Ningning :star: ')
                await ctx.send(random.choice(self.ningning_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Ningning :star:')
            await ctx.send(random.choice(self.ningning_gif))
            await ctx.message.delete()





def setup(client):
    client.add_cog(aespaPings(client))