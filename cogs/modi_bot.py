import discord
from discord.ext import commands


class modi():
    def __init__(self, bot: commands.Bot, special_cogs):
        self.bot = bot
        self.special_cogs = special_cogs

    @commands.group(pass_context=True)
    async def mod(self, ctx):
        '''
        Base command for all module tinkering.
        '''
        if (ctx.invoked_subcommand is None):
            await self.bot.say("This command must be invoked with a subcommand (`unload`, `load`, or `reload`)!")

    @mod.command(pass_context=True)
    async def load(self, ctx, module: str):
        '''
        Load a module.
        '''
        if (ctx.message.author.id == "164342765394591744" and module not in self.special_cogs):
            self.bot.load_extension(module)
            await self.bot.say("Loaded `{}`".format(module))

    @mod.command(pass_context=True)
    async def unload(self, ctx, module: str):
        '''
        Unload a module.
        '''
        if (ctx.message.author.id == "164342765394591744" and module not in self.special_cogs):
            self.bot.unload_extension(module)
            await self.bot.say("Unloaded `{}`".format(module))

    @mod.command(pass_context=True)
    async def reload(self, ctx, module: str):
        '''
        Reload a module.
        '''
        await ctx.invoke(self.unload, module)
        await ctx.invoke(self.load, module)


def setup(bot: commands.Bot):
    bot.add_cog(modi(bot, ["main", "modi_bot"]))