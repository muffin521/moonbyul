import discord, random
from discord.ext import commands

#//people
muffin = 488423352206229505
dj = 373369932303433728
k8 = 573974040679809044

class gifcog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gif(self, ctx, *, arg):
        if ctx.author.id == muffin or ctx.author.id == dj or ctx.author.id == k8:
        #.2ne1
            if arg == "2ne1 cl":
                for x in self.bot.cl_gif:
                    await ctx.send(x)
            elif arg == "2ne1 dara" or arg == "2ne1 sandara":
                for x in self.bot.dara_gif:
                    await ctx.send(x)
            elif arg == "2ne1 minzy" or arg == "2ne1 minji":
                for x in self.bot.minzy_gif:
                    await ctx.send(x)
            elif arg == "2ne1 park bom" or arg == "2ne1 bom":
                for x in self.bot.parkbom_gif:
                    await ctx.send(x)
            elif arg == "2ne1":
                for x in self.bot.twoneone_gif:
                    await ctx.send(x)
        #.aespa
            elif arg == "aespa giselle":
                for x in self.bot.giselle_gif:
                    await ctx.send(x)
            elif arg == "aespa winter":
                for x in self.bot.winter_gif:
                    await ctx.send(x)
            elif arg == "aespa ningning":
                for x in self.bot.ningning_gif:
                    await ctx.send(x)
            elif arg == "aespa karina":
                for x in self.bot.karina_gif:
                    await ctx.send(x)
        #.April
            elif arg == "april chaekyung":
                for x in self.bot.april_chaekyung_gif:
                    await ctx.send(x)
            elif arg == "april chaewon":
                for x in self.bot.april_chaewon_gif:
                    await ctx.send(x)
            elif arg == "april naeun":
                for x in self.bot.april_naeun_gif:
                    await ctx.send(x)
            elif arg == "april yena":
                for x in self.bot.april_yena_gif:
                    await ctx.send(x)
            elif arg == "april rachel":
                for x in self.bot.april_rachel_gif:
                    await ctx.send(x)
            elif arg == "april jinsol":
                for x in self.bot.april_jinsol_gif:
                    await ctx.send(x)
            elif arg == "april hyunjoo":
                for x in self.bot.april_hyunjoo_gif:
                    await ctx.send(x)
        #.Blackpink 
            elif arg == "blackpink jennie":
                for x in self.bot.jennie_gif:
                    await ctx.send(x)
            elif arg == "blackpink rose":
                for x in self.bot.rose_gif:
                    await ctx.send(x)
            elif arg == "blackpink lisa":
                for x in self.bot.lisa_gif:
                    await ctx.send(x)
            elif arg == "blackpink jisoo":
                for x in self.bot.jisoo_gif:
                    await ctx.send(x)
        #.The Boyz
            elif arg == "the boyz kevin":
                for x in self.bot.theboyz_kevin_gif:
                    await ctx.send(x)
            elif arg == "the boyz sangyeon":
                for x in self.bot.theboyz_sangyeon_gif:
                    await ctx.send(x)
            elif arg == "the boyz jacob":
                for x in self.bot.theboyz_jacob_gif:
                    await ctx.send(x)
            elif arg == "the boyz younghoon":
                for x in self.bot.theboyz_younghoon_gif:
                    await ctx.send(x)
            elif arg == "the boyz hyunjae":
                for x in self.bot.theboyz_hyunjae_gif:
                    await ctx.send(x)
            elif arg == "the boyz juyeon":
                for x in self.bot.theboyz_juyeon_gif:
                    await ctx.send(x)
            elif arg == "the boyz new":
                for x in self.bot.theboyz_new_gif:
                    await ctx.send(x)
            elif arg == "the boyz q":
                for x in self.bot.theboyz_q_gif:
                    await ctx.send(x)
            elif arg == "the boyz haknyeon":
                for x in self.bot.theboyz_haknyeon_gif:
                    await ctx.send(x)
            elif arg == "the boyz sunwoo":
                for x in self.bot.theboyz_sunwoo_gif:
                    await ctx.send(x)
            elif arg == "the boyz eric":
                for x in self.bot.theboyz_eric_gif:
                    await ctx.send(x)
        #.BTS
            elif arg == "bts v":
                for x in self.bot.v_gif:
                    await ctx.send(x)
            elif arg == "bts suga":
                for x in self.bot.suga_gif:
                    await ctx.send(x)
            elif arg == "bts jhope":
                for x in self.bot.jhope_gif:
                    await ctx.send(x)
            elif arg == "bts jungkook":
                for x in self.bot.jungkook_gif:
                    await ctx.send(x)
            elif arg == "bts jin":
                for x in self.bot.btsjin_gif:
                    await ctx.send(x)
            elif arg == "bts jimin":
                for x in self.bot.jimin_gif:
                    await ctx.send(x)
            elif arg == "bts rm":
                for x in self.bot.rm_gif:
                    await ctx.send(x)
        #.Cherry Bullet
            elif arg == "cherry bullet bora":
                for x in self.bot.cherrybullet_bora_gif:
                    await ctx.send(x)
            elif arg == "cherry bullet chaerin":
                for x in self.bot.cherrybullet_chaerin_gif:
                    await ctx.send(x)
            elif arg == "cherry bullet haeyoon":
                for x in self.bot.cherrybullet_haeyoon_gif:
                    await ctx.send(x)
            elif arg == "cherry bullet jiwon":
                for x in self.bot.cherrybullet_jiwon_gif:
                    await ctx.send(x)
            elif arg == "cherry bullet kokoro":
                for x in self.bot.cherrybullet_kokoro_gif:
                    await ctx.send(x)
            elif arg == "cherry bullet linlin":
                for x in self.bot.cherrybullet_linlin_gif:
                    await ctx.send(x)
            elif arg == "cherry bullet may":
                for x in self.bot.cherrybullet_may_gif:
                    await ctx.send(x)
            elif arg == "cherry bullet mirae":
                for x in self.bot.cherrybullet_mirae_gif:
                    await ctx.send(x)
            elif arg == "cherry bullet remi":
                for x in self.bot.cherrybullet_remi_gif:
                    await ctx.send(x)
            elif arg == "cherry bullet yuju":
                for x in self.bot.cherrybullet_yuju_gif:
                    await ctx.send(x)
        #.CLC
            elif arg == "clc sorn":
                for x in self.bot.clc_sorn_gif:
                    await ctx.send(x)
            elif arg == "clc yeeun":
                for x in self.bot.clc_yeeun_gif:
                    await ctx.send(x)
            elif arg == "clc seunghee":
                for x in self.bot.clc_seunghee_gif:
                    await ctx.send(x)
            elif arg == "clc elkie":
                for x in self.bot.elkie_gif:
                    await ctx.send(x)
            elif arg == "clc yujin":
                for x in self.bot.clc_yujin_gif:
                    await ctx.send(x)
            elif arg == "clc eunbin":
                for x in self.bot.clc_eunbin_gif:
                    await ctx.send(x)
            elif arg == "clc seungyeon":
                for x in self.bot.clc_seungyeon_gif:
                    await ctx.send(x)
        #.Dreamcatcher
            elif arg == "dreamcatcher jiu":
                for x in self.bot.dreamcatcher_jiu_gif:
                    await ctx.send(x)
            elif arg == "dreamcatcher dami":
                for x in self.bot.dreamcatcher_dami_gif:
                    await ctx.send(x)
            elif arg == "dreamcatcher gahyeon":
                for x in self.bot.dreamcatcher_gahyeon_gif:
                    await ctx.send(x)
            elif arg == "dreamcatcher handong":
                for x in self.bot.dreamcatcher_handong_gif:
                    await ctx.send(x)
            elif arg == "dreamcatcher siyeon":
                for x in self.bot.dreamcatcher_siyeon_gif:
                    await ctx.send(x)
            elif arg == "dreamcatcher sua":
                for x in self.bot.dreamcatcher_sua_gif:
                    await ctx.send(x)
            elif arg == "dreamcatcher yoohyeon":
                for x in self.bot.dreamcatcher_yoohyeon_gif:
                    await ctx.send(x)
        #.Enhypen
            elif arg == "enhypen sunoo":
                for x in self.bot.sunoo_gif:
                    await ctx.send(x)
            elif arg == "enhypen sunghoon":
                for x in self.bot.sunghoon_gif:
                    await ctx.send(x)
            elif arg == "enhypen jake":
                for x in self.bot.jake_gif:
                    await ctx.send(x)
            elif arg == "enhypen jungwon":
                for x in self.bot.jungwon_gif:
                    await ctx.send(x)
            elif arg == "enhypen heeseung":
                for x in self.bot.heeseung_gif:
                    await ctx.send(x)
            elif arg == "enhypen jay":
                for x in self.bot.jay_gif:
                    await ctx.send(x)
            elif arg == "enhypen niki":
                for x in self.bot.niki_gif:
                    await ctx.send(x)
        #.Everglow
            elif arg == "everglow eu":
                for x in self.bot.eu_gif:
                    await ctx.send(x)
            elif arg == "everglow mia":
                for x in self.bot.mia_gif:
                    await ctx.send(x)
            elif arg == "everglow yiren":
                for x in self.bot.yiren_gif:
                    await ctx.send(x)
            elif arg == "everglow aisha":
                for x in self.bot.aisha_gif:
                    await ctx.send(x)
            elif arg == "everglow onda":
                for x in self.bot.onda_gif:
                    await ctx.send(x)
            elif arg == "everglow sihyeon":
                for x in self.bot.sihyeon_gif:
                    await ctx.send(x) 
        #.EXID
            elif arg == "exid hani":
                for x in self.bot.hani_gif:
                    await ctx.send(x)
            elif arg == "exid jeonghwa":
                for x in self.bot.jeonghwa_gif:
                    await ctx.send(x)
            elif arg == "exid le":
                for x in self.bot.le_gif:
                    await ctx.send(x)
            elif arg == "exid solji":
                for x in self.bot.solji_gif:
                    await ctx.send(x)
            elif arg == "exid hyelin" or arg == "exid hyerin":
                for x in self.bot.hyelin_gif:
                    await ctx.send(x)
        #.Gidle
            elif arg == "gidle minnie":
                for x in self.bot.minnie_gif:
                    await ctx.send(x)
            elif arg == "gidle miyeon":
                for x in self.bot.miyeon_gif:
                    await ctx.send(x)
            elif arg == "gidle shuhua":
                for x in self.bot.shuhua_gif:
                    await ctx.send(x)
            elif arg == "gidle soojin":
                for x in self.bot.soojin_gif:
                    await ctx.send(x)
            elif arg == "gidle soyeon":
                for x in self.bot.soyeon_gif:
                    await ctx.send(x)
            elif arg == "gidle yuqi":
                for x in self.bot.yuqi_gif:
                    await ctx.send(x)
        #.Itzy
            elif arg == "itzy yeji":
                for x in self.bot.itzy_yeji_gif:
                    await ctx.send(x)
            elif arg == "itzy ryujin":
                for x in self.bot.itzy_ryujin_gif:
                    await ctx.send(x)
            elif arg == "itzy chaeryeong":
                for x in self.bot.itzy_chaeryeong_gif:
                    await ctx.send(x)
            elif arg == "itzy yuna":
                for x in self.bot.itzy_yuna_gif:
                    await ctx.send(x)
            elif arg == "itzy lia":
                for x in self.bot.itzy_lia_gif:
                    await ctx.send(x)
        #.Izone
            elif arg == "izone sakura":
                for x in self.bot.sakura_gif:
                    await ctx.send(x)
            elif arg == "izone yuri":
                for x in self.bot.yuri_gif:
                    await ctx.send(x)
            elif arg == "izone chaeyeon":
                for x in self.bot.chaeyeon_gif:
                    await ctx.send(x)
            elif arg == "izone minju":
                for x in self.bot.minju_gif:
                    await ctx.send(x)
            elif arg == "izone wonyoung":
                for x in self.bot.wonyoung_gif:
                    await ctx.send(x)
            elif arg == "izone hyewon":
                for x in self.bot.hyewon_gif:
                    await ctx.send(x)
            elif arg == "izone chaewon":
                for x in self.bot.chaewon_gif:
                    await ctx.send(x)
            elif arg == "izone yujin":
                for x in self.bot.yujin_gif:
                    await ctx.send(x)
            elif arg == "izone yena":
                for x in self.bot.yena_gif:
                    await ctx.send(x)
            elif arg == "izone eunbi":
                for x in self.bot.eunbi_gif:
                    await ctx.send(x)
            elif arg == "izone nako":
                for x in self.bot.nako_gif:
                    await ctx.send(x)
            elif arg == "izone hitomi":
                for x in self.bot.hitomi_gif:
                    await ctx.send(x)
        #.KARD
            elif arg == "kard bm":
                for x in self.bot.kard_bm_gif:
                    await ctx.send(x)
            elif arg == "kard jiwoo":
                for x in self.bot.kard_jiwoo_gif:
                    await ctx.send(x)
            elif arg == "kard jseph":
                for x in self.bot.kard_jseph_gif:
                    await ctx.send(x)
            elif arg == "kard somin":
                for x in self.bot.kard_somin_gif:
                    await ctx.send(x) 
        #.Loona
            elif arg == "loona heejin":
                for x in self.bot.heejin_gif:
                    await ctx.send(x)
            elif arg == "loona hyunjin":
                for x in self.bot.hyunjin_gif:
                    await ctx.send(x)
            elif arg == "loona haseul":
                for x in self.bot.haseul_gif:
                    await ctx.send(x)
            elif arg == "loona vivi":
                for x in self.bot.vivi_gif:
                    await ctx.send(x)
            elif arg == "loona yeojin":
                for x in self.bot.yeojin_gif:
                    await ctx.send(x)
            elif arg == "loona kim lip":
                for x in self.bot.kimlip_gif:
                    await ctx.send(x)
            elif arg == "loona jinsoul":
                for x in self.bot.jinsoul_gif:
                    await ctx.send(x)
            elif arg == "loona choerry":
                for x in self.bot.choerry_gif:
                    await ctx.send(x)
            elif arg == "loona yves":
                for x in self.bot.yves_gif:
                    await ctx.send(x)
            elif arg == "loona chuu":
                for x in self.bot.chuu_gif:
                    await ctx.send(x)
            elif arg == "loona gowon":
                for x in self.bot.gowon_gif:
                    await ctx.send(x)
            elif arg == "loona olivia hye":
                for x in self.bot.oliviahye_gif:
                    await ctx.send(x)
        #.Lovelyz
            elif arg == "lovelyz yein":
                for x in self.bot.yein_gif:
                    await ctx.send(x)
            elif arg == "lovelyz kei":
                for x in self.bot.kei_gif:
                    await ctx.send(x)
            elif arg == "lovelyz jisoo":
                for x in self.bot.lovelyz_jisoo_gif:
                    await ctx.send(x)
            elif arg == "lovelyz baby soul":
                for x in self.bot.babysoul_gif:
                    await ctx.send(x)
            elif arg == "lovelyz mijoo":
                for x in self.bot.mijoo_gif:
                    await ctx.senc(x)
            elif arg == "lovelyz jiae":
                for x in self.bot.jiae_gif:
                    await ctx.send(x)
            elif arg == "lovelyz jin":
                for x in self.bot.lovelyz_jin_gif:
                    await ctx.send(x)
            elif arg == "lovelyz sujeong":
                for x in self.bot.sujeong_gif:
                    await ctx.send(x)
        #.NCT 
            elif arg == "nct lucas":
                for x in self.bot.nct_lucas_gif:
                    await ctx.send(x)
            elif arg == "nct mark":
                for x in self.bot.nct_mark_gif:
                    await ctx.send(x)
            elif arg == "nct winwin":
                for x in self.bot.nct_winwin_gif:
                    await ctx.send(x)
            elif arg == "nct jaemin":
                for x in self.bot.nct_jaemin_gif:
                    await ctx.send(x)
            elif arg == "nct jaehyun":
                for x in self.bot.nct_jaehyun_gif:
                    await ctx.send(x)
            elif arg == "nct kun":
                for x in self.bot.nct_kun_gif:
                    await ctx.send(x)
            elif arg == "nct ten":
                for x in self.bot.nct_ten_gif:
                    await ctx.send(x)
            elif arg == "nct xiaojun":
                for x in self.bot.nct_xiaojun_gif:
                    await ctx.send(x)
            elif arg == "nct hendery":
                for x in self.bot.nct_hendery_gif:
                    await ctx.send(x)
            elif arg == "nct yangyang":
                for x in self.bot.nct_yangyang_gif:
                    await ctx.send(x)
            elif arg == "nct taeyong":
                for x in self.bot.nct_taeyong_gif:
                    await ctx.send(x)
            elif arg == "nct jungwoo":
                for x in self.bot.nct_jungwoo_gif:
                    await ctx.send(x)
            elif arg == "nct yuta":
                for x in self.bot.nct_yuta_gif:
                    await ctx.send(x)
            elif arg == "nct jeno":
                for x in self.bot.nct_jeno_gif:
                    await ctx.send(x)
            elif arg == "nct jisung":
                for x in self.bot.nct_jisung_gif:
                    await ctx.send(x)
            elif arg == "nct taeyong":
                for x in self.bot.nct_renjun_gif:
                    await ctx.send(x)
        #.Mamamoo
            elif arg == "mamamoo":
                for x in self.bot.mamamoo_gif:
                    await ctx.send(x)
            elif arg == "mamamoo moonbyul":
                for x in self.bot.moonbyul_gif:
                    await ctx.send(x)
            elif arg == "mamamoo wheein":
                for x in self.bot.wheein_gif:
                    await ctx.send(x)
            elif arg == "mamamoo hwasa":
                for x in self.bot.hwasa_gif:
                    await ctx.send(x)
            elif arg == "mamamoo solar":
                for x in self.bot.solar_gif:
                    await ctx.send(x)
        #.Oh My Girl
            elif arg == "oh my girl arin":
                for x in self.bot.ohmygirl_arin_gif:
                    await ctx.send(x)
            elif arg == "oh my girl binnie":
                for x in self.bot.ohmygirl_binnie_gif:
                    await ctx.send(x)
            elif arg == "oh my girl hyojung":
                for x in self.bot.ohmygirl_hyojung_gif:
                    await ctx.send(x)
            elif arg == "oh my girl jiho":
                for x in self.bot.ohmygirl_jiho_gif:
                    await ctx.send(x)
            elif arg == "oh my girl mimi":
                for x in self.bot.ohmygirl_mimi_gif:
                    await ctx.send(x)
            elif arg == "oh my girl seunghee":
                for x in self.bot.ohmygirl_seunghee_gif:
                    await ctx.send(x)
            elif arg == "oh my girl yooa":
                for x in self.bot.ohmygirl_yooa_gif:
                    await ctx.send(x)
        #.P1Harmony
            if arg == "p1harmony intak":
                for x in self.bot.p1harmony_intak_gif:
                    await ctx.send(x)
            elif arg == "p1harmony jiung":
                for x in self.bot.p1harmony_jiung_gif:
                    await ctx.send(x)
            elif arg == "p1harmony jongseob":
                for x in self.bot.p1harmony_jongseob_gif:
                    await ctx.send(x)
            elif arg == "p1harmony keeho":
                for x in self.bot.p1harmony_keeho_gif:
                    await ctx.send(x)
            elif arg == "p1harmony soul":
                for x in self.bot.p1harmony_soul_gif:
                    await ctx.send(x)
            elif arg == "p1harmony soul":
                for x in self.bot.p1harmony_theo_gif:
                    await ctx.send(x)
        #.Purple K!ss
            elif arg == "purple kiss yuki":
                for x in self.bot.yuki_gif:
                    await ctx.send(x)
            elif arg == "purple kiss goeun" or arg == "purple kiss na goeun":
                for x in self.bot.nagoeun_gif:
                    await ctx.send(x)
            elif arg == "purple kiss jieun":
                for x in self.bot.jieun_gif:
                    await ctx.send(x)
            elif arg == "purple kiss dosie":
                for x in self.bot.dosie_gif:
                    await ctx.send(x)
            elif arg == "purple kiss ireh":
                for x in self.bot.ireh_gif:
                    await ctx.send(x)
            elif arg == "purple kiss chaein":
                for x in self.bot.chaein_gif:
                    await ctx.send(x)
            elif arg == "purple kiss swan":
                for x in self.bot.swan_gif:
                    await ctx.send(x)
        #.Red Velvet
            elif arg == "red velvet irene":
                for x in self.bot.irene_gif:
                    await ctx.send(x)
            elif arg == "red velvet seulgi":
                for x in self.bot.seulgi_gif:
                    await ctx.send(x)
            elif arg == "red velvet wendy":
                for x in self.bot.wendy_gif:
                    await ctx.send(x)
            elif arg == "red velvet yeri":
                for x in self.bot.yeri_gif:
                    await ctx.send(x)
            elif arg == "red velvet joy":
                for x in self.bot.joy_gif:
                    await ctx.send(x)
        #.SF9
            elif arg == "sf9 chani":
                for x in self.bot.sf9_chani_gif:
                    await ctx.send(x)
            elif arg == "af9 dawon":
                for x in self.bot.sf9_dawon_gif:
                    await ctx.send(x)
            elif arg == "sf9 hwiyoung":
                for x in self.bot.sf9_hwiyoung_gif:
                    await ctx.send(x)
            elif arg == "sf9 inseong":
                for x in self.bot.sf9_inseong_gif:
                    await ctx.send(x)
            elif arg == "sf9 jaeyoon":
                for x in self.bot.sf9_jaeyoon_gif:
                    await ctx.send(x)
            elif arg == "sf9 rowoon":
                for x in self.bot.sf9_rowoon_gif:
                    await ctx.send(x)
            elif arg == "sf9 taeyang":
                for x in self.bot.sf9_taeyang_gif:
                    await ctx.send(x)
            elif arg == "sf9 youngbin":
                for x in self.bot.sf9_youngbin_gif:
                    await ctx.send(x)
            elif arg == "sf9 zuho":
                for x in self.bot.sf9_zuho_gif:
                    await ctx.send(x)
        #.Stray Kids
            elif arg == "stray kids felix":
                for x in self.bot.felix_gif:
                    await ctx.send(x)
            elif arg == "stray kids hyunjin":
                for x in self.bot.shyunjin_gif:
                    await ctx.send(x)
            elif arg == "stray kids bang chan":
                for x in self.bot.bangchan_gif:
                    await ctx.send(x)
            elif arg == "stray kids lee know":
                for x in self.bot.leeknow_gif:
                    await ctx.send(x)
            elif arg == "stray kids han":
                for x in self.bot.han_gif:
                    await ctx.send(x)
            elif arg == "stray kids in":
                for x in self.bot.jeongin_gif:
                    await ctx.send(x)
            elif arg == "stray kids seungmin":
                for x in self.bot.seungmin_gif:
                    await ctx.send(x)
            elif arg == "stray kids changbin":
                for x in self.bot.changbin_gif:
                    await ctx.send(x)
        #.Twice
            elif arg == "twice mina":
                for x in self.bot.mina_gif:
                    await ctx.send(x)
            elif arg == "twice sana":
                for x in self.bot.sana_gif:
                    await ctx.send(x)
            elif arg == "twice momo":
                for x in self.bot.momo_gif:
                    await ctx.send(x)
            elif arg == "twice jeongyeon":
                for x in self.bot.jeongyeon_gif:
                    await ctx.send(x)
            elif arg == "twice tzuyu":
                for x in self.bot.tzuyu_gif:
                    await ctx.send(x)
            elif arg == "twice nayeon":
                for x in self.bot.nayeon_gif:
                    await ctx.send(x)
            elif arg == "twice jihyo":
                for x in self.bot.jihyo_gif:
                    await ctx.send(x)
            elif arg == "twice chaeyoung":
                for x in self.bot.chaeyoung_gif:
                    await ctx.send(x)
            elif arg == "twice dahyun":
                for x in self.bot.dahyun_gif:
                    await ctx.send(x)
        #.TXT
            elif arg == "txt soobin":
                for x in self.bot.txt_soobin_gif:
                    await ctx.send(x)
            elif arg == "txt yeonjun":
                for x in self.bot.txt_yeonjun_gif:
                    await ctx.send(x)
            elif arg == "txt beomgyu":
                for x in self.bot.txt_beomgyu_gif:
                    await ctx.send(x)
            elif arg == "txt taehyun":
                for x in self.bot.txt_taehyun_gif:
                    await ctx.send(x)
            elif arg == "txt huening kai":
                for x in self.bot.txt_hueningkai_gif:
                    await ctx.send(x)
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
        #.VAV
            elif arg == "vav ace":
                for x in self.bot.vav_ace_gif:
                    await ctx.send(x)
            elif arg == "vav ayno":
                for x in self.bot.vav_ayno_gif:
                    await ctx.send(x)
            elif arg == "vav baron":
                for x in self.bot.vav_baron_gif:
                    await ctx.send(x)
            elif arg == "vav jacob":
                for x in self.bot.vav_jacob_gif:
                    await ctx.send(x)
            elif arg == "vav lou":
                for x in self.bot.vav_lou_gif:
                    await ctx.send(x)
            elif arg == "vav st van":
                for x in self.bot.vav_stvan_gif:
                    await ctx.send(x)
            elif arg == "vav ziu":
                for x in self.bot.vav_ziu_gif:
                    await ctx.send(x)
        #.Weeekly
            elif arg == "weeekly soojin":
                for x in self.bot.weeekly_soojin_gif:
                    await ctx.send(x)
            elif arg == "weeekly jiyoon":
                for x in self.bot.weeekly_jiyoon_gif:
                    await ctx.send(x)
            elif arg == "weeekly monday":
                for x in self.bot.weeekly_monday_gif:
                    await ctx.send(x)
            elif arg == "weeekly soeun":
                for x in self.bot.weeekly_soeun_gif:
                    await ctx.send(x)
            elif arg == "weeekly jaehee":
                for x in self.bot.weeekly_jaehee_gif:
                    await ctx.send(x)
            elif arg == "weeekly jihan":
                for x in self.bot.weeekly_jihan_gif:
                    await ctx.send(x)
            elif arg == "weeekly zoa":
                for x in self.bot.weeekly_zoa_gif:
                    await ctx.send(x)
        #.Weki Meki
            elif arg == "weki meki doyeon":
                for x in self.bot.wekimeki_doyeon_gif:
                    await ctx.send(x)
            elif arg == "weki meki elly":
                for x in self.bot.wekimeki_elly_gif:
                    await ctx.send(x)
            elif arg == "weki meki lua":
                for x in self.bot.wekimeki_lua_gif:
                    await ctx.send(x)
            elif arg == "weki meki lucy":
                for x in self.bot.wekimeki_lucy_gif:
                    await ctx.send(x)
            elif arg == "weki meki rina":
                for x in self.bot.wekimeki_rina_gif:
                    await ctx.send(x)
            elif arg == "weki meki sei":
                for x in self.bot.wekimeki_sei_gif:
                    await ctx.send(x)
            elif arg == "weki meki suyeon":
                for x in self.bot.wekimeki_suyeon_gif:
                    await ctx.send(x)
            elif arg == "weki meki yoojung":
                for x in self.bot.wekimeki_yoojung_gif:
                    await ctx.send(x)
        #.WJSN
            elif arg == "wjsn bona":
                for x in self.bot.wjsn_bona_gif:
                    await ctx.send(x)
            elif arg == "wjsn cheng xiao":
                for x in self.bot.wjsn_cheng_xiao_gif:
                    await ctx.send(x)
            elif arg == "wjsn dawon":
                for x in self.bot.wjsn_dawon_gif:
                    await ctx.send(x)
            elif arg == "wjsn dayoung":
                for x in self.bot.wjsn_dayoung_gif:
                    await ctx.send(x)
            elif arg == "wjsn eunseo":
                for x in self.bot.wjsn_eunseo_gif:
                    await ctx.send(x)
            elif arg == "wjsn exy":
                for x in self.bot.wjsn_exy_gif:
                    await ctx.send(x)
            elif arg == "wjsn luda":
                for x in self.bot.wjsn_luda_gif:
                    await ctx.send(x)
            elif arg == "wjsn seola":
                for x in self.bot.wjsn_seola_gif:
                    await ctx.send(x)
            elif arg == "wjsn soobin":
                for x in self.bot.wjsn_soobin_gif:
                    await ctx.send(x)
            elif arg == "wjsn yeonjung":
                for x in self.bot.wjsn_yeonjung_gif:
                    await ctx.send(x)
            elif arg == "wjsn yeoreum":
                for x in self.bot.wjsn_yeoreum_gif:
                    await ctx.send(x)
            elif arg == "wjsn mei qi":
                for x in self.bot.wjsn_mei_qi_gif:
                    await ctx.send(x)
            elif arg == "wjsn xuan yi":
                for x in self.bot.wjsn_xuan_yi_gif:
                    await ctx.send(x)
        #.Misc
            elif arg == "ses":
                for x in self.bot.ses_mv:
                    await ctx.send(x)
            elif arg == "kiki":
                for x in self.bot.kiki_gif:
                    await ctx.send(x)
            elif arg == "taemin":
                for x in self.bot.taemin_gif:
                    await ctx.send(x)
            elif arg == "krystal":
                for x in self.bot.krystal_gif:
                    await ctx.send(x)
            elif arg == "jessica":
                for x in self.bot.jessica_gif:
                    await ctx.send(x)

        #.else
        else:
            await ctx.send(f'no')

def setup(client):
    client.add_cog(gifcog(client))