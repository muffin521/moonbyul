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
        pages = 2
        cur_page = 1
        #message = await ctx.send(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
        embed1 = discord.Embed(
            title = 'COMMANDS',
            description = 'All commands start with the prefix [=]',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed1.add_field(name='Mamamoo', value=f'```\nMoonbyul\nHwasa\nSolar\nWheein\n ```', inline = True)
        embed1.add_field(name='Blackpink', value=f'```\nLisa\nJennie\nJisoo\nRose\n ```', inline = True)
        embed1.add_field(name='Red Velvet', value=f'```\nJoy\nIrene\nSeulgi\nYeri\nWendy```', inline = True)
        embed1.add_field(name='Mae\'s Commands', value=f'```\nJessica\nKrystal\nTaemin\n ```', inline = True)
        embed1.add_field(name='Ple\'s Commands', value=f'```\nShuhua\nKiki\n \n ```', inline = True)
        embed1.add_field(name='Misc', value=f'```\nNatty\nYiren\nFood\nChuu Heart```', inline = True)
        await ctx.message.delete()

        embed2 = discord.Embed(
            title = 'COMMANDS (2)',
            description = 'All commands start with the prefix [=]',
            colour = discord.Color.from_rgb(198, 237, 154))
        embed2.add_field(name='Iz*One [1]', value=f'''```\nSakura\nYuri\nChaeyeon```''')
        embed2.add_field(name='Iz*One [2]', value=f'''```\nMinju\nHyewon\nWonyoung```''')
        embed2.add_field(name='Iz*One [3]', value=f'''```\n \n \n ```''')
        embed2.add_field(name='LOOΠΔ 1/3', value=f'''```\nHeejin\nHyunjin```''')
        embed2.add_field(name='LOOΠΔ Odd Eye Circle', value=f'''```\nKim Lip\nChoerry```''')
        embed2.add_field(name='LOOΠΔ yyxy', value=f'''```\n \n ```''')
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

                if str(reaction.emoji) == "➡️" and cur_page != pages:
                    cur_page += 1
                    await message.edit(embed=embed2)
                    await message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == "⬅️" and cur_page > 1:
                    cur_page -= 1
                    await message.edit(embed=embed1)
                    await message.remove_reaction(reaction, user)

                # elif str(reaction.emoji) == "➡️" and cur_page == 2:
                #     cur_page += 1
                #     await message.edit(embed=embed3)
                #     await message.remove_reaction(reaction, user)

                else:
                    await message.remove_reaction(reaction, user)
                    # removes reactions if the user tries to go forward on the last page or
                    # backwards on the first page
            except asyncio.TimeoutError:
                #await message.delete()
                await message.clear_reactions()
                break
                # ending the loop if user doesn't react after x seconds



#     #?Help Command [basic]
#     @commands.command()
#     async def help(self, ctx):
#         embed=discord.Embed(
#             title = 'HELP',
#             description = 'All commands start with the prefix [=]',
#             colour = discord.Color.from_rgb(198, 237, 154))
#         embed.add_field(name='Help Commands', value=f'''```
# Iz*One
# Blackpink
# Mamamoo
# Loona
# Red Velvet
# Others
# ```''')
#         embed.add_field(name='Help', value=f'''
# DM <@!{488423352206229505}>
# to get your
# command added
# or with 
# questions! 
# ''')
#         embed.add_field(name='Thanks to:', value=f'''\n<@389897179701182465>''')
#         await ctx.send(embed=embed)
#         await ctx.message.delete()


#     #?loona help command
#     @commands.command(aliases = ['helplooπδ'])
#     async def helploona(self, ctx):
#         embed=discord.Embed(
#             title = 'IZ*ONE',
#             description = 'All commands start with the prefix [=]',
#             colour = discord.Color.from_rgb(198, 237, 154))
#         embed.add_field(name='1/3', value=f'''```\nHeejin\nHyunjin```''')
#         embed.add_field(name='Odd Eye Circle', value=f'''``````''')
#         await ctx.send(embed=embed)
#         await ctx.message.delete()



def setup(client):
    client.add_cog(hcommands(client))
