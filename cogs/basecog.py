import discord, random
from discord.ext import commands



class gifcog(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.client.get_cog("aespa")
        self.client.get_cog("BlackpinkPings")
        self.client.get_cog("BTSPings")
        self.client.get_cog("DreamcatcherPings")
        self.client.get_cog("EnhypenPings")
        self.client.get_cog("gamerCommands")
        self.client.get_cog("Gidle")
        self.client.get_cog("ItzyPings")
        self.client.get_cog("IzonePings")
        self.client.get_cog("KpopPings")
        self.client.get_cog("LoonaPings")
        self.client.get_cog("LovelyzPings")
        self.client.get_cog("MaePings")
        self.client.get_cog("MamamooPIngs")
        self.client.get_cog("PleCommands")
        self.client.get_cog("RedVelvetPings")
        self.client.get_cog("SoloPings")
        self.client.get_cog("StrayKids")
        self.client.get_cog("Twice")
        self.client.get_cog("TXT")

    @commands.command()
    @commands.is_owner()
    async def gif(self, ctx, arg):
        if arg == "giselle":
            for x in self.client.aespa.giselle_gif:
                await ctx.send(x)
        elif arg == "winter":
            for x in self.client.aespa.winter_gif:
                await ctx.send(x)
        elif arg == "ningning":
            for x in self.client.aespa.ningning_gif:
                await ctx.send(x)
        elif arg == "karina":
            for x in self.client.aespa.karina_gif:
                await ctx.send(x)
        elif arg == "soyeon":
            for x in self.client.Gidle.soyeon_gif:
                await ctx.send(x)
        if arg == "kiki":
            for x in self.client.PleCommands.kiki_gif:
                await ctx.send(x)
        elif arg == "sakura":
            for x in self.client.IzonePings.sakura_gif:
                await ctx.send(x)
        await ctx.send(f'help')

def setup(client):
    client.add_cog(gifcog(client))