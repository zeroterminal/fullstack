import discord
from discord.ext import commands
import json
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


def load_modules():
    with open("modules.json", "r") as file:
        modules_config = json.load(file)

    modules_folder = "./addons/"
    loaded_modules = []

    for module, enabled in modules_config.items():
        if enabled:
            try:
                bot.load_extension(f"{modules_folder}{module}")
                loaded_modules.append(module)
                print(f"Loaded module: {module}")
            except Exception as e:
                print(f"Error loading module {module}: {e}")

    return loaded_modules


async def on_ready():
    print(f'Logged in as {bot.user.name}')
    loaded_modules = load_modules()
    print(f'Loaded modules: {loaded_modules}')
    
with open(".kiwi", "r", encoding="utf-8") as file:
    kiwi_content = file.read()
bot.run(kiwi_content)
