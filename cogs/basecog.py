import discord, random
from discord.ext import commands

#//people
muffin = 488423352206229505
dj = 373369932303433728

class gifcog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gif(self, ctx, arg):
        if ctx.author.id == muffin or ctx.author.id == dj:
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
                    await ctx.send(x)
            elif arg == "lovelyzjin":
                for x in self.bot.ljin_gif:
                    await ctx.send(x)
            elif arg == "sujeong":
                for x in self.bot.sujeong_gif:
                    await ctx.send(x)
        #.Mamamoo
            elif arg == "mamamoo":
                for x in self.bot.mamamoo_gif:
                    await ctx.send(x)
            elif arg == "moonbyul":
                for x in self.bot.moonbyul:
                    await ctx.send(x)
            elif arg == "wheein":
                for x in self.bot.wheein_gif:
                    await ctx.send(x)
            elif arg == "hwasa":
                for x in self.bot.hwasa_gif:
                    await ctx.send(x)
            elif arg == "solar":
                for x in self.bot.solar_gif:
                    await ctx.send(x)
        #.Red Velvet
            elif arg == "Irene":
                for x in self.bot.irene_gif:
                    await ctx.send(x)
            elif arg == "seulgi":
                for x in self.bot.seulgi_gif:
                    await ctx.send(x)
            elif arg == "wendy":
                for x in self.bot.wendy_gif:
                    await ctx.send(x)
            elif arg == "yeri":
                for x in self.bot.yeri_gif:
                    await ctx.send(x)
            elif arg == "joy":
                for x in self.bot.joy_gif:
                    await ctx.send(x)
        #.Stray Kids
            elif arg == "felix":
                for x in self.bot.felix_gif:
                    await ctx.send(x)
            elif arg == "straykidshyunjin":
                for x in self.bot.shyunjin_gif:
                    await ctx.send(x)
            elif arg == "bangchan":
                for x in self.bot.bangchan_gif:
                    await ctx.send(x)
            elif arg == "leeknow":
                for x in self.bot.leeknow_gif:
                    await ctx.send(x)
            elif arg == "han":
                for x in self.bot.han_gif:
                    await ctx.send(x)
            elif arg == "jeongin":
                for x in self.bot.jeongin_gif:
                    await ctx.send(x)
            elif arg == "seungmin":
                for x in self.bot.seungmin_gif:
                    await ctx.send(x)
        #.Twice
            elif arg == "mina":
                for x in self.bot.mina_gif:
                    await ctx.send(x)
            elif arg == "sana":
                for x in self.bot.sana_gif:
                    await ctx.send(x)
            elif arg == "momo":
                for x in self.bot.momo_gif:
                    await ctx.send(x)
            elif arg == "jeongyeon":
                for x in self.bot.jeongyeon_gif:
                    await ctx.send(x)
            elif arg == "tzuyu":
                for x in self.bot.tzuyu_gif:
                    await ctx.send(x)
            elif arg == "nayeon":
                for x in self.bot.nayeon_gif:
                    await ctx.send(x)
            elif arg == "jihyo":
                for x in self.bot.jihyo_gif:
                    await ctx.send(x)
            elif arg == "chaeyoung":
                for x in self.bot.chaeyoung_gif:
                    await ctx.send(x)
        #.TXT
            #//not technically in yet
        #.Soloists
            elif arg == "natty":
                for x in self.bot.natty_gif:
                    await ctx.send(x)
            elif arg == "alexa":
                for x in self.bot.alexa_gif:
                    await ctx.send(x)
            elif arg == "chungha":
                for x in self.bot.chungha_gif:
                    await ctx.send(x)
            elif arg == "iu":
                for x in self.bot.iu_gif:
                    await ctx.send(x)
            elif arg == "somi":
                for x in self.bot.somi_gif:
                    await ctx.send(x)
            elif arg == "yukika":
                for x in self.bot.yukika_gif:
                    await ctx.send(x)
        #.Misc
            elif arg == "yeeun":
                for x in self.bot.yeeun_gif:
                    await ctx.send(x)
            elif arg == "lucas":
                for x in self.bot.lucas_gif:
                    await ctx.send(x)
            elif arg == "ses":
                for x in self.bot.ses_mv:
                    await ctx.send(x)
            elif arg == "cl":
                for x in self.bot.cl_gif:
                    await ctx.send(x)
            elif arg == "kiki":
                for x in self.bot.kiki_gif:
                    await ctx.send(x)
            elif arg == "taemin":
                for x in self.bot.taemin_gif:
                    await ctx.send(x)
            elif arg == "lucas":
                for x in self.bot.lucas_gif:
                    await ctx.send(x)
            elif arg == "krystal":
                for x in self.bot.krystal_gif:
                    await ctx.send(x)
            elif arg == "jessica":
                for x in self.bot.jessica_gif:
                    await ctx.send(x)

        #.else
            else:
                await ctx.send(f'don\'t write code when you\'re tired smh my head')
        else:
            await ctx.send(f'no')

def setup(client):
    client.add_cog(gifcog(client))