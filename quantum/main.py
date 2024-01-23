import discord
from discord.ext import commands
import json
import os

intents = discord.Intents.default()
intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)


# Load modules based on modules.json configuration
def load_modules():
    with open("modules.json", "r") as file:
        module_config = json.load(file)

    for filename in os.listdir("modules"):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            if module_name in module_config and module_config[module_name]:
                try:
                    bot.load_extension(f"modules.{module_name}")
                    print(f"Loaded module: {module_name}")
                except Exception as e:
                    print(f"Error loading module {module_name}: {e}")
            else:
                print(f"Module {module_name} is not enabled in modules.json")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    load_modules()


if __name__ == "__main__":
    # Run your bot with the token
    bot.run("MTE5OTMyNjYwNDM2Nzc2OTYzMA.GS8aPZ.pQLl0rjS29lZzyBANyZwnKwEy4Lf8MAZzkkDGk")
