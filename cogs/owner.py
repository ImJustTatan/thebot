import asyncio
import discord
import discord.ext.commands as cmd


class Owner:
    def __init__(self, bot):
        self.bot = bot

    @cmd.group(name='settings', pass_context=True,
                    aliases=['cfg', 'set'])
    @cmd.is_owner()
    async def settings(self, ctx):
        """Settings and other owner-only stuff."""
        if ctx.invoked_subcommand is None:
            await ctx.send("Please select a subcommand.")

    @settings.command(aliases=["name", "usern"])
    async def username(self, ctx, *, n=None):
        """Changes the bot's username."""
        if n is None:
            await ctx.send("Please input a name.")
        else:
            on = self.bot.user.name
            await self.bot.user.edit(username=n)
            await ctx.send("Username changed from '" + on + "' to '" + n + "'.")

    @settings.command(aliases=["off", "log_off", "logoff"])
    async def log_out(self, ctx):
        """Shuts down the bot."""
        await ctx.send("Good bye.")
        await self.bot.logout()


def setup(bot):
    bot.add_cog(Owner(bot))
