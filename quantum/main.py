import discord
from discord.ext import commands
import json
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True  # Add this line to enable message content intent

bot = commands.Bot(command_prefix="!", intents=intents)

# Load modules
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

# Check if .kiwi file exists and read its content
if os.path.exists(".kiwi"):
    with open(".kiwi", "r", encoding="utf-8") as file:
        kiwi_content = file.read()
    bot.run(kiwi_content)
else:
    print("Error: The .kiwi file does not exist.")


# on_member_join event
@bot.event
async def on_member_join(member):
    channel_id = 1199288009003106405  # Replace with the actual channel ID
    channel = member.guild.get_channel(channel_id)

    if channel:
        welcome_message = f"Hello {member.mention}! Welcome to the server."
        arabic_message = f"مرحبة {member.mention}! .أهلاً بكم بشبكة خضر نت"

        await channel.send(f"```{welcome_message}```")
        await channel.send(f"```{arabic_message}```")


# Check if .kiwi file exists and read its content
if os.path.exists(".kiwi"):
    with open(".kiwi", "r", encoding="utf-8") as file:
        kiwi_content = file.read()
    bot.run(kiwi_content)
else:
    print("Error: The .kiwi file does not exist.")
