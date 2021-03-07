import discord, random, os
import asyncio
from discord.ext import commands
from discord.utils import get
from random import choice

description = "All commands start with the prefix [=]\nTo invite Moonbyul to your server, try `=invite`"

class hcommands(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def help(self, ctx):
        
        cur_page = 1
        totalpages = 6
    #//embed 1
        embed1 = discord.Embed(
            title = 'COMMANDS',
            description = description,
            colour = discord.Color.from_rgb(198, 237, 154))
        embed1.set_footer(text=f"page 1/{totalpages}")
        embed1.add_field(name='Mamamoo', value=f'```\nMamamoo\nMamamoo Moonbyul\nMamamoo Hwasa\nMamamoo Solar\nMamamoo Wheein```', inline = True)
        embed1.add_field(name='2NE1', value=f'```\n2NE1 CL\n2NE1 Dara\n2NE1 Minzy\n2NE1 Park Bom\n ```')
        embed1.add_field(name='K.A.R.D', value=f'```\nK.A.R.D BM\nK.A.R.D Jiwoo\nK.A.R.D J.Seph\nK.A.R.D Somin\n ```')
        
        embed1.add_field(name='LOOΠΔ 1/3', value=f'''```\nLoona Heejin\nLoona Hyunjin\nLoona Haseul\nLoona ViVi\nLoona Yeojin```''')
        embed1.add_field(name='LOOΠΔ Odd Eye Circle', value=f'''```\nLoona Kim Lip\nLoona Jinsoul\nLoona Choerry\n \n ```''')
        embed1.add_field(name='LOOΠΔ yyxy', value=f'''```\nLoona Yves\nLoona Chuu\nLoona Go Won\nLoona Olivia Hye\n ```''')
        
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
        embed2.add_field(name='NCT [1]', value=f'''```\nNCT Lucas\nNCT Mark\nNCT Winwin\nNCT Jaemin\nNCT Jaehyun\nNCT Taeyong\nNCT Doyoung\nNCT Taeil\nNCT Chenle```''')
        embed2.add_field(name='NCT [2]', value=f'''```\nNCT Jungwoo\nNCT Renjun\nNCT Kun\nNCT Ten\nNCT Xiaojun\nNCT Haechan\nNCT Johnny\nNCT Sungchan\nNCT Shotaro```''')
        embed2.add_field(name='NCT [3]', value=f'''```\nNCT Hendery\nNCT Yangyang\nNCT Yuta\nNCT Jeno\nNCT Jisung\n \nNCT 127\nNCT Dream\nWayV```''')        
        
        embed2.add_field(name='Iz*One [1]', value=f'''```\nIz*One Sakura\nIz*One Yuri\nIz*One Chaeyeon\nIz*One Eunbi```''')
        embed2.add_field(name='Iz*One [2]', value=f'''```\nIz*One Minju\nIz*One Hyewon\nIz*One Wonyoung\nIz*One Nako```''')
        embed2.add_field(name='Iz*One [3]', value=f'''```\nIz*One Chaewon\nIz*One Yujin\nIz*One Yena\nIz*One Hitomi```''')
        
        embed2.add_field(name='Twice [1]', value=f'''```\nTwice Mina\nTwice Sana\nTwice Momo\nTwice Jeongyeon\nTwice Tzuyu\nTwice Nayeon\nTwice Dahyun\nTwice Chaeyoung\nTwice Jihyo```''')
        embed2.add_field(name='SNSD', value=f'''```\nSNSD YoonA\nSNSD Yuri\nSNSD Hyoyeon\nSNSD Sunny\nSNSD Tiffany\nSNSD Sooyoung\nSNSD Seohyun\nSNSD Jessica\nSNSD Taeyeon```''')
        embed2.add_field(name='Momoland', value=f'```\nMomoland Hyebin\nMomoland Jane\nMomoland Nayun\nMomoland JooE\nMomoland Ahin\nMomoland Nancy\n \n \n ```')
        embed2.add_field(name='Support:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)

    #//embed3
        embed3 = discord.Embed(
            title = 'COMMANDS',
            description = description,
            colour = discord.Color.from_rgb(198, 237, 154))
        embed3.set_footer(text=f"page 3/{totalpages}")
        embed3.add_field(name='aespa', value=f'''```\naespa Giselle\naespa Winter\naespa NingNing\naespa Karina```''')
        embed3.add_field(name='Blackpink', value=f'```\nBlackpink Lisa\nBlackpink Jennie\nBlackpink Jisoo\nBlackpink Rosé```', inline = True)
        embed3.add_field(name='Misc', value=f'```\nJessica\nKrystal\nKiki\n ```', inline = True)
        
        embed3.add_field(name='BTS', value=f'''```\nBTS V\nBTS Suga\nBTS J-hope\nBTS Jin\nBTS Jimin\nBTS RM\nBTS Jungkook```''')
        embed3.add_field(name='Enhypen', value=f'''```\nEnhypen Sunoo\nEnhypen Sunghoon\nEnhypen Jake\nEnhypen Jungwon\nEnhypen Heeseung\nEnhypen Jay\nEnhypen Ni-Ki```''')
        embed3.add_field(name='April', value=f'''```\nApril Chaekyung\nApril Chaewon\nApril Naeun\nApril Yena\nApril Rachel\nApril Jinsol\nApril Hyunjoo```''')
        
        embed3.add_field(name='TXT', value=f'''```\nTXT Soobin\nTXT Yeonjun\nTXT Beomgyu\nTXT Taehyun\nTXT Huening Kai```''')
        embed3.add_field(name='Itzy', value=f'''```\nItzy Yeji\nItzy Ryujin\nItzy Chaeryeong\nItzy Yuna\nItzy Lia```''')
        embed3.add_field(name='Red Velvet', value=f'```\nRed Velvet Joy\nRed Velvet Irene\nRed Velvet Seulgi\nRed Velvet Yeri\nRed Velvet Wendy```', inline = True)
        embed3.add_field(name='Support:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)

    #//embed4
        embed4 = discord.Embed(
            title = 'COMMANDS',
            description = description,
            colour = discord.Color.from_rgb(198, 237, 154))
        embed4.set_footer(text=f"page 4/{totalpages}")
        embed4.add_field(name='WEEEKLY', value=f'''```\nWEEEKLY Soojin\nWEEEKLY Monday\nWEEEKLY Jiyoon\nWEEEKLY Soeun\nWEEEKLY Jaehee\nWEEEKLY Jihan\nWEEEKLY Zoa```''')
        embed4.add_field(name='Purple Kiss', value=f'''```\nPurple Kiss Yuki\nPurple Kiss Na Goeun\nPurple Kiss Jieun\nPurple Kiss Dosie\nPurple Kiss Ireh\nPurple Kiss Chaein\nPurple Kiss Swan```''')
        embed4.add_field(name='CLC', value=f'''```\nCLC Yeeun\nCLC Sorn\nCLC Elkie\nCLC Eunbin\nCLC Yujin\nCLC Seunghee\nCLC Seungyeon```''')
        
        embed4.add_field(name='WJSN [1]', value=f'```\nWJSN Bona\nWJSN Cheng Xiao\nWJSN Dawon\nWJSN Dayoung\nWJSN Eunseo\nWJSN Exy\nWJSN Yeoreum```')
        embed4.add_field(name='WJSN [2]', value=f'```\nWJSN Luda\nWJSN Mei Qi\nWJSN Seola\nWJSN Soobin\nWJSN Yeonjung\nWJSN Xuan Yi\n ```')
        embed4.add_field(name='(G)I-dle', value=f'''```\n(G)I-dle Minnie\n(G)I-dle Miyeon\n(G)I-dle Shuhua\n(G)I-dle Soojin\n(G)I-dle Soyeon\n(G)I-dle Yuqi```''')
        
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
        embed5.add_field(name='Oh My Girl', value=f'```\nOh My Girl Arin\nOh My Girl Binnie\nOh My Girl Hyojung\nOh My Girl Jiho\nOh My Girl Mimi\nOh My Girl Seunghee\nOh My Girl YooA```')
        embed5.add_field(name='Dreamcatcher', value=f'```\nDreamcatcer Dami\nDreamcatcher JiU\nDreamcatcher Gahyeon\nDreamcatcher Handong\nDreamcatcher Siyeon\nDreamcatcher Sua\nDreamcatcher Yoohyeon```', inline = True)
        embed5.add_field(name='VAV', value=f'```\nVAV Ace\nVAV Ayno\nVAV Baron\nVAV Jacob\nVAV Lou\nVAV St.Van\nVAV Ziu```')
        
        embed5.add_field(name='Cherry Bullet', value=f'''```\nCherry Bullet Bora\nCherry Bullet Chaerin\nCherry Bullet Haeyoon\nCherry Bullet Jiwon\nCherry Bullet Kokoro```''')
        embed5.add_field(name='Cherry Bullet', value=f'''```\nCherry Bullet Linlin\nCherry Bullet May\nCherry Bullet Mirae\nCherry Bullet Remi\nCherry Bullet Yuju```''')
        embed5.add_field(name='EXID', value=f'''```\nEXID Hani\nEXID Jeonghwa\nEXID LE\nEXID Solji\nEXID Hyelin```''')

        embed5.add_field(name='SF9', value=f'```\nSF9 Chani\nSF9 Dawon\nSF9 Hwiyoung\nSF9 Inseong\nSF9 Jaeyoon\nSF9 Rowoon\nSF9 Yoo Taeyang\nSF9 Youngbin\nSF9 Zuho```')
        embed5.add_field(name='fromis_9', value=f'''```\nfromis_9 Jisun\nfromis_9 Hayoung\nfromis_9 Saerom\nfromis_9 Chaekyoung\nfromis_9 Nakyung\nfromis_9 Jiwon\nfromis_9 Seoyeon\nfromis_9 Jiheon\nfromis_9 Gyuri```''')
        embed5.add_field(name='EXO', value=f'''```\nEXO Kai\nEXO D.O.\nEXO Baekhyun\nEXO Chaenyeol\nEXO Sehun\nEXO Chen\nEXO Suho\nEXO Lay\nEXO Xiumin```''')
        embed5.add_field(name='Support:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)

    #//embed6
        embed6 = discord.Embed(
            title = 'COMMANDS',
            description = description,
            colour = discord.Color.from_rgb(198, 237, 154))
        embed6.set_footer(text=f"page 6/{totalpages}")
        embed6.add_field(name='Soloists', value=f'```\nNatty\nAleXa\nChung ha\nIU\nSomi\nYukika\nWOODZ\nTaemin```', inline = True)
        embed6.add_field(name='Soloists', value=f'```\nKris Wu\nLuhan\nTao\nKang Daniel\nSunmi\nYubin\nRothy\nHyuna```', inline = True)
        embed6.add_field(name='Everglow', value=f'''```\nEverglow Yiren\nEverglow E:U\nEverglow Mia\nEverglow Aisha\nEverglow Onda\nEverglow Sihyeon\n \n ```''')

        embed6.add_field(name='GWSN', value=f'```\nGWSN Seokyoung\nGWSN Seoryoung\nGWSN Soso\nGWSN Anne\nGWSN Minju\nGWSN Lena\nGWSN Miya```')
        embed6.add_field(name='Apink', value=f'```\nApink Bomi\nApink Chorong\nApink Eunji\nApink Hayoung\nApink Naeun\nApink Namjoo\n ```')
        embed6.add_field(name='Shinee', value=f'```\nShinee Jonghyun\nShinee Key\nShinee Taemin\nShinee Minho\nShinee Onew\nShinee```')

        embed6.add_field(name='Extra Commands', value=f'```\nFood\nChuu Heart\nS.E.S```')
        embed6.add_field(name='ASTRO', value=f'```\nASTRO Eunwoo\nASTRO MJ\n ```')
        embed6.add_field(name='Thank u', value=f'```\nThank you\nfor supporting\nMoonbyul```')
        embed6.add_field(name='Support:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)
        

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
                        await message.remove_reaction(reaction, user)
                    elif str(reaction.emoji) == "⬅️":
                        cur_page -= 1
                        await message.edit(embed=embed5)
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