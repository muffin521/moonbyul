import discord, random, os
import asyncio
from discord.ext import commands
from discord.utils import get
from random import choice
from discord.ext import commands


class hcommands(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def help(self, ctx):
        
        #pages = 2
        cur_page = 1
        #message = await ctx.send(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
        embed1 = discord.Embed(
            title = 'COMMANDS',
            description = 'All commands start with the prefix [=]',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed1.add_field(name='Mamamoo', value=f'```\nMamamoo\nMoonbyul\nHwasa\nSolar\nWheein ```', inline = True)
        embed1.add_field(name='Blackpink', value=f'```\nLisa\nJennie\nJisoo\nRose\n ```', inline = True)
        embed1.add_field(name='Red Velvet', value=f'```\nJoy\nIrene\nSeulgi\nYeri\nWendy```', inline = True)
        embed1.add_field(name='Mae & Ple\'s Commands', value=f'```\nJessica\nKrystal\nTaemin\nShuhua\nKiki ```', inline = True)
        embed1.add_field(name='Misc', value=f'```\nNatty\nYiren\nFood\nChuu Heart\n ```', inline = True)
        embed1.add_field(name='Misc [2]', value=f'```\nYeeun\nYein\nKei\nAleXa\n ```', inline = True)
        await ctx.message.delete()

        embed2 = discord.Embed(
            title = 'COMMANDS (2)',
            description = 'All commands start with the prefix [=]',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed2.add_field(name='Iz*One [1]', value=f'''```\nSakura\nYuri\nChaeyeon```''')
        embed2.add_field(name='Iz*One [2]', value=f'''```\nMinju\nHyewon\nWonyoung```''')
        embed2.add_field(name='Iz*One [3]', value=f'''```\n \n \n ```''')
        embed2.add_field(name='LOOΠΔ 1/3', value=f'''```\nHeejin\nHyunjin\nHaseul\nViVi\nYeojin```''')
        embed2.add_field(name='LOOΠΔ Odd Eye Circle', value=f'''```\nKim Lip\nJinsoul\nChoerry\n \n ```''')
        embed2.add_field(name='LOOΠΔ yyxy', value=f'''```\nYves\nChuu\nGo Won\nOlivia Hye\n ```''')

        embed3 = discord.Embed(
            title = 'COMMANDS (3)',
            description = 'All commands start with the prefix [=]',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed3.add_field(name='Twice [1]', value=f'''```\nMina\nSana\nMomo```''')
        embed3.add_field(name='Twice [2]', value=f'''```\nJeongyeon\nTzuyu\nNayeon```''')
        embed3.add_field(name='Twice [3]', value=f'''```\nDahyun\nChaeyoung\nJihyo```''')
        embed3.add_field(name='Stray Kids [1]', value=f'''```\nFelix\nsHyunjin\nBangchan\nLee Know```''')
        embed3.add_field(name='Stray Kids [2]', value=f'''```\nChangbin\nHan\nJeongin\nSeungmin```''')
        # embed3.add_field(name='1', value=f'''```\n \n \n \n ```''')
        
        embed4 = discord.Embed(
            title = 'COMMANDS (4)',
            description = 'All commands start with the prefix [=]',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed4.add_field(name='BTS [1]', value=f'''```\nV\nSuga\nJ-hope\nJungkook```''')
        embed4.add_field(name='BTS [2]', value=f'''```\nJin\nJimin\nRM\n ```''')
        embed4.add_field(name='aespa', value=f'''```\nGiselle\nWinter\n \n ```''', inline = False)
        # embed4.add_field(name='Stray Kids [1]', value=f'''```\nFelix\nsHyunjin\nBangchan\nLee Know```''')
        # embed4.add_field(name='Stray Kids [2]', value=f'''```\nChangbin\nHan\nJeongin\nSeungmin```''')
        # embed4.add_field(name='1', value=f'''```\n \n \n \n ```''')

        # getting the message object for editing and reacting


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
                    elif str(reaction.emoji) == "⬅️":
                        cur_page -= 1
                        await message.edit(embed=embed2)
                        await message.remove_reaction(reaction, user)
                
                elif cur_page == 4:
                    if str(reaction.emoji) == "➡️":
                        await message.remove_reaction(reaction, user)
                    elif str(reaction.emoji) == "⬅️":
                        cur_page -= 1
                        await message.edit(embed=embed3)
                        await message.remove_reaction(reaction, user)

                else:
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
