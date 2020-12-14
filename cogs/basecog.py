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
    #.Blackpink 
        elif arg == "jennie":
            for x in self.bot.jennie_gif:
                await ctx.send(x)
        elif arg == "rose":
            for x in self.bot.rose_gif:
                await ctx.send(x)
        elif arg == "lisa":
            for x in self.bot.lisa_gif:
                await ctx.send(x)
        elif arg == "blackpinkjisoo":
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
    #.Breamcatcher
        elif arg == "jiu":
            for x in self.bot.jiu_gif:
                await ctx.send(x)
    #.Enhypen
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
    #.Everglow
        elif arg == "eu":
            for x in self.bot.eu_gif:
                await ctx.send(x)
        elif arg == "mia":
            for x in self.bot.mia_gif:
                await ctx.send(x)
        elif arg == "yiren":
            for x in self.bot.yiren_gif:
                await ctx.send(x)
        elif arg == "aisha":
            for x in self.bot.aisha_gif:
                await ctx.send(x)
        elif arg == "onda":
            for x in self.bot.onda_gif:
                await ctx.send(x)
        elif arg == "sihyeon":
            for x in self.bot.sihyeon_gif:
                await ctx.send(x) 
    #.EXID
        elif arg == "hani":
            for x in self.bot.hani_gif:
                await ctx.send(x)
        elif arg == "jeonghwa":
            for x in self.bot.jeonghwa_gif:
                await ctx.send(x)
        elif arg == "le":
            for x in self.bot.le_gif:
                await ctx.send(x)
        elif arg == "solji":
            for x in self.bot.solji_gif:
                await ctx.send(x)
        elif arg == "hyelin":
            for x in self.bot.hyelin_gif:
                await ctx.send(x)
    #.Gidle
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
    #.Itzy
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
    #.Izone
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
        elif arg == "hyunjin":
            for x in self.bot.hyunjin_gif:
                await ctx.send(x)
        elif arg == "haseul":
            for x in self.bot.haseul.gif:
                await ctx.send(x)
        elif arg == "vivi":
            for x in self.bot.vivi_gif:
                await ctx.send(x)
        elif arg == "yeojin":
            for x in self.bot.yeojin_gif:
                await ctx.send(x)
        elif arg == "kimlip":
            for x in self.bot.kimlip_gif:
                await ctx.send(x)
        elif arg == "jinsoul":
            for x in self.bot.jinsoul_gif:
                await ctx.send(x)
        elif arg == "choerry":
            for x in self.bot.choerry_gif:
                await ctx.send(x)
        elif arg == "yves":
            for x in self.bot.yves_gif:
                await ctx.send(x)
        elif arg == "chuu":
            for x in self.bot.chuu_gif:
                await ctx.send(x)
        elif arg == "gowon":
            for x in self.bot.gowon_gif:
                await ctx.send(x)
        elif arg == "oliviahye":
            for x in self.bot.oliviahye_gif:
                await ctx.send(x)
    #.Lovelyz
        elif arg == "yein":
            for x in self.bot.yein_gif:
                await ctx.send(x)
        elif arg == "kei":
            for x in self.bot.kei_gif:
                await ctx.send(x)
        elif arg == "lovelyzjisoo":
            for x in self.bot.ljisoo_gif:
                await ctx.send(x)
        elif arg == "babysoul":
            for x in self.bot.babysoul_gif:
                await ctx.send(x)
        elif arg == "mijoo":
            for x in self.bot.mijoo_gif:
                await ctx.senc(x)
        elif arg == "jiae":
            for x in self.bot.jiae_gif:
                await ctx.senc(x)
        elif arg == "lovelyzjin":
            for x in self.bot.ljin_gif:
                await ctx.send(x)
        elif arg == "sujeong":
            for x in self.bot.sujeong_gif:
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