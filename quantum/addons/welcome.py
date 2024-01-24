import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.event
async def on_member_join(member):
    channel_id = 1199288009003106405  # Replace with the actual channel ID
    channel = member.guild.get_channel(channel_id)

    if channel:
        welcome_message = f"Hello { member.mention }! Welcome to the server."
        arabic_message = f"مرحبة { member.mention }! .أهلاً بكم بشبكة خضر نت"

        await channel.send(f"```{ welcome_message }```")
        await channel.send(f"```{ arabic_message }```")
