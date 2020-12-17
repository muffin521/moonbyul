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
    #^CLC

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
import os
from discord.ext import commands

#this sets prefix to '='
client = commands.Bot(command_prefix= '==')
#takes out help command
client.remove_command('help')

#did it start?
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('=help'))
    # activity = discord.Activity(name='Queendom', type=discord.ActivityType.watching)
    # await client.change_presence(activity=activity)
    print('Existance is pain')

# This loads the cogs.
@client.command()
async def load(ctx, extention):
    client.load_extension(f'cogs.{extention}')
    print(f'Loaded cogs.{extention}')
    await ctx.send(f'Loaded cogs.{extention}')

# This unloads the cogs.
@client.command()
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')
    print(f'Unloaded cogs.{extention}')
    await ctx.send(f'Unloaded cogs.{extention}')

# This loop checks the cogs folder to see if there is a .py file. if there is it will load it as a cog.
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_message(message):
    message.content = message.content.lower()
    await client.process_commands(message)

client.run('NzcwNzUwNjM1ODUwODU4NTA2.X5iHdw.GfBE19DGGzfFhTu2_4qz0o0n_I0')