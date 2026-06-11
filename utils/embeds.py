import discord
from config import MAIN_COLOR


def create_embed(title, description=None):

    embed = discord.Embed(
        title=title,
        description=description,
        color=MAIN_COLOR
    )

    return embed