import discord
import os

from discord.ext import commands
from dotenv import load_dotenv





# Загружаем .env
load_dotenv()

TOKEN = os.getenv("TOKEN")

# Интенты
intents = discord.Intents.all()


class MyBot(commands.Bot):

    def __init__(self):

        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=None
        )

    async def setup_hook(self):

        # Автозагрузка cog'ов
        for folder in os.listdir("./cogs"):

            # Пропускаем системные папки
            if folder.startswith("__"):
                continue

            folder_path = f"./cogs/{folder}"

            # Пропускаем файлы
            if not os.path.isdir(folder_path):
                continue

            for file in os.listdir(folder_path):

                if file.endswith(".py") and file != "__init__.py":

                    extension = f"cogs.{folder}.{file[:-3]}"

                    try:

                        await self.load_extension(extension)

                        print(
                            f"✅ Модуль {extension} загружен"
                        )

                    except Exception as e:

                        print(
                            f"❌ Не удалось загрузить {extension}: {e}"
                        )

        # Синхронизация slash-команд
        await self.tree.sync()

        print("📊 Слеш-команды синхронизированы")

    async def on_ready(self):

        print(f"🚀 Бот запущен как {self.user}")

        await self.change_presence(
            activity=discord.Game(
                name="Limiss System"
            )
        )


bot = MyBot()


if __name__ == "__main__":
    bot.run(TOKEN)