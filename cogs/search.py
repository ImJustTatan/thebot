import asyncio
import discord
import discord.ext.commands as cmd
import praw
import prawcore
import random
import yippi
from cogs.scripts import youtube

import srcomapi
import srcomapi.datatypes as dt

import time

sapi = srcomapi.SpeedrunCom()

rapi = praw.Reddit(client_id="PEwwoOgGbp1onQ",
                   client_secret="0YINpE0eODb0vDvK-u1EnMCfGq4",
                   user_agent="test^2bot-discordbot[python] v0.5 (by /u/thehellbell)")

extn = ["jpg", "png", "gif", "jpeg", "gifv"]


class Searching:
    def __init__(self, bot):
        self.bot = bot

    @cmd.group(name="speedrun", pass_context=True, aliases=["sr"])
    async def speedrun(self, ctx):
        """Options for the speedrun.com API (>>help sr)."""
        if ctx.invoked_subcommand is None:
            await ctx.send("Please see >>help sr for correct usage.")

    @cmd.command(aliases=["yt"])
    async def youtube(self, ctx, *, msg=None):
        """Uses YouTube search with a given input, and returns the first result."""
        if msg is None:
            await ctx.send("Please input the search query!")
            return
        key = youtube.search(msg)
        key = key[0]
        await ctx.send("http://www.youtube.com/watch?v=" + key)

    @cmd.command(pass_context=True, aliases=['e6', 'fur'])
    async def e621(self, ctx, rating=None, *, tags=None):
        """Searches in e621 (>>help e621 for usage)."""
        if not ctx.channel.is_nsfw():
            await ctx.send(":underage: Works in NSFW channels only.")
            return
        try:
            tags = tags.split()
        except AttributeError:
            await ctx.send("Incorrect usage (view >>help e621)")
            return
        if rating not in ["s", "q", "e"]:
            await ctx.send("Please use a correct rating (s for Safe, q for Questionable, e for Explicit).")
            return
        else:
            res = yippi.search().post(tags, rating=rating)
            res = random.choice(res)

            if type(res.artist) == list:
                artist = "; ".join(res.artist)
            else:
                artist = res.artist

            if artist is None:
                artist = "Unknown"

            t = {"webm": "WEBM Video File",
                 "gif": "GIF Animated Image",
                 "png": "PNG Image",
                 "jpg": "JPG Image",
                 "jpeg": "JPEG Image",
                 "swf": "Shockwave Flash File"}

            if res.file_ext in extn:
                e = discord.Embed(title="Search Results - Post #" + str(res.id),
                                  url="https://e621.net/post/show/" + str(res.id),
                                  color=discord.Color(0x3F499A),
                                  description="**Score: **" + str(res.score) + "\n**Artist: **" + artist + "\n**File Type: **" + t[res.file_ext])
                e.set_image(url=res.file_url)
                await ctx.send(embed=e)
            else:
                await ctx.send("**Score: **" + str(res.score) + "\n**Artist: **" + artist + "\n**File Type: **" + t[res.file_ext] + "\n**Link: **" + res.file_url)

    @speedrun.command()
    async def wr(self, ctx, *, game):
        """With a given game, displays the world record for a category"""
        a = ctx.message.author

        def check(m):
            return m.author == a and int(m.content) > 0 and int(m.content) < 11 and m.channel == ctx.channel

        g = sapi.search(dt.Game, {"name": game})
        x = "1.- " + g[0].name
        if len(g) > 10:
            for i in range(9):
                x += "\n" + str(i + 2) + ".- " + g[i + 1].name
        else:
            for i in range(len(g) - 1):
                x += "\n" + str(i + 2) + ".- " + g[i + 1].name
        l = await ctx.send("**SEARCH RESULTS** - Please select a number from below:\n" + x)

        try:
            msg = await self.bot.wait_for('message', check=check, timeout=30)
        except asyncio.TimeoutError:
            await l.edit(content="Timeout.")
            return
        except ValueError:
            await ctx.send("Please input a valid response.")

        g = g[int(msg.content) - 1]
        await l.edit(content=":white_check_mark: You selected: <" + g.name + ">")

        c = g.categories
        e = ""
        if len(c[0].records[0].runs) == 0:
            e = " <empty>"
        x = "1.- " + c[0].name + e
        e = ""
        if len(c) > 10:
            for i in range(9):
                if len(c[i + 1].records[0].runs) == 0:
                    e = " <empty>"
                x += "\n" + str(i + 2) + ".- " + c[i + 1].name + e
                e = ""
        else:
            for i in range(len(c) - 1):
                if len(c[i + 1].records[0].runs) == 0:
                    e = " <empty>"
                x += "\n" + str(i + 2) + ".- " + c[i + 1].name + e
                e = ""
        l = await ctx.send("**CATEGORIES** - Please select a number from below:\n" + x)

        try:
            msg = await self.bot.wait_for('message', check=check, timeout=30)
        except asyncio.TimeoutError:
            await l.edit(content="Timeout.")
            return
        except ValueError:
            await ctx.send("Please input a valid response.")

        c = c[int(msg.content) - 1]
        await l.edit(content=":white_check_mark: You selected: <" + c.name + ">")

        r = c.records[0].runs[0]["run"]

        u = []

        for user in r.players:
            u.append(user.name)

        u = "; ".join(u)

        rt = time.strftime('%H:%M:%S', time.gmtime(r.times["realtime_t"]))
        igt = time.strftime('%H:%M:%S', time.gmtime(r.times["ingame_t"]))

        await ctx.send("The world record for " + g.name + " in the <" + c.name + "> category is held by the user(s) " + u + ".\nReal Time: " + rt + "\nIn-game Time: " + igt + "\nLink: " + r.weblink)


def setup(bot):
    bot.add_cog(Searching(bot))
