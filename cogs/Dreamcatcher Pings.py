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

class DreamCatcherPings(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

        #5
        self.bot.jiu_gif = ["https://tenor.com/view/onex-1x-jiu-hawt-kim-minji-hawt-jiu-gif-18812596",
            "https://cdn.discordapp.com/attachments/771238115255255060/785294061132709930/image0.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/785294061996605470/image1.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/785294062764818452/image2.gif",
            "https://cdn.discordapp.com/attachments/771238115255255060/785294063871721472/image3.gif"]

    @commands.command()
    async def jiu(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@{k8}>, <@!{ctx.author.id}> is talking about JiU :rabbit: ')
                await ctx.send(random.choice(self.bot.jiu_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about JiU :rabbit:')
            await ctx.send(random.choice(self.bot.jiu_gif))
            await ctx.message.delete()

def setup(client):
    client.add_cog(DreamCatcherPings(client))