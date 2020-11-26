import discord, random, os
from discord.ext import commands

#//servers
jst = 735713250225815615
luminary = 758468592957521972
sadboi = 642497143801905190

#=channels
#.luminary bot-commands
kbotcom = 764610881513324574

class gamerPings(commands.Cog):

    def __init__(self, client):
        self.client = client

        #5
        self.mina_gif = ["https://tenor.com/NUon.gif",
            "https://tenor.com/4vrC.gif",
            "https://tenor.com/HydV.gif",
            "https://tenor.com/brQ1g.gif",
            "https://media.giphy.com/media/qzuGfHYC152dG/giphy.gif"]

        #7
        self.sana_gif = ["https://tenor.com/view/sana-twice-kitty-dance-kpop-gif-17314571",
            "https://media.giphy.com/media/xUySTXXuWvIVDggisg/giphy.gif",
            "https://tenor.com/view/sana-sana-twice-twice-sana-minatozaki-sana-gif-18564320",
            "https://tenor.com/view/sana-twice-heart-minatozaki-jpop-gif-10758695",
            "https://tenor.com/view/twice-shyshyshy-sana-dance-cute-gif-9784878",
            "https://tenor.com/view/sanapinkhair-sana-twice-sana-gif-18677676",
            "https://tenor.com/view/samichae-sana-twice-serious-gif-15019560"]

        #5
        self.momo_gif = ["https://tenor.com/UZ2D.gif",
            "https://tenor.com/boSu5.gif",
            "https://tenor.com/brfIg.gif",
            "https://media.giphy.com/media/LOQdYUQeQ1EXUP9loM/giphy.gif",
            "https://media.giphy.com/media/emLsFpAymOfaDgQ7qm/giphy.gif"]

        #5
        self.jeongyeon_gif = ["https://tenor.com/bgvYS.gif",
            "https://tenor.com/bm9Bh.gif",
            "https://media.giphy.com/media/QxYGmXN0vs2W6oHAO2/giphy.gif",
            "https://media.giphy.com/media/Pm3E3SsR3TSeT0eI6p/giphy.gif",
            "https://media.giphy.com/media/jOyCT02EvfnMc7trkh/giphy.gif"]
        
        #5
        self.tzuyu_gif = ["https://media.giphy.com/media/sKdL5e5zah0gE/giphy.gif",
            "https://media.giphy.com/media/jmphxHznc7wBmsuaW1/giphy.gif",
            "https://tenor.com/5MSV.gif",
            "https://tenor.com/Fguv.gif",
            "https://tenor.com/bsSaJ.gif"]

        #6
        self.nayeon_gif = ["https://tenor.com/9b5w.gif",
            "https://tenor.com/YChI.gif",
            "https://tenor.com/bs6Qy.gif",
            "https://media.giphy.com/media/gg3XU0ggfN7B0tlHnw/giphy.gif",
            "https://media.giphy.com/media/URvyQpZe0uoCT6jHo8/giphy.gif",
            "https://media.giphy.com/media/h7dxG65XwW00aBVkBc/giphy.gif"]

        #5
        self.dahyun_gif = ["https://tenor.com/zEfV.gif",
            "https://tenor.com/ZKRA.gif",
            "https://tenor.com/brQ06.gif",
            "https://media.giphy.com/media/gLcbZ01uqIOZIsBWlC/giphy.gif",
            "https://tenor.com/bd1b8.gif"]

        #5
        self.jihyo_gif = ["https://media.giphy.com/media/Ph6A5WjBAI3981PAsf/giphy.gif",
            "https://tenor.com/bnZ6r.gif",
            "https://tenor.com/bbKLS.gif",
            "https://tenor.com/brGhA.gif",
            "https://tenor.com/brT8L.gif"]

        #6
        self.chaeyoung_gif = ["https://tenor.com/view/chaeyoung-twice-kpop-jyp-jypnation-gif-14436666",
            "https://media.giphy.com/media/xUySTt5f5AmRUBgdUI/giphy.gif",
            "https://media.giphy.com/media/lptOHczNAFD1G79Ofq/giphy.gif",
            "https://media.giphy.com/media/Qy2WthVCTLkeT1gZLS/giphy.gif",
            "https://tenor.com/XiHw.gif",
            "https://tenor.com/bn9Lf.gif"]


    @commands.command()
    async def mina(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Mina :heart:')
                await ctx.send(random.choice(self.mina_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Mina :heart:')
            await ctx.send(random.choice(self.mina_gif))
            await ctx.message.delete()
    
    @commands.command()
    async def sana(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Sana :heart:')
                await ctx.send(random.choice(self.sana_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Sana :heart:')
            await ctx.send(random.choice(self.sana_gif))
            await ctx.message.delete()

    @commands.command()
    async def momo(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Momo :heart:')
                await ctx.send(random.choice(self.momo_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Momo :heart:')
            await ctx.send(random.choice(self.momo_gif))
            await ctx.message.delete()
    
    @commands.command()
    async def jeongyeon(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jeongyeon :heart:')
                await ctx.send(random.choice(self.jeongyeon_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jeongyeon :heart:')
            await ctx.send(random.choice(self.jeongyeon_gif))
            await ctx.message.delete()

    @commands.command()
    async def tzuyu(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Tzuyu :heart:')
                await ctx.send(random.choice(self.tzuyu_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Tzuyu :heart:')
            await ctx.send(random.choice(self.tzuyu_gif))
            await ctx.message.delete()

    @commands.command()
    async def nayeon(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Nayeon :heart:')
                await ctx.send(random.choice(self.nayeon_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Nayeon :heart:')
            await ctx.send(random.choice(self.nayeon_gif))
            await ctx.message.delete()

    @commands.command()
    async def dahyun(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Dahyun :heart:')
                await ctx.send(random.choice(self.dahyun_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Dahyun :heart:')
            await ctx.send(random.choice(self.dahyun_gif))
            await ctx.message.delete()

    @commands.command()
    async def jihyo(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Jihyo :heart:')
                await ctx.send(random.choice(self.jihyo_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Jihyo :heart:')
            await ctx.send(random.choice(self.jihyo_gif))
            await ctx.message.delete()

    @commands.command()
    async def chaeyoung(self, ctx):
        if ctx.guild.id == luminary:
            if ctx.channel.id == kbotcom:
                await ctx.send(f'<@!{ctx.author.id}> is talking about Chaeyoung :heart:')
                await ctx.send(random.choice(self.chaeyoung_gif))
                await ctx.message.delete()
            else:
                await ctx.send(content=f'Wrong channel <@!{ctx.author.id}>! Go to <#764610881513324574>', delete_after=2)
                await ctx.message.delete()
        else:
            await ctx.send(f'<@!{ctx.author.id}> is talking about Chaeyoung :heart:')
            await ctx.send(random.choice(self.chaeyoung_gif))
            await ctx.message.delete()



def setup(client):
    client.add_cog(gamerPings(client))