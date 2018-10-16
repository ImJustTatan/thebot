import asyncio
import discord
import discord.ext.commands as cmd

import os
import sys

ownerid = 264195450859552779

bot = cmd.Bot(command_prefix=">>",
              owner_id=ownerid,
              description="haha yes")

cogs_ = ["cogs.owner",
         "cogs.info",
         "cogs.search"] 

for cog in cogs_:
    bot.load_extension(cog)
    print("Loaded <" + cog + ">")

@bot.event
async def on_ready():
    ownerdata = bot.get_user(ownerid)
    print('Logged in as {0}'.format(bot.user))
    print("Created by {0}".format(ownerdata))
    print("Using discord.py v" + discord.__version__)
    print("__________________________________________________________________________")
    games = discord.Game('>>help')
    await bot.change_presence(activity=games)

@bot.event
async def on_member_join(ctx, member):
    await member.guild.get_channel(499773739144052739).send("Welcome to the server, {0}! ^^".format(member))
    
"""@bot.command()
@cmd.is_owner()
async def reload(ctx, cog="all"):
    """"""Reloads a given cog, or all of them.""""""
    if cog != "all":
        cog = "cogs." + cog
        try:
            bot.unload_extension(cog)
            bot.load_extension(cog)
        except ModuleNotFoundError:
            await ctx.send("Input a valid cog filename please!")
            return 
        print("Reloaded <" + cog + ">")
        await ctx.send("Reloaded <" + cog + ">")
    else:
        for cog in cogs_:
            bot.unload_extension(cog)
            bot.load_extension(cog)
            print("Reloaded <" + cog + ">")
            await ctx.send("Reloaded <" + cog + ">")"""

bot.run(os.environ['BOT_TOKEN'])
