import discord
from discord.ext import commands
import json
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_message(message):
    # Check if the message author is not a bot to avoid an infinite loop
    if message.author.bot:
        return

    # Check if the message content is "hi"

    help = ["help", "مساعدة"]
    if message.content.lower() in help:
        arabic_verify = f"إكتب اسعار لترى أسعار الإنترنيت"
        verify_message = f"type prices to view the internet prices"

        embed = discord.Embed(
            title="",
            description="",
            color=discord.Color.red(),
        )

        embed.add_field(name=verify_message, value="", inline=False)
        # embed.add_field(name=" ", value=" ", inline=True)
        embed.add_field(name=arabic_verify, value="", inline=False)
        await message.channel.send(embed=embed)

    #

    price = ["price", "أسعار"]
    if message.content.lower() in price:
        arabic_verify = f"الخدمة غير متوفرة حاليا"
        verify_message = f"service is currently unavailable"

        embed = discord.Embed(
            title="",
            description="",
            color=discord.Color.red(),
        )

        embed.add_field(name=verify_message, value="", inline=False)
        # embed.add_field(name=" ", value=" ", inline=True)
        embed.add_field(name=arabic_verify, value="", inline=False)
        await message.channel.send(embed=embed)


# on_member_join event
@bot.event
async def on_member_join(member):
    channel_id = 1199288009003106405
    channel = member.guild.get_channel(channel_id)

    if channel:
        welcome_message = f"Welcome to Khodor Net {member}"
        arabic_message = f"{member} أهلاً بكم بشبكة خضر نت"
        arabic_verify = f"الرجاء الإنتظار حتى يتم التفحص من حسابك"
        verify_message = f"Please wait till you get verified"

        embed = discord.Embed(
            title=welcome_message,
            description=arabic_message,
            color=discord.Color.gold(),  # You can set the color of the embed
        )

        # Add fields to the embed
        embed.add_field(name=verify_message, value="", inline=False)
        embed.add_field(name=" ", value=" ", inline=True)
        embed.add_field(name=arabic_verify, value="", inline=True)
        # embed.add_field(name="Field 2", value="Value 2", inline=True)
        # embed.add_field(name="Field 3", value="Value 3", inline=True)

        # await channel.send(f"{welcome_message}{arabic_message}")
        await channel.send(embed=embed)
        # await channel.send(f" {arabic_message}  ")


# Check if .kiwi file exists and read its content
if os.path.exists(".kiwi"):
    with open(".kiwi", "r", encoding="utf-8") as file:
        kiwi_content = file.read()
    bot.run(kiwi_content)
else:
    print("Error: The .kiwi file does not exist.")
