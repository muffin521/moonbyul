import discord, random, os
import asyncio
from discord.ext import commands
from discord.utils import get
from random import choice


class hcommands(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def help(self, ctx):
        
        #pages = 2
        cur_page = 1
        #message = await ctx.send(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
    #//embed 1
        embed1 = discord.Embed(
            title = 'COMMANDS',
            description = 'All commands start with the prefix [=]\nTo invite the bot to your server, try `=invite`',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed1.set_footer(text="page 1/5")
        embed1.add_field(name='Mamamoo', value=f'```\nMamamoo\nMoonbyul\nHwasa\nSolar\nWheein```', inline = True)
        embed1.add_field(name='Itzy', value=f'''```\nYeji\nRyunjin\nChaeryeong\nYuna\nLia```''')
        embed1.add_field(name='Red Velvet', value=f'```\nJoy\nIrene\nSeulgi\nYeri\nWendy```', inline = True)
        embed1.add_field(name='aespa', value=f'''```\nGiselle\nWinter\nNingNing\nKarina\n ```''')
        embed1.add_field(name='Mae & Ple\'s Commands', value=f'```\nJessica\nKrystal\nTaemin\nKiki\n ```', inline = True)
        embed1.add_field(name='Blackpink', value=f'```\nLisa\nJennie\nJisoo\nRose\n ```', inline = True)
        embed1.add_field(name='Misc', value=f'```\nS.E.S\nJiU\nCL\n \n \n ```', inline = True)
        embed1.add_field(name='Soloists', value=f'```\nNatty\nAleXa\nChung ha\nIU\nSomi\nYukika```', inline = True)
        embed1.add_field(name='Extra Commands', value=f'```\nFood\nChuu Heart\n \n \n \n ```', inline = True)
        embed1.add_field(name='Support:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)
        
    #//embed2
        embed2 = discord.Embed(
            title = 'COMMANDS',
            description = 'All commands start with the prefix [=]\nTo invite the bot to your server, try `=invite`',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed2.set_footer(text="page 2/5")
        embed2.add_field(name='Iz*One [1]', value=f'''```\nSakura\nYuri\nChaeyeon\nEunbi```''')
        embed2.add_field(name='Iz*One [2]', value=f'''```\nMinju\nHyewon\nWonyoung\nNako```''')
        embed2.add_field(name='Iz*One [3]', value=f'''```\nChaewon\nYujin\nYena\nHitomi```''')
        embed2.add_field(name='LOOΠΔ 1/3', value=f'''```\nHeejin\nHyunjin\nHaseul\nViVi\nYeojin```''')
        embed2.add_field(name='LOOΠΔ Odd Eye Circle', value=f'''```\nKim Lip\nJinsoul\nChoerry\n \n ```''')
        embed2.add_field(name='LOOΠΔ yyxy', value=f'''```\nYves\nChuu\nGo Won\nOlivia Hye\n ```''')
        embed2.add_field(name='Twice [1]', value=f'''```\nMina\nSana\nMomo```''')
        embed2.add_field(name='Twice [2]', value=f'''```\nJeongyeon\nTzuyu\nNayeon```''')
        embed2.add_field(name='Twice [3]', value=f'''```\nDahyun\nChaeyoung\nJihyo```''')
        embed2.add_field(name='Support:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)

    #//embed3
        embed3 = discord.Embed(
            title = 'COMMANDS',
            description = 'All commands start with the prefix [=]\nTo invite the bot to your server, try `=invite`',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed3.set_footer(text="page 3/5")
        embed3.add_field(name='Stray Kids [1]', value=f'''```\nFelix\nsHyunjin\nBangchan```''')
        embed3.add_field(name='Stray Kids [2]', value=f'''```\nChangbin\nHan\nJeongin ```''')
        embed3.add_field(name='Stray Kids [3]', value=f'''```\nLee Know\nSeungmin\n ```''')
        embed3.add_field(name='BTS [1]', value=f'''```\nV\nSuga\nJ-hope```''')
        embed3.add_field(name='BTS [2]', value=f'''```\nJin\nJimin\nRM```''')
        embed3.add_field(name='BTS [3]', value=f'''```\nJungkook\n \n ```''')
        embed3.add_field(name='Enhypen [1]', value=f'''```\nSunoo\nSunghoon\nJake```''')
        embed3.add_field(name='Enhypen [2]', value=f'''```\nJungwon\nHeeseung\nJay```''')
        embed3.add_field(name='Enhypen [3]', value=f'''```\nNi-Ki\n \n ```''')
        embed3.add_field(name='Support:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)

    #//embed4
        embed4 = discord.Embed(
            title = 'COMMANDS',
            description = 'All commands start with the prefix [=]\nTo invite the bot to your server, try `=invite`',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed4.set_footer(text="page 4/5")
        embed4.add_field(name='(G)I-dle', value=f'''```\nMinnie\nMiyeon\nShuhua\nSoojin\nSoyeon\nYuqi```''')
        embed4.add_field(name='Lovelyz', value=f'''```\nBaby Soul\nYein\nKei\nlJisoo\n \n ```''')
        embed4.add_field(name='Lovelyz [2]', value=f'''```\nMijoo\nJiae\nlJin\nSujeong\n \n ```''')
        embed4.add_field(name='Everglow', value=f'''```\nYiren\nE:U\nMia\nAisha\nOnda\nSihyeon\n ```''')
        embed4.add_field(name='Purple K!ss', value=f'''```\nYuki\nNa Goeun\nJieun\nDosie\nIreh\nChaein\nSwan```''')
        embed4.add_field(name='CLC', value=f'''```\nYeeun\nSorn\nElkie\nEunbin\ncYujin\ncSeunghee\nSeungyeon```''')
        embed4.add_field(name='TXT', value=f'''```\nSoobin\nYeonjun\nBeomgyu\nTaehyun\nHuening Kai```''')
        embed4.add_field(name='NCT', value=f'''```\nLucas\nMark\nWinwin\nJaemin\nJaehyun```''')
        embed4.add_field(name='EXID', value=f'''```\nHani\nJeonghwa\nLE\nSolji\nHyelin```''')
        embed4.add_field(name='Support:', value=f'\nhttps://discord.gg/Ntk9Jp26yx', inline = False)

    #//embed5
        embed5 = discord.Embed(
            title = 'COMMANDS',
            description = 'All commands start with the prefix [=]\nTo invite the bot to your server, try `=invite`',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed5.set_footer(text="page 5/5")
        embed5.add_field(name='WEEEKLY', value=f'''```\nwSoojin\nMonday\nJiyoon\nSoeun\nJaehee\nJihan\nZoa```''')
        embed5.add_field(name='Cherry Bullet', value=f'''```\nJiwon\nYuju\nBora\nHaeyoon\n \n \n ```''')

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
                        await message.remove_reaction(reaction, user)
                    elif str(reaction.emoji) == "⬅️":
                        cur_page -= 1
                        await message.edit(embed=embed4)
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


    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            title = 'Invite Links',
            description = 'lob u <:moonbyulheart:790333102924627968>‎',
            colour = discord.Colour.from_rgb(198, 237, 154))
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/775473868277284885/778452371607912518/Blue_Moonbyul.jpg')
        embed.add_field(name='Support Server', value=f'https://discord.gg/Ntk9Jp26yx', inline=True)
        embed.add_field(name='Invite Link', value=f'‏‏‎[Moonbyul Invite](https://discord.com/oauth2/authorize?client_id=770750635850858506&scope=bot&permissions=8)', inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(hcommands(client))
