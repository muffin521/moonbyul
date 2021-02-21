import discord, random
from discord.ext import commands
from datetime import datetime

class miniGames(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rockpapertuna(self, ctx, p2: discord.Member):
        p1 = ctx.author.mention
        p2 = p2.mention
        message = await ctx.send(f'Dog Cat Tuna')
        await message.add_reaction("🐶")
        await message.add_reaction("🐈")
        await message.add_reaction("🐟")

        def p1check(reaction, user):
            # if user == p1:
            return user == p1 and str(reaction.emoji) in ["🐶", "🐈", "🐟"]

        def p2check(reaction, user):
            # if user == p2:
            return user == p2 and str(reaction.emoji) in ["🐶", "🐈", "🐟"]

        p1pick = await ctx.bot.wait_for("reaction_add", check = p1check)

        p2pick = await ctx.bot.wait_for("reaction_add", check = p2check)

        if (p1pick == p2pick):
            await ctx.send(f'it\'s a tie!')

        # p1reaction = p1pick.content


        # if p1check == p1 and "🐶":
        #     if p2check == p2 and "🐶":
        #         await ctx.send(f'it\'s a tie, try again!')
        #     elif p2check == "🐈":
        #         await ctx.send(f'{p1} won!')
        #     elif p2check == "🐟":
        #         await ctx.send(f'{p2} won!')




def setup(client):
    client.add_cog(miniGames(client))