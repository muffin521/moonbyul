import discord, random, os
from discord.ext import commands


class secret(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.psy_gif = ["https://tenor.com/view/psy-dance-horses-gangnam-style-music-gif-5419832",
        "https://tenor.com/view/psy-daddy-dance-dancing-grandpa-gif-5064834",
        "https://tenor.com/view/music-music-video-psy-gentleman-dance-gif-3459771",
        "https://tenor.com/view/psy-gentleman-gian-hip-sway-shaking-gif-4566558",
        "https://tenor.com/view/snoop-drinking-psy-gif-10281800"]


    @commands.command()
    async def mariah(self, ctx):
        if (ctx.author.id == 690313474265710749):
            await ctx.send(f"Mr Mullin's favourite physics student is <@690313474265710749>")
            await ctx.message.delete()
        elif(ctx.author.id == 488423352206229505):
            await ctx.send(f"<@488423352206229505> is Mariah's favourite :partying_face:")
            await ctx.message.delete()
    
    @commands.command()
    async def max(self, ctx):
        await ctx.send(f'A gift <@233442758088589314>')
        await ctx.send(random.choice(self.psy_gif))
        await ctx.message.delete()

    @commands.command()
    async def cam(self, ctx):
        if (ctx.author.id == 380455128299208706):
            await ctx.send(f'https://youtu.be/rRPQs_kM_nw')
            await ctx.message.delete()
        # if (ctx.author.id == 488423352206229505):
        #     await ctx.send(f'Dance Monkey Dance <@380455128299208706> :monkey:')
        #     await ctx.message.delete()
        
def setup(client):
    client.add_cog(secret(client))