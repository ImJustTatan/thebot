import asyncio
import discord
import discord.ext.commands as cmd


class Information:
    def __init__(self, bot):
        self.bot = bot

    @cmd.command()
    async def servinfo(self, ctx):
        """Displays info about the server."""
        g = ctx.guild
        if g.mfa_level == 1:
            a = "The server requires 2FA for administration."
        else:
            a = "The server doesn't require 2FA for administration."
        e = discord.Embed(title="SERVER INFO",
                          color=discord.Colour(0x00ff00),
                          description="**Server name is** " + str(g.name) + ".\n\n**Created at:** " + str(g.created_at) + " UTC.\n\n**Server ID is** " + str(g.id) + "~\n\n**Server owner is** " + str(g.owner) + "~\n\n" + a + "\n\nThere are " + str(g.member_count) + " members.")
        e.set_thumbnail(url=g.icon_url)
        e.set_author(name="^_^")
        e.set_footer(text="Command requested by " + str(ctx.author) + ".")
        await ctx.send(embed=e)

    @cmd.command()
    async def botinfo(self, ctx):
        """Displays info about the bot user."""
        e = discord.Embed(title="**BOT INFO**",
                          description="""**Owner is **""" + str(self.bot.get_user(264195450859552779)) + """
**The bot was created** at """ + str(self.bot.user.created_at) + """~
**The bot is present** in """ + str(len(self.bot.guilds)) + " server(s)~")
        e.set_image(url=self.bot.user.avatar_url)
        e.set_thumbnail(url=ctx.author.avatar_url)
        e.set_footer(text="La weá weón fsdfdslkñsfls.")
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Information(bot))
