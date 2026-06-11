import sqlite3

import discord

from discord.ext import commands
from discord import app_commands

from config import (
    MAIN_COLOR,
    SUPPORT_PANEL_CHANNEL,
    COMPLAINTS_CHANNEL,
    SUGGESTIONS_CHANNEL
)


DB_PATH = "database/support.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS complaints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT DEFAULT 'pending',
        handler_id INTEGER,
        ticket_channel_id INTEGER,
        reason TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS suggestions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT DEFAULT 'pending',
        handler_id INTEGER,
        ticket_channel_id INTEGER,
        reason TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


class ComplaintModal(discord.ui.Modal, title="Подать жалобу"):

    complaint_title = discord.ui.TextInput(
        label="Название жалобы",
        max_length=100
    )

    complaint_description = discord.ui.TextInput(
        label="Описание жалобы",
        style=discord.TextStyle.paragraph,
        max_length=2000
    )

    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

        conn = sqlite3.connect(DB_PATH)

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO complaints
            (
                user_id,
                title,
                description
            )
            VALUES (?, ?, ?)
            """,
            (
                interaction.user.id,
                str(self.complaint_title),
                str(self.complaint_description)
            )
        )

        complaint_id = cursor.lastrowid

        conn.commit()
        conn.close()

        channel = interaction.guild.get_channel(
            COMPLAINTS_CHANNEL
        )

        embed = discord.Embed(
            title=f"⚠ Жалоба №{complaint_id}",
            color=MAIN_COLOR
        )

        embed.add_field(
            name="Автор",
            value=interaction.user.mention,
            inline=False
        )

        embed.add_field(
            name="Название",
            value=str(self.complaint_title),
            inline=False
        )

        embed.add_field(
            name="Описание",
            value=str(self.complaint_description),
            inline=False
        )

        embed.set_footer(
            text="Статус: Ожидает рассмотрения"
        )

        await channel.send(
            embed=embed
        )

        await interaction.response.send_message(
            "✅ Ваша жалоба успешно отправлена.",
            ephemeral=True
        )


class SuggestionModal(discord.ui.Modal, title="Предложить идею"):

    suggestion_title = discord.ui.TextInput(
        label="Название идеи",
        max_length=100
    )

    suggestion_description = discord.ui.TextInput(
        label="Описание идеи",
        style=discord.TextStyle.paragraph,
        max_length=2000
    )

    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

        conn = sqlite3.connect(DB_PATH)

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO suggestions
            (
                user_id,
                title,
                description
            )
            VALUES (?, ?, ?)
            """,
            (
                interaction.user.id,
                str(self.suggestion_title),
                str(self.suggestion_description)
            )
        )

        suggestion_id = cursor.lastrowid

        conn.commit()
        conn.close()

        channel = interaction.guild.get_channel(
            SUGGESTIONS_CHANNEL
        )

        embed = discord.Embed(
            title=f"💡 Идея №{suggestion_id}",
            color=MAIN_COLOR
        )

        embed.add_field(
            name="Автор",
            value=interaction.user.mention,
            inline=False
        )

        embed.add_field(
            name="Название",
            value=str(self.suggestion_title),
            inline=False
        )

        embed.add_field(
            name="Описание",
            value=str(self.suggestion_description),
            inline=False
        )

        embed.set_footer(
            text="Статус: Ожидает рассмотрения"
        )

        await channel.send(
            embed=embed
        )

        await interaction.response.send_message(
            "✅ Ваша идея успешно отправлена.",
            ephemeral=True
        )


class SupportView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Подать жалобу",
        emoji="⚠",
        style=discord.ButtonStyle.red,
        custom_id="support_complaint"
    )
    async def complaint_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await interaction.response.send_modal(
            ComplaintModal()
        )

    @discord.ui.button(
        label="Предложить идею",
        emoji="💡",
        style=discord.ButtonStyle.green,
        custom_id="support_suggestion"
    )
    async def suggestion_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await interaction.response.send_modal(
            SuggestionModal()
        )


class Support(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

        init_db()

        self.bot.add_view(
            SupportView()
        )

    @app_commands.command(
        name="supportpanel",
        description="Отправить панель поддержки"
    )
    async def supportpanel(
        self,
        interaction: discord.Interaction
    ):

        channel = interaction.guild.get_channel(
            SUPPORT_PANEL_CHANNEL
        )

        embed = discord.Embed(
            title="🛠 Поддержка сервера",
            description=(
                "Если вы хотите подать жалобу "
                "или предложить идею для сервера — "
                "воспользуйтесь кнопками ниже."
            ),
            color=MAIN_COLOR
        )

        await channel.send(
            embed=embed,
            view=SupportView()
        )

        await interaction.response.send_message(
            "✅ Панель поддержки отправлена.",
            ephemeral=True
        )


async def setup(bot):

    await bot.add_cog(
        Support(bot)
    )