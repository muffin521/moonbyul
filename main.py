# invite link: https://discord.com/oauth2/authorize?client_id=770750635850858506&scope=bot&permissions=8

# purpose: pretty girls hehehehe
    #!
    #todo
    #^
    #//
    #*
    #=
    #?
    #~
    #&
    #.

#todo:
    #!status command- owner, helpers, ping(?)
    #*Devin "let's go" confetti command (JST server) #//can i do this??

    #?Minzy
    #?Dara
    #?Bom
#//custom emojis~ look at kei command in `Lovelyz Pings.py`
#//discord hex code colour (bg) #36393F


#todo GIT COMMANDS
    #*Link: "https://www.youtube.com/watch?v=BPvg9bndP1U&start=34s"
    #=git commit -am "message for commit"
    #=git push heroku master

    #//optional:
    #=git add .
        #=if I've added new files
    #=heroku logs -a moonbyul
    #=for my github: git push origin master



import discord
import random
import json
import os
from discord.ext import commands

muffin = 488423352206229505

#//prefix things
# Checks 'prefix.json' for prefixes.
def get_prefix(client, message):
    with open("./json/prefix.json", "r") as f:
        prefix = json.load(f)
    return prefix[str(message.guild.id)]


#this sets prefix to '='
client = commands.Bot(command_prefix= '==')
#takes out help command
client.remove_command('help')

# Default prefix = '='
# @client.event
# async def on_guild_join(guild):
#     with open("./json/prefix.json", "r") as f:
#         prefix = json.load(f)
#     prefix[str(guild.id)] = "="
#     with open("./json/prefix.json", "w") as f:
#         json.dump(prefix, f, indent = 4)

# # Remove prefix on server leave.
# @client.event
# async def on_guild_remove(guild):
#     with open("./json/prefix.json", "r") as f:
#         prefix = json.load(f)
#     prefix.pop(str(guild.id))
#     with open("./json/prefix.json", "w") as f:
#         json.dump(prefix, f, indent = 4)

# # Change Prefix command.
# @client.command(aliases = ['moonbyulprefix', 'changeprefix', 'byulprefix'])
# @commands.has_permissions(manage_messages=True)
# async def prefix(ctx, message):
#     with open("./json/prefix.json", "r") as f:
#         prefix = json.load(f)
#     prefix[str(ctx.guild.id)] = f"{message}"
#     with open("./json/prefix.json", "w") as f:
#         json.dump(prefix, f, indent = 4)
#     embed=discord.Embed(
#         description = f"Changed the servers prefix to `{message}`",
#         colour = discord.Color.from_rgb(59,214,198))
#     await ctx.send(embed=embed)



#did it start?
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('=help'))
    # activity = discord.Activity(name='Queendom', type=discord.ActivityType.watching)
    # await client.change_presence(activity=activity)
    print('I say Mama-Mamamoo')



#//cogs
# This loads the cogs.
@client.command()
async def load(ctx, extention):
    if ctx.author.id == muffin:
        client.load_extension(f'cogs.{extention}')
        print(f'Loaded cogs.{extention}')
        await ctx.send(f'Loaded cogs.{extention}')
    else:
        await ctx.send(f'Fuck off, no perms')

# This unloads the cogs.
@client.command()
async def unload(ctx, extention):
    if ctx.author.id == muffin:
        client.unload_extension(f'cogs.{extention}')
        print(f'Unloaded cogs.{extention}')
        await ctx.send(f'Unloaded cogs.{extention}')
    else:
        await ctx.send(f'Fuck off, no perms')

# This reloads the cogs.
@client.command()
async def reload(ctx, extention):
    if ctx.author.id == muffin:
        client.unload_extension(f"cogs.{extention}")
        client.load_extension(f"cogs.{extention}")
        print(f"Reloaded cogs.{extention}")
        embed=discord.Embed(
            description = f"`{extention}` cog Reloaded",
            colour = discord.Color.from_rgb(198, 237, 154))
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(
                description = f"<@!{ctx.author.id}>, Fuck off, no perms!",
                colour = discord.Color.from_rgb(198, 237, 154))
        await ctx.send(embed=embed)

# This loop checks the cogs folder to see if there is a .py file. if there is it will load it as a cog.
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_message(message):
    message.content = message.content.lower()
    await client.process_commands(message)

client.run('NzcwNzUwNjM1ODUwODU4NTA2.X5iHdw.GfBE19DGGzfFhTu2_4qz0o0n_I0')