import discord
from discord.ext import commands
from discord import app_commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(
        name="ping",
        description="Проверить бота"
    )
    async def ping(
        self,
        interaction: discord.Interaction
    ):

        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Пинг: {round(self.bot.latency * 1000)}ms",
            color=discord.Color.pink()
        )

        await interaction.response.send_message(
            embed=embed
        )


async def setup(bot):
    await bot.add_cog(Moderation(bot))