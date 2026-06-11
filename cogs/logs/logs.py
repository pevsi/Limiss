import discord
import asyncio

from discord.ext import commands

from config import LOGS
from utils.embeds import create_embed

from PIL import Image, ImageDraw
from io import BytesIO


class Logs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

# ==================================================
# ЛОГИРОВАНИЕ МОДЕРАЦИИ
# ==================================================

# ==================================================
# бан
# ==================================================
    @commands.Cog.listener()
    async def on_member_ban(
        self,
        guild,
        user
    ):

        channel = self.bot.get_channel(
            LOGS["moderation"]
        )

        if not channel:
            return

        moderator = "Неизвестно"

        try:

            await asyncio.sleep(2)

            async for entry in guild.audit_logs(
                limit=10,
                action=discord.AuditLogAction.ban
            ):

                if not entry.target:
                    continue

                if entry.target.id == user.id:

                    moderator = entry.user.mention
                    break

        except Exception as e:
            print(e)

        embed = create_embed(
            "🔨 Пользователь забанен"
        )

        embed.add_field(
            name="Пользователь",
            value=f"{user.mention} ({user.id})",
            inline=False
        )

        embed.add_field(
            name="Забанил",
            value=moderator,
            inline=False
        )

        await channel.send(embed=embed)

    # ==================================================
    # разбан
    # ==================================================
    @commands.Cog.listener()
    async def on_member_unban(
        self,
        guild,
        user
    ):

        channel = self.bot.get_channel(
            LOGS["moderation"]
        )

        if not channel:
            return

        moderator = "Неизвестно"

        try:

            await asyncio.sleep(2)

            async for entry in guild.audit_logs(
                limit=10,
                action=discord.AuditLogAction.unban
            ):

                if not entry.target:
                    continue

                if entry.target.id == user.id:

                    moderator = entry.user.mention
                    break

        except Exception as e:
            print(e)

        embed = create_embed(
            "🔓 Пользователь разбанен"
        )

        embed.add_field(
            name="Пользователь",
            value=f"{user} ({user.id})",
            inline=False
        )

        embed.add_field(
            name="Разбанил",
            value=moderator,
            inline=False
        )

        await channel.send(embed=embed)

    # ==================================================
    # кик
    # ==================================================
    @commands.Cog.listener()
    async def on_member_remove(
        self,
        member
    ):

        channel = self.bot.get_channel(
            LOGS["moderation"]
        )

        if not channel:
            return

        try:

            await asyncio.sleep(2)

            async for entry in member.guild.audit_logs(
                limit=10,
                action=discord.AuditLogAction.kick
            ):

                if not entry.target:
                    continue

                if entry.target.id != member.id:
                    continue

                diff = (
                    discord.utils.utcnow()
                    - entry.created_at
                ).total_seconds()

                if diff <= 10:

                    embed = create_embed(
                        "👢 Пользователь кикнут"
                    )

                    embed.set_thumbnail(
                        url=member.display_avatar.url
                    )

                    embed.add_field(
                        name="Пользователь",
                        value=member.mention,
                        inline=False
                    )

                    embed.add_field(
                        name="Кикнул",
                        value=entry.user.mention,
                        inline=False
                    )

                    await channel.send(embed=embed)
                    return

        except Exception as e:
            print(e)
    # ==================================================
    # МУТ / РАЗМУТ/РОЛИ
    # ==================================================
    @commands.Cog.listener()
    async def on_member_update(
        self,
        before,
        after
    ):

        moderation_channel = self.bot.get_channel(
            LOGS["moderation"]
        )

        if not moderation_channel:
            return

        # ==================================================
        # мут
        # ==================================================
        if (
            before.timed_out_until != after.timed_out_until
            and after.timed_out_until is not None
        ):

            moderator = "Неизвестно"

            try:

                await asyncio.sleep(2)

                async for entry in after.guild.audit_logs(
                    limit=10,
                    action=discord.AuditLogAction.member_update
                ):

                    if not entry.target:
                        continue

                    if entry.target.id != after.id:
                        continue

                    diff = (
                        discord.utils.utcnow()
                        - entry.created_at
                    ).total_seconds()

                    if diff <= 15:

                        moderator = entry.user.mention
                        break

            except Exception as e:
                print(e)

            embed = create_embed(
                "🔇 Пользователь замучен"
            )

            embed.set_thumbnail(
                url=after.display_avatar.url
            )

            embed.add_field(
                name="Пользователь",
                value=after.mention,
                inline=False
            )

            embed.add_field(
                name="Замутил",
                value=moderator,
                inline=False
            )

            embed.add_field(
                name="До",
                value=f"<t:{int(after.timed_out_until.timestamp())}:f>",
                inline=False
            )

            await moderation_channel.send(
                embed=embed
            )

        # ==================================================
        # размут
        # ==================================================
        if (
            before.timed_out_until is not None
            and after.timed_out_until is None
        ):

            moderator = "Неизвестно"

            try:

                await asyncio.sleep(2)

                async for entry in after.guild.audit_logs(
                    limit=10,
                    action=discord.AuditLogAction.member_update
                ):

                    if not entry.target:
                        continue

                    if entry.target.id != after.id:
                        continue

                    diff = (
                        discord.utils.utcnow()
                        - entry.created_at
                    ).total_seconds()

                    if diff <= 15:

                        moderator = entry.user.mention
                        break

            except Exception as e:
                print(e)

            embed = create_embed(
                "🔊 Пользователь размучен"
            )

            embed.set_thumbnail(
                url=after.display_avatar.url
            )

            embed.add_field(
                name="Пользователь",
                value=after.mention,
                inline=False
            )

            embed.add_field(
                name="Размутил",
                value=moderator,
                inline=False
            )

            await moderation_channel.send(
                embed=embed
            )

        # ==================================================
        # ВЫДАЧА / СНЯТИЕ РОЛЕЙ
        # ==================================================
        channel = self.bot.get_channel(
            LOGS["roles"]
        )

        if not channel:
            return

        added_roles = [
            role for role in after.roles
            if role not in before.roles
        ]

        removed_roles = [
            role for role in before.roles
            if role not in after.roles
        ]

        moderator = "Неизвестно"

        try:

            await asyncio.sleep(1)

            async for entry in after.guild.audit_logs(
                limit=5,
                action=discord.AuditLogAction.member_role_update
            ):

                if not entry.target:
                    continue

                if entry.target.id == after.id:
                    moderator = entry.user.mention
                    break

        except Exception as e:
            print(e)

        # ==================================================
        # ВЫДАЧА РОЛИ
        # ==================================================
        for role in added_roles:

            embed = create_embed(
                "➕ Роль выдана"
            )

            embed.set_thumbnail(
                url=after.display_avatar.url
            )

            embed.add_field(
                name="Пользователь",
                value=after.mention,
                inline=False
            )

            embed.add_field(
                name="Роль",
                value=role.mention,
                inline=False
            )

            embed.add_field(
                name="Выдал",
                value=moderator,
                inline=False
            )

            await channel.send(embed=embed)

        # ==================================================
        # СНЯТИЕ РОЛИ
        # ==================================================
        for role in removed_roles:

            embed = create_embed(
                "➖ Роль снята"
            )

            embed.set_thumbnail(
                url=after.display_avatar.url
            )

            embed.add_field(
                name="Пользователь",
                value=after.mention,
                inline=False
            )

            embed.add_field(
                name="Роль",
                value=role.mention,
                inline=False
            )

            embed.add_field(
                name="Снял",
                value=moderator,
                inline=False
            )

            await channel.send(embed=embed)

    # ==================================================
    # СОЗДАНИЕ РОЛЕЙ
    # ==================================================
    @commands.Cog.listener()
    async def on_guild_role_create(
        self,
        role
    ):

        channel = self.bot.get_channel(
            LOGS["roles"]
        )

        if not channel:
            return

        moderator = "Неизвестно"

        try:

            await asyncio.sleep(1)

            async for entry in role.guild.audit_logs(
                limit=5,
                action=discord.AuditLogAction.role_create
            ):

                if entry.target.id == role.id:
                    moderator = entry.user.mention
                    break

        except:
            pass

        embed = create_embed(
            "➕ Роль создана"
        )

        embed.add_field(
            name="Роль",
            value=role.mention,
            inline=False
        )

        embed.add_field(
            name="Создал",
            value=moderator,
            inline=False
        )

        await channel.send(embed=embed)

    # ==================================================
    # УДАЛЕНИЕ РОЛЕЙ
    # ==================================================
    @commands.Cog.listener()
    async def on_guild_role_delete(
        self,
        role
    ):

        channel = self.bot.get_channel(
            LOGS["roles"]
        )

        if not channel:
            return

        moderator = "Неизвестно"

        try:

            await asyncio.sleep(1)

            async for entry in role.guild.audit_logs(
                limit=5,
                action=discord.AuditLogAction.role_delete
            ):

                if entry.target.id == role.id:
                    moderator = entry.user.mention
                    break

        except:
            pass

        embed = create_embed(
            "🗑️ Роль удалена"
        )

        embed.add_field(
            name="Роль",
            value=role.name,
            inline=False
        )

        embed.add_field(
            name="Удалил",
            value=moderator,
            inline=False
        )

        await channel.send(embed=embed)
    # ==================================================
    # ИЗМЕНЕНИЕ РОЛЕЙ
    # ==================================================
    @commands.Cog.listener()
    async def on_guild_role_update(
        self,
        before,
        after
    ):

        channel = self.bot.get_channel(
            LOGS["roles"]
        )

        if not channel:
            return

        moderator = "Неизвестно"

        try:

            await asyncio.sleep(1)

            async for entry in after.guild.audit_logs(
                limit=5,
                action=discord.AuditLogAction.role_update
            ):

                if entry.target.id == after.id:
                    moderator = entry.user.mention
                    break

        except:
            pass

        # ==================================================
        # ИЗМЕНЕНИЕ НАЗВАНИЯ
        # ==================================================
        if before.name != after.name:

            embed = create_embed(
                "✏️ Название роли изменено"
            )

            embed.add_field(
                name="Роль",
                value=after.mention,
                inline=False
            )

            embed.add_field(
                name="Было",
                value=before.name,
                inline=True
            )

            embed.add_field(
                name="Стало",
                value=after.name,
                inline=True
            )

            embed.add_field(
                name="Изменил",
                value=moderator,
                inline=False
            )

            await channel.send(embed=embed)
        # ==================================================
        # ИЗМЕНЕНИЕ ПРАВ ролей
        # ==================================================
        before_perms = before.permissions
        after_perms = after.permissions

        changed_permissions = []

        for perm, value in before_perms:

            new_value = getattr(
                after_perms,
                perm
            )

            if value != new_value:

                status = (
                    "✅ Включено"
                    if new_value
                    else "❌ Выключено"
                )

                changed_permissions.append(
                    f"`{perm}` → {status}"
                )

        if changed_permissions:

            embed = create_embed(
                "🔐 Права роли изменены"
            )

            embed.add_field(
                name="Роль",
                value=after.mention,
                inline=False
            )

            embed.add_field(
                name="Изменил",
                value=moderator,
                inline=False
            )

            embed.add_field(
                name="Изменённые права",
                value="\n".join(
                    changed_permissions[:20]
                ),
                inline=False
            )

            await channel.send(embed=embed)


        # ==================================================
        # ИЗМЕНЕНИЕ ЦВЕТА
        # ==================================================
        if before.color != after.color:

            # Игнор если цвет реально не изменился
            if str(before.color) == str(after.color):
                return

            moderator = "Неизвестно"

            try:

                await asyncio.sleep(1)

                async for entry in after.guild.audit_logs(
                    limit=5,
                    action=discord.AuditLogAction.role_update
                ):

                    if not entry.target:
                        continue

                    if entry.target.id != after.id:
                        continue

                    diff = (
                        discord.utils.utcnow()
                        - entry.created_at
                    ).total_seconds()

                    if diff <= 5:
                        moderator = entry.user.mention
                        break

            except Exception as e:
                print(e)

            before_hex = str(before.color)
            after_hex = str(after.color)

            # ==================================================
            # КАРТИНКА OLD / NEW
            # ==================================================
            img = Image.new(
                "RGB",
                (160, 90),
                (35, 35, 35)
            )

            draw = ImageDraw.Draw(img)

            # OLD
            draw.rectangle(
                (0, 0, 80, 90),
                fill=before_hex
            )

            # NEW
            draw.rectangle(
                (80, 0, 160, 90),
                fill=after_hex
            )

            # Текст
            draw.text(
                (25, 35),
                "OLD",
                fill="white"
            )

            draw.text(
                (105, 35),
                "NEW",
                fill="white"
            )

            # ==================================================
            # BUFFER
            # ==================================================
            buffer = BytesIO()

            img.save(
                buffer,
                format="PNG"
            )

            buffer.seek(0)

            file = discord.File(
                buffer,
                filename="colors.png"
            )

            # ==================================================
            # EMBED
            # ==================================================
            embed = create_embed(
                "🎨 Цвет роли изменён"
            )

            embed.add_field(
                name="Роль",
                value=after.mention,
                inline=False
            )

            embed.add_field(
                name="Изменил",
                value=moderator,
                inline=False
            )

            embed.add_field(
                name="ID",
                value=str(after.id),
                inline=False
            )

            embed.add_field(
                name="Старый цвет",
                value=f"`{before_hex}`",
                inline=True
            )

            embed.add_field(
                name="Новый цвет",
                value=f"`{after_hex}`",
                inline=True
            )

            embed.set_image(
                url="attachment://colors.png"
            )

            await channel.send(
                embed=embed,
                file=file
            )

    # ==================================================
    # СОЗДАНИЕ КАНАЛОВ
    # ==================================================
    @commands.Cog.listener()
    async def on_guild_channel_create(
        self,
        channel_created
    ):

        channel = self.bot.get_channel(
            LOGS["channels"]
        )

        if not channel:
            return

        moderator = "Неизвестно"

        try:

            await asyncio.sleep(1)

            async for entry in channel_created.guild.audit_logs(
                limit=5,
                action=discord.AuditLogAction.channel_create
            ):

                if not entry.target:
                    continue

                if entry.target.id == channel_created.id:
                    moderator = entry.user.mention
                    break

        except Exception as e:
            print(e)

        embed = create_embed(
            "📁 Канал создан"
        )

        embed.add_field(
            name="Название",
            value=channel_created.mention,
            inline=False
        )

        embed.add_field(
            name="Создал",
            value=moderator,
            inline=False
        )

        await channel.send(embed=embed)

    # ==================================================
    # УДАЛЕНИЕ КАНАЛОВ
    # ==================================================
    @commands.Cog.listener()
    async def on_guild_channel_delete(
        self,
        channel_deleted
    ):

        channel = self.bot.get_channel(
            LOGS["channels"]
        )

        if not channel:
            return

        moderator = "Неизвестно"

        try:

            await asyncio.sleep(1)

            async for entry in channel_deleted.guild.audit_logs(
                limit=5,
                action=discord.AuditLogAction.channel_delete
            ):

                if not entry.target:
                    continue

                if entry.target.id == channel_deleted.id:
                    moderator = entry.user.mention
                    break

        except Exception as e:
            print(e)

        embed = create_embed(
            "🗑️ Канал удалён"
        )

        embed.add_field(
            name="Название",
            value=channel_deleted.name,
            inline=False
        )

        embed.add_field(
            name="Удалил",
            value=moderator,
            inline=False
        )

        await channel.send(embed=embed)

    # ==================================================
    # ИЗМЕНЕНИЕ КАНАЛОВ
    # ==================================================
    @commands.Cog.listener()
    async def on_guild_channel_update(
        self,
        before,
        after
    ):

        channel = self.bot.get_channel(
            LOGS["channels"]
        )

        if not channel:
            return

        moderator = "Неизвестно"

        try:

            await asyncio.sleep(1)

            async for entry in after.guild.audit_logs(
                limit=5,
                action=discord.AuditLogAction.channel_update
            ):

                if not entry.target:
                    continue

                if entry.target.id == after.id:

                    diff = (
                        discord.utils.utcnow()
                        - entry.created_at
                    ).total_seconds()

                    if diff <= 5:
                        moderator = entry.user.mention
                        break

        except Exception as e:
            print(e)

        # ==================================================
        # ИЗМЕНЕНИЕ НАЗВАНИЯ
        # ==================================================
        if before.name != after.name:

            embed = create_embed(
                "✏️ Канал изменён"
            )

            embed.add_field(
                name="Изменил",
                value=moderator,
                inline=False
            )

            embed.add_field(
                name="Было",
                value=before.name,
                inline=False
            )

            embed.add_field(
                name="Стало",
                value=after.name,
                inline=False
            )

            await channel.send(embed=embed)

        # ==================================================
        # ИЗМЕНЕНИЕ БИТРЕЙТА
        # ==================================================
        if isinstance(
            before,
            discord.VoiceChannel
        ):

            if before.bitrate != after.bitrate:

                embed = create_embed(
                    "🎵 Изменён битрейт"
                )

                embed.add_field(
                    name="Канал",
                    value=after.mention,
                    inline=False
                )

                embed.add_field(
                    name="Изменил",
                    value=moderator,
                    inline=False
                )

                embed.add_field(
                    name="Было",
                    value=str(before.bitrate),
                    inline=False
                )

                embed.add_field(
                    name="Стало",
                    value=str(after.bitrate),
                    inline=False
                )

                await channel.send(embed=embed)

        # ==================================================
        # ИЗМЕНЕНИЕ ЛИМИТА
        # ==================================================
        if isinstance(
            before,
            discord.VoiceChannel
        ):

            if before.user_limit != after.user_limit:

                embed = create_embed(
                    "👥 Лимит пользователей изменён"
                )

                embed.add_field(
                    name="Канал",
                    value=after.mention,
                    inline=False
                )

                embed.add_field(
                    name="Изменил",
                    value=moderator,
                    inline=False
                )

                embed.add_field(
                    name="Было",
                    value=str(before.user_limit),
                    inline=False
                )

                embed.add_field(
                    name="Стало",
                    value=str(after.user_limit),
                    inline=False
                )

                await channel.send(embed=embed)

        # ==================================================
        # ИЗМЕНЕНИЕ РЕГИОНА
        # ==================================================
        if isinstance(
            before,
            discord.VoiceChannel
        ):

            if before.rtc_region != after.rtc_region:

                embed = create_embed(
                    "🌍 Регион канала изменён"
                )

                embed.add_field(
                    name="Канал",
                    value=after.mention,
                    inline=False
                )

                embed.add_field(
                    name="Изменил",
                    value=moderator,
                    inline=False
                )

                embed.add_field(
                    name="Было",
                    value=str(before.rtc_region),
                    inline=False
                )

                embed.add_field(
                    name="Стало",
                    value=str(after.rtc_region),
                    inline=False
                )

                await channel.send(embed=embed)

        # ==================================================
        # ИЗМЕНЕНИЕ ПРАВ КАНАЛА
        # ==================================================
        changed_permissions = []

        all_targets = set(
            before.overwrites.keys()
        ) | set(
            after.overwrites.keys()
        )

        for target in all_targets:

            before_overwrite = before.overwrites_for(
                target
            )

            after_overwrite = after.overwrites_for(
                target
            )

            for permission in discord.Permissions.VALID_FLAGS:

                before_value = getattr(
                    before_overwrite,
                    permission
                )

                after_value = getattr(
                    after_overwrite,
                    permission
                )

                if before_value != after_value:

                    if after_value is True:
                        status = "✅"

                    elif after_value is False:
                        status = "❌"

                    else:
                        status = "➖"

                    changed_permissions.append(
                        f"{status} `{permission}` — {target.mention}"
                    )

        if changed_permissions:

            moderator = "Неизвестно"

            try:

                # Discord создаёт audit log с задержкой
                await asyncio.sleep(3)

                # Берём САМЫЙ ПОСЛЕДНИЙ channel_update
                entry = await after.guild.audit_logs(
                    limit=1,
                    action=discord.AuditLogAction.channel_update
                ).get()

                if entry:

                    diff = (
                        discord.utils.utcnow()
                        - entry.created_at
                    ).total_seconds()

                    # Если лог свежий
                    if diff <= 20:

                        moderator = entry.user.mention

            except Exception as e:
                print(e)

            embed = create_embed(
                "🔐 Права канала изменены"
            )

            embed.add_field(
                name="Канал",
                value=after.mention,
                inline=False
            )

            embed.add_field(
                name="Изменил",
                value=moderator,
                inline=False
            )

            embed.add_field(
                name="Изменения",
                value="\n".join(
                    changed_permissions[:20]
                ),
                inline=False
            )

            await channel.send(embed=embed)

    # ==================================================
    # ЛОГИРОВАНИЕ АКТИВНОСТЕЙ
    # ==================================================

    # ==================================================
    # УДАЛЕНИЕ СООБЩЕНИЙ
    # ==================================================
    @commands.Cog.listener()
    async def on_message_delete(self, message):

        if message.author.bot:
            return

        channel = self.bot.get_channel(LOGS["messages"])

        if not channel:
            return

        embed = create_embed("🗑️ Сообщение удалено")

        embed.set_thumbnail(
            url=message.author.display_avatar.url
        )

        embed.add_field(
            name="Пользователь",
            value=message.author.mention,
            inline=False
        )

        embed.add_field(
            name="Канал",
            value=message.channel.mention,
            inline=False
        )

        embed.add_field(
            name="Сообщение",
            value=message.content or "Нет текста",
            inline=False
        )

        if message.attachments:

            attachment = message.attachments[0]

            if (
                attachment.content_type
                and attachment.content_type.startswith("image")
            ):

                embed.set_image(
                    url=attachment.url
                )

            embed.add_field(
                name="Файл",
                value=attachment.filename,
                inline=False
            )

        await channel.send(embed=embed)

    # ==================================================
    # ИЗМЕНЕНИЕ СООБЩЕНИЙ
    # ==================================================
    @commands.Cog.listener()
    async def on_message_edit(
        self,
        before,
        after
    ):

        if before.author.bot:
            return

        if before.content == after.content:
            return

        channel = self.bot.get_channel(
            LOGS["messages"]
        )

        if not channel:
            return

        embed = create_embed(
            "✏️ Сообщение изменено"
        )

        embed.set_thumbnail(
            url=after.author.display_avatar.url
        )

        embed.add_field(
            name="Пользователь",
            value=after.author.mention,
            inline=False
        )

        embed.add_field(
            name="Канал",
            value=after.channel.mention,
            inline=False
        )

        embed.add_field(
            name="Было",
            value=before.content or "Нет текста",
            inline=False
        )

        embed.add_field(
            name="Стало",
            value=after.content or "Нет текста",
            inline=False
        )

        if after.attachments:

            attachment = after.attachments[0]

            if (
                attachment.content_type
                and attachment.content_type.startswith("image")
            ):

                embed.set_image(
                    url=attachment.url
                )

            embed.add_field(
                name="Файл",
                value=attachment.filename,
                inline=False
            )

        await channel.send(
            embed=embed
        )

    # ==================================================
    # ВХОД НА СЕРВЕР
    # ==================================================
    @commands.Cog.listener()
    async def on_member_join(self, member):

        channel = self.bot.get_channel(LOGS["joins"])

        if not channel:
            return

        embed = create_embed("📥 Пользователь вошёл")

        embed.set_thumbnail(
            url=member.display_avatar.url
        )

        embed.add_field(
            name="Пользователь",
            value=member.mention,
            inline=False
        )

        await channel.send(embed=embed)

    # ==================================================
    # ВЫХОД С СЕРВЕРА
    # ==================================================
    @commands.Cog.listener()
    async def on_member_remove(self, member):

        channel = self.bot.get_channel(LOGS["joins"])

        if not channel:
            return

        embed = create_embed("📤 Пользователь вышел")

        embed.set_thumbnail(
            url=member.display_avatar.url
        )

        embed.add_field(
            name="Пользователь",
            value=member.mention,
            inline=False
        )

        await channel.send(embed=embed)

    # =========================
    # ВОЙС ЛОГИ
    # =========================
    @commands.Cog.listener()
    async def on_voice_state_update(
        self,
        member,
        before,
        after
    ):

        log_channel = self.bot.get_channel(
            LOGS["voice"]
        )

        if not log_channel:
            return

        # Игнор mute/deafen
        if before.channel == after.channel:
            return

        # =========================
        # ПОДКЛЮЧЕНИЕ
        # =========================
        if before.channel is None and after.channel is not None:

            embed = create_embed(
                "🔊 Пользователь подключился"
            )

            embed.set_thumbnail(
                url=member.display_avatar.url
            )

            embed.add_field(
                name="Пользователь",
                value=member.mention,
                inline=False
            )

            embed.add_field(
                name="Канал",
                value=after.channel.mention,
                inline=False
            )

            await log_channel.send(embed=embed)
            return

        # =========================
        # ОТКЛЮЧЕНИЕ
        # =========================
        if before.channel is not None and after.channel is None:

            disconnected_by = None

            try:

                await asyncio.sleep(2)

                async for entry in member.guild.audit_logs(
                    limit=10
                ):

                    if entry.action != discord.AuditLogAction.member_disconnect:
                        continue

                    diff = (
                        discord.utils.utcnow()
                        - entry.created_at
                    ).total_seconds()

                    if diff > 15:
                        continue

                    # Discord может не дать target
                    if entry.target is None:
                        disconnected_by = entry.user
                        break

                    if entry.target.id == member.id:
                        disconnected_by = entry.user
                        break

            except Exception as e:
                print(e)

            # Отключил модератор
            if disconnected_by:

                embed = create_embed(
                    "❌ Пользователь отключён"
                )

                embed.add_field(
                    name="Пользователь",
                    value=member.mention,
                    inline=False
                )

                embed.add_field(
                    name="Отключил",
                    value=disconnected_by.mention,
                    inline=False
                )

            # Сам вышел
            else:

                embed = create_embed(
                    "🔇 Пользователь вышел"
                )

                embed.add_field(
                    name="Пользователь",
                    value=member.mention,
                    inline=False
                )

            embed.set_thumbnail(
                url=member.display_avatar.url
            )

            embed.add_field(
                name="Канал",
                value=before.channel.mention,
                inline=False
            )

            await log_channel.send(embed=embed)
            return

        # =========================
        # ПЕРЕХОД / ПЕРЕНОС
        # =========================
        if before.channel != after.channel:

            moved_by = None

            try:

                await asyncio.sleep(2)

                async for entry in member.guild.audit_logs(
                    limit=10
                ):

                    if entry.action != discord.AuditLogAction.member_move:
                        continue

                    diff = (
                        discord.utils.utcnow()
                        - entry.created_at
                    ).total_seconds()

                    if diff > 15:
                        continue

                    # Discord иногда не даёт target
                    if entry.target is None:
                        moved_by = entry.user
                        break

                    if entry.target.id == member.id:
                        moved_by = entry.user
                        break

            except Exception as e:
                print(e)

            # Перенёс модератор
            if moved_by:

                embed = create_embed(
                    "📦 Пользователь перемещён"
                )

                embed.add_field(
                    name="Пользователь",
                    value=member.mention,
                    inline=False
                )

                embed.add_field(
                    name="Переместил",
                    value=moved_by.mention,
                    inline=False
                )

            # Сам перешёл
            else:

                embed = create_embed(
                    "🔁 Пользователь перешёл"
                )

                embed.add_field(
                    name="Пользователь",
                    value=member.mention,
                    inline=False
                )

            embed.set_thumbnail(
                url=member.display_avatar.url
            )

            embed.add_field(
                name="Из канала",
                value=before.channel.mention,
                inline=False
            )

            embed.add_field(
                name="В канал",
                value=after.channel.mention,
                inline=False
            )

            await log_channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Logs(bot))