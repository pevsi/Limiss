import random
import io
import aiohttp
import discord

from PIL import Image
from PIL import ImageOps

from discord import app_commands
from discord.ext import commands

from config import MAIN_COLOR

BROKEN_EMOJI = "<:broken:1514252311369617532>"
WHITE_EMOJI = "<:white:1514449214892146688>"
PINK_EMOJI = "<:pink:1514246601823092787>"
RED_EMOJI = "<:red:1514449200707014787>"

PERCENT_EMOJI = "<:three:1514449183329747045>"

BROKEN_HEART = "/home/container/assets/hearts/broken.png"
WHITE_HEART = "/home/container/assets/hearts/white.png"
PINK_HEART = "/home/container/assets/hearts/pink.png"
RED_HEART = "/home/container/assets/hearts/red.png"


class Ship(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def get_avatar(self, user: discord.Member):

        async with aiohttp.ClientSession() as session:

            async with session.get(
                user.display_avatar.replace(
                    size=256,
                    format="png"
                ).url
            ) as resp:

                data = await resp.read()

        return Image.open(
            io.BytesIO(data)
        ).convert("RGBA")

    def circle_avatar(self, avatar, size=180):

        avatar = avatar.resize(
            (size, size)
        )

        mask = Image.new(
            "L",
            (size, size),
            0
        )

        from PIL import ImageDraw

        draw = ImageDraw.Draw(mask)

        draw.ellipse(
            (0, 0, size, size),
            fill=255
        )

        result = Image.new(
            "RGBA",
            (size, size),
            (0, 0, 0, 0)
        )

        result.paste(
            avatar,
            (0, 0),
            mask
        )

        return result

    async def create_ship_image(
        self,
        user1,
        user2,
        heart_path
    ):

        avatar1 = await self.get_avatar(user1)
        avatar2 = await self.get_avatar(user2)

        avatar1 = self.circle_avatar(avatar1)
        avatar2 = self.circle_avatar(avatar2)

        heart = Image.open(
            heart_path
        ).convert("RGBA")

        heart = heart.resize(
            (140, 140)
        )

        canvas = Image.new(
            "RGBA",
            (560, 200),
            (0, 0, 0, 0)
        )

        canvas.paste(
            avatar1,
            (0, 10),
            avatar1
        )

        canvas.paste(
            heart,
            (210, 30),
            heart
        )

        canvas.paste(
            avatar2,
            (380, 10),
            avatar2
        )

        buffer = io.BytesIO()

        canvas.save(
            buffer,
            format="PNG"
        )

        buffer.seek(0)

        return buffer

    @app_commands.command(
        name="ship",
        description="Проверить совместимость"
    )
    async def ship(
        self,
        interaction: discord.Interaction,
        пользователь1: discord.Member,
        пользователь2: discord.Member
    ):

        percent = random.randint(
            1,
            100
        )

        if percent <= 25:

            heart_emoji = BROKEN_EMOJI
            heart_file = BROKEN_HEART
            text = "💔 Не совместимы"

        elif percent <= 50:

            heart_emoji = WHITE_EMOJI
            heart_file = WHITE_HEART
            text = "🤍 Хорошие друзья"

        elif percent <= 75:

            heart_emoji = PINK_EMOJI
            heart_file = PINK_HEART
            text = "💖 Есть шанс на что-то большее"

        else:

            heart_emoji = RED_EMOJI
            heart_file = RED_HEART
            text = "💗 Вы должны быть вместе, это судьба!"

        image = await self.create_ship_image(
            пользователь1,
            пользователь2,
            heart_file
        )

        file = discord.File(
            image,
            filename="ship.png"
        )

        embed = discord.Embed(
            description=(
                f"# ***{пользователь1.display_name} "
                f"{heart_emoji} "
                f"{пользователь2.display_name}***\n\n"
                f"{PERCENT_EMOJI} **{percent}%**\n"
                f"{text}"
            ),
            color=MAIN_COLOR
        )

        embed.set_image(
            url="attachment://ship.png"
        )

        await interaction.response.send_message(
            embed=embed,
            file=file
        )


async def setup(bot):

    await bot.add_cog(
        Ship(bot)
    )