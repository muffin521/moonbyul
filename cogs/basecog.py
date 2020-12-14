import discord, random
from discord.ext import commands



class gifcog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def gif(self, ctx, arg):
    #.aespa
        if arg == "giselle":
            for x in self.bot.giselle_gif:
                await ctx.send(x)
        elif arg == "winter":
            for x in self.bot.winter_gif:
                await ctx.send(x)
        elif arg == "ningning":
            for x in self.bot.ningning_gif:
                await ctx.send(x)
        elif arg == "karina":
            for x in self.bot.karina_gif:
                await ctx.send(x)
    #.blackpink 
        elif arg == "jennie":
            for x in self.bot.jennie_gif:
                await ctx.send(x)
        elif arg == "rose":
            for x in self.bot.rose_gif:
                await ctx.send(x)
        elif arg == "lisa":
            for x in self.bot.lisa_gif:
                await ctx.send(x)
        elif arg == "jisoo":
            for x in self.bot.jisoo_gif:
                await ctx.send(x)
    #.BTS
        elif arg == "v":
            for x in self.bot.v_gif:
                await ctx.send(x)
        elif arg == "suga":
            for x in self.bot.suga_gif:
                await ctx.send(x)
        elif arg == "jhope":
            for x in self.bot.jhope_gif:
                await ctx.send(x)
        elif arg == "jungkook":
            for x in self.bot.jungkook_gif:
                await ctx.send(x)
        elif arg == "btsjin":
            for x in self.bot.btsjin_gif:
                await ctx.send(x)
        elif arg == "jimin":
            for x in self.bot.jimin_gif:
                await ctx.send(x)
        elif arg == "rm":
            for x in self.bot.rm_gif:
                await ctx.send(x)
    #.dreamcatcher
        elif arg == "jiu":
            for x in self.bot.jiu_gif:
                await ctx.send(x)
    #.enhypen
        elif arg == "sunoo":
            for x in self.bot.sunoo_gif:
                await ctx.send(x)
        elif arg == "sunghoon":
            for x in self.bot.sunghoon_gif:
                await ctx.send(x)
        elif arg == "jake":
            for x in self.bot.jake_gif:
                await ctx.send(x)
        elif arg == "jungwon":
            for x in self.bot.jungwon_gif:
                await ctx.send(x)
        elif arg == "heeseung":
            for x in self.bot.heeseung_gif:
                await ctx.send(x)
        elif arg == "jay":
            for x in self.bot.jay_gif:
                await ctx.send(x)
        elif arg == "niki":
            for x in self.bot.niki_gif:
                await ctx.send(x)
    #.gidle
        elif arg == "minnie":
            for x in self.bot.minnie_gif:
                await ctx.send(x)
        elif arg == "miyeon":
            for x in self.bot.miyeon_gif:
                await ctx.send(x)
        elif arg == "shuhua":
            for x in self.bot.shuhua_gif:
                await ctx.send(x)
        elif arg == "soojin":
            for x in self.bot.soojin_gif:
                await ctx.send(x)
        elif arg == "soyeon":
            for x in self.bot.soyeon_gif:
                await ctx.send(x)
        elif arg == "yuqi":
            for x in self.bot.yuqi_gif:
                await ctx.send(x)
    #.itzy
        elif arg == "yeji":
            for x in self.bot.yeji_gif:
                await ctx.send(x)
        elif arg == "ryunjin":
            for x in self.bot.ryunjin_gif:
                await ctx.send(x)
        elif arg == "chaeryeong":
            for x in self.bot.chaeryeong_gif:
                await ctx.send(x)
        elif arg == "yuna":
            for x in self.bot.yuna_gif:
                await ctx.send(x)
        elif arg == "lia":
            for x in self.bot.lia_gif:
                await ctx.send(x)
    #.izone
        elif arg == "sakura":
            for x in self.bot.sakura_gif:
                await ctx.send(x)
        elif arg == "yuri":
            for x in self.bot.yuri_gif:
                await ctx.send(x)
        elif arg == "chaeyeon":
            for x in self.bot.chaeyeon_gif:
                await ctx.send(x)
        elif arg == "minju":
            for x in self.bot.minju_gif:
                await ctx.send(x)
        elif arg == "wonyoung":
            for x in self.bot.wonyoung_gif:
                await ctx.send(x)
        elif arg == "hyewon":
            for x in self.bot.hyewon_gif:
                await ctx.send(x)
        elif arg == "chaewon":
            for x in self.bot.chaewon_gif:
                await ctx.send(x)
        elif arg == "yujin":
            for x in self.bot.yujin_gif:
                await ctx.send(x)
        elif arg == "yena":
            for x in self.bot.yena_gif:
                await ctx.send(x)
        elif arg == "eunbi":
            for x in self.bot.eunbi_gif:
                await ctx.send(x)
        elif arg == "nako":
            for x in self.bot.nako_gif:
                await ctx.send(x)
        elif arg == "hitomi":
            for x in self.bot.hitomi_gif:
                await ctx.send(x)
    #.Loona
        elif arg == "heejin":
            for x in self.bot.heejin_gif:
                await ctx.send(x)

    #     # elif arg == "soyeon":
    #     #     for x in self.client.Gidle.soyeon_gif:
    #     #         await ctx.send(x)
    #     # if arg == "kiki":
    #     #     for x in self.client.PleCommands.kiki_gif:
    #     #         await ctx.send(x)
    #     # elif arg == "sakura":
    #     #     for x in self.client.IzonePings.sakura_gif:
    #     #         await ctx.send(x)
        else:
            await ctx.send(f'help')

def setup(client):
    client.add_cog(gifcog(client))