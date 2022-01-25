import discord, random, os
import asyncio
from discord.ext import commands
from discord.utils import get
from random import choice
from datetime import datetime

description = "All commands start with the prefix [=]\nTo invite Moonbyul to your server, try `=invite`"

class hcommands(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.unsorted_groups_list = ["Mamamoo", "2ne1", "f(x)", "LOOΠΔ", "Stray Kids", "Lovelyz", "Weki Meki",
            "NCT", "Iz*One", "Twice", "SNSD", "Cravity",
            "aespa", "Blackpink", "Brave Girls", "BTS", "Enhypen", "April", "TXT", "Itzy", "Red Velvet",
            "WEEEKLY", "Purple Kiss", "CLC", "WJSN", "P1Harmony", "The Boyz",
            "Oh My Girl", "Dreamcatcher", "VAV", "Cherry Bullet", "EXID", "SF9", "fromis_9", "EXO",
            "Soloists", "Everglow", "(G)I-dle", "Apink", "Shinee", "Golden Child",
            "Seventeen", "Momoland", "I.O.I", "K.A.R.D.", #// end of groups in old help command
            "Hello Venus", "woo!ah!", "TVXQ!", "Rocket Punch", "STAYC", "Astro", "Gugudan"]

        self.groups_list = sorted(self.unsorted_groups_list, key=str.lower)
        self.groups_list.append("Misc")
        self.groupName = "\n"
        for x in self.groups_list:
            self.groupName += x + "\n"

        self.unstored_soloist_list = ["Natty", "AleXa", "BIBI", "Chung ha", "IU", "Somi", "Yukika", 
            "WOODZ", "BoA", "Wonho", "Kris Wu", "Luhan", "Tao", "Kang Daniel", "Sunmi", "Yubin", "Rothy", "Hyuna", "DPR Ian", "Dean"]

        self.soloist_list = sorted(self.unstored_soloist_list, key=str.lower)
        self.soloistName = "\n"
        for x in self.soloist_list:
            self.soloistName += x + "\n"

    @commands.command(aliases = ['g', 'groups'])
    async def group(self, ctx, *, arg = "DEFAULT"):
        now = datetime.now()
        channel = ctx.bot.get_channel(self.client.logs)
        current_time = now.strftime("%H:%M:%S")
        await channel.send(f"`{current_time} | USED COMMAND [group {arg}] | USER: {ctx.author.name} [{(ctx.author.id)}] | GUILD: {ctx.guild.name} [{ctx.guild.id}]`" )
        embed1 = discord.Embed(
            # title = 'Mamamoo Commands',
            # description = description,
            colour = discord.Color.from_rgb(198, 237, 154))
        if arg == "mamamoo": #= has a group command
            embed1.add_field(name='Mamamoo Commands', value=f'```\nMamamoo\nMamamoo Moonbyul\nMamamoo Hwasa\nMamamoo Solar\nMamamoo Wheein```')
        elif arg == "2ne1": #= has a group command
            embed1.add_field(name='2NE1 Commands', value=f'```\n2NE1\n2NE1 CL\n2NE1 Dara\n2NE1 Minzy\n2NE1 Park Bom```')
        elif arg == "aespa": #. no group command
            embed1.add_field(name='aespa Commands', value=f'''```\naespa Giselle\naespa Winter\naespa NingNing\naespa Karina```''')
        elif arg == "apink": #. no group command
            embed1.add_field(name='Apink Commands', value=f'```\nApink Bomi\nApink Chorong\nApink Eunji\nApink Hayoung\nApink Naeun\nApink Namjoo```')
        elif arg == "april": #. no group command
            embed1.add_field(name='April Commands', value=f'''```\nApril Chaekyung\nApril Chaewon\nApril Naeun\nApril Yena\nApril Rachel\nApril Jinsol\nApril Hyunjoo```''')
        elif arg == "astro": #. no group command
            embed1.add_field(name='Astro', value=f'```\nASTRO Eunwoo\nASTRO MJ```')
        elif arg == "blackpink": #= has a group command
            embed1.add_field(name='Blackpink Commands', value=f'```\nBlackpink\nBlackpink Lisa\nBlackpink Jennie\nBlackpink Jisoo\nBlackpink Rosé```')
        elif arg == "brave girls": #. no group command
            embed1.add_field(name='Brave Girls Commands', value=f'```\nBrave Girls EUnji\nBrave Girls Minyoung\nBrave Girls Yujeong\nBrave Girls Yuna```')
        elif arg == "bts": #= has a group command
            embed1.add_field(name='BTS Commands', value=f'''```\nBTS\nBTS V\nBTS Suga\nBTS J-hope\nBTS Jin\nBTS Jimin\nBTS RM\nBTS Jungkook```''')
        elif arg == "cherry bullet": #. no group command
            embed1.add_field(name='Cherry Bullet Commands', value=f'''```\nCherry Bullet Bora\nCherry Bullet Chaerin\nCherry Bullet Haeyoon\nCherry Bullet Jiwon\nCherry Bullet Kokoro\nCherry Bullet Linlin\nCherry Bullet May\nCherry Bullet Mirae\nCherry Bullet Remi\nCherry Bullet Yuju```''')
        elif arg == "clc": #. no group command
            embed1.add_field(name='CLC Commands', value=f'''```\nCLC Yeeun\nCLC Sorn\nCLC Elkie\nCLC Eunbin\nCLC Yujin\nCLC Seunghee\nCLC Seungyeon```''')
        elif arg == "cravity": #. no group command
            embed1.add_field(name='Cravity Commands', value=f'''```\nCravity Serim\nCravity Allen\nCravity Jungmo\nCravity Woobin\nCravity Wonjin\nCravity Minhee\nCravity Hyeongjun\nCravity Taeyoung\nCravity Seongmin```''')
        elif arg == "dreamcatcher": #. no group command
            embed1.add_field(name='Dreamcatcher Commands', value=f'```\nDreamcatcer Dami\nDreamcatcher JiU\nDreamcatcher Gahyeon\nDreamcatcher Handong\nDreamcatcher Siyeon\nDreamcatcher Sua\nDreamcatcher Yoohyeon```', inline = True)
        elif arg == "enhypen": #. no group command
            embed1.add_field(name='Enhypen Commands', value=f'''```\nEnhypen Sunoo\nEnhypen Sunghoon\nEnhypen Jake\nEnhypen Jungwon\nEnhypen Heeseung\nEnhypen Jay\nEnhypen Ni-Ki```''')
        elif arg == "everglow": #= has a group command
            embed1.add_field(name='Everglow Commands', value=f'''```\nEverglow\nEverglow Yiren\nEverglow E:U\nEverglow Mia\nEverglow Aisha\nEverglow Onda\nEverglow Sihyeon```''')
        elif arg == "exid": #. no group command
            embed1.add_field(name='EXID Commands', value=f'''```\nEXID Hani\nEXID Jeonghwa\nEXID LE\nEXID Solji\nEXID Hyelin```''')
        elif arg == "exo": #. no group command
            embed1.add_field(name='EXO Commands', value=f'''```\nEXO Kai\nEXO D.O.\nEXO Baekhyun\nEXO Chanyeol\nEXO Sehun\nEXO Chen\nEXO Suho\nEXO Lay\nEXO Xiumin```''')
        elif arg == "fx" or arg == "f(x)": #. no group command
            embed1.add_field(name='f(x) Commands', value=f'\naliases: `f(x)`, `fx` ```\nf(x) Victoria\nf(x) Amber\nf(x) Luna\nf(x) Sulli\nf(x) Krystal```')
        elif arg == "fromis_9" or arg == "fromis" or arg == "fromis9": #= has a group command
            embed1.add_field(name='fromis_9 Commands', value=f'''\naliases: `fromis_9`, `fromis`, `fromis9` ```\nfromis_9\nfromis_9 Jisun\nfromis_9 Hayoung\nfromis_9 Saerom\nfromis_9 Chaekyoung\nfromis_9 Nakyung\nfromis_9 Jiwon\nfromis_9 Seoyeon\nfromis_9 Jiheon\nfromis_9 Gyuri```''')
        elif arg == "(g)i-dle" or arg == "gidle": #= has a group command
            embed1.add_field(name='(G)I-dle Commands', value=f'''\naliases: `(G)I-dle`, `Gidle` ```\n(G)I-dle\n(G)I-dle Minnie\n(G)I-dle Miyeon\n(G)I-dle Shuhua\n(G)I-dle Soojin\n(G)I-dle Soyeon\n(G)I-dle Yuqi```''')
        elif arg == "golden child": #. no group command
            embed1.add_field(name='Golden Child Commands', value=f'```\nGolden Child Y\nGolden Child Jibeom\nGolden Child Jangjun\nGolden Child Tag\nGolden Child Bomin\nGolden Child Daeyeol\nGolden Child Jaehyun\nGolden Child Donghyun\nGolden Child Joochan\nGolden Child Seungmin```')
        elif arg == "gwsn": #. no group command
            embed1.add_field(name='GWSN Commands', value=f'```\nGWSN Seokyoung\nGWSN Seoryoung\nGWSN Soso\nGWSN Anne\nGWSN Minju\nGWSN Lena\nGWSN Miya```')
        elif arg == "gugudan": #. no group command
            embed1.add_field(name='Gugudan Commands', value=f'```\nGugudan Sally```')
        elif arg == "hello venus": #. no group command
            embed1.add_field(name='Hello Venus Commands', value=f'''```\nHello Venus Lime\nHello Venus Alice\nHello Venus Nara\nHello Venus Seoyoung\nHello Venus Yooyoung\nHello Venus Yeoreum```''')
        elif arg == "ioi" or arg == "i.o.i": #. no group command
            embed1.add_field(name='I.O.I Commands', value=f'\naliases: `I.O.I`, `IOI` ```\nI.O.I Nayoung\nI.O.I Chung Ha\nI.O.I Sejeong\nI.O.I Chaeyeon\nI.O.I Kyulkyung\nI.O.I Sohye\nI.O.I Yeonjung\nI.O.I Yoojung\nI.O.I Mina\nI.O.I Doyeon\nI.O.I Somi```')
        elif arg == "itzy": #= has a group command
            embed1.add_field(name='Itzy Commands', value=f'''```\nItzy\nItzy Yeji\nItzy Ryujin\nItzy Chaeryeong\nItzy Yuna\nItzy Lia```''')
        elif arg == "izone" or arg == "iz*one": #= has a group command
            embed1.add_field(name='Iz*One Commands', value=f'''\naliases: `Iz*One`, `Izone` ```\nIz*One\nIz*One Sakura\nIz*One Yuri\nIz*One Chaeyeon\nIz*One Eunbi\nIz*One Minju\nIz*One Hyewon\nIz*One Wonyoung\nIz*One Nako\nIz*One Chaewon\nIz*One Yujin\nIz*One Yena\nIz*One Hitomi```''')
        elif arg == "kard" or arg == "k.a.r.d": #. no group command
            embed1.add_field(name='K.A.R.D Commands', value=f'\naliases: `K.A.R.D.`, `KARD` ```\nK.A.R.D. BM\nK.A.R.D. Jiwoo\nK.A.R.D. J.Seph\nK.A.R.D. Somin```')
        elif arg == "loona" or arg == "looπδ": #= has a group command
            embed1.add_field(name='LOOΠΔ Commands', value=f'''\naliases: `LOOΠΔ`, `Loona` ```\nLOOΠΔ\nLOOΠΔ Heejin\nLOOΠΔ Hyunjin\nLOOΠΔ Haseul\nLOOΠΔ ViVi\nLOOΠΔ Yeojin\nLOOΠΔ Kim Lip\nLOOΠΔ Jinsoul\nLOOΠΔ Choerry\nLOOΠΔ Yves\nLOOΠΔ Chuu\nLOOΠΔ Go Won\nLOOΠΔ Olivia Hye```''')
        elif arg == "lovelyz": #. no group command
            embed1.add_field(name='Lovelyz Commands', value=f'''```\nLovelyz Baby Soul\nLovelyz Yein\nLovelyz Kei\nLovelyz Jisoo\nLovelyz Mijoo\nLovelyz Jiae\nLovelyz Jin\nLovelyz Sujeong```''')
        elif arg == "momoland": #. no group command
            embed1.add_field(name='Momoland Commands', value=f'```\nMomoland Hyebin\nMomoland Jane\nMomoland Nayun\nMomoland JooE\nMomoland Ahin\nMomoland Nancy```')
        elif arg == "nct" or arg == "wayv": #// more or less has three group commands
            embed1.add_field(name='NCT Commands', value=f'''```\nNCT 127\nNCT Dream\nWayV\nNCT Lucas\nNCT Mark\nNCT Winwin\nNCT Jaemin\nNCT Jaehyun\nNCT Taeyong\nNCT Doyoung\nNCT Taeil\nNCT Chenle\nNCT Jungwoo\nNCT Renjun\nNCT Kun\nNCT Ten\nNCT Xiaojun\nNCT Haechan\nNCT Johnny\nNCT Sungchan\nNCT Shotaro\nNCT Hendery\nNCT Yangyang\nNCT Yuta\nNCT Jeno\nNCT Jisung```''')        
        elif arg == "oh my girl": #. no group command
            embed1.add_field(name='Oh My Girl Commands', value=f'```\nOh My Girl Arin\nOh My Girl Binnie\nOh My Girl Hyojung\nOh My Girl Jiho\nOh My Girl Mimi\nOh My Girl Seunghee\nOh My Girl YooA```')
        elif arg == "p1harmony" or arg == "p1h": #= has a group command
            embed1.add_field(name='P1Harmony Commands', value=f'\naliases: `P1Harmony`, `P1H` ```\nP1Harmony\nP1Harmony Intak\nP1Harmony Jiung\nP1Harmony Jongseob\nP1Harmony Keeho\nP1Harmony Soul\nP1Harmony Theo```')
        elif arg == "purple kiss" or arg == "purple k!ss": #. no group command
            embed1.add_field(name='Purple Kiss Commands', value=f'''\naliases: `Purple Kiss`, `Purple K!ss` ```\nPurple Kiss Yuki\nPurple Kiss Na Goeun\nPurple Kiss Jieun\nPurple Kiss Dosie\nPurple Kiss Ireh\nPurple Kiss Chaein\nPurple Kiss Swan\nPurple Kiss Teaser```''')
        elif arg == "red velvet": #= has a group command
            embed1.add_field(name='Red Velvet Commands', value=f'```\nRed Velvet\nRed Velvet Joy\nRed Velvet Irene\nRed Velvet Seulgi\nRed Velvet Yeri\nRed Velvet Wendy```')
        elif arg == "rocket punch": #= has a group command
            embed1.add_field(name='Rocket Punch Commands', value=f'```\nRocket Punch\nRocket Punch Juri\nRocket Punch Yeonhee\nRocket Punch Suyun\nRocket Punch Yunkyoung\nRocket Punch Sohee\nRocket Punch Dahyun```')
        elif arg == "seventeen" or arg == "svt": #. no group command
            embed1.add_field(name='Seventeen Commands', value=f'\naliases: `Seventeen`, `SVT` ```\nSeventeen S.coups\nSeventeen Wonwoo\nSeventeen Mingyu\nSeventeen Vernon\nSeventeen Woozi\nSeventeen Jeonghan\nSeventeen Joshua\nSeventeen DK\nSeventeen Seungkwan\nSeventeen Hoshi\nSeventeen Jun\nSeventeen The8\nSeventeen Dino```', inline = True)
        elif arg == "sf9": #= has a group command
            embed1.add_field(name='SF9 Commands', value=f'```\nSF9\nSF9 Chani\nSF9 Dawon\nSF9 Hwiyoung\nSF9 Inseong\nSF9 Jaeyoon\nSF9 Rowoon\nSF9 Yoo Taeyang\nSF9 Youngbin\nSF9 Zuho```')
        elif arg == "shinee": #. no group command
            embed1.add_field(name='Shinee Commands', value=f'```\nShinee Jonghyun\nShinee Key\nShinee Taemin\nShinee Minho\nShinee Onew```')
        elif arg == "snsd": #. no group command
            embed1.add_field(name='SNSD Commands', value=f'''```\nSNSD YoonA\nSNSD Yuri\nSNSD Hyoyeon\nSNSD Sunny\nSNSD Tiffany\nSNSD Sooyoung\nSNSD Seohyun\nSNSD Jessica\nSNSD Taeyeon```''')
        elif arg == "stayc": #= has a group command
            embed1.add_field(name='STAYC Commands', value=f'```\nSTAYC\nSTAYC Sieun\nSTAYC Seeun\nSTAYC Sumin\nSTAYC J\nSTAYC Isa\nSTAYC Yoon```')
        elif arg == "stray kids": #. no group command
            embed1.add_field(name='Stray Kids Commands', value=f'''```\nStray Kids Felix\nStray Kids Hyunjin\nStray Kids Bang Chan\nStray Kids Lee Know\nStray Kids Changbin\nStray Kids Han\nStray Kids I.N\nStray Kids Seungmin```''')
        elif arg == "the boyz": #= has a group command
            embed1.add_field(name='The Boyz Commands', value=f'```\nThe Boyz\nThe Boyz Kevin\nThe Boyz Sangyeon\nThe Boyz Jacob\nThe Boyz Younghoon\nThe Boyz Hyunjae\nThe Boyz Juyeon\nThe Boyz New\nThe Boyz Q\nThe Boyz Haknyeon\nThe Boyz Sunwoo\nThe Boyz Eric```')
        elif arg == "txt": #= has a group command
            embed1.add_field(name='TXT Commands', value=f'''```\nTXT\nTXT Soobin\nTXT Yeonjun\nTXT Beomgyu\nTXT Taehyun\nTXT Huening Kai```''')
        elif arg == "tvxq" or arg == "tvxq!": #. no group command
            embed1.add_field(name='TVXQ! Commands', value=f'\naliases: `TVXQ!`, `TVXQ` ```\nTVXQ! Max\nTVXQ! U-Know```')
        elif arg == "twice": #= has a group command
            embed1.add_field(name='Twice Commands', value=f'''```\nTwice\nTwice Mina\nTwice Sana\nTwice Momo\nTwice Jeongyeon\nTwice Tzuyu\nTwice Nayeon\nTwice Dahyun\nTwice Chaeyoung\nTwice Jihyo```''')
        elif arg == "vav": #. no group command
            embed1.add_field(name='VAV Commands', value=f'```\nVAV Ace\nVAV Ayno\nVAV Baron\nVAV Jacob\nVAV Lou\nVAV St.Van\nVAV Ziu```')
        elif arg == "weeekly": #= has a group command
            embed1.add_field(name='WEEEKLY Commands', value=f'''```\nWEEEKLY\nWEEEKLY Soojin\nWEEEKLY Monday\nWEEEKLY Jiyoon\nWEEEKLY Soeun\nWEEEKLY Jaehee\nWEEEKLY Jihan\nWEEEKLY Zoa```''')
        elif arg == "weki meki": #= has a group command
            embed1.add_field(name='Weki Meki Commands', value=f'''```\nWeki Meki\nWeki Meki Doyeon\nWeki Meki Elly\nWeki Meki Lua\nWeki Meki Lucy\nWeki Meki Rina\nWeki Meki Sei\nWeki Meki Suyeon\nWeki Meki Yoojung```''')
        elif arg == "wjsn": #= has a group command
            embed1.add_field(name='WJSN Commands', value=f'```\nWJSN\nWJSN Bona\nWJSN Cheng Xiao\nWJSN Dawon\nWJSN Dayoung\nWJSN Eunseo\nWJSN Exy\nWJSN Yeoreum\nWJSN Luda\nWJSN Mei Qi\nWJSN Seola\nWJSN Soobin\nWJSN Yeonjung\nWJSN Xuan Yi```')
        elif arg == "wooah" or arg == "woo!ah!": #. no group command
            embed1.add_field(name='woo!ah! Commands', value=f'''\naliases: `woo!ah!`, `wooah` ```\nwoo!ah! Sora\nwoo!ah! Wooyeon\nwoo!ah! Nana\nwoo!ah! Lucy\nwoo!ah! Minseo```''')
        
        elif arg == "misc":
            embed1.add_field(name='Misc Commands', value=f'```\nKiki\nS.E.S```')
        elif arg == "DEFAULT":
            embed1.add_field(name='Groups', value=f'\nTry `=Groups` followed by one of the groups listed for more information! ```{self.groupName}```')

        elif arg == "solo" or "soloists" or "soloist":
            embed1.add_field(name='Soloist Commands', value=f'\nSoloists have no group! ```{self.soloistName}```')


        embed1.add_field(name='Support:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)
        await ctx.send(embed=embed1)

    @commands.command()
    async def help(self, ctx):
        helpEmbed = discord.Embed(
            title = 'Commands',
            description = description,
            colour = discord.Color.from_rgb(198, 237, 154))
        helpEmbed.add_field(name='Groups', value=f'\nAliases: `Group`, `G`\n \n`Show available Groups and Idols, and more information about them`')
        helpEmbed.add_field(name='Invite', value=f'\n`Invite Moonbyul to your Server!`')
        helpEmbed.add_field(name='Bot', value=f'\n`See information about Moonbyul`')
        helpEmbed.add_field(name='Ping', value=f'\n`Pong`')
        helpEmbed.add_field(name='Support Server:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)
        await ctx.send(embed=helpEmbed)        

    @commands.command()
    async def NOTHELP(self, ctx):
        
        cur_page = 1
        totalpages = 7
    #//embed 1
        embed1 = discord.Embed(
            title = 'COMMANDS',
            description = description,
            colour = discord.Color.from_rgb(198, 237, 154))
        embed1.set_footer(text=f"page 1/{totalpages}")
        #// can separate
        embed1.add_field(name='Mamamoo', value=f'```\nMamamoo\nMamamoo Moonbyul\nMamamoo Hwasa\nMamamoo Solar\nMamamoo Wheein```', inline = True)
        embed1.add_field(name='2NE1', value=f'```\n2NE1 CL\n2NE1 Dara\n2NE1 Minzy\n2NE1 Park Bom\n ```')
        embed1.add_field(name='f(x)', value=f'```\nf(x) Victoria\nf(x) Amber\nf(x) Luna\nf(x) Sulli\nf(x) Krystal```')
        
        #// do not separate
        embed1.add_field(name='LOOΠΔ 1/3', value=f'''```\nLoona Heejin\nLoona Hyunjin\nLoona Haseul\nLoona ViVi\nLoona Yeojin```''')
        embed1.add_field(name='LOOΠΔ Odd Eye Circle', value=f'''```\nLoona Kim Lip\nLoona Jinsoul\nLoona Choerry\n \n ```''')
        embed1.add_field(name='LOOΠΔ yyxy', value=f'''```\nLoona Yves\nLoona Chuu\nLoona Go Won\nLoona Olivia Hye\n ```''')
        
        #// even (8)
        embed1.add_field(name='Stray Kids', value=f'''```\nStray Kids Felix\nStray Kids Hyunjin\nStray Kids Bang Chan\nStray Kids Lee Know\nStray Kids Changbin\nStray Kids Han\nStray Kids I.N\nStray Kids Seungmin```''')
        embed1.add_field(name='Lovelyz', value=f'''```\nLovelyz Baby Soul\nLovelyz Yein\nLovelyz Kei\nLovelyz Jisoo\nLovelyz Mijoo\nLovelyz Jiae\nLovelyz Jin\nLovelyz Sujeong```''')
        embed1.add_field(name='Weki Meki', value=f'''```\nWeki Meki Doyeon\nWeki Meki Elly\nWeki Meki Lua\nWeki Meki Lucy\nWeki Meki Rina\nWeki Meki Sei\nWeki Meki Suyeon\nWeki Meki Yoojung```''')
        embed1.add_field(name='Support:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)

    #//embed2
        embed2 = discord.Embed(
            title = 'COMMANDS',
            description = description,
            colour = discord.Color.from_rgb(198, 237, 154))
        embed2.set_footer(text=f"page 2/{totalpages}")
        #// do not separate
        embed2.add_field(name='NCT', value=f'''```\nNCT Lucas\nNCT Mark\nNCT Winwin\nNCT Jaemin\nNCT Jaehyun\nNCT Taeyong\nNCT Doyoung\nNCT Taeil\nNCT Chenle```''')
        embed2.add_field(name='NCT', value=f'''```\nNCT Jungwoo\nNCT Renjun\nNCT Kun\nNCT Ten\nNCT Xiaojun\nNCT Haechan\nNCT Johnny\nNCT Sungchan\nNCT Shotaro```''')
        embed2.add_field(name='NCT', value=f'''```\nNCT Hendery\nNCT Yangyang\nNCT Yuta\nNCT Jeno\nNCT Jisung\n \nNCT 127\nNCT Dream\nWayV```''')        
        
        #// do not separate
        embed2.add_field(name='Iz*One', value=f'''```\nIz*One Sakura\nIz*One Yuri\nIz*One Chaeyeon\nIz*One Eunbi```''')
        embed2.add_field(name='Iz*One', value=f'''```\nIz*One Minju\nIz*One Hyewon\nIz*One Wonyoung\nIz*One Nako```''')
        embed2.add_field(name='Iz*One', value=f'''```\nIz*One Chaewon\nIz*One Yujin\nIz*One Yena\nIz*One Hitomi```''')
        
        #// even (9)
        embed2.add_field(name='Twice', value=f'''```\nTwice Mina\nTwice Sana\nTwice Momo\nTwice Jeongyeon\nTwice Tzuyu\nTwice Nayeon\nTwice Dahyun\nTwice Chaeyoung\nTwice Jihyo```''')
        embed2.add_field(name='SNSD', value=f'''```\nSNSD YoonA\nSNSD Yuri\nSNSD Hyoyeon\nSNSD Sunny\nSNSD Tiffany\nSNSD Sooyoung\nSNSD Seohyun\nSNSD Jessica\nSNSD Taeyeon```''')
        embed2.add_field(name='Cravity', value=f'''```\nCravity Serim\nCravity Allen\nCravity Jungmo\nCravity Woobin\nCravity Wonjin\nCravity Minhee\nCravity Hyeongjun\nCravity Taeyoung\nCravity Seongmin```''')
        embed2.add_field(name='Support:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)

    #//embed3
        embed3 = discord.Embed(
            title = 'COMMANDS',
            description = description,
            colour = discord.Color.from_rgb(198, 237, 154))
        embed3.set_footer(text=f"page 3/{totalpages}")
        #// even (4)
        embed3.add_field(name='aespa', value=f'''```\naespa Giselle\naespa Winter\naespa NingNing\naespa Karina```''')
        embed3.add_field(name='Blackpink', value=f'```\nBlackpink Lisa\nBlackpink Jennie\nBlackpink Jisoo\nBlackpink Rosé```')
        embed3.add_field(name='Brave Girls', value=f'```\nBrave Girls EUnji\nBrave Girls Minyoung\nBrave Girls Yujeong\nBrave Girls Yuna```')
        
        #//even (7)
        embed3.add_field(name='BTS', value=f'''```\nBTS V\nBTS Suga\nBTS J-hope\nBTS Jin\nBTS Jimin\nBTS RM\nBTS Jungkook```''')
        embed3.add_field(name='Enhypen', value=f'''```\nEnhypen Sunoo\nEnhypen Sunghoon\nEnhypen Jake\nEnhypen Jungwon\nEnhypen Heeseung\nEnhypen Jay\nEnhypen Ni-Ki```''')
        embed3.add_field(name='April', value=f'''```\nApril Chaekyung\nApril Chaewon\nApril Naeun\nApril Yena\nApril Rachel\nApril Jinsol\nApril Hyunjoo```''')
        
        #// even (5)
        embed3.add_field(name='TXT', value=f'''```\nTXT Soobin\nTXT Yeonjun\nTXT Beomgyu\nTXT Taehyun\nTXT Huening Kai```''')
        embed3.add_field(name='Itzy', value=f'''```\nItzy Yeji\nItzy Ryujin\nItzy Chaeryeong\nItzy Yuna\nItzy Lia```''')
        embed3.add_field(name='Red Velvet', value=f'```\nRed Velvet Joy\nRed Velvet Irene\nRed Velvet Seulgi\nRed Velvet Yeri\nRed Velvet Wendy```')
        embed3.add_field(name='Support:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)

    #//embed4
        embed4 = discord.Embed(
            title = 'COMMANDS',
            description = description,
            colour = discord.Color.from_rgb(198, 237, 154))
        embed4.set_footer(text=f"page 4/{totalpages}")
        #// even (7)
        embed4.add_field(name='WEEEKLY', value=f'''```\nWEEEKLY Soojin\nWEEEKLY Monday\nWEEEKLY Jiyoon\nWEEEKLY Soeun\nWEEEKLY Jaehee\nWEEEKLY Jihan\nWEEEKLY Zoa```''')
        embed4.add_field(name='Purple Kiss', value=f'''```\nPurple Kiss Yuki\nPurple Kiss Na Goeun\nPurple Kiss Jieun\nPurple Kiss Dosie\nPurple Kiss Ireh\nPurple Kiss Chaein\nPurple Kiss Swan```''')
        embed4.add_field(name='CLC', value=f'''```\nCLC Yeeun\nCLC Sorn\nCLC Elkie\nCLC Eunbin\nCLC Yujin\nCLC Seunghee\nCLC Seungyeon```''')
        
        #// can separate (but even (7))
        embed4.add_field(name='WJSN', value=f'```\nWJSN Bona\nWJSN Cheng Xiao\nWJSN Dawon\nWJSN Dayoung\nWJSN Eunseo\nWJSN Exy\nWJSN Yeoreum```')
        embed4.add_field(name='WJSN', value=f'```\nWJSN Luda\nWJSN Mei Qi\nWJSN Seola\nWJSN Soobin\nWJSN Yeonjung\nWJSN Xuan Yi\n ```')
        embed4.add_field(name='GWSN', value=f'```\nGWSN Seokyoung\nGWSN Seoryoung\nGWSN Soso\nGWSN Anne\nGWSN Minju\nGWSN Lena\nGWSN Miya```')
        
        #// do not separate, 6, 11
        embed4.add_field(name='P1Harmony', value=f'```\nP1Harmony Intak\nP1Harmony Jiung\nP1Harmony Jongseob\nP1Harmony Keeho\nP1Harmony Soul\nP1Harmony Theo```')
        embed4.add_field(name='The Boyz', value=f'```\nThe Boyz Kevin\nThe Boyz Sangyeon\nThe Boyz Jacob\nThe Boyz Younghoon\nThe Boyz Hyunjae\nThe Boyz Juyeon```')
        embed4.add_field(name='The Boyz', value=f'```\nThe Boyz New\nThe Boyz Q\nThe Boyz Haknyeon\nThe Boyz Sunwoo\nThe Boyz Eric\n ```')
        embed4.add_field(name='Support:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)

    #//embed5
        embed5 = discord.Embed(
            title = 'COMMANDS',
            description = description,
            colour = discord.Color.from_rgb(198, 237, 154))
        embed5.set_footer(text=f"page 5/{totalpages}")
        #// even (7)
        embed5.add_field(name='Oh My Girl', value=f'```\nOh My Girl Arin\nOh My Girl Binnie\nOh My Girl Hyojung\nOh My Girl Jiho\nOh My Girl Mimi\nOh My Girl Seunghee\nOh My Girl YooA```')
        embed5.add_field(name='Dreamcatcher', value=f'```\nDreamcatcer Dami\nDreamcatcher JiU\nDreamcatcher Gahyeon\nDreamcatcher Handong\nDreamcatcher Siyeon\nDreamcatcher Sua\nDreamcatcher Yoohyeon```', inline = True)
        embed5.add_field(name='VAV', value=f'```\nVAV Ace\nVAV Ayno\nVAV Baron\nVAV Jacob\nVAV Lou\nVAV St.Van\nVAV Ziu```')
        
        #// even, but chebul will have some members moved soonish (5)
        embed5.add_field(name='Cherry Bullet', value=f'''```\nCherry Bullet Bora\nCherry Bullet Chaerin\nCherry Bullet Haeyoon\nCherry Bullet Jiwon\nCherry Bullet Kokoro```''')
        embed5.add_field(name='Cherry Bullet', value=f'''```\nCherry Bullet Linlin\nCherry Bullet May\nCherry Bullet Mirae\nCherry Bullet Remi\nCherry Bullet Yuju```''')
        embed5.add_field(name='EXID', value=f'''```\nEXID Hani\nEXID Jeonghwa\nEXID LE\nEXID Solji\nEXID Hyelin```''')

        #// even (9)
        embed5.add_field(name='SF9', value=f'```\nSF9 Chani\nSF9 Dawon\nSF9 Hwiyoung\nSF9 Inseong\nSF9 Jaeyoon\nSF9 Rowoon\nSF9 Yoo Taeyang\nSF9 Youngbin\nSF9 Zuho```')
        embed5.add_field(name='fromis_9', value=f'''```\nfromis_9 Jisun\nfromis_9 Hayoung\nfromis_9 Saerom\nfromis_9 Chaekyoung\nfromis_9 Nakyung\nfromis_9 Jiwon\nfromis_9 Seoyeon\nfromis_9 Jiheon\nfromis_9 Gyuri```''')
        embed5.add_field(name='EXO', value=f'''```\nEXO Kai\nEXO D.O.\nEXO Baekhyun\nEXO Chanyeol\nEXO Sehun\nEXO Chen\nEXO Suho\nEXO Lay\nEXO Xiumin```''')
        embed5.add_field(name='Support:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)

    #//embed6
        embed6 = discord.Embed(
            title = 'COMMANDS',
            description = description,
            colour = discord.Color.from_rgb(198, 237, 154))
        embed6.set_footer(text=f"page 6/{totalpages}")
        #//can separate
        embed6.add_field(name='Soloists', value=f'```\nNatty\nAleXa\nChung ha\nIU\nSomi\nYukika\nWOODZ\nBoA\nWonho```')
        embed6.add_field(name='Soloists', value=f'```\nKris Wu\nLuhan\nTao\nKang Daniel\nSunmi\nYubin\nRothy\nHyuna\nDPR Ian```')
        embed6.add_field(name='Everglow', value=f'''```\nEverglow Yiren\nEverglow E:U\nEverglow Mia\nEverglow Aisha\nEverglow Onda\nEverglow Sihyeon\n \n \n ```''')

        #// even (6)
        embed6.add_field(name='(G)I-dle', value=f'''```\n(G)I-dle Minnie\n(G)I-dle Miyeon\n(G)I-dle Shuhua\n(G)I-dle Soojin\n(G)I-dle Soyeon\n(G)I-dle Yuqi```''')
        embed6.add_field(name='Apink', value=f'```\nApink Bomi\nApink Chorong\nApink Eunji\nApink Hayoung\nApink Naeun\nApink Namjoo```')
        embed6.add_field(name='Shinee', value=f'```\nShinee Jonghyun\nShinee Key\nShinee Taemin\nShinee Minho\nShinee Onew\nShinee```')

        #// even (5)
        embed6.add_field(name='Misc', value=f'```\nKiki\nS.E.S\nASTRO Eunwoo\nASTRO MJ\n ```')
        embed6.add_field(name='Golden Child', value=f'```\nGolden Child Y\nGolden Child Jibeom\nGolden Child Jangjun\nGolden Child Tag\nGolden Child Bomin```')
        embed6.add_field(name='Golden Child', value=f'```\nGolden Child Daeyeol\nGolden Child Jaehyun\nGolden Child Donghyun\nGolden Child Joochan\nGolden Child Seungmin```')
        embed6.add_field(name='Support:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)

    #//embed7
        embed7 = discord.Embed(
            title = 'COMMANDS',
            description = description,
            colour = discord.Color.from_rgb(198, 237, 154))
        embed7.set_footer(text=f"page 7/{totalpages}")
        #//can separate
        embed7.add_field(name='Seventeen', value=f'```\nSeventeen S.coups\nSeventeen Wonwoo\nSeventeen Mingyu\nSeventeen Vernon\nSeventeen Woozi\nSeventeen Jeonghan\nSeventeen Joshua```', inline = True)
        embed7.add_field(name='Seventeen', value=f'```\nSeventeen DK\nSeventeen Seungkwan\nSeventeen Hoshi\nSeventeen Jun\nSeventeen The8\nSeventeen Dino\n ```', inline = True)
        embed7.add_field(name='Momoland', value=f'```\nMomoland Hyebin\nMomoland Jane\nMomoland Nayun\nMomoland JooE\nMomoland Ahin\nMomoland Nancy\n ```')
        
        #// uneven (6,4)
        embed7.add_field(name='I.O.I', value=f'```\nI.O.I Nayoung\nI.O.I Chung Ha\nI.O.I Sejeong\nI.O.I Chaeyeon\nI.O.I Kyulkyung\nI.O.I Sohye```')
        embed7.add_field(name='I.O.I', value=f'```\nI.O.I Yeonjung\nI.O.I Yoojung\nI.O.I Mina\nI.O.I Doyeon\nI.O.I Somi\n ```')
        embed7.add_field(name='K.A.R.D', value=f'```\nK.A.R.D BM\nK.A.R.D Jiwoo\nK.A.R.D J.Seph\nK.A.R.D Somin\n \n```')

        embed7.add_field(name='Extra Commands', value=f'```\nFood\nChuu Heart```')
        
        # embed7.add_field(name='Shinee', value=f'```\nShinee Jonghyun\nShinee Key\nShinee Taemin\nShinee Minho\nShinee Onew\nShinee```')
        # embed7.add_field(name='Golden Child', value=f'```\nGolden Child Joochan\nGolden Child Y```')
        embed7.add_field(name='Support:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)
        

    #//end of embeds:)
        # getting the message object for editing and reacting


        # await ctx.message.delete()


        message = await ctx.send(embed=embed1)

        await message.add_reaction("⬅️")
        await message.add_reaction("➡️")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["⬅️", "➡️"]
            # This makes sure nobody except the command sender can interact with the "menu"



        while True:
            try:
                reaction, user = await self.client.wait_for("reaction_add", timeout=60, check=check)
                # waiting for a reaction to be added - times out after x seconds, 60 in this
                # example

                if cur_page == 1:
                    if str(reaction.emoji) == "➡️":
                        cur_page += 1
                        await message.edit(embed=embed2)
                        await message.remove_reaction(reaction, user)
                    elif str(reaction.emoji) == "⬅️":
                        await message.remove_reaction(reaction, user)
                
                elif cur_page == 2:
                    if str(reaction.emoji) == "➡️":
                        cur_page += 1
                        await message.edit(embed=embed3)
                        await message.remove_reaction(reaction, user)
                    elif str(reaction.emoji) == "⬅️":
                        cur_page -= 1
                        await message.edit(embed=embed1)
                        await message.remove_reaction(reaction, user)
                
                elif cur_page == 3:
                    if str(reaction.emoji) == "➡️":
                        cur_page += 1
                        await message.edit(embed=embed4)
                        await message.remove_reaction(reaction, user)
                    if str(reaction.emoji) == "⬅️":
                        cur_page -= 1
                        await message.edit(embed=embed2)
                        await message.remove_reaction(reaction, user)
                
                elif cur_page == 4:
                    if str(reaction.emoji) == "➡️":
                        cur_page += 1
                        await message.edit(embed=embed5)
                        await message.remove_reaction(reaction, user)
                    elif str(reaction.emoji) == "⬅️":
                        cur_page -= 1
                        await message.edit(embed=embed3)
                        await message.remove_reaction(reaction, user)

                elif cur_page == 5:
                    if str(reaction.emoji) == "➡️":
                        cur_page += 1
                        await message.edit(embed=embed6)
                        await message.remove_reaction(reaction, user)
                    elif str(reaction.emoji) == "⬅️":
                        cur_page -= 1
                        await message.edit(embed=embed4)
                        await message.remove_reaction(reaction, user)

                elif cur_page == 6:
                    if str(reaction.emoji) == "➡️":
                        cur_page += 1
                        await message.edit(embed=embed7)
                        await message.remove_reaction(reaction, user)
                    elif str(reaction.emoji) == "⬅️":
                        cur_page -= 1
                        await message.edit(embed=embed5)
                        await message.remove_reaction(reaction, user)
                
                elif cur_page == 7:
                    if str(reaction.emoji) == "➡️":
                        await message.remove_reaction(reaction, user)
                    elif str(reaction.emoji) == "⬅️":
                        cur_page -= 1
                        await message.edit(embed=embed6)
                        await message.remove_reaction(reaction, user)

                else:
                    cur_page = cur_page
                    await message.remove_reaction(reaction, user)
                    # removes reactions if the user tries to go forward on the last page or
                    # backwards on the first page

            except asyncio.TimeoutError:
                #await message.delete()
                await message.clear_reactions()
                break
                # ending the loop if user doesn't react after x seconds


    

def setup(client):
    client.add_cog(hcommands(client))